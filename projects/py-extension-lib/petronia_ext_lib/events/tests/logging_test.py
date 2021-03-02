# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-01T15:28:56.999511+00:00

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
            '$': 'ϰƮ0țƬgӇˀӫ҆=/¬ȒSπȻͳӞϱĐȎÔҺŬ&ϐɍϒç',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7244870193249669034,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 304586.03260651807,
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
            '$': '20210301:152856.880685:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ȱ͵ǠѳԪǟ˛ƶб˱ǢɭŃȪԫŒ҄ͱRҲ\x9aӿ{ȜӞǙȏƛ\x8eĖ',
                'ӏӣϯVʟșĳνʮˠ>ǞƊУ˝оȬ҈i¨˪ǣԑWčАəÞњť',
                "țήǃɣ^ľȢʄµŭѴɎĪʖγϷɀƺϸBǜéԛʛʾǔӦҶ'Ł",
                'η\xadГƏϹиĆǤϬԃ˖ơʿ˽QʬΰϴЍϏÂƃ]ʗùÖǀɂ`Ҳ',
                'oŻƻЛг˧ЭΆNŗфģȷҟԦ1Ԛ˕ȽφͺҤʌҹŉĘçƳwӯ',
                'ʣîҿĵǩAΊзΨpҧԓ\x8aǦ˕Ğѽєȹƹï*ϏɶÅÕš\xadŶҫ',
                '˟ŪuӉē§\x9cǎφHžЊĄòɳĢɔϾʆɱҌѿЦķӴӮɠľ¶ǧ',
                'ӦœѥȆŌ«ģˬӦү,ˢǛ8ʱӧɒ°ӞǼÝÒөюɕű¯ϜĐ˙',
                'ƨƩέƹšΞϵҒρӘȭɡˢWǷТӝԥԔҫ\u0381țҌ˪ϫäΗʘǆǙ',
                'ҴǝгŲɦ*ÕĻѧĞ{άɣτҶǧǫǶАÙǮѣ(sщΤͻŘҡî',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8059451240027346929,
                2120798027627357181,
                8693471613550300502,
                4484321287253789737,
                -9134003618278858503,
                3791786206350546074,
                2409160795823129457,
                -2242962581449626220,
                523622101396944893,
                -7801916758431370316,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                910738.4820264092,
                -20797.421759075092,
                430971.5618006465,
                114251.68609291184,
                369789.2316131103,
                683066.7045794607,
                715281.6633182722,
                701526.596454063,
                736885.2322829737,
                981426.4579650206,
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
                True,
                True,
                False,
                True,
                False,
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
                '20210301:152856.881684:+0000',
                '20210301:152856.881699:+0000',
                '20210301:152856.881709:+0000',
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
            'name': 'π(¬ġːüҸřȮ˹ȟҴĬȣǳѐҐċϤ',
            'value': {
                '^': 'int_list',
                '$': [
                    -575720037352919540,
                    -4526031437359984746,
                    8684838195455915990,
                    -1019237724206026141,
                    -6913232714776832162,
                    2307094715068614582,
                    -9058120156569736570,
                    8221577532699693953,
                    7132539684750743503,
                    5890374905874055933,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '¯',

            'value': {
                '^': 'float',
                '$': 477328.94341622246,
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
            'catalog': 'ǴǾßˬϓʀ\u0383eŚ¹1ͱҸ¨\x9fʊ\x8bӻҥ˴ǙƄ\x9eфŸйèosƍ',
            'message': 'ΠĬ\x84Ċ:ҘƵӷĔǯ¼΅ѕɊ˫ʃРϗĎb\u0381҉ȊʩăϼĽŦňȳ',
            'arguments': [
                {
                    'name': 'όʬ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ǀňэͶȢÔɲâЙήķ\u038bp˝ʝɧƒəñυͱ˩\x95˕ǂѩνЮѣȿ',
                                        '§˦\x82ȰԋŔEϜĜҐļ\x8f\u0382ЮйȺ+Ŭƃń6ʾȣDP\x91ҩɧҗϧ',
                                        'ģƖȁþɟѦ\\Ҳć¤Ҹ\x89˯Żǫæ\u0380pӥȃː˽Ȩˣɪ˓ӼǾӖͷ',
                                        'ÔɪϽяľхÎкѠ\u0381ςәŘ\x8aӲŨѨͽԥӹНӀıǠÈυǪҶʱɆ',
                                        'ΐɡ˄ŃԀӷȖ\u0378ʦãԧËʟĶ{®ɊŠķǲԀˇϔéȣЫϻǶˆǬ',
                                        'üЏ¥ĢһüʌșǏƁƀƫиĦÚЅƁőŐǠŉʫŎ"Ǵ4҈ΫŪΗ',
                                        '˫\x90ʘ§МbĢǤɩĂҜČΊӊǬ˻Ǻ˕&ϱϵѲύńČHрΐ4ϰ',
                                        'ȗТͺNѽȁ˶ΫwɢįЈƈĴƘѦĕʛфǝǸҪõ`HǻơĆοə',
                                        'ƾɾ\x9aäʦцȀΜ˖ΜӜϾзĴĜeЗ˴ґа\u038bŔǯкǊѷӲǁ\x8cş',
                                        'Ҏ\u0382ϩȖСλϰѰnĚͽɟќ˩ӦϴŻуī˹ƽeтŖş!ƌ¨ϻɋ',
                                    ],
                        },
                },
                {
                    'name': 'Έȇɮɻ_ǄǪϮTҡҋEśѷȕǡǐƄɁԄΕκѝŴ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        299721.297938511,
                                        398090.3416501172,
                                        6169.547203594731,
                                        758810.7302106472,
                                        352407.1095732936,
                                        961615.299422805,
                                        142567.9508769169,
                                        654519.9627260434,
                                    ],
                        },
                },
                {
                    'name': 'ӺξƵιԟѣǙİȌȴȔĜȸ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210301:152856.878428:+0000',
                                        '20210301:152856.878443:+0000',
                                        '20210301:152856.878451:+0000',
                                        '20210301:152856.878458:+0000',
                                        '20210301:152856.878465:+0000',
                                        '20210301:152856.878471:+0000',
                                        '20210301:152856.878477:+0000',
                                        '20210301:152856.878484:+0000',
                                        '20210301:152856.878490:+0000',
                                        '20210301:152856.878496:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ȦʤБʷʊŅϰΦɩĶӋԏϋԆˆi˘ĻҥǏˤлŃщԉӋāŬ6ū',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        777523.2856458898,
                                        591014.8630695533,
                                        813939.0125901317,
                                        42236.19166075118,
                                        414860.38464291574,
                                        297725.0346269606,
                                        127531.80464711107,
                                        576902.3433959624,
                                        540740.2597364362,
                                        989132.9204092012,
                                    ],
                        },
                },
                {
                    'name': 'ƱËːɢϸģƒŖÞ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        193823.47168932267,
                                        9478.560008089815,
                                        349577.72028480814,
                                        361339.1775796134,
                                        83353.83249100344,
                                        778842.6656902595,
                                        39809.97256636532,
                                        36171.878822238825,
                                        -9275.53540822219,
                                        643122.2860887958,
                                    ],
                        },
                },
                {
                    'name': 'Ȭɒȱȳȃґ˸ƉǏ˲ӎϤƄ\x93\x9dОXSЁӬ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ɹҽaƦ)ȋǸƨ\x87ɱҟǾʙԭ˄еĐƢ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210301:152856.879367:+0000',
                        },
                },
                {
                    'name': 'hǏĢд§\x86ɂŎηоӂŭȈϮǜт¨¿ҷψyʖűƎĳɯʫӇΒɖ',
                    'value': {
                            '^': 'float',
                            '$': 256165.69351702143,
                        },
                },
                {
                    'name': 'ƺ\x8cƴμӋŬЛˎΩ¡Nφǘ£ͱĲų®ӧȧ˧ȟ',
                    'value': {
                            '^': 'float',
                            '$': 947462.7293274867,
                        },
                },
                {
                    'name': 'рĮɴşϴ\x80ˏҸԔ҄¹ŭûţ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        892562.387407195,
                                        219148.61631867161,
                                        988627.6069356233,
                                        873287.6706564307,
                                        55279.32553369511,
                                        985873.4147106162,
                                        992998.77520293,
                                        546295.0474890951,
                                        771950.3923886335,
                                        951332.4604537927,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ưъ',

            'message': 'ǹ',

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
            'scope': 'warning',
            'messages': [
                {
                    'catalog': 'ʙӠ\x99Ɖ˸ŧҴ\x96Ȉȏƾ@Ɛū˳\\ƋӉȚԄvӫΌƆEуı϶ʉˢ',
                    'message': 'ŃʍħMΨżǭЅůƄҪŐԗτĪǘòȬΦjɃWǙŘɏʡѦԜƺӞ',
                    'arguments': [
                            {
                                        'name': '͵ϑ¼ѧëҳ\x85ϝuқƳɆà.ĎȊ¹ȦnʳѓrΐиК҆Ϳгԝď',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.844700:+0000',
                                                                            '20210301:152856.844736:+0000',
                                                                            '20210301:152856.844746:+0000',
                                                                            '20210301:152856.844754:+0000',
                                                                            '20210301:152856.844760:+0000',
                                                                            '20210301:152856.844767:+0000',
                                                                            '20210301:152856.844773:+0000',
                                                                            '20210301:152856.844779:+0000',
                                                                            '20210301:152856.844786:+0000',
                                                                            '20210301:152856.844792:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ќԓяΈ\x9fǎԫŌљɅUɞĭ\x91ˏʻ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ь©ψ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            301976.9928318286,
                                                                            940992.5121527686,
                                                                            638117.5286626971,
                                                                            707885.5609648373,
                                                                            209854.72475401778,
                                                                            878258.9166490113,
                                                                            -35827.24346612194,
                                                                            771125.2142496967,
                                                                            795292.7344506952,
                                                                            404557.83185825305,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8aȥȾъŋʖҵʹ\x98Ž¥îÝҺԀϢȉćÖƙРąўϠΕƘўðϲ¡',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˗ɘǁȼԥŀ˳c+$҃lԐźҌҝΪ˶Ўрқ\x87ϙӾȾǞɣʉ\x9dë',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʯϫʮŊǑºʩÛĮƏЛǺ¼Ò_ƶӛƃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2284865836292098825,
                                                    },
                                    },
                            {
                                        'name': 'ѳʮѷ\x8aɏȷьƠИӁѣwõʬĵrƮǓȱŉƽwɗҿɀҮ[ԚӔƅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.859951:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ư\x96ƼŌăɿҕчø˕ÈҤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.860125:+0000',
                                                                            '20210301:152856.860139:+0000',
                                                                            '20210301:152856.860147:+0000',
                                                                            '20210301:152856.860153:+0000',
                                                                            '20210301:152856.860159:+0000',
                                                                            '20210301:152856.860165:+0000',
                                                                            '20210301:152856.860172:+0000',
                                                                            '20210301:152856.860178:+0000',
                                                                            '20210301:152856.860184:+0000',
                                                                            '20210301:152856.860190:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x98',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.860423:+0000',
                                                                            '20210301:152856.860437:+0000',
                                                                            '20210301:152856.860445:+0000',
                                                                            '20210301:152856.860451:+0000',
                                                                            '20210301:152856.860458:+0000',
                                                                            '20210301:152856.860464:+0000',
                                                                            '20210301:152856.860470:+0000',
                                                                            '20210301:152856.860476:+0000',
                                                                            '20210301:152856.860482:+0000',
                                                                            '20210301:152856.860489:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӝC΅Ԧɶ\x9eшǋɾÔƹǓǯ\x9f˰ÏǬĸ\x8bŅ\u038bŮʈ¦eʄˈýƑƴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.860727:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŞЇƐƜΠҎZɮɃ΄ÚԦԄȫ\u038dǫѡӴϺ¨ÐдэɥԙΓaŉυʐ',
                    'message': 'l΅ɊǱѢȊϡŞеȻÿɌǍЏŋҤϱɡʋџϊǗˮΤƟǠγʤдϝ',
                    'arguments': [
                            {
                                        'name': 'ȁΣϹАѿȖż©5Ԯʋǝʸϲtŏ΄ҨʸѷĭӲŮŞϻq',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'İӿC\u038bɎɄǚωƗĖ¸Ԁǲɀԝсƺ˱ȴƳřЏʿӝ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ňťìΣɕҔʠ͵лƊŜɈʳӠw',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.861734:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u038dӕыȴƻ˯˾Ӈ˺Ǿƨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ԇɦɢʏǜ˺ɄEԮƗҙʊäΚǈ˛±Ωĥ\x95ӷùІǴťԩVҔɠҙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ңǃ(њMψȹϹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            572705.6548427532,
                                                                            315846.53854100814,
                                                                            61762.807162528625,
                                                                            409433.1804014347,
                                                                            693155.1513933003,
                                                                            351947.7899270319,
                                                                            -24971.686863272873,
                                                                            529052.8938345152,
                                                                            437540.3109236108,
                                                                            286053.3301097413,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӰχҸȅ§ȄŴԑϽӍǺҸİͺɠåʼѮʇɱ}aњӤҧ҆ͰʏѺӨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8858813549670809725,
                                                    },
                                    },
                            {
                                        'name': 'ΔXȅŒţƂwϛŶĨɿөӣϛǋΡ\x97\x8fɱѫӵ҇ȭҔȪéдíƷƻ',
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
                                        'name': 'ŴЮ˅ŤҭԗΥѓĪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĥȱǾӺȹГʷČХȷҲÿёȘЕȋȠƥǍźҏΧõӌȇr',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 529927.6361327042,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƹPïȠӏ>ϣ\x81hÀïӓ±żñɷƒʺʢԤ!ӭʌǂȑ',
                    'message': 'ѮLζȗϚҩεԇĝʤҔ<ƫәɈРҬÑΪжÑΐѳ;ɵVƴ˽ȧʃ',
                    'arguments': [
                            {
                                        'name': 'рѝЮѭϳuȗŨˮǦ[ƤʄΉɚʯʒʀ\x82ɨѣ\x83ʅϩʡïΜҨЌ˓',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĚΏtǾĳčİϳŊĨӞȞӝԄȆǼ-˕ӭȡ\x88˗ȐǩЉŐƄźϠý',
                                                    },
                                    },
                            {
                                        'name': 'ӅгƁ¶ˎӁʸϲп§ó#ǜzԠΆǲʷ\x99(ȋ˜ЪȼХċ\x9f31О',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ұҌΓ\x9cҟѲϥт3\x99ĕőˏ˥ɸƱjơȝʡЁӊȼΞ˧Ēԙʘʒȓ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.863969:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Əʹp',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            156027.3107629166,
                                                                            387154.14143786946,
                                                                            -46685.44026252455,
                                                                            619109.0285280695,
                                                                            455561.1293954315,
                                                                            -11350.978119334191,
                                                                            -67820.61245442923,
                                                                            717593.7486988059,
                                                                            22835.438892123144,
                                                                            924704.476719542,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԏ5',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 479595.11752355145,
                                                    },
                                    },
                            {
                                        'name': 'һɄ\x95ÑqɧҘ*ΪÈʁѬϐҎ˽\x94ȫƢoϿǟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÊĶӐʋ\x96ȸŹӞҶâӧŤťϰΚÆħpѠ˗ѼɝǴ˕Ԃ\u0380ÑǱʤş',
                                                    },
                                    },
                            {
                                        'name': 'ŖԆÏΧWɩ\x91ЅȇІǗþĒĺǘӬʽŐ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƠҷΰʦгāэҗР!ˌΆãeHӱЯԇƾʟƖˤΠҺȣόƏßÔȈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7835977554180480224,
                                                    },
                                    },
                            {
                                        'name': 'ҔнȤԚƂƋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.865018:+0000',
                                                                            '20210301:152856.865033:+0000',
                                                                            '20210301:152856.865041:+0000',
                                                                            '20210301:152856.865047:+0000',
                                                                            '20210301:152856.865054:+0000',
                                                                            '20210301:152856.865129:+0000',
                                                                            '20210301:152856.865146:+0000',
                                                                            '20210301:152856.865155:+0000',
                                                                            '20210301:152856.865163:+0000',
                                                                            '20210301:152856.865170:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Χϣȡř\x8e\x9dȫǿėҦəŻƏśŴ\x81ʈMëʹ˚ѡϵ"˭ǝ$s8ȋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'H΅ϐ^ғӤϭͱƈƺΑԞȼѾÈ˲owǩ͵ѪßNҘЯωàÄӚ:',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϟBƹŌβνǡҗƯ©ǌƙʫºǠфɑͲΓ҅ɩoŶwRӕǞϷɕΚ',
                    'message': 'ĂƼǀɓҥӊӵҙϚɺGϏϴřçƘϥβ)Ͷ˵яϟʠɾʯЭȹAé',
                    'arguments': [
                            {
                                        'name': 'ҪѫӣҿĕȄ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.865911:+0000',
                                                    },
                                    },
                            {
                                        'name': 'úΠ˾ȚFǩşԅɡМҶпƄŢşеѧ÷Ξ˦џ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.866080:+0000',
                                                                            '20210301:152856.866093:+0000',
                                                                            '20210301:152856.866101:+0000',
                                                                            '20210301:152856.866107:+0000',
                                                                            '20210301:152856.866113:+0000',
                                                                            '20210301:152856.866120:+0000',
                                                                            '20210301:152856.866126:+0000',
                                                                            '20210301:152856.866132:+0000',
                                                                            '20210301:152856.866138:+0000',
                                                                            '20210301:152856.866144:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʗ˰ӳ0ϢνȨÞɎǖέοʷҊȬKΨɮΗϩʆȾƣɎθɐιԮęҢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԀĮÉϣЭӳ1ƥèӱӨϟ˽rЉӖͲ\x8fȎƉόÊɄǡ\x92ΕƸӇñϞ',
                                                                            'ˇžƿиѪӇʀнˡʋӶμâјӋдáɛӺӥĵҩơÛѻTòłӥȯ',
                                                                            'ĢԜїыӘ¬Ў˶ӬΕļ˂ÔøğͰ}ßǦЧǵŵӶɆгέԈBǣʙ',
                                                                            'ɫԒ˾ˣ\x99ǥƀǢȼҁY\x9ddǈԑԆǧ\u038dŔȋϺΫ\x82оΪɑӿӥʪ˭',
                                                                            'ҕѽËǜˍ\u0381ǂϷfϻϗȜ®ʓȖѴĳύШɣԃ\x9fȎ˂Ѥďιƙ˔\x88',
                                                                            '1ęńüʯĲă˻Ǖˉʹςĸɑŝ\u03a2åӥōөϮěѝ?ԣƎұѥƊȓ',
                                                                            'ΥýѸ+ӄӎʾ0ǞӭϠϩĄѧͺŀӭʠњǐƏKʳИӃʭɡ΅ҧǦ',
                                                                            'ғ,ΰӼӳϞý˲ęҖƩʳšʺÝԦȚӔӧČHÎώƃǹ\x86ÚЌ«Н',
                                                                            'Ԙ˵VɨƆǓ\x86ƦНüȽĉ§ºʴѽЅҒ˨úʷ¹ŘНŀɈMƯФЋ',
                                                                            'åʴҾ¢ҜƋǽȢˤǢÐҩɒ¾ɚƻӈ҄ӿ˽0Ɵҕ|ɵΜõ˾ʺІ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӡːɔǫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8434974638468990864,
                                                                            3208207894469170986,
                                                                            -7797941373982385464,
                                                                            7975223757627434476,
                                                                            -6920140406429424014,
                                                                            -1753972193731920480,
                                                                            6324726806788351764,
                                                                            3537696521934728555,
                                                                            -2274542599881990696,
                                                                            -6629904109152220917,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ПƯƪу˵ΨýΨӴѺʍεȲĮĪϑǋÔɖϸÒ҂ӢɈԃƴӡɹԮͲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ĩ҅ĘӗъɔUǳʆʜÌŋҩ΅ʵřQ\x8aŖǎœīψ\x8fʕÝӋ(@\x80',
                                                                            '˝ăоǠӅлʨИ˅]ʩɀǱbԉÞˋǁϬʿFΑ˚Hǿǡэȳưɼ',
                                                                            'ѻųǉŨҶЧĬʋà¬¥˭ǽ\x9c˗ɥҾ\x9eԠѵδʨóΒǹ+ɻŃÈɝ',
                                                                            'ђ҉ЦˠӴӥζРÓˏήГhǛӊѱĄäƛдϢԐĽɔэКǂԌÜÕ',
                                                                            '&Ӱσ˹ΠɣмӶӘǭÊëҸÂ*\x80ë˕ʔҸȺvԘɾ¤/ʳԝҥT',
                                                                            'Ҫ,ҩ\u03a2˟ыǸбΝúCǥɐĖyԏ¬ʤ÷\x86ɏ=äάӳďʹq¨Ԫ',
                                                                            'ԦʉɃʁӗŘ-ѿƹƋԧо{˘Лϗԡˀ˦ɥāсǔПbʹȺƑʄ˟',
                                                                            '˰ʀƾȪќəоөχµΜ·ҥj<ʋH«Ŗ¬ӇųĆԔʆ¼\x8fǯ(ҿ',
                                                                            'ҏсΚȬĊҤΑ£ҴӎĿ˼ŹϚwλ¬Вʷ¢жéŞ\x8aҟæǀӰ˚ȝ',
                                                                            '@ФʢɒǘĢ)ԚЍĜìǼÑʖɔˠΎȏ\u038dБҡǵŬӦ·˟´Ζ\x92Ú',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0379Υŗ˗Ҧ\xadſθ¿ԀϦǡʃĤ°ńѨҰƁЪҍχ˳ƭɻǸЦϢѽӥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 190463.46881283715,
                                                    },
                                    },
                            {
                                        'name': '\x99ÑԍŖӃŎƏӏɧΤĺάӾ҈µşұɇѾԙЄˉԫˮúʳÈӈǣ%',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 794842.9184320131,
                                                    },
                                    },
                            {
                                        'name': 'ǓŮΤřΕÃ6ΰȼԄĝәʞȼԓΐě˳ʄжʕŚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6628092225573826779,
                                                    },
                                    },
                            {
                                        'name': '\x98ƸȪǷӦĐ\u03a2ȹ\x98ΐ4ΣŦ6ǔԗȡ1ԧǸʃѤgЋ~>eϟԋŲ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 106278.85113595784,
                                                    },
                                    },
                            {
                                        'name': 'ǔЪɄúҫµɮԐ˖ΨЁĂçĠǫТӻΈρ¼\x8eʿ©}ˠҁΥɜƹɜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.868256:+0000',
                                                                            '20210301:152856.868276:+0000',
                                                                            '20210301:152856.868285:+0000',
                                                                            '20210301:152856.868291:+0000',
                                                                            '20210301:152856.868298:+0000',
                                                                            '20210301:152856.868304:+0000',
                                                                            '20210301:152856.868310:+0000',
                                                                            '20210301:152856.868315:+0000',
                                                                            '20210301:152856.868322:+0000',
                                                                            '20210301:152856.868327:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǆ͵Ǐ\x8fe2σʀ°ϻȘ,ʖǪҘƅƹŖĲԁƵɹҸԚѷТʕ\x7f˖\x94',
                    'message': 'ˊτ^ƪϖė˒ŐǦɲяɑѝ\\Ԏ±Ԅ(ϒ\x9a§\x7fƚŭŲΟΘǽƟҞ',
                    'arguments': [
                            {
                                        'name': 'ǔɰΦǐҁФÐǄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.868913:+0000',
                                                                            '20210301:152856.868927:+0000',
                                                                            '20210301:152856.868935:+0000',
                                                                            '20210301:152856.868942:+0000',
                                                                            '20210301:152856.868948:+0000',
                                                                            '20210301:152856.868954:+0000',
                                                                            '20210301:152856.868960:+0000',
                                                                            '20210301:152856.868966:+0000',
                                                                            '20210301:152856.868973:+0000',
                                                                            '20210301:152856.868979:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¢ΧċÓВɟϭfλҏĕƭ$ȓхϐǐʶŤǋɰʣϑȶƧє',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ä˛ƲԣǾϮӠͳфԁɐē\x89Ԙ\x7f˭ĩȂУƼɳͳŪŅӢҥŴǈj%',
                                                                            'ɻϠͶ¥ɗŔÍ½˻óʟѰʗ˒ʋʌʚƞQυʳӵӉӒуŴȑǺеʱ',
                                                                            'ʿ\x8aȝяCҾʑЦӰтӪ\u038bFƊѨzĔt$ȬvǞѦǑΚnȋρ~β',
                                                                            'ł˴ώ҂ɏӌүwѢηЛѣňǋԁȱΦǠʜÞɑϞǉIˀɇźӎSк',
                                                                            'əҍ+ӄǻӷӧҏЫʁ˼,ӉĠЁȳǤӪŢąџ϶ґɤã҃ɁƿӗǨ',
                                                                            'ӧş+ŃˤǈěŶǎѐ\x8bˮĦŶЁƦVƐ\x84Ͻӆ\x90ʅԘ vÂ}ƆΔ',
                                                                            'ɲǤ҂˙λæ˄\x9eӁνԀѫʔ,һ˗ʠҡϪЊłÔ\x9dӠӳНɴАêk',
                                                                            'Δȴːϭ\x8eßȌӟʎüΌ\\Ғѩ˶Ь¸шԄȏξӍԜѧԕβӀŭ˩ä',
                                                                            "ǬȄ¥ǱňhˎĨ«šȍȒ\xa0ʄЕσņ˂ӺđĉëЗʸӦČӚ'è<",
                                                                            '£ѡђѷýАϨϤ˪Ź½ʻɭàǌʮÝ%EɦѣԤӬϼϻЂƹƲҽȿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '°ϺÊ\x82Ⱥ4кӴƟνȹ˷ͿɓҭƑĬЁZɅƶÈȗ9øƩԈˣ¶Ԋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӁԘǥҹɑƛΈѰƂӿQеӨ\x9eҋʓq',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            377413.19480577146,
                                                                            617969.1396404986,
                                                                            -19025.332327296244,
                                                                            713629.9230461802,
                                                                            205933.3973912308,
                                                                            121336.7286419986,
                                                                            406451.6073757905,
                                                                            986388.6961091836,
                                                                            527662.738476965,
                                                                            560833.4886311747,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҇яѥ˙ǜӵҥGΩԀˍɋɈк',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            42239.31658434219,
                                                                            787731.9374168058,
                                                                            546243.7099602785,
                                                                            110198.05718437777,
                                                                            451465.3542826072,
                                                                            -45748.99057729396,
                                                                            293272.3534198259,
                                                                            941277.4732652943,
                                                                            199625.11384184536,
                                                                            382140.97258740506,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϛѧФƍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'wïɉγǼģЖǕɻˠȦЍ\x83b\x95˯ǯζĽĥĸĉǏɡХʌͱ<ɯЀ',
                                                                            '˙ΔЭ˪ÓʞʐОɱ¾ȘƫΛŭЂҾo˂\x8aJɞΫÄʗϠ°ԧɎϿш',
                                                                            'ӽѭͼɹԒůϊƵɇҠˇΌƚ-ϐгčЄνȘû3ȵªЀǧ@ϻԣʕ',
                                                                            'ˉĒƔіǾȒ\x84\xa0ά<ðѸ"эǸɜҝʨЬŝόȍӜ\x81˖-ʊǤȽә',
                                                                            'ȳÎΔ¤²ŚżԞєҊЅǸЋƩĄЦϒ\x9aΜдǊ˄АΎňԞơɮƗͷ',
                                                                            'åсǐğ`ҏ©<żg2Sԩŝ[ɻÉ˞ć7AɜҨη&ȎƠǉӒλ',
                                                                            'ƐȰ¦ĉ͵\x84ʑɞԐіѸ¼ɪeӏĤҌ¨ͽ¶OϽКʤ˞ӰÐƉȊт',
                                                                            'òŬĩҙүЉϊÞĵԏƩһɄВ\x82ŗ\x97ԂѠœϩňšÅſɉȟĊȃχ',
                                                                            'ƽ\x8eʊˉhӹӞΊǯƯͶZĄŕˏʠ\x8eԁ¬ʻĻλЪɮýӊҜӻĪӷ',
                                                                            'ћ@ȓʟҩԒлҋǍȖʰȰǆԀϘ˓p¦ƕҒF˛ɉɩŮɧɌɼѲ\x9b',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˲ƌʑħÅѩBĞ;aǉΧŋǍ˸ȓШǔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2107763722333991525,
                                                    },
                                    },
                            {
                                        'name': 'ʯϥќė˔ȚϋҜȧӥɇơӞ˪ʬ/ҕùƂŻ%$ƑϷӐɔћɃжѵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.870992:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӣΒт×ˆΤǉƪĤTӦѝ\x82',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʮζːíɩšҵϫˣӌʗǙԛǬˠß±ȏΟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1413222984230524198,
                                                                            -1465611556734707055,
                                                                            8512634272226181081,
                                                                            -1098287359326274020,
                                                                            8438360866934521778,
                                                                            -5501147319679011504,
                                                                            1290391861026072569,
                                                                            -105041127937239442,
                                                                            1273936971864846353,
                                                                            -6817202155945092380,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҳŃӪǇƣŘǳԐ+ԬôɆĴʇѐāӀѱπ\x9bюϒӬĵӶоˀƩϥ\u038b',
                    'message': 'ҩʻҗѝ\x82ÜеjˆŻӤПӸţĥ+2ȌϠ,DҺʕ|ƂȦѹƃ҈ʺ',
                    'arguments': [
                            {
                                        'name': 'Ô',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.871849:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʄǑ%αÐǉʢȊ¹',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5920724549897501563,
                                                    },
                                    },
                            {
                                        'name': 'ʟɘƈ˒ѻƦƖȠĤ7ä',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ГϪɀĬҎϙ\x9bɉԢȾЂѴцǉÜǶ˲ȺҙǷϲRɀ҃ԓʕʹƸШǝ',
                                                    },
                                    },
                            {
                                        'name': '҃҄ʜΓ/ҽѝïǯ£XϜǔƯƮǛǥӭȭ=ĤӎčÄ\x83ɎʞΒйʕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.872795:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĜΌƮ¯ů®ńͿрȷ\u0379\x861\x82ɐIѠǮҎѽʄʅҳǇȸѱʠӅVͽ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8aϽǔӀ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6322635044129114227,
                                                    },
                                    },
                            {
                                        'name': 'oǔϥƎ҉ǇȂZȃͻɸѬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 217899.56620852806,
                                                    },
                                    },
                            {
                                        'name': 'СЋļɦǉĢÞCǨ˥ʪâ˕ЄĪǟΒɴцџϏϰȁƫ«ǸʰǕԙű',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5478338074526796693,
                                                                            -1204240002384702154,
                                                                            -6386606927496667118,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '®ҭԊΟҰԄǚŦʈιҍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʬѱřȫб\x85ԕǲƖҟ1:ԡǠɧfǌӕԃŰҰϡoˏ˃ȏºȔғӷ',
                                                    },
                                    },
                            {
                                        'name': 'ŨͳǉԚѲŢǧͽснĎíʗԢʘӱȟӈҟҳSϪˇŎѮȮŝɨрȣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            446547.99487888056,
                                                                            743583.1608117723,
                                                                            771360.6539195817,
                                                                            648191.1322961445,
                                                                            197949.68725601205,
                                                                            403929.65094675444,
                                                                            201637.09503617516,
                                                                            654356.5705147845,
                                                                            32342.769734762755,
                                                                            39839.39363135677,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ґ,ńěү¦ǑʒάӪɚÄ˧ФgȪǌѱ˨ӀǶԋůԊXͱÿǎӵʿ',
                    'message': 'Ɉ¡\u038bԑã@ȌдÖ˫ҳϩĀȝӐʉɏΠ\u0378Ӌǁ\xadňŠ\x86ƋЖʢkϛ',
                    'arguments': [
                            {
                                        'name': 'ʉ\x9aǐ<ǭ˛ʵɁNӵϾɍ˚ʘĮƖ\x92ɔȽwԉ϶ƴÿԏɌ\x8dĪǚˣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԌʾʝÓǯǲЉėǾɣŌȕϸQбюƬͿÈƠËˏƟƤôʩƛθ~Ĥ',
                                                    },
                                    },
                            {
                                        'name': '#ʹƄЍʊԏƠ˯ҡҷƕȥҾԅа\u0378ѰĳĒα˧ďʹҲӁ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.874668:+0000',
                                                                            '20210301:152856.874684:+0000',
                                                                            '20210301:152856.874693:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'iǍ½ťԔǆūʊʩňԅрԀҬȓ˘ȽӺĬҠʻԃПɮЌӡЯʰƨͲ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            84220.51849855261,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǹƭќŹÕʛѭԠҢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 71877.9939854021,
                                                    },
                                    },
                            {
                                        'name': 'Ö',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 643076.6545309444,
                                                    },
                                    },
                            {
                                        'name': 'ĝƸԪЯ4\x8bԗҤŬoƩŃξUʖB˄',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3853007566573389559,
                                                                            -7484951098613294554,
                                                                            -1000437438739466936,
                                                                            -996061118032564429,
                                                                            2183742198251734488,
                                                                            4830401299214204663,
                                                                            8930598254803714726,
                                                                            -3215529824096584379,
                                                                            -6088633342061060241,
                                                                            7768175628639303957,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҥȃÒí²ʊҼū¯ęçƌ\x9bмƋʲ\x94ˊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.875746:+0000',
                                                                            '20210301:152856.875762:+0000',
                                                                            '20210301:152856.875770:+0000',
                                                                            '20210301:152856.875776:+0000',
                                                                            '20210301:152856.875783:+0000',
                                                                            '20210301:152856.875789:+0000',
                                                                            '20210301:152856.875795:+0000',
                                                                            '20210301:152856.875801:+0000',
                                                                            '20210301:152856.875807:+0000',
                                                                            '20210301:152856.875813:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѥЊƀЌwΟѩɩώǓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3737205821783628543,
                                                                            6726848197062610147,
                                                                            3024930520409199430,
                                                                            -6329623109124625644,
                                                                            -8009435709094594527,
                                                                            509145026725811277,
                                                                            7072428120787811398,
                                                                            -8770543043936397533,
                                                                            -8644575009380835145,
                                                                            8862894365577376901,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҆ƌȂϝ8ͺԛÒƥĚԫαњӇӴԦóίKƖ҃ĕԟ"т¯ɑɱˉλ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3049179435127378342,
                                                    },
                                    },
                            {
                                        'name': '¡˪˵xӵϑҥҠѨ˩жʦÏŔѮχ˘ТқɅ\u0378ҔĴ\x94хϓφŨϐ8',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3861726829046009646,
                                                                            7511608217287476013,
                                                                            6904707787420070914,
                                                                            5362036472055512917,
                                                                            -320176672189102345,
                                                                            -707486532877954915,
                                                                            -2519339058017282951,
                                                                            2479622612999581944,
                                                                            -228497348216132501,
                                                                            8016579109361643000,
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

            'scope': 'verbose',

            'messages': [
                {
                    'catalog': '¯´',
                    'message': 'ǽ',
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
            'identifier': 'ЉԆӦϋʰȸѶӒdҝұƊϦǬЫǈѭʐȦ\x90ҍԐȥѮѤŬКљ\u038bѡ',
            'categories': [
                'configuration',
                'os',
                'network',
                'internal',
            ],
            'source': 'ËԝӂǠОԉԍхдŊӵŭ.ȧɴʷÎɲѴɡʐĬʦҍћ\x8aǶР¥?',
            'messages': [
                {
                    'catalog': 'ɫͿ.ҘӬЛĀ˅ðȄұӱρÃȟǕ?ѿЛǋԑΔ#ˑϻώtћFӵ',
                    'message': 'Ȗɼ˅ʨĨΝHЂȊІȪӖŐЈŜ\x91ԭǿʟpŹȸοCƩ%˥λǐŝ',
                    'arguments': [
                            {
                                        'name': 'Ҿ\x80ǙЭǒęɏϗ°˲įʺΛôɰĶƘ"Ķa=ϨLYǪРEɑϺU',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 50913.93294529605,
                                                    },
                                    },
                            {
                                        'name': 'ǛŊǳԐǾĉǹȐńɣ__ƶšɦɨħι8ϚȓбàӥʰÒгΐȝҦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -98560.8915272378,
                                                                            606685.9110085281,
                                                                            282569.9008673026,
                                                                            628750.7286426665,
                                                                            472284.18501434627,
                                                                            457612.20937815064,
                                                                            761923.8247048777,
                                                                            872065.1539380345,
                                                                            268131.20124291605,
                                                                            56864.20572528412,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'џ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.902407:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƔxώԇϦǲ^Ҋ˭ƚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -605197757094830338,
                                                                            2831341316393669272,
                                                                            -6725829999046575411,
                                                                            -8474577667204677843,
                                                                            1590278158041922442,
                                                                            1441080339472235249,
                                                                            -6942966943140520624,
                                                                            -6160752945802338448,
                                                                            -1551776435560076461,
                                                                            425260100652031493,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҺɽХɿǰӡuĒ\x8cԊɱәȩȠǡφӮƯ»âӣ¹ÄЮʬɅΌԮϏϾ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƍPźьϿ\x89ϱǓŋPѫˈŮʾ˵Ơеɰʋǝ\x90ҷ.ȉКlʄϫрӖ',
                                                                            'ĵҲΈ˜IǙУϘ\x91ԇҚӌʯųȺѝŀʙóȔΥпΨƣƖ#+їL¥',
                                                                            'ǌŃĜ˻ǁĖ\x97ӬÍΖԓѷȖO˱ӹĊϦІQǩ\u0380ÝΨЗʔЦбǖԬ',
                                                                            'ÚьƽʳǲмːҜҶƾŌΩҢƮÌɖӋ˫˧ü|Eg=ú҃ҪƵ˯Ź',
                                                                            'ѯ°ҹ7ľȌþԪԪĈĔϊ"{ǚʕ˱íȘėɺµӶԇϑþÃuҔǲ',
                                                                            '¤ĒȎũцόªɊɓmͽLΓµƆЅӉǹĶ(ӚĒēµԧ¥ǪpϊӅ',
                                                                            'ŷýĖ3ϼѶ®ëΟʇαĻį\x8eŞӴĵșÙԈξ\x90ȷӒǪùƪǎˀʽ',
                                                                            'İʿҼӡӤϝӸȯúΊÌμӂԌÿǫȤҊϩɠʒƌEѮʟ˳Ƒ\x9cǲÖ',
                                                                            ']ȮԤҤŇŭÍ҈ǙʜˍȥҐɆҺƏԐЧȱćȊʒӆÚǷΝëēҲª',
                                                                            'ӏ¼ϗыԔϏķƁò\u0381ʫmѥгC϶ŋĠ&.ŪΟ×ȏŦ¸ɯÎŴЯ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ІǰμƂԆȓʎưůʬ´ҞšłȈҾΨъӠΨķϼΆͷŁɁȸē',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2888361665007276661,
                                                                            7161952754030995096,
                                                                            5671291583416207002,
                                                                            -3954504579207121197,
                                                                            -5467992296512030633,
                                                                            1762666611552403819,
                                                                            8331205708440731704,
                                                                            48863286281868472,
                                                                            -2552747064280149415,
                                                                            -3950925854130084791,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԬӛƽǢ˚ɥɋɷβfԮԫϓƤ͵Ď\x99ȽɎƷςƓ˄<ˇĸˡ(ϸÈ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.903487:+0000',
                                                    },
                                    },
                            {
                                        'name': 'чÈŰʠq˲ÁůĸƔҙЀÍqƦӾ˰щżʰ˭ôʍĘğ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '² ŴHʾ×ϥЁ¶ȋώы˾hұРǼeԦΡçӋҹǅƾÞϾυĀҽ',
                                                                            'Í%ÞѫѷНρȄϔʡȷƼӊɞʆʠĕӞIǭΑǧсȞtǿ΅ĤƈŎ',
                                                                            'ĥӑǹԀЊθǒѠĎʃƋĂGĜԠ½Џͽ«ǎѳχ×Ɩ˸ƃĻѫÅŤ',
                                                                            '\u0378ńŹhȔ\x9bͶ\x86ϻư~×5ȹŗ·\x8dԎÍΛȌǳ£ΖĞѡɒԣԝϵ',
                                                                            'ԢӶȔǃȩoԣә΄УňҾӪϙâҕаlԄOëϐ¨ρϢ~ϜҦł%',
                                                                            'ǔӐʋ\u0380ѥȱçϖŘыéϔŨԙËϮѤӑЙūĄΩÐēĴΛͿίʈҲ',
                                                                            'ƦWʟ\x89ёЦȸ\x91ŕƨĀ\u0381ŖÚѷĐϜəԭâGÍɎƁŐɎ\x7fʟΥ3',
                                                                            'ÐƲmуƍʲǛŤ3ĩҟţѾ\x9fˠɥŤʏ×©ҶǳʩҫǎϬɫΚĚͺ',
                                                                            'Ӕ6Ȑ͵ѰҌӦώҶξêӌÞϽг\x95ϵЖϝЕӲξ\xadþ\x92ЮԆŮРĥ',
                                                                            'ίʶǲɮƑ±ӻˏЛуͰʥˢƅӈOъ˱ęѽÎĺĠŐӢïĘӣ>5',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȥȸҒԞӄ˱əԓϟ҂κǕ\x9dҌȳѯӁΉй=ъпŲűδӯʪĔ\x93Ҍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            197928.10496938042,
                                                                            921175.1493585868,
                                                                            785479.5781801878,
                                                                            858804.5772238141,
                                                                            856178.5845536009,
                                                                            752650.6720591182,
                                                                            974972.3479550807,
                                                                            789065.5800861275,
                                                                            554465.1308641321,
                                                                            946460.3708282037,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 't˘ˤ,\x87ӿ\x88ӷɇўľЙΕϞɽԆԊ¸ȅţǇ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԝƬйƳ^ӦТκӆӵbɪĦӾǫȁӗŬӲЬϜѯŌΌȩµϼĘŠˑ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˺ÿÿʃɯъԇ˗τʶˑϟѵ\x85ʫˠƕŜęȪƉҵȊϬϐƹɻɝ$ȸ',
                    'message': 'ԠĈɾӶȌĽCсИʯд2ѶИѵĿҙԥԤ\x97Ã˔ΌźʈJÜ@ˤĪ',
                    'arguments': [
                            {
                                        'name': 'ԠϠ΄ĳ1˗§ЭøŦӬ%U3еͲ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˪ӀЌȐɃrсĈ˻6ǰ°ԕĭɹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 106481.40547824162,
                                                    },
                                    },
                            {
                                        'name': 'ĉԮλΧĘɤӭɬ}ѓóˑҼ:µȡ\x99ԉɎԌ˗ʤԗǄ\x83Ϥâδø´',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.905573:+0000',
                                                                            '20210301:152856.905596:+0000',
                                                                            '20210301:152856.905604:+0000',
                                                                            '20210301:152856.905611:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŃӝЂѴÏɋΖЎ·иʗ2ƒÌǝĴȞøϊϿ\x8bķƯØɣńÓðиÉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'әǠЮ¾ˉʫ¨1Ⱦΰў\x8cΌ÷fǝ¾ˡЩɥó\x9bӞ˲ŸƝ°3\x95Ѻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'εԔюʘ\u038dǫʦƕ·ΑŭӕκƋτȻǎӍ_ùɪǪːǑӖИǒÞˮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϋďȹҕȝ\x9aЭƩЇɶÊŹҍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 616243.3525049256,
                                                    },
                                    },
                            {
                                        'name': 'ӆüЭŅÕԞʳϢ˾˳ŷ҉ѮҮɼĒφŶǷŐ˚϶ΣӇԂ\x8dӜ΄ʑˑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 287850.3111139093,
                                                    },
                                    },
                            {
                                        'name': '˴қˇȹҌʵɜƜûԇñ˰½÷ʯǑʹөԉѬцқɄɇѐҰÓΰһЛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -98440.87514168101,
                                                                            525957.1937464282,
                                                                            69379.30617361172,
                                                                            639624.4705130135,
                                                                            562100.9232339591,
                                                                            -2720.419910726254,
                                                                            858969.1103717056,
                                                                            426926.5204830691,
                                                                            528991.716795329,
                                                                            970209.4344514338,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӥȪȵͿοæŎмǥȱҷŷǪƸ±Ԭ\x8fȘß˷ёŢpҫ˴Ƹ1ƙτł',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΡōɾȠӴ\x9dÂÄƮƦěƛƞǼĭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7122731891254480361,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҝɕϼ\x97ӫǺͿҮҽш-ôŧӠЄʉɰƄˢ\x97AӞäϱσEęˊѹ;',
                    'message': 'Ԧͱ±ʈιƴюҖ˽ƃпʱį\u0383^ĝфĴӺƻ˞ӏɸDƿ¬ÝʹфԜ',
                    'arguments': [
                            {
                                        'name': 'ҀԋӮѵXƢąϳόϜЩҤʩɼӹʅƫʑɎŇĸȊÃìɶΘÜĞ?ɓ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.907528:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΏħĉΡҿԖԈĞų',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.907692:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɭɳģľҗǣˬ©\x91ѯн˩ωщ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҳȞаΝԁʶӯœӰҚΖȮǁřĴƴŘƱː\x8cȚǦÜϺɏαÊUï9',
                                                    },
                                    },
                            {
                                        'name': 'ҥŉǭǥaĥԃÞĝКʓѝΑЛŴzßħɝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2817509862267265523,
                                                                            5310116256344120938,
                                                                            3582423924611056886,
                                                                            6830856637671459529,
                                                                            -813649605084934558,
                                                                            583773285090891128,
                                                                            -476183699376411304,
                                                                            -6263248365307943668,
                                                                            -359479954375756357,
                                                                            -3526837024609814321,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'º\u0379ĐĻròǡėԆѴǭѬǱʞ\u0382Ĕÿ\u0383ŶÅԎĽƳҙźкЮҞȡΣ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.908294:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ɍ;ŨӬԟǯȍǽɥ|ӇήĔ˟ČīǳČ\x94ɇѵʔŘƠʶӵԨϏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8483915260682850170,
                                                                            2087489917163454529,
                                                                            73060087107537564,
                                                                            4032918462144506768,
                                                                            5010454673917987863,
                                                                            -6629490764599000923,
                                                                            -5568362007096212530,
                                                                            -7007353696253141535,
                                                                            -6399997938754401616,
                                                                            5272647452307068903,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƠȾΠϦЈÇ\x84.ήÔ@\x86',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.908730:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˈä·іˁɌˣϐҒƐ5ͺįԞwŻ®ǥԮБӖ!ͲǟԔÀΏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            61817.01411195469,
                                                                            -5109.389488418412,
                                                                            375418.81015799264,
                                                                            66821.21218796019,
                                                                            558695.3678030607,
                                                                            91639.42171229637,
                                                                            793182.8833754824,
                                                                            385066.7584008685,
                                                                            737289.8994842913,
                                                                            681014.653518067,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʸщ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 58982451016231360,
                                                    },
                                    },
                            {
                                        'name': 'ϔ;ҲĹ£ƠΉʔӶӃʨƉůϱĖǅVІԅȵȘɍɲǇπԙ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 887651.4448883085,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'чŪ\u0383\x97ΗƄ÷Ӝϳȃ\u0383ˋ9\xadȞ^ʬ\x9cӆʈĐĘƪŎɠÀI˘\x8c\x8d',
                    'message': '8ЦˌǊҙѲǂ¤ѾѼԢҗƜƾӣĘΙ_UѭɝҺǰЛϪǴĊҦÆʷ',
                    'arguments': [
                            {
                                        'name': 'ϧӜͽȑŔĚǂ\x9cӿĨȟŢσϝϚЗѿѡŘӮ˾ƯǚˀÚ\x93',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3033826766247644109,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'βŽȬɲŗ\x90ω˭ŏM˫ƣӗӿϊƙƘʹ¡ϢǎaɰʗϿʴťǝĕѽ',
                    'message': 'ө˱\x8bʴɧԈ¬\u038dȚјɧˆʇʈǳ>İɽЭ˦ԓàҊѥǼʳΘҟҍ®',
                    'arguments': [
                            {
                                        'name': 'ŒŬ\xa0ɞƱɖӚƭǏǽȌłУ]ơʞΗĘąϋ˙дΨŜѸŎ˱',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.910082:+0000',
                                                                            '20210301:152856.910097:+0000',
                                                                            '20210301:152856.910106:+0000',
                                                                            '20210301:152856.910114:+0000',
                                                                            '20210301:152856.910121:+0000',
                                                                            '20210301:152856.910128:+0000',
                                                                            '20210301:152856.910135:+0000',
                                                                            '20210301:152856.910142:+0000',
                                                                            '20210301:152856.910148:+0000',
                                                                            '20210301:152856.910155:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ū\x86Ǭ®äʤ\x85ǼɱĤ,Ȼǆ-ȡō{ҳĂыԩƋэϹӰАB',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.910424:+0000',
                                                                            '20210301:152856.910437:+0000',
                                                                            '20210301:152856.910446:+0000',
                                                                            '20210301:152856.910453:+0000',
                                                                            '20210301:152856.910460:+0000',
                                                                            '20210301:152856.910467:+0000',
                                                                            '20210301:152856.910474:+0000',
                                                                            '20210301:152856.910480:+0000',
                                                                            '20210301:152856.910487:+0000',
                                                                            '20210301:152856.910493:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƌӡ͵\x95ΊeǵҶʛrŭŃƜ\x9c',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ΟΌήϦéĤƊҞĭ"ÃɱѮƙƚѻ/ѩʏɯ\x87ŻŌŨӓŴȈ\xa0ҟЗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˱ϢѐЗ\u0383ΟġЃ|ΘƋсЩӨ@ϙqɢϛr˂ʋ?\\Ǭʫǩ·ҬЁ',
                                                    },
                                    },
                            {
                                        'name': 'ԩƭЊʣȧѫˎîĲ)ЄÂ^Υ!ԩżњҟтʢӟLґǝěŊȃʽć',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'źƶ\x86ȩԜjȉѩ҉ɻǅɞ-θфмӖҷΚЃΨԀӮˍøȹҌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.911455:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ͱƝǛƹǞȖԤȪĢĝԫÍҧЍΕөóȺƑфǏϖĖěǴҪΒʼǜϣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ηʉǵ\x82Ȓ|ūЍŴіЄ9҂úǾŉȕГяύȒ9ǟĎΟɃАşѢΦ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÿŢ\xa0ҪΠʪɲ¡ɣƆҺǁϟʜЃŚA\x9cӋѢɸɌǨҾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1415154948002156437,
                                                                            2743689869740889509,
                                                                            5433573161929117035,
                                                                            6531122219169521421,
                                                                            -8771273435413367417,
                                                                            4690013810279836813,
                                                                            1737417035531366035,
                                                                            -8955591528793694573,
                                                                            6407721022974017151,
                                                                            1655027108036837750,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŨϜЮfcǒҵȍʷ\x7fǚӌгȴ\x8dγwl˭ŬέҰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.912477:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ԃ³ͱѾԪԍœŉѕmԔãə{҆ӹ«˥:Ҍ϶ҰŕPŷɺǲVɎҤ',
                    'message': 'ԎЉ\u0383ȕԍҝʩŧ˖˅Ҭȋ҂ʁ#ѬͼϛͽƒԐҭƥɣþ0˟οĚӖ',
                    'arguments': [
                            {
                                        'name': 'þɝӫȠëѱġԫϿЦЛȐǏmҦƒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.912964:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʗɋέчȄ;ƷʱșйҐѪԈΟІҙźƺӈʭȏǪƗҨĮɮǊφƔ\x82',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ώ\x80ÃΤ˵ŌǱóлǐʟюƉͱɆƂγӢĮøƼҭȠͷˆɹ\x7f\u038bʕĶ',
                                                    },
                                    },
                            {
                                        'name': 'ŇǼ\x81ĦrĽBɴĢĹΓè¹Ҋҗλ±ЉК˰',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѻțƫȧˈ,Ƚг¬ƻǑϮџ\x8eӏή˷Ŏę\x9fɒǀҡÂѭƤrӏӽɺ',
                                                    },
                                    },
                            {
                                        'name': 'āǧů\x9cΛƩșȇʴШĠɃŔԂ˵д',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            23313.04292125153,
                                                                            471911.36140912527,
                                                                            290357.8358183878,
                                                                            613921.6096109179,
                                                                            782866.5668137625,
                                                                            607112.9564120515,
                                                                            954677.394014786,
                                                                            276024.62352927023,
                                                                            114724.01074191817,
                                                                            722492.6003453544,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɡʺǘȕѢƜȇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9053716756229199213,
                                                    },
                                    },
                            {
                                        'name': 'čş®ɟχЂƖ҂Ȋİǈ¼ԫϭͿâʹԙ~ȝǛӃǰσ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5268220557917601447,
                                                                            -4069722539431796945,
                                                                            8718231277175483126,
                                                                            5141494648005269602,
                                                                            1470166148021732825,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'RīҎȾ˕ėҫ±ЖʹҬζϢōƾȒƙΙʚǘ]ѐȧìҍȡӯȿȅӅ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1442285010578111160,
                                                                            -7211484972925474533,
                                                                            4505593225201097664,
                                                                            1069048284679533226,
                                                                            1443178482275520974,
                                                                            681904882390843007,
                                                                            247942611901048115,
                                                                            6169102834864934291,
                                                                            -669177560835175908,
                                                                            -637404658520555201,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȁ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '½ˋӘǒҡjͿHԀԕΜӼèʥԡȝѥèŲ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.914662:+0000',
                                                    },
                                    },
                            {
                                        'name': "ĻӼӹǳŷξ͵'ЄƯ¡ċ\x9eйŏʻѥԜӅԐӮΒԆѤ0±ϔňδҀ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5095023288436738382,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'șԊЖɗҝȅǫɁqΐˢψѵͷЄΈ˭ӎƥȯ\x8bϞάΰʘɩҁȘʒˢ',
                    'message': 'ΥºșȰ«ŧ;Ǘċԣ¦ŜļëѢCҭɁоqϱǖƊʊőȶ5\x99с\x86',
                    'arguments': [
                            {
                                        'name': 'ŵҷїΤºˁƆ˞ԀķZϊн',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '7ΑʨϤԒɒǉɐːÃӏҋΔϩɣ½ȓƶīȃ$ɢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            882581.1476579747,
                                                                            339779.78473105095,
                                                                            985473.9618124885,
                                                                            525287.6757276257,
                                                                            569772.3083992884,
                                                                            626413.5351042391,
                                                                            -58498.81485629842,
                                                                            970524.8326381426,
                                                                            691768.9769106557,
                                                                            386408.00109154417,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÿ¾ӺĲÑ³иԚǄѱǜƗȷɨȱȞņѣҵ8ŴɕԧʟΧɥΑ\x87Ĺɮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4001418896841007477,
                                                    },
                                    },
                            {
                                        'name': 'ĘƵɞǱaӏӆƿѶœ¾ϋѰП1,Ɨԉˌȯɣƣ5{ԓϞȇϬѲҥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 114135.9283217196,
                                                    },
                                    },
                            {
                                        'name': 'ƁШÂɁŬɣύʧĐ{α¿ҀѱҥеѱƛΒѴгϤз˙ʉϏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϛѵϓђ_ÃѪҟưɔGɓŋ!ͳʹéǗú˂ʧĕ\x93ĠϠϵɛΙα~',
                                                    },
                                    },
                            {
                                        'name': 'ʐƓǇʧǖӅƜԌЀBˎ¯ŎÿÒϛǩǊӽʱŜI',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʔɁԛȦȰ\x8bӵƲąӮҿ\x99ƗˆȢ\x9cˋҞѵĥġΞҹLCɶʌ˕ʷя',
                                                                            '6xʆŮąȚҟ҃ŝÈԎϘӗ˩ӎІʓɷǮΛĥԂӳșƈǀӁȩαS',
                                                                            'ӡĳӋ˕Ʌǲί˻\x8fʝԙ)˹Ň˛ϙvыșʸ҄ШȲȊӷҖуžˊÈ',
                                                                            'S³ϩ\u038dòϗЅǶѓǄʶ´AļҁΩ˚ԑԆԢƁιěČҋΓ·ÜϕɅ',
                                                                            'ǜFƤʼåҔŚɏӋˆʈϽ¿ϮΦʼѰӦƜíʕâɅÍҧϫʅºΣɓ',
                                                                            'đʘ\x9bŪ`ğȖΐŒԈç\x93PфΡ\x9aȳѳĭPіϏΧηǖwőǣƕӎ',
                                                                            'ȋȪǭҝÉԡλ\x81ĜΫfƊɧùπӳ·ʩXϷǯѢǠ\x91Ŭ\x83Ӝ\x8e\x86ԑ',
                                                                            'Ȋ|ȧ\x9bþĶhýɴď\x9c˷ʅǬ˒¶ĕϳƛ&\x91úƼҨϠʩӞ˜эҍ',
                                                                            'ņӔȃ\x8cΛYǑOMϤτĔÈπƷǏ;ƴ\u0383*ǳXЦ1ϖ¢ɳНǉo',
                                                                            'ЄèăȢɑǌ\u0382.ι9ȃðӃƇɭȑƕ]˻ɪԓˮϼ¢ǽКsϻ÷ȑ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'űĖšŶҸӺϔ˱ǿǩŊЛƖӰ˕ĔЋҹäόƸƎ1ȱӈȶɝ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ұˇȜŸƱЄӴɊǘьêƶɼēȋȫĕ\u0383ȜϠΐеНԗƋѵ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɉͷǪԫĨκϓŻ\x81Ȟģj-Ȏ҃ГŖćÌǕԊĘƮÏЊŝШĥĤȩ',
                                                    },
                                    },
                            {
                                        'name': '˪3ӪÞʓΦϱ˸łř»ț',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϯӋťɿ:ΈӧЄȂȺєǓΛӄbȳǃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -12438.50166494785,
                                                                            280848.01610352815,
                                                                            799626.2665444993,
                                                                            281900.7811050473,
                                                                            335.91995993712044,
                                                                            441341.1481857768,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'УȣĕîϏѳp®πήȎΛԡÿʣ\\ӥЎӥUӊŔӔӗƧŋйίʡВ',
                    'message': 'ùъǷГɌȿǛ1ȼҽʡҸӂяʢÙČμҔɡϖю҃ψöȏŃЪĺɣ',
                    'arguments': [
                            {
                                        'name': 'ɾ¯Ї1ϭʎʤÛťLŕŨΞˊ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ϚɆѹɌϰ϶',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            ',ǴɶȦОƙҡютÌȘҝԋύԈξƑɆιѹΧȷoѱѤѩˆşѾЪ',
                                                                            'ΈͶѴɴȻĪԡˍʾϤȑȄԚѡɞǯɱԆΖɕō˗ǑśѢȠҠӎǾ\x9b',
                                                                            'ȻԐƒǇđЮÂáћӰҜąѹѾĜ\x95ԖŊŒĪȫŷ\u0378Ӱґ\x8fϭÑʒ\x80',
                                                                            ';ŧRŃ\u0383ζˎvĭЗ\x9dńʶЋȄωс;˺ː&ʈ!ГʣτÇǻťҷ',
                                                                            'ΠҁΨϊˊċҭɋҼɚϪϦЁͻĺǲҘӽрÐґźΊtҢ˝K˺Ξ˂',
                                                                            'âΛȴǙƲ˺țͽҤȤɡȨʹѬӈʮ˩D`҃ǬɅùŞĜ\x85Ǎ¸ĥɹ',
                                                                            'Π\x86˖LȺæȲ҉1Ð\x89ăғʡԕ͵ύ\x84ƽΫɃIɾȪ©ɠĝřƿг',
                                                                            'ȚģžʩҨʅΆ»˽ɖƆԛøʡıŉǫȴ˦ԙǆß8ĠÛǹӫĜҦ)',
                                                                            'ѴɳÝ^уύҺуϚȴƈʜѻӥȐόɸůɏӒĳ\\ѧʦ˩ʺΪʠΝέ',
                                                                            'ĨŔÝҔɷǲΉҸ¨\x9fԙʂѤѭɚԖҠэƦʽɜqΰξŊɋvɬ˔ϊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˶ģŖƶaēӏǷцԚԭРѡȉҠɦʭ\\ɕҨáԔʘҭɤοÖƂЋ҈',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152856.918642:+0000',
                                                                            '20210301:152856.918658:+0000',
                                                                            '20210301:152856.918666:+0000',
                                                                            '20210301:152856.918674:+0000',
                                                                            '20210301:152856.918680:+0000',
                                                                            '20210301:152856.918687:+0000',
                                                                            '20210301:152856.918694:+0000',
                                                                            '20210301:152856.918700:+0000',
                                                                            '20210301:152856.918706:+0000',
                                                                            '20210301:152856.918712:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˝ϖҜǬˋȟχɲĉŇϥ˫ƱбјԏԔʩΑКíȌԩӻːӕqêз\x9f',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˎўӁņßGҖϘ˶ϚþȠɳӬǇӄʂѽԬɓǺɻɯҜӿ˺ІȬϋȳ',
                                                    },
                                    },
                            {
                                        'name': '˞ſ\x8fŭҗǖϠʃƻЩèԨƓиǲϔѭоǓ˯Ϡɝµų',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'īcÑļϫ^kђњфОԀĵȍ<\xa0ǫƻЮ\x9fόȀƽȏǏƬҠԂŠ\x8a',
                                                    },
                                    },
                            {
                                        'name': '˭ÚǇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 493389.46691904427,
                                                    },
                                    },
                            {
                                        'name': 'Ŋėʿò¦˻ƙǙȳȗѫƔ\x8aèɝLЈ΅Ұѱ*ΒЊʌЭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -440054584320691599,
                                                                            -1542560377661451004,
                                                                            -6476237636481364737,
                                                                            -8064495345024233455,
                                                                            6583260191455344092,
                                                                            3352263473445415033,
                                                                            -8998330960837187814,
                                                                            -8104479141869531616,
                                                                            6988421185602220419,
                                                                            -1162718007333121377,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ČĐ©ρ˞ǛƞћʋȕĠuJɿԭƒοӻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 832004.4425824152,
                                                    },
                                    },
                            {
                                        'name': 'Ѧ˟҄Ȼ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8809990783300061202,
                                                    },
                                    },
                            {
                                        'name': 'ҟ.ȖĘϖßӞ˓Ҹ˯ɺӆԁ\u03a2ųƧĶҧη(Aȉ˫ŬγǸ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 924147.609628067,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ņҿҗɷж6Ƴ\u0379Ě\x84· ϮʃŅЄԩ˅ÇǔЋXϐƦOĽğѮʲğ',
                    'message': 'ԡȖªĽȭԧçΟŔǮuԛŉÔɽǝxk"˂ŮĂñqӻƴҥҗǼƔ',
                    'arguments': [
                            {
                                        'name': 'ΘҔėҷҁʐ%ˌʯћ\xa0ԑůÃϬ©ƊTũƔŐͳŤƴǹɼӐӸΏʑ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƦGДҿПɊ˵ѵƲŗҖϞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˁɆ\x8bȢƱ˷ȉÊɂԢvϺŸ1ţµŪѱȎ@Ԝʯǝͽ\x90ĳСȊx\x80',
                                                    },
                                    },
                            {
                                        'name': 'ɼʲϴԅϱвëˍҼ:',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5882595538954663733,
                                                                            -4095333340568251832,
                                                                            -4949617446484780193,
                                                                            899231601669030802,
                                                                            4219375762174861789,
                                                                            4525893268871630903,
                                                                            8633886385765672384,
                                                                            -4737238001425945468,
                                                                            -4293083395815350494,
                                                                            -8394670750186709083,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɧӕľԬŒɏɕІƕĔŤɰӥĴǐФ\x9aƠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŹΠηԇÓĆӸтˏӫHiAȝ˷ưƜ\u0381ȓϞʟÁϩʃԤѸcÛԦˋ',
                                                    },
                                    },
                            {
                                        'name': 'ϱ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʥ>ɎѼÃͺӸҎ}ӲѯŻöȭΫыƒ°ěλƲìиΉIȊ҆\x84ͻԚ',
                                                                            'ˑʱçǈɑ˘˗ǦǹüəҬǯ<\x9fƲ.Ġ˼Т·ťϋɞɱʛͻСǿÄ',
                                                                            'Ʋ¼ҵɏƎ\x88϶ξƺ\u038dZñӕϤ¡ӉϿѠˮŐңʡĲéɚŏϕąɯԃ',
                                                                            'ҎȩЂͻ-Ϟɥғ˽ϭȑʽÎϐəƼŞӟͱϓÌæѤƇʉҙʷŒԜʔ',
                                                                            'ǷWŚмšʘϕȵǏǩõІgϛȟǆЖǠàӓǭ˼ˬͱԌȲC΅Ȁҁ',
                                                                            'ăϸeДƛʇΠɑœʂԓĝμ@Ϡһ®ǯĤӒӾǢə˝˃mӳÁƬ&',
                                                                            '¿˕ƑɖȥÃӖ;ЖűơɱφʊˀӞǭ\x98ǙˢźéĆʵάџ΅δӌϴ',
                                                                            'ѩʋЛӇǌ&ƪɱθkӊ\x93ΙӯѲё¸¹ɸєёЄò\u0380ĿƝqéЀӽ',
                                                                            'ЁӘ˒»αPӣԔȤ$ҊļÛ˻ƘԌάB΅\x8bɱЋŶƏ4&ϢǗ\x9dς',
                                                                            'Ҝb\x88\xadҫʖЈıɡǮӔОȴѿĴʅίȩҿœöʏµIΙˊŶϥϷϧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϤĥɀӹBʢŔĺuη',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8641102514167277039,
                                                                            5348649242703720819,
                                                                            -8836953788814798931,
                                                                            7471003558574955935,
                                                                            -6573528039422631494,
                                                                            -2048124235974963689,
                                                                            -3970526151844490591,
                                                                            -749721223171485251,
                                                                            6845325885474266528,
                                                                            2701482152159693957,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȁҢɰɘϟѿŀ×ʺȁ\u0379ʎ˗ÀάЕǢʷȳEȳӨàãЀǛˬʥλǨ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҿηǩēϨƂŗɁȣæĞό҉D\u0382¬ǔƏͳǳӄ5ɰгΜȝԦʄљƧ',
                                                    },
                                    },
                            {
                                        'name': '°҅MΟˢѳÕãϺƦ˶ȜƝ\x9fԞѝɟʠħɃŖϱȰ\x82ϭɤҥYЭΘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 78095.78853404956,
                                                    },
                                    },
                            {
                                        'name': '0ӂјĭѓʓɒњˡȡҏϽͳƊы\u038d,ϕκҔţљќǗбΘƄ\x92ΘϪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7756464497461985779,
                                                                            -6222174053392840572,
                                                                            4419852488839330178,
                                                                            -4949863502976188798,
                                                                            9219668470738156502,
                                                                            842199949402515553,
                                                                            -173531050863186709,
                                                                            -4475856523690951574,
                                                                            4397500965115118953,
                                                                            -6569830367258717277,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x84ʛŢŴ^ʫџùǝҖԎ&ǯāîƺҒ˳Ŭ˩ˈ¢Ӏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3625423532675609002,
                                                                            275990782949002661,
                                                                            2571634073383761267,
                                                                            -591447900951101235,
                                                                            -4214130247680218196,
                                                                            8300477021665286202,
                                                                            -437971813736030102,
                                                                            106521725822106054,
                                                                            8047529004091216671,
                                                                            -3332957088533121610,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '2IӉӷӿ\xa0ϋȀĳ-Ƽç˶˲҂Ǳʋ~Ҁ\x97\x7fѫŠ\x88ңӿ˽ьѲâ',
                    'message': 'éηƩƆ;\x96j˛ĲƲĕɤЧҢŵůϩҫƎҼщɲĐóѳʾ ʽҒ҄',
                    'arguments': [
                            {
                                        'name': '\x8eċԜΆʶ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.923007:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѤϏ\x9fƐҾэqɟʶӡηàʷ˃ƓѲԟəò½ЀʤȭаҾhʽȖɻJ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 791709.5152490076,
                                                    },
                                    },
                            {
                                        'name': 'ļʕÙӾʳјƞǩ϶\x8dϴ\u0378Ύă϶Ȍƀδtя×ǳОϠ҇ÞϺ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            390838.6845809327,
                                                                            568647.6558246259,
                                                                            805667.430348711,
                                                                            784572.0505798319,
                                                                            479362.1949026424,
                                                                            348161.86025612545,
                                                                            69746.3859043869,
                                                                            274345.29451308545,
                                                                            433063.76953885774,
                                                                            940070.8599683509,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӝѕԉҝҙĶΩͽҜœȿϼԜѐδŤщ\u038dԂɳԏГÉΧύAϣɐΜŸ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152856.923618:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Н¥Ŋ\u0380тӎϋ\x9dӰ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4646239104470903531,
                                                    },
                                    },
                            {
                                        'name': '\x80ȝȩӟ˩ƿӈВѲc˙ZѠЏȫɪӿÆ˞ČЦ\xadʁѿƂƷ\u0382ʻνӤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x97ҳσǜʯϼƓΕÂŕҴ¯ϮS~ʜРӕƻ¶Ħû©Ű˛¶ɀŔ=Π',
                                                    },
                                    },
                            {
                                        'name': 'ϋΘ˻ŠƸƢ\x91Ą҂ӚáCƞũӎ3Ԏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            150016.18524159104,
                                                                            24514.852173220323,
                                                                            67959.90372493403,
                                                                            950737.1288742865,
                                                                            715156.8140411479,
                                                                            -84473.53357831943,
                                                                            745710.0572835881,
                                                                            577835.1058259915,
                                                                            -16926.399081821102,
                                                                            -59308.22675938185,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ċʽϜȤɴИĻʤǂɰӊǹĨ¼ȝϐËǏΗЧ\x9a½¹Ң˦рǩ·ŅȺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5542452489538239620,
                                                                            5774440698200815262,
                                                                            4326636130507614967,
                                                                            -3297553295139847978,
                                                                            3335092588044172508,
                                                                            3209379489527280064,
                                                                            4636344739011163197,
                                                                            4218891772988852223,
                                                                            6299253913603672352,
                                                                            -3842117525647105536,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Äɵʿ΅Ȟj\u0382ӬXѐļ˲ѩ`ЖӂύïҐșǼДҶҎϾϓEƆΔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Жǒï˲ԟ˕œ\x85ҬҒ˞¡',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -44236.198549814086,
                                                                            927480.6531169916,
                                                                            574445.9163079446,
                                                                            969165.2570777372,
                                                                            394944.3579588537,
                                                                            356550.42781343183,
                                                                            464949.0018430294,
                                                                            221646.7298048099,
                                                                            982169.4910439402,
                                                                            -40450.14456682146,
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

            'identifier': 'ԥˆǥȸҭ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'β\u0383',
                    'message': ';',
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
                'identifier': 'ӀȸɿʚǔԈԪ˶ӿŉϭȊԔɖ\u0381ŶΏ7ġҩѥΥԢƦ_ăЍшƥĊ',
                'categories': [
                    'access-restriction',
                    'internal',
                    'internal',
                    'invalid-user-action',
                    'access-restriction',
                    'invalid-user-action',
                    'invalid-user-action',
                    'os',
                    'internal',
                    'internal',
                ],
                'source': '\x97ɠȌˣŔS<ӭ^ЍԨьůұWľİ\x9eѻɡ7ʍ¾M\x82ɲ͵ɴϩӵ',
                'messages': [
                    {
                            'catalog': 'ɐ˂ŠfőʴɠƝ˜Ůʒ˃ŒǋўaĩұŻϦСͽ˪ʎÙȒдȒ/μ',
                            'message': '±ùťӽŕǄ=δΤ<ɗҍӣӗȱũ\x8eТԠ\u0383ƽҴӰщʹȧҸ˛]ļ',
                            'arguments': [
                                        {
                                                        'name': "υӘΜNʢϳԟľșŪпłǑѪÁŘԍǰЃ'õŗѱӈќʑǃʍǂƱ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѸϭӧÞŇːЭńԉǑΆǥӾђЅЛџθġԥͼȂҋѺ2',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΰУŔȯŅſҞȯ\x95Ҍ^ěοʅɠӶƗԝˡЗϵΏàӇƲȶԫȆʩή',
                            'message': 'іҕĦЭѣÞǦąűиͼɌɳΡǶʌ˺Ѳěɐ1îĶȜȻ˵ΈəPԑ',
                            'arguments': [
                                        {
                                                        'name': '~ӎʬƲИӦȀɁɌʌƫнǥƚmřʝɹĞӏşХѝьɮ\x86ͻʭҚҾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ºǬÞԂҨðɎưʥšԪŐ½ȝ˗Ҽǻ\x86ü!ˊpѭJΠɂʊɿЙЊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3967834614752778243,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ψǺʅʏǽιʅʱԂŌӁƗѫ*\x91ÖΘ1Ư>Ɓѥ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7173263501745628306,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƠĳǒԕâȦƖҚɷɇӰ͵ӴiӸГƙʳéԀǊǚƵѨŧƢˬΈϕѣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˇÝԥōʦûvΤńυҬ\x8a҆δ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐ˻СûƖѽϧ\xadξ/РϹőȸӄљŚĵȶмȹϤ˘тӐџŹͳ*ˣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'FҩúǛBȄƖtϧǇНѢψǐǜȅ˳ŏĤӶÚˢŷȾ:\x95ŪʹҀх',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȐèǾӧ/\u0379ș˧юҕǲʤʫĉˁɔіͿӅӝˍǡԭàЄÒƅʯǢ˸',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 87417.24250446903,
                                                                        },
                                                    },
                                        {
                                                        'name': 'хņ˵ńȁƒ҉ŕ×ӵѫм˾ǚϋējt¤Ǟӑј¦˄îɠҶѼŦ%',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.883822:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΝăȈЂԜƊ/ŪǙºԉłВ·˲',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.883963:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "²Ԕˠɽͼm¤ëʛȨ\x80'ǅ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҽîȇӉƈʿųǾӵʁ»ХxǶ\u0383ąѦɖƐҾ˶Ĺɭёӫπ@ѵΦϘ',
                            'message': 'ɵ`ԛѿÏұΞǲƍɗҭҴԡƩũÛ\x83\x9dҿêɬ\x85ƘҦӰѿÐϯȶñ',
                            'arguments': [
                                        {
                                                        'name': 'ӿKӀʀѫξěŪȮÌ˫щǾǕŸǨòӛɡѻÕҢжț˴ɕșЁˁ\x7f',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϪҔɉПЃґτШÈΛʺоˍԍʘȃ˟˙nЫӖʗʐWβÅǚӑǠӌ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃӏÇƜƬŀɻÝ\x98ĞѪєʜϗʧRƥѽΜâԩ͵єˡĵðԆԔƧo',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.884861:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ůȕƭɴӯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΛΨǤǗϔԩԨ\x9f',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.885170:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȐŴҋЙŵ҆NŷѦʖãĩǳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӑɠ˭·Üй˖ƪŖèɗŻ\x98xӕ˽ȨυҒ˹ι',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 850640.8918118369,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˑ҅ϪʻϝǠ\u0382ΎyȤɯŐÀҰYБ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѿǸɾ˥ԬіϦϷ\x90ĽѰğȘʑ;ǃɻɢ\x80ƵżǓӺƌǓψžƳċɤ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȁƛ\x85Ưя\u038dҒǡǔ\x94\x93_&Ϡ˭ʢȺʖ΄ʇÚǏƄǚϞəŝ\x90цǎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ќ\x82Vԛǳ\x8bӲVĤŉþѼǆĂʤƝͶϳ¾ėҡťԒÐɫΐ˽;ӱӊ',
                            'message': 'ɝȝˏҝїǆīҴѻ˟ȻƦӇŎ\x89ôɗйӡ!ǣҪ¿ӥĩȾМʊһƴ',
                            'arguments': [
                                        {
                                                        'name': 'ѷʴԈ\x94ĨɁċʩŷԂʌɤԮ6ΪìôԛρʱԘŮĠɐѱҬΓԈŘ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.886349:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃǢӚɄѶǃӲȱѾԑάʃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͽ˫ŢȳɿǆǵČεϠ«Нí',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.886659:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'іɱ\u0381Ǉ\x95ȢҀhƑӇɷíжǣ˓ƇðːͿȐϭӛ҉Ώ˹ˢЩɠϜԬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9cǩЦњ´ʒїұΟӼɖĺʃƭƂkͳϣ6˲b',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƤŒʹŇʿҠʈӜʧϋɫñÝϬЀ˲ƽ×ƯŗЄҴʍ\x86ĭԈԚҭӲŸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.887205:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѱƋķҔұāǰаƚˁS',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҊþĂĳǆԈƩҴ[',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȩӬOӞ)ѿΎƢԄёΎȎгɒ\u0378шҚ\x9eЃσϠɵǥˤǓЅɹσ҂Ԗ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¤˽ɆǅϋʎсύѮәцŰĘώӂˉȔɰΉǅҨŪ˺7',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 332799.9269669838,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƏԕјCȃфýѪӀưʜœԐ˙ǓsТ¼ʤʉмҕŷ]ƞ\u0378Ӏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԅŹɼǶq\x8eŋ>ΧЧЦȃƙŔМɒΌхĽĘÃɀРΝ¯ɨɃªϯҨ',
                            'message': 'ϯŌԑǘ·ɜ˝ҍǠÎƅσгFԃѲӑɱɨНќł!ґӷӎхŘ˪Ū',
                            'arguments': [
                                        {
                                                        'name': 'ŷϨȄͰǠǨɒ)ÀɄж\x88ƥǃđPί',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˛ÊȨ\u038dv˦ɤ\x97ĒЧΚǭЮŁѫɣκ˄˷έʯTǫ҅ΖԡĄ ʟ˝',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЈƋɏɍɻʁϤŸԌɠ?ƭы©ȱ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΏДЙԑŁžǂƶČĜȷϭҋÎǼƠԎӗϰ¶ĮȘÃŊȣԌԏȝϏî',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѲΡǥΥϓԩʻƼЂҏҀɅɐҡ\u038bYΨūŏɉϹЌ˹ФǥǛ\x87',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŕԧӄƮϼӫʦѣЎsλȎƳĄůǽĿȁҤψҳĐĩŕȳɚԌʑˤб',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫԥkĿөêˁϬ˫ҥҘϻьίĜř¹ǝ¤ȫŢÐԘȴ\x9eǅã#Νģ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȪӤØԎүòƜЁłҧҔƂΐýʣŦрşςѡ78?+ɻǳÔЕǏq',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӃЏҦ҉jÕɇěХǫĻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7008780354222503253,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟ\x89Ϊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŁӣӻЅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ă!яϣʜɺӵʻӢԡĎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ԮȜNƁë©ƬcưʡфЦj'ԉĳǆ˵ԘЕāđӛǑɣɞԚύɃÆ",
                            'message': 'ҏήΠɚњǴĩʻɎŮ˹ÃZǣɽΞȀŉĉ϶ˈΫϘӰɵԠʲʇZӰ',
                            'arguments': [
                                        {
                                                        'name': 'Ķ˨с˰ӘÌоɻѵӟϥѪЅÚӡÇ-Ŏ˄c\x95ƂπͿƊȠǹĮɄό',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3920840278401845816,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҲƢϲéɽǼi',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϟˋђ\u0378Ҋɷοļҵπȭϔü\x94ÔǒΉζӖҰ»\u038b§ѐʪϭƺӸʡú',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 240546.3117101965,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǴĺуŪµƿB£|ÉȗѴ\x81Ě*ȽǱӘ\x85ф˨˥ĘɐɯȈǄrͲԟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.891492:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђÕ#½ʐ\xadʛϱϧǃŲҎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ČӤπԛƋ=ÈΏɕ\x8cӥû\x8b҂űŕӪЋεǛΠɹҕӟîɰҷźʱμ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɢϯɄʗηԈԦíĈRϮ>ӂӡ˄ҢИԞhÅĉϧċĂÚҀʨϐȠԙ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x84xрŋƅҜöȓ˅˖Ԩνϒɖŀ\x9d\x9bѪƩӵ[ƢϜǵđgƒѺ˵ͻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҳȪ˪_˓ʴʃћǬԢыȬӱКϞѕеƺƾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɰЋɫʁИƸĹέķӚʊYà;ϴ\x9bÐǱúŜƣy\u038dȍɊɪԄҦϘҮ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'DѫҀϾÙʖŤưтӄϴ\u038dџʰ˫´ԘġƮĈЫ4ÛϔΔĤȈĘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƺŎɜǰЍԐťȎŇϹƘӻΟҺԭҖӡƣүTăнƀԜÏʽ˔Ɋ\x8fŒ',
                            'message': 'ȜƬKȺԆɑƒǝȹűzѧЧčóƌԨɰӭŘʞʮˠЩɈϹ˯ƸʕГ',
                            'arguments': [
                                        {
                                                        'name': 'Мɣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÌβǑġҧӈƅϗȖÙ˧ȏЃϤԂǾǞƬɃĽʒsΒѣ9»ϡ˘XѢ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣѪɺĭǇȐҺ®ҾÜơùϤEϵ\x96%ˏğɉƿЂƎЊԕ\u0380\x90И3',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '|ѽҟê§Ë҅өԛŬµӦȜ˱čÙÐŪʲϓЧίӠϷËνұҟŊӊ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˙ØmԫȋƓπdЏĽʩĄɨѨU\x88śʚǮѶчŖɺ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŔȼĶăəЋӖƟѤȪ\xa0ɋΡƑҨДЧĉΰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǫҷǼ\x92ʕ\x85ɂǳ¹ǋӉŹο˧ɥɖ˾ĿҎЃăĔǱƄƚ\x8dҋͺ˹Ë',
                                                                        },
                                                    },
                                        {
                                                        'name': '˯ƍťџűÏΖ˙òƴуʇ\x88ӕɉΟǹȏӽʹϼșǜΘφˊ4εÅʊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 722097.9962059039,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӡɓɣβҋ҂ǠʁӻŹўЇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˘ҁԞɺƭȢĤhȟȩŋh/ˮȻӣΫßҌДЦp',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.893913:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'pǤѥ²ҶĳȡϱԊd˗°ЂǬȑұƯĆģɋӶĵŗԟȡƥŘĲӈӄ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '®Ȑɑʩćɻƍӭ\x98ŝĪϋϵϊяſʬƄЪˡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'śΚ\x87Ͻϗј\u0380ʘűԏòʤˉЖіʓɊӥ\x9dáщǮÆӏÆҳȄα\u0380ă',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΜӣÂԔǀʚӻĸɑŽ+˞¯Ӣэƞœѵ¡ϥЩŏƂΡȿºì˹ҽϴ',
                            'message': '\x98ɫŗƎi\x97ǕƩɩƻǢŗԗǶӯŪɂ¥ŞҷcԅˇȠȧIˎԮ˟ӫ',
                            'arguments': [
                                        {
                                                        'name': 'yÎΤԞЧđτȽ\x93һҦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3031956980950632912,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӴʒНǴΐ\x98ѢƷЕДǝдÚŉρa',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɗȆɻʼɲԏϳ˲ι',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 431941.8174640647,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϪАƨ҅ӖÅϼӳBŠǐǒӦӘ÷ϔ˚Ҹˬ˼\u03a2(Ӡɖɐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǉȇ?ęÝÕü˯JȻƛ˳Qôǭ\x91ƑŬԁѽԊȒњȂɁΔ҇Ѽơͻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.895953:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽǹʲЕȔϮƊӶb³ͳҁϖžʄvƳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʩʺСʄɾ\x9cʠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҍ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ňđxύϨѸϥ¨ҍæјǞ4ͻрӸÏ=ǡϾÚəƣ\x93ɖѰԥҰǛʱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ţζȫºǩлm\x7fӖ7ǃӂϽΔ´ϗҚ<ʉgɶМÒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŐƏÊɪϠ˚˄ТͲбő;ҖϵŇƞ˩ȴɅЯйϯШÆІĝÞșϺο',
                            'message': 'ԣӀÊ4ϴҼÌĦӞѧσͻȊӤҤΝŲǰʗŞɪ˦ԧĳњ\x9dȳϞіҫ',
                            'arguments': [
                                        {
                                                        'name': '˜ĚͺʂӺΤˈӷ4Ҳǳ£΄ȓĳ¾ĪžãɐɜҌƅ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.897112:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '϶ƓȧǄ^ ˢ\\ĞҌɛͼ\x8bƘPԟПǿŝͷӍ²+|i',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѧϹԮӣƵ]ȚȚĸʖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'цґʏɒΫÕԃĳӑҬӘǹˍÔǻ¥ӁɕҷɊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '·Ӊ»CΈԧľ\x90ɧʯƍā϶ȏϭҚӞҟԇʻԏұ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђˋΠƇǶɰӀZ˫jɆҐԤυ=˼ǉƞЈӺэƴЈӼІκÍϏ˜Ȱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɻåӑǃłȥ>ΕұǿÚфÁʪĽʘҢƏӸƉâԙīҊвğ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҥӕ\x91ƛԘ\x98ɞҟƪɪr\u03a2ѢƾȓȑʽԜьȆŘ\u0381ώύǡζˇϵÀє',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǲɝӤМȖĤƼ£ѷΒɽйǥКɴćȊ\\˟ĆƑˍс_μπјѤѷѵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'џ҂ȍΕ(œӌȚӇӜȏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.898495:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '1ɒӱͻVÞЫ\x89ˎϒʶƆɟΝϚ{˥ǲʿԃźːҔȞȢuʲș˚ԝ',
                            'message': 'ǂĜ\x84\x91!ǊĞǕǩǇ¹Á\x87ЌǊʇʐэȜǽɻțɉɄƺʬФСǘã',
                            'arguments': [
                                        {
                                                        'name': 'ϙ˖\u0381ӷΉ+',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '϶ϊСʏʫӧӘҗͼǾиŋĬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΔŸСƞҧʌѿɱÐĆϺΙĆ\u038dΨƻѨƌÝҵ\u0378ѩđԫȳʵɷӺџϊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӹљұĺΏʇͱӾɎЋÆͱрɬоGʩĶʛʝȈʕ÷ƾСѣÀ˫',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.899195:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÊŹԑѼ9Ț7Ӱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉɊмϦŜsιŅΤӤƇήȕҁHӆƭÁғʎЦҬƎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.899557:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʳΖϖ˒ψӁԩĻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.899691:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˶ώԠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9aƥƶǌȾЮħГξҀѭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.899938:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѢɛӈĂĿ˰Њ\x99ɡǘĀӾȹуϱДԥkʩĽǌ\xa0ȪӇ×OԮҹʙД',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭƵЙҼŗĎȊȟƉǳPI˰ǶĸΛĔѿζѦµΰȑʥǿˈǘ˙ʽƝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.900245:+0000',
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
                'identifier': 'ĎĐԡѱɔ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'QҮ',
                            'message': 'Ҭ',
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
                'identifier': 'ÉͽԅüԘԦњMdħΪȕӚɪʛͷϫеȝɽӜÎͳȏӔǼş\x85łш',
                'categories': [
                    'file',
                    'access-restriction',
                    'file',
                    'access-restriction',
                    'internal',
                    'access-restriction',
                    'access-restriction',
                    'network',
                    'internal',
                    'os',
                ],
                'source': 'uд˩θĶϓƗíȉ÷˚Ƌ\x8dóφӔνξϕаЂȢȊƴγɪәɿ\x93Μ',
                'messages': [
                    {
                            'catalog': 'Ƥԡʪ?\u0378Òʘǋȕ"ѸĪʽǮɿȏӢǵˮԀ$ԏūρƞ¿\u038dк˦ƾ',
                            'message': 'ʕ˻҆×Ԛȍŷ˲ԮνʦеńЏϰȲҳԊԙԋ|ǯ¸ƠʲԠħԄÕȑ',
                            'arguments': [
                                        {
                                                        'name': 'ĪҔßǷ\x98ѺǭɷǓǥÊbˌȇĤҎҩoӫËƚǌ\x91ӱØŏƱȦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƣ΄Ѣ϶ą~ҭԇʤŏǙŃ*Ь¼ŏżȟӭȉŏͺƋȯԢȰҢωɯŋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 789315.4442335579,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ū\x95ԚȸŚˣʧɥ\u038d҃ŝΒλ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'έśˏ\x80ćǀȵćɣíȄ±\x9dИεʊ|ËʜÒŝȯ¯',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˘ďY\u0378ɴ&ћΆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҇ɨʒфԌĩόƾêɮʠԚ˙άŮΖʞσýѷtϜξώɸʇAҞ\u0379Ĥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Īƹҗ҇миƱ҃ȗȤǡżˉȧκǾџѶѰͺέэҗǫҫϙӶ\u03a2¯ˏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x91фƪӤʲԞҜȡҶӏӽÌԢҦŇλͿєȴ˪ɶĶľφʶƭԚҋĝÿ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǕŁВ\x84ҁdɛœlˌkПίҗЀʥҨ˶ŃʛҠԩǱŽƻɓa\x87ă#',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫέТΉǬϞ}ѺIŦŌʝ¶ǨàœɁϖњҪӊ4Ĭ;˵ȓέǨҠѾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԏ˷\x95',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѹHƝɻ˳š\x89ïȍʈϯΘӂ҆цӣѣŜѾԉԘЙƺČȟӼƐ˔ƤѠ',
                            'message': 'ƸɊϑηԤȧȰɉĹϩȾ"ͿƪȧҜҋˑÂѲoҎǩàøƭɶŲъӣ',
                            'arguments': [
                                        {
                                                        'name': 'НаѤȲοğďʀƜƃj˲ңſϬˮԙӋɩԓĚŊÑƩȉȪΦÆ\x9f¾',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'AϨħ÷ǰΉɅÖƲˣȲҟҢҥҌԐȧˈ˺ɔҎӂ҅s˧ɘџiúʲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѺӿĉĽǪӈԋˮ\x84ӱ\x83ȋʽԇΧʦӧԪϋšƵȱьā:5ΠШʻŉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1034586391603891734,
                                                                        },
                                                    },
                                        {
                                                        'name': '˭¶ƢΛϤ˰Ѱβԓбŋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.928568:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŁȣѵYʼԓҧӊ˴ȕȴďͼԚϻƐʀ\u0380ԦÆϢϢӢòȳԥӍţϗƃ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˓˚Ӯԅ$Ʈʣ\x9fȨΊǎӏƂϖŽƅϬǊǯʇ\u038d\x9dʺ\u038dbɡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5574462025954489339,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌѭɽһ\xadȐǷɀϔÆƢɰ¾őҴƜLư\x9eó˜ȐҺƌ\x94˙ӞЖ˖˯',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻȾw˖Ҡ\xadȫƹҍЅ\x9aʭɥʹҵΓϑϭ˂Ǵ˫oҡϒˮȃǌΪҙɷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'íΊæɜ\x96ӢӓxÜƣґDˇǛĭәżȺéˮʉaƚφPǜȽÔĜȮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0383ƲÖ.ІΆà1ϚÛϡĪϹȺЉԧйĺϬƔøŷ\u0378ȕԥϓ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7021500962080796309,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҁƝԫϰâǶǨȜ˕ΦЕƌӢħ΄ӑԏϽØ\x98ɳƖˡĭ˥ǒXÍϦ\x89',
                            'message': 'ʹ҂!ōӂÂέ˾ͲŠɕҢɱã\x9aюͶȸÇɼγɘωÿǴɳΪƅ`ń',
                            'arguments': [
                                        {
                                                        'name': 'ȡѥпơеĥgʭԃґѠºţÓğɔҽʁcȉˆҌćѫrHͺΈԉM',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5503584745401054858,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽҊ\x8cÅűͽ(ǥ¯ѹβΣϸΊ˭єΞϼĘ\x99Ï¶ҳѣҫˉ*ʱ҂Ɣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8bƹͽaϩõˬщɡ×φͰĔːɿƪƧȪJǻέϕԜ хŜ ʪ˾þ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 382016.663624793,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŎЌӶȢҭʑɿǝƨȅǻ\\ğ§ŖɎƙͲΜΰɴʉϕȡȡѪ.à˪Ͻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǒ/қ\u0379þĒ|ƱȚƐƝƛϸωĦȟ ЖČďÖʆ´ѠˆԔϻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1665680375192341875,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛǾ˳ɅǇ\x9fѭԅѲȭɼʠɯҰǨѸN˦ΌҬѳ\u0379ȹÁ˶ƦŹϐɺ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 149858.69929369685,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϳӅӧǊӱ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6545469848387008509,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŗ˗ӈѵʶʤŬрҋϯĽōγ\x8cǳǙȤ\u0382πзäΘ¸`ġȼŵȂ¡˻',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 479345.0449221375,
                                                                        },
                                                    },
                                        {
                                                        'name': 'йɜŁŹϑōӤUюϏҐĻѦǬ&ʀȰũ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞ\x8dǜƈӰҢͿǑñΦɑń,ӎ˼Тϩħΰʽˍˬ.бǩȅлӷӫǜ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÏɍяѡѶȁzˡƜϴİ˰ϝɨéӑӽԫʛυΏӊˊЉԖѴeĄƅΈ',
                            'message': 'ӖˈʬàӦdjΌÊҿʎɭҫǘю;љїÜӰǾ˄ҩɗЛċŀŴ(Γ',
                            'arguments': [
                                        {
                                                        'name': '\x8bнŭÉ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƉԖÕ÷ьƜȵέʇЭƢϧːċѳʴԌѾʨĀӎμ\x91˜ǃˌʡ\x86ǢΙ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧǓİ\u0380ȵ+Жӓ˩Ȯǫĩ\\ї»ӬÏƩôiыƔΖϥɕ1ѩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԋɃӛԚџʠŒǵʴǍˁ!ѵǯǫ҈ɭӰãųӨӬ˩ͲД8ʒƎǢɻ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ь˹ѱĚ}ЫћйԇɱʗʄϿơάҟɾҊќϏцʚĆΈȴԄҴћ҄Ή',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĊΗȑƿœџǃӂʭԫӴǂəϝÉƦìэђɽɤǒҚ\x95ôԮmɼͶ|',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҞǌȗƅβΙˍ˦Ǵż÷ÌҗӋřʅ\u0379ҳȚ¯ɭɰ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.932165:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԩȤǘˇXǕюэƟŬÈóϑƕ£ӔɘЎʡßѰđŬʺ;ёɮĨҜϊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƨŨĩԡӖŘ9xýКŒѣͷђκĥ˘ȟŸ\x92ԀèЁǵԂÙЇɎӮѤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ìϛ\x8cŨɵгȷȫҍįϳӴΈƙѺȁɕпǺġÎ8ȇʪCĻɀŸДѡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯƍɽǒŽӵŵТȃʠĔΗƢďȔt1°ɅŎĽ?ʜӚƙƤԑΌҠò',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӏŒҰɭӒСŲјиІ`*ӴƐϓ\x9dɞęĨНÈΠҬЈ\x86ƷɿԊԞϨ',
                            'message': 'ӄӝ¾ӔӔЛŏSʚӺǾłǈÿÆΫůҲ϶įɕʒŧ҂ҹĄĄ-ȲȆ',
                            'arguments': [
                                        {
                                                        'name': 'ʕ˘\x87ҶȚþδЎŌΟԦªѾƛ2Úɍ˘',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȰĊͷ˴\u038bԘR\x90вҷǮɫŔѢƶϜЍӛʏѬϭѮҤϭϑϯϴȞПũ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.933449:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '^ƚӳȂǗ4Ɩ£«ɮƶЛŷƎˁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 158392.49094579532,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϰΉǈͰшƮĺŊ˪ÃŖΘǎԄȏȨϩ¤Ϣ.ӺȶƵɨ;ɼžŊң¡',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҘʭѡƘȇêǌʣїsӄhΘŇ҄NȇÚˣʏéĔæȂǰĴ\xa0ѕΧ¦',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐǄːЧʦnɖанǋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵķθȮΥƼˢ~ΏŜ˳ǿ\u0382ƶԗҽ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1962930813998357613,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8fʣ϶ʳ\x90҅ǆƾƏĜϗŹRЛО˥ФЄ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΓJӾˊɮǈĖ#˱ɉĕǎӿÏԥƘ˘£ŔʬŕÔЙϋЖĔĄŕ\x85Ԋ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕȪϓ§mσӌ>ğӌΆшÕ£ҌЩԄęΩÓ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'N˟Ǔ5ƹÎџҪŢĿiƝλ4ŧѶӽĘȷȧ˘ǄϖɉǤЌɪƋДɆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'µӬĽΊȅδʺʜ¾ҭĹӒĒŜÔ_˪ҷĐzӂϒϨǅǩӹΎέȋʱ',
                            'message': 'HǇßʾ ˤǎ7ĶfфƦ˧¼ϨȳȅAϷϑǬʌǌĢЊǩūȽÂԧ',
                            'arguments': [
                                        {
                                                        'name': 'ʖɼпԊϪʢŃķ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˡ!˽Ďbѫ\u0381«˕"ԣÒ\x9aǋѬҜĶВǺԞĳʀĄϱӒԙ$˃ʃΐ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҖƜƶʆƛL˞ϓĽϱ"ȴǷ\x9bԪЪΗμʻɖѯϪɗĬҾѱň҆ɂǆ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 943492.0225965548,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Nξ1ŀͼøЉԔ˃ʣӜ҇ϒɪѓɱşƔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2071715016113595054,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΞӲ\x98şÞȶËȶˢǓ\x80ңҫɇwҸ҅ǻЌЫĶQʠȇ˹ҊӜɅͶ%',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.935495:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ãЧƘͻȔ%ȣζŴĹΝҜɁЉƨÇάҮҢԑʝȔ҄č҉Ӝuԩˏǃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æеҦrόǲʢŽѵI£řɗ˕çĳϹPǠʹ\x9fʌ¾ˮăƤӗƆԒЂ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.935795:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƭҼ¤ѰɄΕѣÖȯҘѾϥ!Т\x9cφːмĔɾЪgƲԀΨŞүɳǶƠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӳЛŐ-ζӛϤБuǋɸӻЊЉҐȧɍƢϫέԂϼ˹Ѯϋ˧җˊʗÝ',
                            'message': 'ӤžҥяʮȻЂͻЖɈ˴Ǉʔņӫǘ˔¡˱ɿɛÑǃ\x94бѓӴÅɉѠ',
                            'arguments': [
                                        {
                                                        'name': 'ԕϟ˓ѮѸĚ¶ŕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6385408279682631461,
                                                                        },
                                                    },
                                        {
                                                        'name': '¸ƈǃ҈ʎʀȀĂǲőd\x86',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƽ¸!ɒӱφ\u0378ʪԥŐĶɤοî\u0379ŢӰöɥƢůřѻμӢͳΜǄʿ\x99',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'τŬL\u038dѯԞŦҴѲ˘ȝФ\xad΅ƫɭч˂ǑˊHҔҒčaƙ˶\x87Έș',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.937411:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'уáb\x90ŃʎζfΡĐɷ\x89ŉίƄΫǖȓӸˇϨѭëԝĖȏƴΓÛȞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂӊŻʨӿѯЂϾȘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '(ѧɴʔϊČİͷμҋԛΌӢҩ˙ЂЛļƋ˘Ԅ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝˌðäX',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 883997.5352629325,
                                                                        },
                                                    },
                                        {
                                                        'name': "\x88҃\u0382ЄҳŨǕΚȒǜȌǡĭЋʡǫ7äӶ\x7fǺžÒ6'ŕūm¨®",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 817914.9601028797,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȧǺ\x86ѮӝэŉȔԁȯͽѪFʧǡȴԆ\x88@ҩáҋяŦšZɄϰԝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϴ½ŝȆïʪψƛï\x7f˜ϳѥôΟαНӋʑğǰãĲπҖКϥÙʘǾ',
                            'message': 'цѻŎԗȭҍӗҺвńԏǖĨȏΰüĻ\x7fťπʅÀҦǢëϱĤѰщȚ',
                            'arguments': [
                                        {
                                                        'name': 'Ŵŋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5864850724840808407,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĸюɦȁɠ°',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΡÇӻԣÙŵµßZͱ\x8aήŶΏп£ìÀ<âΒӚŎ8ːА˽ɫǐԒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'BŭĈƞƩӨƋƍ˚МÜ²ʄǴ6ϊϨЩϷѹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǰ\x87ѽɂƆÔИńȍүɁɚйґвӲĺƙӫôŞłюoǎȗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ċόɸǱԇϩσҞȶÏІζѕЈϢȲƯɕІɷˊʈʴƧǑə˰\x9fєț',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ӽ\u0382ґÄӍїŇǔӒĵʜƦ¼БUüÏҴǂªšɧŶѰhјőΨӵH',
                                                                        },
                                                    },
                                        {
                                                        'name': 'į˞ƣXy×є§čӯP',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҷȴß·ΰɶǗѧπҁӸĕɚңʬó',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸sʿ˫ɫѪ(ïǐmʏȍԇЕƁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6226335779977127870,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷӥĝƎĊʢŕѪҠʟ³ƢͰǉ\u0380ɻLƟήĨы',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 253334.62703762122,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȥŕκԡН\x97ǰыЛɼȇǑмƘԬŗĒɟЬŴĩ*҃˂/Ӌҳʏ˲ɦ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 914171.2604323712,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ШӁ˅шѸЙ˖ҹßTôˏ6\x92ѽŇΟѕɅæɏʓôǴƱ½ıĺʡН',
                            'message': '˼Ԑ˽ɝϴʋ\u0380ƤĸϕɄǭѹÑùýИПӈыa»\u03a2$ơм\xa0\x8aҽĺ',
                            'arguments': [
                                        {
                                                        'name': 'ŒȰϻ҅³ȸɱá˚ĬϕьϮљǉʂǀɤĠҰțdăħʛǎȸÁ3Ұ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ςӑŁǅ^ϐҼŻʴͼ&ÒвĶÇĹƚɤîʗЖеķө=Ȑ\u0382˱ˆҼ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠԚјѩ˧\xadѣϞВș\x9dΗ˹ĤӜɩ\x99Ƹˑ\x98gӇǫķǇũøόͷο',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7466513474154527819,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĞȚ҂Τ]ŁԠÌƈʡɖʽƚˁȐԕŮ\x88ɈʔʜҴʗΈś\x8cŬȵϠč',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǾĐѿc˟\x90Ҽāˁȉ˗Ŏŧʹпɧƴ˕Ƿþ¾\x98ˑʨ\x8fäҌԎʘȝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5710615791742396843,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĥҝʃ\u0379ʳșҥƓǘŷўʌΤӽďIÅtǃqјӌћӯvʁҊɎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑԀѨƨҚыȠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˼+óËɭѱČɶ.ҙєʭωÅˮǛǓȖĊȖ\x80ԗȢғˎțðϫ\x9fˬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȑτ%ʗϚҌĵǖǥΏ7ˆϬƽŔŴҭsϩʃЃɍ\xadԗhЦǩˑ4ȼ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u0378ӀǞʑ®1ɭҎƈś6\xadϭɇ˰ȖͿŇʃӞ\x84ԉǍ˜Ξԙ\u0380оɆϴ',
                            'message': 'ɈϦȆƣVχ§ЁȜʨ˂ȤǢĭ\x85ӎÞžӧѦŇӉìЖïǜ˻Цӿȱ',
                            'arguments': [
                                        {
                                                        'name': 'ҞɁƧɲŌǈ˾ȝұɥ҄ˤЙ1ɐϜ,aĴĵĦ˕ɺ˛ͽ˙ИɊ¦ӟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʓ҇șвҊɑжʫϮƞЀįhł\x8dɥĩъ$\x85ġýԀǍˆҪ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǠŉӘŷȐŰЏƤɤҢ\u0383Ә+źÎǣҐϲϹңπͰӚ˺ȿ\u0382ɢԨƘȚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҹƛʏύ}҄ĀǄЖƐǵϥέʾ(и±ЗˍԏÜ\x96ɡѢʨыӈȼ\x96Ǫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x81\u0378Ƭǳʅ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\\ʤƓĞÅ҅х',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 166160.35141537042,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˎƞӻӧӏиѶľþʻԒˇӒɸ\u0381.ȯƘҝЧƝƯđ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʙáĿѧƾw˛ӄ®қ3ĄψәƓϭҲη',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԬÂȗɢԞΞ½ĕǋ\x98Ϋ\u038diΨē¯ɈӄӮ˹ԧԍӃўԛȃЇͼŭʹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕFşҺòĩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '!ǎǸkѴԛсɃ*ͱЋ/ԎЈÑ˙˹Ҩɤ5İú',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152856.943654:+0000',
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
                'identifier': 'ǄŤƂΘȠ',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'ķԡ',
                            'message': 'Ŕ',
                        },
                ],
            },

        },
    ),
]
