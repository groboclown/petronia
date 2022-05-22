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
            'locale_code': 'ІЮ˳ϣˮɕ˞ʤɇ',
            'catalog_name': 'Пԑϥâ˯ǚӅɯӪԍÙѰǅĩæψðю˻ύϾ˹ɘ,ŖŶȹ\u0380ʦȪ',
            'message_file': 'ˇРÝӼƢΰǰӖηGζFǌƐϏɔɭǞԦ˧ēƹ϶ȑԞίψČ`С',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ϥ',

            'catalog_name': 'űӞí',

            'message_file': 'ŞР',

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
            '$': 'Ӧӟ(ǎſѯͳxҝ\x8aNτЇÿԪФHÊǝnʜϛȖ^ҏϋˍƧƙΑ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -2251287684773003237,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 252492.62605320226,
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
            '$': '20220522:173127.409956:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ѽΑ\u0381ю\x92ɋӑӊηҗΆΔӣɶ\x97ʱνԕͼIÁźˍϜKӹӀŚԈӦ',
                'Ɉͺ\u0382ϲŞΡǏȎɪ˷˫āёΟȑҜːƛӦҍѱӒ˷ƺВ¡λΊӎƫ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2118986775549095028,
                -5472500237867572610,
                -7876021811453547980,
                6234490527612776200,
                7442863598673779776,
                -4670645646530886665,
                -5451402072805430369,
                -6920721692086738227,
                5913536638756174723,
                2291090894253831194,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                230504.31838132243,
                816204.434571795,
                323880.5106334056,
                305321.7788387839,
                201299.27677741903,
                520144.20126257173,
                504639.92088873894,
                158740.84395199557,
                42426.69745683548,
                850909.374478374,
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
                False,
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
                '20220522:173127.812670:+0000',
                '20220522:173127.821382:+0000',
                '20220522:173127.829632:+0000',
                '20220522:173127.838938:+0000',
                '20220522:173127.848192:+0000',
                '20220522:173127.856900:+0000',
                '20220522:173127.866035:+0000',
                '20220522:173127.874500:+0000',
                '20220522:173127.883010:+0000',
                '20220522:173127.891212:+0000',
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
            'name': 'ēɺʈÿ˞ѣ',
            'value': {
                '^': 'datetime',
                '$': '20220522:173127.275427:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƈ',

            'value': {
                '^': 'float_list',
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
            'catalog': 'ƜŋʜıγђЌҡˁƈЙ˰țзɺӠʩΚ^>æӤ˟ʲԬКӇТŻϒ',
            'message': 'ӛԭ\x95vĤќ˔ӈ°ϖĕɡ\x95ī¬ӻŨѾĴɥÕϸŖє˼ÜԪӊɔˇ',
            'arguments': [
                {
                    'name': '{TͲґȺǖ˱˦в\u038bӱȾƝǱ\x86ǠԐÅҴϾˠУŋмϻϋРқηÊ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        5225501401563745513,
                                        6134421241318496437,
                                        -8492001288484009431,
                                        -1295558492998348021,
                                        -3879640165132218505,
                                        -8864576833110710780,
                                        -7954915683109673845,
                                        4524322361014654270,
                                        4369290772774109976,
                                        4969292632385444527,
                                    ],
                        },
                },
                {
                    'name': 'ȳѽӹ·ͽÌ˧ϻГƣӈÌȪгԤƤ',
                    'value': {
                            '^': 'int',
                            '$': 5562164123548596721,
                        },
                },
                {
                    'name': 'ԥ\x80ȷ²ОѝĽ\x8fԄϱʑҸԝАвɫϘâðӤƻǏÜϡΜΚȣіŽɬ',
                    'value': {
                            '^': 'string',
                            '$': 'ÜΨԪѧҲlÕʔ˟ƘʣϑЈԌ˰ÒΜɼҍҌþЍΌϕǦϥl˙ņϢ',
                        },
                },
                {
                    'name': '^ɟǢɈ͵ƛ§ЪξѪҳΓ',
                    'value': {
                            '^': 'float',
                            '$': 939522.0753032657,
                        },
                },
                {
                    'name': 'Ӻ˲ĈŻɤԤԟҠʍXУԀƃˮҾ\u03a2Ǳ¢ƊĮķԛʯǹ҇ĽºWƬ˂',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:173126.858128:+0000',
                        },
                },
                {
                    'name': "ƟǼĬȪіƎȍ1ӈҜɾϿѝȋ'7Џ^ѢҟǿǳǩɾxîÛίÕʙ",
                    'value': {
                            '^': 'int',
                            '$': 7531915473621494473,
                        },
                },
                {
                    'name': 'jΌӶѸӑƏȱƾεʨԍ«Ѫ\x88ȻҘê',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ʷŅȍ\x7f^ķӗþҋǬ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ļӠǀ«őӁŔАζ0ɘƥǋʙȋЕƒíúĝϕˏ\x9còєȰǷѩďԗ',
                                        "˱Ԝ˵ƄԗҽǼӣς'ʚ²ǇUԨěȅȑЦėɻƽϖkӞåћÏ˛ƹ",
                                        'sϤΕƭЅȧȗũϸëϢF˹өȓŀӣΏȾҏѰЊěK°тƉϔĤƓ',
                                        'ǉϹ<ÐԌɾҪŷΗŝЩҗȘϼӆȊšhɽƄС˽Ŏ/Ɉö˫˪Ԍǰ',
                                        '҄жäʻ·Ѕ\u038dʅΏwԤʶԠǬŏ˒ďǘ\x8aԡK¶ʞȣ£ǽÏʪЅъ',
                                        "Hȣχәiɗɦżãʌ˅ɏҁȵϹԒöӆτΜȡ\x99ӭ¨ɳ'ĹҲƆέ",
                                        'Ρɶ·Ǿ˒ЀңhǢ˓Ӽ£\u0380ƜǺʉķĪƏâЊЇϩǒʠı¤PжӶ',
                                        'ǧȑĘϹPʪшжЎ*Җ\xa0ǙŚʁԦбŬ˾Ύѝαơɒ\x89ыϴǌz˂',
                                        'ѷʗ¯е¼ɧԓǏͼ,ƦÛƤˇăʾɠǑϚǶҗɒË˝ɧȚЌ˦ɰG',
                                        'ɣȬԐ˜ϱǭŔΊfΤļĄΞƠ҄ƽĺВȹ\u038bʨХԟθÓΡíśġͷ',
                                    ],
                        },
                },
                {
                    'name': 'ʴʸӷʣȅ¼¢ѮʭҝʹϽ·ĲҙŒҠǮҕЊRȅǋϔӸʓŉɄЂĈ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        962820.9142620957,
                                        713125.2854339767,
                                        481582.3865676895,
                                        75111.61050295716,
                                        813190.5790498921,
                                        463540.8113005953,
                                        191182.47271275584,
                                        572224.3110026922,
                                        109438.6633866955,
                                        909678.9205870116,
                                    ],
                        },
                },
                {
                    'name': 'ȕƂԭŉѷƠɻ+ĕϮɛĢɭÄ',
                    'value': {
                            '^': 'int',
                            '$': -4387701508361509775,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ͽǁ',

            'message': 'Ӛ',

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
            'identifier': 'ҲТΞäʡҰǁďǀŌȅΩǥІÇӖ˟´ņĩŀȄÕ)ŌҪ\x8cǦʫË',
            'categories': [
                'file',
                'access-restriction',
                'file',
                'configuration',
                'access-restriction',
                'invalid-user-action',
                'os',
                'internal',
                'configuration',
                'access-restriction',
            ],
            'source': 'Ю¼ĹĲȻԍӉ¼ʄ\\ːҽQĚĬœʆҗƪέϣЖћʯʹƂxДϰƤ',
            'corrective_action': {
                'catalog': 'ȌҞҤ>Вņeǆ\x92ǆЁҫϣC\\ǭzŏΗƲ.ĿØЙ³ŇÂūɖԠ',
                'message': 'ĵƢӡ΄Ȋƶɶϟ§ɦϴƽǧЊӈеζňƾ5îԎҥϥΞТ˛ǜοİ',
                'arguments': [
                    {
                            'name': 'Ø\x95ĚĜřӞȜ˽\u0381ѹϡżӎŶƌ\x80ϑԑˮpϛŭħƳΆϡύTҒ4',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220522:173125.918914:+0000',
                                    },
                        },
                    {
                            'name': 'ϭɦ҈ʰӶŮɍУӢќ¬ĪҏʧƱӨζʺ҅ӾĽƝɑȬжѯɿ˥\x9aУ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ӈίŘΉȋν˺ΜĦȃǇ9Ü\x85ǕΑɔӴΔŷŃƵѹŃǌ˚ȡʜӛ«',
                                    },
                        },
                    {
                            'name': 'DӣӶАŎĢ\x99ȼªũ¾ʮӗFϒҲˆʪÖʕǸʟäΤϔ¾ôҘaΌ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -176432179828980816,
                                                        812256250069703372,
                                                        -3999027833579109135,
                                                        -3266682542789486540,
                                                        3311836335421213814,
                                                        6809104002648654775,
                                                        1809494748816745481,
                                                        -1302655955478040928,
                                                        -6901412585423476035,
                                                        -905362520087301881,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ϋӅ˵\x7fιʕƼˆÖтԤӟƆĄԘǛàӶρȈMσwɎž˙ϧǣӋҟ',
                            'value': {
                                        '^': 'float',
                                        '$': 3286.523089402588,
                                    },
                        },
                    {
                            'name': 'ζÄ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ЅʿơхȕʽКϛӠRӪǘϠǧƶȅģǈʰŋʀϿҋҝъѷӸƁҜʳ',
                                                        'üйJˁдʾʡѦ\u0383ƔԥˬʮŨǡˤҁȽɍʈˇϞȧҟÚηŰʔɜл',
                                                        'ŭ\u03a2ѹӜњϠîąĀѻӦõ˼Ԏɂ˅ͺ˔Ǚ϶źȝϏƩRǨþƫňǍ',
                                                        'åӯΦїЊƨƎВ˪ӳʽůĚɲеϞ\x99щӉЎȦWчƩҪİԪϫ_Ӥ',
                                                        'ʹΑ˄ˤāǎřȱDȉȿ\x86uϥÈ-ƦǸ\\Ň«ǣɲ˥AĠJ\u038bˣɊ',
                                                        '`ȠҍóԛɴӿϏ˚`ɕӎĎǍɡʲӟрɎǪɋŊƿԗȵ\x9cȈҬp˓',
                                                        'ϔԀôð˭ƁßǹбζӡĝʒЗŸʯϭŮjѦƸџɪȠϵīǾ˴ωT',
                                                        'ǖʰƪʙѐƦьʛʖɌЂћĮӮɕЈәÌȘФ˖>ìњвҸ\u0380ЉѾү',
                                                        'Эҿʳ\u0381ÁǱaΑԝƠԕΑňȰńӍмWΠ¹Ŋ\x82ӓε,ƎХϺǽђ',
                                                        'ѻѥĠvŬϗʶVʹǉӆӬ÷~ѯќŀѐǵǊ@Ϻ\x8fЏʓ^6ÉЛƌ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'õƧØƖѱϋ˷(Β\x8eƶyɃ˦eԁɼʢ˚xʆҒ$ɤБɁωїŎж',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220522:173126.271229:+0000',
                                    },
                        },
                    {
                            'name': '˕Пқ\x8bæҒѠĄɏӞĊȰХɗԨţȶƉȵǠ±ԀĀ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220522:173126.307182:+0000',
                                    },
                        },
                    {
                            'name': '}ѽgŊ\x88ɃǠ˲\x8bΠΠǾƦ˛ΕȴºӍѶģіѓɷŽφҜӖʹɤº',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ʷѿŃņФħҹMƮ˥țūȜĪƮɵғΜäƘĹΆҏĮˆÏҊ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'с',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'евƠ\x82νҷүΞϳΕǠɚtͶê#ύŰôӆƵ\x8dʷәɼͶԥҢǒǋ',
                'message': 'αȩ`Ѿмϰ5И˕ÈΎɈѽˏԝ~ҁŕɿι҃;ɧʹ¬ȋƋͻʘК',
                'arguments': [
                    {
                            'name': 'RŵҢəĺĩӫǺƼԝȝԍƳPΦŖɘͳΐӾĎřӚ¸ĻіƄˏҰW',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220522:173128.016782:+0000',
                                                        '20220522:173128.025283:+0000',
                                                        '20220522:173128.033706:+0000',
                                                        '20220522:173128.044072:+0000',
                                                        '20220522:173128.053853:+0000',
                                                        '20220522:173128.062723:+0000',
                                                        '20220522:173128.071363:+0000',
                                                        '20220522:173128.080360:+0000',
                                                        '20220522:173128.089533:+0000',
                                                        '20220522:173128.098672:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'υӱƚ¼àſâƁř\x88ӇǢ¸˥ҔŁŹ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '˞ӝȪá7ΨԭһĖϯ#ΘŀƓΞɝȣЯу}|ȎâѶƔԕϏғcҬ',
                                                        '8ϮǤPǽπџ҃ҽɤɠcǳӊθѠˎʐ\u0383ΦѶƞŮӇˁÕҞѸҗɇ',
                                                        'ЭęʐƩБUFл˺ƛđκˋſӺωʐȠȭӣəǺӱͻǞҼ%ˌɱԍ',
                                                        'ĮϟƠυԌĆѫϴӑφˠКʐċɽûǃѬѿ\u0380ȣҿʅ»ʪӃǌςӁy',
                                                        'Ɋ£Òɍˌȳ˰Ԑɞː˪ͰˀŷсǼ΄ļјȅȀǖИXĨăӗá҇ɢ',
                                                        'ЩҒɐƧҦԏҪʖЖŉӖϐÓˣ%Φ˜ʙųĪʜҲДŔǡӌДŭɄ˚',
                                                        'Ƿ˞FʢΝОЦŤқЩ¥\x87ǟϯ˛ϷŴ˸ёΐ\u0381Ƒ±ҕʹҹ¨Ѕǰň',
                                                        'ˎɍȯμѬ¥ЙƞрϨϔЮϒaÓѴĂĈƃɜȟЪ~щЃά¸ЍӜГ',
                                                        'ĝɄҡêŲѦ\u0379қ³ʠԉԁ%ˊԣґɅўԑ\x81ŉϳ\x8c˒ЀȰɵҗψϓ',
                                                        'ƆæҴʏʂ˫УTĦӕʲȊƿƁ)ԗ˱Ϋüàˮð(ӆϑǴӒӹ\x98ǩ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɏEÑϥ¡ȹΣѓԨώҪԇĠӢʷӋ\x9eѼҖŴ˕ЃАӍӒƠμíôˠ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ʼȐ',
                            'value': {
                                        '^': 'string',
                                        '$': '\u0379ˁΠӁԕƀгAФѽгʼͻѢΫʉʑ%ɯŐĪеӷɈҟƾӓЙȽΣ',
                                    },
                        },
                    {
                            'name': 'ѝ\x9dǰ÷ЙɨЂʽʇăƀИ\x9bŠɬҸfǅˑƦʦĥȚKƭҰΫҮǀa',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ì\x8e˱ΒȈ!҄ȀѽίǛL?ǣΞƧɵ}эŜƔMđϬϕҾѕ\u03a2ɮ\x99',
                                                        'ǆ˅ДԝΑÞƲò˶ԭԚЁĀeɌƭŢ˭ΣѦɑƒŁǊэ˩ģнӸĄ',
                                                        'ҳǍӜȔ;ĶƓΣ2υȇнό˅\x8bΠϭҶԂҟƧȶčуƎĸÊɂ6\x8e',
                                                        "ӕВȰµƢ@ѳ)'ʧƥϫѹэзŃ1ĳӅ˶҃҉\x9cɂÓѴЙɶɕù",
                                                        'ҵϲβƯʔˊǫŋĩʨԪ\x93ϴŬͿЮ˽Ȥ\x9b1ɯ˯ƃǊίȍįĺUѼ',
                                                        'ӈЉѮ·nԪȖĵ%uҠ\x87ǥε҆âӆʎжȓƾ!ԇĨӾѰѿƵȊm',
                                                        'ʳ˦ÂķƅƙсŻƽʕˣΧėЗԊΧӣĚЫ˭ɳŽʘʪϼΪε÷ɵǛ',
                                                        'ЀɣÐ\x92Ӿɑɀ\x83ЪÞѻƟыǙǋy¡ьЋøŅԤǴĲȭ2ɒŔЉþ',
                                                        'Θ\x9c#ӵ^Ȩ˦ǜϺDͼӄ·íΖ1ŋ҆ģхƥ¨ä˦ƥѭӂǑԭʛ',
                                                        'ŏΘӁƚɠϼΖŪȵѵȩѝ˨ҰƞΌҮυѨȰǒЦȜԣŖƩǑӾȡɂ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ϒÄӝҋŖĿӲÿƳўʸѫԊҷŐ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ŽЇΈLŴҾ\x90ФӉɧŒāҘӋCҖíŖŽJѪȑʜԕȓАӪtԍЅ',
                                    },
                        },
                    {
                            'name': 'ɭʧŎĲΆǍʰҚːƀ=ʕΏȘӸŃǟϦɍ\x93\x84+ҖĖ\x99ɐŵɁʰɶ',
                            'value': {
                                        '^': 'int',
                                        '$': 3899351840113127719,
                                    },
                        },
                    {
                            'name': 'Ƹ˽˵ԍŲͲ҂ҕѡϖϤ¶ɡ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        870181.7889193585,
                                                        978953.0232373588,
                                                        374887.68261262274,
                                                        945389.4942385546,
                                                        501504.98646195955,
                                                        626789.4088958568,
                                                        2471.5362595237384,
                                                        802899.1239349992,
                                                        344869.6718943387,
                                                        889293.2883844645,
                                                    ],
                                    },
                        },
                    {
                            'name': 'εѽЕҗƷÆȂ;һƺԍ\x928ʄ˳þɻĴҏϧ.ΎnǣȻŰŚӚɗΙ',
                            'value': {
                                        '^': 'int',
                                        '$': 1848448768847085814,
                                    },
                        },
                    {
                            'name': 'ӈȞѷÄKĞвӐʽяāԛϼӺϑԮҏȼʉҘˢΝΦіǉǷĢԓ,Ǽ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'IȴϏƦ˟',

            'categories': [
                'invalid-user-action',
            ],

            'error_message': {
                'catalog': 'Πԉ',
                'message': 'î',
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
                'identifier': '2ÀžθВɫ\u0381fǆǎϖϠУɮЫС\x89\x8cčϰʓ˓Ĥ˯ǨʪƤŔľ\x83',
                'categories': [
                    'network',
                    'invalid-user-action',
                    'invalid-user-action',
                    'os',
                    'network',
                    'internal',
                    'access-restriction',
                    'invalid-user-action',
                    'internal',
                    'access-restriction',
                ],
                'source': 'Aʸ\u0378ŲЀhÞА˚¥Ț˟Ƽѡ˸ƃ;8ʲҒ˱ǺόԝжªƋÏΑ˵',
                'corrective_action': {
                    'catalog': 'ԟ½ȝϻ əͳҚȍнѰԂЯàӳXњ\x83ǭʐЋ˹ԍӛјԬԧςϖ¡',
                    'message': 'ӱȢɬǳҦǛŔŕTЩԫͰӭʐӱǐϏҸ˰Ǳɾ҆X\x91ʫϼϋǒВԤ',
                    'arguments': [
                            {
                                        'name': 'ÖșЪɎşѲɤѮưŸ˨ĜÀеΪϧɧūʽјȳѪ˝όʨХΚɅѭğ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1463301206571501106,
                                                    },
                                    },
                            {
                                        'name': 'ӥλΑҾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173124.323574:+0000',
                                                                            '20220522:173124.332498:+0000',
                                                                            '20220522:173124.341243:+0000',
                                                                            '20220522:173124.350048:+0000',
                                                                            '20220522:173124.358969:+0000',
                                                                            '20220522:173124.367380:+0000',
                                                                            '20220522:173124.376534:+0000',
                                                                            '20220522:173124.384956:+0000',
                                                                            '20220522:173124.393136:+0000',
                                                                            '20220522:173124.401682:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʳĊLΖ˜ǈIDϊɂƚσ\x8eΣ\u0382эȑĿäɱƱĳ҅ʁϗԊćҸƔU',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173124.443595:+0000',
                                                    },
                                    },
                            {
                                        'name': 'бκќŲ&Ų',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2158253261479396926,
                                                    },
                                    },
                            {
                                        'name': 'ɊÇЄȽґȖаǼƕŊώѴϩ¹Вɿ\x8fǊƶØϼóˎåŭŲҭĭē',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 756853.9051817714,
                                                    },
                                    },
                            {
                                        'name': 'ßΩʀНѯˌ\x85ӥɓΓӁɜ,Ч',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6688268828047233235,
                                                                            -8518281402034759254,
                                                                            -2445804386652716846,
                                                                            -3001967256753749486,
                                                                            1507174819810432070,
                                                                            -5181710657263577698,
                                                                            4418771418827356187,
                                                                            -5980193618509502549,
                                                                            438245012213607353,
                                                                            -867620376243788941,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '@ÆÁĺ˲țӹԢ[ɶЁɽϴϑʸ òʘêӇĩўͺԄ\x85ҵЄh˯ɨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԝàɜтʣНіŽΕϨ\x80ɯɋąϞɧƨΥȈ˥ɞΖǄӦ\x8fΎǤȳť.',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'иɊӍȐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173124.723312:+0000',
                                                                            '20220522:173124.731561:+0000',
                                                                            '20220522:173124.740525:+0000',
                                                                            '20220522:173124.749564:+0000',
                                                                            '20220522:173124.758736:+0000',
                                                                            '20220522:173124.767074:+0000',
                                                                            '20220522:173124.776144:+0000',
                                                                            '20220522:173124.784837:+0000',
                                                                            '20220522:173124.793945:+0000',
                                                                            '20220522:173124.802660:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѵ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            389125.29620004835,
                                                                            739868.4014061237,
                                                                            644894.0347195823,
                                                                            212291.30834505812,
                                                                            371242.14855035313,
                                                                            899060.5358604377,
                                                                            500336.8866133243,
                                                                            425034.5283847024,
                                                                            479157.5673373169,
                                                                            74893.91427527138,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɮȑӽӮÞσʧѕ«ŉ\x84˺Т¿ʉȵˢȪҋƐɼĖόЂȳĺѲÊʡϗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173124.969611:+0000',
                                                                            '20220522:173124.978732:+0000',
                                                                            '20220522:173124.987693:+0000',
                                                                            '20220522:173124.996910:+0000',
                                                                            '20220522:173125.005392:+0000',
                                                                            '20220522:173125.014188:+0000',
                                                                            '20220522:173125.023580:+0000',
                                                                            '20220522:173125.032687:+0000',
                                                                            '20220522:173125.043052:+0000',
                                                                            '20220522:173125.052136:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ҰИȎiҜơČΚԏӗԜӖʚʾoҿĸѶȊÊҪɾΚǩ˫ǫǹǙǍu',
                    'message': 'ŹҳƎĹ³ģȝуĂԐͿ\x8dɿ˕ĺŀöɋùлō\u0383Ίʜ˒˦ѕёǐˆ',
                    'arguments': [
                            {
                                        'name': '\x98˒ŧǧƦԝϨЦɄǩǕÁȻѮѢ-ɐѭɋҰΥҍʹΖŹԢŜѤ΅¥',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': '˂ĦľɹǿŊĿϏӋÒv[ƁΌͰRЭȱΣѸΌɛɀȌąΣͷϖȅо',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173125.250524:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѹìδҘʊʑКԒðӖҳǟȴīȖΕƋƽЊǆ˃ʆǥ\u0378ҍǞ˅\x80',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʐŠƩŭǃӽɻʴɇϱśϤʶȱȹèǯǂɼʂ_ȪɨYЊӿҤɗˀƨ',
                                                    },
                                    },
                            {
                                        'name': 'ґΓvӶӟ=|Ο˰ұęǪp',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 972423.7511237832,
                                                    },
                                    },
                            {
                                        'name': 'ȧıˡˋσɾǵİɫʄϵèѬӏÓEƍƜӝ\x96ϋӿYϺvĸҴȁš˫',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173125.356344:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҺӒĴˉϽʍkόˈǃţĨeѤҞӽЇѳ˾ƻǻҍʀǀ˚η',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -9169892109547747632,
                                                                            1987171873315193889,
                                                                            -5885322484020866838,
                                                                            6207215940950898951,
                                                                            -3259668984934059686,
                                                                            4350565774277068088,
                                                                            -4248428128039960052,
                                                                            -5943493120052833303,
                                                                            8229384684723731814,
                                                                            5479185833816950048,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǅɢ',
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
                                                                            True,
                                                                            False,
                                                                            True,
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
                'identifier': '҈œìЏÍ',
                'categories': [
                    'file',
                ],
                'error_message': {
                    'catalog': 'ϸӵ',
                    'message': ')',
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
            'locale_code': '7ϕÇ£Ǧ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ӎ',

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
            'catalog_name': 'ӱ»ˁϙĔѻӳһϷ˯ġȏΐŐѼҁ\x9d¢˶ɳґѲϪίɭсƞĭҪР',
            'locale_codes': [
                'ȓȰ',
                'ŕqΏюǄǌҞĩ',
                'ĽχɰΘƌ',
                'Ҹ¬ʊ˲Óφ',
                'ѻäĕ',
                'ŊѺΛɀ°ΑŕͺԜ',
                'Ԙ',
                'äBѷ\x9bϭԏƽЛ',
                'Ɵ\u0383уŏȈ',
                'ȴxɺ\x83',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ŋјq',

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
                    'catalog_name': 'ÐÐǓĬȖ˨qЄεȐʼʹӾѓÄЄŭ_ʚýȱ¦',
                    'locale_codes': [
                            'ҖЀɎԘɬ',
                            'ȄҶØсЙ¯iЖÆȏ',
                            'ØԠλƼȱ×Ӡ\xa0',
                            '˲hƲ.ӭηĉǖԃ',
                            'зҧ\x81',
                            'ѭȪvπϔöӣĬӈ',
                            'æƽѹѺn',
                            'qԩƽȇԍϰ˟кn',
                            'ЬˀeњЅ',
                            'ÒϙȤ[Ӌ϶ǬʬĄ',
                        ],
                },
                {
                    'catalog_name': 'ҨȣŶȷҍķЛ˹ӭӕ5ʦԎ×?ҌP/ēОόљѱǕ˩|ԇҧз˔',
                    'locale_codes': [
                            'ԁдүǇ˧ ôӺξ',
                            '¶ͼϷϙǒ%Е',
                            'ԈƚȄӈƄ˥ԡ҉',
                            'ðŘƵ˗҇ɛϱɜʩ',
                            'ŮԢÔʉ¹ž',
                            'кčԦçʛŋȝΘ',
                            'ÎàŨӦȸ',
                            'ϟǌƄʏ',
                            '˲Ӭίćd',
                            'ƩƍϊƧϐ˄',
                        ],
                },
                {
                    'catalog_name': 'ɀρʺґʒƧÁԤėǋӰѫͶɦʛǺzK\x9eŬ˄΄Ԯà¾Ϸˁ(Ԯн',
                    'locale_codes': [
                            'ǰȯЯЎ',
                            'Ż˳ʨӧͷίҚɴ',
                            'ήԠ1άǿ',
                            'Ȕԧ˹:õˇΪÊČҎ',
                            'ę',
                            'ԥȊЦėɯ',
                            'cӋχч҉',
                            'ӬΪȆ',
                            'ŀӜгчŵґĐƓĢҪ',
                            'Ώ',
                        ],
                },
                {
                    'catalog_name': 'ʼȋЫÀʩƄʻґӌнãЮĜТÛŊҍљҗƖоƹĮÃέƻÊИʑ˓',
                    'locale_codes': [
                            'ϱýѿҚϋӸʘ',
                            'Ǧ;ҢɆǒŔ˶ϋ',
                            'ρƅĨϬЙԠϡ',
                            'ʏ',
                            'ʸяӽɋ´',
                            '˦Ƞǆɧ',
                            'Ƃxːѧ˞ӬѢ',
                            'ŰΔьÝ',
                            'Ғʠz',
                            'яЦ˳ʙ˒;вĖ',
                        ],
                },
                {
                    'catalog_name': 'ȯϥǅӧ˚ʐƷЕȤ˳\u03a2ɋƸ˫χЛЧҾ{ċϙʮɮǐğȵǽ҅Ѹà',
                    'locale_codes': [
                            'ŷʜ£˃',
                            'ʻ',
                            'łӴʱǹ҂ɺϊ',
                            'ƒӧѪ\x8dPƉϟʍǓЀ',
                            'ǙҷӰўÛ«ĳҔúÉ',
                            'ğʭґ',
                            'ƷҸº',
                            'ƚ2ԅ\x8d6',
                            'ʍ',
                            '\x8fǄͲːæԡÊ',
                        ],
                },
                {
                    'catalog_name': 'űφӝ˅`ӎΞСϽȋħϊҲϥʵȶ˝ȏŗ\x9aͼźňˎ\x86ǁĒàƎ¤',
                    'locale_codes': [
                            'Б\x84ȌЊôҦшӺ',
                            'ϱҸƗϗˢʳξǌƩ',
                            'Aӎǟӊџ',
                            'ԣ',
                            'ʟŭӝ҆˕',
                            'þΤĴѼ˾Ð',
                            'ȮİʺԨ',
                            'ҳÝȤǧǶǈ\x83ͷϙɹ',
                            'ƧʓηXӖ',
                            'ғԙĢѶʢ',
                        ],
                },
                {
                    'catalog_name': 'șѫҼgƂś©Ó˙˻\u0380ʘғӒoɑ˘hčңȏԣ\x98ŭĮԠ³ſϯʌ',
                    'locale_codes': [
                            'ŖΡˍ`ϥĀ',
                            'ν',
                            '҃ʖщɱ',
                            'ҷ',
                            'ţ',
                            'âGг',
                            'ЊŧɁ',
                            'Ԣœª˝ÁǙȨíʫ',
                            'Іŷ\x8fҋƘѺќn',
                            'ҭϕ',
                        ],
                },
                {
                    'catalog_name': 'ђY϶ЇźȚһμͳҋ΅Î˲ˢ2ͺґɫƓӴоеĿϨˏӇ˵ӎ\x9aů',
                    'locale_codes': [
                            'ȠąҜȻǒƚςʟ',
                            'ҳԈǀБæɮ',
                            'ΊǌԘ©ù=ƪ˼Ӵ',
                            'ġͷG\x86Ԟ',
                            '×ΎŨѴʄ˸ξƨȊ',
                            '/нɆ˷pǛ4',
                            'ҕ*',
                            '\x80\x8cԇĔԥ',
                            'ʰõϵдȌӚԙ',
                            '({ΊÄҷ\x80ҦӦˋ_',
                        ],
                },
                {
                    'catalog_name': 'Ǣ҂ԖҤƛѼɸѵɜǣ',
                    'locale_codes': [
                            'Ѽ',
                            'Ɵǐюȫ¬Ҁĺ}d',
                            'ȣŝǸ\xaduʉŎ\x8e',
                            'ϫɢ҄',
                            'ɬέɜ',
                            'ȭˊъǇα"Ȝ',
                            'UǈǰÜЃ×čǵ',
                            '\x85ğț',
                            'IǊ',
                            'ѸɌϕÌ(˝ɲˌĬŉ',
                        ],
                },
                {
                    'catalog_name': 'ɼҧǹǐ¼ŜȤέZһҶΎƔѸͺԄƙϭυŌʍɮƆƨǶőƖƏɏѱ',
                    'locale_codes': [
                            'ѶĨ',
                            'ȕ',
                            'ʿųҬĤЍΟ',
                            'Ӷ҇ҨԦŏ˪',
                            'WўӇʴҭ͵ĪâƓџ',
                            'π',
                            'ėß\x98NJԨħ',
                            'ЦˑԁϻǴ',
                            'ӏԆ˃ˉκηʁó¶ȭ',
                            'ǧȺįҹ×>ĐFӕȱ',
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
            'name': 'àѥϖ¦ʇƟʶӔϋ˗ҸɻРșɨȣ˶ǙʠɦϷҐJ\xa0ΟĺΈɻԒȒ',
            'code': ',ѻѼƇʽњǉʊðō',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '_',

            'code': 'ʽ',

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
                    'name': 'ҷχ7ɕԭ˻ӝϕ˷ȑԭĘʈǨʟʿɶ\u0382ưˉƞО\x7fҼѻөÙϥ\x82ʀ',
                    'code': 'ê',
                },
                {
                    'name': 'ȝΛ½¨Ѝņƕ΄ѽӥ˄ҚΥŶэͼĸԉŉƙьéȱһ\u0380Ӳɮ\u038dмд',
                    'code': 'ϺӌʡŨȥ\u0380\x81ЋԖӏ',
                },
                {
                    'name': 'ɿЍΝȉșŪīȦһœӆ~ŠȼȤrÿUԃ҆ԜӦє\x8bÆԪӧVʑў',
                    'code': 'ҡU±čǨǮ',
                },
                {
                    'name': 'ȟʈŤаʪ˘іȗqÔ\x85ӲǻǵĭT%ѺŴҾƱа΄ƦĚƂƴȼʇЕ',
                    'code': 'ɹҶɿɉˏҸ',
                },
                {
                    'name': 'ǙŬ˷Ԑʠǭ_ҼϴȫĻÿˇˇЄûҸԓŻȅʹǄ\x97ͷ\x9f\xa0ɦιȍç',
                    'code': 'ЬɎɭˆˠ¯',
                },
                {
                    'name': 'ăʘ˱ЯХңʃ˕Ώʬģ;Ŧ+\u0380ЊϽѿ˭0ϚѠÁʘȚȥҴ)ìӕ',
                    'code': 'ˬKǸƏ²',
                },
                {
                    'name': 'ϞɈŲtƉɧ¡Ӥɷ½ưгϽʍä˃ÂrіфŧʻӺȑ;ÈЫÿªӪ',
                    'code': 'ƃ',
                },
                {
                    'name': 'ΝĲξǦėӠΔ\x83ѶΜ;Ì\x93>\x93ԦÏ»ɞȳƳǮǰΰ˟˚Ŭʘ´Ą',
                    'code': 'Ζǹ',
                },
                {
                    'name': 'ȴʈɥʡ˒ы\x9dVήΥ˃IҁͲ§ƟԐŔØϻĥȱńΖƅДЗʭʸҳ',
                    'code': 'Ӥ',
                },
                {
                    'name': 'Т˝¼ȭҬӶɈ˖ɥʨŮȒҨÁõÛ¡ƒ͵ΞƣǚǅȱǢϞӦƢЫ;',
                    'code': 'ҔЎ',
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
            'locale_code': 'ũˠ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ӱ',

        },
    ),
]
