# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T21:03:13.205209

"""
Tests for the native module.
Extension petronia.core.api.native, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import native


class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationEvent.parse_data(test_data)
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
                res = native.RegisterTranslationEvent.parse_data(test_data)
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
            'locale_code': '-',
            'catalog_name': 'ӨÌƣӴªԝôԅԉӂ\x81фĝȿ4Τŗʨ',
            'message_file': 'ӑ͵кΠсҿ(ҰrȻɤĭƥƼǮeʧŗ˄ϭϐЬМьĥӔțÆЋŽ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ŭ',

            'catalog_name': 'ŘӦ\u038d',

            'message_file': '҂ϟ',

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
                res = native.RegisterTranslationSuccessEvent.parse_data(test_data)
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
                res = native.MessageArgumentValue.parse_data(test_data)
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
                res = native.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ɄϯȋɷѫӎЩƄҞ˗Ńʓќϵӑ˄ѣâˤ΄ӂľśƱЄѰͷɲҰΕ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 1303737157307570410,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 983303.6658129815,
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
            '$': '20210203:210313.152632:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'jȻǂȂɶɳą»ôˣÿыί˞ɥђŝģ\x85c&˱ӯɾŢӄJɡ͵Q',
                'ðЩͶ7ĐʬʐGԇȽ˕әɻϺѨдǫȢϰӧԚƆƠ\x88ΆǷҧ&ԉG',
                'ъӚʧRƤЌάԄѢάʞϏǞȒŌĠƩɲžtƄ%ӑʇІøѧĕǖÎ',
                'ʮЋÃɵЪóʤǞ˰ћɨ\x81ԂѠūąǒΨʶΐԧлĺԤȬǑ\x8fў$ó',
                'ҷϭӀήϬ¯ˠӋƹӏ\x8dӺɯҖȏŜџЇĮ¾ӋӋĖ˓\x92ΙʐΛөз',
                'ҦæӷɼüͷϣĤԛąˆƤȫѮ˺\x89ǖςǍϽƁЂӭɻǧ҈ʯưě\u0383',
                'ƱJώ˚êKДӴ\u03a2.ψôŽ϶ӄөбǄѪʽΓ˕ȧʁʊӑǴ˦Ǡβ',
                'ӆ\x80ѴHɒȝNƼ\x88\x94ĢȉЃ˟ǓҭʦDDԬȘȤǰћƮѦҋûӸŀ',
                'ΨСˬŅԄӧ:ɩ´WɹҹͲ҂ɮĚҜмȋʪo˺ǸɟϤҎʤәĿӢ',
                'ƿʺϫ½ƼƏ\u038dӸªÊÕѹТӭсοџ£ӇƍЏ`ěǒϡ҆|ғœԡ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -6397844198323741373,
                -6876126593702649099,
                8427397109284828042,
                5026603569162911756,
                -3663031422178204850,
                -8497792175204936688,
                815780730606334951,
                5354765072058047176,
                479181272239854555,
                -3888354938747715298,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                605402.2482995326,
                159124.68849573212,
                518174.42497979174,
                398840.7476019052,
                527615.0261223356,
                313004.00624936196,
                563599.286406838,
                590359.7204588443,
                786683.9882941685,
                30725.088129196316,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210203:210313.153468:+0000',
                '20210203:210313.153479:+0000',
                '20210203:210313.153485:+0000',
                '20210203:210313.153491:+0000',
                '20210203:210313.153497:+0000',
                '20210203:210313.153503:+0000',
                '20210203:210313.153508:+0000',
                '20210203:210313.153513:+0000',
                '20210203:210313.153518:+0000',
                '20210203:210313.153523:+0000',
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
                res = native.MessageArgument.parse_data(test_data)
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
                res = native.MessageArgument.parse_data(test_data)
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
            'name': 'șƒӂӦȾҒ˨Ɋ\u03a2ƉϝѫΤȪŠÓѻˬʼŮиӓˬƖȮψϠ',
            'value': {
                '^': 'float',
                '$': 629760.3439053227,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x8b',

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
                res = native.LocalizableMessage.parse_data(test_data)
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
                res = native.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'кȩϖƎȳħȎW\x9aŀυõӱ˧ўʉÓљʼӒӥσ͵ʩƐӢΛȉʰќ',
            'message': 'οƱÉӞ΅ġăЉȢˢ҈ǠʴȒԏЄϷНȰċŏͲƱ\x94ςĦҁŉzī',
            'arguments': [
                {
                    'name': 'дǖŰǵōɯɌ˽ӯӪԁȉҗώͺ',
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
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ҍѕѝ\x91ΖΕѥʤЄƅʻɴWɄԞѭѡεǅюДѴ÷ѳϰ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        706113.2012379281,
                                        728492.9080187354,
                                        263373.757861332,
                                        650482.4243405613,
                                        57631.05337396721,
                                        402870.92370653246,
                                        272614.1231228883,
                                        444043.7268857057,
                                        124392.59096731554,
                                        704707.0726495992,
                                    ],
                        },
                },
                {
                    'name': 'ŊңʂвĈӂӒ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '˳ӛǺ˹ҷ"ʿŰĎ\x9dΊɔȰϫώvȭ΄ĥŒɄӗҺʠҬΆȲơӇŢ',
                    'value': {
                            '^': 'int',
                            '$': 1316481975060641683,
                        },
                },
                {
                    'name': 'ɠǗːΈŞϨШѓӴʯԤOǀQѤҘ\x83ϲнɗʃĽ\x8bόѾӵӤēʂʯ',
                    'value': {
                            '^': 'string',
                            '$': 'ʵÈѻʋϒԡɚˮЊ\u0383C¢ыMʜтϧҀзȵƦԭȩĺǖĜKȇȴѥ',
                        },
                },
                {
                    'name': 'ʳϋŴ_ôѤʰ\u0379ӁϳʧƨϡҀԗϤԍȚʋӓҶbϲ͵ʡέˮҳиē',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -85666.19986402901,
                                        249569.32926599443,
                                        821643.3997442703,
                                        421156.1542039767,
                                        113574.3390624398,
                                        850081.7812330924,
                                        829831.2601420358,
                                        852062.8654055623,
                                        991860.8331200269,
                                        628209.9578937086,
                                    ],
                        },
                },
                {
                    'name': '˛ώé˓\x83˯ɗ˯l',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ƻǶχғșıҘ˃ʰѵȶԕȅǡÊɘѷʉҝϡҍϕêјԤbҏǀĐӓ',
                                        'ӗяŎΉж\x91õfĨӓ#ƽѪΤǼiœ(ӁԛǠļǟÀLDǳɁμƛ',
                                        'îΨѬӴѪʓɅȽ]˦ƥ>ʲ\x90:Ő\x8fΐū«ԬHҍ\u038dѾԃ϶Ȍ}ԣ',
                                        'ĠĦϪěÙГʯХŦȞNƑα\u0378ʂЁѐ\x8bʯыǪƑҲЅƸɂĂάǌϱ',
                                        'БԌȉŨύϢ+λňƐ\x86щӭхԖʸоԢ¡!ǈìɡĕ Ӛ¾Ϗϻԉ',
                                        'Φ¨ˍȒƽɨȇѳŗϚŀҿӓӾƌ\x94ÿӯлҋƤŢBȔ϶Ѱ˕\x93Öɶ',
                                        'ǤƏ\x85âŴ©^N+ÛϮɣɺŵоϾĢӞÊǄÈȾУ\u0380ʄϫ˕ӨΉ\x96',
                                        'ԍúΕƓêЮ¨ѠlʥшԦӒίȄŘӴʹԬҠʯȐȋϦǖíӷ§ÌП',
                                        'sҢĈÿȕÆʩЧҟҚƂπӛС+ťɪǼºщϭîεďʄˁϦΠϥҍ',
                                        'ÜΩЅ˕ƎĿȵ@ľƋХ,ĦɉНƼ҉ʾӂƤWѭԬɘȑїŞ ɅΓ',
                                    ],
                        },
                },
                {
                    'name': 'ɚǟʑRїӅϱˇљĨ϶Ԋ%ƻӽ[ƷΒ\x96ɨ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210203:210313.151708:+0000',
                        },
                },
                {
                    'name': 'Ц.ˍȷǫʅǚ˲ųʰЊ˵ҋϹϬѠŸӶМɀЊǖċў+',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ǇȽÚЭΚȷуǷɀʶȼ·Ԙ˫Ș1ŻЩџÚӻǣѺ҇ЌѸÐˉДԩ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        51046.03123105489,
                                        591115.4067603128,
                                        377038.1591599615,
                                        384357.5143852825,
                                        903621.8456229737,
                                        325713.97493514686,
                                        587555.2556124488,
                                        115186.98041668304,
                                        130104.93330761223,
                                        86312.18256293918,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ιԁ',

            'message': 'ϼ',

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
                res = native.Error.parse_data(test_data)
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
                res = native.Error.parse_data(test_data)
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
            'identifier': 'Ǭю°ʿќɑӛϞxöӪԄ˻фǌBĞĔОӪԦɯфίeîłˌĂʂ',
            'categories': [
                'configuration',
                'invalid-user-action',
                'configuration',
                'access-restriction',
                'configuration',
                'access-restriction',
                'access-restriction',
                'internal',
                'network',
            ],
            'source': 'ͱŝǛEƅǳСÏȴζЯǫԏΣϓyӴԮӛϱϿƦӗăɃ˥ƥԘąŜ',
            'corrective_action': {
                'catalog': 'Ȫǿ×ԬѐҘ¦ϻˈďѩЂǄұηяρůʉʹǠʊȣЇˠˇʷȐ\u0383ɺ',
                'message': 'ӍҭҜʸЍ˞ͳŽʥӨѲ/ŖČΓȚԓ˒ǩԩɶǉ\x87łϘɞƺ3Ћѽ',
                'arguments': [
                    {
                            'name': '\x9bӲäȜ\xa0Ȕc',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ϭƒӰӈԔɭ˜Ǿʑʽ/lΌ\x94ø&ĤĤпǲнƣ½њҲƶɇӢɯˠ',
                                                        'ΉѕȘҌƽ×Ä˃ΘΜăԬөŵķĈʻʹȣɭʏʡΜÀѳдĀÜі҉',
                                                        'ãѱ\x97BƥФ\x90ɛŔчӡǇ΅ıȿ˔āӏŤǼˀԑɉέԎɾ>ЄҙĻ',
                                                        'ԡģГ\x82ĪɝÂpˑЋϹɥѥΡЉÀʕΦ˅ǹ˱÷ΘˈЖrΓůę0',
                                                        'ʨɜӱщРĈХ·ȎŎ\x9aȆԒJĊ\x99әӭѕɫϺIͳȎ˧ʆ\x9dłʫЙ',
                                                        'ɡҫӜґιόͰƉĚ\\ŽͺέɴôАəǧȇƛ¤ʎȺɭVϕѓN¯ǋ',
                                                        '˵ɶȏȡˏ\x93\x8d(ΕӀү´дӎɆưςK҆˘ЈƑҨ·τÊҨʶҥе',
                                                        'ǽƟѕBҞĴʦ»ԜMɪǳ|ʏȐΫĞŋǍɥ\x95ǸÔǶçĽʼԘuѩ',
                                                        '\x8eƑʷ?ԃĻʉʿăťɁƽ²ћĬĢСǒϵ4ĳ6\x9cϴʗ;ͱАҗɞ',
                                                        'еʲɡʗмӛѪê|œȝѩȫ¹ĕДʹrҜЭзʻLԢˠѠĜϗє¾',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɏêɚȣжлӪƛҠΗōƖˮüʙΏБɺľѝțɍʒэ\x86ѹԘāГϒ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': '»ŘȵǓ)\x9fѽǴþρZҫƭʠГŧΥѐűΧ¿οҎōҟʘmȮԖ¸',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': '˼ɔǣЧΖŀԠƆ=ˏ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        -83176.53894072896,
                                                        512326.9621794588,
                                                        -12252.590759567945,
                                                        783924.6493918322,
                                                        441209.5857785598,
                                                        -49161.61360727515,
                                                        927125.6862043678,
                                                        38576.0881265479,
                                                        255658.92158114025,
                                                        361679.7984322739,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ěƆЇʬŨČӡΊҕʄIυЙϰjҁԥLΨ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:210313.148681:+0000',
                                                        '20210203:210313.148692:+0000',
                                                        '20210203:210313.148698:+0000',
                                                        '20210203:210313.148703:+0000',
                                                        '20210203:210313.148708:+0000',
                                                        '20210203:210313.148712:+0000',
                                                        '20210203:210313.148717:+0000',
                                                        '20210203:210313.148722:+0000',
                                                        '20210203:210313.148726:+0000',
                                                        '20210203:210313.148731:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΪſĐ˔ѓgÎʎбō\u0383ɺȋâŀ҆3_@ʦȅĮ˂˃ʥΑɨȤʹǱ',
                            'value': {
                                        '^': 'string',
                                        '$': 'Ƭ£ƂϳьŠ҄ĘҥKɌп\x99Р˙ЂеĨϹîʕĤЫʀΪ˲Bѫ@ɹ',
                                    },
                        },
                    {
                            'name': '˃ĕύɵѬтԘăÎζϣИȲȟϣǟȭҡάѐŖѶ;ɦ<ȤÔȜ\x93Ϭ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        4895734506958409001,
                                                        -478726832011172201,
                                                        4569633574634705011,
                                                        7079892666017253857,
                                                        538750886807839380,
                                                        -3449346412585458880,
                                                        -1734393060068654271,
                                                        -308750936242115705,
                                                        -4776654298268979370,
                                                        4420816732044486331,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʏИ҅Ƥ˱ѶťϵyȒΊȄĘ˵Ԙ\x81ǦwҮʌӝô\x9eĊpĮӛ',
                            'value': {
                                        '^': 'int',
                                        '$': 4700791616865569260,
                                    },
                        },
                    {
                            'name': '\x7fҷûΏӖäϹӂĩ¢ľЯћϜĘǻƘʠάͷϱ~',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        6086216958259051576,
                                                        4261021728209642620,
                                                        7518128061850153454,
                                                        4431705879650524591,
                                                        2821961202980147551,
                                                        -5548447414138956409,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȈҠĞɛΒуӪă͵ӂɸĦПŵɾƓΏԠǔˢӟѣċѹˬԌɨ\x85Юԓ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        1767534132658457907,
                                                        -7463808356950177993,
                                                        -1494048744204600616,
                                                        9029474110544301664,
                                                        -619335354919776303,
                                                        502833001613497219,
                                                        1978227318321124212,
                                                        5413991272246550551,
                                                        -3016670351753293356,
                                                        5512991035353348363,
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ϋǉŰʦΜЛƱʧjηΰČ˨ԪˆϙγӑŁнˏóßԝÕҒǀ\u0382ћώ',
                'message': '^Ж˘ϕЛFεʇηŏ\x95Ҍ΄Ҁɗʤ\x99(ÆÍÂѲHɞԧ±4Ӂϱȁ',
                'arguments': [
                    {
                            'name': 'ѣț¬ɵƳC;JҕˆӲȮвIĞſȭĹЍͿʓɲԟӀȰќѧоϵɲ',
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
                                                        True,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǱƏƧƹуēФшХ\u0381ӎȵϪfğӭԔѼʀҮ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ΊņϪŲ|ƾġÃӋĜ\x97ӕȰ2ȷɋҥϝÃȐ϶ȓ˟ɚΗƧҬōЋ˨',
                                                        'ԋҺɁ[ĄϣҫҦҹѩЫʩ˧ҥɪ©ƐȓԟҏŚīԉΟ8ƺȃĄƹa',
                                                        'ìчҶÔÐÑ˓ϭΝ҃ĪʹɣІưӷЕĹɘŲ˒ſњ\x9b`\u038bьĜĝт',
                                                        'ЛƳ2ſĿљƥǿǘӏɦʎǓА˸ˈ˥þˁʙäцāŏƑkŋʏԥҬ',
                                                        'ͲơХºνɑǧԭʟȖӟ\xad\x90Ҍ\u038dÅǦ±˱8Ɨпħ¡ЪƜ͵ӛAÛ',
                                                        'Κǵʩ˰Íͳ˯ϙʸĴΏÌћӿͿáɥŎϸЕԀŨу:ÖЂѡÏϱĩ',
                                                        'ӎԋ)ńǂ{=ʋΓĤuˌŰ\x9bɧƳ˫ɻ\x8b\xadҼ4ȺɢŔƖʮʏƔѨ',
                                                        'МɵʒƝɭδǰǋчƄԭДхйѣ©ҐɴȷϺ¾ҔÛĺŰǕ?Ǟʀρ',
                                                        'ĜðˍƒңʾöϤŬҀИǡÍț?Ќʺ·ŢǮұϢϤɽʐˤ*Ѳ˴E',
                                                        'ʢχӑ¢ќŗљĈķƱȰѻʗ¶ıɃUʪµʒ\x8fȨv\x8aİзƁĳh7',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ˡϸˮӖКѭʞȭΔk¹ȱѰӖų',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ӤЍ¹Ԋ\u0379Кҧ˟Ĺȶ˾ΓОfϊƟɩǾіƙӁυϸǴԬ\x85ųΩҟԇ',
                                                        'ȲƅʫǈöѓL˘а\x8bʻʺƣÌҳ\x85ŚεХňǊŤЌȗ,˽ɨѺԨƀ',
                                                        'һƬУȔaɃͲˏǲƱŗmϭяӱӎσŬԘԣȑǟʼɔŎÙʄіɒç',
                                                        'ÈγʊҔҧĺĦķƑΕĒÄ\x9cNȟǙʌҾϜ˔ӔǡԞʆʱ\x8bįʦįѳ',
                                                        'ӧ˨³ǵԌĮǘѯ҂ͼƛÄȌǁʥχь˶ȸ˱ӲŕψЋӎӝãЪŏĎ',
                                                        'ΌƲĭǘϣԣĥ΅Ѐ\x90ϋÿȲƒԤӫaНӌ<Ö\xadʁЯɹΆĮҝyƞ',
                                                        'цȉЏэŽŅiПӕŜǕтȖťҲʩҊƩӀǹðhҬи\x8bƅ϶Ûí˰',
                                                        '҇ӹӤŠӬѥƵԎSǌ&ɿќȴŷǌƤΚ\x8fǸҷǘӈĀİƏϋȝўɫ',
                                                        'ϯǀæʧÐʾ«ΕǇŜӯɣGʼŘěĝΞҽĳɋɡǼԂԘ@ҶԮ Ǚ',
                                                        'ЂςʗǿЏ½ұ\x80\x86¤˪ψѬǼ°яМѴ\x8aȾˁюʏǐԅȸʾӔȻ>',
                                                    ],
                                    },
                        },
                    {
                            'name': '˱ĞˁГѺЛǅюȀӦȸήfӰŸ\x87у±˪ʜǜЙǝҡϺʽЛԗ҈Ƣ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ųȲйύӆӂќӤùҕȪ\x99źǑFфƎɽǮʰμFǑōˌҮΎɦιİ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:210313.155050:+0000',
                                                        '20210203:210313.155063:+0000',
                                                        '20210203:210313.155069:+0000',
                                                        '20210203:210313.155074:+0000',
                                                        '20210203:210313.155078:+0000',
                                                        '20210203:210313.155083:+0000',
                                                        '20210203:210313.155088:+0000',
                                                        '20210203:210313.155092:+0000',
                                                        '20210203:210313.155096:+0000',
                                                        '20210203:210313.155101:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȩʶ˗?ϫӯçŧŅʃ\x8dǴӓȠİƻ(\x90',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        -69025.81130056824,
                                                        893981.635961916,
                                                        609949.7861031033,
                                                        124287.15839981739,
                                                        5265.395455418693,
                                                        876316.8580736492,
                                                        94435.01684937635,
                                                        606037.9058560686,
                                                        2924.151328493157,
                                                        12329.855360176836,
                                                    ],
                                    },
                        },
                    {
                            'name': '\x7fҚϽ҂ɢĿɍųBŽ϶ǈӵƃǒ˵\u03a2ѩͶı5ƃØΕʫïĉƲƩʌ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        3189034418014175208,
                                                        7373246043770121427,
                                                        -7840655447856390425,
                                                        8538616322942350747,
                                                        4045168482189407064,
                                                        -440977748858832687,
                                                        2094663570579284830,
                                                        8814188028102310026,
                                                        -591034706470748020,
                                                        3376848737627887064,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĊοƥΎʞǌ%ı\u038dʍЧшαȬȥ\x91',
                            'value': {
                                        '^': 'float',
                                        '$': 680047.6539677053,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Ȅ""ʺŨ',

            'categories': [
                'os',
            ],

            'error_message': {
                'catalog': 'ҝ\u03a2',
                'message': 'ʐ',
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
                res = native.RegisterTranslationFailedEvent.parse_data(test_data)
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
                res = native.RegisterTranslationFailedEvent.parse_data(test_data)
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
                'identifier': '<\x8fâԇŏƌĤŬυªƛÂ²ŸҝѸFԕn¼ƽɂʼ+Ҧрʌ˩ʦā',
                'categories': [
                    'file',
                    'file',
                    'access-restriction',
                    'internal',
                    'os',
                    'internal',
                    'internal',
                    'configuration',
                    'os',
                    'file',
                ],
                'source': 'ʦǿӁˠшҰ˵;Ρ˔Рˇνĥξ΅ɒԤ£ĳˤģʵĦė҂ͳȒ¹Ƶ',
                'corrective_action': {
                    'catalog': 'ѳ\x98ɚȑȪɺǋ\u0383ȸϫ#дԦª5øʓҡʨǰʓ¬Øƌbω½χĢʙ',
                    'message': '\x81ϭӪ˨ϖÄƔρΔ˴ʀĥȤʰŢήњξЫ˾Ǝƺʮ@ΛƔ˺:ёʟ',
                    'arguments': [
                            {
                                        'name': '\x85Ҙʾ΄\x8eŏæƥƧɰϾǔȐѝĐưĴªˈʰΧʄ+',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŝAȭҽʢϖŃΕԝˇϋѮɱңƭûˏƽnҤ҇Ėҩ}ȬYˣɔЋɭ',
                                                    },
                                    },
                            {
                                        'name': 'Ǔƞ½',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210313.142249:+0000',
                                                                            '20210203:210313.142285:+0000',
                                                                            '20210203:210313.142293:+0000',
                                                                            '20210203:210313.142298:+0000',
                                                                            '20210203:210313.142303:+0000',
                                                                            '20210203:210313.142309:+0000',
                                                                            '20210203:210313.142314:+0000',
                                                                            '20210203:210313.142318:+0000',
                                                                            '20210203:210313.142323:+0000',
                                                                            '20210203:210313.142328:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʘѭʢӉԧ»ӯǩӭźƖʔ˩ȻAΰϠңѭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 202911.08815289044,
                                                    },
                                    },
                            {
                                        'name': 'ǐ3юҀûϻˠÖϭӹƳȁʄĠȕβīӼƀОϐҌĿѠĮӯ˽ƜȥТ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ФЍƈΉƐĸ&˽ŦȌӞŋÇ]ͽк˘ȽßˡΆԡӛȎѠȡ˽ȃƣĿ',
                                                    },
                                    },
                            {
                                        'name': 'Ҫˁ2˨ŻʰɒΒïыÛͷ}ҿ¼ɺ\u038bԪԗѱŘБAСƷБМ<ŎƊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210313.142890:+0000',
                                                    },
                                    },
                            {
                                        'name': 'MԞĐҧӎɂˋґӜƟūӷԍϡϯйČ¼',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210313.143027:+0000',
                                                    },
                                    },
                            {
                                        'name': ' Ŋьӱӳ¶бȥÒҋēғēƐĮΒӇӄˆ\u0381ҏ˺Ѩ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƜŔ\x81Ћƨ˭G\x9cЈήD˾ɬ\x83ΧǛÈήǠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210313.143413:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ă˗˄ZΔǣ҉ȧʛĽsȺƵƽȖïӄĻjԘ\x83јǂғғыԌ¹ѡԑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 508123.1212713652,
                                                    },
                                    },
                            {
                                        'name': 'ыѡҚɗ҅¨ҖÉǴӠ=čѦ ȩòĶԀуƕʹԦяǰĝŋ\x8eΆʎϱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210313.143696:+0000',
                                                                            '20210203:210313.143705:+0000',
                                                                            '20210203:210313.143711:+0000',
                                                                            '20210203:210313.143716:+0000',
                                                                            '20210203:210313.143721:+0000',
                                                                            '20210203:210313.143725:+0000',
                                                                            '20210203:210313.143730:+0000',
                                                                            '20210203:210313.143735:+0000',
                                                                            '20210203:210313.143740:+0000',
                                                                            '20210203:210313.143745:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ŌƳ9ǼҖǎӹӳʆ"ɜѣϝӅɨȬμԙӡƪǐαάũɫßͺԨТʰ',
                    'message': 'ȱŻɳɇɭƾɱθʹűĥӮ\x9bӧ\u0378ʿɷɅJŅǍĵʑʉ§з҅ȮΔȃ',
                    'arguments': [
                            {
                                        'name': 'РԞțœƮlÉο+ǸҿþҬƔ\x80êԫǕҌ¾ϾһʈпİΌˇҲɜŚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƶʂĪ˚\x85ωŪΏѢ˅řұԐ_˄Ș\u0378˖ӍҜϛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɑ\x98˕ɌҬŋЈˤ˗ǊǔҁΐҸүrҀȏĆ]ǘȥɺѕаãϮα˘h',
                                                                            'ĦĮԧ˰\u0378ÊʶĖɶ˕ɣJӽέ˚Ȃϡӵ˶ӃƆ˅ȂŪҤ\x9cԇϦɕѴ',
                                                                            '_йƠǙԗʣԔԜӓћΓԆǟƆ"ėϓċ·ŝТƙӣӽǞȓ¼ŅЈĻ',
                                                                            '/ЃԨҤѨŏӐ\x86ƗJÝ\x91ҝɚϓϖ)ȓʹТſǄЌąÏLɧȓ\x95ѥ',
                                                                            'шôȟѓ¯ЎӒħЙʻǌŕыɑˀńӓ\x9aĜ§ЛŉӒѥŧàÝͿǷ\x87',
                                                                            '¹²\x8dŹθϴėǾԌΜǤРҗʓȳďɹіɅˮŦѴɷΞήØЯWŇϙ',
                                                                            'P_ҜǽÁȫρĐeɛŤƁǌƾĵԋΥ˺ʴŸʊǿ˓к\xa0ÉȨӉӗ\x95',
                                                                            'ӕӂԥpԍӡʯѴ˰ɩԚmӯńǂŲѩƾӱкҨȰȞРuïЁ\x91ƒʭ',
                                                                            'ҌϬεϦˁˬBˈӺƎșӁʒП«gɀɥȁȍŊļΖwˡ±ԙϵÇӹ',
                                                                            'ʹʎ˓ƘӒӱӭЦŔ]ɖϴώʚО\\âȅνǑӾõҞΖȿϿЎɮKf',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӖМƚȪF%˝Ωķÿ\x8bĨǲ+ˊ˂ԧęԙӜȶŏϛ˄Ú¤dΠuǒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210313.145172:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȐҒҎˉΐēÂůϣ<Ԇ@ҞϥҖĜӐ3Ϳ\x8cɜĭӸǲǧѳĨӢȥÊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210313.145577:+0000',
                                                    },
                                    },
                            {
                                        'name': "ԍdѨǰΦK˷¤ȥЖĹҸɐΘžӐԀӲıƱυɻϙҜӓϕëţ'h",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            333297.3494601296,
                                                                            468026.1988376373,
                                                                            -87903.61805833263,
                                                                            637640.5749102369,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɞɅүĸÿǻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɖђЕïϑƏµǶ\x98ĔțíūвҚοʇϗӧÙӷʤȰfϹǹʇѲѭƗ',
                                                                            'ȞǩνҖ×УɃʮɪˤ§ӷƦҒїк5Ȥďžšӝҹć˟Ƶ˼*ɐŁ',
                                                                            'ʞÆìƚԕıÜ˥Ȕę*κDƥƆηǱӅǶǨСтƤʏŲԓĉÓЈӗ',
                                                                            '\x80°\x8eȃĪL\x82ҥ\x99ȴʭȗҕԈŷҲĎîȲĤēaȶïĈЗˬġӇĈ',
                                                                            "ˬͻСюӜΐȼҡʼоӇ'œą_ÝĺϸĭЊͼəͿчǽȝ˶ņɁɖ",
                                                                            'Ȼ»ӿҐȱҸāɨϊɸǉҤңСĩʑѓŷȆƨʋПqĢӝ˷&ǮҧÉ',
                                                                            'PɲłñƅĀȏЖ΅ƻˤюƢȓưǹƻġǻ҉ʷȀǅʒҗʈŦˡҪȂ',
                                                                            'ЋɆɫ\x86ϒ%a\x97ơ˳΄ЙſчȦĴԕ,ҌɢP˾èǆĘ\xadͰΐƧȧ',
                                                                            'ϬЂіǚȭψǆǧҜȎȬÔĒζęЎ@˽ʤʸƞԍϧï~>ΔȰ˖\\',
                                                                            'ǦǁɈͰÖȐƞ˚Ĝ/˱˧΅τԇѡȏ˛?êǑùɕșɷˌʺìʕv',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'źж±Ϭ˻',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8107163875044762236,
                                                                            6545629912441130749,
                                                                            -7594441562746196831,
                                                                            8052292901248815044,
                                                                            6440164195936547777,
                                                                            8901447447546570763,
                                                                            -3968913129546966299,
                                                                            7875644711940868045,
                                                                            3738397732930073194,
                                                                            264642387824484745,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '«GǉǫϤȱƳʦɡҥʌǔ±áҌԧɂȷϲϚӳĨжѓ¾ɂz',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210313.146566:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˁцʖΫyɬ\x93ȅɍʋǩԍǚǻÿ΅ӒĈуğԠѝƕɈư\x80ŁȬVȢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210313.146705:+0000',
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
                'identifier': 'ѽ\x98˛βĖ',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': 'ɓӠ',
                    'message': 'Ĵ',
                },
            },

        },
    ),
]


class RegisterTranslationMessagesEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationMessagesEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_MESSAGES_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationMessagesEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_MESSAGES_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationMessagesEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_MESSAGES_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


REGISTER_TRANSLATION_MESSAGES_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
        },
    ),
    (
        'bare-minimum-fields-present',
        {

        },
    ),
]
