# GENERATED CODE - DO NOT MODIFY

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
            'name': '/\x7fȼǨéԨÂɓϻʜΒēД{\xa0ɗΛŎʺòѰʄԉĚӲѭ˹ƃ;ћ',
            'minimum_version': [
                -5454404978916700619,
                -1027860761913524620,
                -6026436194272095084,
            ],
            'below_version': [
                -3659103898488981878,
                -5009958662111529216,
                -1534891286519396612,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ĩͷ`',

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
            '$': 'ı\x9bǚǯŀŁҾɗӹgWĝћʱʖκÏƷ\x81Ŵƒӽ½ŇˈпςˏǪн',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -6059130437585908910,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 242805.08336055838,
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
            '$': '20220526:212405.230530:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ɀӂǺǡѱBäӘҼʝӒϧӓŊň}ƖαқȖ\x99ȌόĤӲϦˍ˵Μǣ',
                'ԩ|Ӽ6ʕϛʸQОŤчŝƿůƨ\x86ϙºөxěү˭бɒԆņӸɜи',
                '˨³½ʡϞѧăŴţ¥ӪɥĽƛ7ǾЅĘȅˆ\x8eǟèҢ¬Ȅ°ʮΘЏ',
                'ŶȈ˧½Ηʃ8а¨ρeф{ΛΗɺʐĽƵtӉά\x8bԤыǲѻʙÿÐ',
                'МұͱźҖ˄ѫÏԐʎϢҐfώǐŵ˹Ėʿ¯ыíň°ΔVĦԤԣэ',
                'ϾԖэ¯İɌԗňѩӅȨ.ǛϨ\x8dDҝƱë´ιҀӅŞХеʅsӫ\x95',
                'ǗһΟʥҨȁҝѤŖӴͼʽ˴Vʈљ҈ϠɶͽǥƮ\x8bщҭҜɂԆʝƆ',
                'ώǊ4āҟŕ6ûӝѶɠƺ\u038bǀ¨ьÎɞʳž\u0378ΣҲƕƺѩ҂ɔčӳ',
                'ˡɄҸˤԜнɧЕ˥ƚгϣΆŘӨFѺϰӱΊǞфWɳҕњpâ\x88д',
                'ˏыӣˠˁϮɼѸƼ½ѣǵŭ\x97ȭǞδ\u038bːGɣưÛҰѳǟŔѢѳө',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                6431602639653458250,
                -3509012813646680486,
                -2775470667513905714,
                -1765966032170744663,
                -8721657441014761480,
                -6530755317082060392,
                8333439182692772703,
                -4569827925808828954,
                4212922728633273656,
                5658553827608928845,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                334816.3054417565,
                39855.1127676052,
                565438.0623346396,
                209143.7780678115,
                155741.06521113619,
                574375.7475260384,
                -94121.48951858257,
                115176.95100370678,
                280194.7939436962,
                519991.8576335062,
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
                True,
                True,
                False,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20220526:212406.225438:+0000',
                '20220526:212406.250007:+0000',
                '20220526:212406.267216:+0000',
                '20220526:212406.284490:+0000',
                '20220526:212406.300835:+0000',
                '20220526:212406.316605:+0000',
                '20220526:212406.332602:+0000',
                '20220526:212406.348713:+0000',
                '20220526:212406.364754:+0000',
                '20220526:212406.384991:+0000',
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
            'name': 'ҕd\x82ǈğ©ĴɪƆʌˉȆßƠъ\x86ҙРŎʄѡǑɖ',
            'value': {
                '^': 'int_list',
                '$': [
                    -5772887235709573165,
                    -6425484020042391462,
                    7112599015760902290,
                    -8682427740253116709,
                    6688957114580237547,
                    4473310576203981342,
                    -2580872732970166641,
                    -5171894696984047918,
                    -6677399181879844098,
                    2715735098669430893,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'í',

            'value': {
                '^': 'bool',
                '$': False,
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
            'catalog': 'Ȉ[ɹŁϙЇ\x9dȕҜқʆɨòȍ˵ӖҟԎǾеʠʳ\u0378ʰҊǮ\x93Јʚȿ',
            'message': 'üċ\x9dʮҭΜԪК\x89Ϳ»ӯȗΧǹԙ¾ĀӱɰȋȊуˠНƮНρӈҪ',
            'arguments': [
                {
                    'name': 'ЗăIӛЛЙΒ2Ыȃ҆ҳΨǠдwß˒ҁ\x82əČ\x85ΫĸŅ˰җRĖ',
                    'value': {
                            '^': 'int',
                            '$': 2313497848667687396,
                        },
                },
                {
                    'name': 'ƿҬȠ²υ½ӈÓ\x9fӹƮĞȜĢɒľӂʥуюj\x96',
                    'value': {
                            '^': 'int',
                            '$': -6729214689921898615,
                        },
                },
                {
                    'name': 'ØX˳ƂλzҽuӰέҼ)˭˅αȂʰкąşİ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220526:212403.633049:+0000',
                        },
                },
                {
                    'name': 'æȈˡΏнɨщȶʭʀŲɛāīϐȶͽʆŢЋѩёœ˘ϡӟ\x93ƺʙê',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ǖӧԚưŻ˙ͶƁʆǼӣѳͱQƷυЅΨñǶ5ѾЮĚcˀÕЄϺο',
                                        'ÒЁѣ®ӽԘǇȍϿį˙˃\x92G҇ԑѧаϗӓu˼ÆϹЈǧɓ¥цN',
                                        'ӂѭѮú\x9cȁ˴Оťϥ\x8aϐčӨjʙ҇ϽˀĺʽϚЄ4Ӗʜ"ˁъɠ',
                                        "ĊæΩεһҎå$z'ϮѸƫӔiοɧҹFHωƁӓ҈ǐ\x9bJΖüƗ",
                                        'ӉμͻҍԊƄǫrƺѼƖ[Ɂ\x9aιǛ«UŤĂӹУ˒ƅҥҎȢqѴ\x80',
                                        'ǲъQ\x8aǿeǢľѶɃΘ͵ɢМӠΜѹɩɍ\x9cʍƶɆˬɒƴǲ5ȣ˒',
                                        'µ±ȀԄʵӚȿʿгЕñӲ,Ԋ\x98ŰˡʚȻ\x88ɾˁǅη\u0379ƜрΟнƘ',
                                        'ȲĥȆɞWȗҍΥǕëȶνҗԝѦ϶ӀґӍӻӶѮyτɂwӓѢųq',
                                        '͵ǔ{ʕЬϖуԜǉƳȑǌˡšӽϻʠѤȆǘτƤ҇\x9fƕϥ\x82ԒѲЃ',
                                        '|΄Ŧ˯ʒǙłĠˡĕϣ©Їʬ/ёԡϾ˂*ƉԈ ǹϼɰȪĐĚƈ',
                                    ],
                        },
                },
                {
                    'name': 'ͶÁƻˤϛ',
                    'value': {
                            '^': 'string',
                            '$': 'ѲÁǔ\x8cūÞ×ЅқӢӭҫsėŬƓƋˉҚķζԦȊÆƉȧˤ˴ûɥ',
                        },
                },
                {
                    'name': 'ϏԬԠʬÏŇťǡЍƓl^ʙЕčǸИÀǊVԮпZʭѪSβԉƂϢ',
                    'value': {
                            '^': 'float',
                            '$': 606126.4907134554,
                        },
                },
                {
                    'name': 'ȗǜӡаѧŒҐQЀ\x9bƏєƖĪȾδԝȻcĩǜԪ',
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
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ʯҏϞãґɰǜєŎѦщѤɋ\x84QȵŲ˛ԮΘǟѣϪ@˷ѝˤȣLǷ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -8776625360848623221,
                                        -1230878377376066330,
                                        -2194583360065272432,
                                        5638299707020923230,
                                        1839286437737368735,
                                        -7373864514002821877,
                                        -5283310973450273647,
                                        1704416839508362325,
                                        4160671657268249422,
                                        3874108048855252294,
                                    ],
                        },
                },
                {
                    'name': 'ɑ˾ϾŗҐ΄ΑõҮǋȀȡӗͶ\x87',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'KŚËԒãȜ8ѦԬȾąŕΙǑÓЦϨѶ˹tͻ*ŗ\x98ʆēƂӛƼˀ',
                    'value': {
                            '^': 'float',
                            '$': 677406.5406197454,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '˵Ӿ',

            'message': 'ϭ',

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
            'identifier': '҂§σΡЇɼśӸɀ\x9b˓Ӊѯ¬ʢFðОáϖҼȺúɕȤŁłɴԍӱ',
            'categories': [
                'internal',
                'file',
                'network',
                'file',
                'os',
            ],
            'source': 'ΨЉЏЯĴӥģЌǼ˦ǎƹȌФ˂ǥňǢˤά\x9eϩĶˡȃʐɉÞˮɯ',
            'messages': [
                {
                    'catalog': 'ʈїʶÈȻŵҎǷȺүԊĻȢȅȹǧkͼoΫǋɋӔЃHԍɫȹŗ҉',
                    'message': 'ɿ\u038b˹\x97ƆӫΡ\x91євL\x94ǩmӈʰ¡ΤѨͷԣȁ»ɲɊƆ\x93Ӳėǈ',
                    'arguments': [
                            {
                                        'name': 'ӭǵѓӢϽ˔pңӎʬ«ûßʣȚȃы\x86ɔεȻŚӓǙϤɌĉ±Ý',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȂMˀӥĸЪөØɂ!ЗkÏäʕƠɏӌãҹϥýɋǓA˽ƖԐƷ½',
                                                                            'ǿ®$Ťʌ;ųdЄʨґӝ˜іΓ\x8bΉtȀýƢǺѮиԓӶʜƣÝ«',
                                                                            'đЊҲŠĈlŴ×Ɖͱоϟ+ŜȃԌɱeκԖҮ½ӄȪЩӳ%ư͵C',
                                                                            '˝ɈÈĀЧÈҽӃ}Щʍӵ͵Ҭ\x99ӰӼāҍłӷΣOԔʪѻԈ0Ŏη',
                                                                            'ϬƋʅʱœƽңԉԗȶЍ$ғсćŸŃ³ω\x91ŝЋěЦǎθΉɤЍj',
                                                                            'ǹƈȢȨ˥ϥɱҪEƖͿҽɷĲҵЧѻ҄ɐЩȞŝʚĨϳю\x9fƸ˭ȁ',
                                                                            'ϹŽΫƙʓgóЅ\x98ɊѿƳ·¾ȼűѻʞ£ʝŃɀПԉ3ǐԕĨҼЕ',
                                                                            'µԮÉȅǡWÒĘώҟΫƗJͳЎɉÅƓ\u0380ǖԭң\x8eӨюčĀȕRÚ',
                                                                            'HԚ\u0379ùήЮҕľͲ҂ΔŊЗϲ˰ȋ\x83&҂®ːЫʉϾѕƞĮʼɋó',
                                                                            'ͺpǷӾȪɴĜ˥ѷ¤¬ЫŐЕԤϕόҾɸϫĞķаƂα˃ӱ\x9eԥH',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'GǊȇ|ӳΚεǗzγϱ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŭˤӇ˸ψǈ\x93%ȈѫɢØѥƲġЭʍԉƤ"ʑ~ѩ®ӸǕŊȵàЈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 412128.43444780447,
                                                    },
                                    },
                            {
                                        'name': 'ϕãĿНƣҒŀѴ˻ˀ˗a±ƛ˶ЂCҔĿӘªԑ/ԢѨѴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ғǭԂƢӉ\x8dhĢрѣɌȅΙѦ1ɐõȩј:ȇ`ɫȒσΊŞѿRȁ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212348.113584:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЋΏϲˠǭ\x96',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212348.211414:+0000',
                                                                            '20220526:212348.238885:+0000',
                                                                            '20220526:212348.258399:+0000',
                                                                            '20220526:212348.275463:+0000',
                                                                            '20220526:212348.293474:+0000',
                                                                            '20220526:212348.315037:+0000',
                                                                            '20220526:212348.336611:+0000',
                                                                            '20220526:212348.357163:+0000',
                                                                            '20220526:212348.378236:+0000',
                                                                            '20220526:212348.405796:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϤȏΔǗ˞ӰӆԗБʿүǸǡϓΏɼƃъΌȞŰ˫˒ȩĲ[Ӟ¬Ӻς',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 403521.79795364937,
                                                    },
                                    },
                            {
                                        'name': 'ˣЅțΧ}ɕǉ»ƜɐÐƻʟĥôЙɄºǾЧѨˌЧоǥΆҝǡŢW',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 100725.30926976149,
                                                    },
                                    },
                            {
                                        'name': 'ʾǿ˗ƑЇŽʻ®!Ԓy˼і',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\u03a2κę\u0383ǀҴǘʺÔЍȵӃâyѧԉƈýК͵bΞZʫѰɫ\x95κ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ːι\xa0ʅԄˎЕŖǴß\x83ǽä˕\x97ȓ_ț_Ʌҥϣƛǫʻϧ˶ýΖӸ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҍӌӨәҏ\x87\x8bӧʜϽϺâƕªȲėӛ˱ϰxΆӪ³ĊϭҷʄǼ~ò',
                    'message': 'ԀʞΧҚ҄\x85Lň˻ƶ˯\u0381ƝňļȀ˩ÌÁәǘпªϝɂɘƁȴȎѠ',
                    'arguments': [
                            {
                                        'name': 'Яǝ˸g_ǽțmBͻΜǿȵʴȞʛøǑѧ:Ʀ)Њŋ0ɚ\x8dԢųʍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212348.943772:+0000',
                                                                            '20220526:212348.963324:+0000',
                                                                            '20220526:212348.983181:+0000',
                                                                            '20220526:212349.006647:+0000',
                                                                            '20220526:212349.032199:+0000',
                                                                            '20220526:212349.055853:+0000',
                                                                            '20220526:212349.080077:+0000',
                                                                            '20220526:212349.104486:+0000',
                                                                            '20220526:212349.128173:+0000',
                                                                            '20220526:212349.153236:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'đƈǺȷԪňШļȃȂԏȋϾƣ\x9aɈ;ΓǹźŌ\x99Ƞ¥ǋɗǦ\x8cӎԬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'þX"ȺƻȴʴПɋɰL±ŸƵȜưÉć˅ӯƠļӛţρȗ²ȮҬ6',
                                                    },
                                    },
                            {
                                        'name': 'iĩ°ԒǈɣɩȒɓ\x96¼Ӥ˗ʨɯɨгʶ\x89ϭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212349.314864:+0000',
                                                                            '20220526:212349.331859:+0000',
                                                                            '20220526:212349.351142:+0000',
                                                                            '20220526:212349.368465:+0000',
                                                                            '20220526:212349.385505:+0000',
                                                                            '20220526:212349.402679:+0000',
                                                                            '20220526:212349.421306:+0000',
                                                                            '20220526:212349.438485:+0000',
                                                                            '20220526:212349.455306:+0000',
                                                                            '20220526:212349.473393:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'œ$ʵ8ЂŴEϔϮÛşъǯ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212349.565765:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ұǢʩʛςϨȊÿƙǵӛΓӰ˶ʬҏˡʛ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212349.636406:+0000',
                                                                            '20220526:212349.658056:+0000',
                                                                            '20220526:212349.679505:+0000',
                                                                            '20220526:212349.699845:+0000',
                                                                            '20220526:212349.723978:+0000',
                                                                            '20220526:212349.746860:+0000',
                                                                            '20220526:212349.777947:+0000',
                                                                            '20220526:212349.819344:+0000',
                                                                            '20220526:212349.851451:+0000',
                                                                            '20220526:212349.882713:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȩ҇¾ƴȋɆ΅Ҁ͵ψƽȅĕϙǝaɣĻӥѳɔʡíˏήІʦЈʥɵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3193296482382217605,
                                                    },
                                    },
                            {
                                        'name': 'ȄЗѝĽƝŊņůˤãȉŅǑҧ˚Ҁʻµåɒж',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '3]lˣ҉ѢѐǛϦѼъ҄ɈΑʕԁӛσ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 8767.589351187882,
                                                    },
                                    },
                            {
                                        'name': 'ɺ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÖƢĿҒÊύļяƷтΑΚԇåҩȄʮǸθɫҴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȱ˰đɰсŸθLу×˘ȿȻɞƴͱĚҌ˅δ΅ӊ²ãǄǪĞŘѦÀ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϕCĝϱţҟѿþŲDŤǓȦĪσԃӉӬǇ¯÷һ\x9dƯȆÇÑԁҲɻ',
                    'message': 'ÔϜ±ӣϊŎɫ\u0378ҢƭΜŃʧȜӱЈº#ԇǧǘɔǩÊԤҦӿċƅů',
                    'arguments': [
                            {
                                        'name': 'ưȒȠɍӮƋԫΓƜȘЍȧǺӜ\u0380˾ѷàѴ\xadýǦҾA2Ϝʓǥɟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'γʧύϯƒʿúƧƚʊȼĮΕˏˏáПжŪIŀЎrʎњМѵӕѦΔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            656693.6445079425,
                                                                            116906.77452989909,
                                                                            208742.33196267608,
                                                                            598658.7851523949,
                                                                            307110.99371945707,
                                                                            484890.34284601,
                                                                            685292.5799650096,
                                                                            111464.96358868596,
                                                                            688135.928001333,
                                                                            249589.73896466725,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҙȗ*Ȱ\x9a˻ΘRůΝȘʹ,Ͼ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7397887532251271536,
                                                                            -575850213593189136,
                                                                            6489834198346527061,
                                                                            -7873293035050726202,
                                                                            4615941318228521134,
                                                                            380940192778300206,
                                                                            -7558291602258488267,
                                                                            3295845367287282141,
                                                                            -1404740622615649448,
                                                                            1803672113359808696,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˉ1ō˼ғ7ĢЗoқϹɄĐnӷÜʉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƗҙȋǍˀԍƷ˹ɜ3\x81±Ύ{ԐѼѮͶ\xadӆ˖¨ʗƇȼÕȐЙӬˇ',
                                                    },
                                    },
                            {
                                        'name': 'Ѐ˦˒ÎSť>ԇÎʱ@N¼άǊǆϡԧП\x9cʹtԮЮz\x82ѾŴԮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 628366.6380998561,
                                                    },
                                    },
                            {
                                        'name': 'ʯˋ\xadϺƒϵǕHÃśҲµŲќÈѩʢGɈ\x82ȾҞфàΧͺө7фԪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8573447883631833840,
                                                    },
                                    },
                            {
                                        'name': 'M½ȎğȢdв=ǂğҤc\x9bʁӱҿȠɅǸĩīX\x92ăѹϒΤԞϋƬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 13943.158846652295,
                                                    },
                                    },
                            {
                                        'name': 'Ǭʉи˱ɷƷɣȍєàϵɳǆĴһɪʡäôƽàĺʙȳƋӂˮм',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212351.601990:+0000',
                                                                            '20220526:212351.618587:+0000',
                                                                            '20220526:212351.637407:+0000',
                                                                            '20220526:212351.654880:+0000',
                                                                            '20220526:212351.672041:+0000',
                                                                            '20220526:212351.688729:+0000',
                                                                            '20220526:212351.706509:+0000',
                                                                            '20220526:212351.724106:+0000',
                                                                            '20220526:212351.741209:+0000',
                                                                            '20220526:212351.758565:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˔ǗưȌԆʾƈ˫ŝɧɤ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ZȭҟCͶŢӒΏŋªɪȘȞίʇҴ˴ǏŸїɌĽȰ˄RĪŀ»Ѵϗ',
                                                                            '`·ƮǬԓԎ\u0381ņśʮñUń ϔԗŚȷбѺȓϘѴԝ6ȆҔȠȧт',
                                                                            'ҝ˺Ѳ\x89˭ʊƲͷμʻɇɓθȵʲԚЧİҌōșǴƀӹmӝĲ/ɏʆ',
                                                                            'ĳɠϕæѝӯӦѻĊҵΌô\x8eȖΊ9ĤȰʯϛϙȾєѶӇШѕ\x96·Ϫ',
                                                                            'đðô(¯ԗ άІ\u03a2νЫġЈǘԃӡʌΣ\x96ёŦ?ԄѾɪ?ŝӺ˟',
                                                                            'ºҴЃӆϺ˅ÐҲȟƤĶʦ3ʓļ¥ҘέċŤЕÞǶʈŉϻĄϸŲʦ',
                                                                            'ʦo\x97Ų˂ΌɂϑŰǫ\x98\u038bǟв÷ɝʎͷԫ˯ɈұөЙϪʦ˜ĳҹԫ',
                                                                            'ƋÔóΓɛɹΡή¼Ҋʤʜ&ãӋȴ×ʧӁΧѫġɻҬǥ\x88әӳȚɃ',
                                                                            'ģëǔˌƁcGΌ_ѧµɮŧÍԅ>ƤȪˡĬʷýƾ\x97Ŭÿvïʪʮ',
                                                                            'ŽÚүŠŅӽԖȪvʍ·\u0380ɌԚÁ\x82ǗƇSŸ\x9f)ϦϒɜϱѤλҼÔ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϲӀ˜]˵ƹǑïɄӄ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˝Ӡʰ$ζўσʭǊʕÇȻƪϴњǓɨ҆җ˃ѐfdʕ\x92˥ϒБɡϾ',
                                                                            'ˣϤi{ҕԡHЕOƸ\x99˨Ǧ\x85ΛőΫĚÊмŇĞƚəМǵĪâʒѺ',
                                                                            'éӪ\x87ǷqȑƔǕJoԏ,δԟŹʠʈŀįõӆǯɖӘӇƓΥԐźр',
                                                                            'ЅI˹ԑɶăŉԣTәǹG˧КԨ*ãҙȟȩȘыӒɍƐ\x91ГņɋǤ',
                                                                            'čўʳːѮϻϷɲЮ\x90pέʡҮÅϕĢĿʠϳсˀêƅĞǶǬũɉ҉',
                                                                            'ȬԎӠñЬ˝ɐԕҽ8˻ĺǗÑĮǒ´õқļԈЭϙeјѓϟѤȜƉ',
                                                                            'Ԕʾ½FȲĻųэ^ȝUУŷźÆΧ¨ɿØԚˤӸΨ\u0378üķȜǃM/',
                                                                            'ҊԛĴтЇÛц˕ǪħϓѷʧЇЁÛĖȫʞƞӞǇͺʚƅɨȼˀңϚ',
                                                                            'ʂӭĘҙҬӟ\x92ҌϺņʊŌϏɽҝ5їńԣеѐҎɐ\\ӝИ\u0381}ĊӬ',
                                                                            'ĒīǋʶȝɎǮԤ\x9bуэʣǉ·ǺɺƽŠҤΛ\x9eʬ4\x94ӂΝˤГʎϵ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȴϼsʹȵϲѴʹƂΠɼԅċȘԈ³ĊхQĂϹЩ˺bT˭ǳҥ$Ɔ',
                    'message': 'ǩ×ƵxϼϠϣɡ\x8dХǍɅҠƅӗҮʭеǯԎ=Ĥ\x93ŸºŤóaŮÆ',
                    'arguments': [
                            {
                                        'name': '{ʤ˜ųřӿũžςЇͳŸȘϪƃϙԫɚȕӋŎԝƩɖΑƤϵ1ɧʎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '1ԥˤѭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԤҟѰн>әɔpʟԗǬƀ\x89ϔŉąѪŐǡßȐĤ©ɵϒЬԈͻЇļ',
                                                                            'ɫĚѲƬˆ8ďʞɆԌϒȽύϟӓӤӮѫǘѵҦLǏϦîƣɪêūʠ',
                                                                            '\x9dѻºàŋӎȦμŶϼɑʄЊȼªŰώе¹Yʌɨԉхϻϸϔ<ĜV',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΛÇϸӋǘПņǐɜҲÕΟȩJӑǁԟфǃӱ©ħ\x9dĹʛÑȼɛЪF',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212352.687401:+0000',
                                                                            '20220526:212352.704189:+0000',
                                                                            '20220526:212352.721161:+0000',
                                                                            '20220526:212352.738320:+0000',
                                                                            '20220526:212352.756705:+0000',
                                                                            '20220526:212352.774394:+0000',
                                                                            '20220526:212352.792546:+0000',
                                                                            '20220526:212352.811420:+0000',
                                                                            '20220526:212352.829134:+0000',
                                                                            '20220526:212352.848096:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'фùúӇÝȯԫıХЊġɳϛɿξkʵж҆ʱƢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            924996.0232036212,
                                                                            930586.4368433853,
                                                                            431988.7992231251,
                                                                            388502.0049681005,
                                                                            752487.0914147384,
                                                                            802201.8650898982,
                                                                            910569.4530206376,
                                                                            913229.9343840895,
                                                                            487803.03934361157,
                                                                            753690.7115949567,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÍѴȗÈɥŏ\u0382АˑɯǢŘҶʤӊŭȟϺȤďʣӧȱ\x96жʬ·і',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            313806.51794809464,
                                                                            712520.1220184149,
                                                                            75194.90457095148,
                                                                            621274.0485308404,
                                                                            605636.8780716786,
                                                                            648962.9154147629,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѓǅPϯέԧǥӛĬǫ¢ɽĈŦϐӰӮTψφϡԬʩҺėǆґ<ë˝',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212353.456854:+0000',
                                                                            '20220526:212353.474862:+0000',
                                                                            '20220526:212353.492585:+0000',
                                                                            '20220526:212353.508741:+0000',
                                                                            '20220526:212353.525880:+0000',
                                                                            '20220526:212353.543036:+0000',
                                                                            '20220526:212353.559699:+0000',
                                                                            '20220526:212353.576537:+0000',
                                                                            '20220526:212353.593038:+0000',
                                                                            '20220526:212353.610358:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȱӫȈϦŋȬ,ӂБƚǨοċéȚҠ˹',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8311902821712004341,
                                                                            -2985858538594869722,
                                                                            -3606450767869557872,
                                                                            5051867188151987787,
                                                                            -4936773882330959491,
                                                                            8033873511198513871,
                                                                            3049158224959630934,
                                                                            -8162814043864639491,
                                                                            7801094367510854348,
                                                                            -8721645417981289210,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'íκӈȞƿϸѼԋԃϑŷԣZʘҊҥȟҪʦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -38947.89824314488,
                                                                            131470.11489545362,
                                                                            332273.86247525195,
                                                                            985769.5678481313,
                                                                            349922.9272334952,
                                                                            965254.5402562818,
                                                                            887192.7062488148,
                                                                            806974.88546596,
                                                                            510951.6852556701,
                                                                            435182.41959287704,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '³ƩӣɅǃŖԇĉ˩',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 728833.9949054031,
                                                    },
                                    },
                            {
                                        'name': 'ȝwȠҝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĭǡǄŉŒѾǝѲŸǴÍʂėǪԅĔѨ˨ÞРЀʲʁκц˺ңͱԎӞ',
                    'message': 'ùȄʸˌзҁ͵ȕ˵ΓҭЋmĵϷˋę΅Ʃ!˟ʾьƥ\x85Χ˃ΞÒҐ',
                    'arguments': [
                            {
                                        'name': '·ɍ΄ǭĵĈө\x9dɣǟȇķȆǈҠȒД˗҈ЌΤԅλ˙ƖByˌΓʙ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'źŌƉҵà',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 800141.2092563891,
                                                    },
                                    },
                            {
                                        'name': '\x98ǋǳ˃ɤƤ\x9bơ\x8eԝ\x9aѿŎǭ]ʜWϡҠøпқаżѻºÞӓʤʹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŋԭИѠȘƼΥɆӨ˳ǰʠϻҒӜǡӭԦԒĎ˴ӌώƃӋƽû\u038dĭ\x90',
                                                    },
                                    },
                            {
                                        'name': 'ųēӕʩ˴ΞвхɿҶǀ.ÔȞјǃƵūѻӴ·a¹ԭёӏ?\x83Ӧθ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3634783698642078827,
                                                                            -3329767712239160484,
                                                                            6061859057588987142,
                                                                            4457331613668501544,
                                                                            5364545589637292917,
                                                                            8667071245356166679,
                                                                            1800124083848858786,
                                                                            5375878729817342347,
                                                                            2978130439728228388,
                                                                            7594718993034215626,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Щ˕',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212355.179634:+0000',
                                                                            '20220526:212355.196917:+0000',
                                                                            '20220526:212355.216019:+0000',
                                                                            '20220526:212355.233784:+0000',
                                                                            '20220526:212355.250442:+0000',
                                                                            '20220526:212355.266728:+0000',
                                                                            '20220526:212355.283605:+0000',
                                                                            '20220526:212355.301123:+0000',
                                                                            '20220526:212355.317487:+0000',
                                                                            '20220526:212355.339945:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѭӯѡ˩ɂǖѷ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212355.541115:+0000',
                                                                            '20220526:212355.556815:+0000',
                                                                            '20220526:212355.573614:+0000',
                                                                            '20220526:212355.590126:+0000',
                                                                            '20220526:212355.605963:+0000',
                                                                            '20220526:212355.621833:+0000',
                                                                            '20220526:212355.640491:+0000',
                                                                            '20220526:212355.656602:+0000',
                                                                            '20220526:212355.674894:+0000',
                                                                            '20220526:212355.693467:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ς',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҊŜӔ©˘҆őґǋřԁɲҞǈŉɶʮǂȪ˖Ƽ¢ĜүˋSσɢőӀ',
                                                    },
                                    },
                            {
                                        'name': 'ĥĢҤǗªʥ˻ӂǙȃǢƼÞԮɒÁƪȏʶƔȠǔČϱ˥іƜǟ\x8dӝ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϛʜёǘ΅˼Иϝŕ˸ɜ?jҍȠɯҠ¸ѡ\x9cɅɼӼϛĀҟΐƐ\x92ˑ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8806658121425268565,
                                                    },
                                    },
                            {
                                        'name': 'κ¿*ў҆\u0380Ϊȹå\x84ʡóǿŇ҇ό\x94\x88ӻŭӌԝԪԭ\x83ЍƊʐƈϷ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212356.173537:+0000',
                                                                            '20220526:212356.202923:+0000',
                                                                            '20220526:212356.223862:+0000',
                                                                            '20220526:212356.241720:+0000',
                                                                            '20220526:212356.259010:+0000',
                                                                            '20220526:212356.277536:+0000',
                                                                            '20220526:212356.307013:+0000',
                                                                            '20220526:212356.335277:+0000',
                                                                            '20220526:212356.360043:+0000',
                                                                            '20220526:212356.381421:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'řƣҜɒÏʆьξ¨\u038b×ʺǚèӈĻůʞűӛǓίҊĥԠѶƞʹƸё',
                    'message': 'χΥěǱŜėǾĢѧǌҋжʧӥԁȣ:Ш!˰ҨеҘȮːдʢ Ӭŋ',
                    'arguments': [
                            {
                                        'name': 'Ώşԣѽ6χηԄǔ«ɇˌgę˽Ԁʂы˶˭\x81%ˍċ\x81Ǖ˭Ł$ú',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212356.527861:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u0381ǥĻɄŖ˲˙ȡQɲǓO',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʕʓӨӻӟѰʓήξžԔĴ\u0379|ВŵаѨϬкȞ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƕȆԒưѮƽɺπҺȷ_ɜɟ1ʲԩӉƆϙɸҮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            24650272841463693,
                                                                            -4353666967055877684,
                                                                            -7454665619845647039,
                                                                            3439239249580909044,
                                                                            -4517802319440224294,
                                                                            -7357108364365457172,
                                                                            -7117041630039401921,
                                                                            -131994558931501115,
                                                                            5075310491187267294,
                                                                            -4431637514999408646,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƀĢŇɐӬԍʇϛӳƴȚǽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Рϳ=ѲƃȲ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212357.478340:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΙȘĬƇԉəÒǔȁԙɘҗӃǲϝĩНѱѦǹɠH',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7217215312056139114,
                                                                            -5071979863415973134,
                                                                            -8581051129803257315,
                                                                            -876892424268628517,
                                                                            3450126442056255796,
                                                                            1462900548245387165,
                                                                            -6587943080788075263,
                                                                            -1620452405002161442,
                                                                            1421652965976764337,
                                                                            -6659895385235654141,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɩӕɼͻ!ɔȝˁ҅',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2450810919139093243,
                                                    },
                                    },
                            {
                                        'name': 'ŶͺɡѫətπЛ*ѫNƟXǰǬƚƗρ\x9fɸŬąƬķтϤǿҖԉĤ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȘÄǼcˎʅϲЩЪ˺À¼ϬӂƺñŸ϶KͷǗɩȒÊ5ƄϲȨJȸ',
                                                                            'ȽŦίΔ\u0383˽ίåЂŭ˼άκҵ\x89ԕ¢Ѷ˥;ĕŇȨʑðѷґǯ˞Ϭ',
                                                                            'ŽѪ\x88жͺÅ_уWҤДʁ4k!;ˋʦãƈĬ˼ʆϔԞ¯ϡAɪǛ',
                                                                            'ΪɄϰϵǮɨɲʨ˛\x91Șғɇ˶öĀ¤ŹӉƾˁԎѵ¬υϘʙӣȿɽ',
                                                                            'ТŀǛΡ¨ӂʷŶ҇ҩ˖ёa\x99ѷƊƻƩǪʭԏѕ ˰ΚɮЂˮÎͺ',
                                                                            'ӻǄķǉОԓȉęФĨ\x83ɾĻӉćΗÒ˯ħ\x8cʒϾʜƎƪΐˑǼƇZ',
                                                                            'ǫ\xadσсƴēďҜÛõćӼİ{ǔȇѦ/¼Ǔƕө·ԮŅƭĖ4ǭϕ',
                                                                            'ЊȧАƇϫsŀҷȟŉшӂӘ˯ӴTǳůǴǘΌДİUѤ˨nγԐŶ',
                                                                            'ĴӋ\x9cĤƱʌˠ÷ʨˊ\x88ɲĆW\x81ϽˡϻǢԁǾѦҳӂʰÛѐ\u0381Ǟò',
                                                                            'ЛĈάƸǔŝϹғƅΜŦǛĜӬ5Ќ\xadđˈɰǤ˭ƢΤ\u03a2ƒũҾęM',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x91Ӭ҃Ͱ§ЩÆĎұϗ¯:˖ŅǺ˱˱ϦÇ|ɥԠԕóЬŤЊʍ\xa0ҹ',
                    'message': '˞ǙÙƚcȖEϹLȲƤΗǒ\x9dÇĄ҈҆\x96Ȭƣņ`ԂͲı.ƤÅÄ',
                    'arguments': [
                            {
                                        'name': '\x8bɣʹɮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5818414761555220914,
                                                    },
                                    },
                            {
                                        'name': '»ũɴӇïԌҼǩŞҶǇ˘Ŧ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212358.388266:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȭиҔΥŰԗȹϚĩЬ¡ϒŎӅȟ˹óü',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȤåʻЖƚʗнÓƌҨĄʆśƘ\x96ǝЫіʇ˗ψ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ԩȏ˽ȋɇŇҽʤͽԭĚӮȢʅϓˇƹ\x85şĒϖO·ЁɫӜ;ĳɵ҆',
                                                                            'ǹԍţўø$ҦēʞɗǕ0ǱʱĴȨſ˾ԆӑЙȩˠѩЮʿ\x9fȖi$',
                                                                            'ǟɑϦɪǝɒŪɺȀϠӕ˕ƐËǗÕ¦тǾũ¸ƶ\x80ƲĿʇ¸ȣhϻ',
                                                                            'ʆȨ˷˹ϾÉQȀ4ʓƿ(ǫʗđȡÇωҾɍҘўѿńʺǃЋϞKȆ',
                                                                            'ƼʶЌȒűʟϗԀ\x82ʟǆÆǵ7Λѓęɟӝå\x7fʪ¥ҮÓԭҧґΗѽ',
                                                                            "oˋȑƿļ'рÌ§ͷҜȗ§Ҿ/ìЧĮ˭ƻпΡnƚƥѱԭ=ϫȱ",
                                                                            'jВŒâʉƳɕ\x80ϚƫѺȟIήĚӰԔˈ҉˾ˤ!Ө>Ξȅʆėԟ¨',
                                                                            'ɊРïϫЬцҽW\x96ɗыԢƁϭjΨωƲ«ŧˑčxȪʹԌͶӷZʿ',
                                                                            'ʻɸúƗÈ¸пɅӘƎ±ŇӉХҞ)ϓȀΣбϱˁ\u0381ŧʗΓ\x84ċȢЂ',
                                                                            "ŜɀdΑȺљ+ҢҖƩ'їɞϩԄŌ\u0381ϐӔʿ\x83ƘґưǴ\x9d'ɮž´",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҙɮӼĤйǒҙŦӋȡ\x98Ӟύȉԛ\x88\x9fȟϿɗƦɂǾſςԡјżȲӘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            658586.2147837685,
                                                                            221050.71887951536,
                                                                            381184.9175710822,
                                                                            -59949.858332409276,
                                                                            404957.6865858971,
                                                                            782858.4786904035,
                                                                            979068.5527789786,
                                                                            642662.25774251,
                                                                            610162.191649121,
                                                                            537486.9652588672,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȋϐӃѾƷúƝʓu\xa0ԇԧѶě·ѸǹȽӉ\x81ӳɞƛ«ȿŐЦ¿ɑĦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ЃƉҽɘƩ\u03a2īȂŏQʁõɠ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ÄĺoӬȉЙԎĤ)źόƸӒ˸ɁӸßĎͿƟ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5463180600459198340,
                                                    },
                                    },
                            {
                                        'name': 'җ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "þʿϭ¡ԕˣʘԌɉѷЛɃɬɕ\x9fǳűЬϜҾЂϰΪǿ\x88'ήŦÅǢ",
                                                    },
                                    },
                            {
                                        'name': ' Ε',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212359.688721:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʀԄҦɗƐʴ˫˫ӰÆɄƋҾ΄ϟñşѼƎΈõĿȇŴЈӖͿ$κ}',
                    'message': 'ǴDMӈôʴºk˛ӒƛɻɈӾ9ºȡȑяҤҁė\x7fҊɉ¶ҴǉӯƎ',
                    'arguments': [
                            {
                                        'name': 'ǅФˮЇƣų˩ȒKԑԞǠʢҪѼƇСɝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŜƈΖ·ǨнЅԤŜȫcԜɺq˼ԭСˁҳȻ3ʭƎȁυ}\x8fʌďȮ',
                                                    },
                                    },
                            {
                                        'name': 'ϦʥςǳԄӲƖӣ˼х^ӼmʼʧЅɞϥʓÙǊĸș˄ɹɧĈ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ',ȥј|ŵЌϨɢԔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŖrɲêΏΛӍɦҊ˷ԊȥѢ¨΄ŧҟϭİţȃɠș\x81ҩǷ˚ӑMŦ',
                                                    },
                                    },
                            {
                                        'name': 'ŰӏӅÓɨ7\x98łƹύұʢʯϽԒιªƦ˔ɝКӥãΫëϣ\u03a2ҧ˹Ƕ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -41715.257279235826,
                                                                            441084.9517807418,
                                                                            520022.5490428547,
                                                                            694463.2142577404,
                                                                            739012.506096992,
                                                                            934664.6138833901,
                                                                            283905.21978518023,
                                                                            186483.0322437674,
                                                                            983743.3240753545,
                                                                            160137.72643917685,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӌΊɰˤAʿ\x94\x92νÈĴӰ×ͺWΉ`ѻƨ˯ȴɞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212400.552540:+0000',
                                                                            '20220526:212400.569611:+0000',
                                                                            '20220526:212400.590905:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҍ˒',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            945283.794072211,
                                                                            251330.2397910991,
                                                                            156528.97258460204,
                                                                            614658.6871838373,
                                                                            531679.0203873169,
                                                                            923562.5999121204,
                                                                            342366.6564777122,
                                                                            596301.3547292083,
                                                                            893643.4296151011,
                                                                            713410.9750287599,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɫʗѥŬɅ˂νɴАΈѺ˷γǕ:ҸțɹӇԦrә9ŹѾ·ÖłRá',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212400.988192:+0000',
                                                                            '20220526:212401.005309:+0000',
                                                                            '20220526:212401.020996:+0000',
                                                                            '20220526:212401.036936:+0000',
                                                                            '20220526:212401.053992:+0000',
                                                                            '20220526:212401.072415:+0000',
                                                                            '20220526:212401.088140:+0000',
                                                                            '20220526:212401.106196:+0000',
                                                                            '20220526:212401.123845:+0000',
                                                                            '20220526:212401.140946:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӿаɴ҅ǂĖωɿԔԀĶ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1397965029500331748,
                                                                            2743733848166980072,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x91ε[ӜԣȬϰӼśԆƖ:',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -93446167452174423,
                                                    },
                                    },
                            {
                                        'name': 'ɾʽѵö˘΄ϚΦҽƟҸƇǁì\x98ǒɝѡƅ˂ĀѦÎɩQĥвˎLț',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1691816040206839173,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѼPǱКÐȉ¹ų±Ѝ\x7fʬˇ˝ɦͳÙ\x84ĺſȥ˰ҾƎŁǓҍľɮ\x83',
                    'message': 'ɃӛΜȾçƂ΄Ϭ$ˮ\u0379ӻѡȸcʮԡĶȼԀЙΥhóňҢԑϭZͻ',
                    'arguments': [
                            {
                                        'name': 'ʠʔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 459480.31217074755,
                                                    },
                                    },
                            {
                                        'name': '˴·ӢûβӨµʦʉԤхӐĥШ¦Čƍɼ°ƪ\x93ʡȏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѡƁяîˆЋˏˎŻťƹʔ\x87ƊÙ\x93Рԇ\x80ʦҶƯͿ£Ůʸ\u0381ǮʜÒ',
                                                    },
                                    },
                            {
                                        'name': 'Ϧ˥Ϝʬnӳ~ȘtǝҠɏɕåϫǲIŚ˚ΓњƳЦZńŬРžҫƊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3544503104943291458,
                                                                            2243913070907044145,
                                                                            -1492735285508018658,
                                                                            -599513665077325433,
                                                                            2455608876476208770,
                                                                            4235511705095017025,
                                                                            3527748109979904249,
                                                                            -8743467365529613062,
                                                                            -6976582384666694179,
                                                                            9141830092255105549,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ζþǃȧí\u0382ҹзϫɠͺ2ȏ\x8aԓˏ¾Ѯ\u038dƊȺĥˬϥМ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϗ*gϤɕ\x8dҖҒ˚˗zƜΧŝΡιǍɝ~ZӽԓЈâ\u0379ԙѲŭѳЉ',
                                                                            'Үҷҩэł/˃éʶ£òŤʤѬȔД˜Ҝ£ϒхėǭ|ʹҾɆмȦҀ',
                                                                            'ѐȳ¼oȥˁfŦɪҎԇϼœѠʦҲĢ\x9bÏŭ\x87ЃκƉЊүѴ˅ǜӼ',
                                                                            'Ȕ§ĕəˤ\u0380ȲńѤƚіʖҸʋѣѓɃͶƾЬҮ˭ďǏŨąϔѾǷƝ',
                                                                            'ϨϘ҄ѢŐ\x8b҂ХΓԮϣҏЭ\u038dԇжйѓĚҩĝԬ»\x81˃Ďж&ɦɅ',
                                                                            'ĲϥԡɛfХƠˣǛӦ˨˦ƐĴ¬ĦpҌɦѨҨĜʏ-ż¬GδBӠ',
                                                                            '˹ʈ±ŮǥϧӚҺɄ\x9bъԐˉE˗ŭҤĦȆˣбŐųԧϯ«їȶӐϡ',
                                                                            'ӸʢΣǒÃĭzϝŀĮƵϮĐУɅǨ΅ʀă\x82ˣњƪ¸ʘńĲɥČ"',
                                                                            'нƶ\x84ƙÒљԅɩʎ˰ǣŷļȤ˭ɽ\x8f\u03a2¬ʾΫǴѥŅħϰʡԥϩЛ',
                                                                            "Ԛ\u038d;<ȞҹєDѡŮƅCѳ~ÖτƂŗԏ3˩ċĄƃO'ξȺȵv",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ν²Ƒ˃ЍȒЪáӨ҂\x8b',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɉÒҶӾ˄ё\x8eɭчĭӨǉˀѸσϒĝ.ԎÔ˃ОÝҊʆɧ\x9aǧΩԄ',
                                                                            'ĢîΗəϫÉ\x86ɝƏʲΆėŠİǿԗ˙Δ\x83μǭтїЎΖdӂӡӳφ',
                                                                            'ǏÑúƙӜӏΪԖ\x8bʈαː҃Ρ˝я˘ͽӐѓЁǘ<ÒʙɱÁSÄÑ',
                                                                            'έĨӨOț¿υȘżĭѭĿÓ4ƘЩĬåԊɾϛůƜǠ-ɚПҲºĐ',
                                                                            'ьȦӯ¨ƼçҫΕϐӃȜζʬЩΡ\x86ǨΞʊԭ«\\\x86ŉɔӄĒ˂чђ',
                                                                            'РŧƁǍĴǥӏȵĢsҔCʗм®ý+γҵȗԭӇѥϷ\x97ȻʷłΗɔ',
                                                                            '?ҾożВҲӗňɈJƱΎԌΣϛӋ˫є|=į>I½ƉԭκхµР',
                                                                            'ȘɃȋϜȸpϙӠBŢҐӚҌʻҳˎşǑƲГŪ»˱¡ƞ҂*Ӗļ£',
                                                                            '\u0380Ϳσ\x85ҏ\u038bƚĘȾǵƗѕԐĽįКŮҧÇѝmӆҡ˟ƌǟ×ªЎҷ',
                                                                            'Ǻīϓ±ʓ˶ǜˁюӪǼWҽÃҰ5ǙӅʜʇ6Д¡>ơВͶԦ\x93Ѯ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƽ§ϡwѩϲγҤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212402.511539:+0000',
                                                                            '20220526:212402.528770:+0000',
                                                                            '20220526:212402.544336:+0000',
                                                                            '20220526:212402.560182:+0000',
                                                                            '20220526:212402.578530:+0000',
                                                                            '20220526:212402.596109:+0000',
                                                                            '20220526:212402.615724:+0000',
                                                                            '20220526:212402.635687:+0000',
                                                                            '20220526:212402.654319:+0000',
                                                                            '20220526:212402.672013:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038dʴșƑơԢͱãӽƔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 247520.47855794727,
                                                    },
                                    },
                            {
                                        'name': 'үі',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8433357643390067049,
                                                                            -1650499884490335817,
                                                                            523585042230477125,
                                                                            -6330689137182703352,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŐǮϬӃ\u0380ƫȨʺϷˊʸȊżŃȈΙǣԎȍӻÇˡʙӚȹΏÑĦэΔ',
                    'message': '\x7fӵĔƞŞІĮǰďſǏɍƓӄѲ¢Йҫ˯;Ϭ\x92Τþ˃ʂΏŒˣɕ',
                    'arguments': [
                            {
                                        'name': '˔(ό\x82Ŋ¶',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212403.030718:+0000',
                                                                            '20220526:212403.047291:+0000',
                                                                            '20220526:212403.062989:+0000',
                                                                            '20220526:212403.078686:+0000',
                                                                            '20220526:212403.094616:+0000',
                                                                            '20220526:212403.110432:+0000',
                                                                            '20220526:212403.126439:+0000',
                                                                            '20220526:212403.142106:+0000',
                                                                            '20220526:212403.158052:+0000',
                                                                            '20220526:212403.173826:+0000',
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

            'identifier': 'ŏϞˇɑ:',

            'categories': [
                'os',
            ],

            'messages': [
                {
                    'catalog': 'ˣƶ',
                    'message': 'Ɯ',
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
            'name': '҅ɒȁӽȃϙɲʭňЌÅR˘\x98ΟXF\x94iŚŻʲ˔ƃȧȔhǶ\x94ʷ',
            'error': {
                'identifier': 'ʹ:Ȍ\x9fу΄ʖƿѯǌˮǸˈԟΕǖҎдÛʭƵϋƳӔԭěˏлƲ,',
                'categories': [
                    'internal',
                    'access-restriction',
                    'access-restriction',
                    'file',
                    'internal',
                    'file',
                    'file',
                    'network',
                    'file',
                    'file',
                ],
                'source': 'Ԓ˥3ǆƮǋȢқмńô°ȞҕͽßӴǨОȍѱRǚǶҮщԪƙ˻ń',
                'messages': [
                    {
                            'catalog': 'ҋҮ˘ØΜͿźώ\x9fGЪҠϰÀbԜϔпĿĚƲԦõɎǳƒ˨ǻˋÃ',
                            'message': 'iԅˠԏtҚρύƹԫºFɈзƏΰуɑ0ƱŲǰůԕ҄ϗҶҪͻȶ',
                            'arguments': [
                                        {
                                                        'name': 'Ȼǂы nũͿаɻЗͿеƠǴϤӯʀËϐƗɣӨǯԊæÝĚΩ\u03a2,',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 909642.1007359809,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɥϬԓûˁ˵ԇʹ¼Wҗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212337.101472:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'цʌʫȟǊтĭɏΒТƌΌÑƻ/ŅÁǊȻȴkő2ʩԣԜƅƪjÈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЫȠνɾʼ˪ʀÎɦɷǱϦђ~dâʉɧŽ»Іš˥˨gſćzȩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ń\x94ʆ÷˲ƑӀŎǳĠ¹ҙɖ(ҍȪÎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͻŐҢҁξÀɚѝ~\x8eͱź¬ǠîɶȀѹεШ҆Ѿѹƹҳ>Їǿˬή',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ',ˬõɸҊȠ\x93ɣËҎʇӣƀȵҬҊЉÉɡόƙˋɉ˪_v˩ƦĄȞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȜЌöӒӑŶҊˋ&ƽɡćЮǉΛŞ@ϵқԇǧҰáαU',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃʋäĮ\\d®ДзбАԎVөҰͺWɫԉĪɇұƲȿȝϛ˜=ʋҕ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΐϞˁϴΓwďюƼ\x91ӜҗǱϼƪαɲѬУöƐ¦ňѕƃJ˃ɬèҧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŋȷòʞӒéʪΩˣēухRԅοǴ)\x94ņrľ×ԓŤвĔæȻʏH',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ԗ»ǦаӒψ\u0378·ӱɣǜŝŉĭѤ˚ҮˋĬҬǽƋ\u03a2ƘʁŒïԢˮɉ',
                            'message': 'ŇǈӃæӷ[\u03a2ɒѳ˓Ӊ˷ʾӖĚҟӗҙahł#Δ˃ɗɹƟǶвă',
                            'arguments': [
                                        {
                                                        'name': 'ƨƈщйѹɩˌĕ¦{ÑѾȏȍȮǖƄǻѡͿÕʫѰ\u0383<ǙĊΫƺù',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǦΗǶԜŻӔǢӣӝ5ȈԠДÄľΠʃˇҚɹϴȯƑȯʪǣù˧˅¨',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2691023274977282134,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϗǯƊҚϋԜΜѴƀæə\xa0ɞӀƘǂνùśѺƔüʅӫψŪǳ½',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 619388.5760952001,
                                                                        },
                                                    },
                                        {
                                                        'name': '?ÞΔ[ȼӸǼӑʝԟ˧EВӝśΜҷѫσ\x9eĹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 677756272628439109,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅɬϞѮū҆öŲƕÓǝ\u038dєǽҽɔӲНѷµ\xa0ǷȆĞĸѳĉͲ\x7fϦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '϶џϦɢВʓӊ\x82~#ŖΌĜ1Mʷҭӓƫʴ\u03a2шѪЎДϞԞшˏƏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǧʻ+ǬºĭҲ˓ǹǄΤϮЗʌЀ΅$ӷӣEîlȊEʦÂĲШÚц',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 889405.9922933956,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Úʖǘ˘\u038dƨe\u0379ќ\xa0ˠǖεÊ҅ӃЩΥΡ\x8bиǚ!ҀĪcɾþΟŏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1088679612917191893,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÓɟѼƉϓʇæhǥԤGňŐɁԦђ\x88\u038dǗǣЫɁ]ʣѵƑɽʏŵϡ',
                            'message': 'ʇԮǠЉǕҜѲ\x8cǿъΐ@ĜȇˀÎ˜Ɛ¤ŒЁƃʟӏЂќԌСʄҜ',
                            'arguments': [
                                        {
                                                        'name': 'ΕĲɞуˉʼʏ\x82пɚԬŰɷǻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĵǭҢ£©÷˯óƪƫyʾBȚƾ˲űϻɦȴǧдīƛП',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7421063173630651391,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҁϯ\u038bήɍ5ҫëԋɫЯȓȭżѨԧʎHʴïΡͶӸ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'άċ˼ƦƺϧӀȥŘʚͺtϝ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʊςЛ҈Ѐƨ҆ԃʑĜϚďłХ҃ĤѕЏώƴљÚҸƔı\x84Əć˹n',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8889890135093615730,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǘǡ§ðnɺ˅ҏοѡҰCƐпȪ˨\x93ΝЂŭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4819737604112810053,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҴӓƍēÇƶĐȸώҏѽ±Ѵ\xa0ŕ˹ɸԥ҄ѻЦИа˹˄ѦӫϐԑÑ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԒѤŻӃєҹɲħ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'IϽ΅ԇːҠӓϟϤƷŎ\x86ӈʹʞ\x95©˽¸ҩɁāƣƃľƘәlƖÜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǑʃћȼӃgɴӔҾѯҟjο\x8dɥ˗Ɲ6|\x84ÝÝϫĝІӈĒŁ˨˷',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÆӒΦƮҭYšƂ0ΌÒēÏɩȺԃ϶¶ƏԁƽԒЧÙϤǴʦ·ˣƿ',
                            'message': 'ėѺŞů\x9aſМͳʳǅԇӓ˂ѦȌѼЗÜǶvɢ\x9dť\x8c\x8eӣʆˮϒʈ',
                            'arguments': [
                                        {
                                                        'name': 'ŌʿƓɴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ԧ"ȔŞΌĔȻχɔʫќͷĿ˖ɍƍȩįЛʁº\x9cǾϳ¥ɔƹԋiΚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʢсӛ\x9e?0ѼȃӏΥ˚ϾӒĺѽȄīѸȌѧ¶ɨ7ŭоƤЬԫѡԩ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 810396.6717967754,
                                                                        },
                                                    },
                                        {
                                                        'name': '6șʙŵȟΒĈɑíʰƳӏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸Ƿҧȉ\\ȁɹϺʃʒʨԛʋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212340.666050:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɵɵϑġ˜Ԩқжˈ¢ЂΜĄρǏҵƚŉęǕ\x80ΦЫ#ʍˁƝQԚԢ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɐǚδȍӞЊ\x9fŹ\x80˭ұȮ˟ɷǒɆĉɑ˝',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖ˶Ѹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5354377255683633254,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƦȓHσˬǭӻˢ\u0378ԍѼƨЌԙċҒ\x8fϡЁħιЪ˓·Ǫq,˒ԓŮ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212341.012410:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҘГG˄ʄϑεȆёC˩Ҟȫα\u0383җʔͺ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĚUП³pϞ˱ƢΚμԓҕӱӱŢ\x88<јϽªΑȰǻ1Ԣć˷\x9eӅє',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'þ*úӁÉиˌ\u0382ҦвӣԢħɏȡʝʶġԘ˻Α˭ξƿɤёМт҆ǜ',
                            'message': 'ǥʭԒЯ˹ǰƬ\u038byѝи¿ʂ£ϤӃϏĚѫԛЙϵυĹϚđ˸·S#',
                            'arguments': [
                                        {
                                                        'name': 'ΰıЦӣ˫ђȵ˧ӅѰŕſDѲŦɦǿĭҤʻғΩʝЇÄĵȖ˫Ⱥʻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѵµňǓVаюȴȯ˂ʏԊӍĆÔӘνNƶҢȓȦƭŇҲŎХ\u0381ųʆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1953011247021164197,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҩԙŸ҉Ζʤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ä%ƘшZŷπӄϜЄªdбβ(жɦҤέҲȁù˄',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2203083922672122697,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƫυΝɺ˄jƙαɑñț^ѹˍʡ˟ѐʫlɞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ûĘϣØасΙƴоЭȅȄÛԘ\x86ȶň˟#М҉ʍīΠĞ\u038b',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'õǱɶѲU˳\x98ʁп\x93',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ę?ƺǿɑʶȂЋǒˎΔˠÿíğГѓΖƴѮƲˡȩ˱јđˠʈ˭²',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Hөɥԁ{ɚĊϪ\u0378Ǎ\u0379ËŅӗǃԝˇѻ˳ɹǉøɝʦ¼Ǡƈk',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȶԟʘȑρɎʯǹҡөӉˮт˛ԔǠıųҨɬˉʹʋÀ\u0381ηlÉƚέ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'λª',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Mȝ®ʇÞƳ²ĀŭYɶʭƈʹЬ(ˣÕ˚ϚӌлȎјЫɘ\x82đİˎ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ȋȓ¡ДʎŒӥСҷìмȸæҿӇȢ±¦ɷɪņȪʙ¢ƠÔǍөӷϕ',
                            'message': 'É\\ԏԊԆёϱő˥ɱĀǚҞҊñǇÆŽ{\x85ԨØĨƺίϑǞѩŰѧ',
                            'arguments': [
                                        {
                                                        'name': 'Ԟˑɥ¢ҡ×ӯ<ĢԅΚϒƟҕʹ\\ҕΉ\u03a2\x9bû{ƺȉвӿҚ˶҈ԡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǝǵЊҲҢϊЖď͵ȏДԑΓʧ;ǒ³ʍѡԤќΩӻǘǅӬӽҒ\x84ũ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038bͷǓŅ҄ЖōȽӉɹУȮʽЕW\x9fưöһ>jò',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǈďӣƔ§ŵȂɾěёʝ\x80ҥ÷Ў6Ä´ʍƕǛȊÆÊБ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212342.267244:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌʸя',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212342.354462:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓʉȱϘ˝Ưҟ¥҅ԉȕΰʙ\u038b\x9eÒͿҜҥξ˟ɗɉΈ\x82µaҜϘϽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4877871310808550664,
                                                                        },
                                                    },
                                        {
                                                        'name': 'MʵуĳΈņҩĵɇўė˾ǛŨ>ʒGɿɤѹĤïȅĸǦȳ²BāЦ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɊƢò5˞ӯHҷњȠѝřȁƕIӿÌǦbʥ_ʹȪӋø˨ÇȠóҍ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4697978521460260189,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x85ļ\x93ϩҁρɔ{YВηĲǫȵnłӛƷΩϤЁǸɃŃΆͺҭνĕ\x91',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'чȨɶʹӲϤԃéѷĂ\x8fЏ҃üΥdǜԞǀÁҠКМɩ[ȏ\xa0Óϕϔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212342.869421:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ү˝ȥӭˮψЀɳÚϗѼЊɨĔiϿѫӑˉɇàҎɟƜТê´ȆԨB',
                            'message': 'ԘɝҶƟӶʶӄвʭʣɡԗ˼ƈƝeƖЬǖƠŧǓV¼˽ϣҡÐƿʢ',
                            'arguments': [
                                        {
                                                        'name': 'ʤϙ\x91wã˽ŤĶɍýoʳÉбїѢȕĆрΚæɮ{ʡǷӓєȕƨʵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 742507970690389996,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϳÂӒʡɝӣΖʟĦǳB҄҄ɕӁ˪Ԁ˖ưʴħԬdӘӢБŘĴĢϛ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1950626333502431257,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Åӟȕ\xadɦҜáÄƁƞͳԨĢӇѯқƿγΟҰ\x92ƀ˒ɞҮѹѢӠɡǴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '9΅ńʱӨϿŃʮƆǄɱϺðɆɚԧÏbѺʖʦыʁɀ¿ʟ¿ӐӶ×',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȥäðͼȾ±ԄûͷҭǪЗʚԖҺ\u0379ȵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1031734179209579900,
                                                                        },
                                                    },
                                        {
                                                        'name': '˟υǷȠɏӓѤ\x9cʘx%ȡϻӍȡ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȫ˔',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒëэ?φѤБʁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӞȋӆЋџɚʃȠ`˴ȃÓЀŢʩџɐīǀљҿцτЬ˳ưȩҘ˒\x89',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇҒDǼűϚȁŞð˥\u0383sJϐћ-ʖĄƠƿɼɰÌúҰ҄ӤiƔś',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑӲҁϿҬv',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6575736203627111921,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'сzҲpϽćɆѷƯ\x97ƅņÃȝɰżŅŘңљʥ˄ΐԙ˭ťϱƩҪҿ',
                            'message': 'Ş|ґƄ\u0380æíMŇƣͽ\u0382Ӟɔªȥʦμĥ£Ε˘H϶\u0382¤ȷΧƌɅ',
                            'arguments': [
                                        {
                                                        'name': 'ˉʥ3ԓύpǞϋ)ńƆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5568533667745410355,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÐΓ¥ǷˎdҀϻňÖȧ/Ǹʼǘͷ²ѺŎƟϟϽ4Ȼ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĥɸ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҋʆңңÀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'жý©ǥţ$ȼʨɁ\u038dĤxӢǥǁ_ԣnҧ\x8e`\x8dʑ˻дĠǒmʙȓ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƄΗƂѶΌŢΝƤΑ*·öĆìƎʀÓҷ·ґŗҌ\x92bξίϚ\u0378ƹʰ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212344.352781:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺʟȗ\x81ҭхoӉϖҨɮЎȈȄʐ\x89Ҡ\x9dɪȜȫΓґȯҚК@¥ϹϠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩǅ϶ŇņƖ҃ʆƨҭԀ\x8fîϼԧ˱ɆāŁȥĳƲhԝιÔϿӪ\x94҅',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 878176.7952841643,
                                                                        },
                                                    },
                                        {
                                                        'name': 'åc¨Ҵ¯ҖƂkƭ\x84ƻʒҹʇ=ϫóɉýł҄Гҥ£ϸEϦӅò®',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȌΣӧdϢ˘όȧĤʨ˴Ȗ®ʵͳȥɰŨFЈӀѽƅҎ҆>ӥ\u0381ѭǱ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӧʝʱŒҀĈҞwȗʔӷʗÔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϟƳJTӱȗƐήυâӖÈͷΎԒęǂƍˋzȇҡÂ ÑЮ>Ȫb2',
                            'message': 'ѭϿƓӃв3ɝѤǺǪŀŚӃš͵΅ʿϠцӂÁƗˋƓ˒ŰːƯǺľ',
                            'arguments': [
                                        {
                                                        'name': '҃ƌęÆȰĀҼϱæŔŭҏΎғȂƶvɤ\x98ФҔɹ]ÏʬưґѲʋл',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋ҉Уǆ҃ƷѰ¯Ȯάԗ¥˛ЍҦŘƁȕțŞȦûкФҳύ\x8b˂ĵԔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɹҢȗҼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3346002619155806939,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϢԌɳɞǽǤŤҰŒŰȼˁҼӬұ\x99ɛɄӛʺұĨρ*ƤʦƂɼ4Ơ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'w\x8dĨɆŬ˕oŦτ´wǹƊԣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'І[˼\x91ʥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈӞ2ԅӠХɭğϵкŜӯȣȀȖɺӰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÙcԅωĒǖƫЯӰĢұÆ˽ʩҭ˱.ʤ҂ʾѧȮӘàѝǞǭħźȵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӹşӡ˭˛˫\x8așѝӰǙ˵ȊɒĐˠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѻȧЫʎłμŻļȎěřЧɎɼȑҦӠӤ\x9a˞ӨȨϊÐđǧʐʒϑÇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʞľΆ\x80ʱşΨȵɏʮΊϳʭǂȐȨʗϸjGӸѫͻЕԨjŗдЯϬ',
                            'message': 'Жˍěƥ9ԡʹѯбɋĞ\x8dœǄБ)ϟԌʞʛqǃγϹϭҕŷʼԧÉ',
                            'arguments': [
                                        {
                                                        'name': '{ƒφ˂ØԂҍưq˥¤ѬѳԉƳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'âĐѫ;ȍȹκˉӕũӈ˃ɽķ\x903ˊӾƢŶҰЫȱΪŌ˻ǜˆφп',
                                                                        },
                                                    },
                                        {
                                                        'name': '-ӘӟϘÕͺ¾Jʩ¯ӲŖʧкȴğӜ+ҟɓƻ˅ђӸѺΟĒϢύŷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '»ǑǣˁҔHЖ°Ū7ćŷɄʇƸʢѧ˶ϻÑʙӸϔǿȋўǐԫ˜Ƃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Эũʣ-Ө·ӉҽΧʔӆύƌӇҦιҞ2ϳEɍҿ£Ϫǀ˷\x9fǓĻ#',
                                                                        },
                                                    },
                                        {
                                                        'name': '˦ҽηũáӠӁȆѿŕө',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 4011.604242415473,
                                                                        },
                                                    },
                                        {
                                                        'name': 'іɜГǖɇɋ$ǨÜɘҫʽ\u038dҕŃϕϩ˼ǷӢҭ¿ǀæ6ҩК',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 752184.0535179434,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʄϐϓѡƟòGι˯Ҡ\x7fɬĪāɶƐǺҾэӹ&η˩fÊʹÌŬƲȯ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'â˨ә`ŵŸÔ{ʊė¡Ƙ˲ҾÜԔԦăÛ˸ľԉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ğҳ˧Ӂ˦ǩeԑȫǦáƋϟƧѮƤʃƹη±ĥЖQԟΤƷЕΨ҅Ӽ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћ\x81АȺ҄˛ӣɏ+ω×˧S˺ϲɔśʱpћü˩ɾƏşƼҿɍзԝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -13580.370753347888,
                                                                        },
                                                    },
                                        {
                                                        'name': 'čÞƱɩòĮɝύǠӋϠԞƇŦΎùϏϧжƬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ⱥ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 322803.0034415496,
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

            'name': '@#ԑ',

            'error': {
                'identifier': '²Ϩ\x8dȲ\x91',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ςʐ',
                            'message': 'Ѭ',
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
            'name': 'Ķԉéюȃ˙ϬßÀŨԮӰϟӞϻԭAǨʜƪÜьӗǱŅńɚÛqʒ',
            'version': [
                -6617004869434893480,
                -1073477345948503343,
                -2703219749407721259,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ΫDJ',

            'version': [
                -4430696749702724393,
                -1368078484145075737,
                -3321076452512874381,
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
            'event_id': 'ĩʑʐɐǢҊДǎȭБɝ',
            'target_id': 'Ɛ\x8d¸ΊҡҾѾưѰžȧƧͶӖάʀǰ˴®ǬҾ#ƨµǤɓӯĻυê',
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
                    'event_id': 'ғïΪ¿ǹ˅ñǴé͵ÇȒŹӭˏȽɈǜÇ\x9fҽˇĻэˡŕЙүÚԢ',
                    'target_id': 'šǨ˱ʧο˟Ǟѡ\xadғɧČƐǏԧ˹zщйʽ\x99өǯǑԙɓӚ¦ʏǅ',
                },
                {
                    'event_id': 'ĨϋˮɂΡƁҙj˒ĉΕӠŮǇΎʘ˞FƩϳ.ҾЈҗŽ\xa0ЧĲŵɉ',
                    'target_id': 'зҹ#ԡ9ÎȀ˃ʦӚįǎϥӹʟŶxȚǢ_ΨŇ˞ɎƒǸȭmϫѡ',
                },
                {
                    'event_id': 'č҇Ɛȋј7ІӾѫ^ЫǕĭɿ˵ԈϾÐӠɲTɶJΙȧǉćƧӥұ',
                    'target_id': 'ƴQӇƝʚƘƣӏɓƩоЏȔȮËԥȷŇƗλåϥːġɔ˅ӯԛХν',
                },
                {
                    'event_id': 'ͿΌ˟\x8e\xadʬȗƯŗİ]ūή˙TKƴӁԛƛŁ\x97ÒѤưŋМʸӍf',
                    'target_id': 'ȥͶȦǍǤʎĤǂ˶ƇŜ,ӣ\x9bΘɏ²\x9c{ÄҮТǻńοұϚ\x94ˬw',
                },
                {
                    'event_id': 'ҜʿKԢӥéͱÙҹ΅ʟɷ`ãĳĲǡдIȱȵҐaӗϫІ\u0380Ўņҽ',
                    'target_id': 'ɢŰˮʪ\x9cлͺ˖ӞʟȕķϋеɺѕĎS\xa0εГƻƿϑʝɒƭ\x92\x8cω',
                },
                {
                    'event_id': 'ΖӸОѾ"KŮāˠϑǸϏGŴхƗсƆɭєäƝήĔũaǘȬȌԞ',
                    'target_id': '˥\x84˕ˬnĽџԅӳ=ЭıƠУņʯȾνŎƫнÎŴƥПʬҲΣÞ(',
                },
                {
                    'event_id': 'еĳϭҳʤğ§5ӅϦХѲZÁ˗˼ĥƚǀԃχΏѰκМŬ\x8eԆʥʆ',
                    'target_id': '\u03a2ʃϠɪΪ\u0378ӴʄЋԔЧlњŠɊȐҝƦëųϪʥýŶ\x9ațʥƊʴΈ',
                },
                {
                    'event_id': 'ЮԖϻʓȅEЂѠџѿȬJ ϚǁͷɖșuΎĐ"ӲЃѫӀӒƘƅė',
                    'target_id': 'ȺԟԣɗԓЦӮƅǳ\u03a2n¢4]ҽҕѪɨIòGϬĦӳɉɠҕěżm',
                },
                {
                    'event_id': 'ĺƐѦŲʛʻχɅˁʎϴʇƬӌȿϡƝώ¹ɟƲŰȅҭ˕ĺɑÃӉӧ',
                    'target_id': 'сĥƜХ\x92ӕϨǻԥŨτͺШϺɈžаϻ0ӺƊϙЌ\u038dΏѶχʤ\x97Ѳ',
                },
                {
                    'event_id': 'ӍйӯЍʑΩŇҦñѯѵƿ:æңͳżʖрȺõʱЫϪԚqșʑЂʟ',
                    'target_id': 'ѱϝѠρт˟Kĭȫ\u038bѿˣєʀԘʥ\x8fǇʌӴºΓέĔǌ\xadϧ˻Ңӗ',
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
                    'event_id': 'GΨΞņϻΔӹƱϚƏӞ˹Ǘßϡ»х˞U҆ÙĜʇ2ϛ\x97Ҡų±\\',
                    'target_id': '\x8bǩÖȐĸǍíɧѾʙ+ѝԡȩҘƃѐȮԞїǀźȇгԃƪƀĄŋŘ',
                },
                {
                    'event_id': 'óѫǁψҒҟ\x88ϝ3éɚǽįӶҧʁƼ²ʧεöɒA2ч\u0381Œŗȕλ',
                    'target_id': 'Ӛ*ɏɶ]ќʂхϪ¡ϤҊӸ÷Çξ˙тů@бƣчǈԍϚƨӨҁ$',
                },
                {
                    'event_id': '\x88ˀĄƚ˕ĘƉˌɷͱΑfϺĚδŻŎɑ˸úьˏÒ\u038bҔɾ¨ɿə\x99',
                    'target_id': 'gÞ\u03a2ϽȊӔɖΈÔSѓΨƯέѨUʔԑƨÅ˰ˈ\x99ѓϰϰǺǩѕɜ',
                },
                {
                    'event_id': 'IѪϝ$Ƨʛ˖\u038bLBüƛӐΌѼÜȬԣǧɅσϖтэѥŭâʷӷË',
                    'target_id': 'ēǁԫЄĕΘЉĐȋӇΟƒ×ЧԌІεӪʳǑϙťʑогéėΎΘζ',
                },
                {
                    'event_id': '˩ĳθӋƗӓUaҼĎſūɐӧɫɦuƆΒɧĄÔʒ\u0380ԝȨ΅мŅ˝',
                    'target_id': 'їǵʓŰʩʉΊİӌ\\Ʃұ×ѕ\u038b¿ӖӥɋԠʼƤǆɰԊĭÒϵУǸ',
                },
                {
                    'event_id': 'њ7ВϘҮ\x8d®ԐԍȞӖӪ˗ԢϗͱҍӚ2Ç˧\x82ǭɯɸȡĳɞ°ɪ',
                    'target_id': 'ĄҮɂńҞЅѢϛƽЇȤǺϊcʍҵɫӆӥʼ\x87ʲʾǚǭųǂГΣє',
                },
                {
                    'event_id': 'ӰȳϗӄӴϵ˻ϯ#Ȉòɲ\x87ϊȒʏ&à·ŘƚÌʦͳθ4¹hȭȥ',
                    'target_id': 'ЙΥŞɩʉӊо?;ɡʰɂӘƮŔӰȕӨ\x96ǫʣˋȓ&2ƠΓȲҖϑ',
                },
                {
                    'event_id': 'MƽπũʵњҙĩϙʘʁȵΚŘΗрȹхÄ\x84І;ĖԞɴԀ5ŽĩЗ',
                    'target_id': '\x96ͲɠŔΗ¦ȂxÇ˶ʷǓ΅Ԙ¼ԤΣǌȮԩͻɬ\u0381ßÖċɹӶDŝ',
                },
                {
                    'event_id': 'ɍǥŗˈ·ȒƠϺ>tèԧҨȜΖʀӗĔԧƓŇԗ҆ĵ«Û˙ӧ_±',
                    'target_id': 'ϟȚƤïϚŲϟΞʎ¬ӗʹӥԃχjӶ´ӦΤȎΈҐÚЈΥUrҪ\x95',
                },
                {
                    'event_id': 'ţÎ®ĨϡƏəþĕϸМΣДԖƬό!ō˴Ƙ1щԩÎӘйЦГĭ˅',
                    'target_id': 'ʷԮ¦јģĐɪӘĻhӯДµ҆ΈҧǸӜпѧҬԧԐԨÙçԈǬҏð',
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
