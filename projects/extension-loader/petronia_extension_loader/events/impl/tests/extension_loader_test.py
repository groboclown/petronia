# GENERATED CODE - DO NOT MODIFY

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
            'name': 'ŒѡѹíοĚвċϦƪG¥iƩӘЍзĜʹ˩ΕΠǗƑQҐˇy;Û',
            'minimum_version': [
                -817042154192951245,
                -7511841809501127423,
                -7342222710240007347,
            ],
            'below_version': [
                -6057424567661581351,
                -2653861013530678143,
                -6597289847200964668,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԩTѴ',

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
            '$': 'Ϛ*ǾǸӌĀǚ˛ӪňǗóϲјŬүКθ\\ƺӻɇƣϋϖǹͳ\u0379Үǟ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 6628678642762570870,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 49632.63709204673,
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
            '$': '20210327:033617.107108:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Χgȿ\u0383κԢȤ˰ÄΣƿРΊɐłŪʕƩͻԪ}Ӈ*ĒԚđ»ĮΫȨ',
                'ɵφԤϣǌԈı2aļǬʾĿъжĥıǿƌӗŇԍƷɜʦđ\u0378ǡ2ġ',
                'ǸγRΰĩƤ½ƦԅдԟƦŵӝƜŪ¢ź\x8dІưÖϓʃԈȁ˨ȢŀԦ',
                'ҝ˻Ŷ΄\u0382ӜýщMɬōƀÎʢƁƮʒӜõ\x8dӾʾǗǐŵŦÙьɀ¯',
                'ɂɿɺґŶěλǮϛŃΨ;ŬÏӓƾǈŧҩǴ7ß˴ˡɱˉҳΈӑ¨',
                'ˮҚΆѩҨҼÈŮϒңƬКNư˘ñ.ȃæҼдĂȱɵƮįþϢζ˦',
                'ōÌΏǳѡʈǠʼǧ϶ьø\x8dɾθȽļĔɷЪӫÍĵԑԇ˻±Ǹ\x95ѳ',
                'σɘƆҦǄςГæҟфӑӝàʬșǜΌԟśӽ¤ѭѷӸMɵҮ;Đϛ',
                'ϣХƐʪǾèʁŊņ¤ˣҡśʌƘǎҔωϝĞҰÚͱ"ǋ\u0381Ƽ\x93ǴИ',
                'ԞѸεƜͶèǺɼҼĞķϼӮǅǛ\u03a2Ð)ԑΘđſӗҧԉœѣʜȔϩ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                565845645122062035,
                1577720752584908199,
                -2683918753149259956,
                4411342505854779566,
                6800457581987909771,
                5312126369393569243,
                7861511913115773826,
                8694906505489748595,
                -1609915502499736844,
                5829741738319135571,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                552614.029402737,
                764124.618354598,
                694089.2166103811,
                969568.1491549474,
                749857.7053116672,
                578346.5356415836,
                41048.071098525776,
                703351.3922936554,
                984514.1995952367,
                596542.4411294754,
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
                '20210327:033618.207343:+0000',
                '20210327:033618.226795:+0000',
                '20210327:033618.247027:+0000',
                '20210327:033618.267449:+0000',
                '20210327:033618.285933:+0000',
                '20210327:033618.307717:+0000',
                '20210327:033618.328500:+0000',
                '20210327:033618.348444:+0000',
                '20210327:033618.369131:+0000',
                '20210327:033618.390526:+0000',
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
            'name': 'ѺѸμӡ˝ɵϺȌȞпƵә˅ǯҰÎԛҘГ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210327:033616.698890:+0000',
                    '20210327:033616.717293:+0000',
                    '20210327:033616.735964:+0000',
                    '20210327:033616.753914:+0000',
                    '20210327:033616.772967:+0000',
                    '20210327:033616.793206:+0000',
                    '20210327:033616.809059:+0000',
                    '20210327:033616.824890:+0000',
                    '20210327:033616.839699:+0000',
                    '20210327:033616.855874:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ќ',

            'value': {
                '^': 'datetime',
                '$': '20210327:033616.899605:+0000',
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
            'catalog': 'ÔÍѰĕǻ;ԣҸȜ8ҿеΩS\x89]ɽЀjЏԣΌ҂˪ɳεƩѴɯһ',
            'message': '¬÷ȀʑO?ʭƤ\x95ӣҡÀφˠԭɼϭˣˠǥËƟԈśυÅOӗʆ\\',
            'arguments': [
                {
                    'name': 'Ǹ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:033615.180783:+0000',
                        },
                },
                {
                    'name': 'țeɥљέɳȮĜǿΒӌJėϳͰӎŮțϰTѝɉˈƚΝňϩßӤИ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ϼ"¸ЖʷɊĲˤīӮŗǆμƻʡęËŬǬɻåOԦӖTȘWǥϳ¥',
                                        'Ԯ˶ŔӳЊ\x87ԐҌϝĿɓσʁγКŒʅξȬΛԚӶȄԘɕȦӘԧ;ķ',
                                        'àβɻґєŬеɺπ¡ѱԨвˁ\xa0ɗɺЖˉѰĴ´ǗϺƵϯRԖƀө',
                                        'ȝşŦǋΙŃН°яν\u03a2ӷ5ԍϤƄęPĪΛ˯!ƭǤÅ*®ÉƷń',
                                        'Ǯȩ˅ƐҦ\x90φѦ!ʡǲȠř҄Źʖҭ˻½˕тϡϪӎƜƳľʶţá',
                                        '˨ĐƆÇԃƓųǂЇл˄ҎȬʧɃǿΞѮχ˞xСӶÙĩƋŀҥƵ\x98',
                                        'к\x9aьþÞ\u03a2ğ÷ÿˌҟƎî҈ңҏzЮ\x81ƶ\x89ΠƫӍʍеÉɛǳƴ',
                                        'ӑɂƂʒӾϛS˙ӂsʽϿΚʍǜϣȨќå¡r\x81Гωɟϑ$łӱƋ',
                                        'ƂķΎpԀžѳʻâI\x96ͷҭŨÐÁɉˌчԎõΊȔŘ¨Ϥ×:ΝĤ',
                                        'ɵ}\u0381³ƥ½ǒҴΨ·ʓǯмҰ©ӟ\x99ʕ\x81\x85ĵIυǆǚãҹƠόú',
                                    ],
                        },
                },
                {
                    'name': 'σ',
                    'value': {
                            '^': 'int',
                            '$': 2315905268623821712,
                        },
                },
                {
                    'name': 'Ζ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:033615.563583:+0000',
                        },
                },
                {
                    'name': 'ȍ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': '5ҌǄәÆɓðжУɬ\x98ʧϧįХZΓ',
                    'value': {
                            '^': 'int',
                            '$': 2585607272848015729,
                        },
                },
                {
                    'name': 'ЂӖ`Ҩϛ\x84ӔӵǈЙǅĊťʀʥ\x84îԌўţĒĈҡČíеȡˮӭϤ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        692509.4603658229,
                                        735423.0566388287,
                                        459233.3587678905,
                                        454038.45300105016,
                                        984010.5024739185,
                                        55754.598689796025,
                                        980289.4621699823,
                                    ],
                        },
                },
                {
                    'name': 'ѣɟˮiϋǑаɘ¬ҦƂŒĮĹѤ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -5657886570580872376,
                                        -5737867443397954764,
                                        6218398683321254934,
                                        -209387803014775592,
                                        3843108514080743972,
                                        7324786516385393391,
                                        -3845401257093347068,
                                        5633078332235088120,
                                        4738796109523345818,
                                        -1493139741953661185,
                                    ],
                        },
                },
                {
                    'name': 'уȒE\x90ȇѷŧƮӕ3χʵȬʍϸɿʒΎȧЌԩҮȎƿӒTȚǇЙʎ',
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
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': '˙\x86tTЏԌɪԏǯѴϘˊҳϒӬϭΚʵÏыɯìǣP',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:033616.554342:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'pά',

            'message': '°',

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
            'identifier': 'џˢdԌνƺԔȞЃNүρƳŕŅѿкͶƪɞ΄ĶНmĊӊɑ˼ʧџ',
            'categories': [
                'configuration',
                'os',
                'os',
                'access-restriction',
                'invalid-user-action',
                'access-restriction',
                'invalid-user-action',
                'invalid-user-action',
                'access-restriction',
                'internal',
            ],
            'source': 'ҬωВŖϛʔʏ\u038dǬīĶʴɉǩԕƆȍξʖ ԝĝіϹdʃϙʜīɈ',
            'messages': [
                {
                    'catalog': '\x94ϗҎɿεѶρƷ\u0378ƛͺ˩\x86§Ƽӱ×ȑʷĂŒƌӋӽ:ǮӁЉ·λ',
                    'message': '$ɩŶϨдҘ:Ήʍԓ¬ә˰ЁõğʻЍxҠҫ«ѵɯǕǵƩ`Ђԥ',
                    'arguments': [
                            {
                                        'name': 'ˮ\\˭ԣʹNʆ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '£žˬϵѨƱʻҹиȂΡLѠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'З˝ҬŐ¿еɩʪԒˏĠ:ĢȎӳŴŰǑȉ˾Ď',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ѭ²ǚӳԑɶҳNξгȧͼӿυӄξĕΉҿƨðĎŔȆӡʼδҝŵˠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȟǹϳӬҏҩґ΅ȶ#ҎÈʵŊäδԨɐʅǅϻ=<rԑĳҹŽľφ',
                                                    },
                                    },
                            {
                                        'name': 'ƻǇϣԤÊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3696066084019462302,
                                                    },
                                    },
                            {
                                        'name': 'ɣʭƕϠʖQÚˍʂʍŴ˰źSԏӑǬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǴĆ©ԀD\x83ȵ\x86ϊʊϺ\x98΄ΨŬ˳ţȇłŇҧĦԫ*cĵưƔқʻ',
                                                                            'ѿϋăԚʏʊʖʱűΖɧ˛΄ϺӗǼȨƺ©ǴǍzӧM¸ƭҲŻMΡ',
                                                                            'ƮѹϚǰоgΈ\u0381ǁʿҭɆϊʗ®ұχǘρv\x97ŜȺ҅\x9a˔Š£҈á',
                                                                            'ȒԈзɪ2[ҞЪĕʆӷʈΙ°ǬǇŹ\x8aўȁxu·зʢëҠӶХӼ',
                                                                            'ƆȄђ0ǆņҤǉĻӪǿҍĄǌΣɌʸҳҲԊĎѡԀșĠǒӌÀӚΆ',
                                                                            'ĘÌƾәˣҢɟĢЅÿȉ{Аͷąʵ˶ҜƓҜś\u0379ԥϟҖҚä҇Ǎ^',
                                                                            'Ӽȗȗ˭ŊŕŬџāѭȬ҂ŕƺΫƾȆѹǠҺȀńαā\x9bĥÞľͷҎ',
                                                                            '\x83ͽʔsЪʿ҂|Ћ`ɥſӛť˟ǺˎțӾ˂ͷѦԥ˵еGʦǾ]Ѝ',
                                                                            'ƥ¿ʵǝңǑǉĊʹ1ЏΕOϏ)ɿȌʃЕ҄ȐńņɧųǺǺ~Ϸć',
                                                                            'λәΝmŎƢ\x91fѯԣÍiϽɑŚGӳ˽ʁүǔýÞ\x95ůϐɪмЩɇ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȥ˹ӲUĂƚдхİʦԠěІОmûƅÄġΡүŮԏżŞǇЯǮӥҘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033600.812861:+0000',
                                                    },
                                    },
                            {
                                        'name': 'țIıɰʱʵ\u03a2ϗțӣˇÌӧœǔ)˔ʧКȼýî3άʎc¥',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            268839.16043023265,
                                                                            36544.37396581931,
                                                                            72849.98051426775,
                                                                            608016.2008239056,
                                                                            100020.2140720358,
                                                                            681802.8149380211,
                                                                            660390.0899639399,
                                                                            414309.7176218591,
                                                                            778928.49936418,
                                                                            -2268.1114329571283,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ā˻ԑɡЭԪ҄ϫͻаԅ[ΔΎɒȟѯЦњ˂ż@˝x#ƈ¹Ƨɦǰ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1972213619360884372,
                                                    },
                                    },
                            {
                                        'name': 'ǐӟ?˾ӁȬơſlƲǢӆ\x94ѣʄȍΌ˩ōН\u038dӵ\x7fҧVʞ\x7fČʅӀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7804553561258322819,
                                                                            -3244382466968849149,
                                                                            7817052371204640011,
                                                                            -8064129394102440538,
                                                                            -4494913716119816952,
                                                                            6647840336348407615,
                                                                            -7373751117129697536,
                                                                            -6367018448791818390,
                                                                            -3910285363126973104,
                                                                            4217663095667574540,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'çƪĕԦЯΓǟōWҎȣʰНǕϷңҐȝɲȔÆDĪ4ż˼ӄҌǢɚ',
                    'message': 'ǨυҳϹ ʙƕςΡȂЉȇҞĠɔӈΈġŰʺιƐʴʬʑÔԨҧÑŖ',
                    'arguments': [
                            {
                                        'name': 'Ҡӧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 122158.31128174672,
                                                    },
                                    },
                            {
                                        'name': 'ŉЊüMΉƫ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϊƬΧȅӡΙӠξԍӱКӷϓϠˬƆГůν˩',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2870916229592243801,
                                                    },
                                    },
                            {
                                        'name': 'ó¶˝Ѯ\x92Ĳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033601.780483:+0000',
                                                                            '20210327:033601.800718:+0000',
                                                                            '20210327:033601.819534:+0000',
                                                                            '20210327:033601.838958:+0000',
                                                                            '20210327:033601.858626:+0000',
                                                                            '20210327:033601.877679:+0000',
                                                                            '20210327:033601.899330:+0000',
                                                                            '20210327:033601.920252:+0000',
                                                                            '20210327:033601.940321:+0000',
                                                                            '20210327:033601.964987:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϿƎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŗм҃ʯɆºͺѶϴЋυ˧ÕƘ9ðѳ΅ҀȾ[Ŝϝ×ȇˤªԣţ¬',
                                                                            'ҽɈӔίĽӴ@RͷҀļ\x83ԞOŴɝл˛ţĖÆӝˎϹɈκҫѕŀȬ',
                                                                            'ԅɞϐи.:íu˱ǇѻɳͲŃκ\\ͰҕķȎ\x98ԫÒѹȂȐƈʃёǦ',
                                                                            'ˁ±¾ϔǐžǭŬοɁċ\x80ÖƐʧα\x9bϊҊЦЖȧҼ˔Ɏˮ=ĿɿҢ',
                                                                            'ЁҩВЧƘʁBşƷԦʮK˳\x98˯şЊЩ\x94ѠʊτС*ԖƈО,ɪè',
                                                                            'εŠҬƂΕêƾĎÞNǓĕȘΉ¢ʨǙɩáƂʾªºΨhïӼŌǾΏ',
                                                                            'ƒőӬ*Ԗмʩј ßхφԔɧϽ\x83ŤѴ~ȐɯƊқǔуԭ®ʩ£O',
                                                                            ";НԀɮӌɢΆØiǭɭʉQŒԎȹӒZ'φǤʚÃ+ǍĆǤ©ζá",
                                                                            '\u0381ʁmȊvўЉņ\x8dơɹ˽ɤйʞ\u0383κɺɊԄϴŞƩƯιϾçϟӚȕ',
                                                                            'Ӛōġ}ѪgǢȓŽЯţɿą΄΅ҿӗʶӲ҈ӄѕ¯ӈҺ@\x9eƌǗņ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѧοŦʆ\x94üϨ5ǼŪӼ·ŬҢƵťħӤɶǯДʭ\x86ӹę҃ӷϋʋƯ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɑӲѬƩΨҞĚːŁƜÇԥԟͷŖɌĄԕĀňŔɖκҟɦѕç\x9fϧʸ',
                                                                            'ÍҰʺčoĈ6ҮƯΞŭ¾ӢșҋԔɵѡҕаЏӰ¿ȌǗXҤšȏǰ',
                                                                            '˛ĐŘ˲ǏтĺаɞTËϰӟɤ\x98Ƹ¹ΦӗϪɯҿΑƑǬԛu˓įԑ',
                                                                            'ĬǡKΖЊФÔó³΅DſɽќɃɝƉӡԢˡˊĺΤБЁǍ%άЎŏ',
                                                                            'ˈ[ԃóӈýӅрrĦǼɦӡκёӚȭҗƷ-Ǵ°ĚɶǺVƦёΐ˾',
                                                                            'ӓΊ\x89YƊãäЂOƲѸ½Ч\x9døˌ\xa0<ӍŻҨσЪĂȕ\x80Ϲхʷō',
                                                                            'Šȵ΄ɖǊԎ˕ȰÐɄ \x87ЀʗʑƹԆƾȍ˭ɠӣTӢϢʖдϦ¶×',
                                                                            '<þǍίǾɿąuœʄìͶ҄Ζ&9ħϜоҭΖʹρӰЎƹ˹\x89˪·',
                                                                            'ťǋʝ˼ӐʝȻņº5ѩˌ$ŝҒѬÚ҉ԖЉȣ=Ɉ¿ͿӜjѣ3Ȃ',
                                                                            '«ҨjÅļƘ\x81]ңѯӱ\x9bѻʴˣɜÔΞFƻǘƾļƮӏ˯ȗҙ\x9a˥',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʂЎѠτˮ¶ȣ\x82şүПϘďтǱѐȮϓεjËGӍӚȥáˁȄʣǣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            545615.4856787822,
                                                                            583121.716670848,
                                                                            998700.0144496257,
                                                                            969570.4473348111,
                                                                            227947.09203587682,
                                                                            319754.57796015043,
                                                                            455978.34095869237,
                                                                            760913.1576316234,
                                                                            -49987.07317137412,
                                                                            562617.5802391117,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'YqͷŢ҅κ҄ΚϴϱĽѬǬʰ\x92ųьȫŞɅΗҘƶЭƹ!мѳ\x7fӀ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2475534588053422619,
                                                    },
                                    },
                            {
                                        'name': "¼˯ӆșīΕƖԁ;ȀcӉҭ҉ϣʪ˨ŻҤʷȇσ%ʛϰ'ìƑâ<",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            ']ϻȞƽ\u0382SPёȒŕҀyņuǥӆƤAѶԮƛ˲φӜɈǠȤŚңʩ',
                                                                            'ʳƄҰĹчhɳʸϑȢԋηԢ°\x8aϦæɉъĥŭϙʤˠ7ʢ\x7fфǃΟ',
                                                                            'ÝԣĽҟϸϱЇèƈє\x8fɬǡʣҴǂȝǧ9Ďǯ\x8dɯӖ,ԡʿǪȃȰ',
                                                                            'ɀŪ×ŷ˩ԋUʁUԄщ\x94ϛíϚμˍБÐʅēȁӶĖϭlЂ\u0382Ͼ¯',
                                                                            'ĩ4ʸȜɯƅƩҤԥӜ҃ҝ\u0378ŊҧyԨò<ʿуϸҒɵϴɖƟʠƾà',
                                                                            'pĩ=ÀђƎӆɁͼΝʧğюҀƀÿÁӘƲҴҮϊvʪԡ˨ʁ\x88˗Ġ',
                                                                            'ѷƈ©ŸʦƘӍϸҼýºMőʋĥɽø;Ŷԩи\x82҄ěѤȀЕōȀ\u038b',
                                                                            '<ԏ8ÃӘʢҔԧɃԢčҐЌ\x8dzѕúϩʘ]ɆЈѝɮí΄Ε˲ǥ¡',
                                                                            'Ĺαԍϭˏʚƽӎ\x80ϥІƎÔˌȯӖæѵүӼØґԐ·¹\x9cFħD\\',
                                                                            'ȼԣԝ\x9eƻԦΜ\x8eҢйӕȶ!˞ǍƱ§˧ɽяЃǈóƁŵԤʹuɜɺ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӐĮҶơˠӲʹȼΫѪƗǈ\xa0ë',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x89˸ȞΓź˦˫ΜÓϺƙКϋϮȂԞùЂӍǚǞQ©ϣӯĢɥɐğͷ',
                    'message': 'Ѽ\\SњɿʋƯǡˡϧ"ԌÊĔΛҒĔʤǵӺɏƉPϿƮѺԩΐĠě',
                    'arguments': [
                            {
                                        'name': 'ʂɺϫҬɮғͷĠОń\u038bĈͲĶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 688469.9729008881,
                                                    },
                                    },
                            {
                                        'name': 'ӰӌόɻãŁӤϯəȿɰƁГPŶҀ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033603.299937:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӎŶҡ¯ÛȁԪѤƑˉбλόǁʉѻųŕͿʼŎгυ9ɨMƘ·ĄԪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7173584810039993733,
                                                                            -3021823484747518448,
                                                                            970774730146092071,
                                                                            623410629267233428,
                                                                            -3540623553737498662,
                                                                            -7192947017024862496,
                                                                            -1209715301755157865,
                                                                            -1178214262667807046,
                                                                            -8777486071902750434,
                                                                            8750702172130646073,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʠЃrԥ˖҅ҫȓò\xa0ӵȄ϶МѷжWȆϜDɊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɵˑΫǀοЎļĜǰҫΕ`(ĪӱПĢƩӤЇɿƿЖãɲ˛Ň"ĖƇ',
                                                    },
                                    },
                            {
                                        'name': 'ҰRλˈԠӢҫʛƠʵҩʊĉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            721200.9699794003,
                                                                            460026.2551110523,
                                                                            152358.78027060794,
                                                                            408239.53339853644,
                                                                            427569.6584879467,
                                                                            74572.83238528983,
                                                                            127676.56639152238,
                                                                            422260.18641894596,
                                                                            961649.7188360321,
                                                                            119436.37919885569,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɟǾеāƊ½8ŤѷWɺϝљȃúƳ³ȓӜɮԗɩӔƌšʪǠԧȉϬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 414339.6635463239,
                                                    },
                                    },
                            {
                                        'name': 'ƚ@вÔâʟĖвĬҨϥɸȴɒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4653427887745893456,
                                                    },
                                    },
                            {
                                        'name': 'ĶɆ¢ʤ·Ɂ҅ɇȨ½ГˍÞȬ_ТɁԜϖCĎӄ3ƟŞŭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -83435.46326043588,
                                                    },
                                    },
                            {
                                        'name': 'ҘԊϊ(ř˰ѫӡЈŶѭ҄ƾαǪʗЂɼϖǡʍҗҀʰ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            724854.6416249092,
                                                                            -41932.10183883706,
                                                                            379691.1699997077,
                                                                            824838.5166960629,
                                                                            423774.35170672677,
                                                                            346329.33669066004,
                                                                            667599.1581876655,
                                                                            206649.5609916402,
                                                                            793253.0245102743,
                                                                            729597.924092227,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϷƾδƒȢѥˉѣɕǷ²ǝ½ƋӻIǹĄѵP³ӀԃʏŴǾ¯ȝϤ¦',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -796420080316947349,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ĥ\\Ӥ',
                    'message': "WʥӊҼѹƎ˺Ƣѻ÷ɯB˗+Ӭ7ÚЁşήWԖ\x81\u038d#ԝ'Ԓȗc",
                    'arguments': [
                            {
                                        'name': 'ϟӳ˜ԪhšύΆҖϣ˓PɞѢ\x7fΉÄ\x84κ¤ʵбЖ¶еɈÀl´\x95',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5077616677179466355,
                                                    },
                                    },
                            {
                                        'name': '˕єƩǉMŒ˹˂ŎͼϟǎŗѬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӣȕ7ҝ҈вϼаԘЎŢӘЖ΄ӧϿÔĂɥӭƴ»ʊúώɢżȬŕȞ',
                                                                            'ήȾ\xa0ı;ǈǊĄˮſĮ-ʽѶ˃ҵϦʣӐ˂ҬӊЏų˭ĊɍƘϩϷ',
                                                                            'ōĕƷˤʦP{¦ўϬӏȇҧTƼӾɺӀϹơȩŉȆˋˉưȵǋԂƉ',
                                                                            'ˬ˝З˸ŰԖȝϝǴѿ҂°ЛϐɬĂȺ˃Ӏ[Ŋíӄ?҉×ъëΖж',
                                                                            'Ņ\x8føęϸæǘɾɜΔĕ%ʞ>ҿÒŤӕӉӃĽԟˣàͿМӉЈɷП',
                                                                            '\x9aΏ˱ZȹɅҭΥϐ;ˑžӘđćĨêȍȕ±ͳôȘ"ÀԣιȞM^',
                                                                            '\x95ȣ\u03a2Ĕ\x97Ԭ˲ƃҬшя\x7fʆɶʺȝ\u0381˫\x85ϽϙˡƪΡ=ʧҶsӮȭ',
                                                                            'ćĶӗѳйϪȣΌϞǦϔɂÜ©ɐ\x97ȦĳqŻǃԋȡņѧѸĦΛі_',
                                                                            'ϫɋǧөīćǮɇ¿žǈƐɾɻҠɫĽȴҎǔҏеɆr\x9bŇǞ˼αө',
                                                                            'úɶMĸɭȆʹЄΓÕɷëü;ШϟɫԢʈȖɍɉÓìЖƔџ˙,ӻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˖*ЀɠԛӃӡEõɕĲ¼ʍȎŗЪċӄϑϔԧƒš',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033604.830721:+0000',
                                                                            '20210327:033604.848512:+0000',
                                                                            '20210327:033604.867966:+0000',
                                                                            '20210327:033604.886827:+0000',
                                                                            '20210327:033604.904967:+0000',
                                                                            '20210327:033604.924022:+0000',
                                                                            '20210327:033604.942231:+0000',
                                                                            '20210327:033604.962294:+0000',
                                                                            '20210327:033604.987201:+0000',
                                                                            '20210327:033605.007321:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǟȯӵӊϦϋXҝкɭκʞԢĨȲʨЩ\x82ȧƔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӅΊˠƥςѻŴȝĈëúГÉʞȆԋ\u0378ԞĘƲҼƷʆñӂбˢȷΑY',
                                                    },
                                    },
                            {
                                        'name': 'İõӕɢϑ±ɩʜӈǥȸ«ɲ\u038b¼¿WӽΞį:ǏТɺń\x7fŞȀ҉ò',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033605.197759:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƃ\x89ж)ХΥ\u038dђѐ¹єɾŊӶӨя΅ɗѻĈŤΆ1сɑɕ˞Ȇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 329493.25164242875,
                                                    },
                                    },
                            {
                                        'name': 'ëϚʣӡаŅрÃƇɤ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԥʡǭɷƚЗԕϚϭ!PЕ_ЖͽƘO©ʹɥq[;žҰțцҏɠĕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĿƼɡʒƧƤθéӺǎӢԧԙȳχʵĘͲÈJϻυьõƬρСʶњ\x97',
                                                    },
                                    },
                            {
                                        'name': 'ʌŌʞӷĔƾҷъƝӦΫǢΤλΒĿ\x8aӨԖʉʿɤ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5909945165762470589,
                                                    },
                                    },
                            {
                                        'name': 'ǋЋgѢξ¬\u038bЛљΑϘǤêϛ;\x95ϋɼſʋҲԡğƽ˦\x83ʳɦƐŖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -57977.09075209895,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƏYϰȘʃĝʪǍ9Άȗ½ӆĬǶқÕщåЩӲȋԫӆȑʪȋѳʂˈ',
                    'message': 'Į;¶\x97ѪӰ"žԎǾѵѺɢ}ҀѧԌNǺǽXÙaІԞʴњȿӄÆ',
                    'arguments': [
                            {
                                        'name': 'ŬǳΝɔҝ&Ыȯ^Ҟ¨AʦǒʄЪϠԤ¯ƼÄҎǣɒĹ˹Ǎϣƚl',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʎͶϣӺїǚɗΦƜ\x8cŀǶϣ˳',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': '\x95Ũ\x9dѼ\x80ʛ\x8dĤŝʖНԇҎū\u038d\x8dӀƺѬȊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΙČςӄĮŖ˜\u0383җğğѻƽĥɎϖȑęԑԬȼŖѥɑǆӮӍſІͲ',
                                                    },
                                    },
                            {
                                        'name': 'ԛӲ,Ƣɒ˻ϐͺǠʇԌπƫéɸʋǅƴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033606.365535:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ĭ\x85ΞŒȷκʾΤʛğԏјԠ˘ӧŖʫ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Cň¹ŐſӦˈ\u0382ǍϛΚʕë\x8dϕͽÜ\x88ĨЄÊ\x88jȲÓâϬԨ˂Ŗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8351414963419093553,
                                                                            -2294331278798819683,
                                                                            6598416983702662392,
                                                                            3432805453215266437,
                                                                            -1976450618700995985,
                                                                            -6415336548920115775,
                                                                            5694373305530451191,
                                                                            8693884529062658725,
                                                                            -3726180441974785358,
                                                                            -9067112654757971577,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'зӘĩυ¶СSȖ|ʺԥԐůКėƈĒǸăҵĵѹȵsѕȶԮπ˫һ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '¢ȋϽӳƉ¡ƾɲƓыȐӡԐЩͿϮƚҎ˫Β\x91ɓʑΛӰ\x89ƛӛжϲ',
                                                                            'СˊэӤӝ¨Ǜ2ԃȘʬ]ƷƢԣλTЙɈƯÜӊΎΆԊȖ@Ǻϸŗ',
                                                                            'șĴɰΉäƻ΄ЀжРџȽӱÎƦҧϛʃП=ԊNƢř×ѓғΣÒƂ',
                                                                            'ƤӱсҮơ\x89ƱҗʾĂr¥uŽ¶ÄȷƏʹĊǧ)ұƮʊ˻ʼͿΏƱ',
                                                                            'ƚmöКԋ\x89ŀ\x97£ҢɷĚжȁѺɝӐũȏ\x9cˍαӫʩ>ƤʡÃβN',
                                                                            'Ӫ-ǣͻϳщbϝҮlЂŻʘПЫ¥˺ρǄƆӻƓńŨ¨˦Ҹ\x96ӝ\x9f',
                                                                            'ɅϮýӰŪͻѬɜƘԣƼɪǒѓWÃǪ˹ČпԔ\x8eŞĨϠɯԋԨѦč',
                                                                            'ŃnǷƌɽαˌρmӨ´҇Ã˔ѝʀˇǔхҮsĆϭжԣəӆӂˢԫ',
                                                                            '~тȏĞ˒ăҤĞҨÚÈϾъ˲ԘϒĈԞЬLХŊȪ^\x8cόΧʜи¯',
                                                                            '"ɽǉϵÙʙЃ¨ȵѮǃС®ĨŋɤͰʌúԖϬΉū˳ʞԓɪԃҟŋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЗˠĀ\u0383\x97ɦϝŭ&ϻʓ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'ȀХȇέԤ\u0382Ą!Ѐӌʰ=+ɿоĩϡѨӂԛӜɉɲˠΒ+ˏЧïѬ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033607.510969:+0000',
                                                                            '20210327:033607.531709:+0000',
                                                                            '20210327:033607.548991:+0000',
                                                                            '20210327:033607.566190:+0000',
                                                                            '20210327:033607.583431:+0000',
                                                                            '20210327:033607.600905:+0000',
                                                                            '20210327:033607.617893:+0000',
                                                                            '20210327:033607.638867:+0000',
                                                                            '20210327:033607.662467:+0000',
                                                                            '20210327:033607.683133:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'UԦΙƣʒQˈċбɹɪɃү%ҪԄπíhň`\x99\x8e',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȔͽΑʭоǮɔġϛΩŅԘĪȾэϐМЉƒѯǾśǶŘѦƒĵ˓ϙǖ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĝȸ\x9c\u038b\x98Į˘˝ŭĚƖχĩ;Y˷\xa0фŮӁšӚҏħuƌáȥǧ˭',
                    'message': 'ČϕӲǅϒ\x97ũӔԆƭωüіӦɎѝѸҼЦdĪɩȉ%РӢı<ɱԛ',
                    'arguments': [
                            {
                                        'name': 'ˑOƟԑԛ<ςŦүǜÆɭþƹуӁφɗŻąҮԟԄкЄʹȥɱÿŮ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ģ`şρΥӀ\x92˰ԕȪūɦ´ĻҏȉlĭǠј',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƹ˘ӛϼԗϐBɌèVӛ¤õ»śұǒėǨϸ<JŀЄĎÔǬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033608.484860:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʕНŏɫƈˡΡ.MÖɻȠ\u0379ɻʎԆhʈę|LƱžˑƌȲ˲ѵԥk',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ȕб\x96ЦƕґʐΌǨƇȴǳʇôʘÁ˲ēԢĕɞųȾùȝ\u0380Ǡ2Ǌã',
                                                    },
                                    },
                            {
                                        'name': 'с]9ʝŁǁŗˈ˄ĠȣÐӷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɓʹ4ϊ×ӞџΐϼʐЖ˯×Ɖ\x9f[ԅћ¿Ĩњ҃&ʨΙɸ˃҇Îė',
                                                    },
                                    },
                            {
                                        'name': 'ȩĎќԌƢƑƠƙӈͿѧϧʷā5ԜϞԣіȘŠ¯ˇ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ñ¨ϔѕɼѯĺ˷ϱҩҳѢ\x9dѼşʈɂǺʺϏϟήфɰϩϧҮ¦:Ű',
                                                    },
                                    },
                            {
                                        'name': '&҇Țč1ҽї҅ʓӻ\u038d`ʠŸͿī҃ȂΦ¥ɃзԊͱ+¥Ƒ.Ʃƾ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033608.767469:+0000',
                                                    },
                                    },
                            {
                                        'name': 'i˫ȿҽȾӓʔ¤ǢVλҶŷɯԂʫĢЍґǋшĻɠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            623521.7431940528,
                                                                            953311.3003838772,
                                                                            980158.2396028263,
                                                                            -53275.48569701719,
                                                                            522947.75174340943,
                                                                            912596.8056612934,
                                                                            120451.96178437478,
                                                                            918016.7040835517,
                                                                            595350.4025864876,
                                                                            551333.0318296235,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹДԨϭĽē\x93ҔȗʯŗŐʠČ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʩēǿЖсɖГҡҘɱʾĥԔ9јĳȨxƊѕʇϡЉj¤ǮùыÁȧ',
                                                                            'ƓƍԖЇ˓áЦͶ\x90ѿ\x8cй\x9dŊ˛Ьʫ\x80lҭԎȀ¸Ҩ"ԁϖd˾ɛ',
                                                                            'ƉϊҁÓ¾μȏƦɻώҠӝ\x978ƤЌœϒҽɈȳɑɼû˛ʞнѕɗŽ',
                                                                            'ñдĖϡǨƿɒδЉҾħRͰˮӳ\\ÃƑц˔îȥͳǽȹεϨƥԌѼ',
                                                                            'ĆԎέțÖʋҭʷӞŝʬİϨ~3ϑ˖гӢȧԂѣǏµϡǉǧǟΔ¾',
                                                                            'ʮȳƣҜǢԈ;ːÿȼɖĎЫßĪ¢ÂСŋхÃϹϰčŠșɎЅϟƔ',
                                                                            "Ҍѹ¶'νӛʓɍԔȐϽʶѰѾŮɋɿȣԝԡƛ?sɸǆшѨș˷х",
                                                                            '49ArʟѬхԠsѐýʗɕʑӫΜɒˇҳҏĵҜɃȼϵGф\x80Фʎ',
                                                                            'Ľ˅ɞʾòȄǕŌԕģ˯ˍpǖɲĹƞȰǯ˰"ɿȭĤӤҒɎӠǛρ',
                                                                            'ɮпʅύĺª|ӒЫˈƳȬ˳Ҁ\x9dҭƻϔԝÔǘҏƢϬfʞŽɦĎ˼',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'βӷȉ\x9dBĢɒ8ɠӮɻĊ\x9c',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8564375448815330839,
                                                                            -3507814192886168546,
                                                                            8514430721009566423,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĠԞҞ´Ŀŗч˧ȊЌқĩqш҆ǈ',
                    'message': 'Õ\u038bәІȤЀВмȷÛɈmŮЃОɣΑʴ˹ƅ¨ϋΠͽŝԍƛВȑÞ',
                    'arguments': [
                            {
                                        'name': 'Л&ӲȨъ˜ӀƜ˅%2ʶҪθϝưMѥүԌγńȸǻAʭƔoˇӬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5517004011894064212,
                                                                            6075811757928370610,
                                                                            -1154985175768203916,
                                                                            7137215563973009709,
                                                                            -2732905356952005578,
                                                                            -2490715023505010511,
                                                                            -3611752231931837356,
                                                                            -9067376295328404171,
                                                                            4764332570526238708,
                                                                            -3673542461038701921,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǕŶǣǞκsƁĚħӒӀΪ¾˰ɳȣǽĹԀүĵԂǮǖ8ɆӧǅưŲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÝĉӉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 102474.06658880864,
                                                    },
                                    },
                            {
                                        'name': 'ŨȓƟĊӊƇКİ¬',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9144025391474369528,
                                                                            7134276298984306882,
                                                                            6794500562717469171,
                                                                            8145123599087542142,
                                                                            -6969881510117119868,
                                                                            -6578569099463347952,
                                                                            -2709281848066820391,
                                                                            4296121330831571959,
                                                                            -62841781084770529,
                                                                            1107074547148775432,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'σӾŭҼŰϿǅĆȼʕβÓϣĂӷZLÒЇ8ӺčЊˬéM\u038bʱȤˠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '¹;ӿɗъψ\x9dѕζȶȎʄˆƛҹcÖɣīʣƀcŷͽȑΩƑ҅уΧ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŦɠdћËĈōͲȴӁY˞ʜνºʋcӗӚǮϰЍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033610.435529:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԂǑӢҋӦjȶȓ˭ťʦÝ˃ĉΡʩӌǿȱрĬԝˈșѵϗӕ˓ϢР',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            855870.7550634829,
                                                                            337973.19500009285,
                                                                            489909.1164009472,
                                                                            461965.5704708989,
                                                                            547911.5939640562,
                                                                            978771.1266589267,
                                                                            327651.9840387586,
                                                                            -74864.28854296303,
                                                                            839144.1207014042,
                                                                            414794.00315862166,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԁƣѡЀўxɂBóȞƕЄКÆħ˓ӲƇȿɓéĚŶЉлõҴªǵȺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5799872147413544155,
                                                                            -2646452754920275296,
                                                                            -979949757529928908,
                                                                            7649578516166056251,
                                                                            -9220656655624204405,
                                                                            475358183604562434,
                                                                            2280421654409321420,
                                                                            5171814805409954445,
                                                                            -1956143554884725561,
                                                                            2627021018833452125,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҎŬξкϾǵǡǝ¶ɠʰǊŵŬÉȘƌ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            986588.9681827645,
                                                                            -37215.765985439306,
                                                                            496782.36517081456,
                                                                            454925.3574144166,
                                                                            723527.9908968281,
                                                                            547680.8539095229,
                                                                            809127.2066978448,
                                                                            -22660.191142657466,
                                                                            -80171.61491221737,
                                                                            953081.0093156912,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʢΑўǄчȳ\x8ať\\ɭԤкљҿǼʃғʙ\x9eВ\x83ŢΑѷǈɺLϮҜ;',
                    'message': 'Ԡ\x7fǶa˘ǕЬԄӹАǳЇȰӔУLQƽПҰ\u0381\x85;ʔƹçɓƨҟӌ',
                    'arguments': [
                        ],
                },
                {
                    'catalog': 'ҾʬьϓƔ˺\x97ͷĪЀʁȦ7ɤıÇ:\x88ғͻҮsʰʞeǦęʽξĦ',
                    'message': 'ѿɃǞnˉŧЋЭþ¤\x90ЈȀ͵Ĥ҄ʔѪ҇ΜŃnпԐǓɱĴїåҚ',
                    'arguments': [
                            {
                                        'name': 'ÍľҹǒӾ˺ЬʴћʅÕƶƇϩˀʬѾПҢЀgяǸŃӱε\x87ТЙɷ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033611.446910:+0000',
                                                                            '20210327:033611.467256:+0000',
                                                                            '20210327:033611.487624:+0000',
                                                                            '20210327:033611.508444:+0000',
                                                                            '20210327:033611.528593:+0000',
                                                                            '20210327:033611.548545:+0000',
                                                                            '20210327:033611.565956:+0000',
                                                                            '20210327:033611.582847:+0000',
                                                                            '20210327:033611.599659:+0000',
                                                                            '20210327:033611.616766:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'G˕ѧĕȂđəǛϸįÍèҪӅԞɜʂƮӁοȞȳӬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ɂ9ŀμцϹӧԝŹăΰўĮ҂ŏǪ<ЮƼԆƺӧӞӖәĢӸũʥӽ',
                                                                            'ƎәϋԌ:"ӶƫȃŦҪʲϗËʰʏÉ.ëőϯϥɮȆ/ҝƐǞ˵ė',
                                                                            'ŻɓϰҁǘќҐӺȏӎƾɓ«ȉϓƐǇʬęˤWӀȶ˞ӿ˺jòâʆ',
                                                                            'ҺɟеŀȸсOԭžѫ\x7fŅ]ƭŰǎΕóƳǘҽӍʑѩĚϧ΅ʮҍǤ',
                                                                            'ԊЄϝē˨ƟȔɬŢ҂ȚʄԂĔɝɛnÖØйКóΏȫԞѮԐҬрǰ',
                                                                            'ʄΫy˫ȁıϐӵΓơȱɨДLѮΎȊӈɤΕƅǃ΅ҳɵɡħğːʳ',
                                                                            'ϐͳǅäȒɉЂūԂϺȼΟΛ*ƌǽ˵Ì\x956ЗэťɞЭӄɺԈӮм',
                                                                            'ŀüЦĿüΫĪįϗŔãOѯôŝs\x9cìxɥѭ÷˱\x95Я˅ȨɦЅΡ',
                                                                            'ԔλŹӊǗǎƣƷŴ͵ɂʸȨÊČǑƊӫѣАʮƎҹϲΨΪϐΌМԐ',
                                                                            '=ͽW\x93ħϊĺ\x93ΚțϪϭԧҧʐ˻ΎȬ8ήӒŅϡɍʪХЀũǘΌ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҅Ыȝ(ǗɛŸ˱ǟ;ǐěŞÒiǂƙӖƷȐŴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033611.982358:+0000',
                                                                            '20210327:033612.000686:+0000',
                                                                            '20210327:033612.019035:+0000',
                                                                            '20210327:033612.039164:+0000',
                                                                            '20210327:033612.058794:+0000',
                                                                            '20210327:033612.083027:+0000',
                                                                            '20210327:033612.100105:+0000',
                                                                            '20210327:033612.115328:+0000',
                                                                            '20210327:033612.130425:+0000',
                                                                            '20210327:033612.145158:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÜϐҝζĂοŋǬǔѵý˭İȴȬċԥ϶ʺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033612.236557:+0000',
                                                                            '20210327:033612.255685:+0000',
                                                                            '20210327:033612.275965:+0000',
                                                                            '20210327:033612.296416:+0000',
                                                                            '20210327:033612.314512:+0000',
                                                                            '20210327:033612.332996:+0000',
                                                                            '20210327:033612.351196:+0000',
                                                                            '20210327:033612.368676:+0000',
                                                                            '20210327:033612.383971:+0000',
                                                                            '20210327:033612.398743:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǫʤǥԮýѮˆԍғŤϓsƍĝĊԪʧāʯȍȂƶnʳ ģ¬ȽɜͰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 2494.4626416042884,
                                                    },
                                    },
                            {
                                        'name': 'ƖɬËԘ\x9eʅȃą;ɿư҈ѻӼ¹ӫχϙɕȫĎȶ=Ͳ˛ІЅ\x91Ĉо',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033612.550718:+0000',
                                                    },
                                    },
                            {
                                        'name': ' Ҟ,ʭΥΫҠϙӣԎȸjЧʪư¡έѩĻĪ\x8a',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5000668918387640905,
                                                                            -2353033582806475938,
                                                                            -7722754475459498306,
                                                                            8616989521483829894,
                                                                            -4711793242211064757,
                                                                            -6572275605972722073,
                                                                            -7844203774474944037,
                                                                            -6541524447353271103,
                                                                            7716406459332175478,
                                                                            4253299135466819994,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѡūǀă\x83¹ԤȱɊʨȉЀҥ˵À\x95˪ȌŋȅΖDH¹Ӓǖqȅ%ǋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033612.910029:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȒҳȈǋêμȑH',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033612.987777:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԂǒѶȲХϦǐͶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 224934.111389214,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɿɃ˭±¹ӮΐҠȟƹĤ"|\x8cмэˎôӪЏԆɃЫӞжӗƗϋKм',
                    'message': 'ĞŔЖґŀәʜӲǳѺɿǬǶѡƘҕƐдºʄϼƮѦŵțÝ·ñїъ',
                    'arguments': [
                            {
                                        'name': 'ιÉ1ҔҮӫň',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8320618431602254959,
                                                                            9115705471099330936,
                                                                            8751841377269674465,
                                                                            -1184446370326404594,
                                                                            -1075772932175740349,
                                                                            6296619058553479457,
                                                                            -7734743794773150905,
                                                                            5715567162694234968,
                                                                            -7613781912710350680,
                                                                            -1956398222194159411,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ԁʪ'ǪąùēØρΤɁɖϟɉȼāХʊ\u038bЖƔЄӯҘȪƳ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7862132543482012632,
                                                    },
                                    },
                            {
                                        'name': 'ӭ°ʟƆ0˵ϹƶϷԆǢŮȹεДέ)@ӦĺɣӣßǅŘƜ҆Ί\x9b',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҒšȢҎҋ$τŇϓŽӳwІӾ$ɭϡϮɑ˄ӄл{˃Ô×àӫчұ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ģӤưӳѹύΜΩÁзм¨εýѿɋ˪ţǛÄϛӜư&ɠмʌʥҔӋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5714630050971476721,
                                                    },
                                    },
                            {
                                        'name': '=ϮǏɣʇ]¢\xadʁŎ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4456206033822206246,
                                                                            -130386824511032724,
                                                                            -3840240499011662320,
                                                                            -3714992953917275063,
                                                                            4041127549119208859,
                                                                            -5633320773456700032,
                                                                            -7744273602786751839,
                                                                            -3000904442958622955,
                                                                            3018980937083529580,
                                                                            -1418694654860526683,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɡʊщ˻ǵʱӨӄƂшВϾ÷ĭΙЙ˩ҽЭ\x9fǕǮƤŖρ\u0382ȄϚŸ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ķ˾½ϣͼńÇʰ^×ӪһǾ9Ͽũȋ\x89ӤĈ\x88йĐȦҗԣŹЖʲ\x9c',
                                                                            'ʱԌɜԌͺκǾӳřҖуŒɢқȅʩͱÂʒѢiGƒыӥ@VƹԌʴ',
                                                                            'těʉµҦƍƛӻГˇШӚт˼aӊӻĽƒϭȦԨƝ1ʠϥȴӒǍИ',
                                                                            'ʂMҕźÔϐ§ʩɩԤӓҋƛȷ\x99˜´˝ԧЂɒɧӟιˋ\x97ӮưӐϵ',
                                                                            'ÙÌqŚЎǟ\x9bЌΐ:Ы˄ѪɁПv҉ӀȌӤзǅ˚ΏѕƨȇЦǓP',
                                                                            'εŚϛÁ͵ЗӚ˹Ѓçɏʺ+8ѢʤϛӹƥьÍʼԞˈЌǎψԐԩļ',
                                                                            'ӌӼћʏ\u0380ЀɃʻÅԉЛłϙɳçԛȄ\x86ǖşƠɴʏ¡ɇŹŤƱнϠ',
                                                                            'Пȃƃ-ӲRҊҝѻȵμЯЭԌҠ¶Њύ%aŇАȆͶǜнγɫĳӆ',
                                                                            'ѝ§ȭʗēǙωЫȍѵΌ˴Ȝɼ\x83ϯҎ˄μʯˇƂЌԜ҂˖ɟÈȕĿ',
                                                                            'ϻǃɉŪȅĔΒɊIˤǭƢŹǓӡӴѹΑʌʍ˅ӕҘĶͿԇИƅöџ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'гźӘʧȴҏēƆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -87201.39392313654,
                                                                            495004.42735271214,
                                                                            -2931.638257961531,
                                                                            487204.14212407207,
                                                                            162293.4086742156,
                                                                            -12422.704236040387,
                                                                            28157.93788765154,
                                                                            -63793.72546966201,
                                                                            152467.39989930298,
                                                                            513718.5119911283,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ђhЎȗƨʹҞҋԑɅЕĉϸ˥УўБ\x80ąǩ\u03a2\x97V¾É¼ƺɠ˝ӧ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӨºЗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϖ\x9cŴԞ{ſ(Ҍ³şɱɕˉȜ/ϚƢťҤɨ\x89aԎɆΔɰƩϡśǰ',
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

            'identifier': '\x8aňȂʊʇ',

            'categories': [
                'os',
            ],

            'messages': [
                {
                    'catalog': 'ɜΪ',
                    'message': 'y',
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
            'name': "К˘èvQʟɸĨhӭißňȞ΄\x8fȲɰƬÜωϨ'вǅԂƙ[pÊ",
            'error': {
                'identifier': 'ͰÙiɵʢӔРӹҝЍҿ˔ÄҼȪ°Ǵвʦʿ)űϛĨ\x90ьүΙúǂ',
                'categories': [
                    'network',
                    'os',
                    'invalid-user-action',
                    'configuration',
                    'file',
                    'access-restriction',
                    'configuration',
                    'file',
                    'network',
                    'network',
                ],
                'source': 'ÓWҔɮΎ¼ԕԬҌ˷.\x8dˢǙϜöûͷǢ=˒ÅĘ³ТͺĶδĻÙ',
                'messages': [
                    {
                            'catalog': '˭ōɢÕ\xadԟĖfɹɅňԝτ\x9dͰԏŴɊőέĄ',
                            'message': '\x88ϣ§ӌӐɆȟȴӻǭϓčѕɇɊ˵Ͼ¿˂ϐɯ˫ «ӞҶ²ԓҾԑ',
                            'arguments': [
                                        {
                                                        'name': 'ԧ-ЄžʯƏȝȍЙΪΪÁ=сăèюϞӟЉʗģԟѱԤ˞˚Ҳ˽ʃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '҃˞ԣѣӌѴÕѾȳ\x80UҲŵɒҾſдǞęӓŀːǞmŌΕʮӒдǛ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҙ¥ŐȂѷĤҐӌ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԍӘǂo˧ʡͱƴPȳтźɄжíиѷâѴɻȗǎʞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'čе\xadũԓԫeǓæԍțÉėȍРӊß\x9eÁԕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 988775992281733763,
                                                                        },
                                                    },
                                        {
                                                        'name': 'D˅σѶͱȹäӒ{Χ(ўʢɿǋӨǙǙϕŧ®иӴӠӠėŹΙҕȂ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȃ\x8cҷƽɗŃĂ\x8eʐϣƃЄŀȘǗвȱƵиӈʎ^ĥͳԚǽӂʞƣх',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˢ{ƾϧȷL²зʔFѓмî²ӼӾȿɇǚǌĦĶШҾϓ#ԗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7644493446388742946,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӻÉΫɣǜĞ˞"ǍĦάǟЖʔӥôGáΑ\x9bӴϭԎǴƋĺ҈ʐʦ\u038d',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033550.578878:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǪӶLaɄȓȆmϴ!š˵ȮÑԙǸѢŅЏ˧ʬϔαЮǲӰ¯',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØʋƔȠƕ\x92ˇƒȁԓ²ʪʯɧ˸οżǅϨȦǿȦʊѬ¡Ёҹιґ˷',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033550.722462:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЂȔ3ɣTøˡ˨î҂ԍƭ\u038dΧѥǢWčǡѬɣłйοϐёԬƣÔЛ',
                            'message': 'ÀȏԝшͳˍʙЅȑԄѢ\u0381ąѮʨʌĴλѷуϪĝŮʒóċјоиȨ',
                            'arguments': [
                                        {
                                                        'name': ')ԎƗˌγīµùɜɛÆ©ѹǔҰЗɩҳӠfõ\xa0Ȝ\x81BВϝȱҝˢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉΈκˎҞξΓ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЯÔŀȡӤƳ.ȡƹǬʱðʴ˒ӫȘȨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -181852935507239141,
                                                                        },
                                                    },
                                        {
                                                        'name': '©Ђûſѡбѝϣ\x89ό\u0379Öʌğ¯E\x9cdͻİόϱʅʑ˭҉ΟҰôӍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣҪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʐģҿ\xa0ÇĊ˪ϡЁʹǙ8\x904ʈ˜UИ˴Ұ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4034018173563193933,
                                                                        },
                                                    },
                                        {
                                                        'name': 'чòѼ÷ЭЩшϚŽϷυϨӓb',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ªɍĜӎĬāʍ˚ӧƸЪѱ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 568679.8404201124,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҤΡħϬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȂøϦ҉ǃЏí\u038bÛËĴч˛ÏԠɈҬіҊԊϬ˙ȪӔǊʥѤàǵӟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ѝϙɂ\x84ԑ"ӓǚεϐԟ˞cʅӨԉϠҦӲ˼ҤĐ˯ƽʓȰɇÆǲΊ',
                            'message': 'ξϯ\x8cүԓ΄П\x9aңɾɟP-ŎȗԇɧβoӦɡMӃŢʐκŹŊ\x7f³',
                            'arguments': [
                                        {
                                                        'name': 'п˔ʢǨӽʹʓлӹЅƎ\x9aХ\u0383ʓ2ȄđѬþɢäFÀɆȻŷĵɛɃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033551.870457:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'MĨƛκ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӘkʍÃѨƷҫӉɴg˴ȸɆͺ6ȿǱʱԠӐñΕƂʞȬƘȝ˻ȵE',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёқŴõӜϫɁʳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 606373.1628797387,
                                                                        },
                                                    },
                                        {
                                                        'name': 'îʢÅ¿ϙϵÞĶƾǁѰԎʹЧ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƹė\x863®ҮǫǶ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ťWźьԐ˲ťÊƬ\x8aѳЭ*ɸÆȸɒaԞˠđ\u0379αӓЕрǌϵŔʭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'іʰǟςɌҽaȃˆϦ¿ѮÇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 9248.292761926423,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗİHƭΠɻƲˣΎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾҐԞĔȂ˥ҼóäˋȌɧEЃ\u038d\u0380ұ)ϲŵǄ҄čӉÁǸǮʩɞӀ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ȫ˒҄ʞƾɱґȿˁ˽ȿͷė*χӾȨɂ¶ŴĴɭʵ҅ϸχåΗưЃ',
                            'message': '×ɜёϒȰìɦєp˟\x8cθҳƴɳɲБŜȣԙȐԝȁЂ˓ͼȸ{ȠϠ',
                            'arguments': [
                                        {
                                                        'name': 'ЊȾӡɝȚλʿȋ\x94<ѕƾҏ3ʃюӼѵŋÊ˶ҡKθŃϢęτǁ˜',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӛčϰˁϖ®ѳьr˥\x8e',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 257458.62079066352,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϬԈɰuԨь_ЯΰʐȺȥ˷Цƭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʎͿҨǘȈǼĶˍƏðɜԤƕȂ˟£ӄǾӭũɉȢ)ŷ°˭ǹґӲV',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԖфŝeAƵňЭȭ\x9fӢӷ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˮӣϱɬ`҆ɯzШϚѴСΉʬрĩϛҖʟʀԏÃ\x87һàΌϳЈ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033553.136402:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӔТԈƪżüԈѳЀſȨĵϓƩľPυʲȏƩˇΚІɴϸĆƠȫȇǤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚȟɦԬίјɄ\x8dǈ*ӸõНʖʻɘ7ƨɧĜͽ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4575074826143783118,
                                                                        },
                                                    },
                                        {
                                                        'name': ' ϮǴŠҬɷϩжӆǝɼȷǍɿҾԄҪǓбǶΜȾѯzĒSɫɷЈų',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƌ5m˻oƘφĴɽҶIñÑyΫɌî0рk{ϧφӣŢӡ˨Т¡Ì',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ńƌ=Ϳν#ϰƹјӬ\x89ԉʅ:˼өѺԉç5ъȤĚι×ă˘ҞĤв',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033553.446420:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x98ȱȋӕɥѨϲԒȂʵқǗЍŀfʪ·ñɛѣˣsʸɋϡɜѯ@ӑԐ',
                            'message': 'Ѫʴź¶ɤǲơ¿´ȁÛΗ˴КҺƾӐƳ\x92Ŕ¯ϠHьϏҿïӉȤ<',
                            'arguments': [
                                        {
                                                        'name': 'ґD˧äЧӟѧёù]',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΛȿɬΟɹȰȉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033553.693255:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽİ\x8cΈϚʠʎȵӳӌū\x7fҎ6¸ȼԍųMӘơ±ѼGӳŢΗƬϷȰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 424000.75795438193,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɸǳЦŦ?ĶӠûgЏҥšÓƬÓЌиƸːзɮõˌҍɫ6ξƑԣƛ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 950307.0001826587,
                                                                        },
                                                    },
                                        {
                                                        'name': '0ƗȣɡΑƮ˟эʄǉ ĕšɢéǌЙȴ˼ӲɈɡÃǲˡҦʮѼYR',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 770069.2698497124,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÝȜȗӒԓǚУǡǷǇѹϠͳǓӖʣƺέΑ®ѩȰŌԦ?Ǭsϸԏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯÂљÕģϺĶ\u0381ЃȩıғӋǒχъпʚǜŤԌʘў˜еZKЈб\u0381',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѩǩ´ʓӛҘí',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3121932159552535228,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЯŤIοă¸Ű;Ӈ˚їȆʎƣ\u038dĥǨɖӎЮ҈˪Ӫü˼·ƺҠˡϠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ηԏγï6\x9aϲɶϯɃ\u0381XЅ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033554.535703:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʋSʮˎʎ©ηϒǇԛАʧқǫԨҁɏЏ-ѐȗΌˮJҍŉȧÐĩԭ',
                            'message': 'ʜϧήѯmϤöȁʄ\x88ӍǪȍʟ\x7fГóӨƼłҽΒƥüȽ½¢Ϣ˵ɾ',
                            'arguments': [
                                        {
                                                        'name': 'ѥ˹ɼԊҙЮEӅźҡoќ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɚŷüЧȞɭĽҎΟ\x8ešЗӽȤѡԍǶpˏǪˁϼˀˌԗԓĞDўǍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƷʊўİέώƽmϜɤơΣǝξЭԈϷ˪ńԅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'еΘ{ҠЮ¶Ɩ0Оȁʩə¾',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'áψάӎ\x80Ⱥ¾ьӂŉѡŢʗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ʯԠƐҕяúƄʇȪѹΗлɠїʦG¡ʅқƁ˫Ɗ\x80˾ԏ'Çvyā",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԋčщш4ŵƄјҒѰлƸѯӜӨ˩\xa0ˇΝҊ҆ѭӞ\x8fȃǘӸСǙƉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'з}\x9eňˑȺçʘʾʍʃǝʽёͽЌϲт:',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϑγ-ă',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϝɕԏ9\x8fǿȧѷǄŀő϶˝ѻċĜǝ\u0382҇ƱԌǦʲʱʦΖȻƙ¼ʮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋҋ\x92ɞƼʒюΨǬοǼ`ЀͷˠǷɏ|юЖѿĒǻӬ|ҭӈϺѶӆ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǻСˊˉюə\\ĞӆȾΎФɢ/ϢϫãŗξǓǄ;ϯҝȼƕaǩϢІ',
                            'message': 'ʐ˻ĆšǡгѰǷϤҡ\x9dɷөʃˀΩ"Ǔa\x88÷}ǈƴZʠ˚ðȯŚ',
                            'arguments': [
                                        {
                                                        'name': 'ȣʈ˓Ĥ@RìҺŷѡԛŜ¨˺еώɐÔҚʩԤΡĻͽʂоЪ?ǆў',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʻԇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʋҧºɜQ҅',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾǡǼċԇʗǗԑxѣʎРð-ʄĕЄǣми1ΩVB,ŪӼȿез',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'χĬАϭͷ˃ɯɲ6ӪΕŪɽ΄˶ҦеŁŖʼȕԘαƋӚɸʥʓųÇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȀĐȾжńĤҊĥ¬ʈpѯωÈѰǱ(ğBłΘɽȢĝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 975380.2777914233,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͰjʄϞѶǞĥNɡѳϭԧЅώǉŹǀÁ¹ʋŚѐů',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'UҜϋķɛˈͼ]ǔ˱ѿĒ£˯ҧÌÄɴ.ȶǙǱÈӳʾşG˲\u03a2',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ǟ\x83ӟ˱ɞ\x91γ\x84rɕīŇΫӛ,âȱ¬МʈĸǮĘʶ\xadӟě҉ͺά',
                                                                        },
                                                    },
                                        {
                                                        'name': '҄ÁϔԎʜѫ\x86¯ǽ\u0378Ēӛʝȑɺȿσ˄Ŧ˵°ҠÇ~ћȲŐǧĞԊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƶЫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӟ˓Ο\xa0ʴΛÃʕЦ˶ЩčϡĤʏ@ŭϥȚÃȨΌɴΫ ´ĤǕǜ|',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҳŋљНҤƊзȷӼzȼɌǷɃү˼ϒĀ΅·ҷж*\x90ӓ¥ΚjǏĖ',
                            'message': 'ɦҦΌŌҟӥȟʁΡҝɦcϟÊíԭĵrҪÏτåʉ;ÖƂ\u0383ȣǖԏ',
                            'arguments': [
                                        {
                                                        'name': '\x80ãԙιƤĀ˚ȈƛǚίʰДýǤ˴ƛͻҤƖǵˌ\u0380åңУŤƨ˒ѧ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŗɃȏǌîΧц»Й5ş\x96\x93˫ҎȚрũȇüϹʐʮ\x8dɛìӿ˧łǘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˸r¦ӟũˈɟåģþMԐU/Ö\x99äөҀŜȡêƔ{Ұԇΰȍȣȼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033557.293326:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҬŠŽ˱û҉ȐԥЄӿˀΰÚȑԖ˟ƢƥÑǏʲ{ΜńɌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӄMíĻ˭cίžўєǮΡзƿɩ·ӽŀKZˍʿMGКҕ˟\x85їӡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠĥY\x81϶,Ǜ±ǿȘmǰů±îeʷΡɑŲFӆˬhƬ&ҜˑǚȆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ñѴѠCѮȽϮőȂм\x97лå\u0380ǪӜҁδY҇\u0381 Ҋǫϴ=Ѵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǲƦŃŢVïΖLħӏη»ԮоӣТ˶ОƓ2ӼƉ©ΡŬδǊǦƋТ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 161638.6698317504,
                                                                        },
                                                    },
                                        {
                                                        'name': '˨Ŧƣ(ПҔкƐɈѭϱ«Ƙέİ×ˬӾЦƬƓԩ\x80ҺɮĎɑǗǆ˅',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ι»QΛƆ\u0380ԣЋϔ˲(ȈԙĒȇƉơʔɓƀҮúЁDБŷǀҦˍϡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'љϐɵʭέßԒιʅҕɔӯϰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 465107.1679385784,
                                                                        },
                                                    },
                                        {
                                                        'name': 'VȿǯΣˋ)Ϭǈӈ¼ʗ˞ѓƈɒɭßĬîɛѳĜũǞҎĦγіȳӴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033558.111788:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ýŎǟ˧Α˜ϯđʈΛíӫ\x8cŃьƓӖĭŸɿĩɧ҆ε϶ʣBɾňͳ',
                            'message': 'pÖˈϽͳСʵǵϩѦ÷ȕԙпʴʔʵԕϐî$ԩҽɠӷԄƲѼϐˮ',
                            'arguments': [
                                        {
                                                        'name': 'Ĕ{\xad\x8bšèʕέǈмє',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƙ˂ɿчˀ\x9cѹӈΩ˨Ⱥƺ˅Ҙʽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҅ˊΖĿнǵçŮԏ±ɭĬΟ#ł-˔AҮÞđDw',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'җȨϯ;_ǁНˬßÄɝђȴÑуŵ˾ˊɩěԎҕĠūрǝɉʍCÂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 592024.7668561577,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ðϲ҂ǇɗϏNӑʭ¾ÒԛшӓǢԋɇƟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033558.632910:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѰŦϕč&ɒΗ]ҿҬӱҫȃӂɼήʴνюŪýϾҦĵ"ˁȌΰȌʮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4642466115527375903,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǫƜӪxЉjҁ-ԍӤАĮϘƓԝѯ\u0378ЏЧԡˊԠȑҖ\x85',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 420858784003147347,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩΈϦΗϣcӼÏťșǤЩåщʦʶҕȟ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˈĹɿΎǨǒ¹α¡ШʪɟҦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'еμ®\u0382НљĀ²\x8aѾƹ\x8fƸiɴбéȇМʥѪ˄Ƞл˗ΪȴђДź',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4998030946984345519,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҞčӆŻɋ\x90ʃҥɭ\x8aőÇ\x98Ɨ´ʊϱƙ\x9ed˪ӎȒŰӈĨƽȨʉ͵',
                            'message': 'ψɀŮΤǨ\x8a/ѣӾΣԍΪǝ˄ʠgĤŲϹ±ċӦĤýɡϟӪωʕѥ',
                            'arguments': [
                                        {
                                                        'name': 'ũbƅΦɂɂ.ɞɎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȾİԭȼšƋ˾ȥˉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϦΨϧ\u0381ӯŻΨǹtЏҵ¦ӔӰȡřǐʜϨ+ӘŸbӽZү˰ɹ&Į',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Θ҈łҹʧ&ҺňϾϮΛ˸ϑϧAȅé˒ԥѨʛNԐƈɕҜəѢ\x94ʹ',
                                                        'value': {
                                                                            '^': 'bool_list',
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

            'name': 'Á´˴',

            'error': {
                'identifier': 'ğәȧʧˋ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ʛĥ',
                            'message': '\x9c',
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
            'name': 'ÜԠ\u038dØѡ\x9fѿяё˻ÛȋëцņĐjįGҫԙğԣлƚ\u0383σԀ\x8aǗ',
            'version': [
                -1789955133530031442,
                -2695329515811700363,
                -4876853196685643249,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ҭп\x91',

            'version': [
                -1261760915390441490,
                -7928388297824112063,
                -3327297098290627433,
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
            'event_id': 'ȤdŬҕʕҦXΫ\u0378ȺѨτʤ\u0379Ǹ\\ёԉіjÒФė˼ȵĴĘҪŲĲ',
            'target_id': 'Ͻ½ʅҦҲƍѱɇʆҩ˖ˠʌΠ˵ÁϤǙϓșεȡҋԧįƓǉ+ъΤ',
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
                    'event_id': 'ɶh˅hđεɺʡЋůε\u03826рІħˢ҅ˮҴïҕǾΉ+ӑȀ΄Ԗɧ',
                    'target_id': 'ąķπĮӆДƋēƅңϏĸĹTҍƘOÜʫϓeNy·˸ʭȦȷϜӷ',
                },
                {
                    'event_id': 'ɑҥ¤ŃүЫ¶ҮЀҘͳϸϗϴήǲҞҋ±϶ӪԉǪғχ´ʑĦϼ7',
                    'target_id': 'řθϧǵOʕӳͰɰЧͱç¹sʴѭuϳ˾ʮӁʀñԩөѪβŝęǜ',
                },
                {
                    'event_id': 'ǆɑ÷ДɗӽѯǼ}NȣΪƫʂȦǗPɥ˖ԜҢŅ˖ȈÓɳӋʭΆϗ',
                    'target_id': 'ȑǜȔ¸ϞŭxÙӽоńТ͵ƹԔ\x88ԁϚɃӶƜöŎ˱\u0380ЅǄ3ɂȼ',
                },
                {
                    'event_id': 'ЙƪӎǣԅʴÞϱήΦѽ½ĿȤƞŖb˹Ӑ¸ӂPθ҅ȂMȃĉσČ',
                    'target_id': 'ʺʴЄϷчáɞǑѡĴ˗ϞȰ\x8cƩ\x9cƿȇĪǎɜƳȼκҕФ˅ȷlϸ',
                },
                {
                    'event_id': 'ҫҚμԢф˃˳ÿǸɬЄǥ\x9eѭzѰ',
                    'target_id': 'ʿqϭĹʳԑʬЁǩĵ˼ɣ˜éĩʓԞǤȪȣаӑþȮĴʹҡ;Ý˂',
                },
                {
                    'event_id': 'ɇΏѷѰà\x93юˆӿҿɻБΒĥͱ˧ʓңԛƋԫ\\υû\x91kĄϐv΄',
                    'target_id': 'ǊáҸŚдȿêǳɅΦҥѦȇЈɠςĺЌįŸɋƦҲрҚҌt\x9bɫΫ',
                },
                {
                    'event_id': '\x84҃ЮSͰĮɸБŨӕʜϘӛŚƼуϳҺДƿÀʍƧèͿxʚƙϞˉ',
                    'target_id': 'ϣωѢl\u0382јëԂίȷDКЫΠΒă£ЂEǝÎǢЙѓĝǷƲҳΎ\x84',
                },
                {
                    'event_id': 'ǤǓя5ƉϊʘɕɪқƂʝҷÜõĶ´ϥ\xa0łˈљөԟˆȹΖȧ\u038bɩ',
                    'target_id': 'ň\xa0Ƥ˚ьǶƂĩҸʧđΜȳҭƕӴʤʯѧƁÄďæѪԣӬҤëÔ\x95',
                },
                {
                    'event_id': 'ɏӫӺЇϻАËҢӀґЖȎɕ2ϢӰʅtϛϤǷo_ѼʅƦ=ʺθǟ',
                    'target_id': 'ÈČйˑƥï\x84ƅΪνҝώȽĥίӶΨhɠѱĢҐӘԢĢ˔ΆаǑ#',
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
                    'event_id': 'ȧĊοǣҭKʄĨˀѾɶѶɯŘӢŭģϲрĺяŪɠšԛЌσӀ҄Ǖ',
                    'target_id': 'ŐŝԅűӳhήΣŞȨŘ͵҇ϋҏ©jϒͰϺvÁҭz\x92ƶϞ\u0379ӉԦ',
                },
                {
                    'event_id': 'ϖЌŻɵȮ\xa0*Жǻ',
                    'target_id': 'ӅϒɌи˓Ý¿\u0382ҝ\x82ǀʪчϚȀƽVʖҊǶæΧ\x86\u0380ŲǞȢ˖ҦǍ',
                },
                {
                    'event_id': '`mюη÷ňɅӲʵȐ\u0381ί¬Ѭώ˵ԝ\x82ҭΙßɩĆчȑˣƬī\u0380ʊ',
                    'target_id': 'ЖɆҎˤɿаǢԒÊĹГŶgÄ1êƱӼ\u0383ǧ˹ȚƺϟĨӾ˷ҺәΒ',
                },
                {
                    'event_id': 'ӂѕʜӛɉĒÑϤ˱ҚμҘŘӶƠ\u03a2ĩ<Λʅ˒ÛǢώ·ԒɞąƤϬ',
                    'target_id': 'ҞRӔöƓ´JņӳĚҝ\u038bȚͺϜɣȹ\x9dӛʿǒζȓҨĵɨЯуʓǽ',
                },
                {
                    'event_id': 'КćŖшŤƙԏ˛\x9eɶїПϲʃñɩʕ˹ƽ˟мȡшǝ˃zԮϏаĈ',
                    'target_id': 'ʟ$ҀÕΡʷȅʂȻӔĺҙϗ\x8dыӛнŔÐĒͰǩǷѱƴ½ŮG¸н',
                },
                {
                    'event_id': 'ǘĽʘʞʪō˥ŉеЯΟԦȟыùx˧ɟƲ˲¤ƊӹЩȥɷғԮԃµ',
                    'target_id': 'Đ\xadԇѽTъѮÝ҄ʍ/ӿüԮҾȼʹʁÒ6ϿƓǘɄsÿΰ˰Óɺ',
                },
                {
                    'event_id': 'ºƃͲ£Ϧ\u0383ÒηŖϞŠӔ¦èӏƁĆƑ\u0382ņǃŭžȕңåɤĘӯр',
                    'target_id': 'ļБԞˁ°XǴĞЕŮǎӒЭŜʡƣԧȩʈͳͲƴφΞнΥCɢȕǡ',
                },
                {
                    'event_id': 'ӬφžԀʋӝώĤȧWȂϬξҊģĘЂҍΙϕɆԥěÃύċӪȓǥź',
                    'target_id': '¼ϰƀюĪƮȆFʛҴġʙėɽҍʓˤČΫΊŁѡΘȋԢԂɊˇРҦ',
                },
                {
                    'event_id': 'АңȜŲǦǗϼЁȡĘӵБϜǬŎƶǫ\u0381ϬѹɚzҔYо{Ғʊҿɱ',
                    'target_id': 'ˠƍGƥӡĦΘÇʑȟɁϋѬаԤn÷ԝρĊРΎŔțĿȽѳҚШƽ',
                },
                {
                    'event_id': 'ЉǛθÚüȌ0ϐˊȹōȺʌӄЉ°ɞɿĨǑͶѢəǱμzӆʚˣã',
                    'target_id': 'Ǌé\u0379ΠМӌʀƄα˹ʹµ6ͺğ˯ġʀʝŪМȐƶʚǝУωČԟ϶',
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
            'name': 'Ǚƫȱϯ\x99ԃШɽƐмәŃͽˏͽɫ˄CѸbɓȦĵϮ§ӁѪϦ˫\u0378',
            'version': [
                -6141227816265795209,
                -6442483500149983256,
                -4938705048987601962,
            ],
            'about': '˳øµĎƔ©ɣĒúӮЌӔ˾GʵÃ˭ǣǋҴĈϽԅvӹϐʀǉвʕ',
            'description': '\x8bǩȪѥЭRӒØʹ˕ĒɂĵӤ¹ɓӍk»әïRЙϐǰяȞ§\x90Њ',
            'authors': [
                'ƬӵǡԦʻɩÛ\u0379Дg\x94о˺ɃúӵȤlmȨѰŪ\x8cǵǽЖȐWќΛ',
                'РǸèԆʏȒІΥɺΑ\x9fӴɮ\xadфϰŹŌǚʔɢkùήåȁєшҡˣ',
                'ʳϞӮэ\u0378ƑљƫʔɤǱЮΜɾɫȑчѰĭӧʎԐ˓řǌϫϰŒԈӨ',
                'ƖȔ˚Ʈѷϻ´ʘѓƶѣ\x98ѾĜѕ§мӦΊŴΧǵFңǱϴĴΨMŦ',
                'ζ΅Hϐ˖ҏϜȝǿØGĢҰɟтϮʆ',
                'ҒāҠ(ĕ\x98ʳЮʣ\x81¾ǲϩƦȚĳÒõΟ·ά÷Ę_YԄӉӅǚл',
                'ʙżĕȠѣзϹҰψ˷ȆyǀǨёϞƗĽÕ',
                'ǴõɩӋƚԡ҄Σі½ų\x8fʾʜТғǋˋŌʎIȏ¡Ӵ4ʯƎˢɽΣ',
                'ҜԞțʯАħŒӥХÓмЪwԕǸΕ˘£ȄʱѥǴ|ӂƬǇʲɛHη',
                'ƭ˨ģδԁʨԞƻȆЯʍУԕȿӋҪϷϷԧɶϧɲÞԨtʷЅ±ɝƧ',
            ],
            'licenses': [
                'юΛbʇ?ǱϵҧǗϣ1ηƤЂϿӳȇНʓĹȁdʏ˃ųÁҝƼδо',
                'єӪҒŝȲ¤ѐИtƉˇˤϟνÖъ˧ςў¦p©Ԓҏȇȳ\x98ҽ¡ˍ',
                '´εUƵ®Ñψ5æΟȰήӞńѥѥ·˸á¨ͱ˨ƶРϣԑūʮʔƖ',
                'ѲΡϺŸЬњŁԘѼсyɑƐƸηҳçɋНП¨oѱġƳĵ|зάӓ',
                'ǚ8ҌҞ3ƨҎ§ĘĪ˄ѱјȳ҂ϼɏɞʣ«Ϥ\x8fcĭӧţrѦȖѼ',
                'şĐ½ʡƠ\x9e¶ȱaȰӼ҃ƊѪȁ\x95\x83ƲžЍWǢћȾӰƨԏɗҐѶ',
                'ȝLύʸўV΅ѠǧOΊĉ\x81ˠʪŋӡƺʵşŻϕҞӰԔÄǐō\x8dŤ',
                'ȥ˩\x83ԌpňºЪ\x8cʳQϓЖ\x91ѸƜżˢ\x8f}žŗǟ΄[ϩ҃ÀлӺ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ұĉŢ',

            'version': [
                -1902389779153015132,
                -9020132588701316766,
                -3519328076152675909,
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
                    'name': 'ǷѐүкɤΓʅȽ\x9eƬͱÑĜǃϡϱȆӥӭʸϼ¢с˽ɍS˯ɀɝÔ',
                    'version': [
                            -6779704176428565375,
                            -1678511261916525768,
                            -4021162059847977327,
                        ],
                    'about': 'ɽ\x83ȭɆȨǚϹʹ«Ҏ\x92Ʊďɐ×$A\u0381ӈѵȍɠǓɘƥо?Ɨ\u0383ƺ',
                    'description': 'ˀŖГ˄ʏΈЩ*ÞƖīHƩԡy¥оƶȥΰɗʕԪҬϢώęԎӐ5',
                    'authors': [
                            '^ԟӃΩɈƷҋɗ3ɀσΪŎ¦ƗÈ&ĤΦ˼ξȊΛ\x8cӴƳѧ÷БE',
                            '҉Ă+nӰθɭӄʛ\x97ӬЗǢá}ҸԏyţƛǕǷсrϘçъȦΐǝ',
                            'ɋԜǪиWÏӛßõǸÆжSƈӕĻζʧɀĠĄуƭѹǼkȔťňҠ',
                            '˲ʑӰ1СԮƟʵұƛЈÔҘʂˆ˦ʚЦԨɀåŐƀ˹ԉʤϔ¡Ӡĝ',
                            'Б˵Ȅ\x94Ȁ¯҅ʷı3ȡÉǀǲԄĥ˟ʿ0ҥ¦ˁłмhӗӠҀċǤ',
                            'Ӂ˥ҵϟw»ÔӚ\x99ǩˣҕʹƆȋĀԇɶĨÄɞѦ\x88ϽŃïɼЛ˱ǣ',
                            'þʙŁjԭǚΜӍňΜѻԔǑƵű\x9a',
                            'Ԩ)Ԭӱ˨Ƽ×}к;Ŗļȡʧ˔кʱȊƼɱĉǈʿђ\x9dƉÌԗԛû',
                            'èʽҧƑʑqӱÕȑ;ԨϞȌσżɓҫɌӉͲӶρ\x97ŧ˽ɝˡƧĴα',
                            '×Ъϔ«āƩrӊԝҀƝȐ\x97ӀɭѕĤʵεɡǰȵ˼ԗˬʆЄ\x98\x92ʀ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ʞμǼԗĿѼ"ЂɷǄŲϩŚwїԎɓ°ˊʕȓǬΏҷЋӵԝjǹȪ',
                    'version': [
                            -7444047402353573579,
                            -2113284650718311838,
                            -7760624055396427102,
                        ],
                    'about': 'ИƌԩǟĕÛͽΈΦÌǵɒϙĶ¨ðˡΓΕƁӄgҕӕԤԕϢÍΥ/',
                    'description': 'çҮ£ХГЀҟċ\x9fΚəǆԒɗĊ¢ș6ʏˣƹǵҐĵͻʆ\xa0ϻǚϮ',
                    'authors': [
                            'ġ)ˍҚāйǉήӀнqΚʏŖӫҜřŻкŀaɖʘʰŬўȨϭԍӇ',
                            'ĝȢåmǾ\u03a2ʿaǄʝθĭùƌͼϻ',
                            'τ\xadŲųĘıóGʭĺЙ±ӌȁ\x93ƏБΒ҈ȋ҇ͷ\x83ʜәˊБʪȑƬ',
                            'ӑ\x8bӇЈшɍˌѵǢνʼӆiȶӴʨУҨŻŔŜˮí·ѕ]ŰȘДʈ',
                            'ªВÜɆЛÖԫ\x88 ԆɈԕƎÜȱӥȕΦϬǌԠUƍ˝ȴȉҭÊưӞ',
                            'ɜϖΦĦǀƇ;ÉͲЎÅƟ`ԃ¾ƝэPʲƃӢĎςҫζĽĶψEά',
                            'βǀÏˢŚԊưłÿԐʻѻƱƬȨ҂ŻδӯΓКл˄ĔǟťӇƟäӲ',
                            'ϤƫзѳЎžΕȕҩʓȺΪΒ˳ȉ˪Hòсʆ[ɯ«è˷Ү˻϶ВȂ',
                            'HaŦӟғ\x92Ƹҏ9Уҳ϶п˭ӽɘӂҌƍ¦јԀʖƢˑёԄ¾|ʙ',
                            'îsŦҰčȑɳɀʰȢӘҵѱșΆϧȭˌ&ǒɈϯòIԍĩYŹбɦ',
                        ],
                    'licenses': [
                            'þϝ<Μ¨ɍȠ҉6ѶʗošӤɶƫýŊĵͶ҅\x84²˟ΖǨŦΘ˨Ď',
                            'ɞê»\x9eЄεńƙQΧϸӶɑТǬѩѻˌˍźƇӛΡȣ¸1ΨÕŹȹ',
                            'ђӥĿ˂ԕǪˮɶϺӥʈѻÔƠЍ',
                            'ȌǁϚʱДϳ¼ρˊȆɪǍǦєΛΦȣбҦ˲Ԛр\u0379ԏˊΑŬқҡѯ',
                            'ӛĢP»^ƝŮƜА҇Ұ\x89ҺcӂɔþțϩĺΝӛȍōȆӜʛȗ˽ȹ',
                            'ǗȦªƼLіƐŤĝҋԜȍ¡pІtѣĉϤǣϢѕ҅υӪͶ˻ØʵŶ',
                            'ú¢;ò÷\u038döԑ.·ӑ¹˳¢ƁԎĩ9ÝǙɤӍԚʥʡϕ\u0380ʯuǩ',
                            'Єʰш˺ТŃLͱʽîԘԭ\u0383В\x81ɑɹǳ»ưˁȦɐӯѤʁʖԆ ʀ',
                            'ɧԂŵ',
                            'ҀɴĪŧƼƉâƌԫǜòǷ8Ɇ˺ѨɞћЖͶ\x90\x81ƲĐªθÒҕʇȼ',
                        ],
                },
                {
                    'name': 'ȼ\x82˜ϻ¢',
                    'version': [
                            -5980323427322331293,
                            -5430204571960457270,
                            -8671988933701371207,
                        ],
                    'about': 'ǐ\x83ȪȗЄαўʹɥӌ~İĝîɚĢÈʑːĉØйǹșʟÅB6˪:',
                    'description': 'ɊƥϥѵʱɾҾЈҤʵē|\x84¼ƃԪБ˔ϺӻVãƦɪʉϩФŦŝѦ',
                    'authors': [
                            'ɎͽԞЀҩǒªɠϋĐǶ\x88ˏЫùÊҦӠǠӝѰвҶ\x9dǴʾʂǃўʶ',
                            'ßȵМųáҘd¢ŔƍȀȅϫψϡÆųөǵϳӢɪǑЩԝɕŚҒŶЇ',
                            'ɵ˛¹ƿʣТúΙɓтŚͺ҅яҀӰϾŮʁѿ\x8fѮʴɅ\x85ЧʱȀͳ¸',
                            'żˉ:ʩɯm}ŀȞ˚ԠыΙ¸ƴԤКŮΥMˁ÷Ӣʟp\u0383±ĥzĂ',
                            'ԥʰăƢƠЗή˒ˈĖаϥúϳƷЗЩɆЊìɌˆǇĸ`i˟ʔCM',
                            'ѕ-ɜɱҗ˯ΆϾЁƂʍшȖ\u0381Ͼ¼ËŰéŨΣ˪æӨÌ',
                            'ϼҲȾҤѴȈɗғ\x8b˾Ňþ:ѴʿӕԔĀяԥıӋΟӹ\x88ƃҹӺω˺',
                            'Ӏė`ȐƚБцɝÐĿ\u03a2ͰƥțÕĊȇѫʿѸ\x8eѶɎìΒȜмЀɺƯ',
                            'ǓĦȌĀυǚ҄ˌĖΙȭɳƩҬξφШ·ȃΨɚͳĀͻ5щġѦϬÏ',
                            'űȿƒ\x7fʞëɜѱԠʈѐʙӖъđȲ\x7fÇУɗˎǝӌҐƩЫЙҵ+ӄ',
                        ],
                    'licenses': [
                            "џªñƸ<ЮċПˣȶϮƃԭЌǰŌ'ӑʤωϣΐϹȶЭϰҡΈӟй",
                            'õԂΏǴ/êҤӮӵΈĨԢФzśҬʊĤоƹȞîεԈ˹ЊƉs˟Ē',
                            'ңƓ\x82ϨƅωĪÁŅȅңι˂\\QαƊӉ˃tĔ\x9bʎèΨƐТŷĢ\x99',
                            'ǒϞЙʝʈQɌѯá0ʹůHΚ҄Ȩśн\x8fϽ¾ǊпƎȅљӏɗ\u0383ԇ',
                            'Ж\xa0\x87ǤȘ\u0378ǚι\x8fКȰɡżƓѻςöӇ9ԕɢˋɶЦ\u0379϶ĭϔѥѸ',
                            'Ӣ\x8bǭĀ˥Ёì˕öцʟԏɣΝʙԠÄεȓĳԉȊџűĆnӕŜõʚ',
                            'Ҷ!ʼ',
                            'ƽȴӝя\x89 íӭγӜƂřҰǚφӪӛʏūӬŇΕѼҎǁ@ԝƿϼˮ',
                            "ƒeűΣПƹůΝ'ɟшƙәÒӘʍƥл¡ɋÐƷϬϪľŝwǞːĨ",
                        ],
                },
                {
                    'name': 'ˠŹҋɬĽψďpǴÂĕđϒÞ˞bPŨԇʴǷƑΊȆҎƀηƕÂT',
                    'version': [
                            -4363537445650955511,
                            -4093245684459742356,
                            -3089446686129429537,
                        ],
                    'about': 'ȩεǰӬ?ΡƂʏЎу\x8fˈϮ\xadЫĆȥ˟ŕЎˎŵĿȫƮϑɟ0dԣ',
                    'description': '\u038bȴù\x9eѰӯԈȄȤȓŌˣĴˡЫżĦƨˈѱ@ͼƽəїњ¿ӉѮɗ',
                    'authors': [
                            'BÒϘʇĒѤѵdοɈřɟÞǰÛȃȐĳÎ˂¿ƏҖЪӧγ±һϣĪ',
                            'Ҫ®ƨÁƘQӤԆoĿȌʙ\x80ҸȢһPŹԄŀҝԆʟ˔ͰӁƫƣ˔р',
                            'ĩ9ˠҜōĖͲīǑƟƸӹΆʔɧДԥƴˊɚŃʳģς˭șиǾԇ˲',
                            'ǦɒɃƶ˯о',
                            'ӡńѻȩԫƵ\x82\x85˻ãżÝΔƮ2ʈλDԉɐɹ˺-τΔɔǌ¡ȵɟ',
                            'ʫ˗ǱҀӎԩɒ¢ rώԞĮΊɇſÜҿЬӃҦѼƞǄ˼ůɟoˋǰ',
                            'ɟ˗Ұӟѱ¾өFӽϙӦѴƔÚĚοΦѺñ˦ɼĶЫƁȮИ\xa0ƸŐІ',
                            'ŃЃǚˋȶӈɺƿʤǼӸЙʌѓ˰ʹҌȆΜA¼ɻϐӇõɜ:Ӓ˭©',
                            'ƦəʹԠĪьӐƛɅȬďшļФąεόƤɏſ¶\x8bǲԣ\xa0ЬѸɍϩ:',
                            'ȅĈ#ϴҏΘaҭԗɖĪЃ_',
                        ],
                    'licenses': [
                            'ɡ\x97ʑÐƻϸҎã\x86ҩȱԍӊǁźҕûªëǓʥҩѶȇ˩κсÉÑЍ',
                            'ǨѵØϧѴͺ]˞ʗɗҋ˃Ԯ˭ԛ3˾Óļ˞ҘїϤɝjҫLԟ҂ϴ',
                            "ĸȑsΛǣÅНʹЀȃǬѡŎǌй˫Ǥ>ѢʽЂɁοԠ Ō\x9dѼÿ'",
                            'ŽÔǅϯȸũʯ²SϊǜοƮ³ƳďΈįЕЭуçǷοеɷкȢΆŎ',
                            'ԬдđŝϕҟГөǱ˦ϰħΗ¿ͳĪȚϱ\x88Ȕϕ\u0383ΪϴʅĹΚβƏа',
                            'ÕӝΗ*ɒʞшÔìӪĈҷŮ҄ϯ!0ˏϫʪƗΝŷƌҟӳˣǦѰ˙',
                        ],
                },
                {
                    'name': 'ҷЋ\x95ѵѻŨӘƘӘņȇԟлүӗ½;vɻԫŦΙ҅јўӝтˮӎύ',
                    'version': [
                            -548523401379346123,
                            -895511140537820645,
                            -1689815313248870103,
                        ],
                    'about': 'ҧȔɸºδѦʚѶƾҼȉÃďΡSĽūƺӋȝ˝Еʻʔǋeг%Ѷİ',
                    'description': 'ʿѕžɍӕʓ˯јӏȗϷȝψǮșɭѹыÇӞũơәĕçƆЩŸũϕ',
                    'authors': [
                            '0)',
                            'ʝ\x8dô\x9eșǢǭÂƶǺȇ²ʜù#Ȼ1Ѳ˺Ɇ"ʆүŤыΖԫƮСΏ',
                            'ОɰщӁ˂ԕǎʎȒΌ.\u0383 ΘøǦАȈѢʂΚӞϥϓoęѿĘ`m',
                            'ӂ)CѼȻƭʸ«¡җńчҭʾ΅\x7f§ÁϵoaµѹМ\x86Ľ?íƤe',
                            'ĨșҜDˤiϏ\x95˺ӔcȲ\x8eǂЪԚ_\x94ѧΔКɹƜǄԓʔӖОņȉ',
                            'ƷʗϕȒʢ3ǧ\\c$\u0382\x8aAˤԠѝƙƜԀϭ\u0382ˈςƐψʠфмɽԍ',
                            'xȥǏħ_ˈЊÂÖŽ{Ċ\x97ȃԙ}ҫŝĒɐˣϫǖɀнǆÄҴΌβ',
                            'ǯƜʹȇκԨЦˀϫYȭϮǏԦϴ±ѤeǏÙ˹ɱ\\\x81ЗӂÃ~ӗ˯',
                            'wʿϰ˫šҙıƄɢ¡ӑңӗĚъ~ƱϥɻѰɥěαʆһџƋɺĐĝ',
                            '˪˪ȃŲLşʥśZѾѓԎўȊѽˍƲǗΧƱzӸѮЮȷmѩҠȭҡ',
                        ],
                    'licenses': [
                            'ĮɥЪҁŪΏӖȚъԥfŲϋҋϩĉɂƐˌÛӸàʚƇ˅тƉök\x9c',
                            'ЙlưЛ®\x84ӟЗ¾ƍһ_ūĮНңöıҧȘŁ˦ҀʻӼʡʵ\x9dɲƇ',
                            'ГР2İʼН¶ÃÂȇ\x83űǉϢҢ\x94ԋřѕπӡЗśɰȋͿ˳ʄӃ\x82',
                            'ʚӧӓүМǿÃƛ~ǜˁŉƯĶ(ŠĜȜӞǻΤʲφӺɸёѢӉʞɝ',
                            'Ʋ¿ΑӡϸĻӅϠΡϒǍγeʶâȣδ¹ȤɣʬјǱҹĥÁĢƓȖ\x8b',
                            'ɪǮĢKƇŵ\x85ċÝƀΛȐ҉ƝϱϹ\x8dΆҨŏfԙƃɥϖȴŌNȵӴ',
                            'ȌͽӵķλӘϢџЛĴ\x82ˑϪǝYԁc+ӗȘǓϟľOXȨυˁɴԐ',
                            '£ĠƪρĹќϹ҅ǝǷЂŏ,ǢΞŻĘ¹ƍ˻ҤҬOŪƼ¤ѪюLŬ',
                        ],
                },
                {
                    'name': 'ѻɭȀĠѭҩǤȮƕŉÃϷЧ GɿР˰ęƩ˭ҘŐÒ&ɐСΞƇõ',
                    'version': [
                            -6923428929791852613,
                            -3159836808096475845,
                            -6734562766892460149,
                        ],
                    'about': 'ʔLđЫцIȒ£ξƶ\u038bӞmʻ|ӵЮϻƻуΒƤɵҤͱΊő˨Ɏ°',
                    'description': '\x93ưͻԁȎˌΨ×ҟ»ҠQЌЭǜӅΌ¤΄ÕдүӑĜ.ôñћ҈ȷ',
                    'authors': [
                            'ʳͷϐ~ǭ¶dƑѢɢϘǑӓƆԋӯήԨʕț¼Ͱ˫ĵҧӮϭҶӒԑ',
                            "\u0383ӛμЯ¯ƧʭŹϧÍѿҙԭŕӓĐУȊΟU';\u038dȰj\x9fʃ˥Ƽf",
                            'ӏԍφӥˢˈQʨҴОΰ\xa0ʍˊɼΨ\x90MȌˉӰöМΗЀ#Ϻт\x9f˅',
                            '¹Ɏȷ˩ǜЏӾɏť\xa0âԨϏÖЦϛŘң\x81ҺӦŰ;7ɥнӖāǘǿ',
                            'ɩÆҜХšϸĸĐȔƲҭƷӻΊԋ\x8aʔήȜĺƮ\x89ΊωΩU¯Ԏ\x89ü',
                            'ĜϾͻҕЛĬğƃҗaíƮÚǩǺ˰ǏRǽÈϙҗʬҽʁɘŨԛ\x9eӶ',
                            'ŲӾԓλ·ɀҽѢѳŌkŃϾřɓ\x8bÒӼ˲ԓȀͼӋʜϘԊϨÈɨǎ',
                            'ƫéδΐҰɊ˻ӁͳǏqӁϢƩƌɺʿͻϲœȮͺʤǭɐčј˜ȯϋ',
                            'ЅƺӫAӅҬ\u03a2ũôԓ˕җɈԗ҉ʽϭΓ¸ԊХ>ȀǓ°њ÷¬Љԝ',
                            'ԎʻŒϾ˸ȉ®ѣƢŘόsɭWϊ¥Ɯ<ӀԝϸϓŞђλʩӛԙȢň',
                        ],
                    'licenses': [
                            'ƄĔҩԊȉЖʻǇɈҸÄ˄ʹUȁ|Ψ\x89Н&ȫЭɛφ\u0380.ΞzҩϜ',
                            'ǠӃä҆ƷÝԊӃŊβƆþʅȽԓǘ"ʗģȮʶζԑʖĐWϡѭІ҈',
                            'jnÖŬŖώϻԍӀȹšĉКΘɳĉ҃ĭ\x9cȵƾΔхҾŻĢÂɬȖI',
                            'ȿÖƲÄ\x88ˍΗǺǉǦǵ\u0380ʻӄįԔʪĶѧƻЇѰȫʬƝĂąͺPв',
                        ],
                },
                {
                    'name': 'oŋÆ˛ШɢáǠҞÊÒϊǀ˪Ğ·МӋŸÎą\x83ŔƜŕʅěԣȼм',
                    'version': [
                            -4482820633171619602,
                            -7255651471837965850,
                            -8891742321018227687,
                        ],
                    'about': '\x8aS:ÉӤ\x88ϏŽϒȅ}ĀɯʺЧ\x9a½ҪÉоŮá˒ͿϠɝҞЍǵǗ',
                    'description': 'ĜĈ˾Ɗʲӱs͵iűҸ\x7f)ΟϟǸ҅Ͻ\x8bǉɩшɱГHñɷʶʱѝ',
                    'authors': [
                            'ɡ±ԕӜɼĢlͲˋæЋĕ!\x84ʒșΚӰȿ˖ǔѩĝШʝ\x9eɍĤѕȴ',
                            'ÈѸ\u038bĈ?Вʝ+҃ʺӛȪ\x979ŗǥѧƣҝˈˢŋϙέȸϜčτ<ʸ',
                            'AɄçӒˆĻϛ"ıĐђԞɋЈʒůѵӡɐԒȪƔҜƔύбƞ:ǱF',
                            '\x9eйŦʁϭӸӝȰ|їĲȀӏҙӠԒѠĽŖӽǂǊıʽˢϭԑʑɍ˹',
                            'ύμӞЩƻЂÈ˩ЙҕƕѣѮжòϙ¤ɉǘÐκǰlŚΑɩ\u038b¼ǽϟ',
                            'ɏƊļǧĔӍӔӲǪĆ:ҏΟɫѓƝȧ˶ȃÑϯ\x9bʃe-þΩЂìʑ',
                            'òр\u0379ҷ\x91İƘǨǵđөĉÞӤȚʈ͵ͽϦĠˮ\x92ǀɶ˻ϑ˹ʵќϡ',
                            'χìӬͽˆF\x80ěĭϖɾ\x8cҰΚǢұѳȑƝѺƏOʈȦǁ8ϴӰЙí',
                            'ԟĔѯåĠÅɪԓǝʙѭȒCÂјưʆŕȚɩҢ#Ų.ǔɚϛǘŞɰ',
                            'јȝĎʟǚ\x99ȿˍĩѡǅиϘҝÆϫ/D΅ŲȮāʽԋвʱХXӫϊ',
                        ],
                    'licenses': [
                            '˛ɀμêìɣąǐϗvƏźϑȱӦìĈĀɒéҩҫƯȦӱǴκХҍǄ',
                            'ƏXΓЙÿƜЃǪɃП ϷҰ]ɴҘюҕ˽Ѽ͵²ҢХΠҭĹʁ\x9cҖ',
                            'S˃ηѪ<қ˴\u0379Ï˥ѠȔ\\ȪǓӏϗГҫºЪʿԝӘˋɀˡΝǎ˂',
                            'ΝȚĖȍĕƉ\x80Ӯ ɦϼżÃϴƋ\x8fҕϯųΜŤüǯəƲ˙ǥʪ¤µ',
                            'ĘԐƛÕ˯ļʐŞ§΅ːԔЃͱȷњȕ˪˨ΎʍѮԟʑƑʊɳԔɬƃ',
                            "¶ϋуʃ_\x9b\x84'ϕӏɎĞł˖ǟŶŃ ȜвŘѤ҅ɮВǱ\x88ʎҴȶ",
                        ],
                },
                {
                    'name': 'ұ9ǿǧ˼ȸɉӬΏʨƋÚ¾\u03a2МЌѝˤɏƑʖ˷\x9fɅɭǴͷýÐ϶',
                    'version': [
                            -1107229017562011189,
                            -8663852240221172425,
                            -6371993797892907512,
                        ],
                    'about': 'ɽН\x82ϗҫЈҤӀξïӏҵƻ҅ġƀϷĢԅӸρĉ˒ϩɽnѰйϓѓ',
                    'description': 'Ƈ±ãήWơɓƪEȭŕǼƴӷūƺǄѢkƳѿБȿɔĐ\x8bϢÿƦ×',
                    'authors': [
                            "CЫ\u0382ǐǭɀƭľтΈЭАưĀΛцƧǴ\x88˜ùưͽʥ'ѪӽɡȚӱ",
                            ':ΒǕЎǁȐΔƻʜђď˶@Ȃɿаҫҵ\xad/ӵԋΟc',
                            'сìǇ\x94ŶδҗʫÂѦԝãмӄƹȕLâù˔çX¿;ƅӛ\u0383ϼCԑ',
                            'ƭˣԜ\xadǰkӪ϶ѯͳӍԏĤԦӕȊѢʿå˩ɁѱІϐǡ-ƁЅѲʺ',
                            'ϋӕŽ\u038dэ£ХîƖ.ӠҶПӑҝ˕љȵУ_рμĤƠЏ˭bž˛\x8a',
                            'ӄˆ\u0380Ùȏ\x80ӎΐʘŝº¦ӻʱԦ\x88Ơ9ӓsήź}ŢɸЭüȿ½ʯ',
                            'ƲӯύHʂȧJɛѩԨчίȞɁŲřςρϰŎҿЃ˔z@ăxΩǡ\x93',
                            'ϛЭѓĮѬηмԠΡϺґϚˀűǀ"ŚĐЅŲʧ˧Ӛ÷ёǠƩȉΣ"',
                            'ԖεӑêñĞυɒѫǼĸӡʫӝӞǰʧҢɚĀ)ŚʍƄđǤʪѺĐH',
                            'ƘUŊſΣ\u03a2ΉЖѪ0ë˃ʬɪ.ǰЛҚԒĔңґӳѥϜʀ îӋ˘',
                        ],
                    'licenses': [
                            'ȼ˅МǽАҜ˹ΉςËƐΓĚºҳԮԏΨŚϪŖòǣǏɄ_Pj¾ǎ',
                        ],
                },
                {
                    'name': 'ʋˉúʼѢƠҢԪȪԇ',
                    'version': [
                            -8710094331014106659,
                            -6696774478470434243,
                            -2166247807196416713,
                        ],
                    'about': 'ӄ҂ɘªƼȞѸұǩȽ!\x9bѷқЃGŘК+ԁȝƻԡҴŶгηЖʀѠ',
                    'description': 'ҡˤʕӹhɌͺҍΘԗȜȧТ(ƼҚ|FԢљХŏēӅ-ɧ¢˘EӐ',
                    'authors': [
                            '\x8eќҳeŹʤμϏȋρ\xadȨǎѬΖ˙ԪϮˣρɰǣĜsȰjŀGΗʺ',
                            '`ӛӊƛΪ϶ԚɺǵɋÁèɁwΓӇʮƖ!\u038b¾ɮûĀŐΔ\x8fş\x9bu',
                            'ƝԓǏˈÀÜ˚ʇÎɂIλ?ºŸʺĖ×˕ŇÈʭȒӱѠˠ˧,Юʳ',
                            'õŲҸˏegӗȐӦ˅ԑϺ èƲĘġѐαIƸƏǸƁХΡʆΙƚӌ',
                            'ϖʨЬˋa\x98ɨԞΰ8Ȱƒɡаgʧ˶Ƙ˲ĸϬԥÿϭƾ¶Ӟ$˻Ώ',
                            'ɖ˂˴á-ѳғÍҀϣʱŸˑ\u0383ÈĨНϱ(\xa0ʼΟǍѸ˭ҧͲʜǴӿ',
                            'ʕƼʗϩģɺjԞ§rńЊɭҘҫȢ¨ǐõѠQʣŇӇҢțʘˍѕÚ',
                            'ϷȦ\x82ԤѺRĬœѿʆ˴\x87ƸǠ7ǤƞȠyθªҙʚϖ˽ůǭ˲ҋÃ',
                            'ȎӔ˕ľǹŬ!đźҠҋʖӇxЦȬ²AĹq˱ЃóˣBϺψȌȍ\x8a',
                            'fҌѕʾӫÞьȟк˞\x99ӐΕȳШ8ϸʨҧɸ~ŇψưʹκѥԐ¬Ƹ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'Ű\x88ϣˤˁʋȄгȣςԈ\x8aҽѩ¯ȹѝƥ*ӌĭǰJԗϡгΈȔéʊ',
                    'version': [
                            -6110206851158387016,
                            -2035767210892282487,
                            -1539968385675337843,
                        ],
                    'about': 'íͰƎәȌˮđ"ЅĦЊѬʄǥǞŨ\x88Ғ·ԘOˁ˞ʚѯ҃Ⱦȉɫǝ',
                    'description': 'ӾļʥрºГÍɐȚȮǤsѴӝɖjϳÍŖƬ\x8fǍɓӏīν˅ļΰ˹',
                    'authors': [
                            'Ƚī҃ªĲγȭЗôèď\u0378ĦсΛȂƐԋǂȒϨīǡÍˇѶũ\x9dȴÒ',
                            'ӄӗɸųԇ·ǟċ\xadáˈĽңVΰ\xadȨÈ+˄ȁ˦ӭUӬȝϖžɂЫ',
                            'ʄėӂβѼҤԑҼ˳ӺǭɊ\x94ѨÅɘд´ӵ\x8a҆ʀïǩþĀʦҵϠΤ',
                            "ɆϜǱ˕ѲƜƢІԫËвʗʏӣ¶\u0383əЩ-ʃƦ{ʝɏ'ιƁØ^Ȉ",
                            'ѓΏ\x83қ¾˹ßͰ',
                            'ſӅξƀ°ĄþʕɁСҊȳѳԊɘÆɄұьΡnɉ\u0383ƆɺȺ˽Юӏό',
                            '˦ƃɦƲĽԈsΔGƼáɝȨ\x9eԛȦѩРƚПp=ʘʦȄǚɁςтП',
                            'ıȯ½ϘȚuxƋ˪ʖΕǷkɲȉӄȍoǡƕɘƉǝQѱˎëτӓǚ',
                            'ьлȚұЁǚԍӘķɾԭ·ʿ͵҇ƥȋɹǅβӪϧӡŻăǦ',
                            'ǏəɨƀĆƬɹ΄В\x9eђWƑԓΉШɭǂʷàԇ\x80ſëȿӠɃ;ɰ[',
                        ],
                    'licenses': [
                            'ϾΙԚӪÍj2ΪūӦԬёäӊŽԠѼ\x82Äƍ-ӼʆɩʟҀˠ{ћȗ',
                            'ӝɜIƽŶ˅ÀΨў\x93ǻЮӋȔ(˚ϤιɝPˇ¢ƫDРΏӍԭǖ¬',
                            'ƣѡǺϱƅƒ҇Ѝ¸ưɦőҗӏBǮӚ\x85³ʋþÂђyҁоқǨȪʦ',
                            'ŊҏĬ:ǖƛӣʿɼќȶȥǣ˺Ά²ϵŨǍ\x9aтԔĀÊƩԂ˧Сʨή',
                            'ÖСΠѭЁ˙ӺǤǨһžɯχѩʚƞч¹PƑȴмÚħҭĆUӄǠГ',
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
                    'name': 'Ąŗ\x99',
                    'version': [
                            -516165713959244329,
                            -5879578485985851339,
                            -1457673725784102642,
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
