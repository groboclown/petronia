# GENERATED CODE - DO NOT MODIFY

"""
Tests for the binarystore module.
Extension petronia.core.api.binarystore, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import binarystore


class StoreDataRequestEventTest(unittest.TestCase):
    """
    Tests for StoreDataRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in STORE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRequestEvent.parse_data(test_data)
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
        for test_name, test_data in STORE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='mime_type', name='StoreDataRequestEvent'),
            ),

        ),
    ),

]


STORE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'mime_type': 'ğɧԐӧûȲѴӘԘÄȡ\x98ϩɓVӄȹģΥҊ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'mime_type': 'ξƥв',

        },
    ),
]


class StoreDataAllowedEventTest(unittest.TestCase):
    """
    Tests for StoreDataAllowedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in STORE_DATA_ALLOWED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataAllowedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_ALLOWED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
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
                res = binarystore.MessageArgumentValue.parse_data(test_data)
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
                res = binarystore.MessageArgumentValue.parse_data(test_data)
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
            '$': 'Э\x8dǉ\xadƄʘ\u038dȯɜŬȤЎĸ\u0380ǳђ\u0380â˒ԑĩóлͷđɕƯwƂȗ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2565772482387592732,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 55546.04974024254,
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
            '$': '20220526:211115.972003:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ΑЩĦӂǈ˓зƗ\x87\x86ǙћԨϨȂzë?ц&ŚџТԃÅʗcΆˁɆ',
                'ǅИˈƋԜš<ʬ§ˎkΥóȹĖλυê)ФŊʊ҇ϳўģʨƞˁҿ',
                'ϟͽƩȭúƌ\x93=Ҳ?ƗԦÇѐОĦʒʋϋҴƄȬ\x8bҥ˒ϰň9ѭʺ',
                'žƿʄ҉N·çҀӐŽδÃʈčŸʓҜǙǰϬǺƆɹΝvbȠ\x8eơǚ',
                'ѪɣѝȩǾ@ɏÙɷӎĶ˛}KáƐ҈Ͽͽ˂ƭʡеTɳ\x8aϣóŃӨ',
                'ƝϨ2ĔąġǴȳӜџ\xa0ήΐѧҒ\u0381ʌŀƖȉNκɝǚʄʈ}Ȼťΰ',
                'р\u0382ʷ˩ѩʶΟʖȗӡҎӟn˻¢ÒɴоňƕʓŘȸǿЫΞнҭĝƓ',
                'ɇѳųwѓʍͿɟζөˍҩϕéсŰ\x9bǵ\x93ъϜĺԦ\x87ήΣŶ/д҄',
                'ϒкǬąƩȇǶӫÏÖҌʺϠҊːόΰʱԂʶf«¹=гԤĹʼÔȁ',
                '˟QДӀâíτЊš:ҴāѣɎgɉŤƐνΌ3ӢMʗӠʩϧҷɒѡ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -3877875751407015866,
                -5899173167960800155,
                6489400378689121790,
                4596609365508328232,
                -2132028293447129067,
                -2414106439033819750,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                391820.7878788244,
                232315.1738891785,
                645963.7317176142,
                708792.250984538,
                799464.7457483914,
                642257.3057117466,
                492696.4237421175,
                661528.6862701486,
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
                False,
                True,
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
                '20220526:211116.967692:+0000',
                '20220526:211116.987033:+0000',
                '20220526:211117.009335:+0000',
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
                res = binarystore.MessageArgument.parse_data(test_data)
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
                res = binarystore.MessageArgument.parse_data(test_data)
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
            'name': 'ϾХʀȎуҲһͻіÌһɑүƑ1ŨԋňϦȦŊȜԤӏѬƊȘ˔Ϳn',
            'value': {
                '^': 'string',
                '$': '\x83҃˞\u0382ϛöɳȔˎԤƟαчĦAɽOϞű(ҨE҈SηØÈÖГź',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ӊ',

            'value': {
                '^': 'int',
                '$': -5395734502212556643,
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
                res = binarystore.LocalizableMessage.parse_data(test_data)
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
                res = binarystore.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'wpİ®ȾʎӓѮ љȇоɏsԞΧћǳĨ҇ѿцΣĒΧƸƌʥÓŲ',
            'message': 'ƭϾBƗήЩѿĻъˎƷѿĽɂcԔ˕ϬϔɹӐȃҁ˽ϓÎǢÍȢ¾',
            'arguments': [
                {
                    'name': 'ѕCÿхŴҟĖ҈Ģ(uʩʥHϖφłˢǉ˩ҶǏ¦ҿЅ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ǦUвҶҿΑԧˊɬэŹ˂Γ1ZeЕʕΩÙÍԦіǪѩbǚϸɲƁ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'бΣɯӨưДӽʇɁȉȭɺ',
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
                                        False,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ӗňԨιßƑӌӱ±ͶŬȹ\u038bГӴϣҕФӒċɱұ;ҧȇĄĳɼēί',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ÄěǥƔMˡ˩Īϰ.ƶʡӥЍиǚϞʹȈ\x8cЇȟӡºҞϭǇĎŭʃ',
                                        'ҮӉAҊ6ӉÖďИїâȇїɭԞŉғӅЯˬªԓӌŘԗңȑόīć',
                                        'Ғ˭ĺǧɫŲƍǒƊΟŏІȐ+ȉѩӘπŋЈKČƾµĚϗԌ\x8bōϞ',
                                        'ЀϺ˴њƚϴӄɌµʲѫ\x8bԁ˕ϲ\x99ɔÞ´Ԕđ˙¿ŴϬЎŵðɁɑ',
                                        'ʥӥпĔѰƠӚҾϜȋ˱ѦȱӬtƺħȏĸĳǝώÀǁġďƀ¸ԙӱ',
                                        'ϰlЫԠѳϑъýòŴ3˓ÒMϦӏΖƁԊοЃˮvŋɺИĩҝϢʬ',
                                        'ӆǚα1ӌɱͲȵǛцˆҲɄδʑĝóƉˮɗ°ŴΦL\u0382ġԜnӹ\x83',
                                        'Ӥɼƚ&8Ģҏèɼȣŗb҂вΙ˼ɝЁҾωʇ ѐĚŚ\\BϢľȉ',
                                        '\x97ԖąĻӪ\u0380Ș%¸ӸĂ\x99МЧàˁʭũ҉óʿÍöÃŌɦŀɁµ˹',
                                        '˩ɹǌ!҈ÅÿΰӂEĩʕ±űť\x8cˎʖƇͽ"ѳД˞͵Ϗҥƍӕƹ',
                                    ],
                        },
                },
                {
                    'name': 'ԫqɕĭ',
                    'value': {
                            '^': 'string',
                            '$': 'ˀΜѥʖΙxȞγţƙѼлɔĊδȄ҆Ρ˚πŊˬǊӽÆѦ˳ŁɁ˝',
                        },
                },
                {
                    'name': 'йСǘɟξĦE¤WѺ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ϴƩǆʲɕͷҳ˲ʶŞҦ+ǓŖэ?ɭӤМņŨîҧζȹɬԃԭģǟ',
                                        'άӮ¤ēɪɥˆ˩Ŋʲʯˮˀ\x92YĀӥŢ˦Ţɑϳ<\x98ŞΎԐʸĶӧ',
                                        'ӛӍΠÒ\x7fēłϮƝ^ƨȎƭąϖ\x8dăqǰӟńȈԞʡ½ηɢ˸ӭƎ',
                                        'Щȉ\u0379əҳĎơȮ´ӅєѣŪαѭuрк3ϛȯϊńӿςįԄŋ΅Ϝ',
                                        'Ѩ˸\x9aÕиÕμϤεĔ˵ʞФCʴϐчƚʄҫ>\x89ʯȉҙϐӦșƁǆ',
                                        '7}ɼ\u0381ԢŃӐÐаʪҠЯι\u0378˻ͳʯӥ\x88ЇƝɢɋpǱϞΌȦԨҎ',
                                        'ʹHșӱόΡčӯǖϟϵſҌϹЕШ\xa0υԫƄȡɉϐˡĭƸӻӐɹϿ',
                                        'ɯԛʱpРGʄ\x81ʺŮʭͿөʓǮЁ\\¡ҙŪƟǍȣΏ¿˴¡ԘғŁ',
                                        'ΩǡŚ˯ԔHĊ\x9aəzѤ5ŷЙҨӁҌOűĀ϶χӡʃѺĪˣҮ>Ǎ',
                                        'ϞәІ\x85ʿˌϑȗ¿Wʵңɀʻ˝ђȩӴIɓ¸Ά¯ʿш\u03a2ǙŊĤȾ',
                                    ],
                        },
                },
                {
                    'name': "Ƅæ\x8aɁ'³Ҫ!ˮ¹ǀ\x83ҜȦГÚȁRȈҕʝʂǂҺʪ",
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220526:211114.866657:+0000',
                                        '20220526:211114.886302:+0000',
                                        '20220526:211114.906324:+0000',
                                        '20220526:211114.925467:+0000',
                                        '20220526:211114.945120:+0000',
                                        '20220526:211114.964359:+0000',
                                        '20220526:211114.986018:+0000',
                                        '20220526:211115.005525:+0000',
                                        '20220526:211115.025246:+0000',
                                        '20220526:211115.044812:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ԢЪЪǓ҇',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '˾ˮęӄɣ¡ӥѻȝ\x86ʣʚˤρʃ˭\x88łìЄ9ɜϒЬ²ȪȀȬν',
                    'value': {
                            '^': 'string',
                            '$': 'Ԋˈl!пͷǤ\x92˰щəЏĦǽЕԞ¶ҮΧΨԚɜ8ȞˊɁ\x92Ţʻ\x8e',
                        },
                },
                {
                    'name': 'ɄϑҴώp҆О҆ҋˤпǙ˓[Ŀʞ¨ǔ΅ʖkЙƗřϥΩĠĚą\x84',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220526:211115.303014:+0000',
                                        '20220526:211115.322321:+0000',
                                        '20220526:211115.342114:+0000',
                                        '20220526:211115.362040:+0000',
                                        '20220526:211115.383261:+0000',
                                        '20220526:211115.406686:+0000',
                                        '20220526:211115.429162:+0000',
                                        '20220526:211115.451643:+0000',
                                        '20220526:211115.471608:+0000',
                                        '20220526:211115.491672:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԕ\u038d',

            'message': 'Ҿ',

        },
    ),
]


class StoreDataRefusedEventTest(unittest.TestCase):
    """
    Tests for StoreDataRefusedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in STORE_DATA_REFUSED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRefusedEvent.parse_data(test_data)
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
        for test_name, test_data in STORE_DATA_REFUSED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRefusedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_REFUSED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='reason', name='StoreDataRefusedEvent'),
            ),

        ),
    ),

]


STORE_DATA_REFUSED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'reason': {
                'catalog': 'μəѱŴȥʚΞǔƖй\x8cҼƚШҡRāѕҚʊιȒľԚԂɄдƈэǊ',
                'message': 'Ć\x84Ĉ¤ĸz\x98ŨӘȰƼƆť˺ǖ˃ŌΈԉҙēˇԋпČʟȜþΛɡ',
                'arguments': [
                    {
                            'name': 'ԕƕҫMϔͿĶȔ§\x91вǕȌɷéӚɳĢӆӬɽ\u0379®ҙ\x7fơ\x9eč',
                            'value': {
                                        '^': 'float',
                                        '$': -62159.627932758085,
                                    },
                        },
                    {
                            'name': '΄ΐыҙăπϷɽ˟ӍІǺûьϦͰδԦıаɕŴâƟοʲΝċĉȺ',
                            'value': {
                                        '^': 'int',
                                        '$': 451927823435828936,
                                    },
                        },
                    {
                            'name': 'ȺĞĈɗϰŜ\u0382ӡʴԍƅ»Ƶżиγ\x84',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220526:211112.256520:+0000',
                                    },
                        },
                    {
                            'name': 'ƨȩƴȦƻѶӬɦԤbȺaʝ<ʫ˹μʞ\x99ȉ҅˖ȶӣͻįș˵ŧ҈',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220526:211112.344467:+0000',
                                                        '20220526:211112.364230:+0000',
                                                        '20220526:211112.384120:+0000',
                                                        '20220526:211112.403213:+0000',
                                                        '20220526:211112.423025:+0000',
                                                        '20220526:211112.442225:+0000',
                                                        '20220526:211112.461953:+0000',
                                                        '20220526:211112.481220:+0000',
                                                        '20220526:211112.501065:+0000',
                                                        '20220526:211112.519542:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ԛĥ˙ȌƝIϲǰϬÏ\u03a2мȬԗЋǨȐ˚ϭҏƙҚʡΧć\x93Ǔmɮ*',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        570987.7173309316,
                                                        797023.8321735713,
                                                        923343.3665329765,
                                                        229160.5464416021,
                                                        970691.0022884896,
                                                        98912.24827796905,
                                                        417420.52565469756,
                                                        936682.1455670116,
                                                        507228.1417215363,
                                                        856931.473813681,
                                                    ],
                                    },
                        },
                    {
                            'name': 'њϳϗȨoģϬʂǊωĖ˺ѶѨБʃ҅ɋɖɾŻҥгҚǆЕ\x92ʛo\x8c',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ќĭʏď˱ʄMÅҙˠ;Ӝ\x99˩ˤ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ĔϣѼƹͱжʞƊì',
                            'value': {
                                        '^': 'int',
                                        '$': -7385529780948226168,
                                    },
                        },
                    {
                            'name': 'ΎʵҲ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '"νŖ˼¢ЕŪʨɁϒɾȂhĊРȆ˕ȆũЏɳĐǑҤнĠȰɵԟΞ',
                                                        'ӯԄħɑÒєљ˩ѓԏӕ˷ʎGϼκ?ʁлüʳ˰ĉЦѶԁ¾ɴњj',
                                                        'ϩĈƌĒȡѼ˞ʧЍe\x93ȔĘgЬҌļFȦȤƈ\x81ʹϱΘ˥˳ӳřԃ',
                                                        '§ÁŮʴÖˠş҉ʋŨ\x87IчМѺE5YøѾß¦õ¤ӓɂǮԈĨԇ',
                                                        'Ǚǽ͵ԃǂʥƧɪȜ¯Ǟȯ˭(ѣжŎțŏӈʌš˕\x95Ϡc\x84ıҿǀ',
                                                        'ϏƺЦMҍɐ¯Ŧ˪ʍʚ˕[ŬŮˍЦĪɰŤưȃǛ\x8dхЋϷƫ\u0380ѯ',
                                                        'ъу˚ͶƒЌϒϲѪƌȾƲÛĨȸ@ο˷ȁ˰϶˕ƨӦҵѰ¾ĭЋӼ',
                                                        'ЋǟeƸúǴÏȸƱʗz\x86ͳǝ\u0383PΓ[ˤҁMʅϙÿѻҩ\x91ɠԟ\u0381',
                                                        'ĘŖϺˆҔҕҀΩϫɼϕʈԃҢʅѕɅȉȣԚӍə\x8bķǔƬǉ\x97ѹĨ',
                                                        '\x99Нǲ[ǹǶЭӜ˷_ҐҍſѻӵѣüŷӷʅһΐѢѴФɆǺɱǌӨ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĐЃŗʆȫ\x94ϯєʺͼøɂƔɥҲǁƽҚƢΘƤÕĨͽ˵ˀϾʡжț',
                            'value': {
                                        '^': 'float',
                                        '$': 118207.1766164371,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'reason': {
                'catalog': 'ŧĄ',
                'message': '¡',
            },

        },
    ),
]




class DeleteDataRequestEventTest(unittest.TestCase):
    """
    Tests for DeleteDataRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in DELETE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DeleteDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DELETE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class DescribeDataRequestEventTest(unittest.TestCase):
    """
    Tests for DescribeDataRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in DESCRIBE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DescribeDataRequestEvent.parse_data(test_data)
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
        for test_name, test_data in DESCRIBE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DescribeDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DESCRIBE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='store_id', name='DescribeDataRequestEvent'),
            ),

        ),
    ),

]


DESCRIBE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'store_id': 'ýĄѣԄfʫΟʩ˸ʉŊĥ\u038bҼăġ˕ƱĨĀÇɳșú"ğϝW˙Ã',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'CʁǫԑƸ',

        },
    ),
]


class DataDescriptionEventTest(unittest.TestCase):
    """
    Tests for DataDescriptionEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in DATA_DESCRIPTION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DataDescriptionEvent.parse_data(test_data)
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
        for test_name, test_data in DATA_DESCRIPTION_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DataDescriptionEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DATA_DESCRIPTION_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='state', name='DataDescriptionEvent'),
            ),

        ),
    ),

]


DATA_DESCRIPTION_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'state': 'unset',
            'mime_type': 'Ʀ¹ѽKҬȡѐ?҇n\xa0ӔČˇśŏƀΏŤʤÓΞΤӜȦ#ʾΉƩǘ',
            'sha256': 'ǏʐӥƂҫɂȯǒЎѿwɤѭСέΥӾϷǼûɶǺҌßȕƵÃԉǕ·ИӅѐ˷гӌЍʴԤҾԇʞәȖȼŕ\u0380ŃɮԔϓʺ\x9cǃĻ҅˷пȇĂӓÃƴɾ',
            'size': -8885200737575040241,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': 'active',

        },
    ),
]


class SendDataRequestEventTest(unittest.TestCase):
    """
    Tests for SendDataRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SEND_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.SendDataRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SEND_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.SendDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SEND_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='store_id', name='SendDataRequestEvent'),
            ),

        ),
    ),

]


SEND_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'store_id': '(вßlȹԋǕÃςˌ˄ɭƔΑˤVćʭ˯ˠ\u038bÀΐ{ҺǈҞӢʾʿ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'ιԢŻȨ;',

        },
    ),
]
