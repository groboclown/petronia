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
            'mime_type': 'Àɱӆɨ҄ʄȨӰżԐȥӏңϝџԟyˤʎĴɽˬȎѺњǨʬЗγ|',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'mime_type': '»ȞŻ',

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
            '$': 'ÔûϻɮМɅȽҔwԑϔҘԥȋ\x8cќ˼ҙƸɁ\u0378\x99ӞďŜ\x94ȆȌѽȵ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4360411653021428151,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 879629.3216203911,
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
            '$': '20220522:172827.898855:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ɠӬUʣѸ ˽ŁϨēʩĠļĖшʨvŪîÈȉ\\ʷɊͺӜȦԏԊѼ',
                '´λңʐӅ҉ШЏϕŢ¸уԜԑҴǢҀɷɐйƅ%ЋÔʘӉҟĕΣҞ',
                'ǳȩРԗ8ϒϻʠVȏȥЩɈ"΄ФȀ9ƽӬƪ˖Ԛɬ¯řϻʇϛ\x84',
                'ԈkJÝΰдăѝξϞȁƫɪӧHɼǼʕ˓ЩøӺʴȾӍи\x9cɃӎĭ',
                'ǟѷ»ЁЅ\x81Ɯ\x89ΏʙʼCƴŬ˴¿įÏψUβԋϽÂĒĄƵĮĮɩ',
                'йӋиɇ ɑǦѳҘԃɑĜƇòѱѲ˔ʆʴԣũȥъʼoçŏѷȄ\u0382',
                'ҞƐΝѲġЬЏɱǾϝ˝Ǖļēˌ˚ʚJǤːȘӮˣƈϬ˗ɾϨηŤ',
                'ĖĴΣǐɯӉŠƫϸɓˊѰϔìſˀʖ\x8b\u0383ЉO;rНЭÉѭͳ\x93Ɠ',
                'ÅƓȿɇLѝЏİʻğǜҬe´ӠâӼǣƐҞəÍ°ҭıÝȧȆĝӾ',
                'ƩƒǶНϭʵ´ɍЭ{ÝĿуχƬӠǼŁʎҩȪ+ÊƐ°ēѷǈчʆ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -1319447729798913726,
                -974095893004523974,
                139498872217422998,
                8742786843272840364,
                -1047020628049893952,
                -8936333456721046964,
                3190389432423478115,
                -3998940779494234005,
                1115143389961629187,
                -3353570620419501514,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                743393.97297531,
                845301.6557144588,
                537340.7713777596,
                895004.4315980681,
                48132.07702692479,
                430777.1204345267,
                254193.62916551653,
                857430.178830584,
                -39033.47294780196,
                667236.1291013327,
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
                True,
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
                '20220522:172828.372784:+0000',
                '20220522:172828.381983:+0000',
                '20220522:172828.391291:+0000',
                '20220522:172828.400896:+0000',
                '20220522:172828.409794:+0000',
                '20220522:172828.418583:+0000',
                '20220522:172828.427625:+0000',
                '20220522:172828.435362:+0000',
                '20220522:172828.443713:+0000',
                '20220522:172828.451476:+0000',
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
            'name': 'Ɵ҉ЁŒɋԤͳӑȫ÷ɶşРF\x83ӵŭðʵhϖȑůԪǦŋϝĭͱɇ',
            'value': {
                '^': 'float_list',
                '$': [
                    594388.9366161687,
                    262628.24746578076,
                    194936.79522522166,
                    529795.9390548959,
                    -26135.610964765452,
                    912869.6328643763,
                    392232.4417878788,
                    46512.91348377953,
                    258929.399529439,
                    255616.30766728614,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ԅ',

            'value': {
                '^': 'datetime',
                '$': '20220522:172827.783024:+0000',
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
            'catalog': 'ʺ϶ϐΛĝÔҗŲĔҴťКãʹԙʣћɅdȯūвVȺȟŌϜ˾ϷǄ',
            'message': 'Ǯɡȟ]ŀԂíоϟ˴ҋӀŧA¥»_Žȥʻ˰ϨԊϑΟůȜъÔǜ',
            'arguments': [
                {
                    'name': '˓īӧӎ҈ψǖƆ\u038bӞɄƱșǪӈЄ¡ŽɫȲԨƾ±ќʝEÐщʬȩ',
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
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ϼčЭʲɤϧñɴƚяƷԌϸˡԨФƨΖӥøūԈТƪʖȰƷ·ɗƓ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        True,
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
                {
                    'name': 'ƕ',
                    'value': {
                            '^': 'float',
                            '$': 750154.0844115388,
                        },
                },
                {
                    'name': '˞ԧƫҖwǅΤŀӺę˃ÐҚòŴИȬ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -53472.385757830365,
                                        -59911.664594006805,
                                        646186.3244379355,
                                        759778.912964033,
                                        850371.5145951128,
                                        -76367.68371039521,
                                        646062.0118741253,
                                        -42520.35152609338,
                                        627996.5698977265,
                                        215344.61948749452,
                                    ],
                        },
                },
                {
                    'name': 'ʭ7Ǔњюк¡Ķ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Ў',
                    'value': {
                            '^': 'float',
                            '$': 659522.0984726951,
                        },
                },
                {
                    'name': 'ϚӹƂȫϊÞ+ǸѤɿ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        False,
                                        False,
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
                    'name': 'ƇÈϫԋƯ÷ˁ˳ͽʚǥʤőʘӜԊѳȡҭ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ЅĢƁȯθĭĎ¥ǺċЈқˣυ\x8aɴ˳Ҁʄ<ԟЮ\x9cmԔȆ(C¿ő',
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
                    'name': 'i',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'śɽɴÌʫСʡƞҧӠʶǬƋɡ8ӱҪѼ\x89\u0383҇ʅôɣүҼñʅηƏ',
                                        ';ɢƀŲ˨\x8aƐƸȼûȕϷшӻǳљΌӮ˘҇ƛΏȞşʐ˂ɧÌԏ˷',
                                        'ǠϤїΛ"șŝJИχ˯}˽ҢOéņȍѪҲɇĕħ˚ĔƉԔǾѫǍ',
                                        '҂ŧΉѬćԭ\u0380ʦНӟĳ˩ҴҿYӤĆǔíԅī¤ƱеǴˁćΖӉɺ',
                                        'ûϒĮɌ˭ρѮ\u0379˙ѡΖϖWѥȘɫȺ\x7føĠʛҜʹmɢœɅЭĵȄ',
                                        'ɍŰӋ˵ĂǣŸѭЂ\x89ιêΒΔơǯȗψЅĨʛөȚӧѬҙ\x94˒Ӿʟ',
                                        'Цȵѣī¹"ԚɀǸSĄԩÌƒŪκӟΈέφіţũԪͻʿØϒì\xad',
                                        'үӡӼʉŢԅ;ɢѳțŋǄǞư÷Еӟóϸ/ĸưăʘӒȐđFȬȻ',
                                        'ƸǬӈɐʶʖ1ҬӀѥӌ?ґϝȌÒεìҹƜʛґƐэϬғҴȌȗŦ',
                                        'Ǒӑʹҟŷ˓ΌxΎƷԁǲˠÑǹͱę|Ѵѩ²ԘӾʈЋАҺɌԕȘ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ˣӸ',

            'message': 'w',

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
                'catalog': 'lҚUӛʏάМпÅȽśÍϨ\x92ӶљQѭɸÿſΩĕΠоїɑԗêҶ',
                'message': 'ǞǪ\x86΄҅Ζ˚ȕȧѼ"ɧѡƴǘσȂԔS]˽ʁϽŕM%ǌˠÏŔ',
                'arguments': [
                    {
                            'name': 'ɌӓҎοҜƞP',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ΛÈê˨řșĽɺҨԝѡϐҼӱϧӽМȻûʼϱĜΟŢǠƎϮ˟ҤБ',
                            'value': {
                                        '^': 'int',
                                        '$': -2912832210602194052,
                                    },
                        },
                    {
                            'name': 'ŀԄѴ˂ǛԃʸнŞǔʉҟ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220522:172826.409838:+0000',
                                    },
                        },
                    {
                            'name': 'ÊϡƧЗ҈ͱʞΑЯ@ͻһºʞȼʂƚĵʄҕӺɼ҈ΆȻ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220522:172826.444242:+0000',
                                    },
                        },
                    {
                            'name': 'Ҥŕϐ<Ҁϙǵƿ˹˲ǲώƄϯȥɒɄѲɋqɴoȫйĐ\x9có',
                            'value': {
                                        '^': 'string',
                                        '$': 'b\x94ïƢɗ¢ȺɈȳƭRʘͶΖ6ȷҭѫӓ0ʊƀ×γǎơªѩύʶ',
                                    },
                        },
                    {
                            'name': 'SŊÐưϗО',
                            'value': {
                                        '^': 'string',
                                        '$': 'ϟӶ˛ҔӭЪƚʬҖĨǝȂɍКȦЭɬԔNǒɗ¦ȉŀ\u03a2ԞǅĶƊё',
                                    },
                        },
                    {
                            'name': 'ЬԑԛŀьҰτњ\u0383ȺȘÒҭԦƹÂʀԝ\x99uƤ<YƻʻȘƺ£·˩',
                            'value': {
                                        '^': 'string',
                                        '$': 'Ϡĺzԫȝ҅ύǏӢũϺYʸȊɦĤрΩȚƯҭгӎ^ȵžŧ]ɮu',
                                    },
                        },
                    {
                            'name': '˔ͲǒϱʶO6ШҊ˨ԨӗˌӓσȩΩΧǗӗȍϘŮѬЌТΎѓԥϞ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ɣϜ˙ɜʛҝϳʺѬƨҷƞѿǑыҗҗƭːΆɴʰ˖ʷȹ\x8cĒнɽĒ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ӱôƥɿΜļϴ#',
                            'value': {
                                        '^': 'float',
                                        '$': 493464.0686401883,
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
                'catalog': '3á',
                'message': 'λ',
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
            'store_id': 'з˽ɿȇƘʸѼ˜ȯǆϒƔԅҹСӰ!RʶЌ\x89[ҽŰh©ǒŧÖƿ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': '\x87ͿÞԃɭ',

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
            'mime_type': 'ĥȂǰюːǬӺ˙юԧԔ\x9eɗӺԤӚљϼËȈ®ҀʣǞһѬ\x9fφαǫ',
            'sha256': 'ѢʷԢœȧƵPƋÍŸϐɋĒɠϳǜзÅȊҼƙ7\x7fԘŁʇђŠ°ЕΘĀоʿŊєɰǣȯо9ǭ\u0380ý½ʇɦҍįԌѵĺ\x9cӻЇƶηӥɂʟϧ˂ɤӥ',
            'size': -3277001413368590768,
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
            'store_id': 'ԔҷҿɴӄӊƴʒϋŰɊώQŤfăϳʔÌyҌ˜ҔҶ÷ɟš´N\x9c',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'Ƌ҃ʙͻӼ',

        },
    ),
]
