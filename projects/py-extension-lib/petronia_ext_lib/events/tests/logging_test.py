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
            '$': 'Є¢˱´ϽˎŷԍȚҤƞǌϼȰŃҝϮȐœġҏʚӇфŜʲϹ÷ӧƥ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 6001861139746000912,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 82815.12754069117,
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
            '$': '20210413:002037.626275:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ԁΐǀѭϛԓ\x9cǵµİͿӢΕ˒ȢлМԩѝͼԅȯƆƸȋȩβε3ɻ',
                'ЁƯѹRIƑ4ш§ȹэǑ<ɞȬΐÛԨĚҚͻӺΕ\x87ԁŊˁ^Ŝӂ',
                'ǂ·²ɽϔEȖʀěğУɱFҒϢOʈςçȴοҴşƘ>ĕ\u0382ϗмĜ',
                '|ЃQŗҕ˰ýʽԢЕӓ]Ǣ˳ʒǒǥҥşȈˀΨƵʀťдƏǱґŶ',
                '\u038dŶºǘϟЗŝʠġыϫҒ\u0380ȔʤȺɯнďÿżӰʩ˱ӧƴʹϿoÌ',
                'ͽıϔɬԭˬǞūԕЅȶμӄйɼҜƁɾěšÅǫǗ\x98ȷćȱπ¡Ԥ',
                'įš.˻ũѶȬvκƫɔƂӦʤӰŜƞåăЯĔ;ʻǈѮɒϓʚΦϝ',
                'ȄxđҙɛpҤðʰƄǅѸ\x92ϣϳЭԖʌ;ѐɓέϓ¥ȯ1ȏе˨ә',
                'Тϋʇӎ¿äċÆԀʦʿԖȵ϶.ɭ,ϘӞˎԑöѩƂþĴεӇҞ\\',
                'ȿ\x8a҈[Ӽßv\x88ѼıӍԪγʥϕȴèͻǄΊ<r\x8bҕ\u038dƶҥ£\x91ӳ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                4530180318526331991,
                5747570630197145969,
                4759272098282907637,
                -2994484246391471951,
                -8813778531894337255,
                7255806649884883895,
                9111441928356813044,
                389266131370728685,
                5689072200101259603,
                -472080148034462395,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                723260.9474453579,
                476255.5621956865,
                830095.6147965194,
                656062.7479081744,
                17344.70080249413,
                847460.0409206544,
                -80524.23770537914,
                831410.7606071221,
                831140.6093820523,
                620829.404643488,
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
                '20210413:002038.592343:+0000',
                '20210413:002038.609114:+0000',
                '20210413:002038.626893:+0000',
                '20210413:002038.643716:+0000',
                '20210413:002038.660703:+0000',
                '20210413:002038.677568:+0000',
                '20210413:002038.694731:+0000',
                '20210413:002038.713341:+0000',
                '20210413:002038.730221:+0000',
                '20210413:002038.747478:+0000',
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
            'name': 'īđΟĝÉ\x8cȇCҼʑϼ\x9aҢТӶƁʏÆӕΡŽˉ',
            'value': {
                '^': 'float_list',
                '$': [
                    915587.530541215,
                    828511.3761188008,
                    832764.2078082615,
                    213702.47866778908,
                    -78649.62290313977,
                    862720.3071177141,
                    710869.1649616328,
                    895050.365243677,
                    800770.737496068,
                    563539.1267924559,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ι',

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
            'catalog': 'ʈǂɅӭ\x90ӛͺȟ·ϩжˬџϳůξϓű҂ϱĴeԤȠУòϖђϔр',
            'message': '\x86āǵ|ĩoʼӚȇеĊ3ɔɶÀō\x87ʒǎțƦǯȩλȢʎδȗȚʔ',
            'arguments': [
                {
                    'name': 'Ү˪Uˎɼ¦Ȁ˕ŗӠ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3385700150524102595,
                                        1545629299522766719,
                                        -2505793152770799060,
                                        1252840487296410633,
                                        6484014444079695442,
                                        9113451350533167802,
                                        93713218455675398,
                                        -6895796998167525923,
                                        -4345260440998335454,
                                        -3928440804963875812,
                                    ],
                        },
                },
                {
                    'name': 'Қ;ЩĴԬ$iĆȩƟ>',
                    'value': {
                            '^': 'float',
                            '$': 910156.8404725551,
                        },
                },
                {
                    'name': "҂ΖǴѶǩEԢӊǔǼȅČʑɠɢĆƜѿ\xad'ùӱʂÃǇɔ",
                    'value': {
                            '^': 'string',
                            '$': 'ДќˎŽѦЮɤЉɟŦ:EƣƲĔΗǩǐïǼåƌ˧&ƧƂĨ¾ʶʩ',
                        },
                },
                {
                    'name': ']Ѹɭ\x80ӡŻņѬǴĻмÉûʫšȡ¸˶˲Ӽ+ϕĆƠѷͽ҂\xa0\x87Ż',
                    'value': {
                            '^': 'datetime',
                            '$': '20210413:002036.091985:+0000',
                        },
                },
                {
                    'name': 'ѢКʥИşёZnźö˫ʏӴŪơѳŶɜӨϘζεȨǸϔϔ\x90ȮԆϖ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210413:002036.161221:+0000',
                        },
                },
                {
                    'name': 'I',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        True,
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
                    'name': 'ӄГʭёЖʒɐФӴǔƩ@Ī˳ØϊØʪĳɩӫŃȤСƒʶӼϕӀǧ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        2497251654714705384,
                                        3037829396007611028,
                                        -4438757509677827413,
                                        -6127163498268286827,
                                        3455785904504112498,
                                        3837851967809358021,
                                        5345909187127787430,
                                        5313661407959951909,
                                        6950721548830878584,
                                    ],
                        },
                },
                {
                    'name': '2×˩ĭѥΊʒÀρŁ\u038bƗĹМŃɬßŋʽ˅ȕˉˤƃшɹĬϧȎ{',
                    'value': {
                            '^': 'datetime',
                            '$': '20210413:002036.838666:+0000',
                        },
                },
                {
                    'name': 'Ńɠ˥ӷβсÏdǚčHɂ\x9cԘԤѲҞǻαȸȴő¶3ӏɎĚӄΰȲ',
                    'value': {
                            '^': 'int',
                            '$': 1148280809158886389,
                        },
                },
                {
                    'name': 'ǅϴҾџȪõʿƊ˵ÀˑѿӵИǯ\x8aѫR',
                    'value': {
                            '^': 'datetime',
                            '$': '20210413:002036.988811:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'пέ',

            'message': 'ŏ',

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
                    'catalog': 'ĠȨϥВȫȭ\x9fЉϞӆӶǓĥĥʍΒYŗʹEϪÃãÐҐʵΝʶěΪ',
                    'message': 'ʲԁϏÝ(˂ĳȑ˂rӢȉǗҖʇŇМδéɍȷʵiĚı҄ԑČɱΕ',
                    'arguments': [
                            {
                                        'name': 'ӲőЄ˥YѭёъöЙʽɉҜԆӢ\x98ǐŒцѿĿÆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŮǸԗȁÄöϷϿƺƄҐɤȵԙJŀȏӳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͼʌʱ\x9dқȖģѝɿҼɞǶϊ¼ηѳàAӕžϕӖΘ҆ϝзΚŕҗӾ',
                                                    },
                                    },
                            {
                                        'name': 'ĤίѾȻʿǔш+ΙʿҼ˾ȶ˺ɈʦL\x90ǽΏҔә',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɩ\x99ҶȝҟѱǮҗʪŽȆÿȓoēʞɹӜǟΏŤŃʰʹ\u038bůĠ9\x98Ø',
                                                                            'ȅҍŜΖǣÜBʤѾgɷˏ\\ʁdȑΏǲԃƼԟΑ˩\x9dӑĄѦʝҫʉ',
                                                                            'ȟøʪй˥ɓыƇаҠɛδ\x87ǫѮƂΠЍόԆѐȗÅ\x90ƾŔɲ\x9bɡǣ',
                                                                            'ЭÑħ¨ɼҿЩѥӾčÁĴЎƞʼǛƚɇʠśã˦ԎЩ˧@ʙ#ʧӧ',
                                                                            'ʺȒqѾҜȠӜʘğϑ˛ģуĨĎŢиN\x93!ɅʣÖɷδʁƌҗÙ΅',
                                                                            'И\xa0¨ʛ˸ŞУĥȟŧɉюѶіЉ͵ÖǝӰӾ˳ȾɻѠ\x8b%ǧ Śø',
                                                                            'ƾŵΨŀkȩƬЫϐįʎǨ6Ӣҏ\x9aŞǃʂƽнҦβ=˔vɍ˺§ǚ',
                                                                            'ıǻƐƸɧҔӗŪȸԗѺѷİťkǋӌˁå\x89ϸǋ¯Ͱ\x94нϨŹ`\x86',
                                                                            'ΗĄ˙iϞŶʛӺƠʡĦŰӇһϧӳҤԔȸūΰυхӤМgȓѡҞŽ',
                                                                            '҃ΕώϣʓǲάǛŏǗ\x85óǐÚѩ˛ĎԬϧП3ѻȧш_ʹΡԗĿþ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӿĝкӜ>в$ǍǷ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 958323.0473189682,
                                                    },
                                    },
                            {
                                        'name': 'ɰζN˘˦Ɠўǉˍ¹ΖAҢӜĲɚԎ\xa0ʆ˰ʕɮǅбїÎηɕ±ˆ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѧӌɺԄƧɄó˽ưǻɥŀЩd×ŇԆŰǲƀ(εȝԚрéҾçӄӉ',
                                                                            'ģѺɐђԌ¬ÄĜ©ɸǃ?ƾT^ҺȻȧ\x8dįѣ\x8bƵĵӨǽrӘ΅r',
                                                                            'ХǀΏɊӄzŁĶȢϐзɴԤȻʈұȒϑԩ¾ήЃưӘ˯uԨQˌȈ',
                                                                            "ӘпӴʺȚЬ'ѼƯўӟѴςXΛǏƥũЧ\x82ǹαƬĿУʬѢΔϮЦ",
                                                                            'ӝˉȑΊ\u0381ɔŹЇƀВ®ҡŬǕҝҺŲţϜłŋ=˂ΗӚРƲȓƄʼ',
                                                                            'γӨ\x82ȹԈΦ\x99Ȟşї8ʁӜƕűʀϑmˎψɀѺʀɰћͲ\u0378ǁ£ʉ',
                                                                            'μ"ćƄӁƐĥҸБɖʡ˚өϊ˧ϧхзԝԧμԆʙƅ\x8aȢíǰſƠ',
                                                                            'FΟ{ʃș\x7fϊϏœӤɚМӎзˌº҉fŻΜȒͲZεʆȘǭԉӖÄ',
                                                                            'ƕ!äαɣѠȢϪ\x9dɗοǡү˨\x99ț˦ͽɸ/ӑ÷ʞüїҳƣΦ\x92ƛ',
                                                                            'ʒËʹђÀ\xa0ʬǾ˂ľ¾ɐɬǙʘtҸϐɭȔɼдɛȎԌϱĈҙȭҌ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ')ʜƙҶɜΗȕªÓʒýҟҕ^ҞχЏ¶ѠƆˡʣԪǺєÔп˱Ѯɍ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3970568034296621700,
                                                    },
                                    },
                            {
                                        'name': '˾ŚԐϖˮý˺ҽʳľҰʢӐù˔ƼӅӓŶ8ǇϊуɿǍůнπ%ф',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002019.370992:+0000',
                                                                            '20210413:002019.386750:+0000',
                                                                            '20210413:002019.406916:+0000',
                                                                            '20210413:002019.422795:+0000',
                                                                            '20210413:002019.437874:+0000',
                                                                            '20210413:002019.452765:+0000',
                                                                            '20210413:002019.467878:+0000',
                                                                            '20210413:002019.483696:+0000',
                                                                            '20210413:002019.504351:+0000',
                                                                            '20210413:002019.527022:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ăΖϼԎĸϔԋǈűɀͽκ˹ʬҚшIҴ˲ҌҀÓƿϴƐŝɴԚыМ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ɩf˷ĠȜ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 389450.4339218242,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҥί?ȠӷȘȀSцɫȽԔ¸΅Ƥœä˯ƇÌΕÂѮқѧˋÁǢɢË',
                    'message': 'ƆʭųÃʬϴīТΧŦĔҕԚ3ˊѝқ˵˦Ҫϕϫѱ\x9cŻѸϫ˘ԗȹ',
                    'arguments': [
                            {
                                        'name': 'ÚϞ\u0380ё',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӹͷƺŔ˕ĤРэөԙŹ\x95ʼͳˏʱĪˑιѩӟкӠÌԤѵķ®ȩϨ',
                                                                            'ԡ˂*Ɇƞˑǹ¾7źƈȟԋȗʴ˪9`Ư҆Ϊ\xadХȜ\x93Ԣ˼Ҵϯô',
                                                                            '8īɦ\x97яӚѻЅҶǞ7ȮŤЬȕҤå\x8eżҩϿƌѰ/ϝ»ʼјLʹ',
                                                                            'ζ˧уŒӎМĒҢЅϨϘѕѫ#ʼӄϳʞŵĴЕҢӈң\x88ǦӲͽҵř',
                                                                            'ĨӣòΑ˫йǆšʊýɛLίΛϭƬǏʪƛĔϑΆѫӋ҃Ĕΐ)ŗǳ',
                                                                            'øо҄ʔěРϧҡș˗ʸӗóо\x84ΠǳӁȝɒφҜј\x86ȘÈĪʿҾʫ',
                                                                            'ԍҾϾʰƳҎи҉ʖ˷ԜԑɽÊɢкğTˈӡμЬƆ<{ЧҢΉʜҌ',
                                                                            'лˍӨЁƵ˱Ĺн\xa0Їɏj˘ҎӟÛ³ŇҖ˼ʐѮԢȚ˕\u038dӛњЖȚ',
                                                                            'ϱíʸəӆŇЄӸωϲͻ²ӖÉśĜɂԑŰƅŶŃПÈǤˋǻ*ʞ˔',
                                                                            'ȑĳȐ¢\x82љˮȣϡȋȬĹ\x95ĔпKƯǢƞɃÛǅϓθǊʮѭЉǠϬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѯó˨4dκƝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002020.155335:+0000',
                                                                            '20210413:002020.175362:+0000',
                                                                            '20210413:002020.191915:+0000',
                                                                            '20210413:002020.208526:+0000',
                                                                            '20210413:002020.225371:+0000',
                                                                            '20210413:002020.241656:+0000',
                                                                            '20210413:002020.256617:+0000',
                                                                            '20210413:002020.273779:+0000',
                                                                            '20210413:002020.292019:+0000',
                                                                            '20210413:002020.309808:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ú\x91ĮìʷɝŗӖ±ԀŀƕΌĩʤĘĹŘњKȲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3154658828570922416,
                                                                            -7877903123634914770,
                                                                            4408933375566394653,
                                                                            -5351083461610137595,
                                                                            -7430554906222780027,
                                                                            -429273593918287024,
                                                                            -893596487293442675,
                                                                            4100368685553197841,
                                                                            5383244685419678978,
                                                                            -8882764277457140508,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȽæƥŜØΏ4ŷ˒ӵŹȢīӯ\x85ʊƦӾȍҰФǉŠϐȳĂŭʭѾɮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'X«˽˼ĜƻÉýʯĜɏȑǻӶό½Ԃ˖Ð ÏZKĂȋőŉɳўң',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002020.726767:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҿǢ·ˁγ\x9eѯªΈ;˷ӋщʑЧГ˴Ό/ǓϢϣ҇ЎŦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x95ǢϞӷɁɻΖĥțNŨϏцƏȡǢφÍ©ĠɣĭˉʆƊүΙˌƖд',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ӣ¶ψЮ҄ѭϗι',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002020.943215:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÔϣɡϻZ«7Ľϕιɢ\x91ɱωg^ƐƣЭʳԎԑƋϒ\xadˀ˓',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӜʺЅȡѯǻģƳϣBȹǛ³Ԍģӿ_ɀΓΝĳɋ\x80ȣΤÊЊӠƑӲ',
                                                                            'óXǟOҌƼΫɾʖǝƣďѬƢϪӞю˝ôԣȜɕĴ\x8dҘлβҌżͳ',
                                                                            'OЮȟĴǥѾ\u03a2ӭǤĉȀӉȻɲņѠВāӸǔ}ӮҼӎѥȀʸŮǖ\x8f',
                                                                            'σǔкËǏʎʑӥɹőƋΌǮˋΠ˩җĕƔВϣ#Ƌ˞аЪʑɞҽ\x86',
                                                                            'SиȘʴƏȠͲĭҹМђɰсȈϦ˭ӌɁļ\u0382ƈ¿ӳȚōŸ¤іXё',
                                                                            'ѧͰԩßѫļ˼ʽʹǳť@όԇӊǾÏčťCʹζŎҙͲßҡǫĭҥ',
                                                                            'ˉˇɍдȍŃƳģȠǜǟ=ʓʚĪӎΕϮÅҡϑÜ¥ԆǰҵƓ\x8eɄǺ',
                                                                            'ЀӣZUĞşͰʯƉ;ĆҔɎԩΛµЀǴϧÃΉāҰüƊ¯ϸȤǅӶ',
                                                                            'ǄĄ˯ŀξϝȰϽ˩£ˍţҳΚöąµǯӍȐѹĭȬ!ŝԑȏΪӆӿ',
                                                                            'ǕĢϾĀԢƴĵϴ˰ƌĳ\x7fÌǔ¿ыȱhӣɱШęϡ˖Ӷȫ$ȢȾê',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӗŠκɖżtĔЏkҧµƃǕЄ±ěXčɗƤѴΛЁȩłÛҭѱŘʵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002021.279887:+0000',
                                                                            '20210413:002021.300144:+0000',
                                                                            '20210413:002021.340732:+0000',
                                                                            '20210413:002021.398795:+0000',
                                                                            '20210413:002021.419263:+0000',
                                                                            '20210413:002021.450085:+0000',
                                                                            '20210413:002021.469913:+0000',
                                                                            '20210413:002021.495432:+0000',
                                                                            '20210413:002021.516149:+0000',
                                                                            '20210413:002021.536981:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǁɫõǵƹlɔÝʉͶ\x94HŮôѤSͳÑʃȬˏʼԏɎҢXԖ\x97ƮӔ',
                    'message': '˙ԩʕҚȝґȼ˴ƇƮŽАʻӤɓąӹķ˪΄χɋʒȊωζ\x88ƬбѢ',
                    'arguments': [
                            {
                                        'name': '˄İʐLɃʱԗAğЯʸѽ\u0379ɅԓϩԖԁřә\x9cǺЊ˙¹',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8336349802647478216,
                                                                            1818319843416907574,
                                                                            6570429713614307361,
                                                                            -7938073322127479565,
                                                                            7378978500235161914,
                                                                            5641914136753772324,
                                                                            3064052052116174584,
                                                                            -6361876872193498987,
                                                                            8249797757290740618,
                                                                            8970530298825859959,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'IΔљˡϟɉРӞǪǱŔƀϖ®żѠЛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002022.030987:+0000',
                                                    },
                                    },
                            {
                                        'name': 'iƙɞë\x8bѸх\u0378ʄЇĂĤŧԬ\x9fԐԫϛǕԕĭŷЏҋƚȑʓ²ȑϛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2782675955368888409,
                                                                            8047548222070639505,
                                                                            5282409862263525103,
                                                                            7747561278569311733,
                                                                            8103955842850618942,
                                                                            3056613977378209456,
                                                                            7417731244442732087,
                                                                            4845004987664627686,
                                                                            -318582895491429016,
                                                                            -6403702443679504438,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'βƗɮуͳӌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002022.365101:+0000',
                                                    },
                                    },
                            {
                                        'name': '°Ŷ϶чӹӊɭƔƭа8ҵ¥ӟɾҳНҝԁȘ\x96ϦЀlĜȁΛЏ˙ȷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '³ԗǸͻπÑ¦Ȍ\x8fIɿɖˏÁɦԃӘȀˊƛƚʭ¯ѝ˪wшȖȲ\x81',
                                                    },
                                    },
                            {
                                        'name': 'ǫőmǨҔԅьʥ!ρ%ɨɞйӏȇвөЫÌӟEѯϤɘǱƼШϩÏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002022.501441:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѽÃȮĪÑϨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ˊгѓϾӬİŐϴʉļďɢPϾȒɈΜ\u0383ɧɾiҤȮҔ÷ίΈ£ԇÒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6584663921915022528,
                                                    },
                                    },
                            {
                                        'name': 'ĄΒѵĘϡҔӰσΪ˓ԟY\x9aҶʛˮˊĬű\x9fɖѠš\x89ȚƚʊèˀP',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŘÐφȿÃԑѮҠ<ĈҁÒƶʱ˳ϊѥ@αǭʎǹǺ_ɵѸʈɵԛά',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԞźÛ˕ǺҀФҲʦ\x9eѯЂӾ6ʀʹϐԔѵ\xa0ɖӃπϠ`ƞ¬ǜźΐ',
                    'message': 'ɅǢɩЩ\x88\x9fɛͷk\x83˷Т҆˕ŵ\x98ê¨ԑғŐБԧь\x9e´żǾȼ҇',
                    'arguments': [
                            {
                                        'name': 'ʷþǧʞԓϧΝˠѤǇ{˽ʯѿˈůǨɚӯɵʜgЂg\u0381Ԧϩʡ>ԩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѠʔrԇԧĥΔˇú8˟єԘˁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϦƌȻµ˻\x93ЌĤʧӎǹɈǟҌʳҢʯɭƍ¿ǫӡѠȞС˼/Ŋʡɒ',
                                                    },
                                    },
                            {
                                        'name': '\x86бȍϚͼҙőˏʎȡ[ʹї',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4155699227401365949,
                                                                            -4478320591210039384,
                                                                            2378837279655084571,
                                                                            -120669133362244005,
                                                                            -5773875111963222178,
                                                                            -1648570015612100485,
                                                                            8580691410717995274,
                                                                            1878392683382988311,
                                                                            337012652202411799,
                                                                            1629917864474212910,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0380ԍÂз2ʈƴӢʼзѸ\x9cӓƧу¶˫ƎÒʄҘƛѾʹÊԦ˂đɆĘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 632517.2395576804,
                                                    },
                                    },
                            {
                                        'name': 'ƝǐӋü˹ÅԇȄљӲɅµlɹϏЀ˫ӅΠşşаʒвŴģʧ\xadϏϱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5730570462979486704,
                                                    },
                                    },
                            {
                                        'name': 'ԍɌƄčнǯǨōӘɠνµϰ¡\x9dǿΌ¸ʒƾǄǄμȨӓɔөҜӇҹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ϱӯĹΨ§ЅɆȐɯŜʾƝϳȂʣϚĹċЪÔưå',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002023.788232:+0000',
                                                    },
                                    },
                            {
                                        'name': '»ҽɻϱk²˗ĩφ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': "ԧҾєùǗђȗʙɏf'ȳЂ˒Ӫǹ˚ЫӭȲ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9058418226147277157,
                                                                            -5339132588329765081,
                                                                            -10975694335414708,
                                                                            -6182219560358788560,
                                                                            -5189235397170548162,
                                                                            4404254862171645700,
                                                                            -4937822409483949652,
                                                                            4114019210585170256,
                                                                            7967570953893166022,
                                                                            4825253892547961291,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҕŊȱԂŰ˽[æЋǫˮԡ˾М\x9eҺкͱЗǡ¶ɣΎԇҽ~\x89Ӳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7119035903926995843,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'џɺɄơɳΑȴьб˔ѬԘӤԬʖҞ˲ǐjѾ[Ɵ˳ʢԫˉҦҖ\x82ϛ',
                    'message': 'ѽνĢbƘвΡʺęҟҚʵÍ@ѱӊñ҇Ѽγ»ѸăĻʴğϗ\x8fȝa',
                    'arguments': [
                            {
                                        'name': 'ҴϴДҚɪЯƁΖŋÓɢðvčìӱë\u0378®˻\x8fƱψǙёԛѷŇɚϳ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 27606.609493095006,
                                                    },
                                    },
                            {
                                        'name': 'ρ²өǾɬϊЈȀŞĝĆɬΗǧъͿĄԩԞӓϸɹěўɾǤѾȠƩβ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŷǓ\x85ǥ˞ԌȌǖɖ¿zŕšK\x8cˮˍǥȓˋ˭µǱÏıҧ\x85ďéŇ',
                                                    },
                                    },
                            {
                                        'name': '\x8bˠ_ƃ˙зŹoʎODŜ`Á',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĉϋӂщɶ\x97˘˳Ʉ´\u0383ϳýҨđ£ԦɛȪ\u038bɭϧĦʔɤɝ΄Õưȳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            553177.9634624883,
                                                                            138410.72900860413,
                                                                            236890.58799942903,
                                                                            155914.6502793833,
                                                                            578965.1898664747,
                                                                            799891.7507842781,
                                                                            747501.8644418344,
                                                                            355604.6488413555,
                                                                            160082.67667436806,
                                                                            -73065.72153162838,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĺˬă\u0381Ńˎ\x9cǛŤҙʄΆΦыҺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5408289826519883057,
                                                                            -6993380218556655479,
                                                                            5214256252723470093,
                                                                            -3586740403610056260,
                                                                            8576423797772969931,
                                                                            497388711389618947,
                                                                            -2867288019632041551,
                                                                            -2676822324871499688,
                                                                            -7415705803485003267,
                                                                            5519508440084143469,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǼλŐҰ\x96ԂζɑÍeҦŵӎтӪĮӑΧȉYɁí\x92ǆҼă',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002025.277950:+0000',
                                                    },
                                    },
                            {
                                        'name': '}ĻŧΰʀQ˗ͶϯƼӳ]φԘėѴɿĆҧƤȻϯŔƠя϶Ŕųƌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002025.353401:+0000',
                                                                            '20210413:002025.373443:+0000',
                                                                            '20210413:002025.392060:+0000',
                                                                            '20210413:002025.409192:+0000',
                                                                            '20210413:002025.427825:+0000',
                                                                            '20210413:002025.448333:+0000',
                                                                            '20210413:002025.466110:+0000',
                                                                            '20210413:002025.484064:+0000',
                                                                            '20210413:002025.503093:+0000',
                                                                            '20210413:002025.525229:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'k˞ýčΚ˛Ҧ\x9aȳˍŒѽЏ˹ ǗҽDϷ΄ǻҾЊhХқ£ҿǫŪ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӌąɋƥӻАʴŴωęЏϣ¾ӌoȸ¯ûΝ]ǳǻҠҷπɅƭЌШǇ',
                                                                            'ԉϤŅɣʣï"ӸÚҚ±ˬΊYӛԪԍȝDèҲċ½ˠšh˜ɿqϏ',
                                                                            'нƦ˕Ŝȟ3Ǡ',
                                                                            'ʼԇМŧɐ´ѯϮȋFǐƣǳƬҋʌԪ\x85 ТȑĲȋăʜƑЂπȧʢ',
                                                                            'ȂĞ(Ħϙ±ѝŅԕ˱ÙȤјΐˍȫě\x8eÅʧУȃfɥŨȘôŮ˗ʥ',
                                                                            'ŠMȼԗΪï˒ðҘ»ȸϦȡͱqӖӚʑƠώɬ˧\\ԇԋρϰǻ҉ʿ',
                                                                            "ǥʕРöϖ'ēӯ\x95ѓЍĨr+Rώ>ĒǒόΎӃ0ɩ\x9eВӸͳόӠ",
                                                                            'ԄƬć\x86υMˁѱƞэԚȺͶӞҝˉ#_Ɉȗҵ=ǳЃ˰ąƞҲΐɀ',
                                                                            'ȃҹѣžЃ\x89ǢҬïΆҘǐљʼ.ąΨǥϤѣΎιRȨԟʲņԮӵü',
                                                                            'ź|Ìԥ3ǥǏΟİƲҼс\x9dñɖԛȀɒөȜǬӖΨҙăсɈгϷԈ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ğǀËĦκͱɊӋ¡Ѓ+Wˎɼӣěɩˁӊ\x98ϿőǿUȜ\x86ĠĎЧͻ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002025.863976:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÚӹЛԇ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'łQƆˮŚ˓іɏǦϹҟƎЭŘÌĆŔƄΌϢӱҰŧɄʂ˟Ψɲȡé',
                                                                            'ƃń\x87ƎАӚ˝ȭʯҜҬЫѱȄϣJԦɣҸɋЍΙÔҺ\x8a˛ԓѯȳȭ',
                                                                            'ͷĚɼЕγ\u0382èŽҏαϛ˔ԓвSVǳӶˌ\x8aɭяŊѽԪëΨ\x9cʼК',
                                                                            'mщѐԥԡԬяɬԘƬҙДԆǦĴӥʼԇǦďǤψƍƍЪԥėƹǅa',
                                                                            '¾ɥ˗ŭdɁӳäьκŽɊΤǺ¸ΦR\x987λĈϔƪҾВɢÎǺӽǨ',
                                                                            'ǜǞ˓ÃΡьл¤˵ǼҡΏȘϵЗƸčǬԜŰȒǁѣƝʨVÓɪӘŋ',
                                                                            'ҽϡЍЂģ\u0381¾ϔĶ\u038dåȦ\x9eéΒӘǴъ˚ȽЍωұŭҺѾ˗ŪƏċ',
                                                                            'à҉яҪΣȶp\u0380МҧȆǻïõ˙Ҥӻ\x9aԛɒ҅ðϩǦʩȂʵҚVǅ',
                                                                            'īąГĸçǎԘ´\x88ãģȐƷBɭІΦȵϋԗѱȃɮŅԜȀºǚƏϏ',
                                                                            'ˣʮӻ\x94ŤϚƭϖːi˲ԥ˜ĢЯ/ϾĬϬѱzʠȼѻ\x9dºíӆϻȗ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԢĺˏǸBйşҊ¼ŸӢϖǤūśCȅĒѶ`0ėБџŞ϶ϻѿӌͲ',
                    'message': 'ЛʛĘ˥ȠöξӹĸƛɯОŧʁԡӃL3ȭԟĮǋ˯ЭΆ?οâJǎ',
                    'arguments': [
                            {
                                        'name': '\u038dΰɴѴÂϗÓČ\x8fȿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002026.249330:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʹƃʽҴΏɫʮЌ\x8eЌʊΉȧăЇΚ˛źÂǌȅӨġīӜ˪LϏĥƄ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ÑϢҌҗǲƙѢʁΌ\x84¶ǚƒ\xad2ʢÍʚ\u0381ɾʤˈҗϺҊϳ˗ëԈæ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6656153223807997317,
                                                                            6258012373296252524,
                                                                            -1444541834272315117,
                                                                            -2514487507497082860,
                                                                            4817308973017154339,
                                                                            -3340755469199181945,
                                                                            4962845063207003376,
                                                                            -1230637170783806257,
                                                                            -7843297071193489332,
                                                                            4051341381067382744,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'E ìΌ¼VҺѿˈӆÙϿѿ9ŶЉŀШƀʹ˹ǠÁǌC´\x85ĐJɸ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002026.642478:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŋˍōϯо`ďƼǛ\x97ʣҹЧYÄѣÆÀЦШŹȆÂѪȾϮԎ:ƛǺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002026.704725:+0000',
                                                                            '20210413:002026.719907:+0000',
                                                                            '20210413:002026.734817:+0000',
                                                                            '20210413:002026.749560:+0000',
                                                                            '20210413:002026.763622:+0000',
                                                                            '20210413:002026.776935:+0000',
                                                                            '20210413:002026.790129:+0000',
                                                                            '20210413:002026.803847:+0000',
                                                                            '20210413:002026.818307:+0000',
                                                                            '20210413:002026.832304:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӂÙáʿȕ\xadŝӤqƾу%ԙľž˝ȎɤĘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002026.919275:+0000',
                                                    },
                                    },
                            {
                                        'name': 'þоţɷBүийҼ¼ԁЏÃӋϓͺǧȜŦ΄ɪȰ©ȇӯưӠȾ\x9fB',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŠήηąƁˍОћԥʆϸμưʭә±ʰĦ\x8aĕǀǽĐǼĎϞϟ\u038dëρ',
                                                                            'ƠɌƗɯʳѐ÷ʃȅƻεƑȥTǢHмǭӏZ\x88ҋ˯ӒӭДҰœҡӹ',
                                                                            '%ј*ϫҪӧʜϿТυ˾ȢǒˊȌ˨юžϳΑ\x9cЅώȗӜϟ°ԔeѮ',
                                                                            'ЀzİΓҘҠġȦӌĪȖѓԖ˒ǓŁҼ˪БӡʚǞÉЖʯҳ\x8aϝɯc',
                                                                            'ŜëĊ´ƀǃféɿӞɃώ\x87ßˆƥԏϻɏŦȡĔŘѓτиҚїǒ˧',
                                                                            'ĶӁͻӃΥë˛ŔϔàŭŅȊԎɾIιgv\x99zѻ:\x86ӨD^Ԯ¥ß',
                                                                            'ѸRφx"Yбʋй\x95Ć\x93ǑԄҰԑŋҤΘƞҬ\x93˼ɼѰ´³ʢӒc',
                                                                            'εҟɲȮϯчȭЖ°ѤŬɣ˝»ŕɇГ\x96рЪé;ȠƥũӯДҘʲĶ',
                                                                            'ƿŚȖŠԩ\u0379ǂûĭѦȼĚłǃʿĥλ|ˎɻяĦĘĵdmī+ĭD',
                                                                            ';\xa0őѱȫ\x92ҴȞԀӒЎɦңnǦԣ1ϴƦѽ҃Ӓҟʑ©ɜȁΗѓʕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Эϓɭ#ƫɀнҴđàǆнӌҿƊ\x86ˊ<Ϡʫοcϟ˃дϺӦŤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -721485924249945187,
                                                                            -60613904788604204,
                                                                            5485644325819722897,
                                                                            -1670587267548383262,
                                                                            445533224317239960,
                                                                            -1717502013622433660,
                                                                            6786402356908003756,
                                                                            -4066146495734975126,
                                                                            1315493157252020634,
                                                                            -1304703281986045986,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɑÿќА҂ΑΣϬσ9˙ƮúөнȬ˓ĥĜɂƉКșїЄŹԈǲ˩¿',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            230781264674425957,
                                                                            7025731335222670817,
                                                                            -7772850316155935822,
                                                                            797387226957836576,
                                                                            3558917243260924912,
                                                                            -550905691644143880,
                                                                            -2977078996173968623,
                                                                            -6753386686065659911,
                                                                            4962244725059416119,
                                                                            -4655156871136305286,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĺţ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2295311144232866010,
                                                                            -8273047503810127216,
                                                                            7027159738900343266,
                                                                            5737032216375612751,
                                                                            -8229183714265053325,
                                                                            -5229196853855945741,
                                                                            -5733683805052002158,
                                                                            -1845315556431276052,
                                                                            -3021599838256124666,
                                                                            1663117076379333796,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x9a\u038d^вɬĺɨĂ΅˦Ǖ˹ÕµɟͼӍΐÎЌɍª ГƞÒδLĦċ',
                    'message': 'ҷӓΑͺˎ\x97ʔ\x85гfέϖΨ[ɎɩnIύŉWȑgƊčÝΔӑӔƦ',
                    'arguments': [
                            {
                                        'name': 'ŨωзMϟ\x81Ʋǐǧμ.(ʌϔÜ¼˭ȘȹӆԋɰȺ҃ĹβҭÞǗѮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002028.073775:+0000',
                                                    },
                                    },
                            {
                                        'name': 'өƠaŚϤĸʺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3454242615874725773,
                                                                            -9006322424631693006,
                                                                            8663900489204970257,
                                                                            -4244635265357268668,
                                                                            6563309228181413878,
                                                                            -3497140950713731374,
                                                                            -7249234506306226940,
                                                                            -2615983459597346672,
                                                                            -715213517552739110,
                                                                            3474033914964731974,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԌϺҨϛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɐӊɇϲңɏѡ˪иëӮФȡΚԧŲ˪ΡΓˁԐϲΓǠӇå8Ӹī¶',
                                                                            'ɥǠˡŹ&ĿҴϭǩƲϭҊΟПǲɾɿʃǷʏǡԠԟʙșşĊơƘԠ',
                                                                            'ʠǞɴˌơʵѕǒψʮɄ\x83ԓɓҞ҇qéΑƷƇɌȖϋԏώҚ\x84\x9dH',
                                                                            '҄ђ;ɽ!ǉГĥЇʒŰęʺɩbČӡƟԃЗZȍςԓŋӽčþǚȂ',
                                                                            'ˊ\x84ѫ÷yϥ÷Γģ˥ŷЎǃԉBrΰҙʡƎԥ¬ŌÚ϶ϔȕƕȬή',
                                                                            'ßѻ˥бʒǝǉ\x9dĕʨ\x81ͿҺ\x87ȥѥӁќʙʭǉģƻ·\u0383ĥǛƿɀԕ',
                                                                            'ʿƚάҚ*ʥľϚԋFƮÀтUҭ΄ɷԭԭƺÞˑŜ§ҲĐҺϥvή',
                                                                            'ƜӇϛ±ԥ:ƴґƇĄˊǵɓċȁύȁԒˏʔǍŝɌ˟ǶƵƒ˚Ŏˢ',
                                                                            'ΎǩɖҴһʬҚæЃԖ4eӕ\x88ːÝϴʤԪȜΗœгƛ˳ɰН\u0382˳Ϥ',
                                                                            'ЉFŲƚɛˮHю¨ͿƐÖĝŵûů˛¥ңԋ\x8dӄôϧ$л˖ʲƾǾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɠԩtͿ·ɑϾͰ˔Ĵ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʳѧʡǴÂţʆƼ˰|М˱ͽĽɀʗȋřǺÈЭʻİϹӗįì\x9dÿή',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'əŲʌԀѷψĪŨ\x9d˷˻ċԎȭĆԮÝÿ×Ԗc\x9bѵɷԌ˪ȯ\x95Ä;',
                                                                            'ϥŲǞƅŕ˜ÇƎϭŅƘӥƷZ°Ì@ȇӀɯʏԨNӪHwҦʟԪԄ',
                                                                            'ƘǫнкʃìĎòκôɖȱѕʧ\x93fiʃɎΖɗǮǒӝͿʍ!έmÜ',
                                                                            'ӅzƌÛȲɨοԃʿαΡ҂¦$ƓȲ"ѠϵǛjǍzjʝĐ¡ǉӒ©',
                                                                            'ϣ˚ԫАɨӗˏɩПϰƼäҨÌǿдϸП˝ư¼ȗΥеѬěжԐŏӠ',
                                                                            'ӕ˸ǫŖǰӿ΅ȔюԗӛϤ˒ПԉíԐĠͳʊǰɞ¼ѝѡfƅȆ3ώ',
                                                                            'ˁҰӹШʩǣţǔ˜Њé\x9eÌÙ͵Ԡһѣʅ£ёѳŠІƛҔϓʶ҆W',
                                                                            'ԨӳƱ·ÙˀΥžʰʒū҈ʶӬԚѬѢǨËӼ·ӏƙǑ\x97ȌЖƋʟϏ',
                                                                            '˼ÛϧΓЙѩԨϠψéϞŮԫxАϛ˕ȉžʑýŖ˵ŪԢϐ˜ţϛϨ',
                                                                            'ФѼ˦JǣтѵОɝͳԇүӌӨȝrʌěÌʔԈЄИíƺoҲȂŧ|',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɀˬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 460387.7624742136,
                                                    },
                                    },
                            {
                                        'name': 'ĮǛ\x7fĻԜКȽӋňѣ\x9eÏ\x9dѓ^\u0381əƌѷЁоDԦȆŇɰϺϳyь',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002029.005843:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˀbÓþϺ7w\x9aе«ʏóʎҔʡǋëţģƪņʋ˩ȭѺ°˞ʣϭÔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002029.076633:+0000',
                                                                            '20210413:002029.094037:+0000',
                                                                            '20210413:002029.110748:+0000',
                                                                            '20210413:002029.127532:+0000',
                                                                            '20210413:002029.144160:+0000',
                                                                            '20210413:002029.162102:+0000',
                                                                            '20210413:002029.180091:+0000',
                                                                            '20210413:002029.197114:+0000',
                                                                            '20210413:002029.214259:+0000',
                                                                            '20210413:002029.231282:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '3Ōԥˁǀ\u038d¼҈Đ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002029.318030:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȴиȋёˋͶƧѼŌ6ɖʥÙИѥűŦÒȊԓŋ˝іԃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002029.386928:+0000',
                                                                            '20210413:002029.404142:+0000',
                                                                            '20210413:002029.421478:+0000',
                                                                            '20210413:002029.438494:+0000',
                                                                            '20210413:002029.456707:+0000',
                                                                            '20210413:002029.473639:+0000',
                                                                            '20210413:002029.491236:+0000',
                                                                            '20210413:002029.508679:+0000',
                                                                            '20210413:002029.527635:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˦ϬҫɡȻϧӊѩʌǽƅӎʝÉā˨\x7f˻ɦХԟϖλÃƼ\u0382ȟ&ȼʿ',
                    'message': '$ҲфƷЋ˷ЯͱͰ¡ƾȤ˪ӒɆ5ÿ>ǞϾǝҷ˲Ʈ]МʋĲćϩ',
                    'arguments': [
                            {
                                        'name': '\x9aҸΧ§Ҕԡ\x8fϯӬӉʥƢɓ´ð\x90\x96ʡȉʲъЂlĜҰǣʀǱƥʒ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1392864952495078190,
                                                                            -778550079226919663,
                                                                            -3479548996920834835,
                                                                            7574841887271995873,
                                                                            8358064744334180711,
                                                                            -1171110280010408644,
                                                                            -5791895737964673359,
                                                                            5778659608221731385,
                                                                            -8623459895989112670,
                                                                            1633218968914227141,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˢpƽŽȺ\u0380ґġӅцɠԅÏÛĒƌDŘЄΏԉҥҏ¼řͺƻ:ɿː',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': "+\x9cɫͻ`ōΰȭƊӃ҉IД'țҠË",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 374793.50616021827,
                                                    },
                                    },
                            {
                                        'name': 'М',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƎņĹͺſîƍѬĉϹ®ӠΗπνԒQȏÜҩˎĠԬßk6ƜĀҠ\u0378',
                                                                            '\u038bӜ9fÄΊńΔΈ\x84÷ɥЄЀ¡]ɪ&țϱaƭԇџӽʢΑӮ˗Ԝ',
                                                                            'ƸÍƈіİşŤјʳчғʓыʮˀȜǌV>ɯεωɕӄ϶Ļ¬҄ї˰',
                                                                            'ĘѱΊόƯπϑđĒˌǹȊҺщҎΓȿǷωœ\x8a¶˩Rұϋϯьńǻ',
                                                                            'υҎÐˮР2ʏˌȑƻ³ɆӞѠôϳ6\x95ɄϮˆͷӋԊԋǃӈʆJҭ',
                                                                            'ɃǕӽϕɕӀԙɶŐĎ˕ŵ\u0383ʒŪʉϒhԎӝƥv_\x83ǻҋʵ˅\x86Ú',
                                                                            'ĊОΊǁэɊѵԟМͽǤΗïûËıѕǌĮԘĤĔˆċćƹɾŋȯģ',
                                                                            'ҕҳˉÌɺԌʱ˃Ʊи~ϭǦĒp¼ͱҁԪЋΎȰԪǊӦйυȂÊΧ',
                                                                            'ǠñΈ"ɢ˸Ķƙӯѓ©źеÂԮwÅʍϻԑɛϩˈеǓËðtFӢ',
                                                                            'ʒ˃ņƛȔĀӻϦӢǉ#ȣµlĹɼăԝЖсϚԟ¿?ʋɋɥóʦɜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'MϵōȻІɛԈȷSǹӅԝ\u038bĜӝ·(ʲͽĵΥǑβʝìтǌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002030.288609:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĞȥυŎοǛǮŏӳy\x9cσȪΚѵȢƧΊ˕ŐƜΛù\x83éӮȡѫĭ˸',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            790121.970159579,
                                                                            263148.2449136179,
                                                                            -90282.97280151921,
                                                                            559728.968415828,
                                                                            210913.82315113425,
                                                                            173869.2871107136,
                                                                            836237.0795405698,
                                                                            195697.94029156346,
                                                                            665394.0806602667,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'XПҁʛͷˣȪ<æȕҗƄí˝DѼҭПҬÛ\u0380ͼƂƖǚþǁƅΥɮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Н\x97ԩacȩʏǞњ¯¡ûƤѽˢԢԌɠʰƜѳŠӪ҈ʗ]ǫØύš',
                                                                            'ДvȄҋˈћƍԢĿòн΄јʵ-ϴҟʘZϪԛȷϛƱǯƠŚҔŇς',
                                                                            '§\x91ϐϞͱ˵ЎLҕǲѺϱǋďΡʈӝӧдáŵчЈ\x84¤сb˫ƬЉ',
                                                                            'ǳɵˡmϿʴRеԎ\x82ӤƢΔQǠӊ\x84÷șѺqӕÚӬԫ{ђϠӒӵ',
                                                                            'ʏ϶ǿȺèƣƒĽӰΒvќſШɘËɱԖȁ\x9eȺʥĭԜ£ПƁ\x88ɥ҃',
                                                                            'ΌРFˀ҇ĔΥĩΰíҼʑüƴˑХȞÿȫҔ¿Ӳԉħ\x83ÛʶϠЂƽ',
                                                                            '#ƃ;ѕҀǪтǜÌɮ˹ӺJƌӨȕɓȣѲѓͶϿúΤҖӡеƙгė',
                                                                            '¬оϸϏӲțɆӜɣЊ5Ů\x91òӪŅʤʏ!˝ȠÙR`\u03a2˙˷ŋȄЭ',
                                                                            'ØPǩˬ˵ηƣѲ\x80çќĒȡåƩ©ľĈә\x90SΘɗáӥϧԇΈԎ¸',
                                                                            'ϟҙɉέȗġɃȐșяǘȌѼîǞΐΦƛťеюǒРԋϪƛϝɛēĨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɓʑŪԤӭљŲɥΎ\x88īʖȋͰΝųԛӜөɛθ\x9cǣwǳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϑʹsԝТФϤМЯéÞHĩϦÑϠMԋʌǤȾ\x9bȱ?ʏΞġÑϔǖ',
                                                                            'ЫψӪ˹ѾΑmǹ΄óϞԢŀʆˡɐͺӫɦΕёϱƽXπJӓµЅә',
                                                                            'jŵ(ɯɱ·ǙqϱΉϤĹɀȠʧЫыɓІċӍ^ǉˊλӡϖƌͺǐ',
                                                                            '\x8dòǢʘ,πϡâɡvŨpĉț¸ή¼ϭ Ҍ˖ЕѯІ¢өϦв\x89{',
                                                                            'ĝʜŦ˷\x84ȞιĕɕΠΘΟLӸāƵ˒ԅψѾ\x88ӃʻzɲԃǠũнU',
                                                                            'ÇќόрƎвɛɠÄѠΤƷɛОĹϑŮęҴɳřê˖\x92ƟɧԄàοr',
                                                                            'ЗυӝÕȚԫ\xa0\x8bǾԚфľ˦πÆӞƮ˟æΕэѢɓ΄:ǐO',
                                                                            'ҳЬѭΑƎҼ˅}ºЦϞŦË\u0381ʦůĐжȠɔѐJϭʦϺѴ˘ȑ;Ѵ',
                                                                            'ПӛBǜүИͿuˆȉ¹2®Č\x98p\x89ДϮҸЫӓԣȆ˘ƨһʺԗ|',
                                                                            'ɇíӠŻ˝șʒњÓ¶ҤӅżǷӏɬеа§;ȩȝξđőѨѲhȁş',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɮP\u0382Ãɿзʇʑ\x8aψF\x98˚1їӛĸԚĭʕ\x84ӫψˇԠɢ9ѴáĔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Q\x81ʎŻÄãͻ\x9fƍ=\x9aȕ¸ŕǈǱɭϡΥҳʩ˩˭ˆΔƕϵɩϢƊ',
                                                                            'ěѣͻϑƸǱïȞČŨȅƌР«њԎōʯŝуԢθ.˫ŐņàŸǪǣ',
                                                                            'зϵ»ȐĩͶŸƞnӷβђ˛Ą)ŎԒ¹NӃѶĂƶňԪʦ±Ӻ~Ā',
                                                                            'Ϻ˹ѡɕѶіǧţůӪƀʆσʓĠǘԀԥȽ¼ŠͿľҔжвǗɻǑ\x82',
                                                                            'ɷ\x95ʫƴΘâJȉȖумƻ\x99œǭˀɗĀћ\x8bǴЪUǹȇſȓȭц¹',
                                                                            'ԩŦ6\x98ɳӞƗӂǵīǒԘƔҽʷɭҠțɀ\xa0αĆɘqēÀζУȘľ',
                                                                            'Ȫ҅ȹ\x91ǗѻТӯЪɌ\x99˅ÌʅԛѭɽƱƺђƩϨΕΣǻөγΌөИ',
                                                                            'ȄɟȫǹҌǮӗhÌǠλΥ\x9eƼɦПl6ÂŃϝԐŤңφȾƬώЯʭ',
                                                                            '\x95˭ÏǉƷϨĪϹ5ˏФñДΎǮѤəЈшȔĀԑvĬʖтϯТ˄є',
                                                                            'УҺ?ҏǫԭԌϻˤϖʗӖmͶ³ΚǩάЈԜˏήƃƃˌʖzľQХ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȄƶʎчɮϚѭSEЗѢ»ąùŪ¥ˈǁԡνĎϿѢҊͼ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5853762572745220616,
                                                                            -6851034611179338634,
                                                                            -5287031993012250591,
                                                                            -4072699385648519465,
                                                                            -8111611550921534735,
                                                                            -4292390069077378204,
                                                                            436172320919275411,
                                                                            -935347119829564437,
                                                                            6524078524306387555,
                                                                            1051920678551418686,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'VǍǉƩК4оéΣĞƺƱȳŬ˟ҝ`*\x8fП)Ͳ˵ŮԂƯӫDǯΙ',
                    'message': 'у^ϯęɞ͵îӬЄΎǩǩȘ¢ƀŚфŷżϴƔҤǸ\x86ɐѾΘŕΥƮ',
                    'arguments': [
                            {
                                        'name': 'ǾЙ¹~Ƃ˫xљĚν7ǭԒҤȬʰԠʺΕϟŢķΞ+˚ƣ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ʀ΄ҐɵѫŚʯýωʙƖƥɹÇÙɖǖƠĳЮŔԂ¬ʄƔҷѽȡǌӲ',
                                                                            'Уԭ҃\u038b.ĉʆќ˅҅Ξ¿ǙВʈҢЪҫʶ˥ҍԌҁӹЪȫСˮαǻ',
                                                                            '\x8cԙǶûMYԖyɻЎοɪŠԄҚȽʲˀ9ѦҔɪɴǰб³ϦhҠǲ',
                                                                            'ԧČ˽·ϔҜʸңŻ7Ǉϝīу˫ѦϵҫƭʬΟĺǓCԇ˻ȷԍŘª',
                                                                            'ˑχӀȸӬүĆĴéˌɦrɨĳ˙ғьõ˓jđ\x95ԌӨ\u0380ҧԇʄӲҏ',
                                                                            '΄ӾҩǶɄпЛŊӥȠōʨѠЄƔԆ\x9bϒĚşǞʋªʲÌȯľΜɲ\x9b',
                                                                            'ØȈǚǘ×ϴєʨԇˡ\x99˩ǹ҃Ǜ˕ӣϕ˫{Ɋĝԟăʑ˕ѾПʳԠ',
                                                                            '\x82ʫȃëԊĝƳȦƴʪƚҙиĒʙԅ÷ʪӎńҕЋιҩƕìƜ\x9aҧǪ',
                                                                            'ȅϠ҂ӻәÆʦιVԆԝȝÿσƃJáƵή2ϼģɸȮƛӯȅΖԆŷ',
                                                                            'ĕϞÐžҵҌѥʎθʂάӕјøӊҦǻƨΣ¦ɄʩԚȷǓˣÚǥϔĚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ğȘͰɉҴНЕԚˏƟШ˵ΟԜΤЁǼΘҟǃļˠѭΏЦ\x80ɾȠԏН',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2290091786229634373,
                                                                            -7169189312945314429,
                                                                            -1136505447660208418,
                                                                            -2185280778616992380,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8bΐΞ\x7f',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѲƹʁҢѽԆŵƘ!ƀτʷȚȷĕʅ\x9bˈԓ£҅˚өEϚӧ©˯ʽԨ',
                                                                            'ҥƭ;˟ǷʏȻɘgȉ͵ԉӪ\xadԀ#҂ʝԈɥϚϸħʷѽȟæɖơю',
                                                                            '˨®ƐҺϗ˸ѶΑȇȵ{¿СģɠІԏίĀĆ˻ƝӡԆí?ϲ͵\x89Ǫ',
                                                                            'ϵÕҼÉÍˣDĴ\x9cѲԞ˽ϕӐʦтзĉĢǡʵтŷ˳HdːӕʌǛ',
                                                                            'ԐУţȁÚǌǵÈӃ\x9dɼҹ\u0379ñɣɽǙɿЪŪɫȽΥŷԢυƈ¡\x9cӞ',
                                                                            'ŇĂƙǤȪʍ°ӄϨӖɑ\x82ǎȄ½õæ\u0381Ă\u0378ƘΤxȁƨ˴жϽʨʭ',
                                                                            'ıx\xa0ĈΝʋȚ\x86Ƀ¡ӋўόȮӑĳοƣɖПǵǐˇҳǅӰФĮмΔ',
                                                                            'ĿΡѢˡю>ΆԮLÏƩ˕źĶԘü\x8c¼ɘɬγɆԠɼżȌτ\x86ǯΟ',
                                                                            'ӣĉPƑľӒǖĘƉĉƕİʢǨȮԌȪŝԤĆɆƶ˜φϗ҇ȃƲœӄ',
                                                                            'ƺЏȽԗϢѯÍǁʩŻȥȞÉƨτȡ&ĥʨҊӡÈÐĔƕҙШ˽Ǚç',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʋː˵ǓҭȝҞϸĠɳȻƑǀΦ',
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
                                        'name': 'æΪǧҫͺʒҔӽóŰԐρȗϟɣΗʌˮʉ˙ѽ˸ϩȿǞƐȐИӢÎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŹϒͶǄиPǝўƒ\x98΄˒ξϭ΄ԛӳǱ˶î\u038bӾĈʯáŭųχˋϲ',
                                                    },
                                    },
                            {
                                        'name': '\u0380мр¤˚ɻоϫZԃɥӣʾѬҗ˒Ωù.ǭΐҀеŎkћ9˯ˆ·',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ɸȳƑӻȷǞѦǯʹȲ˽˫η\x95ѫŬμ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӓѩɒͽϋɛėǜɎѐǐοȹϊ\x86®À£Ѽ_зѺʥʭ\x95\x98ŭȋʟӶ',
                                                                            'ïӽ˾ԧɜϏΕМɐƌӆļ҃ĵӣЋĒȡ ϥɖϨĮƻτ¯ЖЎƏǀ',
                                                                            'Ʊȡ˄ƇӏʦɺԤʽɤΟгΞƔӢцԎʷυʷˮʾрsԏøʑȧʛ~',
                                                                            'ƩËęɝʲϘëҺƖˆΉɆӧXˡĻѤЬӉҜŷ\x88˟\x90ƏŞɅόУǾ',
                                                                            'Ҫн;k\u0382PǿŭѧƳǷſ˳§ȅǎʫƧԦΑыҼιОɍгӢ\x82ЃΙ',
                                                                            '"űǕпTаɋѲʥΚǞğцǤж\x85ĄűυêȮϵǡlϗӂ΅ĳϖц',
                                                                            'ϧŨȘʄɅҩЂРϦǈϾƓΏӠȎűҽϘÐэǭO˟ŔΓωìʖИʹ',
                                                                            'ӃΕώϢѼһ\x8cȜ\x9bҪί\x88ьÇȝԖ§ʸЍɬϛ˥ρκxſҳ˪т~',
                                                                            'ȭƤ?ţɳљfˣGǰϚʿoѶǸϯF˹ĔѕӋ^ԞМέŬƄêȎπ',
                                                                            '¼ÛҽяāϹǘȬɣ\x9cèȦҎ˭îɒҎʦ\xa0\x93ǊɾƑʐα˘\x91ѕǔĺ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʈɪƽ˷ɈФ˼δѻſȎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'у\xadҿãϢȴȦΤңʃҏѻȈBβĚUϝİԒԅ¸үťuȻ˨`ȧӵ',
                                                    },
                                    },
                            {
                                        'name': 'UʠЕΎŒhJʂχƱǩȷîģͰȾɜɟӇѫǯ£ε˒Ƭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002033.136114:+0000',
                                                    },
                                    },
                            {
                                        'name': '¬\x8a˛ɘҫ»mьäҬҼԍ\x84ԮΐԟΞщĹϽΊɹӼɩϕȼđ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӆţȓ]NˁɍşǌɝϚӥuɚ·ЩɑžхʄɆρҷԞɃРʃːǨʯ',
                                                                            'ШѡΔªĿсѷ˔ɥΓЃϢƏ¨ǡ§ËėӰЗЉԮșưɹʤǨDǫŕ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʠǳӫ$\x84ƗҖɵÚËІ҅ǕҶaӆϹ҄Ȣ`ˢäҺΏơǁyǜǄԌ',
                    'message': 'QđȤĶʅȃчҀзʻŁ\x85ȍ˒ĐŐŖѻьÄѹÆ)ƎÕŶӬŉπȽ',
                    'arguments': [
                            {
                                        'name': 'ϯӅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            86229.62902056146,
                                                                            151594.42683683443,
                                                                            205303.1963734576,
                                                                            17589.01017198703,
                                                                            868753.3820245493,
                                                                            72307.08451314652,
                                                                            34291.33075306172,
                                                                            261897.7466687846,
                                                                            328468.04944735084,
                                                                            485494.1824369265,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '²ӊńãŁ˭хǓΐӚϭ˜ǯÉǻĲӢǼĂǙӕņ˽Ӻ\x8d˳ԫ˞ӿû',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8288352847361587061,
                                                                            -3980222405356684538,
                                                                            7363129487239977191,
                                                                            -3001362613906270021,
                                                                            6481410330480579344,
                                                                            -1272837496385991198,
                                                                            -4114423648425014350,
                                                                            -6777736736556663558,
                                                                            -8346455322442989270,
                                                                            -8139102674746606771,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Â˵ѦǊƚҒÕȪҼȜдǵōǳȵɅҠȾ˦ҼȃƢЂҸɍ˅ΤђȷǦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5988995662899703856,
                                                                            -4251249884219152203,
                                                                            -1975801677711240650,
                                                                            -1054158169795008460,
                                                                            -1573478791561073921,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĻҬˁţʋȘұʧˬӕЫɮѮŁҢτ˦ԁR˱ѱͶŖņΈșЕёŘˌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 449023338738662173,
                                                    },
                                    },
                            {
                                        'name': 'ʟјDʊпƮǠԫǯƧѿªȔƭμǿʍӸǼGЭԛϮӜʐ]Õ˜ȔӶ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҟJǱǨԗэˣĮЏƒҭӕ˙żǇЄš\u0383˴OӯΤĭяªʪΆΙ«Ɔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˱\u0380ҔûҊƅЪͿûѳ˶ƇӞɈйƚ·0%κ·ƖѪЇԓɱΣŷqȇ',
                                                                            'jΨҢʌʎӄĜЫЎ5ŵƃΈ}ÝđρoЦªʌˈŉʖ˄τɖӵҎû',
                                                                            'ӀϑĤ;ƭ¡Ŵ˦ˀθ±мǁВӝͽʈƎŚѣǼ>ɃzΜJНΚ[×',
                                                                            'ļ\x85Ġ\x94ìʸσҽʠʲɽŎϔȟӾӾԍǚʌԫΎÑú˪ϩҨƖƥ¨ȝ',
                                                                            'ƙϓĊҩʻɓϟЇЪ˩˥\x97йѲƌÛĕѵҡğˉŮňв®\u0378Ͷϖì!',
                                                                            '&ӭǐѢ˽ϯΠ\x8aĚʱѺԢ¿Kӫѓ˓ѳʱԌҕĂ\x86ʚǤņƑư¿Ü',
                                                                            'ƐӂќǗɛŶԔώͷҞҀǡƧ\x8fɳɾΑћӡԙʮҤʫҽʢӷǀѺЪ=',
                                                                            'ɨθͶԔũÃҜ҇Һȥϡǟªʵ\x9dӅ´țӈŀǬӎˢÁɏǓц˱Ё҈',
                                                                            'ʼӼ7ɀǂÇћЦʄоӶȓ\u038bԙɋˋˑź7ŞqР»ӑӥ¡ŒŌεʍ',
                                                                            'ëǎԔмɂҭәјԣțАŹƖЄδƮӣɄҏРɕʩ¥ƨȞύŘљϑ:',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Σ˙ñЉqϝѾʁίїŝҥыǌӥȨΛӪ\\˩{',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'иá2ƴɥɌϤňȭЅԇŇȷśɦ¨ƌ\u038dΗķþԍζ\x89ѕ!ǝŠӺő',
                                                    },
                                    },
                            {
                                        'name': '¼bю®Éǰԕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002034.916326:+0000',
                                                                            '20210413:002034.933708:+0000',
                                                                            '20210413:002034.953842:+0000',
                                                                            '20210413:002034.976798:+0000',
                                                                            '20210413:002034.993783:+0000',
                                                                            '20210413:002035.010966:+0000',
                                                                            '20210413:002035.027658:+0000',
                                                                            '20210413:002035.044583:+0000',
                                                                            '20210413:002035.062808:+0000',
                                                                            '20210413:002035.079953:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʰqȧҔŔÌԩʶѧŔѴӇԍǲҪɑϬҝϐȪ˫ʓŌσș˨ɟüѰ˷',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΘkӆҋͳԪƁН΅˘РΩbĠ\u03a2җcʻэśơŹʠԌpʍђύȨǈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 901684.031089604,
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
                    'catalog': '\x98s',
                    'message': 'ΰ',
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
            'identifier': 'ǼČćśĘӯХɎ/ыˡщŌүԢҕƸȽηͼÜϼӏÞ\x9bɢˉͲӇϣ',
            'categories': [
                'access-restriction',
                'os',
                'internal',
                'internal',
                'configuration',
                'access-restriction',
                'access-restriction',
                'configuration',
                'os',
                'invalid-user-action',
            ],
            'source': 'үқϸuѷȧΆƸȼϯ\u0381ӄüѓĶCơfȽόŭΧ1ǯ<˯ȹ>Νʋ',
            'messages': [
                {
                    'catalog': 'ȼʢΈ˪!´ɨ¦ÿʆҿŪǎʍɹ×ȶǅÔ`ϘǋЕɤ¡',
                    'message': 'ξǠ¢΄ͷҌãðҧЎʰ½ȩɑӢ\u0381ˬЃĚЉѵʹΉêȴ´ʹƵțĒ',
                    'arguments': [
                            {
                                        'name': 'Ⱥǻ҉èȧǌϲG\x8a\u0382Ҳьȹh',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3113994536474845871,
                                                                            228629935779697447,
                                                                            -5537901667253055034,
                                                                            7801740534261069475,
                                                                            -3698911948628243021,
                                                                            -9220289685751478329,
                                                                            8128646154704331975,
                                                                            2339918582363004696,
                                                                            -452298096982075426,
                                                                            -196852901679537926,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȥƅћԫˉ˸ԑv\u0383ZδƒѴȄǄƅʸãͲ2ҡƔҢԬǪ\x91Ҏˬ˲ʰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002047.361286:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÛžǵťâƓԋ\x9dǘԏФŴņ˙ɖųЂː˱\x8eˆƹʋƝ˾ªώϰяШ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'ұ5IɮрҜÂƣƎʼќə\x9dȭ˗БȷōϔsËԜɀÉ5ҥǈΠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002047.611152:+0000',
                                                                            '20210413:002047.629515:+0000',
                                                                            '20210413:002047.646925:+0000',
                                                                            '20210413:002047.664715:+0000',
                                                                            '20210413:002047.681613:+0000',
                                                                            '20210413:002047.700208:+0000',
                                                                            '20210413:002047.717621:+0000',
                                                                            '20210413:002047.734507:+0000',
                                                                            '20210413:002047.752512:+0000',
                                                                            '20210413:002047.771367:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ВȚҴΖϯĄǧԩÔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԛ˄Н£ǳδMωԫϑĬх\x9fӹˋ1ϳǪʡѴˑЙҸϺƨʺĿӮӛɴ',
                                                    },
                                    },
                            {
                                        'name': 'ųʰĻԊĵѪĶ1ΒƆŭɻҳýѐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŷӸȹЛʀϯЪÀΈӞΝтмχ˹ҰȽ͵ύȨˠӱϹϑǆŠЁϧʃƋ',
                                                    },
                                    },
                            {
                                        'name': 'ƝԂȱ\u03a2ҽӡŷʛĩȑˮʍұũ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '!Ԑ\u0380Ƨ<ԧɅί˹ĦǦʯɏϼ\x93υïUϜɣ˲рƝśЗ&˅ǈѨȸ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѱËѿӳɤγÁТǓӐ˓˥ŖœΩÝΌҾԥƁӘʂтŉКχɃӜӣҧ',
                    'message': 'ĴÔ\u0379γѼǠԊŴϺăȾ¾ŽÀήɥ°E¡˨¦ĹŊΐͰӛѷlьˋ',
                    'arguments': [
                            {
                                        'name': 'ЫļӗɖȜˀӓѸǔѰǦ\x88şέ\x9bыʔжȽΜԢͼјŻǳǋҎɵϢ˙',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЀԖђҭͼćňÏˌҠöŀԞώĤДǫ˷ĎιѶͲĤк˹ʴԎǯıő',
                                                    },
                                    },
                            {
                                        'name': 'ԗҤϫ/шǗО',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            468995.34719146125,
                                                                            319312.99139787786,
                                                                            154752.92176273646,
                                                                            841008.1416764726,
                                                                            685564.7954568025,
                                                                            979065.4772216992,
                                                                            565266.572122406,
                                                                            109410.79453199517,
                                                                            189518.4123968981,
                                                                            135105.49356180758,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '5ɼӋ0ӐŲïʾēҲɖʍԖΖЦǩεÍÒċԤӈƵˌӅ\x9fԦǦы˭',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'λӬЍǈΩ5ůɸ\x85ŅȢǹB˞ĵâОŉӦǆGǩǡqƴ:\x8cʤƳč',
                                                    },
                                    },
                            {
                                        'name': 'οäԣѣ9Ѝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            581125.5127129649,
                                                                            511574.6111025242,
                                                                            526346.378321109,
                                                                            82437.63508972098,
                                                                            -68604.5884846562,
                                                                            811205.5426429181,
                                                                            276106.6124881507,
                                                                            499747.09517125797,
                                                                            449014.85054226045,
                                                                            555335.98156937,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÂюӐӜǵȺİ(оʉʨʪҧ҆\\',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 606422093251467099,
                                                    },
                                    },
                            {
                                        'name': 'īҎѬùӁȣȾδԔ-Ǹåн҄ŧŽҹϘ\x8fíÕӯĬôêЗŌҖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȏšЂβʋ.zĆ¼нż˖Ⱦӈ҄қΪОȐÚέgʱíХƻ\x92ԢơА',
                                                                            'ǪSǋԚӟғСɳīǮԦФӸΗΉğԖƄ<ȖӠϲ˥ǷĹǐÁŇŷҗ',
                                                                            'ԄќэкļůӭҘψ˴ͶўЎѱƐŤԆƳÎ˟ƁĔʢΛҾ#ʳŧ¾Ě',
                                                                            'ȍ_ÅӘĜΠǬε\x94ɩĐ×ҖĢο?ҎCĮ¸МĲZуϯӰȘΨȄŮ',
                                                                            'ŧkԞИ®ɏêѽ\xadԔѨΕӑӡʩɀɯÎňBИӂθŬɤԅÇà\x8eɌ',
                                                                            'ǋϘƨY˄þҪɖжpɯї҇έȐ)³ƃԮ˜ΏӄͱҺƶƠϰőԒҨ',
                                                                            'ʯҞҹËˆɸɎ\x97ЕŖȈɰώΛƀáé˝ͻӭ\x90ŉϠЇόʴɚȠȈƙ',
                                                                            'ʷÅ¦ϮĒӟҬƈΉ\x9dѮ˱þÓΉˏȸ·СÕúҗʤøϖԋ³ĝӲL',
                                                                            'ƅϬȀӖқĮоgØЦϕΡԦǀɩɵǸȌǘ˴ɵЉЗʸӂϓʗǿʠĬ',
                                                                            "ӯŚ\x8fǄЗvĢFЧȣуǍķ˳ӏǋ¹ȇĘηӚČȈŸϓчϼƃЉ'",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԟı^Ȣ¯ίʠҼɃѓӌʹ¢ĢʥźѨĬ\x9aɘӖ>ʒƸçĉȳƝĿƭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԘË\x8eĬϑΥɲˢϰҝԫȀҪēk\x93ҚҙϸЫ%èƮĚ҉ʠҁќҊЂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6614222759370663263,
                                                                            4881183366053976775,
                                                                            2331316642625747494,
                                                                            8798525160559196458,
                                                                            -8759509754667668826,
                                                                            -647339199104088983,
                                                                            7782563164406611642,
                                                                            6836434741407946774,
                                                                            3883750072642268315,
                                                                            6359981119057999813,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ǦɯąԖð´ƀ˲˦ϖĬЩѦӵĎɽѹ'ϕɵӚǻԠ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002050.160219:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɩϬԢή8ŋ¡ɝϠʶ+ɌҲǉ¦ɩЋ¾ŕ6\x8bȤőʾʑȺ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ïȬҋâȖȻЃŅϛҐ·ˉΰ\u0379ҮǰΎˈӸ\u0383ԍ2[цE)ŞҌ^ѝ',
                    'message': 'ϢϷӳÀДĬΜϱ¹Þ\x9b˹ƓʶˌͰȻá\x93ƭ\x9bȋÔȱԢϩ\x86}ʠƫ',
                    'arguments': [
                            {
                                        'name': '҄ŴƃҟуĠ·ϯƗǕӼʠҨʗτӭЃ[ɩӛƇê0\x94Śн9',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            238820.85854816885,
                                                                            837620.0392513836,
                                                                            377284.3221834391,
                                                                            280948.6136195942,
                                                                            59193.99721791435,
                                                                            588717.2174164552,
                                                                            967192.7127049454,
                                                                            671033.6546729432,
                                                                            53251.02998639608,
                                                                            750013.5820435466,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x94Ѵԛʇǐ˞ǫɔƻrΐо\x91ǥɫ«#щĶѵIԗɍͷмX˔Ùʾɥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 864582.6721279345,
                                                    },
                                    },
                            {
                                        'name': 'Ȳ>',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȟтӁӴʨU˔{·ŧϱþȖΠΆʖÉӦʸ˂Ī',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8324339121892710210,
                                                    },
                                    },
                            {
                                        'name': 'ԪŦа˓ʢ\x88țǈęЕϟŌ¼1ώЧŧɗȂΉЬ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002051.072522:+0000',
                                                                            '20210413:002051.090766:+0000',
                                                                            '20210413:002051.108064:+0000',
                                                                            '20210413:002051.125317:+0000',
                                                                            '20210413:002051.142305:+0000',
                                                                            '20210413:002051.159176:+0000',
                                                                            '20210413:002051.176834:+0000',
                                                                            '20210413:002051.194412:+0000',
                                                                            '20210413:002051.211772:+0000',
                                                                            '20210413:002051.228393:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'φɈ4tҘΕƞĊϹʡʀǐŸ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϮҦ£>ҏñƬҔŭѡρɮǿÔνʇО˧ѹԨЁҐӿŁfȱʑŻϏǉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƕͿ˫ʐӵ\u0378Ӽ¦ˊʾѧҗņЄƮԂĎˑȦʌ϶ÞƐҔѵѷΘȝƾϛ',
                                                    },
                                    },
                            {
                                        'name': 'Ūȯʆ˽ʸήźō҉ŔɍӦʀÄÑ\x8fͿȟЮɕσӆƋӀ³ʅԦԊɯУ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            694815.5116972429,
                                                                            995690.2192413111,
                                                                            -43596.92523329934,
                                                                            829235.4274243648,
                                                                            14782.350176092878,
                                                                            320431.40166993806,
                                                                            787161.3100909746,
                                                                            791727.8319732161,
                                                                            403477.0864566872,
                                                                            -36254.3875362684,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¾ǅϽаrЪƫɚǈрłXʥ§Őʪīǥ\xa0',
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
                                        'name': 'aǼºw˂ǡ΄Ió΄ķǎςŽÌǦ҅ŇĦDʑʢʟŏӴ\x9b÷ѯɼ\x81',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'Ό"ŴʞɿÆԐЂ',
                    'message': 'ϽΫ÷Ј\x8eʔ˃ԤɕYɿҚʼԏоȻҠɦɧǡªοń\x85өªËȒʒц',
                    'arguments': [
                            {
                                        'name': 'ԠϓͱȮģŭͶˋѷдԬΝNàˎʁϿbɃˑʃκҦǺ¿Гǎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 179253.4035928995,
                                                    },
                                    },
                            {
                                        'name': 'óԐρɴʮŻĝĹԅНӢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'ª\u0382҃ˎԟҲӝɲ/ĖǰŎҖ¨ʸī˞Ţ˒ÌѾţ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002052.593878:+0000',
                                                                            '20210413:002052.612213:+0000',
                                                                            '20210413:002052.631510:+0000',
                                                                            '20210413:002052.650212:+0000',
                                                                            '20210413:002052.668359:+0000',
                                                                            '20210413:002052.686485:+0000',
                                                                            '20210413:002052.705265:+0000',
                                                                            '20210413:002052.723819:+0000',
                                                                            '20210413:002052.741192:+0000',
                                                                            '20210413:002052.758874:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǱˤSцԭўîʖԈИƳжʗ˯\x94ĹǛϻсƛi>ċȔķĦǮ˫ʘ\xad',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'κƥЏʚхĮƙԝжƤǷΆЬʾȵпҚ\x93әƼ҇É!ɦаʃBǭӚϯ',
                                                    },
                                    },
                            {
                                        'name': '@ӽƮԎĆ}ӰѱŮҍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϕңӘƔн˭Ȕ\u03a2\x89ͷǵQBˇƓƭιàdǰƳŌϻӷŃιdҪӴ°',
                                                                            'ƊЉSȏªɸяƬńÅǼӰσҧΐɳΒöËѴғλǯˆŵû˚òĆ\u0379',
                                                                            'ϬѿQˀS\x8aĲĩȑцΰ˱ϔɌąΑȟ҅ĺҐ^ԀЏeδĻ҅ǃѸς',
                                                                            '»ƿxǔԚӃңΛԫǃѹǁИͻėkЈʣ>ҵͶļƤϓćƖZʙ|ʳ',
                                                                            'àâVˏ\x9eȢŰĸѐмЗȴ҆÷HĹΛʙàӥȇǿӰɡżĝÕʃǩǅ',
                                                                            'жѫӱҐèʈǋ˗ƖȼƫØϡžɫ˴ŗǤOūŲƐ˱ȌӱȌņɶюă',
                                                                            'ӆȵÁԤзѠχ=ǨěɂȑāÐȳČϻéχđƝɪǼ`ԟҷʍЋŌü',
                                                                            'ѻлĥρ\u0378©\u0380ȲɇǉɘˠӡƹӶĊе˅ЫϛώѻЉѯì\x81ЙΉȵщ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˊǓ_ȥʛӴƲϤ\x8d4ϥМƔΖҷÃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002053.141164:+0000',
                                                                            '20210413:002053.158150:+0000',
                                                                            '20210413:002053.176269:+0000',
                                                                            '20210413:002053.193898:+0000',
                                                                            '20210413:002053.210902:+0000',
                                                                            '20210413:002053.227804:+0000',
                                                                            '20210413:002053.244666:+0000',
                                                                            '20210413:002053.262368:+0000',
                                                                            '20210413:002053.282462:+0000',
                                                                            '20210413:002053.305572:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɍԭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            849689.5539842371,
                                                                            635103.5812472118,
                                                                            622726.8161943145,
                                                                            156493.0179546971,
                                                                            504852.8186477185,
                                                                            796563.9633918686,
                                                                            591814.4645618408,
                                                                            289437.322433922,
                                                                            563652.7201867584,
                                                                            926289.8119471668,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'B˺Ǔ˰уĩ˓Äɀ¸ΚQԪӏѠҢŗˆ_ñοȣȹԡƎȍƶǝм¦',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӾԭϢȪσºЅƞҙԕó±ШĿȢǫǍ˓ЏǢƆĖ°ĴÓԤҳсϙƑ',
                                                                            "Ԅă;ӝǛνтαӸƱTͰώ'ԊÑűȚD\xadÒ£ӆИѵëɩʲǹȤ",
                                                                            '"ЁшѳMʢɀӋĸɺɉƓԎʞŹͱ\x9bзҴтȓŷэˉʍЊġЁ=Ƨ',
                                                                            'ǁԙó2ыѝ52ũǝϲ˓ԌƠЍɹҀгȐƅԃȿßüЇİǠǏʝЉ',
                                                                            'ŏȌԝǺФãʟ˔ÕyɎʕǀ\x9aȟΘŖ\x98ǾÇЄгѽҮӃţǽŅćʎ',
                                                                            'ʝʥHɄϐmȄ)γȭϢȄтŅ$ŒˢɀɪǪŽԃîɰɅΙȌʟϊȉ',
                                                                            'ȁӅ!ŊOƅŚŇɖҬŢʋÍ}ɡԒˉáԤZˊǷϚēͶʮΰȇϼĵ',
                                                                            'ӡÒԩʵĹˣЍ~·Ԇé҉ӄɪВӸǧ@ǆĥˍɗőˢɾӻɰɎʍȡ',
                                                                            '½żɢÍΈǊί˻ҦВ˘ҠTҪ,^ӫŒɣͽҍѢΞƒĻЈ%бҪ҇',
                                                                            'ɬ8ƕƮӟΝϪŶԑʝ÷҈ęǳǚīɢŗӼʃ\xadÎɹɱΊ·ͶТͰʔ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǦɋҲŧȕ˘ǒɟƽĿ\x84',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2914644154897356343,
                                                    },
                                    },
                            {
                                        'name': 'ɰŦԓȪŦѸġδϝŪ#Ȱ\x8eӂąѮśʦ˕ҸŔǫ\x84f%ҤыыǴǯ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ȩɲ\u038bÞĲѕʎ\u038d\x86ςȵȴбȃɽʨˠҶǀɨ˲ўсǘǶ\x92ʂęøw',
                    'message': '7φúǘɶƜŊϞ˒ȁ®ØҬНͺӹϯʗȁΚ\u0381ɐїòҴvԈîɭљ',
                    'arguments': [
                            {
                                        'name': 'ĥ˹ϓԡʷ\u0382·\x8fΓ҂ԗдİ²}Ѿ˯ϟǺǲȇ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĢԂϏÆ\x9aĸԘЈʓ¿\x80˝¼ǯгɺɠHƈԗÐɨɵφ>Ϣͽ˧ɽБ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002054.326185:+0000',
                                                                            '20210413:002054.346748:+0000',
                                                                            '20210413:002054.366355:+0000',
                                                                            '20210413:002054.387259:+0000',
                                                                            '20210413:002054.406409:+0000',
                                                                            '20210413:002054.422762:+0000',
                                                                            '20210413:002054.438572:+0000',
                                                                            '20210413:002054.453545:+0000',
                                                                            '20210413:002054.469338:+0000',
                                                                            '20210413:002054.486197:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'kʮÛœÅԔ²ĻƊƧԞGȳåƣҜŇъԆϚѨƀӛɹιɭӣA҄ʈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x95ͻ¡ͿȵưȻȺȀѡȚǋѶɎЄ4ϯѣЩŌдϦаȨȇȐИ\x82ʄł',
                                                    },
                                    },
                            {
                                        'name': 'gƳɔѪҖөΓþȝöǮɀάìÊԣ¤·ґÕΙʐɽѴʖυӟϋюЩ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5873288997892542442,
                                                    },
                                    },
                            {
                                        'name': 'žҨǙbǖs҈ǐǐӕ҉дѤțīѩʩǾЏʔΩө\x88Ĵ¨ΒԇʴˎĨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7720469602722793098,
                                                                            -510713169943129460,
                                                                            6559620620028659797,
                                                                            9081229563332762506,
                                                                            -1919613559669909913,
                                                                            -8835065583620969247,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŚҪɮЫʕǻƠԞȬԨМΘӝнұςјńӱ˛¥(ˣɌҰ˸\u0378ť',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ґι\u0378ĭΕŅBɩŰȏѺÜɸόғȇȟƧIȏҨϺƧӟʏдЖɉͺȑ',
                                                    },
                                    },
                            {
                                        'name': 'Ɓ½ÀɆïϖǱĽҩGÝiҵНϢʏŕԟсLɲϦԠҽӘŨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002054.966446:+0000',
                                                    },
                                    },
                            {
                                        'name': '҆ϹҟŉΙ˸ɢĬ;Ӧ°ƒԅΒǂʻń',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҦгĢMҀʛǃʚĮЧ˂КĞĢËӎʒУ\x89х҇\x9dƄ*ƪ\xa0ΎɪŚĀ',
                                                    },
                                    },
                            {
                                        'name': 'ӡТ[Ԟ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӿї\u0379ȍķ˯ɡʮӮҪɑǐˬɑőǰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 277232.530783619,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΞԤɌ%ɊҫŐɀЙǵȸ¿5ęŲÚˇȸΒŗ\u03a2ǋÃ\u03a2?¬ФÀʊƲ',
                    'message': 'ǐҧʄε΄ҠѤȵ(ĉɀǗȯҢĚˡǙϪXҴӄұД˒"ƷîгƱΰ',
                    'arguments': [
                            {
                                        'name': 'Ԥéĺʐԝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002055.602753:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɢӢʿ§ʗýȉԩƎ\u0378ïђьΔ^ȜԔǤʬ£ѠͼкΓЕĹΌήĪ¯',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԡϥѕʰŹȕЏҺs}Ѽo',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 983236.3141572138,
                                                    },
                                    },
                            {
                                        'name': 'ɈҎɭǆΡɻÿŏͿ\x92ƞШ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': "xŠǖгĊʋƩí¿˺\u0382ɳωʙĉʽӪ\x9aӶȯǓɌǰЫƲ'Фŵӑм",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4208931234313768398,
                                                    },
                                    },
                            {
                                        'name': 'ƋӃǘŗΝň\x87',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002055.980762:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԔŦȔʮùǉǈŭƲɒŗŁū~ǀˢń áǣÚԎѓ©ŚĭԎԏ÷ȼ',
                    'message': 'ÿĹβyρǓʙԜɑȺĨŨ\x83\x85ʌ˂ϴҬϟīȅʉэͶΐӧˌ\x98ȩ˃',
                    'arguments': [
                            {
                                        'name': 'ʳϗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɜԮȢ\x9fӮԐНʋĶ˷ӯbДЂҧʌ˙ҝǞӵɆɈӟѺүάʂҥԩˇ',
                                                    },
                                    },
                            {
                                        'name': 'Ѷқ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002056.304238:+0000',
                                                                            '20210413:002056.319110:+0000',
                                                                            '20210413:002056.334554:+0000',
                                                                            '20210413:002056.350405:+0000',
                                                                            '20210413:002056.368191:+0000',
                                                                            '20210413:002056.384054:+0000',
                                                                            '20210413:002056.400820:+0000',
                                                                            '20210413:002056.417645:+0000',
                                                                            '20210413:002056.435099:+0000',
                                                                            '20210413:002056.452147:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǺƆүӁǅÂûͰƜ«ö˯bЮӤѼɩƏųϘԡ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 560882.944786046,
                                                    },
                                    },
                            {
                                        'name': '¤ȿʊ˪ʉƌϵ҅˼Ċιɔńƪǹș',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 193840.6237809554,
                                                    },
                                    },
                            {
                                        'name': 'āWƂϔôbǆ¼ɁȠĠ/ҋ¤îͺВқˇ\x96ǁѓȡcы˷ˤǠ¿ơ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ƥқξѨ˟ϯƌJǂɚԊʣӶ˻ҡϦѤѸšèӂΨΧНðҌľԑԀȍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¼ԏΩӐϙ3ÇӄʶɥƵ¹ѡКѲΘǟíŇӡoϪʋФϾ©rӵjϕ',
                                                    },
                                    },
                            {
                                        'name': 'Π\x84ǲҶɞȳжǒƶЃȆ˔¶\x9cβҍðɗҺ\x91\x90ËӁǹ=ϰȪΏʎ\x8c',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѳŖĨƸ҉Ϛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '8ěЃϹƳҞ:ǾƙǭгοԖΧňXԆ¾\x94Ƙǲɶ\u0383С}˲˰½˓˱',
                                                    },
                                    },
                            {
                                        'name': 'ќúȚЧϸГɺǎiһǰЪȚĳĺ²Ŵϔʑ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǤȮĦ÷¼ąòϚɻǆǓʴԀN®ÖȣêeɪԚ³ȮǹǻиŨҮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002057.233252:+0000',
                                                                            '20210413:002057.250362:+0000',
                                                                            '20210413:002057.266993:+0000',
                                                                            '20210413:002057.283914:+0000',
                                                                            '20210413:002057.304014:+0000',
                                                                            '20210413:002057.321266:+0000',
                                                                            '20210413:002057.338616:+0000',
                                                                            '20210413:002057.355778:+0000',
                                                                            '20210413:002057.374082:+0000',
                                                                            '20210413:002057.391479:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŎĕʺΦʝÐͻǧƠѧл\x83ДßԟʄОĮȄ)Җ҂Ǘɓɐ¤',
                    'message': 'Čˬǘ҆ҹӀόįɬGӏ˂ȠɎǧщѶaϴƻԘГӓӂlөǭԛğ˒',
                    'arguments': [
                            {
                                        'name': 'Зđã\x83íJԤA\x8fʱȠȧȇӫҦӭΐ6ѰԥΞԦЗǑɜҾ\xa0dҝԩ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȞʼÍљҺҝǱ˧аˋ҂\x99ҖѽɄ<ɌǓsY',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -800524765803145151,
                                                    },
                                    },
                            {
                                        'name': 'ɨɼҷԖ\x8dƞԊɟUѦӍ.²˫ϔәȧ}ΒʉøÖɌӎ\x98Ę=хĪƭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ėƛưɗЭŭ϶ԞƦ˴ˀӞʉћˆŔΐĸțԆ\x86ǂưѻęΞљƭ˱ɍ',
                                                    },
                                    },
                            {
                                        'name': 'ÑfӞϪ>ţB\x9fˏɈѠŕ\x9a|ÉÐШΨΆӜKŇƷ˅ЙǬŞԈ\x9eӌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002057.766352:+0000',
                                                    },
                                    },
                            {
                                        'name': '˾ÀǕ˞ө¾Â',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȟºHтқʭϓʨ˞ƯȢЮѐV}oˬŊ©®ŭ˻Ѣ˙ӟMΉӝͷɍ',
                                                    },
                                    },
                            {
                                        'name': 'дѦĽΖцÞɔǿĉ͵ĨɭӪɧӂω˫ΌҊҒʢėȼBԈ\x959æǞԘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 497178.9446986633,
                                                    },
                                    },
                            {
                                        'name': 'ǪћĿȉσɓʫȖȃǩ˵ѵƑŏ\x9b$ҎɎԝ(ņʤϙϾyӖ^ƕſҠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2783957518320502176,
                                                    },
                                    },
                            {
                                        'name': "ƈƧņΟΞ˗+Ԯʎк'ÌZҋǙПϤѦŋҤǗ½νФҜЉЕ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1689488629083216134,
                                                                            6003445784218228352,
                                                                            -4064153488608668945,
                                                                            -2277872423304485727,
                                                                            2842343315804382688,
                                                                            3539145206066095268,
                                                                            39971818334640077,
                                                                            -3725927626459204933,
                                                                            -9110003474344587210,
                                                                            7005786793350287312,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¥˛Hөˇ`ˍɑʐҧBԙǫÞ/bÙӆȍOӏ˘íŽλϢÏɨљŐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǋԤԘΗѥ5\x95γϽс˺ǤԘƾХˆяһԂ¸ż0ЃŚҥʯˊßΣƭ',
                                                    },
                                    },
                            {
                                        'name': 'ӿƜͳĤɕӸѡǯϢ&гǔʰƋǦȷƤҲЅÑҪΔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002058.365343:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ƌ˱EėŃП\x96ʚȿ\x98ЯŅǍΨƌ\x8fˣ¿ѬӖ\u0383|ʦǼҼ҃ÁśѲ˕',
                    'message': 'ȺĹʄǯ#˛ǍȋʸũǢżƅҧĮӇƂѯŒяϏ\x85ˇȌċ\x95˽ȧ<Ѧ',
                    'arguments': [
                            {
                                        'name': 'ԀȝâΨХЂ\u0379ԕńǽɘƅԀҸèҕмϿʀƚěǦК\x89әˀҩÐȨʝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȘҟǜíςȍɧGϝ҄˅Θøϵ\x9bŅɮΜ\x9fɤІÑËѵɑҬҷƎνȮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĭȿƕȇѰϧјȧɡǔΪëΎΡʹʅѸϹˊȉΑȑӶ)ưǺӴƫτf',
                                                                            'nRÐÂȹ/ĸҝɆɢɺѠĎƳ˥˦kѪÈЧʫǗèΊд·Ŵΰ΅ӄ',
                                                                            'ҟҊ˄ѼƠԟǙʎӘӦđҮš÷έȲ3˙üeчΊŊζ\x8fӑüӗԤT',
                                                                            'ЛȭöԈPwʆЄŞӒˏҔnПÍˣŗʮϿ҇G˔¿Ø΄ʼɢ;Ԡҵ',
                                                                            'є7«ǊʡɣLƅ\x84ɩ\x99ʀfÍʗů¤ǝCĚ\\Οӷ˖ҎӰAԀ=Ő',
                                                                            'яȰϬʆǘФɝͽǺhʁ2ѹƟΣɅɎеˣήΕːT\x91ĞXfGĥ˄',
                                                                            'œȹ¦ĲƸԑXˎɜΜȓкέќАöӣˢЖϡư҆ҵǮͻŦǩáʜр',
                                                                            'ȚϨ\x94ԂżϑÑƍҐʃ\x94\x9bԫǮ4ΣȈ˷ɓтǜĻУ;@ӸʝѢѽќ',
                                                                            'ζ¯Ģǿϗäҷ¤рˤè\x93ļÂ\u0383ȖðˡʃµȢɝǜÃǉĉÞ-ԩԤ',
                                                                            'μʻϢѠӑΖύςǁˀÅӔ˰ɴ/Şg˙ҥʇƌυѻԍрϰƋƕzǾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɮʷΝęӲɹҗӵ]ӱӘƢσǠӲ˹ΥЪĸŪԛӁpʄѻҚȞ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002058.820446:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѦμűʽКԝɴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x83ҌûOʶơð˥ϔɘâƗɞʋ˱ġ¤ʢ\x8fӲѠ\x86ϣͱ˶σӽǣ\x9cȊ',
                                                    },
                                    },
                            {
                                        'name': 'Ӑ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002058.957888:+0000',
                                                                            '20210413:002058.974704:+0000',
                                                                            '20210413:002058.991712:+0000',
                                                                            '20210413:002059.008389:+0000',
                                                                            '20210413:002059.025225:+0000',
                                                                            '20210413:002059.042718:+0000',
                                                                            '20210413:002059.059910:+0000',
                                                                            '20210413:002059.078734:+0000',
                                                                            '20210413:002059.095716:+0000',
                                                                            '20210413:002059.113242:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϛȧѭԨԢǯɆϰΝįӉЉИϞƃðͳӣDϒÉȴŹ1ΙɎ͵Ŋù˧',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            559807.4018659155,
                                                                            682725.7486498954,
                                                                            23815.514374242193,
                                                                            299848.54327096266,
                                                                            691144.1835826536,
                                                                            902851.220805161,
                                                                            872367.1708680773,
                                                                            567883.6243125635,
                                                                            927878.0570399186,
                                                                            742468.0635935684,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'mϠ\x84Ӣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x81ѲZđǘϩ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002059.715980:+0000',
                                                                            '20210413:002059.732872:+0000',
                                                                            '20210413:002059.753040:+0000',
                                                                            '20210413:002059.772983:+0000',
                                                                            '20210413:002059.792397:+0000',
                                                                            '20210413:002059.809453:+0000',
                                                                            '20210413:002059.841839:+0000',
                                                                            '20210413:002059.858937:+0000',
                                                                            '20210413:002059.875667:+0000',
                                                                            '20210413:002059.892834:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '϶ʸ\x99ąɮ/ƠǨƝӧͷʗԚ˚',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ѳ{Ј¹˛Я\x93ĊɚӍƨХȣ»*¡ǥԜ˱ΘԡɄȢӀ·ԚԃȂԨϮ',
                                                    },
                                    },
                            {
                                        'name': 'ԨΑԡm',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002100.047722:+0000',
                                                                            '20210413:002100.065223:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x92ʞȴǫıʋ˹ŏ.ʯνɈwŕľˢÊӟĆƍƬӏƃϊү[ЩƻОГ',
                    'message': 'ÕX¾ϏƊέ¦ʑʷŶÓ\x8cπĩнѬ/ОȖſВɀÓʿŲ˕ǔԓ҃Ġ',
                    'arguments': [
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ϖ˳ȯǁΆ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'Шϧ',
                    'message': 'Э',
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
                'identifier': 'ƢӿʆʡŪwжϫԟŎȪ{ɱϯԁƫԌƠӦĄʗѲ×˅ČśƭӡӀō',
                'categories': [
                    'access-restriction',
                    'configuration',
                    'os',
                    'internal',
                    'access-restriction',
                    'internal',
                    'access-restriction',
                    'invalid-user-action',
                    'internal',
                    'internal',
                ],
                'source': 'ŜƤҡѡΈӦɷĠжýōҵȨřÐŢҦϓ\x99я˒Ȅśϸˢ2Łԅԑę',
                'messages': [
                    {
                            'catalog': 'ҒÁØȁξƏώŧf\x81ѺΨŵɳКǨџҦRҍмÖ¡\x93Ȉ˰îeҠӳ',
                            'message': 'И¸úΰ1ȧńКϢϩԦϣ&µ΄ԥѦɥVͷ¶ʰρþͶѐӆӓή\x88',
                            'arguments': [
                                        {
                                                        'name': '\x89Ҿ*ЉӀˆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʏɺΞԭďʄΞəϹϤΓb˄Ϭѵ\x9d˫ңιɏǳǅǑıǱʣǼȑ\u03a2',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŉƶӷàĶ\u038bįˮԈğşѺԈѨβʷÆŶΜzӴÈ\x8cϝ7ϲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΤĵʄLɌʤǂşԔҏҹћ\x94ӦȏäǏФӲҝѭwМaɖƔѐԇ\x8d',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002039.501694:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˹Ì˕¦ԒRňɐš\x88ɛưͰʄʑѤυǢyÞęûĶюUΐʏόŽɂ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŐƜǀǚ˽ΜђnŐԞѕΧªɂϪĂϢӈƋĈ©ÿΟǮΈѥ\x87~Ȱɸ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҟ˱ʏИūТʽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002039.654114:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʜʻʂǱĘͿťÆίȦӃŸԊЉǊҬ7®ʮΛŢſ¯ӒŃώȥɴ6ɰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'лʠÈbɇȦӡƮǍ\x96Ȟԥ~©˵ҕԅĎ¶҉ȲɄԡ\x81ҟǎĦzͶȻ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȢӪɪέʑʲǡǫϠҡҍ>\x8fΗAӖϧƨ-ɐҋЂϗўӺɶ˲ԄûǙ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӦӅωМĉΑ>ЩЏћřύʳ&śģǁЮȪƀɊʏӕϋӖʹϸÉɑγ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002039.969879:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȝ˴ӚҴʏȗ]ӃԙÄпčˊʮúȒϝңIԭ϶þҥДɭɳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'öҰ¨зс;{ƈӗˁϬЭŊşӪɨĿωȘϬȓϪƕЁ´Ěƥϐǒ¥',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȘľȉɈӡκҸҀЉщÂɂбƾŵɳϴ˩ˉ*ˈвɦżԟţҠӏХƘ',
                            'message': 'Ğ҇ӔчӛѵʮǰҞͽɱӕȏΩƸĞSŜĥ\x9c͵χ¡˭Ҳȭ˒Ԩ¸ʿ',
                            'arguments': [
                                        {
                                                        'name': 'wӮҡƗԌq',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǛõҚǔЗԄʱɂĪʋRϮmcœєΏKv\x9aēŉÕҲ[я(ԨɕЍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǄǭѕͱПŐȐH"ĸŊˑӱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŅɝӺνȓӡ˥ԀȥƫӦӊбIƄKȶȐ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЂԑũΈǈКΩΝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'LηƤɆŜ§ʢɒǆmЦŔбǏ/ʪҘ˕ʱδϛʫӂŲ«Wȏũ×œ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ѢŇǔӝ˕ƴӑк¦ʎЩʸӄ˝ɛ'r¥>Vħʾи\x85Ʃƒ\x99ǂÈŏ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЫѲǑȃӷƷȧűа5ҮЃʓsˑȄѵϦʇ΄ѡ°ǂƳŖ\x95ϳȡƘʳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸԮӪŗȓʄȄ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7454489891057805664,
                                                                        },
                                                    },
                                        {
                                                        'name': " ѻTɤҰ'\x91¼҉ĖɈҔÙԭFͽʋ_ҙӍƝ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɴԠéÖǳŜĵĕѢϨ/ĺǣτЯғϕљϑȶƾԁȔǏʻɹѼΪǾƒ',
                            'message': 'ыЌĒʇԘӔ˨ӅÙԥѨƜȩĥ5ɥß˩˩ȞЖёƕ6,ҖӌϚĈѡ',
                            'arguments': [
                                        {
                                                        'name': 'ØɓƁяˢɟȿsӜϔfΟҔ\x97Ū\x99ˢј',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҳEʸдÐ¬ǃúѣųʵˑɓĝтΒƪӊǉɰ˕ВЗԣĩɆjǴȊ§',
                                                                        },
                                                    },
                                        {
                                                        'name': '˴şȉњŁżħȊȂΉƄҗ±Ϗá˯ѠĿaȒˠҞţÝ\x81',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'п',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЊΓˡɃźəȥԝƙɮà}j#ԑȇЕϖӤϊϱȏ\x86',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8905780077278988569,
                                                                        },
                                                    },
                                        {
                                                        'name': "ԭ4-бǼ»ЍȷΔɉ'ͰÂǬ\u0381ӒŧǕɦҋȦώŚ2˫ƨȗ¬ǘΖ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'úͻГȂˌΚɤʹϫņӶιˏǥǌʘ$ǝН˕ˡĈÓĲǪDŪγоϒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 9144.473361060387,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύʫʖ˾Ȳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x7fʉƻʭʵҹˢѳȱȧȶϱʶqǿϘǙп',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˨ȷԛТƤԔŨ\x9eȗĐǜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿʯ҂5мŧȋͷ\x99ϲɐǌÈńˠĔЅ˽РəΟʻҬIӂҢĈãđƎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɣ˲ɨȸʱÝίN҃ȌЛȝȼЉЩdɸ˒ЕʺϜԣѕΎτʁҎZãƳ',
                            'message': 'Ӄˆϑ˗Îφȝˇ\x95ӢŔb˭Ö\x81ьŖűќԬѻϺӾʠͽɻʝȲӯ\x9d',
                            'arguments': [
                                        {
                                                        'name': 'дДϫΧ\x81˖ҩɮԜʿȋǇơԮʣƥšΪǊҲȟįƟϠʙҏ˖;ȈƢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӝͳΒԮϞӊҌȤԧѠĹȫ\x83ΤҹгΆж˼äЖ¼ɔӉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6730727143895052928,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӕh\x99ȗȣbǥ\u0379ӽԍҨˈȿҕɄȗҺʿ¦҅ϥҢƗɈ˰ʌɃȉɈԓ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƸԑʊƝǂϗЎɐʨӬǏ˃œΎ ϟοɤʐǍϒԭҽҌːљʥȋˍɪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͱ\xa0ƮĠ˻ɜÙϕΡǵӮҲ\\ŒҲϪʘӖʘñȘǓȷ/ҌČ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋЁȢԁ\x96œӺѼ/ÿ΄ϼò0ʈSđƋȷēƈϛѢɦԥèԠ\x99Ѭͱ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ў{ɶǃď0ҙӳŜ8ÏǜǇĒтϖ˒ťΩÿѯΛчеЏưΐϡʤʢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ȃϔεġǨӬӯǽCцǼ'ΐoΚ˻ʣĎљď˖Ȅ[ˋLнТԢΫ˨",
                                                                        },
                                                    },
                                        {
                                                        'name': 'TН\x86Ȝȫ?ȪѯiϬԗ.Ԝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6126707228992441480,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖʌ϶ÑЏџЁҧĒϠ¬ϜжúɣNҫԒǊɮҍΛͲńΖӊΧʂ˙ӭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '± \x95ǖҬԍÕȭӃðͳĂЁĐєҰɝτǌΡђɂЪаƝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ӑƀĳшɘš˃tѠȂЈ<ǆǳԅǝЕӷƥį\x8cșçċϒμƀŽǾɗ',
                            'message': 'ɣɥϟǶáźɻϥȁ®϶˗ǕƮǢƫҿąϰĘпýĊк˭ҺӃĵɰʠ',
                            'arguments': [
                                        {
                                                        'name': 'ҐҟԍӀґǬǰɿÏɭ˚ӵŖQҽƉ˴:+БŜÝǄŵʺƕūзπǹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗʖѯiҀǧ˘ơϴϊˣ@ǘK\x84²əɢʅԈàҘԎƨώҺƑĝʷǂ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍ¥ԤûʺÎҥǿӖɛ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĆμɒŦ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '0WΑɡŨƖӡЫʮĂҏΝӖƗҝҩɻȷĻ˹ơөØ7ʎƞȈˁƖȞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ψˮȒūɣġЃȼ˙Ǣ\x9eäȡŸ(ɾщýГ\x89ӴŉђƦʂʅǆ+ʩɝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 488502.7173797883,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļɳùȓϠġř',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'łϽѳɉԅʥʐǉєʨԒʹXϒӈǑҍӊ\x9dɱϋЛӚǫǑϮҼԒɬʝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002043.046502:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'θʟͼβЦѧŴь',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'эЩҿΎʹϿșӿѥɞœĿЅçǆĆҏХƖЌʑɶԊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɰaÐόԋϺƣΆϕĎɭʇȆ¦ϗƤ¨ЌŅɃąĳɎˤƩˤǈɁDԥ',
                            'message': 'ĹӟʻҤп ȳ\x9aӵnńȞƔѫѾҙȯзˆ˄3ԧƞҝriǏ\x9fʨЮ',
                            'arguments': [
                                        {
                                                        'name': 'еʮќɊǚ>.\x7fȰӝΨȋӯ\x8bĺęΚǉ\x80ʈƨҗҩʼʿƹԥӋĥǗ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԋ.°ҫʵϷɅĈҶŨΪДԕҼǲİя¬Ł|ǹΧƇƺϑʊϯџťʨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҬřĻʕŷ)˕ů',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002043.396016:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÝəˢDӨѶŬƎɹʆ;˥ȹʋǞ±kʠϢ˗\x90ìkĆƿӳqɄІ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǰʅʬ]αӉŗӋɢϘǝƌɐȋ=Î_ɇͿ˂РЩҞÂ¥ȡƉԩɥԝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2417801257402829369,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϱäƢʑҜѭεǥǋƸΉπ\x8aԖʆǛɧI˱цЁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϟŠҢʮƀƗȖЙǴǇӊК',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 903953.6924598805,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǣёϏæѩˋіŇûӕ°ҕǆѨҘȚˏɥǓĵ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 916035.8379723215,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϥ\x9fÎµʘ˫ЎϢèάĿϔθϕ=ԍƩϲʑśďǵœʓåΖû҄ҡО',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɛúɛ˂őȰƂƑ#ϦӰɲӧʅќ¨ǰϩѨӺʳƷíǅĝҍɆьΏˮ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ұʇрĢԈэ˵ԂʋԊξˏӧӪˉɵɑòíџίɳѐΚÒùϳɘЍԕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -531543814756136894,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'пÁϊŘȣǫ\u0382Ӧ\x8cɩɘΠà˛ИҘҞŒүʋ˄ӏԋԡǉλĔѴҫʕ',
                            'message': 'ȫʫѵң\x8b¡ɜƕNԉҺӅȯҠşɠ\x93ΠǸҼοРгϐĬцɟ÷ϯψ',
                            'arguments': [
                                        {
                                                        'name': 'яіɐƐʳљ ȹ´ɯʚбȠɮǦѝɵːƞUÂӗĲǮÞ\x99yȨÌ;',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x9aƿũ˖ҴɭѰʓҸϟ\x88ȚāХǸВțʡŏ1ɉћΊԒńmÿǾŻǷ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¶',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 31814.84788966365,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ž',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3733197083770338602,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЈɈƹ\x84ȟ˟õŚůǄɰχѻ\x82ƫȗā҇ǴƵԌӻȕΡſǸ®ӶˏҢ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002044.235840:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'є\u038bѽ҂ÑʈÍʚͻĬȭƝÖӧʒɼύԊ\u038d}Ϳ¸ӫΌӉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĪĒѽ˩јϱӊǆвƹύϒƖŧ˛˟Ź',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑӷŨKԬí',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1892879745443119952,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0383ԤÆʮԏҲƴƶӜ?ɦψψЌӧɇ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʻȂƗĩҏϷєЪƢȉƠǴɒȍ˵ҹĺćӬб,ҸҧӬƋϘΜƙѴ\x80',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0379γςíʟԝїàƘӾѥŊțÂѽo¬BҎǱȬŉȉԇˠƎУӣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȖʓΗ ʚʲ˓Ĩ&ʽʁǀƨƐϚαςʗ\x94ϾLʢiƝԡČɁɝƅʹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ѐ]äͰȧҒƌΐδɁƋƭԪĿћ²ˮɳҳҒͽǠҠÕňŏÈӶӋ\x96',
                            'message': 'ɅΨȹǮɂƹɑʤϣBˉɟſ>ƽϛάŏӂʜёїӒôÃɹůǹѰѨ',
                            'arguments': [
                                        {
                                                        'name': 'ԑ˱\u0378]У\x87ƒơ\u038d>ӈŔһɮĚˠԈɲ˖ѳҲƓӃˡ˟ĬѳƂЏɜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¡ˤ˓nѰćӶÏϴɘÞʢҿά\u0380Β\x96ӻƯĲ˴҇ӑԣɂ\xa0ūщɃɌ',
                                                                        },
                                                    },
                                        {
                                                        'name': '·ɽγΙχ^˸œ@˻ȱǴưϕȋǈʴŴÃȺ%ͻѳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'зѪ˶ҙҋӲĊиʽЌŞԋԤыɜíҿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѷ\x8fΓiƜµЦȐ\xadʿěҭͲβѠѐɾ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΈΌȐыԝғҘӼÞʭCÀ\u03a2õТ˴jΔ2ȘȘÓţωIԉŲ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 595978.520825545,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÌǳˠԭǻƩúǆѣɉͶMӠлҶʊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4772421679483777082,
                                                                        },
                                                    },
                                        {
                                                        'name': 'п!ƇçϽƿLŴШȱ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѥХϬғӴЄ³т',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˶Ϥĵ.ȳӯȌžƕĵɱū˖ʋɥӇʬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϧȶҵŷҭq*',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӔŏĶȎǔŐīЂĐ-ȋǗҭƁǙωϢšӅӒЄˢҡȲ%ǿҫƟŰľ',
                            'message': 'ʛԋUáï\x97ńсǬѠҜċϻѳȱ\x89ӊƳЙϠÔÌȧʬМϗ\x8aĶҢʙ',
                            'arguments': [
                                        {
                                                        'name': 'УeёӕӊŔĨǽзŽɜʥФéӯŦɛƦɰѠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҫŴšɸƊԤʖІʲϋȜԐӏҵʉԓҁIáҹˑɔF\x83ĩŽуâύ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƁʖðԣǛȱŗƩ<ƈʎĲҠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӣ΅Іǲțӟ҂ȄϣˇėҎƜӮҼěʋɘΐѶ?ƅɈāӺ˘Пǻšš',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 437764.4233549078,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƶƸ$',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 127842.21145082221,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ь¬ǌҎ˭Ȉ˰ѺÞӎήŜˍˇʺˇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ф@ԚˬŞДșƪ!ʃҵϊӳԪÁƁŖƹϫɒäɏ˫ѳſ&ϩҵŠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ųӌʤƹ\u03a2ɵэ\x94ƲŠу˟ѡҁӋƬȟӖѡϱɉ/η[ы\x9fǬƤÈј',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002045.962929:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'θ¡ȽıÇ˄c3źȮӧķƧ·˪å\x89Ά˾cıſõʶӓZԜӁӽȊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'җΌKёţwζŸǧ\x81ŎҳɍɁʛóʛάʒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʝӿǙҡјϪөɚˋϮäԦԂňźϴȵϹ÷њΫʑϗíѢƨάǻԝâ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȯʭǎƁǨòx~ëqϘɿ%Șãƿ˩ѯăćԢӒιlԧƍȮѵӽ.',
                            'message': 'ҫҋȈ¿Γӯ>ǴΉϒȸԑhǄȡϩȭ1˭gҘȑωȣδӜԧUų˨',
                            'arguments': [
                                        {
                                                        'name': 'ɴξ˙җҨ˰ԗӇӤɶǥ¦ƭlϜҲκţìɌТаĘӾGЃǨʿԭз',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002046.227786:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƅʕ˝',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґѯѡӺϐȥϛ\u0382ˢɃäкýјʪѨ˪ėԉΎϏƕӫʎPԖΚЀ¥Ù',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Шőǫʍʌȯ¦ĉ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳƑª˂ȻɵϸȄĐEīӤўԙҟ\x85ҵǫϣφɷʕƅʷ£ҪѳάȎı',
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

            'error': {
                'identifier': 'ʺîʏЫɝ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'ªÌ',
                            'message': 'Ϯ',
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
                'identifier': 'ʖʗŰ~ͲӓʜƳӻħţ1ɐɿƔ΅ԧŨΫΪнȁȓɌҎÆӍԝҒʠ',
                'categories': [
                    'internal',
                    'network',
                    'configuration',
                    'file',
                    'file',
                    'file',
                    'network',
                    'access-restriction',
                    'configuration',
                    'internal',
                ],
                'source': 'џɣӦȽʶŗӡԎƹ6ΥĕӡͻüВѷĞˈȕǥġ\u0379ƥĪѧԓǀɮ\x80',
                'messages': [
                    {
                            'catalog': 'ČǜԏƵɍѹюѨѰ[ҕǘ˔ԉе¾˺ɓҴ;ˎИ\x9fȭȈȪÃȊɁҳ',
                            'message': 'ϦҍʙʔGеƳ˞ĆˁƯǁƽ©ȉÜ¥ҵҒќȒ;ȱȖŻъȝɓʶʋ',
                            'arguments': [
                                        {
                                                        'name': 'Ρɽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002100.696003:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'òɷӢпͿ˝ʁϧȂũΫ϶γӉˀʌ˻˓ԥ˗ʹхȑ9ƃӎŔԔϏŪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 134534.371077954,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϤMÂʰξϚ°Î\xadҨӑԄƎôΩϬįԪšŵ\x8cXƕύŬǤԆè˾ԗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ɮǦӯї˥ɵƱʂʸι\u0382ʸԪϊvcǪԐĕ\x90'ȪӀÃԦӷϬԠυΌ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŷΨҎǰƒưʊ˗ǬϩǏ\u038dЕĿҲŴϾщ\u038bËθý»ơĵƊùʃƴɿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѵɸͰΖƿΘӴȟʳϘӺΌnÇúǊҍʕÕýǀϦǏʄþȸˋʻβѳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΣэӜȎʀҨѪі\x83ɖӻϷҕ,ʫѢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '5ʻԅǩϺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ZďΖӿ˹ȻlȺЫȒ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȡѪõØºʴ1\x82ĉΘ\x82ӾĦʜӃƠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002101.340871:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʓѿϯ˒Ř˝ȫϢһ\u03a2ɇǹʬԖĆҺ5\u03808Ξǂͼ}ԉ˒ϓʿƴίť',
                            'message': '\x82҈ΧӔ\x82Ԗʱ&ɣ˳÷ȷ˂ñɩп_śӏцùЂсìʥPùϊЀŜ',
                            'arguments': [
                                        {
                                                        'name': 'ɹ҂ċӳ²ʳ\u0383ˣpԮȉʌưʒɫÛɫĝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002101.478445:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'щĤҴnʹΈ҈σì\x8dŖ҃ɖƙʷš2ďԨȦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002101.551730:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԔǮϪѭ˝ξ\x97ÈӁΛ¸Ԃ˼ǜɊˬԤőУķȒ˔ÑjѦҬѓʏԡȞ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɩ\x95ҘŌѕԢԮ¼ЈіġȇӦҌ1ЩjҴǨϕ´\x88ǹ˽ǡɇШƴʑ\x87',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѡ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ўȤŤ\x82',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƆЫȹưPәΒӄɛȗǖɲӳԝϱȅɷсÈɂΑ\u038bū\x88ΕðƷѦͱӉ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˥ũ\xad˒ğӗҋģ\xadqĥ˸ϹǣʋǇζȓȞ\x99Ѕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƸmǮҭ;χөоȊӍĖԦҭȟ˙ɽϧ\x93ɏʼԇɥОˁӶӪĖ"Ɗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -14615.234660950184,
                                                                        },
                                                    },
                                        {
                                                        'name': '¯>ϴҤʛMǎǕԓўýќğƥҖɽ]ƪ˅',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҍ½Ұđξ2ѨτΛwˤMƚ˷ΰԂѺº\xadoǞɸ˙ԫW˟ɖϭєÖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȴɣĔЪȽĵѨɌƷӣ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'жZΘЂʖp˱ÊԖˤ½ŐҮtĄˬȌĴņщΒȣĀϔФ˒Ʋʝǳɴ',
                            'message': 'ɎɠϝȜ\x85<ƽѮԀŎԊĦ4ɒКԆңƖѫφɂɾ}ҡɵҖϵəΌȺ',
                            'arguments': [
                                        {
                                                        'name': 'ŒôćҁƠ9ьʑşǱǽҜ²ęϲϹPƟʒɢӄçҁњбÜɇǄ7ʩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '5ǺѮǞγ\u038bЏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'μġù5ƿ1ӍЭˠҧҙ\x89ɗ˽ÂҜӕјҾĢҾǛςȹĖӡӽǉȒe',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002102.399941:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҡ˚ƾκƛңŘ˙ĞűIȠч¥Иƽʊ·ҟȺҷΔȺˀːȁŶҤ,Ӌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˋĲôԝˉ*ưӓвȬȂ?ʕjɱǔƩǂӅƀΈɲɣĆâӄњʏ˧ѽ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¾ɽƆҜѶpȦʼǥ˗ƼNӘƄ¡',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξǋхϗɊӞÑ+;ɥɻŒБ\x8fƤѝϒÀеȴӝ\x88Ύ˘ԀÌәϘŝ˝',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠѥҾяȀɆơѥԅθѿǓ¹ƍɨºҶ\x9f˔ӛ©ƜŢ˟ʫfͺŕ\x84ԍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ё\x8bŪӋˠĻҟɷԐàӇЯЫǭʅПƜƪЈʬaŕ;ɍɜǮϮȕӾҝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŢʍԡѮˊz:ť´őɛʰÜŕɪҗĚƮѪʃǁԏTáӹƀɩŷWѨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 756777.4745625803,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛťļVҊƭʓ\x8bǏĂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŗρӦƮ\x9dԮѥҬɔɲ˾ąˠѹіûȰԕǐӡˋԧ+ўyFǒԨģͲ',
                            'message': '˩ɋ\x88\x92ŅΐΠϋńëԠ\x80ѻӉ\x8aΜª7ԗηŞǔԤϥϩԍԢǱ«ǂ',
                            'arguments': [
                                        {
                                                        'name': 'Ǟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ʾӴҊ'ԙJӓȐ4gƌИIÂϯѫϤǁʯǶȕùɒ϶ó4УǈАʟ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -11796.782771657294,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌƗϵeʵȤңВʦǘɖ\x9aƍһ\x9fƢү',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'їĲƀӍƅ˷ЋМ0πФԩǴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˮıĦåΰχȯÒʜŬɇʡBДĢśƀЈ˦˻гИɤЇƸǌŘјAӐ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐ\u0381Ӄм~Ĥ¶ȲԒΈĂбɳŬ>Ƒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002103.329205:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9dҫŚîю\x8b˪Mʢ͵˳ɉԢ%ӈfѠβɊΛ¯\x96Ԑì#.ǡɆɼȷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'қҙʳłЋʃԖ\u038b˫ҰȿüŧԢœͺe[ĺ˼ҏѫͱҴїԨŸϣԥϭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ъĜӱʻ´ȆôțJʴƐʄȯd',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƕʄӏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɼǐǂŲɧʒѪϥͽĂǎęƠҺЯ\x8fÃƂɼèƢƗǅѢuӅĵԄҨӘ',
                                                                        },
                                                    },
                                        {
                                                        'name': '/ŝƿ\u0380˪ҬÅȪÇцԦĔȾ%$ӮȐǈɑȷϮɇĳïǋфĶð\x96Ņ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7392135281116085065,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЪŨȄɍŵѡÛΛØbʰͱ¿ѢɋβÛԃԧӵxϕȜµÈΛ½ğРǝ',
                            'message': ']ɬӺʬģßɈ\x9fƮ˶˕ЗʪŵƫπŃʅ,@Ħˮԅϫӽ˩ɭ˂љǸ',
                            'arguments': [
                                        {
                                                        'name': 'Fѧ¶Āϖҷц',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӷʉȭуЫăĶųġƿ0ɛзhĀЫƏ˄ȱйСͳƺŇƝңºЄÌ˜',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌɢеȔԀǢ\x9fŞʫDĎˍɝĕYí҉ʎʣ\u038d0ȒH',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɽчȆɾ˵ҤŜһɩϿӂɅæҋΉаťӎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 477877.12212965614,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Øƾϵʺ\x99˗ͱȭІȶ\x8a\x9f÷òĩҶˢˑ˷Ɇњ\x85ΗFǬų',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002103.859594:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'à˒ӬÑԕΈɈǦ£ˡɂ\u0382Ȏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'έÊĬѬQȊІӋȞÐřέŜ{ĿˢˋǝѕӮĚѣJǌħгƍμLˌ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -29152.310043846548,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƢМŅøĪȁʘǀ`ȵϕ˴Ūяѓ;ČćΕCԆñҒĲɶθлǢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŜěŜƞɰгĩʩҐϤ\u0379LҢϽȼţ9˵Є\x90ɠѩȼҎΑ0ϮяiΖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7602989803339334433,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɏƛ·ʈҶĊÃ϶+˯Ӕԟ]äǵȰ\x81șŎЕÐȗǬÞͿĬѦϫѰӫ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ч҅śˑ˹ŧŽʎгɂƮ\x8fćɆ\x8eũ[\x93Ų˝ҁɖʹНЈĺтԬˁȉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x8dȔӃNȈǬҎΔòÊťвѾƾΔĦԨӵlɻǇĆĽĄƿԧěŊɐ˕',
                            'message': 'ҥƁΙĞˮǄʿ҂Ȍ4čȤɃȱǴòĜЖӻɟpÄȠȶǄͶϞоѰϤ',
                            'arguments': [
                                        {
                                                        'name': 'Ƨ]ĺțѮɕҒӊϱӉΥɛҸŎėĔЖ¶\x9fˠź˗\x8aˬǧĪžΏѡá',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 768951.1075901032,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԦӠьϒʓƌïƭʀД´ϲʰˡȵƎQсӼԬ\x8cxԋ`Ϲũ5˯¨M',
                            'message': 'ʋê&ǗʦĚФǙĚҍɢϦϰ×ʁϭɂҋUϲϔҲԇȑŕϚĐ\x8eƦ¿',
                            'arguments': [
                                        {
                                                        'name': 'ӫʹL\x8a"ͲXҗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'șÌʢͳȇ¥±κƣʀ˫ɞѝѿºȑǳƏғѸˬ¯çȟǼȡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӬęȥʴĪɠφÏЊʃ˱2ԂˋƵm$ьӗĉүКԒʱ?ķʶɟɶЀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǅìҘ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƾ\x8dɅԍɓԄʄҽɛҽ\u038bǠ|ОȲ˥ʰʌȂɞÇ˜ƾ϶ǮėɇЯʹӰ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃӚ7pӗàǡłķлӨЪȉԄ҂ŃзӠɢԖǘʴʊӘřȳυ2ϏӦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002104.775025:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': ';ƾѸǧԭӉƭÆ\x8fƊ7:\x9eνΔǷ\x91ȃ»Ź',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉQ2',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'çʒƧʑĨʠȧԬϸȢϖưҥ˔ßσƷ˶ȵ҄ÄҴΉѺëˈ˫ŉƇӗ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȔͶƂхĕшʣŗ;ɂ_ɖ˝Νıӆʐ\x9cŶËǕɮӁŋɃӫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 378320152807042030,
                                                                        },
                                                    },
                                        {
                                                        'name': 'MҖû§ȭФӞ˹Ɇ@Ȥэ˅ʔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 142413.93404114497,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԥɓȳ˫ůѷɰϡ˭ƜȢ\x98ЏЧʧѤȥ˵Ԓ˸',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002105.180293:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηÞǆ2ņ¢ØŏɓΕ³εšfГԜɻѩƾȘҬɩϛɏ#϶ȴѰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '~΅ęŧŞағǦӔˍвΎʙΫɑώĞԧȗîѱıіȆÄЧɴӇ¸η',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҧ\x9fķϩԍӖ_ҒЩӖɰ˲ϋˤȬʀĀτĚϊ˚ıСÐрφӑʕ\x9fΠ',
                            'message': 'ΣɰaʨĲІƕκŃŕ͵ÂȫИϐӏLђѣКѰÏŐ©ӗԕȠθȳư',
                            'arguments': [
                                        {
                                                        'name': '˥Ϥζ˃ԃЕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'бĤҿäŃØτ\x95²ϵȯžǒ\x83ϗЀэνoЯȖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1631544524129983992,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑȄÎıӅȏΣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Sź ǔɋ!Ȫƺ˽ˡ˞ʿѨ¼œǕ\u0378áȩѥϑĩ2H¼±ѣϊӆå',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '5=\x8eȭãёӅăδϭðśƌҶЩӿʉƣȭЊÃȀ҈ȱŻƠŭÓӔȚ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002105.686267:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӌŬ\u038dũ7ͽʌӷʡө',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'η|Ϯʂщɯјɓҍйˋ˦Ѧʞӓǿѐɾʄ˗ԫѽŹ%Әţȳ¬ƽӝ',
                                                                        },
                                                    },
                                        {
                                                        'name': "ƔЧҷҟѫƗŅԇΰŰĹǤuћҘ˭ʸԁ'*ʨķƉћǁŠŚŲ_κ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'VĲҥˍTϗ˸āԃŚҢ0ɏæ÷ȰΆřSëҮèʿω{Q\x98ӔǠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ºħϼƧ²¨R»ØmʢѱѰťҸŢʓƲşÀˁУй\u0383NAΊƂԐĥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӇҠǏǈɡ_',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1693461540827768226,
                                                                        },
                                                    },
                                        {
                                                        'name': 'č',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Đư˶ӤŽĻ˹Ɖч;ђʯÆYˁЬǇŞȂȓɺӨäҧіϧɩɖʚɠ',
                            'message': 'ћȼϝx2˼ƤͷʩГɧΤξҦԅԃ¸фþÄcҦŞưāаaӘǏӀ',
                            'arguments': [
                                        {
                                                        'name': '҃ƫßθʠΎʟȒ¸Ŏ\u0381ěªӵȯѯŰJɆɡҦªϦўƸΨȭǠaŌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѦҔņƺ<ʔƛщȦǤſpˁѐѲƌҨɊĉ\x84ӦaЏE\x81˒ĚχЮӌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϞǵȼĳӄċȾƝƞϵÆԨɌˮΓΈɮĤҚǰӿӨӰҲϰʞ3˴ĝώ',
                            'message': 'ѳʸ˶ȜȩԐÞǋƽ:ʊȯфå\u0383ӛҶҬâɶēȱӱȲȽ#ѱΙӔԔ',
                            'arguments': [
                                        {
                                                        'name': 'Ǯ\x85ĘӤлͼѢVӛƠȬ1ĚˬѾѿƎ{ϰѢȦѸŊȄҜ˱ȼҲÁϜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˎӲǪ\x96ϺϮ˄˭ȗÂǛÐˀЙλɆ˩ϐĦ#ωáӅ˗ҌĢҌДʁü',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΊŞæ\\ԬH˹êάЉŲСʾɅƱȡżŬȖćƈГӫ\x80ӻǣǾˋШΙ',
                                                                        },
                                                    },
                                        {
                                                        'name': '÷Ԑ˔ó{ѥł\x8bӖ\u0383ϒʶгҥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԧȗ˚[ēϡt\x88Άŕϩм\x80ʅZȞBʌɃǍпɑ`\xadж\x94ūbӖĝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'rχ˾ɹκԍƐ˂σ˘ʬċɭ҃ԃŔ\u038bʲWѽԈъĢǸ\u038bɺкĈЛ4',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϨѺǊš%ǦɛІɕ\u0379ȰŴҌƧ!ϊûIǔǣόʽħϧǳ\x9eȕǃ\x96ԁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥƂŐȽţҋɞɇÆìɰοΪÿÊïΛ\x87ȼǏЯɴѣʫҖНˀӱĺν',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҶƁϱǆФӝƙõʞфЌŷȱӻ\x9aОΑîИ϶ɾΨĘӡfʨЬӫĜœ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3428706643675266173,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɣʖԉƙ˭ŧюͱƓhϰ7ʰǇːчѾƪϬŒˠСǒȮęĠΰε.ҽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳ\x95ǗŧåѲ:ºťRӐȳҥͻКѡ',
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
                'identifier': 'ȫ\u0383ǺÙ\x9d',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ŒԘ',
                            'message': 'ş',
                        },
                ],
            },

        },
    ),
]
