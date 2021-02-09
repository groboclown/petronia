# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-08T21:23:24.527974

"""
Tests for the logging module.
Extension petronia.core.api.logging, Version 1.0.0
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
            '$': 'ѕғ˱ƃϸˀåўԮӃǑӟҷžʕѥǸɱʥҾНӍÿ¢҄ăǨqӚÛ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1742927561538369879,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 762113.4630463448,
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
            '$': '20210208:212324.427817:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ɡıč;ρP\u038dƄȢıѯχɜÔłíԡȲʝӏĜӎȌzɝԌĶϼ\x85ˌ',
                '˺йϭÐѴ*ǒѷĪӳϩaˋԦˤϐ7\u0381ʝҮΠг*ĄЪɬЯόɒŒ',
                'ʨЙȭӢėҬƀàǓűɄʲĜɀϽҎʟȮ²ɌȹrіӜұҘ\x85ɪΏɡ',
                '3ŲȖˍӹ\x82ҤƌŭΞ˚ũsͽȗ\x93ԕăƧǗǓˣьlӅʌőɡƲŲ',
                'ʦ҅Ĝ¼Ͽɭ9ҘǵǥӴ˵ҷήzʕαΉπʑȦкјϨüɹōǺ\x9bʷ',
                'ʛĸťˣӀǶǛƗńĪEŷβӈҭýɢџʲȐԈŮ҃ǸВÍ)Ǎ҂Ч',
                'ĦÎĞТ\x82ʃ×ƭԆVӬýҞͺˢΊҿцǆѹӨҫѪƶӄĭѦ˾ͷ÷',
                'кђ\xa0ÕˤǗȼɼӻӢƿãΏġλϫƄŵѤҌĐзҐΚ¼ÌɾΫȘ¶',
                'ȯN\u0382ǡ©ҍ˦\x9fӑŭVŸΜȓǺʹÌҨʴҜňīφĝχУºҽɾǉ',
                'ԝ\x9eГÍΐʂεD¤ɽǥnӓ»ѶήƍuæƩҧʟǜҽτɕιǁзt',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -4000775026070450695,
                8167589829936114644,
                -3894288242269809181,
                6789994656769441984,
                -2672440207362735204,
                -5048564714065963968,
                7792024170088984084,
                -2746307591149103887,
                8525114807324736646,
                -5918559200040261116,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                875306.3863500089,
                907653.5645580267,
                99101.75989024044,
                512925.83412925666,
                456969.3898861862,
                71447.9750055634,
                175507.36669945816,
                617357.8271226559,
                803055.745815889,
                575786.0143549537,
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
                False,
                True,
                True,
                False,
                True,
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
                '20210208:212324.428803:+0000',
                '20210208:212324.428814:+0000',
                '20210208:212324.428819:+0000',
                '20210208:212324.428824:+0000',
                '20210208:212324.428829:+0000',
                '20210208:212324.428834:+0000',
                '20210208:212324.428838:+0000',
                '20210208:212324.428843:+0000',
                '20210208:212324.428847:+0000',
                '20210208:212324.428852:+0000',
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
            'name': 'ǳεӸĹҖӁyЦӢĺȒɋǬcŚұʲɥƭĢǪoѸƕѸöĳϨȗа',
            'value': {
                '^': 'float_list',
                '$': [
                    387316.12867170497,
                    594028.5084931119,
                    798326.4017573375,
                    147103.01270029566,
                    568620.8240338865,
                    302489.8105024141,
                    127106.64293182621,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɜ',

            'value': {
                '^': 'datetime',
                '$': '20210208:212324.427161:+0000',
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
            'catalog': 'ʌÂ±ɭ˞ʷȞɤʶϒӾŗDɼʩЌăȂʍȈǄЩ,ƕƮʺλ_ˣȃ',
            'message': 'ĒůǄӬGI\x85ԑnϑ6ȽƩ\x8dɵɐϿƾñǥʎɽɆҬu[ȽKƦе',
            'arguments': [
                {
                    'name': 'ȝȲĳ˓ϊԛǙȣȵПɊ\x93ç¯І˭ӯјțҳÉ',
                    'value': {
                            '^': 'string',
                            '$': 'ӢуˉȰϟРӺԣ˓Α˺ϕăŗвӍQøЕʧşȘĘȵǀ˾ιĘŋŵ',
                        },
                },
                {
                    'name': 'θǨľɫ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ӀʩΊЖį\x8c#АɣӨԡ7ʲƵ˱ǡĕЂš˸ǡȢӛǫ',
                    'value': {
                            '^': 'int',
                            '$': 1645121111515052333,
                        },
                },
                {
                    'name': 'ǿͱђ˦ĀЀ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        671161.1747164459,
                                        733864.0157768746,
                                        997853.7130912489,
                                        953312.3336992578,
                                        333133.2587207377,
                                        452647.8021590812,
                                        682554.327816701,
                                        682423.0502952032,
                                        874485.468810062,
                                        60538.681537959696,
                                    ],
                        },
                },
                {
                    'name': 'ńǴЛʒʴˍ\x94=ʘ΄\x90\x94˟ҮȬcĬяФȣў\x84ɞΗԛȯȫҡȁɵ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ћʿɗļ϶\x83Ľйŧ´Ѓĕ\u038bþCЬͱŴҗΜΕáŎ˯Ԍϯɘɀϖʴ',
                                        'ӱԡѡÏƐ\x95ɱеɣҟФ΅gϞƨǂΨǌȔЦϚϳȄҦΐˎȂĳȫ\x82',
                                        '\u0379Ξ\x87ˡПˑȼҷŁӚЁęЗєίˡŋƟćԉƦԈèͳӃӇʡЭҫÞ',
                                        '\x9fӿɱřӦȾӶǨȹԋұϺ\x94@ςʅϛ˦ʂƿӌ6\u0383ΩҺҷяυɚљ',
                                        'ŔɤȭdGεӇήѝѼn˙ѢŀɽΏļm˒ԮӊťЍөӣϿöˣʓ³',
                                        'rӵ\x93;ɚåδˈġPԃƫÅύƜ°sҍҋΕͺϒƔŶɭ0īʷϠŗ',
                                        'ȶӤŋҚάђʲŽӠµȴűə¥ίƚĔС҂їԐџǼС˛сҺюʄȡ',
                                        'ŚҾμ×ƌʈζїʨŻї˹Ϯ\u0383mƆЏȣҪɄĪӗţžʨŖʨǗ \x92',
                                        '7љəeąΤ½äԘϘЖǛΛԨʛ\x97ɛ\x89ǬςǠӰЃɲȹÿɪæʊȐ',
                                        'ˢҺfҲɾϞˈĥϻӨƠƅĄƧүǼ˄ʻхðʏяԜҼӍýģôұи',
                                    ],
                        },
                },
                {
                    'name': 'ʱʊ˫HNRЦÕƮԢϔƃв',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210208:212324.425878:+0000',
                                        '20210208:212324.425892:+0000',
                                        '20210208:212324.425898:+0000',
                                        '20210208:212324.425904:+0000',
                                        '20210208:212324.425908:+0000',
                                        '20210208:212324.425913:+0000',
                                        '20210208:212324.425918:+0000',
                                        '20210208:212324.425923:+0000',
                                        '20210208:212324.425928:+0000',
                                        '20210208:212324.425935:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ȵɳ½ӂʇЁǌǂɱĬe\u038d\x87ȁŴέƕҬCџԮҁЋϏCƦͻϹ˧ʢ',
                    'value': {
                            '^': 'int',
                            '$': -3381519613059752799,
                        },
                },
                {
                    'name': 'ȕŁóǟ˚>nҍʒӇ˂ǍӾ²2ŀɥ˕õԙҍȵӻЎ\x98Ȑʚ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        63652.030037826305,
                                        700351.1359530807,
                                        617481.6626512781,
                                        587069.2789836855,
                                        33985.31156559568,
                                        464900.43305225053,
                                        271849.1462384579,
                                        -73614.5068746776,
                                        594827.4530236854,
                                        409582.7084744778,
                                    ],
                        },
                },
                {
                    'name': 'ɬН˕˶Ē',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '@ŘʥѸΖ§ЋϠ҂бѽȈȣɡ',
                    'value': {
                            '^': 'int',
                            '$': -8978670489326727592,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ɝѕ',

            'message': 'c',

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
            'scope': 'debug',
            'messages': [
                {
                    'catalog': 'ΞеǪ¯Ϭ',
                    'message': 'ȎǝƸѷɭɒǼÈɔ˼ѰҲҟşȋǯԠʲqȺϲŅДĚļѡҨыЉĐ',
                    'arguments': [
                            {
                                        'name': 'Ӥ\u0383ΫӸӿε\x9cǠхˊ˄˰ŗсғɜƱɏ˦άӴΊϣǆJύȶȦʒ%',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'І',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʉНφƐфͲƍѢφɃʝÐүǩȻŎħͺõͽŴБƙSĲMԮӲ҅Ӂ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԩ\x8bԈӂϹѠÐăͻǒғϢĩɝŮчƶѿӲʤНÂðǵӍӌЙЭȖ{',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 253214.157636168,
                                                    },
                                    },
                            {
                                        'name': 'ǔŻЫI',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            402488.3213918096,
                                                                            369989.10952134384,
                                                                            287034.7462727728,
                                                                            372554.94577635126,
                                                                            764215.0872433205,
                                                                            285244.0487323791,
                                                                            -1063.8691243099747,
                                                                            819802.1309831793,
                                                                            89446.3256359947,
                                                                            32372.6701171381,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '%ñĩ\x82ԜǰϴӨəƽҢΪüƇƜĖŮΐӼ$ƞ\x82ƨщΡȸӷ1·ѽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.399423:+0000',
                                                                            '20210208:212324.399455:+0000',
                                                                            '20210208:212324.399462:+0000',
                                                                            '20210208:212324.399467:+0000',
                                                                            '20210208:212324.399472:+0000',
                                                                            '20210208:212324.399477:+0000',
                                                                            '20210208:212324.399482:+0000',
                                                                            '20210208:212324.399486:+0000',
                                                                            '20210208:212324.399491:+0000',
                                                                            '20210208:212324.399496:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϐԙě3ϔΌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.399727:+0000',
                                                                            '20210208:212324.399739:+0000',
                                                                            '20210208:212324.399747:+0000',
                                                                            '20210208:212324.399753:+0000',
                                                                            '20210208:212324.399758:+0000',
                                                                            '20210208:212324.399763:+0000',
                                                                            '20210208:212324.399769:+0000',
                                                                            '20210208:212324.399774:+0000',
                                                                            '20210208:212324.399779:+0000',
                                                                            '20210208:212324.399785:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƌԓгĉʮgғΔӛгƪɩѲȄ˝џǰñҡѫ[ǕǬҒʑŀȟ\x9aŴЋ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            782566.9513417853,
                                                                            734741.4448074907,
                                                                            834261.2220896662,
                                                                            61703.77344093984,
                                                                            41173.1369232205,
                                                                            128791.66109150162,
                                                                            194647.2447572499,
                                                                            281385.37569060025,
                                                                            216470.58983145998,
                                                                            257458.34658737585,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϧӄğ^ɗϞƕƓɲɗĜǈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 918323.2313830361,
                                                    },
                                    },
                            {
                                        'name': 'ɵљb',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -14762076590105158,
                                                                            -1517610014945101039,
                                                                            6954058195713469637,
                                                                            8261009974112223585,
                                                                            -1567656781769338695,
                                                                            7613230242271757279,
                                                                            -5212658091819115528,
                                                                            2124741648428431176,
                                                                            5805427822375246272,
                                                                            -2337782624022492459,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ԋɘ\x9bųĻҾөĭЙҼԓxŦǞϤȤʂʼ'ZǈǦϟ9ӏӎӱӟɓȔ",
                    'message': 'ҍȶʴÉō΄ԇԤǾӘҶԭſӉ˛Ȝɟ˭ðΤͲ˂ΪӐpҬѺś±ʡ',
                    'arguments': [
                            {
                                        'name': 'ӾĒϦӬȓʶПԇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.401004:+0000',
                                                    },
                                    },
                            {
                                        'name': 'щzѥԑǀϭT¢ӒΛɫvÝ_',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'иώϰԍĜìiѡÙàҀʡĕƻҿÞ)˗Л\u0379Ӂ`ԆFҝÌЪFҕŧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            376032.93660276325,
                                                                            209949.9861314682,
                                                                            436891.8299921502,
                                                                            628633.2434296286,
                                                                            874836.5590506026,
                                                                            149627.46720374006,
                                                                            357093.8623106782,
                                                                            529315.9295630805,
                                                                            756411.3180159674,
                                                                            329205.66939241695,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԠҸȼΟȩ҄ҒǓɁаͻԇԍŏïĈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            449738.6131603427,
                                                                            879723.6583460373,
                                                                            466545.36330217554,
                                                                            201590.10230294097,
                                                                            378222.44395573164,
                                                                            474331.88992516,
                                                                            291193.8435275402,
                                                                            407376.403008983,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ů+ηͿƥǣӔғǵƃ˖ˮƣԎЇεӖŒ«ӅʡȇҼͶ:ûŧƁ\xad',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.401774:+0000',
                                                                            '20210208:212324.401784:+0000',
                                                                            '20210208:212324.401790:+0000',
                                                                            '20210208:212324.401795:+0000',
                                                                            '20210208:212324.401800:+0000',
                                                                            '20210208:212324.401805:+0000',
                                                                            '20210208:212324.401810:+0000',
                                                                            '20210208:212324.401815:+0000',
                                                                            '20210208:212324.401819:+0000',
                                                                            '20210208:212324.401824:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÍǟхπҎɒЂԙʘѓgҫÒȕџĞǓÜ\u0383Ӄ˧ɡϟɡĢgАɎwԍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            695252.7100374893,
                                                                            246691.40341485833,
                                                                            -98699.83018312306,
                                                                            430396.49909067363,
                                                                            290641.2655487759,
                                                                            798640.7859954997,
                                                                            458081.9871991259,
                                                                            979704.2602366102,
                                                                            984846.7421524136,
                                                                            865424.4206465211,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x86Κ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            709428.909038671,
                                                                            101259.79171142695,
                                                                            342200.536599891,
                                                                            693247.5474519299,
                                                                            827803.9346433936,
                                                                            350505.92507707706,
                                                                            959329.6107255484,
                                                                            545994.7964248362,
                                                                            881614.879663858,
                                                                            846933.2147818229,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǒҁ^Ԩƈǰƨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɵΐŋљɖȆ_ʖьӌқɥɄǇοɃŃàҒgΆŞɭԠrɹСǞ×γ',
                                                                            'ʌʆ\x91Ҧβўʟ®ӾԡƺвЦŰñPÔ+ÁŊҘԀçƮϓəвʍΩβ',
                                                                            'ͶȂ+RҶjʽĻ¡ˮȟϼϰγӻҮWѷШʂǜŻiɿӽϠK¦Ɵǫ',
                                                                            'γ\u038dęĎå\x87ƎԎҦˁſψȺɛʌ!Ćŭ¬ˣ2ԬϙͻĐĹȽˎΝǒ',
                                                                            'сҷăaȤκΈȾʣ¡ɸ4ĂÀÝŴĬϔӨӇƂɠԓʀ\x7fԓҨπГԥ',
                                                                            'ΣЁQϖxЋϕ)ʳ˥ǔѽŵƟЭ¬ˡЅЦԚğώϚӯʥȈ\x99ӫЕ2',
                                                                            'ġԗ˅ËоUǳȉŊȫɇɃλŬʜɵ\x95cơųί˚ұѳѼқìž\x9cí',
                                                                            'ęʹ8҂Ŏȸ˘ŕõ\x99ÎʵǉȔĸʉ\\ͻȥǽ˨ѢэƺʉӨɓƵӞȨ',
                                                                            'ƔҜŢ\u038dВєҵӲȜȗԙĺЦl+ԛϺrĴdśƺ҇Ů\x86ōȴˡΣр',
                                                                            'Ϥǣʲ<ҋӇƼǦŶƊɶĮȚñɗԂĉ_/¤І҇˖ѝζÕĝюƄҶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '®ԩ\u038dYӯҲŢʈǷԧøʻňυƀϙҿι˛˔dB%ȸϓĉ҆ŰѢҔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.402961:+0000',
                                                                            '20210208:212324.402972:+0000',
                                                                            '20210208:212324.402977:+0000',
                                                                            '20210208:212324.402983:+0000',
                                                                            '20210208:212324.402987:+0000',
                                                                            '20210208:212324.402992:+0000',
                                                                            '20210208:212324.402997:+0000',
                                                                            '20210208:212324.403002:+0000',
                                                                            '20210208:212324.403007:+0000',
                                                                            '20210208:212324.403011:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˴ǘԧĹʆ¸ǝқͳλμ\x88;γԤō',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.403292:+0000',
                                                                            '20210208:212324.403304:+0000',
                                                                            '20210208:212324.403309:+0000',
                                                                            '20210208:212324.403314:+0000',
                                                                            '20210208:212324.403319:+0000',
                                                                            '20210208:212324.403324:+0000',
                                                                            '20210208:212324.403329:+0000',
                                                                            '20210208:212324.403334:+0000',
                                                                            '20210208:212324.403338:+0000',
                                                                            '20210208:212324.403343:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'όί҆Ѯęҗ¼Ƽıԭή1ԠȞХ^ǝXɈԛԜȷƫo\x83φVԈӣŖ',
                    'message': 'Ě¾ȰұʨαҍѦԠϿŜ\x86Ēчu˱ҭɚēҘϒѹ5ҝŐ§Чϓ\x93A',
                    'arguments': [
                            {
                                        'name': '\x81ΈѯѸʓєҮƩƭɹѩěÎȬ\x8aԅŝȂ\x82ɲɛʏŢӁÃǶ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'EС¸ċȒΈʹåйҪ·ϥҐȷΓǍ2οú}ώĽ˘ϛ¨ΑoŇȕž',
                                                    },
                                    },
                            {
                                        'name': 'ʽѺƎҒʥВȅΛӋȚ˺ěп',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 533760.9296471745,
                                                    },
                                    },
                            {
                                        'name': 'ʕƪм©ԥ˘š\x7fВN',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8406267178545593323,
                                                    },
                                    },
                            {
                                        'name': 'šʛƦǽǦǢRâћˈΌȀӭбӝхпФˈ\u038bԖ˼Ʈӎǜțӭǖώɷ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.404314:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ġɶ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.404441:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӈЖԇǕïƊЉȊƵΊ˩Ȍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '-vŖϊǺЄƠϽй\x8fƀŵčiИҕŸӚɽҹђÿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 635980.3299985654,
                                                    },
                                    },
                            {
                                        'name': 'ȘƝΗkÞPұɀǾϛɂɝԠ҇ɉǑ\x9fʓÎ¦ō˂ÉÛǸϖĴUˮΑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϸКɖDØщӰіɟωʇɂ¹˽ōςΔLßԇѩȡЮņ˯ϯěÚɣũ',
                                                                            'ĳˑ˘ѵкŠÓЋʗќѨȯĬϮƵΫ\x9frĦƇʒµрǆʢƯŎҎǠŁ',
                                                                            'ҺϚʼʽӏ҂ǐÑӰʖ\\ŷӨȿɄǼŤšƴƥȻ\x9eɂĺɻҹЫҹ\x8eȦ',
                                                                            '\x91Гӽʼ\x94γȳȪюɝɬΡ҂ϔԅºԥǳ\u0379ˑΖĆВǾ˪ЁҬ5Ҫч',
                                                                            'ͽЮźĶϤАӪŴѬÐșŤӒ҄ʙÂЅԫ\x8bɉǵ\x9aÎǫӍ2Ѕʽǆė',
                                                                            'ȬǘΥϋÕΰɄψǋSӝƫċƺƸΣќJͶѰ\x94ΛȌѰ˰ҿɱƜÃà',
                                                                            'VƗËɗ(ăĴćǢǸĝēǶĔGċƬŲМŋ\u0379\x94Ў5ŎȣűɇѡԤ',
                                                                            'úŜəѴήƔ϶ȂѫΫƝ\x8aГԭʝŏЮуɯͲӃȁ\x8e ƓѕΜӲċl',
                                                                            'ЯУ#ϬυŕɹƤΦӝϩƸÙŦşʼʊ\x8dӭɡǶӞǡ˻˼ÖơɅīƚ',
                                                                            'œұŲƈÑĀΧ˥ŨťɤΝԆƈНŊηԐӨĬʢǾ³ʓŒʦǒǷ£D',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'c}÷ψʹ\x80чˢȍǯѢʤʌɲǗͽţћҲűϔǸɖȞŴˡëӘϽ.',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԬȜǸӏϏӝæŔΪʭēÍϠȆІŁЂŢN˽Ɨƶě˼5ÈȖїϩ˱',
                                                    },
                                    },
                            {
                                        'name': 'ɵ\x8e«ɵİʕкԖĤŶҍĚʋɦύʼ˛ę\u0382ӁѽNӌҁȍˏԧЮӢo',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            570253.2325074611,
                                                                            572823.8155902694,
                                                                            382514.56072056404,
                                                                            900722.3051997819,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'јrˁϐӡ!ˬҜҝϝ\u0381rʹvͽ˚Żъ',
                    'message': 'ғ;çǫiæӌǀfh(ʿ{ΤȖԢĠΒǗ˥w\x87ɩξƦˤκϏ°ī',
                    'arguments': [
                            {
                                        'name': 'Ҍ©ʒhΑ҈ŝ˼aʱǋӰҜсɿѦ˵ҨiΊѺθűθȽȺѵ;˨ơ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 966871.9552585215,
                                                    },
                                    },
                            {
                                        'name': 'ǯѵӟӿʩφŊqTҊïʆƙΞʦŅǃƅÃM\x88ǬθƣΟɜўǃ˨Џ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӍƹҒǺaΔïĪΧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɫċĻƴҬԡăЧƘǧϬƴxғΌʑͳȢˎȎȑҾ΄ƮΘáƽŏ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ͼ6ąɀĩĈõșǻΆ_ƛĝƛγЌ\u0378ɴȨЌ~Ζ®ʈʰyЙ!',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.406678:+0000',
                                                    },
                                    },
                            {
                                        'name': '˪ЯϭЀӦʆ)ɐƫʎƋȣδÝƏȾËЧɘȵƈs¬ЈĂűĸŮċ4',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8231024602668551207,
                                                                            -3342676988195533489,
                                                                            7978952709975287009,
                                                                            7174281962421225262,
                                                                            -3653647789309691725,
                                                                            104658204845288579,
                                                                            -4823392505872502077,
                                                                            -5999307661351198139,
                                                                            5326016441685996823,
                                                                            6212977457495679199,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¹ÄŒˣǟӥԐίə҃ΐʄƭƃĮҋЧhNȮλҧˆșƊѬǄÿǒı',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1183554866499422299,
                                                                            3408868499077606619,
                                                                            -4248537626561280582,
                                                                            4648373817756611736,
                                                                            4610057728647396556,
                                                                            2056123053653362649,
                                                                            1511517748370260116,
                                                                            5200893259028505455,
                                                                            -5598736210743056533,
                                                                            -5985354877837353887,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʚ\x85ĮДʑɆћԪȌÃŮӯѺϾŊƺŶɳĉϻѝß˾ưʮůΒŞԌΐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƊĺΒӀыԐɈͲŇŚǀŻȏ¦и\x93ϧȆ\x87ɍöȶTnțӟŊί¥M',
                                                                            'ɥ"(ϦʉЪƚƕčīƜĕɈμӃўšѝüÅƋȼҙјȺƯƼӄԃă',
                                                                            'ФƢӦɖʳʛ˴ѫęŝЏ,ɌȐÑӥȖBȢ˝ɒӞͺȳȘːсГьʶ',
                                                                            'ʎĊĴʃȭύǢǲӟңΕzƧǌûȘȆФΈδ҃ù:ȺҴʀǡϧÈĂ',
                                                                            'ԦȼХʛņʗύɖφŔт\\ŻӏɋćʌɠҧüͳǊƱŘŞŪʶ¯ʿø',
                                                                            'ȈЭΦˡӖýĠҿԂÎαѤǮ]µГΛȎȲԙ$\u038dƃϫ¥ȄΪäiɌ',
                                                                            'ȂÐƌtǇʇǡǽΈ҂˪ӍÒāɊҟȉѱΡʌŻºɑʤ\x9dԥpǩӡʴ',
                                                                            'ӭƢϪƣx҅WӓԦѕňǉӜI;ʩǛЛáӼϤԉǵӀǾǜqÝÝČ',
                                                                            'І!Ƀ˄ɿɪŪͻŐӫÚϮņǈΥǓćêÄԎʨοɪȪΦǍϬŚD˟',
                                                                            'Û§ҝóƹɍУɋΕϋȬӬCɠ\x9dзҢ҈ѼeĀˤȧѝʃěǱ\xa0ɬԇ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϋǙʯԠŸEλѾ\u0383ƠƹƞԟӺϮԍǭǾ¯ơʣҐϳ¬ҠķʲЧʚ\x8b',
                                                                            '˝bǊĀƲ˾ơӔѝƫнˏ˶ГѐǇǤʔάŻ˚CΟъЈ˅цȦĄЕ',
                                                                            'ģÃ˝}δǉɟľŌоŉǯ\x83Ò҃ҴƀѼϻӰχгьҜsùҶ¨ŬС',
                                                                            '˴õ£ǘМōϰ!\x86\x9fȕӘś=ӒºʑЮТȓņ^ǽҵ\x90ҲЍȩԗƐ',
                                                                            'ˁ˞Г÷ԙ\x8eͲΈɿÄɭʏW¬ķӁ˚ǵБhŶ˝Ʊ[ɇҜԬӯΐȀ',
                                                                            'ʇӰÉЄғщϡԗϓζŘÄsǡåȉ˻ƉȩˀýřÌÒƸҟđѐ΅ϣ',
                                                                            'ώѺǣ\x82΄ϪțăϨʍԜřԩȭʿőԆιƻũťѳοЭŶɭҥԆ\x9aһ',
                                                                            'ӕƊȌǳƑĿɣƱ®ǷʅҰϤǲФϯʻϫČȼԃ˺҄+k;¨\x9e\x99ν',
                                                                            'ʧφſ˒SϻɖӕЮŦƌϐĒĆɆΌ˴ѮƱCҌƘҒ˗ƈHØÒƧǾ',
                                                                            'ƐѣӝЂӷʔȂѰǾʅλɜbУԞɞΩԚлǕğѿЁԭҟĜĸǽΜƨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ßÌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.408134:+0000',
                                                                            '20210208:212324.408145:+0000',
                                                                            '20210208:212324.408151:+0000',
                                                                            '20210208:212324.408156:+0000',
                                                                            '20210208:212324.408160:+0000',
                                                                            '20210208:212324.408165:+0000',
                                                                            '20210208:212324.408170:+0000',
                                                                            '20210208:212324.408175:+0000',
                                                                            '20210208:212324.408179:+0000',
                                                                            '20210208:212324.408184:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ó©\x95ƄĴκнϫʟаӲ*Ð\x9aѐŷЖɁƭÂўϔ©\xadύN\u0383ҍ˵Є',
                    'message': 'ʨфŖXǈ˄ЏщÈёƜƔѕŮ@Ⱦʽô\x85ɗɎʶƥìүĻПҧɊK',
                    'arguments': [
                            {
                                        'name': 'ԗȯҎұŭƨǵϥŶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 759420.0554642141,
                                                    },
                                    },
                            {
                                        'name': '\x85ƌǩB˔ɆlɏǾӒξΐҏɶŃ˨ÉҭɝХѯџŉìˏĚПϱɢŊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӟ϶˭ʘǭҐ|ŧȔЅеԞ\u038døƕxƿTĝώ6ūʨώοϚϲȷɺӈ',
                                                                            'ѳʨӹĶӵƖшǞŃ˕ơƟ4ϊCѺˇтҰȡʵѹɰ\x84ғɚƲ:Ϋ\x89',
                                                                            '®ΒǨʔ·ӨœНǟңɾ˦҅ǴύǂԀΦĀӖèȳæɘΠϗϚǛ\x8bϯ',
                                                                            'ӗˁЀ¨Ƃ\x8cʌètΜҜĲ¢ĴɁьҝĥȲѓӋϬOǥԐСƭ¥ӛŤ',
                                                                            'ԔҔtǇƱѦӂʟ 0\x8dɔ4ǼĖűɼɽʹǊºҪЎЬϓ\x9cͱͳͺ˱',
                                                                            '¢\x8bǮΪĩҬƚ9dſʑ\x87ϜӸÀԀɁńнb¦żĔȏкņ2ʳҌȗ',
                                                                            'ºƐӝľʨŤʣ\x9dԮĳѫ÷ԬӪψˬšƪτf±ɓýəƎ_ąɻ¬Ԏ',
                                                                            '҂ýȔӲ\u0379ŹӒǁҔ\x9cÓɴŗ˳ǚκѻȘЯȭȀĘ¥ʕÕѠ.ˀúƤ',
                                                                            '˪ĝ\x82·^ȟșɭÂğİ͵\x7fʳǏʹÎãпĒ˾Ѡӟ8Ыж˚õǇǑ',
                                                                            "Hİ$ďФҕ\x8bԧ|ɼMǄAȚʾ:ʱΌъЋ'ҡţѹūˈҋD҂\x91",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҏёĘѽЇ\x85љςʘŐӘʮ®ӐpŸђ҈Ϻȁɛ\x9aɑÏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 358681.97716069105,
                                                    },
                                    },
                            {
                                        'name': 'ЭʃƚƲ\x98ПҚɞʥЪӃŹҠƪ/³Όҍhwžρ\x8cyΌΤʗҪ˳Ƒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '°ÊËԭԁІΝ<ϣӪɵЌͷѿυŪγsζ\\ϮωʏńŞԟ\x9aΌ˩ʬ',
                                                                            '˔ɡ2ÐΠuϻȿԩϱûˡƨøȎėөԨHԂЍƗȑƯ҄ѣ϶҅ʃ\x9c',
                                                                            'ɾøιŌʙȃǷGϞµşėϚЗɁɡrEЂЅRɣӟȮµХŊèʴz',
                                                                            "ίŬĳӂB'ŒɫAӔǨƍɭЁюԝѾʅ\x82ͿͺӼҀìîѨҢĪ\u038bК",
                                                                            'ȣ˕ȤЕEÔЂӴǜĿĹυԓ\x89ҺɳƚƵʬˑDсƖńÊʔЈƟ˂ѯ',
                                                                            'ȰњЁ˖\x93ĺԡϞèòŚʀúÌ)ũԪêƥӰíƍͶШÄĕƷԄɆģ',
                                                                            'ïɝʹ˚÷ąϛƾɧrɉθЈӐƂԗѪҧƁĔԬȃȇѽΩҐÃőʠу',
                                                                            'ȴĊϱɒɆѵǚқӏκАĒȜѫʗäʢʙуǯIǓlμɉҨ˻ϥ°α',
                                                                            'iā®ȯőȑ\xa0ƂQͳ˳ǵ\u0378ЋЙɐІɚgµ˯ДӃ»ʳșbҒҍ҈',
                                                                            'KŏɵƸҼѿʐĠƩ\x8eѯʯ˅ʻžʵ΄ŅӏĜё˘ȨǑӡÍҟҤÿŁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҇ϢĳƕÆƭ˞˜ϘҶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': "ȶңɝƓnǳԕ\x95ćĐўǣĥʚȩ··Юу'ў÷ӊӿɾŏΪĠȎʯ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.410025:+0000',
                                                                            '20210208:212324.410036:+0000',
                                                                            '20210208:212324.410042:+0000',
                                                                            '20210208:212324.410047:+0000',
                                                                            '20210208:212324.410052:+0000',
                                                                            '20210208:212324.410057:+0000',
                                                                            '20210208:212324.410062:+0000',
                                                                            '20210208:212324.410066:+0000',
                                                                            '20210208:212324.410071:+0000',
                                                                            '20210208:212324.410076:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǿȈΤϢĴƆΏÃĜƥìͺŻĿő',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҵ\x9bĚȒŵїЩѧȵԀԄAӍÇʺþFĀӑċөγѷӪӟŃΥuƘӢ',
                                                    },
                                    },
                            {
                                        'name': '\x97Ћ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ſҸŅÉɟӜČ}іǧƆū_ԁҠТΌɁȲЦԧÕȢ8ʛџңҨŲƇ',
                                                                            'ŒϙðƊӫēщ7ϽѬƣ;\x8eʄϻӍʍNѸǌƠ\x91ǰŮvВłǢȑκ',
                                                                            'rДϛəƶ5ҡ¹ӄľ¾ȂƦıȪǓǴľǪ\x88ѧ˜teǯʐ\x8dƙÕˋ',
                                                                            '˗Ͽ¾ȯφҗʁıедӞӵ˵Ҿ\u0381ѧþ©ˌөʄIǃгʤӤχӚɎӮ',
                                                                            '$ϚҫͰ\x97º \x89UϣȤӛҢQƤƓҊϏɱͳȅ\u0379ǈҙʠ.ƚν³р',
                                                                            '˰ÚċНӌǔǋ\x83đΙеƝ!ңЉ˜XĐαȳӝĩмäЙƉŻӝ&Ԝ',
                                                                            'ŘΤʱZŸжҢ\x82Дʯ6ɸϞŌжϱŝ\x94\x9aдʸњąІʳ`ϻŒʤл',
                                                                            'ϕȇϥǐȮήʴϞ Бα_ϰʛǷʙ\xadSĎˆΖӒѨТҕȴƦŶƽԜ',
                                                                            'Ҏ˫ӭƟЌυDŊ\u0380\x88˒ҼӮƒ®ǽƧȳrӟKſс˞õϩ7ȇɵō',
                                                                            'Ͳ\x8fɊ<ȫæ\x8aŃ«ѪUʻ˒ÃҹōƼуĭȘηƓǔͼƺĿŅÕàθ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҵСŹҺɯƉК§ЧԖѨäϚхѠŢɥǝԦǊȚȶˮǑǝ²βЛϔӧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            408551.21237477544,
                                                                            526367.5045288838,
                                                                            80285.60211793717,
                                                                            627937.7683501734,
                                                                            -12542.868973347591,
                                                                            459085.1122157114,
                                                                            -49371.31555871368,
                                                                            842814.3365191196,
                                                                            85087.86154133047,
                                                                            55835.86478707989,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸʺσΙ9sE˂ʔƯҴƖʔΧʋǠϠrМʚÒţʸȅȦƧũСѻʵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.411387:+0000',
                                                                            '20210208:212324.411417:+0000',
                                                                            '20210208:212324.411434:+0000',
                                                                            '20210208:212324.411447:+0000',
                                                                            '20210208:212324.411460:+0000',
                                                                            '20210208:212324.411475:+0000',
                                                                            '20210208:212324.411488:+0000',
                                                                            '20210208:212324.411504:+0000',
                                                                            '20210208:212324.411522:+0000',
                                                                            '20210208:212324.411536:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ªGͰǿβ«ɆјʮǐƛҝǩçĤӯʪϯXϼѲҁøќ!Ԕԛ˷ʙˣ',
                    'message': 'ȢϋԢƄʀсʐөҮӁά˨ɤŮ\u0382ǠŽӄɕԅ҉БƎIʬȆгìϪϾ',
                    'arguments': [
                            {
                                        'name': 'ЍҗΙнfΎƓ\x87ǃɲ\x99˂ơЇǙõKȚΈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.412146:+0000',
                                                                            '20210208:212324.412156:+0000',
                                                                            '20210208:212324.412162:+0000',
                                                                            '20210208:212324.412167:+0000',
                                                                            '20210208:212324.412172:+0000',
                                                                            '20210208:212324.412177:+0000',
                                                                            '20210208:212324.412181:+0000',
                                                                            '20210208:212324.412186:+0000',
                                                                            '20210208:212324.412191:+0000',
                                                                            '20210208:212324.412195:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '«ˣЙ/ҎέС˻8_ʎͰяоð\x8b\x93ļ˃Ͷ¦˺<ȔGǓŖıӐȫ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': "ÑιҐ¼'ͻÏԡɇЛЮňЫ®ƞ˵ɯψѮȄǄєɈǙ\x9b\x8cЬӊʱ\x94",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.412572:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĭΩɲʊʎ˞ƧïΖ\x87ðԍgΪĳgŘѦ˥СĞuʶáƊďXąԣ˺',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 744135.4827380446,
                                                    },
                                    },
                            {
                                        'name': 'ʞЂȷɅ¹ЈоˉˋϖĮŮαҎŝȏӲпùƓԛ\x9důрʂŬʎɮÑǩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͻʖƚǊИ¨ȟԅʚʢ¬\x84Ō\x8fйȦːӸɾʩŒвΩŪ°ŖԫĂ\x95ǳ',
                                                                            '£ɕҫȔ\x85ԋԂӒғӪѠtиŻº,ЌԃҨԋŔ1dƒʰҩҀúǼѭ',
                                                                            'ŤӞϼţ¶ȼԑ¹ʵʷƅѲƷƲΔμȏĮGʲĈ\x9fҊÝLǑϝ\x87Ž˨',
                                                                            'ХӤԊǿ˘чAϜɆ!ĢɺȃЌǷÛúϒмϛȅӪβˤˀôXč˝˔',
                                                                            'ѤĎҽ°òŐʍЉßğϰ!҂ƼӈˇЃˡȁЩԅО΅hӘӥɒѾȏ\x8f',
                                                                            'ӪƂт˴ʻɪȡ/ƾ˯Ͱȵ\x84]@źuƁHҨƨЬѐƜЫœ-ϨɞĖ',
                                                                            'ҝӉɰ§ģԄŦЬĚʭӛѲˍӖЍÝɺ˷³зΛΦ˰ě-˗ˈԨǯы',
                                                                            'ǷćőƀɁɝȈņВҸќӋǁӃëƼӜԅ˟˕ӜȩѺӭͿӗǲɛЬʭ',
                                                                            'źʚɓ«SĭƓÍȀԥЀϏҔѶȷ¨ϕ\u038bčʸb\u038bеʟőǹў»ӴΠ',
                                                                            'ŗґѿƠ-ϿAұŉːщşΟêǕӓč!αɔ¶ˢ˫ʇИʹҘҽӜ˷',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϟɶ\x7fӒΟыҫϑǱǮЩCñǮӝȱʋʬɻϙ~Ӌ\u0380',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '®ҷҷѓԥŘȃ˶Їμσт˼ˮǕ1ȢƯӑŔǔԁ1:ӺзмɄŦ8',
                                                    },
                                    },
                            {
                                        'name': 'Ǒύҵžȫ³҄ÈǋΑϵ;\x9fŒǪɭmʯδνĶ\x99íˍϐēˇ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'cƋ\x89ŰƥϿ\x89\x9aEѾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.413596:+0000',
                                                                            '20210208:212324.413607:+0000',
                                                                            '20210208:212324.413612:+0000',
                                                                            '20210208:212324.413617:+0000',
                                                                            '20210208:212324.413622:+0000',
                                                                            '20210208:212324.413627:+0000',
                                                                            '20210208:212324.413632:+0000',
                                                                            '20210208:212324.413637:+0000',
                                                                            '20210208:212324.413641:+0000',
                                                                            '20210208:212324.413646:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'е',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.413870:+0000',
                                                    },
                                    },
                            {
                                        'name': 'кîyЎ˒βɬӇâˬűŋщǹȶ˦ΓĺҹȠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˝ȓɷωȿŶО®Ӛǎӧ\x9fΟɳβʵзĽϊ;˪ϠĪϯдˣѴњЏʓ',
                    'message': 'ȏԈɞ˦ȼѦфӲiрԉӑʭʅʫǬ°ƨđϙÜЏӵvąɐϕ\x9aѝɜ',
                    'arguments': [
                            {
                                        'name': 'ʎϯĮdȇOρöˡΑԙƕʙЅʦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            876489858048176553,
                                                                            -1045140165819891319,
                                                                            814044387680117448,
                                                                            -4301526139284194615,
                                                                            2200477187662489213,
                                                                            -8314735499316776780,
                                                                            1757257069272354876,
                                                                            5987160188652282922,
                                                                            -7301316553624380798,
                                                                            -5364834913559794521,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȜǸßАЃϰɁèǯĸҰʮĕúưÿʭɽƟƿȑʶξǑƑжǧ`ȣʄ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.414651:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϸҚˈǔΙЄӆƗŎǶү\x97ԬǰѠ2ɫǝқƅ\x99\u0382ēȯńʩM\u0380ФǊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.414796:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u0378Ϫ0½Ǐœ!ΦǲϳƓӅʩƹuɠΰ˫ӰӝǰAϚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            922246.5985434062,
                                                                            855262.9840176341,
                                                                            929725.6641782098,
                                                                            -78022.30665034644,
                                                                            33552.17850246327,
                                                                            252986.89985603804,
                                                                            808837.2922264603,
                                                                            592419.4941722469,
                                                                            875943.9408232063,
                                                                            867782.6208210966,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'γ͵³γĔʅ¶үˣŽΩŪĉӳʛʹƠ˃\x8e$ƼȷˆϞӇȂƧӈ˺˷',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.415182:+0000',
                                                    },
                                    },
                            {
                                        'name': ')ǬΝιƢҁŮÖϜ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ϝ˭φɯˉÚŞӉĪΝˤť',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            161104.62040048503,
                                                                            821906.7161982448,
                                                                            977597.8930351348,
                                                                            -47113.64284208461,
                                                                            934468.3798784895,
                                                                            381946.03382255574,
                                                                            -69844.9953119682,
                                                                            53316.14261301924,
                                                                            674826.4628087222,
                                                                            849616.0970928184,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƽ\x92НϼśӮңʱ\x80ʩĿĜʯӜƟ¥ʌϔɏƃ˳ϡͲӏҥҖǿň?Ё',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ŏнϕӫ\x8fҚ҈nωҁɘ˝ȀПɁ$°ɬѭέΩѼ\x9amϓӒʢQϔW',
                                                                            'ѦĔнѨ&˕Ŷˠťƨǔўz±\x95Ʌɳ¶ҏ˳ȤΈˮδԙəӘΪҨε',
                                                                            'ϸ\x7fƌŤσƤӛÈбΆүǬҨш\x8eͱŬҕҫ5ӶȥеɺŖу˼ӾĤΚ',
                                                                            'ʁ/^XѶ͵ȓϺ|ΪÌ²ˤδӯǞʝРӶ<ĢĶƙłƆÏvĪŖ˻',
                                                                            '҅\xadϮʪǞ_ӲӇƵɣɲdСҟď¢ĵųъ϶ƧÑâбҲһϮŅκƮ',
                                                                            'Ͽ œԘŻŤ.ʃĀˮGѰ\x9dфʜȝɣ[¼ӮIɶӂEϐȯ˯шđӼ',
                                                                            'Ǣϴкѥý\x86Κ˥ЀиOқŚΆҘњûΪԄңŉӟ\x93ΩëӜξ|öĀ',
                                                                            '\u0382ȕԃϥ˴ƞɠΉЛ¢ЈŐӷŧřʘθĆΘҋѵϨтӋˡ¯Ӥϑʑϱ',
                                                                            'ǭȿӫµèȲξЎþј6ʝʄҠБǝ]ͲČèГˢ\x8dМѡҩѪЭƋâ',
                                                                            'ѱ\x91ɟǔȶſÂǹңȀɊȺǶϏΡ΅ÙʺŜӡӬÉ˴ºʗßңȀȣ\x90',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϋʨƜиӹÏϏƜӗʷΘԌʋſϾшƉũϤ.ȹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.416267:+0000',
                                                                            '20210208:212324.416278:+0000',
                                                                            '20210208:212324.416283:+0000',
                                                                            '20210208:212324.416288:+0000',
                                                                            '20210208:212324.416293:+0000',
                                                                            '20210208:212324.416298:+0000',
                                                                            '20210208:212324.416303:+0000',
                                                                            '20210208:212324.416307:+0000',
                                                                            '20210208:212324.416312:+0000',
                                                                            '20210208:212324.416317:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'əѿɳє["ЖöƕҺɟӶȑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÚʏқϊҧǉԎãӞϻǹҭԆǻ´ˬҫpшȡοĘˏϧÐӊјŚӷŤ',
                                                                            'țˏџîo˝ҳˍĕΜBҨϐųӜŃϳˉїѶÍƜŕè]ȿΩƴҟħ',
                                                                            'ҠηͽâyΕɴͻ҈eɛėΤʈǬζѬ\x8fŖѤ)ОѻŲϫԌʑřӯа',
                                                                            '·Ӣ«ʱŤ©˵ˆӮӚėӖȧLήϖ&л\x82ɐȖǆЎǋʫɸΓ\x82ѿß',
                                                                            'ϪλıӏϏǄʼ®ǎżşŸΉ\xadɩýҽɅΫȇ\x9dïӇö0Ϟȟʤ\x87ͽ',
                                                                            "ˁˌíӣʐҺdԮ¾ʴҹpШөЃϾłÓƛпрВѤі'üҼĎěȦ",
                                                                            'ХȀĝЄʺФŘʭˀԜɫƩ\u0382ȾτϞøѼǝȎΖȴ\x8fџŷѬЪ;¿Ó',
                                                                            'ԧЙʂʣĆӰΡ˘ǎҿƓσԮǝƬɄɷЮԡȩѢϵɎҡřɀʼѭǌҒ',
                                                                            'ҏӽζ˛Ѥ°\x9fÇ˻ԙΜЪȿχ¿Ʃԑ҅ɔͶɨԎ\xadļЮΓϮԐɟǓ',
                                                                            'ҿɂϧΥȩpѱӭÑӴȑ˔ĽʵˣķɅЅПОѱÍÉұ¼Џ˂λìƋ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x8dÿ.\xadǚҟАłųϸŧ˜ƁҳɠɦÂιвʗӍѲFѦɦƢǣ˲ЎĖ',
                    'message': 'ЖǇʕȅFԨƘЊ5Ȫ¿ѱЋˉ¤\x9fiʌȠPâțǮќҟǨƷ9ҵІ',
                    'arguments': [
                            {
                                        'name': 'ƳӹƄɍΧûԀĀιuϬӚʧå',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8344564358085358191,
                                                                            -6993071107163074317,
                                                                            -1104213941553895142,
                                                                            -1428823057497114264,
                                                                            -7273542361607635644,
                                                                            -7326131567414600212,
                                                                            -3609008989015688657,
                                                                            4698997200628021693,
                                                                            1671009393752378486,
                                                                            -8596215855185232087,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǬÇϗυǄ5ѯˏɥϝĀϿʰӿʉХԋєϖŖ҃ȄȪýȂϮùүѶҿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͲÃÕĨ˟òԔSʋҵȜƗɹ\x98ΐɑŲˮ˲ϤðұүҤѦÄȰľΒ҂',
                                                    },
                                    },
                            {
                                        'name': 'ϥÿͻǷӱƦ¦ǝϚыÚƔĶęˠѻʣȫƋŭņдãƕȔʍͿŞļʺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.417746:+0000',
                                                                            '20210208:212324.417759:+0000',
                                                                            '20210208:212324.417764:+0000',
                                                                            '20210208:212324.417770:+0000',
                                                                            '20210208:212324.417774:+0000',
                                                                            '20210208:212324.417779:+0000',
                                                                            '20210208:212324.417784:+0000',
                                                                            '20210208:212324.417789:+0000',
                                                                            '20210208:212324.417793:+0000',
                                                                            '20210208:212324.417798:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƾԖϐ҉҄ϖϣÚƧ˥ӤhʙҜ҆ОҍɒΔʥмοZɿԎΦǗΡѾӶ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƔʄʃdӸӫơϊɅʛɁѪ\u038bȂϥԀpCʠʿȅԜǚԤЩΌǭ·Ίϱ',
                                                    },
                                    },
                            {
                                        'name': 'άÈ˽Ύ\x9c7\u03a2ÒΰĚҐƃlA˗ЂƴÆūі9МûҒƎň\xadͰĥȬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            355493.6130875204,
                                                                            354690.5758296064,
                                                                            182121.10767679312,
                                                                            687663.1672283182,
                                                                            310597.61367606896,
                                                                            598837.198084436,
                                                                            511969.1842623758,
                                                                            234103.43509280356,
                                                                            577621.9300055064,
                                                                            564965.3888661476,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˲ԃÏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '¢ϰӺɚˍЌԆʂßȺϟˀ΅ŝÄт\u0382ʗӸԆ8ХǱ~',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.418540:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӝқεŇҚȤĪҚДϰϚψɭ\x85ɬҌ\x88',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǎ҆ÚȃȴȅŻ\x93ȣ҉ȊȄͶԞŲҦįЭŒ`ʐɥÕoрζѻϭҀȝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƃҿ3҉ΣƎˇϦɸǡ@ОԆ¬ӪŢ\u0380 xoϤ_3ÁН\u03a2\x8bҎϼъ',
                                                    },
                                    },
                            {
                                        'name': '\x85ѷȐ.9җҙȸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            425042.76438129356,
                                                                            190897.76992182253,
                                                                            840749.4000644585,
                                                                            686859.7676070426,
                                                                            821487.9072879608,
                                                                            847201.1385408912,
                                                                            334317.6608268286,
                                                                            36885.14662152936,
                                                                            79047.36863883023,
                                                                            -46156.10942860205,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʟ˻ϴĢӃ_Ŋȧ\x89ӮϩÑťŜÜǚӌqСÒϬ:ŚӆҲFǮɘæɑ',
                    'message': '¯wĬСΰӃΤҥӦˈɈԜԮʄȏhԕδќǬѳқӞҟѩǐйǆԐʑ',
                    'arguments': [
                            {
                                        'name': 'ɠԂԂş§CǜɨŀҮť',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȥiό҄ɬμƝȃǕ˳ǽ·ĳήАʥӋǄťѨ"#ͶԎėөӍ\x9bΘà',
                                                    },
                                    },
                            {
                                        'name': 'ШÒɓˬɥ˔ſƑç͵άõȈԇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.419589:+0000',
                                                                            '20210208:212324.419599:+0000',
                                                                            '20210208:212324.419605:+0000',
                                                                            '20210208:212324.419610:+0000',
                                                                            '20210208:212324.419615:+0000',
                                                                            '20210208:212324.419620:+0000',
                                                                            '20210208:212324.419625:+0000',
                                                                            '20210208:212324.419630:+0000',
                                                                            '20210208:212324.419635:+0000',
                                                                            '20210208:212324.419640:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ªɫ.Ŷ§ѠϔĕϨщĿÑ\u0378ɅͶԒMηАҜŚʶæĘĔ\x8d¿ƎҢò',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7688186745369886718,
                                                    },
                                    },
                            {
                                        'name': 'ԩύ˳ƾ×ŸȣӐËǌӄʮˍц\x871ΊЦяĒӬΖ\x93ǯ˓қϮЎϭљ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.420001:+0000',
                                                    },
                                    },
                            {
                                        'name': '˒Ƕˋɷȵɂѡŉţ\x9eǥӶϾƫ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϡȐƑÍǬϰ4Ɨ˒ɽϗ\x8bʧɢϼʍͼǢӪǣĬ?ȑɫΨɅQү˪Χ',
                                                                            'Ǎþ҃ЖȪXΐŮˈ˵ʆŪͺϦӱĢ˟ċҬīӼÈΞGǉå\x87ђ\x9b:',
                                                                            'ЌȌȩûԬӞыƠʤɻѦͶқ҇Ş˔%Ā*Ʈʒ\x9dň҆Ʀϰȹʢ˛Ҕ',
                                                                            'ӭӛȏƤΞȀҐ*ɑ˼uЗҢҚǤҩҐȱƷÅ˻ɞӎӝԤu¼ɫǎҲ',
                                                                            '8Ȏ?PØϚϭЖϿϿŨƿūѢɷǛȣԅǇК[xЙƒ«ɳ-ĊхƊ',
                                                                            'йʽʪŸĤ\x8a ǄżùʕʴԜţơt˾ÓСԫóŲPʍ҅ưԣϓεӔ',
                                                                            'ˠȶԂƭϊ˗ԍƺʮȸȌɳ\u0380ҁȿҏ\x82ɚ(ӲǗŬКѝĪϹ˃ɚƣԌ',
                                                                            'ȄʎOԋӲƤǵѭˣØƈċÒͲĝɫЛԊͿŜԉǟљ>ѝӗȰ÷\xa0Ζ',
                                                                            'ɹȤƗҌ(ȶǱ1ġѾƓыȳҘȚζȑҠΟӥúƼɰüӬӤǭЌЉΜ',
                                                                            'ſә[ƊȨҰŋϐɩͽХϨŒșÒоȋΥԜlͱėϘµηƳ˲Ƕz˥',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "РӇė'q\x89ŹѿЗƮÊƹɌL\x9eΪ΄ġ\x97ʒĈӕΟŶǪqсуăʊ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƒԣϷuҁŦңǜȉğŠЄŒϷΞѧѲ˽qјɜ\x84Vһ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.420691:+0000',
                                                                            '20210208:212324.420701:+0000',
                                                                            '20210208:212324.420706:+0000',
                                                                            '20210208:212324.420711:+0000',
                                                                            '20210208:212324.420716:+0000',
                                                                            '20210208:212324.420721:+0000',
                                                                            '20210208:212324.420726:+0000',
                                                                            '20210208:212324.420730:+0000',
                                                                            '20210208:212324.420735:+0000',
                                                                            '20210208:212324.420740:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǾƈeƱ˔ŗÆ\x95ѫѕʘ˗ƧҟŉĝӠЅ\x91@í\xadÆʏÝ˞Ǉʣ¯Ĵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 379232.2091373557,
                                                    },
                                    },
                            {
                                        'name': 'ŅȻǎъĒʷΆɽ2΄ϖkГĠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 59581.466570913995,
                                                    },
                                    },
                            {
                                        'name': 'ĊԙϬϣѤȭΎæтɾ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -19515.821032660184,
                                                                            287224.9887294244,
                                                                            990779.0662761068,
                                                                            -25123.644374265015,
                                                                            -72564.01561633684,
                                                                            561287.843280079,
                                                                            176230.33382044744,
                                                                            869589.2205774151,
                                                                            40700.73176493918,
                                                                            306117.9097782605,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӰʍͶѫ?ɊĚ^ɫĎ¼Ǒԃ[ɇјǫϺŸΜ˰ƇҲԘΩђŌҲҭҽ',
                    'message': 'áқ;ǔǟόƒUɑȀбӔѥȌŠɷ˜ѳүʖʢΩȲúʗΎı;\xa0Ŧ',
                    'arguments': [
                            {
                                        'name': 'şƋǎ\u0378ƩρǐѧЏϮ¿ƭΧшÑʔJğÊĮ˅ŵ*ȾĳʱƽǥԄЪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǤˏҼ:œӏĵѰиǶ3',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -21171.83394307096,
                                                                            851279.4981511888,
                                                                            395326.5926849848,
                                                                            72902.3091195079,
                                                                            950739.0926102994,
                                                                            202358.78079458774,
                                                                            680781.0294996706,
                                                                            494767.2269593094,
                                                                            573777.8427511856,
                                                                            716960.9928767361,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƹƯĶҙ§ϯʐĦЋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.422118:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȵğVɩөҀŚȫ\x8bȍԛӽŌϝŇßԁ\x88ЂƇʾʶ\u0380ÍίɵǻāÈų',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2769360081069404151,
                                                    },
                                    },
                            {
                                        'name': 'ҭ~uУşǿƶѹƶ8ȺèρšύҞȶRҢƺҨǡӤʦȫǌMԬͺͻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 521764.897133891,
                                                    },
                                    },
                            {
                                        'name': 'ÀǘȟӬ}ЪŚʰNǾðїǳŧˌͰёɩө',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 902646.6374222637,
                                                    },
                                    },
                            {
                                        'name': '\x8eǗʹbqʋŪˬƣж˒ċĽǄ\x8cЋRÚȶɢ¾đZŽͰϝƵŀϙԮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8565796036968107048,
                                                                            -3419604735745617387,
                                                                            -6358107986334712185,
                                                                            -3798656704613972470,
                                                                            5987766220435860912,
                                                                            -4131721859300086483,
                                                                            329907396727310613,
                                                                            -8625393285173314493,
                                                                            1707903847947201096,
                                                                            8108748517580180623,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȰԆԑɍʕƄ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 294909.5340556148,
                                                    },
                                    },
                            {
                                        'name': 'ѫӇқи˲ʪʽӹ0ŝόδǊȲˎϊÒсɎʯĹ\x8eϪϲԫӊξɍ\x9fˎ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6086100719760217812,
                                                                            -1259262099407836287,
                                                                            -5390298446088311412,
                                                                            5704789777785268314,
                                                                            -2347457171567608184,
                                                                            7907470818268464592,
                                                                            -5463478550737667233,
                                                                            9136443455494392914,
                                                                            8849333832573937299,
                                                                            -8589939242990260538,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǁkȄԡϰҜƍEɢς˙ŋɵԅӐ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -234156745447064364,
                                                                            25607645285603405,
                                                                            -7561472712375344400,
                                                                            -8407347367545698283,
                                                                            -1903119091225028332,
                                                                            -3155116337806628046,
                                                                            -3120814496640412825,
                                                                            -6290521356923992226,
                                                                            7753178374871873874,
                                                                            7386768041796354169,
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

            'scope': 'warning',

            'messages': [
                {
                    'catalog': '?Ȃ',
                    'message': 'щ',
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
            'identifier': 'ƇԚԙԋđ\x88ȍńĢǣМÝԥ·Ŋª}\x93ǉƼτˈcɏĞXǶΊɫǕ',
            'categories': [
                'network',
                'configuration',
                'file',
                'os',
                'os',
                'configuration',
                'access-restriction',
                'access-restriction',
                'access-restriction',
                'access-restriction',
            ],
            'source': 'ȈҨ¸ʢΏӌʧrȤԡ\x96ŮǝƯԬͱӶȰӀϤʋҞԑĿҐΐʩѹ~Ѕ',
            'messages': [
                {
                    'catalog': 'Ҿɥбċґ˦ɇʙђǟHʮ˱уjЁЬɔKµћɲΞȆíϘҼϊ\x99ʴ',
                    'message': 'ӣŻŭȾcƗԟyđʱ$ȜʡΙіƙфϡƪԍҼ¡sӒΐΣ˫ǣ&Ӫ',
                    'arguments': [
                            {
                                        'name': 'ҾǉϦɈшӓʣ˾ÖȅʸƢдЈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -38362.54141457802,
                                                                            921558.1813215053,
                                                                            -25839.422928084183,
                                                                            951531.5099938419,
                                                                            327371.78164725855,
                                                                            548028.8969492745,
                                                                            923648.8545139421,
                                                                            569469.611559387,
                                                                            254466.39572254824,
                                                                            427588.62081050803,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҃±ώςɕ\x97',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԉԍѠц´ǼʊÆ\x90ƋȜƭrŚД˧ɀіŹDėѶßĬ½ҀСԊ6ɥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.449388:+0000',
                                                    },
                                    },
                            {
                                        'name': 'iһtċдҏΑу2ÝCʕԜǏιä¶ɖʇëѱҀŮ7ϮДЋƏӻţ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.449530:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ҿ\x9dЇкһ˦˙¯ӌɰǛͿ3XьʐǺ·ÁʃĔŽуǯ˾ʆʜɆԠϾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2594610456214951611,
                                                                            9156023907784766352,
                                                                            7178258926313889989,
                                                                            97545513085816083,
                                                                            -3931460075167530244,
                                                                            190081145425548019,
                                                                            7529480884713798564,
                                                                            5709462471019993745,
                                                                            318368294485851830,
                                                                            -5729369116417047951,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ðǤԚҥēʻл\x8dlԃŮӜˀ9˹ȄƜʍƉĜ˲Mхˤļ\x9bQɵΜǫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.449908:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǡȷì˞ʙΆʥ˻Ϧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9040890238203854582,
                                                                            2687675149014871726,
                                                                            3683799328979750889,
                                                                            2146136237156042489,
                                                                            -8429743616996145019,
                                                                            -4593454611733482723,
                                                                            3258228339301447830,
                                                                            275100870213819968,
                                                                            3659140276857768678,
                                                                            -6253415968875800538,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'щ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.450266:+0000',
                                                                            '20210208:212324.450276:+0000',
                                                                            '20210208:212324.450282:+0000',
                                                                            '20210208:212324.450286:+0000',
                                                                            '20210208:212324.450291:+0000',
                                                                            '20210208:212324.450296:+0000',
                                                                            '20210208:212324.450300:+0000',
                                                                            '20210208:212324.450305:+0000',
                                                                            '20210208:212324.450309:+0000',
                                                                            '20210208:212324.450314:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҈ΖƢǥʳФǬςĸɃʧÑ˸ʒΓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.450533:+0000',
                                                                            '20210208:212324.450542:+0000',
                                                                            '20210208:212324.450547:+0000',
                                                                            '20210208:212324.450551:+0000',
                                                                            '20210208:212324.450556:+0000',
                                                                            '20210208:212324.450561:+0000',
                                                                            '20210208:212324.450565:+0000',
                                                                            '20210208:212324.450570:+0000',
                                                                            '20210208:212324.450574:+0000',
                                                                            '20210208:212324.450579:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӱǂàάźɐƃѻʻѠѢ\x9aўϟЊ˅˺ɐ˴Ͼ\u0378ÊІȋˍŁíϣėŌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԩȶͱ¤ϋůÝϖƊȱǡЏȌлҜҪŜңʮŮε^ЙҊѽͺɒшĕƣ',
                                                                            'ÞƪԂŦ=ŜШÝBȧɸ´¥ҟТƟ¶ѐѮʙǲМёøΪЗɳʚЂʎ',
                                                                            'ΰÐԒǵǯɌbʇÀɏɜυӧѴѼЙʏɔȌƜǾēΔѲËųƥŞқʿ',
                                                                            'ɀΒ\x94]¬ά\x99ϔδŖӤԈʆxӔDɾӎżҤ5чϵ˭ŇÝßʏǐy',
                                                                            '!)ǱǷСŨҺ\x93ĚÉǃEcӼ&͵QĔ\x86ύΘ¢\x85YŏˎʢӁγÚ',
                                                                            'ӑIȒĽѕĴεԏǁҟӼӢӇǻҙʇêҍξӜҤҌɸ?ʴϛŁʀϜƱ',
                                                                            'ªИΙɝɈ˘ˍĈěƗɀƳŭȯϗȚƼſҡӌΪҨ+6҂ƖȺêѬy',
                                                                            'ΰѭσʻѺĊʵʄǯƛΘȪȚϔɦԬʈ\x98ԗƐņԚӖя´ыŁӊ]ĸ',
                                                                            'ҨҨūЖʖ˙ȣʽҬMԢʇϩҎҰ˕ŶҨʼҿˬͱϦƩ\x8cα˧GȲƥ',
                                                                            'Ϧ\x8cɨǂтVԮǗўΔͺƽо\x8cһɌ¹ӭˌӶǹÎһм¢ĊƼӚŵų',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ќʞʃӯѼ϶҈ȋÖ˥Ȗ˙ΰίåɂƐ˵ïÚýʎɄԫƕˌĒǽÀş',
                    'message': 'Ͽ\x8bŗԄ ӉҰ˙ȇєªſЧʾʁӣīѫӌΗО¬ІЦ+ȑԛ&Ǟɿ',
                    'arguments': [
                            {
                                        'name': "ӶǷѕʖ'ҷĒhŔʇӑʗϸ\u0383ƨӇōŖƱӴƗϏһ\x9aиʒâʽˀе",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĴĬʼӪĤϻΠëÍԡƅҺªĽ\x94ъҷȐɫҶӰ\xadˠ҅хԙϮʆϕȹ',
                                                                            'ԢӒžѮԧӰҦȈѳѽɤ{ѸŉȎȺʓӇǢфȠέɻɟmĆUѾȝ+',
                                                                            'ϳˡѐƙǴ)ԖηӤOɺƿʴЙĢȰёǛηΰͿĠй]ӀΙ`ŀ˞æ',
                                                                            'ƙʪόęȒÈõϴƋǧTPˎΓͽϋ\x95ǎвâĞпǷďΣłňȱеǞ',
                                                                            '#Ǳɇ5ΑŻŵҁϼL\x7fǾåĤǵѩěЍ!2Ү\x9dôɱņѢ\x92ԉȸƤ',
                                                                            'тʆȤεέʈϨɳϟЖѨҀʲҋǨʻǆɌпwҌǵïĹɃͿǿҡDǂ',
                                                                            'Йԉ]Qǧʄԇ½>ǩ˾ϣŔƶĆЏxʲÆJɤӕöѱȀԖŴĦӁӏ',
                                                                            'ŖʀÌԥÁ΅ӝӰʬňƠҌф҆ôȼĮkǷǊʩAΪ҅ʬŰʁІӾĆ',
                                                                            '\x87_ɩԉԩǣˈǯԔ\u0380qĪʵƘрÕЇȺĝNҎʝƧџǼûɱЧˀʲ',
                                                                            'ûϸǤɁʺĮöιʲʍ˃Ŋį҈һ÷ć΅ɋ˧ϡȳӎƨŋúӠ?˭ȥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȡ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԤѣǕĽ˓ϞԡƎϾˉϡņҿ?ΧҺʠЛӳԥ҇ĵJŇƌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.452095:+0000',
                                                                            '20210208:212324.452107:+0000',
                                                                            '20210208:212324.452112:+0000',
                                                                            '20210208:212324.452117:+0000',
                                                                            '20210208:212324.452122:+0000',
                                                                            '20210208:212324.452126:+0000',
                                                                            '20210208:212324.452131:+0000',
                                                                            '20210208:212324.452135:+0000',
                                                                            '20210208:212324.452140:+0000',
                                                                            '20210208:212324.452144:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038bǈɠɒʤӏźԇͿǗ½\x96э',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1653144368866036892,
                                                                            -8901771084144181804,
                                                                            7511749848782874725,
                                                                            -5210148935108063826,
                                                                            2666721355158112713,
                                                                            7958949616672413818,
                                                                            -1834146505448052120,
                                                                            -8848141280685468678,
                                                                            8519364754214158633,
                                                                            -4425552401306263834,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ψ˞ѧǘӑ˝ūÖŝāΓÛцUͿʣǔЀԧˌˉŰƮϣƿĽӿӖˤî',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1757670257730937611,
                                                                            -304195332238707230,
                                                                            4369803333796005951,
                                                                            4004132713149509195,
                                                                            -5998237752129535695,
                                                                            2601686126898606210,
                                                                            6578712292740403897,
                                                                            887893757829053820,
                                                                            6049477151860541207,
                                                                            1524022897826473270,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԑǴЈ+ӾсåɭľɄѷˡƼÌȈэǋʄ\x83Ϋ%Ȟq',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 328142.096478187,
                                                    },
                                    },
                            {
                                        'name': 'Ƣ\\ɻЕɥуς)˾ϐ/ʌҲ\x94дHϳǸƉEҠɍjʈlǱϒɯǏь',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 580824.6578678015,
                                                    },
                                    },
                            {
                                        'name': 'RVmÅΪϕңĶ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˢ˕ҙ\x8eҢѮĿ&Ɖʽȧ\x89ƲԐSӜѼԀϵȍʦɿӸ˟nгӴʠϥȎ',
                                                    },
                                    },
                            {
                                        'name': 'ɩσ˪ʊΏɬgЎȧɉ?3\x8dњď³',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5358820241138464631,
                                                    },
                                    },
                            {
                                        'name': 'YЁϔȧ+ʨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8693333481130412402,
                                                                            5595216741199494335,
                                                                            -4579530068232517777,
                                                                            -874419649161789673,
                                                                            3479755410197520689,
                                                                            -1239760422518212538,
                                                                            -2156088301899069540,
                                                                            -7088867849355875816,
                                                                            4490907279247796892,
                                                                            -5698946516087107857,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԊȶτĖӦ(Ζ`]Ӫҷǜŋϣ˺ϑѓüʸўŇűԎҔ%ҠӬîϙɡ',
                    'message': 'ɣ\x95Ӑ͵P\u0381îзн˻êӱԧÒņȎʛƻ÷ưŜӇͲŗÔʾñŰʰϭ',
                    'arguments': [
                            {
                                        'name': 'ΐ˒şɣ?ɻӄ˦˸ƟʵQӍ˛tµǎτΑ\x8bϯȑӨźД\x92қӦңɸ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƌ\x9aÑʹĮЍΊŕΡҀʿљңΉ͵ЗʭČȝεċϯѝϗ҄ƃǋŪĺɌ',
                                                                            'ЃӵìħӍѶŗ?ěΏ\x82hǽ)ðțɔӇѶˏϣ\u0381Ӟ:щН\x9aƥʏ˾',
                                                                            'xƓŝǗŝԐϮĩÖăʧІΊȘӍҀ˭ϼ˶ҾŲ˨ƞΆŲɁ+Љѥψ',
                                                                            'ѺАҮӤͱǴǯϦVҟƛȟnDǉѲОђˢɥņ;иĮˬʥɭҸ\x9bϰ',
                                                                            'µŀÜƮǲјνȺϭ˔ǿŲĲЗȊõ˲ì~ж΅ԡǹǚðʅњØѱԘ',
                                                                            'ƌӽ˰ҖԋĚ\xadÿҖпλ\x91ąƩҀĚŊÞ˙ť\x9aѲɯƜóɏ¨ћѯȿ',
                                                                            'ó΅ӥ!ǎКǷπư\x8fЀƀȵӫѳͰЩϽbɋɗǴŒɉŔУώïȴè',
                                                                            'ȻǊԑUΩĹʅѢ1ͷÕӾ˻ӎûϿŸŅԫĳѕǒɥĂ-5ʢԞɵ˕',
                                                                            'ìʦŏƋȲɆЅƷȯłәă΄ƅӢ˼СʜĆΥɺЊWлMȼϦʼϛӲ',
                                                                            'ÛYθ9ˬIϢÊŢơˠżŴ˗ԊɆвҧqßεѯǟƻʅɾЛȯƒƍ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ћӨʯЬ˳ǃKφɾюӌˁӑӵһƬÃŞҟ]ÿУеAϓ,ԜԎȠʓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҹҨ˕ƭȃЉɝʣΝȍ¹ҷ˨ϾΉͷɔӷȳûҪŨɘȔ\x82ϭ-ƀʭɭ',
                                                                            'ΤϿξ\u038bðԗҾуҫЮɹгϵԔӷǔ£ӘNȰǛĵψҏXӦȡңȤɋ',
                                                                            'ԈʵĖǠʕËϹ\'×ϬÓԩʓѣЙӤŸƋɤȪ"ƛŷҏӢĩ\x7fǙƟɊ',
                                                                            '|ιĂįйғЛƕѥ҉\xa0OǋĨ¸D˼ζƢӄ҂Ҧüæҙέҭμʯү',
                                                                            'ǟжƲԂüŷʹȮƢİʌѦ\x83ȵбΑѥŬʜčԠwĞŢñ҉1ȡӉӌ',
                                                                            'kõɹɆˀ˻ȮЅîχƷЎÚΌƜŕδʃŧƳȻˢԜǜǹƼ3Ƶƶʝ',
                                                                            'Ď÷òƥЃѶȗȷdϘɵɴ˝ӳȉR͵rː\x83A¬ɕ˳кƃˋѶҢȐ',
                                                                            'þϪͶΖͲԊ\x86ȜӱѮư[ӽΚˉј˃Kˆ˜ӒϪɒÝ϶\x97ɸʾŪ\x8b',
                                                                            'ȖςӸґ¯ˍΚʀ;¬Ƥǚҗϙ\x85ΘЇ¥υѡΰͻιнyƯŧЯ\x87!',
                                                                            'BґюĄÅŬυΪѐςǩÃͿīHɏӞӢΟÚƐʢҹЇәӒɣйʁʊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͱӣƑɑΟȭ\xadƶЫ˯íȋɵϸÏθЬʤӰԄтѽ\x8fgȢǿă\x8cȾ[',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7265392805930801771,
                                                                            -2123747250437207340,
                                                                            -1139609093118430320,
                                                                            3216168961970354410,
                                                                            -4520157488955045385,
                                                                            -2751519650088363552,
                                                                            -5668281873223378816,
                                                                            235773501709846065,
                                                                            -2787333460448371421,
                                                                            8819246488344126665,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ўїɿ˗ԔƏϰћΜӎǚɑƛōčʖ˦ŷɭWƍҖű˾ϮТƉ)џc',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѕӱþŇģŪѸlӰЭȥū҆Ťįŋσɫҟ$ĝӢǲΖʗӔӊ˘sá',
                                                    },
                                    },
                            {
                                        'name': 'ʰϙɂͷŪǁѕǉԑîδϴɭƘʉѧ>ƠąӄνǙŐǊϫӆʍjʗɀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.455331:+0000',
                                                                            '20210208:212324.455343:+0000',
                                                                            '20210208:212324.455348:+0000',
                                                                            '20210208:212324.455353:+0000',
                                                                            '20210208:212324.455358:+0000',
                                                                            '20210208:212324.455362:+0000',
                                                                            '20210208:212324.455367:+0000',
                                                                            '20210208:212324.455371:+0000',
                                                                            '20210208:212324.455376:+0000',
                                                                            '20210208:212324.455380:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҁӶӽȚʦϒʿѫ˶ӐҕĹΘʛȐģѻFӐ˄+ρìϪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.455606:+0000',
                                                                            '20210208:212324.455615:+0000',
                                                                            '20210208:212324.455620:+0000',
                                                                            '20210208:212324.455625:+0000',
                                                                            '20210208:212324.455629:+0000',
                                                                            '20210208:212324.455634:+0000',
                                                                            '20210208:212324.455638:+0000',
                                                                            '20210208:212324.455643:+0000',
                                                                            '20210208:212324.455647:+0000',
                                                                            '20210208:212324.455652:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '$ɀːßХƧСʥϩƺЛѧƨcRӮəƱ\x98\x87ԂҳтμɁT³ˑż',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1979779464746498084,
                                                    },
                                    },
                            {
                                        'name': 'ƺȥšʅ\x8770ºÓąӹǲҁ`ǧԞϖZХȺс+ʍʍέɴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8484795004351672359,
                                                    },
                                    },
                            {
                                        'name': 'т!Ǒ˲ҢǉȌӐПɖĸĊɴƄǐί¢',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.456126:+0000',
                                                                            '20210208:212324.456135:+0000',
                                                                            '20210208:212324.456141:+0000',
                                                                            '20210208:212324.456146:+0000',
                                                                            '20210208:212324.456150:+0000',
                                                                            '20210208:212324.456155:+0000',
                                                                            '20210208:212324.456159:+0000',
                                                                            '20210208:212324.456164:+0000',
                                                                            '20210208:212324.456169:+0000',
                                                                            '20210208:212324.456173:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɟƱǖΡһˋĮ9ԠǮQҬпʂĭԕΆҕ·Ξ?ȩƐnʕӰʖåÁӛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.456392:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ёοӌŢʨԟʆӠ}ҝЈΙʁËƑämɢȻӗҰѹЈҩȒȍiʻÂя',
                    'message': 'ɫӲɻ˱ӱĶӯҜыԨʿ~҉\x98ЗЯńŞ˳ɀѩȁǋĒҿȖѧϯțľ',
                    'arguments': [
                            {
                                        'name': 'ȌИUŨΞдʌǭʑԈ˓ɌѾȼ»ӃӸĭͽ˸тϒƆϋȁҳӟȗ)Ô',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԣlɳó\x93ӖPï%LRԣĪųiҾɺϼĄ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Țы#ә˹¿ˠѿΛѨ¡ʞǣϕӘӵϴɞǦГˣһԙϕ\x92ωìƨćː',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'NҭćǫɨΦĳ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2237280233207088168,
                                                                            4004480909156890293,
                                                                            -6057857312312801739,
                                                                            -8810986109090077220,
                                                                            8543503423683378651,
                                                                            -7822208034757831014,
                                                                            -8591537451934273963,
                                                                            3325227757313414748,
                                                                            -234518217359009740,
                                                                            9054218936711050549,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˍȞȓʫɈԬíέĎĥςϞЄ˲ǼАƴƿ˟πǧҿʀǯMβƏЁĄȖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.457553:+0000',
                                                    },
                                    },
                            {
                                        'name': 'čѼɚɎƾďøϡ\x82ŹıʳԖǝQϦԮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɵVʆπɻιÃʑńãԟǣ҅ʟΠƨЙɫцƒҾюĵBж©бғAŜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.458120:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʁˡǛҒБɆǥŅ/ȘԊʿɸѷ)ÚĳĽΨͺ&',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7064969995931779607,
                                                    },
                                    },
                            {
                                        'name': 'ȔĻĈJЌӊƢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4750823904602386456,
                                                    },
                                    },
                            {
                                        'name': 'ØÔʿƩǉƜȱĊл϶)ЖˢԇдҷΩň7ϴρƳ\x93Ū\u038d\x7fôȼĴǕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ιÞŻə/дtȶɤŤέ5øɐƳ[ғѦ͵ǮȭТ5ΞɛƏџѷːʕ',
                    'message': 'ͲԅҨʿ4³Ə,ƫƎ\x85ʛŚĒӲӟɪ}˫ƙͱʱѧфÀȄη˝ϛΜ',
                    'arguments': [
                            {
                                        'name': 'ɦȻ˕\x83ʨԀӇҲ\u0382ǝѩ·˧˲ӉʙιȊʛm2ƻϙʔĪǉəYϊƳ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ξï',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.459186:+0000',
                                                                            '20210208:212324.459207:+0000',
                                                                            '20210208:212324.459219:+0000',
                                                                            '20210208:212324.459230:+0000',
                                                                            '20210208:212324.459240:+0000',
                                                                            '20210208:212324.459250:+0000',
                                                                            '20210208:212324.459260:+0000',
                                                                            '20210208:212324.459270:+0000',
                                                                            '20210208:212324.459279:+0000',
                                                                            '20210208:212324.459289:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȔɒԪϐǁʨѼȶӘŽϊπ˞ѵ¿ԁǐԡɰƬˌMXĒʹϐļЭԔL',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɡЪƖĲΡЧʒǟˏ˺џɲţˎɵΣ=_ȋͰÌÞЊĚiȓưς<˓',
                                                                            '`ʸĎӡӪªŶƆӓ3˰Ǝԅʞ˱˼Ԣ˥ХɇӘş\x8b£ːɦҥҘϐļ',
                                                                            'ӣĪЩӝƶ¢ÂÀдłВѲƲüčˁʌɇǢʐĘϮсŲΨԥҺΈϩ»',
                                                                            'ïѡţɿȭȉõdɞɣЗ#҄ǾƂțψϋѐƖˉӡϤNϩ˳ˏϜ\u0383ƨ',
                                                                            'ǵĎ2\u038bнðɬĿӥǂħ$ɡϽȕЂēƇσ\x92ϲϜʐ\x97ПӴ2ы-ˬ',
                                                                            'Ìė~ǴҵҦϟЮEґіɗұocɛǭҫÿϔ˭ȱįǻɳːǲШIϻ',
                                                                            'ѵ΅ŞЬʬʑŘѼХϤϬkg\x9eͱƤɽĳеԡԄˎLͳtıʐG\x9dĎ',
                                                                            'ӯЋΑĽύѕ˗ãгěĜΉԬĨȂ˄\u0382GҲ˴ͽXg˕ѠҏϋȞӸΏ',
                                                                            'öчŻǶҺJԘԫß×ϛˊļжɂТɭӶƿԍƈBӾЋϷиϛЭʁЪ',
                                                                            '\x9dԟĲ˦ėӵ¥ЫaͳøΧЃįÆ¬íͱфýʲăŴƾŮҚχ˴ΎҊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӓ˛ľԚƽĔАş\u0381uқĝ\x82ѡę',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҪʴиηɔϮǙΪǤвĢėԕҧǄзÃͺÅ˱ɔʯϧ¶ǩjȶ/ԋѼ',
                                                                            'ÊiëșÁщŊ¨ƩӔЁȺǏ҈ǱÜĞӂÀ\x85MȚ˅ЗӋÃυȗȎҥ',
                                                                            'ЪʽŢǮǬҋǊź_ԑɒԔЭԍgӍҧъ\x9cøЇƺʉҕȺξЗØǚľ',
                                                                            'ɲҩ\u0382чҘDǒ$ϔ˼ӎϝÙǌƞYκθ\x8fԭӰϦЛҳЇ΄˻ʗɧʉ',
                                                                            'ҤɸȩÕ˗ʨҞŉЏγͽIęͱáѐΗҴɅӴê@ҾӀԌʓǛɭћԦ',
                                                                            '´ҎɦӯҒřǄviȐǙЊӮθϭĪϜǤ\x83н҄Χ\x7fʴĴ½˸3ȫѬ',
                                                                            'ƂүӮȡ}ĠƵ҃ϱϵúÀӡƧÚHû³ˤśǅƳоԀřѶӈʫƑѨ',
                                                                            'âΏ˒ԋҥŕǁƢnЫƴӖ~ǒѭɀҐр˔ǏҽˁђЊÿӚњ$8ӿ',
                                                                            'lπӐǷƓɗ˸ƀʇʪФʇԣ9˕ƶRĕѪ5ћ¥БϋĢӚâɾǰQ',
                                                                            'źҿ҄ɢΠ·˙ώřЯĭǤӖә~ě҉řϐϱÁҟъȖŦҦτάðƺ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЕȐΣńȡˤlѝЋȿ@Ǝ\x87Ñʔӣ[ÝƩѺа?ȸ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'Ԇӓŭз\x89DɶɚԠŀұђEɉҤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɈĮҚӻοѳĩ°ѾФđ¶łХ\x92_ƻüԂģ]ȝʥϦҠȷŋɅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.460785:+0000',
                                                    },
                                    },
                            {
                                        'name': 'rǴӖͿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʵĔģ\x8bŵһ¨ĥˍӊ;ÖҼʎɠʨʀДάóϭrӁœϡѭʵİЂԃ',
                                                    },
                                    },
                            {
                                        'name': 'ƐŒϻӵȾ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʐқƧrѽĝԧēȶʴ˰ɁҔƩʪSňʉʘʦžʚ˸ѻɻӢβϝ<ł',
                                                    },
                                    },
                            {
                                        'name': 'qԢüØ¦ɿѯ0ӭɮİǭѯȊźΟ\x92η,GĤŵȘȹϯʐƶàĸҐ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            182307.01356656448,
                                                                            701888.4427623526,
                                                                            -26354.968097264747,
                                                                            -48877.85093658122,
                                                                            445899.4092684268,
                                                                            756217.1607452173,
                                                                            606587.5411643442,
                                                                            533890.0376131681,
                                                                            796271.8711479864,
                                                                            395784.6832786678,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'q$ѫĞ\x8aѳ҅ÁѾϲҁтЏŎÕ\x93ʪҏӈ\x7fŌǸ˞ӒfÃƅ ӇЉ',
                    'message': 'ѼΥĩēӯǊƫԕɹӘİ\x9cǑʉǔ˹˖ΩҚʹÿ˞дɟӢɌǔ\x93qȏ',
                    'arguments': [
                            {
                                        'name': 'ҟάԎЂμξƦƌҸŕŗөȭϦǏ\x9fɕҭĄɖɦĬΔɣŸӣɭʯƶԟ',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ͳ\u0380GƇԨ΅ӜºǁƊŤ\x93Ʃ\x93ɧļўXΰүÞȿÕ'ɓDԪԫɁƷ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 573891.1611355409,
                                                    },
                                    },
                            {
                                        'name': 'ńLǃЇ9ʦdʿϾӃɴ5ÌӉ˝Ѫǉ\x86ԫ4˃˲ӷԭÔʟ\x83žɣȢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '·Ԭ\x81ͳɥ8ńŰȧԖȼˆӶʆ˨ŲƆĥʣȠĦ_ԩԬˢӲJά҇ȫ',
                                                    },
                                    },
                            {
                                        'name': 'ˣāƮÜŞʩεȑлȎӴà¼Ňɢ\x9bYғȪˇ¼ȥǔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.462252:+0000',
                                                                            '20210208:212324.462262:+0000',
                                                                            '20210208:212324.462268:+0000',
                                                                            '20210208:212324.462273:+0000',
                                                                            '20210208:212324.462277:+0000',
                                                                            '20210208:212324.462282:+0000',
                                                                            '20210208:212324.462287:+0000',
                                                                            '20210208:212324.462291:+0000',
                                                                            '20210208:212324.462295:+0000',
                                                                            '20210208:212324.462300:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѫĠĈɜuΤЇŠɩzȖYԡɚ҂\x99ʳͰѬѕβ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 627652.3992325686,
                                                    },
                                    },
                            {
                                        'name': '\x80ʡ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9eψҐǒфϸ˴ѵìűԖ˚uƂǵг\x97ǟʳƂȘǤŅӅ{˞ɔŋ˧Ǭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʋѮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.463011:+0000',
                                                                            '20210208:212324.463023:+0000',
                                                                            '20210208:212324.463030:+0000',
                                                                            '20210208:212324.463036:+0000',
                                                                            '20210208:212324.463042:+0000',
                                                                            '20210208:212324.463048:+0000',
                                                                            '20210208:212324.463053:+0000',
                                                                            '20210208:212324.463059:+0000',
                                                                            '20210208:212324.463064:+0000',
                                                                            '20210208:212324.463070:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÁÐҴʇ_ûџԅſЊͳЏҘŏзňˣЮъØƍΊтÜƳƷӤƽɥˏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˞ȱϤҚЭʊǡ£ʽɨɓ\x89\u0383\x86˨ɽӌɞίƵĜȵ$˫:ʹǺĜЇü',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            774363.9823401733,
                                                                            114364.5712349524,
                                                                            559383.6874088697,
                                                                            873320.6725449344,
                                                                            923316.4683329543,
                                                                            589216.5601901442,
                                                                            225946.3425387066,
                                                                            292047.4690273239,
                                                                            474809.79809253465,
                                                                            607682.4487105595,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˛Ȧȇwƌ§ˌˑŪӫ0ȌĈǓ²łõӫШɓҡÌʺ4Ƈĵ˩ɾȧ˭',
                    'message': 'ϛʐÅӈȱ˦ȞÿʴWĳΌͲČԕѿǷǝǉÀŷǎɗƪɉԆǽǭʤª',
                    'arguments': [
                            {
                                        'name': 'Жϊÿԧ5ǔӁBλɓяөΪͺEňҊbоÞ\x81Aʆ˦ЗҢҒԏҷҨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǑÉϩƗҵăćИЖʥ҅EԨʘϺǩԧȭÏЁʜˀϋѯe¨ǫЈ;Ԓ',
                                                                            'ċũЪ*ʤ¡ȿӎϨΏ»ľэѓʍȣӬΑѸѳų\x8e\x8dÓʴǞWƺŨŖ',
                                                                            'ƓÝȃ\x99ϫǅӈҳϮ\x87<ʅuγʤЇȴŷԄЎ2˺uӝԓϤƟ\x90ЁѮ',
                                                                            'ˢųɋɷ˨Ш¦ŊȼԐйɔʕϒϳȰ2mǓ˅ϾʍϘΌÍҪŋƀļ8',
                                                                            'ӽ˜\xadǇúȒmσԥÚ\x89űșƃѴġѪĊ|ʂˢԂ$tΰЗӭѷáƷ',
                                                                            'пȆ˯3ƠӻУ˴kɄ˲ÚԪȓÑʽΊkуˁŦҩŢƘёǍŻђȅŃ',
                                                                            'ҙϹУԤýԍ˴gè)σϠȦƲϸШċƕǄɻɩҥʟµ¡ǰӳƐКȽ',
                                                                            'ҊıөԇƷǗ\u0383ѨǮшҢЇ\x8dɼνȆGȠƽˢʩўƿԙǠ°dԞλ2',
                                                                            'ʡ˻Ѐ°ʫ9ʋίԙҴ\x8cͱîϪȐϤÇΊҝɩԧѵġƱʏȫѭЃ0Ģ',
                                                                            'ҍϡԀq˅´ҳ\x81ˆuɫŇ4˙sΨ´ё\\ғӌɪс_\xa0°ӐùӶƏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѥːƐˑ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6552536240271204917,
                                                    },
                                    },
                            {
                                        'name': 'şăĒЫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.464625:+0000',
                                                                            '20210208:212324.464636:+0000',
                                                                            '20210208:212324.464642:+0000',
                                                                            '20210208:212324.464648:+0000',
                                                                            '20210208:212324.464653:+0000',
                                                                            '20210208:212324.464659:+0000',
                                                                            '20210208:212324.464664:+0000',
                                                                            '20210208:212324.464669:+0000',
                                                                            '20210208:212324.464674:+0000',
                                                                            '20210208:212324.464679:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƿŭʮŵô',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǩҐȿˡЊԙԘњȅÃ¨ǵťȺb',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            176428.44588514208,
                                                                            55293.0102864909,
                                                                            188256.45991206792,
                                                                            190389.3042326559,
                                                                            673731.8054690367,
                                                                            986384.1901129005,
                                                                            178892.30939355807,
                                                                            683273.5176184044,
                                                                            174953.2406944366,
                                                                            952395.207659771,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĲɰÉӘҖȐςĂґƜβ9ӿĴ˦İȴ˜',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212324.465398:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ľȐҝk\x9fęĒĊ\xa0\u0382rǽºƸцБ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'δҙûҪѷαɊЮʲˍôϊннνҡƯҴϾiǕҨ"˘\u038bĔ§-ŻƆ',
                                                    },
                                    },
                            {
                                        'name': 'Кưҭ\x84ʎԖӣϜǤжȢǠӊǢǛȻӋɔ\x80ʰȼǊЂ\x99πÃԂ-Ʈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            174036.33917834476,
                                                                            604108.8903289274,
                                                                            510127.56619722384,
                                                                            586894.0439866459,
                                                                            570763.8709491186,
                                                                            456401.4575451191,
                                                                            232976.5378695762,
                                                                            803541.5135438662,
                                                                            627683.3946202956,
                                                                            347445.9884617173,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѿӯ%˟҇ɿè¢ШgЩȽӭЁëǽɧMdӽҖ\x8eȺ.\x9fơҎѣĂɭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5866606642937730608,
                                                    },
                                    },
                            {
                                        'name': 'xԁʸ¶ɞ,ȼ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9144963051437138556,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҽёùýԍɁβ˻ɾ΅ʏɏŖ\u0381ǋ\x8ec\u038dǍ^ѻϾǟēΦ9ǍĹ\x96ԑ',
                    'message': 'Ԩ˗ƖȁɶϨĶ\x9eϩɊӃȆˣňŌԮǟĴȈЋǼϼΆ\x96Ȝҿѕ\x97Ъ_',
                    'arguments': [
                            {
                                        'name': 'żԫĈϘήWĴʛʓѺūFĩҗ˖Ǔ°ɬʹƤ1\u038bǲ\u0382ѾɆÆŝРǞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3753654673237181210,
                                                    },
                                    },
                            {
                                        'name': 'ЮВĒѺӣԡiӌҋYЌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8055275367798618479,
                                                    },
                                    },
                            {
                                        'name': 'нźЗϢƦǌƩũӶƆӡǶOčĪԔȇŌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ËëԧϷ\x9aУśƛȢəʉхёӥÁ˟ϝŰɴɁѩ"҈ʕƖvѪ7ˠȝ',
                                                    },
                                    },
                            {
                                        'name': '`ŁñFɠØ\x9bӗΟΟǬƊȶÞԡˇȄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.467003:+0000',
                                                                            '20210208:212324.467014:+0000',
                                                                            '20210208:212324.467021:+0000',
                                                                            '20210208:212324.467027:+0000',
                                                                            '20210208:212324.467033:+0000',
                                                                            '20210208:212324.467038:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӅmѸѳ1ҐōӵƦ˫ҪүΩσǌ6ОȿςǴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӵȹϣÐӣȖνqáɺȊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            829464.1262175955,
                                                                            761593.5460646242,
                                                                            614627.3086465164,
                                                                            164557.5513083592,
                                                                            84793.55196345778,
                                                                            773114.701159447,
                                                                            466042.05426034366,
                                                                            -71228.18116586874,
                                                                            -4059.8238093085674,
                                                                            754185.5380273948,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Δ)ԏƆϵԥĽΩȑѰØɛҺӲɓȃȐΟ\x98ѻcĬ»B',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2342835153053019239,
                                                    },
                                    },
                            {
                                        'name': 'ơ»\x90ΤӜüϥǲá',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1815666716392792095,
                                                    },
                                    },
                            {
                                        'name': 'pã\x8bċGξˁŐõȮɎ-ʙ҈ʉԩ:ļɵŪЧɞʣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˭\u0381ԓΙłʱĩΑʀҧьӅϢϜӵΔÏԡĿºĻěŐԜΡÉΉĢӖχ',
                                                    },
                                    },
                            {
                                        'name': 'Rˬ˫ˬԈҏΠŒèƷƌȇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8240257906341994048,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ъʼж˵҉ǓƵͻ˫ǘ˪˲ˎȇɔb˻ӰÀƧ˫ҕŭͰŤĝԇ\x96ϡV',
                    'message': 'ϥҜľJȮǍ\x82ϭɰ{ŬɾǨԗËñгƷRǴɘΔӕ\u038bĶœʇýůЙ',
                    'arguments': [
                            {
                                        'name': 'đ˘˩ȲмƫŷΘrGϟiƟњʣϖϺ΅кŴșЖ\x89ԉǜˣhǻҔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            938416.3124590681,
                                                                            320894.86499129666,
                                                                            578470.3171240697,
                                                                            267900.28522310476,
                                                                            978350.5648388809,
                                                                            621002.0872338292,
                                                                            344142.89004922844,
                                                                            324504.79971809615,
                                                                            416637.48413356213,
                                                                            6826.498146463884,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Їʱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1300804344830201255,
                                                                            2334414864200589297,
                                                                            -5985373701575311999,
                                                                            3720877101837422148,
                                                                            -1959963451242787068,
                                                                            -6719478452648101095,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x96',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ÀԮÌԘԫɴƦȔξԟͱӄţőɎeΤʕēˢðɛŖљƾτĦµӴǱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.469233:+0000',
                                                                            '20210208:212324.469245:+0000',
                                                                            '20210208:212324.469251:+0000',
                                                                            '20210208:212324.469256:+0000',
                                                                            '20210208:212324.469261:+0000',
                                                                            '20210208:212324.469265:+0000',
                                                                            '20210208:212324.469270:+0000',
                                                                            '20210208:212324.469274:+0000',
                                                                            '20210208:212324.469279:+0000',
                                                                            '20210208:212324.469283:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɫʉĄ{Ѽ\x86ԦҺʜӻғ4ϊƹǂԙƚªĒ¹Ȯ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʸɗʜİŠőȏκAȰġĨЈɖћ\x86ԈҽʞӬġЈɮӔƄɃӌʔüĹ',
                                                    },
                                    },
                            {
                                        'name': 'ŎȍĪˁȌƄΨѥ\u0381\x94ȓɿʒȯëøҜ˚tΨή\x8eŞϊƯǅΡėξѧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.469657:+0000',
                                                                            '20210208:212324.469666:+0000',
                                                                            '20210208:212324.469671:+0000',
                                                                            '20210208:212324.469676:+0000',
                                                                            '20210208:212324.469681:+0000',
                                                                            '20210208:212324.469685:+0000',
                                                                            '20210208:212324.469690:+0000',
                                                                            '20210208:212324.469694:+0000',
                                                                            '20210208:212324.469699:+0000',
                                                                            '20210208:212324.469703:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЏɋĘƵƈȧӇÚӽ҅ʖӗϨѼĶмǰΐўԡıɲӯέF\x8aΨĀҝя',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6214233743877927641,
                                                    },
                                    },
                            {
                                        'name': 'ƴ ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȴӱǋǠЬɈЋӻяƨŃɳȚϵӳǽˍʥϥ\x8b¯%Ϧfəȱť\x98ʖЬ',
                                                    },
                                    },
                            {
                                        'name': "ǩʐϨ\x9e˵ʻˏ˳фТŖΦɮ'ʮǆĿȬ˲`ӇԬΝ~҆Ȟ\x8a\x83ԧς",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.470193:+0000',
                                                                            '20210208:212324.470202:+0000',
                                                                            '20210208:212324.470208:+0000',
                                                                            '20210208:212324.470213:+0000',
                                                                            '20210208:212324.470217:+0000',
                                                                            '20210208:212324.470222:+0000',
                                                                            '20210208:212324.470226:+0000',
                                                                            '20210208:212324.470231:+0000',
                                                                            '20210208:212324.470235:+0000',
                                                                            '20210208:212324.470240:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'іúɉИ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѡ\x91ƊLύԅӜʩ҄ӫϫ´ĀŞóȶƃʔêƭĈ)˩ѡɭƅБȇLf',
                                                                            '\x9cũͺӒβɮǲϻʖÿс҄ɑʍɪ¥ĄǦεŽӹĒŻĮӀɝ_hƣɢ',
                                                                            'ʗɱ\x86Π˄ΰӠĲϭÀz˧\x86)ČγƵ®ϖȣ\x8a˟СҎčƊϔʍǾȱ',
                                                                            'žғɌĘҕ§ȳѓҸ\x8dӁʻЇĻǋˡƢΰßηʕÎԝйҤāʳŎǪΟ',
                                                                            'ĹĄđ\x8fѐȂȶŷЂVƶǒɟЮ˫ǉþ±Ǻӯλȡ%±ĪОīԫ˨Ќ',
                                                                            'NбΚЗēϢӂΈ\x8fѹԎΥ҇ˣɓǅȷžŠУԗΚŠӫγȁJӄ˟ø',
                                                                            'ςгĩ˝ҒǛʹIBqɓìŐқϼӆÓʚβdīƢǁƼƂʊ˚#~I',
                                                                            'ʊfʃɉŲòèџϏϑэȑҺ\x96тʅƹ\x94\x91cԠĻωÎЮÐ˒Ԏąʍ',
                                                                            "\x88σf˝ԀϧǼ;ȟьϼľϒϝ\x8eԘǞʲù'ĐˮͷĿѵӣѕɡХѶ",
                                                                            'ʍЃвӔʭǁЂɏ˻Ǿ˄`Ǯ·Ǻʄɤʔÿͼӿԃţś˗ǑˮόԬ˔',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΟʎӪƆɲН£ŹʽЃ «Ġ\x9b΅Ϳ¥ʚĆǋӮͽɫhОȪ\x9eOҿź',
                    'message': 'ӴӗΤчӪѻˆϭȔӧ˱OѕщșÕʬɯȍìɼM¢Ɩˆ%ԔђȨԩ',
                    'arguments': [
                            {
                                        'name': '\x94ʜźȠǶÅԄ=\x85ʨѵǇѡҝΏɲð˚ҰŻΜʜҕӁʹƦ)Ì#ʜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212324.471257:+0000',
                                                                            '20210208:212324.471269:+0000',
                                                                            '20210208:212324.471276:+0000',
                                                                            '20210208:212324.471282:+0000',
                                                                            '20210208:212324.471287:+0000',
                                                                            '20210208:212324.471292:+0000',
                                                                            '20210208:212324.471297:+0000',
                                                                            '20210208:212324.471302:+0000',
                                                                            '20210208:212324.471307:+0000',
                                                                            '20210208:212324.471312:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÏЗϫњ¡ІԫĲԎӛSԖƜ\x9fɪŴ\x98ːQԠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1263462660754370425,
                                                                            2271384272437829426,
                                                                            -5631414279462339344,
                                                                            1013697120320958069,
                                                                            -2612843838296056985,
                                                                            -3371897938346545565,
                                                                            147444800491821092,
                                                                            7889877521528823299,
                                                                            5562539783353869529,
                                                                            420142730639796105,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԢĳИӥӈ³+δĦŃȶθ£5ɺȔɂȊȉˣÔѳӠϺhĘРİ¦ϼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϊҦʊƭȳˡѦĨȐqāċĚôҮƳрVΒ.Ҷƃ͵Ӟͱ8ɔfZʱ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 299590.3425668112,
                                                    },
                                    },
                            {
                                        'name': 'ŔԊYρļ)ĪǓξͺР˔ҐЕŘϼғŷK',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԎƐƱ"%ұҎԗΛ-вʻɹŠêƪšѠӂђ#ʠЂȒ-\u0383\x8bѴŨУ',
                                                                            'ȃǧīЙҋ\x84ԙŘɫǚϹjÅӑ\x95\x9cȽȱёĂ?ɛń¶ʙͺʇȔɗѾ',
                                                                            'ɍʔƦѰϊҹÒ=ԈîŗґύӲɠŲѬЩøčӀʹ˙˅ȵȰѴÊΈ;',
                                                                            'ȥˉ\u0379ʈɰĘ\x85ϒșΐҶґƄƍǓԔƁ¼ǃɖƹŗзϨ{vƟͺȉʥ',
                                                                            'āЪ÷Їľ\x8f#҅ӄɒ˒£6ЃĵƒΙ˄ǬШƳʥȘķŹәĸɀѱƌ',
                                                                            'Ājӏ\x9fŇ\x83Ҙъ҅ʟSϲłΣƭϠʹS˕ЗȐZ\x9bȰŦȾӤΤӐϻ',
                                                                            'ӷʎӌʇѷɿΘԫӽȥiЀҢŢ@ƿЗ#ЍɩʤЫˊþʗɛϛƼ\x9fǙ',
                                                                            'ǣƪÑǯʑͰİϴ˴\x81˜Ӏмν˙éâҥ҇%ɷǶɞ\x8aţƁӎȆǸʄ',
                                                                            'ͰˆвЁũƕĨʱˋƉǃԇόȀǢĨȶЫҢµʽƫŘҔѣ˒ɑȵӫӚ',
                                                                            'ɏǢЮιͽӘԡҫɍǡҰ\x9bóĂʾũ{\u038bǑƴǘ˧ЁǗč }ɰʾʚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˢ4+ΫŪŪΘčğѼԋù÷ɽĉɼɑπӗжžҍ³',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͼӑӹӮ϶ϛϭЀƩÃ©Ýǽh\u03a2υӎμ¾ƾԐтǥˤˮӋƯѦȶå',
                                                                            'ʺʵʀŁǌЏѤЏĬÝϛͻ(`\x9c]ôҿҬȗϸϚɐѿʶӶìĞƳȁ',
                                                                            'ƏęȽƺзӉǑŢθƼ]ԏӖ&.ƦΈťĩɠɧ\x80Ҏφ[1эɍҋƥ',
                                                                            "ԑɓȭϻҜSǆȫøΰ\x8aѶȚħԍѰτĂɨʗɅüRŜӅ'\x97BԮɀ",
                                                                            'FʈΦАĀӡ¾\x89ĐЦӺƒӐŋӞʜɂƞųɢΠȋΪʫɫɻԙҸұǺ',
                                                                            'ɠѶэЉǵ\x8aΧӅ%ОʌɭɧЄҮċ\x9fӺӛɃ\x89ËƟѝƄŤԡǚҁʤ',
                                                                            'ʓŨôȲȽǈǝΛł%ȨǁdѥœӄɤˏʻҤʰ˄ķѷȶŤ\x8fǨπƌ',
                                                                            'ƬοͶƾӺ\x88ǚƮȿÍΘS\u0383ԂƩβ˯\u0380ɞƧӓĚҗǼΫӒ/Ƿǜ0',
                                                                            'ƼŗͻȜʦԗѷˈэøĪ˽ĘӟȠӈѝęϗ®JöȮũў˓.ƤфÐ',
                                                                            'ƨ·ƍͷХиīџ҆ЛϥȱΗʀ\x82Ɖ˝Мϕϝџʑ\x93/āȖȍ\x81ҽΦ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ūƥ\x9eσӦ˰îœŗʆȲʑöԝUǔҮûʨϩԖŨƫԪǛ·aйŢȾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3344295793456029251,
                                                    },
                                    },
                            {
                                        'name': '\u0379CФÓǃЧӓиʴp',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŢŃȡБ\x8fѹΏǳͼΛ҂ǋǓЄ±ťȯΈɭɾǽȂԍϓηѳ}§vŰ',
                                                    },
                                    },
                            {
                                        'name': 'Ŭϭ˫\u038bœTʍʲ\x81ţӀѴыʠĹƩȴҿ"ͶȱԃυϑʐȦϥȁ ȋ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Δġ\x9c˰Ƒ!ҖȓuӘ\x93ʤĀӰʢЄŁñϗʚϕǍɊҎőÈυɳɑҎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 922104.3503311877,
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

            'identifier': 'şźʎɇ\x99',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': 'ȏØ',
                    'message': 'ə',
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
                'identifier': 'ϮɚǢɛñӘŪŋÅ˻Ӳи7ғѽɛяfȍӊ҅ʮ®ǹҖϗϞńъ҇',
                'categories': [
                    'configuration',
                    'internal',
                    'os',
                    'network',
                    'os',
                    'network',
                    'network',
                    'internal',
                    'os',
                    'configuration',
                ],
                'source': 'ҡѬѳ\x91ãâİ4\u0382ϻȚуŵȄŐʶ˫>3Õȍ˴ƸȧʻσЖӗγԦ',
                'messages': [
                    {
                            'catalog': 'щзһǫȗ3ǲӴκ*˸ϊĿýҏҠ΅ƽʐɯӀĎ\x80ɳɪԇѹΧѺĴ',
                            'message': 'ǖjȀҝмо\x9d>҅ХәÿǱӽϟ+ɢφђ÷lʒɏŘ˱ȲʇĆÔĎ',
                            'arguments': [
                                        {
                                                        'name': 'ԢƓɥҿįƥİϑιűρÍżǊԣġҩèƍ\x80ǁҵϠȵ-Ƨѧǹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'џ˙ǵƘʹ±чǳΚ\x9ah_ʱîȥѻұσƵζТѓхҖɗmʧƽмŵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃӦʠрk]ҥȲͷs҈ŋΚŬěбѵҕʐӱıԮϺϽԩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɰƻŘӌӠИαˁċòɾӑȳξƖң#иϤԃɎɏɰșȂҵ\xa0ȖϼȐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋ˶ȷʉБΫĥǈPԂеJͼ¹ЋWжĮʥҊԗҍӜ®ęŅMƇːӎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ïɳϝԈ®ң ŦǼѼ<ĸʯԞ&ΘķάƈƼѦīƉь',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1153603345143876672,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĽɜӑΆѬɪ˒\x87\\ȧɏʓϔώʠă',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 749640.3133954311,
                                                                        },
                                                    },
                                        {
                                                        'name': '.ǒӷќǨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'йҦĐЃ9mˈІȢÄϓȘȣιȘâ^еΫ£Λζːğ\x86gũ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʗŊӨӉƮӜȳѣʊɘϾªԭӀЅΦȃФϬIɍϔɴϲбvνЗƏ\xa0',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƐϗȨɶɡӓйͳǩΦş\x99Ȃ˯ҔǆӭÁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŉKçȒŮйɬњˑʫĪɄӣíǩҮ˳&V˘W˕˵όW\xa0pɡǝ(',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ċ³ǪǮȒҪӫ˫ΤŨĶӠʌòÝɻΖчĳ\x92/ƚīΊŊњƏǒ¨Ù',
                            'message': 'ǪÑϞ΅ϺԄә¦ȓĬҺȧӒҮëΖέʇʆĶǽʽqɲѧΰˋϘëƣ',
                            'arguments': [
                                        {
                                                        'name': '҂ΐĊӮ͵ȱ\x86ЙԅѺʺȂ}ѤýΑÉƑ\x99˃х^ҠϑӧƽȎͽӯь',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӑ\x91ř\u0381ʭăåˏІŉǻȼӟԘʻƯίγԫ˩ðԓнEϖǠō\u0382.ԗ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȣʀɘÝĴǩċʻΕȧȁȤϳüȐӾЧʖԘʲřӚʩЪѡǕˑ<фƨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʏӲԊϣӽ˧oŏ~ҙˈçϸϊˈίŭÀҘá4ҞâȬзљΘф',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3457086614362786881,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁ8ǏʈεŚνХ.ūΠȲЎʂŨӰȐˡљ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȡӢʃηȷƊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺxƚʬ¥ĢE',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 917688.6385933657,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁǜȺ҅p¼',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŢɧÔϑ%Ӛʇǰaͼ˩Ɗȫāό9Ρiӑǚһơ˧ɣǇ«нțƲƪ',
                                                                        },
                                                    },
                                        {
                                                        'name': '{ňűǥûȲµˏοфǑɧȕԍXǗӲΨӫЫȯʢĄČӞĐɗϘˈȓ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.432514:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '^˽ʚɯ¾˽>ǰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΚVȾǈǵӛҠԍЇ\u0379ѽĨoǳhĶěϕ\x98њǥɪ4Өɸķ\x8bΜĒ¡',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԅԃΥӷÔǖШǭÎȪʠťţОωϖҙɻƅԁϩϷűȷȲȃǤɨɆС',
                            'message': 'ԖԍҍØȵǥ˹ɘ\x8d±ÂЫηеΗęΜɡĿӹӾїġ¢\u0381ԅ\x86-ӗЁ',
                            'arguments': [
                                        {
                                                        'name': 'ҭˀѣàŭŎđѹӡUĮƒШȖƏų˽ʹ!3ӯѿԪ\x9fЌ\x9cĠȔuϲ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҥđЦΕC}τЍ\x9fӑˬЩʁɔԕǽ¡Ϩ¿ƪ\x9dԋƋӸçȺnУɟƀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 183487.67115931516,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȌКě.ěԔʉдϞȹ˭ЩѿΫȤϩʸԖъəμɑŲ`ɻБҖќӘǼ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɍ£ѧ8ą1ŬŧÅҦoҸΖ˝to˅ҠϛƲşáʦԎ\x92ɠҪ^ȈϪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴʻ§ɟ\x9aҀǚlԪǦdĄʡUοɪǃЃɸȂʡeιԊѠɑtίñǁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'şɳԕԟъÖȢƲҬŢ-ÒɖΧȐԚŰΧԭʛҦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -925303051592213593,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԗȡӔǸ«ǆȳ˦ɆӼΟΛӿ»Ǔ\x8aŘӇӔǫʥԕϭϭưΪϟ҃əЅ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.434014:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '_ӅÎäʹʽǆȓǦОÝȥή-ΣÆǔӍŷҠʒĻԮɕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3740299341526150296,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴӏѮљû,ȝӞ\u0380ΆĩӢӝǔɼѓǪҎйǟԣɃǘWѴΪ˅ѱзЧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ыȉiO2țɭ҆Ң;Ĥ\x81ěȿά˷·бƤûцЏϺԃŉîÐϭ\u038dŹ',
                            'message': 'Ԁʈ\\ʖǡŁȣȖж˴ưÉǐӂȋɰʘʸmΉįɼcӻˎҏ҈ʾĦʤ',
                            'arguments': [
                                        {
                                                        'name': '´Қ҈ĮŢұcǈϱԙlΑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '_BʥҼѣ1ŗȑƮяǦŽƲ˙ǦɛɏŘȌøʨʜňҩԕʤȠȞãç',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 3852.8539838825236,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0378F\x99ƅΧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯȑğĨȐōϱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΔûǌѠ˕Ԅӣϵʉˌƛӝѝ¤ШǦӯĂ˖ȿКԡϗȱѷȔуԭΫд',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʗıҢҪ¸ϩ¶˄ɵː\x93ҪşʪƴӪǐŪŞǚ·ȥнΫʼȘԂƫҧȩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƺϬˁë\x99ы\x8bƊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "˯ȡӛбҴʹϹÿͰŜ'ӕñÖѷuЈȵȆŇ\u0382ʿȎǙ\x9bѬģΖpƿ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӫȨȏг',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĨĉѭƗыѐһƒ?Јӂ˚ßƙʣʱͲӅЍ<˖˛\x95ԚйÄɪ#ҁK',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÛͺŅʖόñśģʻǗӸԓ\u0381Щӷľ\u038bԙϷȌ%Ɩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ƚҁ',
                            'message': 'ȶŉʆǈ˹ˍˢʚҝˮι4\x9fʛŁɦӣƻȠDʐʎ\x84ŇĚљҩΤ"×',
                            'arguments': [
                                        {
                                                        'name': 'ӭ\x92ӝЌc˃¶Ĵˣл¬КǪ¤ƾϟ҇ɺŗ$џӯψ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'iǶĔ\x8bǫȴͶ˛ĺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƬϤʯŬȩϿʷҭπʁ˱¥\u038b\u03a2§Ǖϕ˱ȸԐT˵S',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.437072:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȊnțȵȺp˦ӄ^Ɓƈ\x9f%Νй\x89ӧҥŮĭѥҊėҸưѸŎ˟ƙÛ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4792874273426961229,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˈΣăϱ҈үɇĮș\x7fА\u03a2ҏŜ¼ӪӕŠʬҴ+·ˏƃΖĪ8ԛūȁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҁ\u0381ҖĂ\x94ӕˁƂɊФ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 87884.90253010893,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŨÄ\x9fӍάǶǯЌ҂ІƵĵɻʪĭȉė',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҀʆЫ3ƸǝƾȎԮ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '|ϩĄǞϓǖɅȒξԣщʤĚԉǯс\x81ÔĒΛźƍϷÖƛ\x88ϊ«ʏe',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȺĲșџĴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ϫ1ĠϫCʫԗԫdǯќǵԓʴЉɣʖǮ',
                            'message': 'ІϚǟɯȔԉɵЁʈ˙ΥѼǋˡʞųβČϭͽɴZŪώМāq19ű',
                            'arguments': [
                                        {
                                                        'name': 'ǯʘJΦXʍɣĳΏƱ˾',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÜԆÔĶȀ<ƣɒı\x8eʫƱǆɩ\x90ΒȵǅȍĵHҕĸӚǫ?ŧӷνt',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '9ƌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĈbȧŘÑҪӧ\xadȽԍ\x7f97ґhàÂǷӪԀɭɷЊxѨ\x98ϑ\x84úò',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'џŏS¿;ҲѬǊȷΨ΅ӰǯώЭUÊΟɠ҆ЉΚϸїƘƉԍͿԋǙ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.439148:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҎɧɼǙȪʈNʛс\x9ačÅЃųŦɫʍŀ\x83ϔɋȝɊѦҕцө\x83ҐŅ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȁèƏСĹîʼʐΚҬΠϏɆηβӢШӐƨ\x8fêƜǖ˪Ԝȏ\x8aΐҷщ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΓѰͳЩБŅ˵ЉоӼąȞƒҔɿ҉єwь·ª\x94ѾԦǢˣ˚ũƁи',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.439604:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0378ӗ\u03a2ˁС=ȉˋʋƞǍˠԅԄӺǖ5ȆúÎ\x9aĢDɭȷѠԎųÞΫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3334263069133916148,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ήϡƨΉˊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5083264318324164299,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'žɍşɯľɧ\x89ʆѿʠƥȾѢŘʈҼĂ/ȅɺļΈgȽǷϚӎӱŃΣ',
                            'message': 'љǋ˷ǌΝƽҒҝЧŁӦʍҘöʠȩϪԔǲǫǌӚďͶȱҁɿҰũϪ',
                            'arguments': [
                                        {
                                                        'name': 'ϲȈҊżʸӴБ/ӑÐÏȘҤ˄ʭźĖӥʯ\x8fÚεÿӏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȕĤљӦәȰҖζƸΚ°юȞʾɀɇ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѲǩŁÜƍʣĉϰƣ,ӗΘąǩѲӦːˀ˙зʽ҆ȸ^ː˻Ϊľòɷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ùțѦԁȞĖфϤɃåǠV',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŬȮΞШĩԔз\u0381ѐ҇ʷџпɵҲҍǉǃ2Ţǌб˒\x8eНáќχʹψ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅŏͶĪҰӄɗǖӾɃϕǥӝÞĸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.440973:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'γˣHƐʹΓƣϝȓęԔǒӀħЄΆīʶ˾јɳΗMԌ¥ѹűϗœД',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'сˉȁѻǷ˂ŀӯ×ƿGԁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 354717.43634204095,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҡ°ʝƉԏBψŃUςŖӯæӉәϥʬȱˆȎЕŭçƗυ8ʈҲȱѻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "ΡĆ҅ϿͿёӒ¹Ưѱԕţ'ƈȩ`ѰӪà¢\x8aĎ\x98Ҫљěϑȯ\x9dΣ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԡДǯǟȥƻ\x90ƑĨŽԌƐ\x8eÿбҧ\x8fŪ',
                            'message': '˛ӢIǕґϲҜϦƴŨȂĈǏӭԮ\u0380ÛoɘÓȬ\x8aÁˋʳ˾ңȼ˙Ƚ',
                            'arguments': [
                                        {
                                                        'name': '#\u0381ƞʋʧ҂ƥϊϩ*ӏÇѕǘ<ɛӝǜҹȟ>Ą˶ā',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7341196631399625618,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ąǊɎцĆΫ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǽȸ\x81ŕžԐʛDȦ`μǦүҮе˷ĜɯҵÕӑԑȝђqɶяȾɶЉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɈѝӪÎȟŹяήɽѣΦ9ɼȩ°ƘΒȌǇŴ\u0383Ϝѹюӡʊѫƨρˌ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'gϏИѭÌЃє6˼ϥϤŉ͵;ƓϰĶ˛˖ý¹ҔĻċϣӪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 792753.2205597518,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƼȅѴԒ·Ϭӛϛųжī˙˽ǯġƛŶŐ˯Ǧ\x8dϵΌɦîΐЄЂǗƑ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '*Ί\x7fίǅȈƭЛЀʱҫϿңЄƵȡλӟЮо˨OɛҦȄŠϓŦã\x95',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'jˑćӗǙƶуɮƵĖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 881922.0117987085,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊˡ5éӀβ˻èʁ\x98ʫ·ͺе˻Ƞǜ8ύƫμťgͿŽӸƅDиӺ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӶŠˎӨˈJʾϱæȕőɑŴāʐQǔҵ¡ϺƋȓѷѮԩяˋǟƋú',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 983467.3336353574,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϝɊȚGƬƏ:«ǖΥʵȦɷԁк˯¥ΏѿǫԃɬFЙʭɭŰeŪ&',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8119870715041160516,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ƈҷ-ƺΣPԖƔќǦǹ\u0381ӴΌ˪ǉνέӟùʱƙƈӃѽВєķĸе',
                            'message': 'ĳЋϽžʬźԧƻӸҌАųӬԅƱѨÂǭÜщÍȭәɿ\x99˘˝ϝÍҮ',
                            'arguments': [
                                        {
                                                        'name': 'ƒƂȝÑģҐƣIɗːԤbӛȣmĳǻә¿ҩā˘ǣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 423824610199772953,
                                                                        },
                                                    },
                                        {
                                                        'name': 'өβϡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'λ^ҎϤҞƞѽǆɴ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8508831124015046234,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Đǰθ\x91Ξ˴ʧÙˣʘΨϏŻ¢т\x90ŏ˒\x9dƯɲҍÍӼ\u0381ӥƶќjҁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŃĈƇɦƸ˟ԑʡҐ¡ȑϊȌɔÀуІFɗҳǞƱØˀӂӀϐѽ>Ϲ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɁƼшԘʶ(ŝȣXŵԞÒgɾɑÿӭΝƿҎϠў×ȰɶӹŸδԠЉ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˾˱ˁɟˊÌĐԑÎӳΦƴŨ˰Пϐƛąźɨ˵ϛ҃ѭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ÿ2ӝȎc\x96ñǰ\xadӶΕ8\x85яԪčŢέϺˍžЂǨΤɂ˂ϳŅŹː',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎΩėƅʏĬӋЁ\xa0һVҮ\x9b˅ϟƣΧğǟʧ\x95Ũ×Ĥˀ$ɩʓíʏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2826154592408178280,
                                                                        },
                                                    },
                                        {
                                                        'name': ' Ӹùǁɭ˭ѷθҶˀԄѨȊԧǜƂЦѣК˙ơƞΑ˼āѫʅǯ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.445183:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȧˀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҭҲħХɎ˗ҸӨąʳŜŔƵ˻ВђхƙʣnτҠĖ)Ғ¥sȁŇё',
                            'message': 'ͳʢ˄źAqǱ¹åӑBϐӗнȫƓкҏĬΥ҉ӠžĠƐНƏҰˍ1',
                            'arguments': [
                                        {
                                                        'name': 'ɶy˱1ʱӕƧ\\ɮ҄ȃɞƫ±Ѝ-ǈǸͶѶǺϗųΙ1ЃӄƾWM',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЪşƜ³ԁθ\x87]Ӂ҈ĥȀϙƯĽĀ˦ǕʟŁİ:ϢүԄmΦːΚӃ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӣʪXºÇ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʮÀȎʭѠȺĴȁԪȘ¨\x90ԝήǼ˾ϨΌԧɦŘȈʐĪ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.446298:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҊȞΨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5851356446893783311,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚȪǗӏHїԄȳϲʡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȱ6ŚӔԫʝ\u0383ŋåŸŷěҦŴčτwҪǗ7ƗǗɫɭħǯȞ˜',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '±%ĀϡΕάԌɏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǰòƫӄʤɸˊ˪Ⱦ΄ȎȠ»ϒɖ\x96]©ʩΫήǸÄ\x96ǧҧЪȝ˾ɮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 411220.1146650758,
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
                'identifier': '˨ʗΓɲˢ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ϊϢ',
                            'message': '»',
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
                'identifier': 'ҧȜҴʝӔȁЦĐΨŨǠλʙΚԦɯƽƆǍȔӃāѤӌѦčԄɮэĲ',
                'categories': [
                    'os',
                    'configuration',
                    'os',
                    'file',
                    'internal',
                    'os',
                    'os',
                    'file',
                    'file',
                    'network',
                ],
                'source': 'Ӯ Íɍ\x9d˾ŝɈҔ˕Ҙ˯Ǩȡ®ρΤʦǯѓʓӌ*ӖΎǣ?Ά@Ӛ',
                'messages': [
                    {
                            'catalog': 'ͶűĵѫƯ\x95ŨɑΟϻGɨӡЕɮħӥϬӼ6ҘΤǐņāǈԠχˏØ',
                            'message': 'ˎ\xadʫҚĚȝ¾ʩ҉ƜДǃʏʉǎхҌƫ҇δҒеϴҾϓ˴ƓҔǆȲ',
                            'arguments': [
                                        {
                                                        'name': 'ԦͼхeԂĀŝƤȹυѩˆȤĶҘǯɟʹ;Ɠљӂө\x88ӖѐǊѮ«ƒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮԢʐǽҧ.ͳǥԔǼҧЅԉϴʛ\x87·ĄèŴϕԕǩïӲ\x88˦>ӟ_',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4881200768484647718,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӬΑМө\x86İŲŗʜʖʾѭпѸųМΔ×ˍŮ˛ιɲɗӞΊĬΝƕЏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x91ȫƅiɆ!ƈ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.475866:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴһȫѐΛȹǹʴɔʾĮȿҾœ˜ιƶĪƉ˫ԁ˝ʨѩтeɋғϣȗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 748935.2925096608,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ы˒&ſɍȲ}Ȁ˦\x90ȄǧϗԤȭОĔǫtď҅ΊLʥøΎӍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҅ȀƕϒèƂ϶MȩҵƢʪɾɞǎΎľʨ×ɲҷØŦͱȢqEзqЎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -17718.813702471467,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0380ϤЁ\u0380giȺΟśЇ˕',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЃŕŔԌίѥԆҞü҇ӸΰHɑ\u0380ΐōӱəѼԜƏɎē',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹ˴ФʒːŮƷӏΙƶԥΎâЯ\x90y',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x85Üӧw<À¤ʙʛɓfʈҼЦΏ\u0379ƀƙШ҈ƽ˶ğɁԁɳĆӒǌȑ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѡWϺȼҪêӤэíЋԜȟΈʙĿ˩zu˘ĚʉήƦɑîüФʄϣΟ',
                            'message': 'εƫǫӼ˨ÕҭҀ#͵Ɵ\xa0ˌϺРѶƒѩȼΨ\u038dƏӟЛȢľưρӤЛ',
                            'arguments': [
                                        {
                                                        'name': 'ů\u0383ƺӮɴѨΚʹÖ%ɼˁӱ¼',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'һģʇЍӒūǄWÝЉǮ>[ԣѨеŐзѺǇ´ń',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂѣЫĈ˗ЭñǀˡˍЖӋȎƚд',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɊĕчǮġƄă˞ԕԁЅĚһ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸ӕĈƛżƿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'сҧƝź˻Vɢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸҵ,ӫΚ˖Ԃȁљȫԍė',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԚȰЈŧ5úƬȜ.ɻѨ˷ğŜЙɊÕʷČƍͽƑοōҏŧã҆Αǅ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǦŝыāȑȀΒĊ»κ_;ȓφƮәƤç˾ɺϬ\u0381±Ϫ\x96Фʫ³ĈԬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҮҲ@цʵíɍѷɦȼђ6˻Ʒҫ˨ԣΦ6ʯ˂ŕʏҕ\x8aRʔS\x8bˏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƊʳÑҮæ˦EҨƙȻĨǯǈėϨaʿaЊdр',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĩЕê±lϕӖOӡʋ˙;¾ɭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '!гɑ&иәkӴхŃ˝ԛȠϖΕ\x82Lξ\x96ϬƝʌЅԏӪ\x85ýѱϿȒ',
                            'message': 'ŧѡŽ?ʰ\x8eƑȏĂȎ\x99ʐŅŋЅƈќϱǕŮÉűřҚһØ!SӦN',
                            'arguments': [
                                        {
                                                        'name': 'ņ®Έ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѻ\x9cȉӆœ\\ɄĔĩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.479083:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϟԀξЛӒúНӝЕƃȚʜŚ]-ɉŸòɫƿtȄқʊɻҳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 769552.4959435132,
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ԒϖǕƧêКɉĔή\x8dΣҔӛĢұƺͼ1Ŏʢ95aӦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'џюԍɃ:3҆ɪϨƂĠΣ˓Ƃ˓ӾǜǊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8c\u03a2ĶƩĀ|c¦ƮӪλ\x96ȼɤЋâӹΎÔCҥɤɲˊƌÎρ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.479661:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʠþo',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'V',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.479893:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӨӉŷ¸ȷŊ\x8dƢ\u0379єŦӄλʜӸАɃóӂW\x8cʅ\u03a2ɗɐҖªΤůÙ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.480026:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠɼȑȉҮϦҽďů?Öƴ¸ʎȯʊƜŶͷσȮӕɺѕ˸˥šˉȝ˄',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɳŚƯ.ɮˮѠҖўʯҌþl \x8bǲǓîȒϣΩȧҗȮуȝsÍƗ\xad',
                            'message': '˕цˡJ;Ŀɧ"ьԏȃĺkȄˎάоҮƥҮƊʬІƍÒȂԟϓҭ˶',
                            'arguments': [
                                        {
                                                        'name': 'ȻͱЊȫTØƑōіȾ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝ˟ԏÞЏƇǭҚϡϓҶ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'όOǳ\x8fϪѠǷԋ͵ʋ˙ήξΦӗĪɏǇɌˏҤk˝Ĉ˦xψʠìԚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ºǈ#ĝԠʡÙ±ȡûǎŨɩҏǃ?ԋз',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7042684029945681493,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x95˽\x8a%àȷoǄӆΉԃ¨Ͼ˹ų˯ƅѼƀӟоǯќƩЗˬϰɵ\xa0e',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -19609.851916153246,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӣğǜϫ˘ҹʌMΔω\x98ąе',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -321990104643113931,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЗǬ}ʂЯȿÒ˰ȱƬɒωӭŐѺƠΩâͱǓӅӱЊЏΙ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.481363:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɼΫŤӑǹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ļ?Ͱԗƅ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҬȽ|ԟǓϪȩˋŘ˜ȎƖǛɽ\xa0ÊɒџʳĝһЋϊªŹ`ǁÇ]Ƌ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĆωɼԊƑүзϲ)ƻû˘ʗʋƟɈLӥҸӊϱǆʇüǺǝ.ӍʒҴ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʃɣжɟǍƿРԃĢȸґȥŎβʥʲˮƊʑtʎԥȯ\x8eΛĕЭv$Ȼ',
                            'message': 'ӚǸĚɞ¼ĿӆӁʹŷĹаXDŬěӒϸɔƉŅtʉșĨʯтғœė',
                            'arguments': [
                                        {
                                                        'name': 'ҳΰѸϡɚŢɰҀȔɊŗăȄʮ˽ÿ\x95ȳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1333112732804323321,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŭƠƚӍ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξғƎҠƩǖȖΪˢȦO\x8dɧ\x8dFɏʪθǳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 498548.1177313799,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɤбɝĚ˱ªƘȌǼԟ˾ӽϽЪŤ¡˘ħˁɳâӧЬșȻÎӏ¢ƋϠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 828049.3922794628,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȨӘˎąϣπǃΥƶҚѨҒ*ǿËƠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'LǍCҞ˶ʂϿзҩșǬΡ˞\x96ωëȃ$ͷª{=Żӆԇϵ Ǣ!˟',
                                                                        },
                                                    },
                                        {
                                                        'name': 'A^ĩŉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵΜΣȐҍ¬ТÞO\x89ǾҜҥɻϤдˡɹƊ\x9cƩɵȖÕ`ƍӳϫ°Ε',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'μǏÊǬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0383іΜиӖıϩɽϱӍηҏɀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 295924.9729907726,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҳŴZǧйÚϫʺˢŘǙȓ[ȾƐнΰƩ˴ʎβѷğt¤ˑK¾ѹ\x8d',
                            'message': 'ӾYҟҫ:\x93ԀϺ\x80Àȱԕ·ϛсŘ4ŤĞCѺͳ˨φϘ+ҳpɴä',
                            'arguments': [
                                        {
                                                        'name': '΅њѧč}ȁĝӰЯƿИʯҁƻψŬ˔ǠέΉtMӏϟăű',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '.ǋԏŶɏJǺЇϱƩөΩ~ӴʁǨΩ\x8dͲΜԀ˒ЂѪ¼;ǆȓΟШ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȱǃ\x83Ϲ˫ƃŞʰΏ§ĹĐYʚԤƣÃ\x98ǇШőρvԒŴԀͽÒѢɝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '`ŭcCɱŧԊҾ,\x9eʧҐƫАӛϦщҡАIëƴеѹiƖӱ˯Ǥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʹĤȴǳǅŔтϊŬzг˝ȱϷƞõΆš˂łИØȺēѹǥLĞA¼',
                                                                        },
                                                    },
                                        {
                                                        'name': 'v,\x9eӒȐ ˮБѰԪп҄ƾѻҋɚ˒ЭŝɏOҖѡÜ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹԅɌC.ĨŦ˧ĳʯàԣxĶЋԆѐ)ĈřŭġҍĨĹґѳxΌɢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ëǋϣӹȰǇšъϾļ\x90Tӣȕʵƌ®ˮѧӅЍɻȎѨͿķ?Ԑȑĳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Й@ɦ҈ƙĈƼИʙҧxϗӜ¢ԛѸūӸǷϒѰĜʹ³ɍŁӸɎʷǗ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'řŵɁʒɼͰǥȿĕҋϫ±ĥʪϭşӊÊ˓ņ<˓ϒԦŝĬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5987922442220743962,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86\x98ǸøłͱѠÎԫĿ_ƫˀƛˁ"ŉƼҋЬҥƭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¿\u0381ŠĻ)ѿRɾ҅˸®˪ĬƬΑʕӎҳǍ˫®ʌǪѱβ9Δʡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÒŘƔҤгǚʟŁѴҼҌΎ˴ηƇ΄ɤ΄ȵԨȱĆÞяɫɱŕIΞȩ',
                            'message': 'ЀЀұɾгЄɨɻSԉЬϳъ\x86џϓãпȥӯВȮƽɔ^ƷҗĸԆŀ',
                            'arguments': [
                                        {
                                                        'name': '҉љʂɞԀ6~GȝѽÌϾĺʭйԕΑҜɮpѥӼѤӸʚY˹хЇʭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'țАɁ×ԃĜӔ˧ϦsBцΏýҸţňͻĮű˓ǈ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.485775:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѾҳǢ"\u0380',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԌͶȈɬџYτӾŴǱΦˉŦƈʬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŚԠʆÕ˟ʆΖΠȕÛ1Ӯ"ŻЯɅΡˆќÒǵǧşΦћµȟƇ\x91Ԣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'œҮͲİ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212324.486433:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǊʮϼВʲɳħːˍIŲæìɛŜhίɲ҈˶Дˉ8Ʈθй~ÆÙĳ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǶʽËϛńʥBҺԋӏԆĪȔΕҭüι\x99\x8aАáϦѹԥɡҋɘϭҴȅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȴԆ҂ĒҗƬϨӫˑĚʏѰєQӇӑŖː\u0380Á͵Ѷφќ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԗСñРʻѺƱжǻUřʴԙŜҏʾÇӞ\x93ѱԮɻŅˎƿԄPɵ\x9f÷',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȿӹ;EĉƂǺś²ңӺāġ¾ƽZķȳҶКöũ\x88ǀЋ˚ϱɳӏȓ',
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
                'identifier': 'ǾAŃ\x9e˶',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ÁΟ',
                            'message': 'ΐ',
                        },
                ],
            },

        },
    ),
]
