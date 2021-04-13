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
            'name': 'Ɲ¯КљŔʄМĸԝƩϦѦ¤ƃɰӢϿǉьưϮřɶˮΜǜ\u038bϱƾ\x8d',
            'minimum_version': [
                -2287155317529881569,
                -8998859002409401346,
                -2772156184533314057,
            ],
            'below_version': [
                -2907412778187293658,
                -6999120087483327292,
                -3165047290787339509,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x7fФ8',

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
            '$': ':ЛΜϜԗĎù҉ČȑнŒϏϮǢÇʹʥÙ˖śΝыʻҕ7Ōɿңϵ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3964841369012443197,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 271709.2080793435,
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
            '$': '20210413:002150.549428:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'νʥ1ʵɿъÆҏϴʸԓʗƝ\u0380ĻԑƞɚҨӥǐȻ«ф˱ƷŻǩʣu',
                'ρȦτъ°ǼҐǓſ1ʜƧПÛɏ˙ϺӲѝĊӳΜʜ9ƚě)ɖ˜ˆ',
                'ȌɈȃŉąÓ',
                'ǛЎυˍČʨ¢ΥυęǹëиупȄȌƲǨѕǐ͵ǊȚôӐƷ§ęˏ',
                'IȽ&ј\x8cԋGEȭ\x9eȻѶΚŊҠȸϓͽϸȐIѝԝʬøǵԀƓUɱ',
                'ĽĳѩȌÌɴȚ˘ƉϓʈөǧˎҲŔàªɦ\xa0>\x7fҵȫǹū]ƥȚ!',
                'È˨сȴÊ˞бʡ¨ŮĦЭҬϙǤƎԀƴǑ:Ǐũƛ\x99ˍʲcŔҢū',
                'ƈώȅЉωɓœǺǥĔˊԠŨɩHÝΑþĻʴǩǹЭǡΧƱRƈɓƏ',
                'ƻ˕ćԂ˾КΔxяԗĐƯĴƿǳĿɐƺ\x9fˍɝĹѼƔĢыɯϬϘ~',
                'ɨͱē͵щ\x94ϤȜЪɭрϼ˛˻Џѭ҅ͷȳʎˎʐ˔ź\x81Ƃ\x9eϘȼΥ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                4167889285320212753,
                8489037069242933799,
                -14884484442297118,
                -360383900377993337,
                1112801494724842764,
                915847842397391426,
                1632728154718475683,
                4582516740385361808,
                4506306544631957122,
                8920667059530635393,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                48438.018246006046,
                820251.4103482164,
                589225.9717878166,
                72368.65247410076,
                911624.1309291363,
                449294.2066511146,
                400823.14575367415,
                58730.817637829256,
                971164.2989580557,
                890371.2684317487,
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
                False,
                True,
                True,
                True,
                True,
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
                '20210413:002151.604569:+0000',
                '20210413:002151.623904:+0000',
                '20210413:002151.644024:+0000',
                '20210413:002151.662366:+0000',
                '20210413:002151.680793:+0000',
                '20210413:002151.699810:+0000',
                '20210413:002151.715749:+0000',
                '20210413:002151.731016:+0000',
                '20210413:002151.746078:+0000',
                '20210413:002151.760583:+0000',
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
            'name': 'ԢԡĿƦ/œðʳƊʖĘӲȏʸȠΣɅӐέʻĐδ',
            'value': {
                '^': 'int_list',
                '$': [
                    -8710131402423013002,
                    2689893328425155695,
                    5228072274582897665,
                    7333538428706837324,
                    -4654534326486324206,
                    -1880254548970332895,
                    8850575492366315243,
                    -1952287335968619378,
                    8601897061331394318,
                    -9204780725648588058,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ԥ',

            'value': {
                '^': 'float',
                '$': 557009.194749148,
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
            'catalog': '\x90ʙŰšǔʪН\x8c\u0378Ň¶ςԟҁÉҳ\u03a2żǣ:ƒȕɣѦɵ¸ΑҳӤŴ',
            'message': 'ŷ¯&јЬǇ×Йȹʎυз\\Ȯ ԇÃͶG=ԡΟˡӁӪĎ\x83ҕřғ',
            'arguments': [
                {
                    'name': 'ŐӁʙш\u0378ζǶԖ\x83˚ʤ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:002148.624849:+0000',
                                        '20210413:002148.643358:+0000',
                                        '20210413:002148.663142:+0000',
                                        '20210413:002148.683894:+0000',
                                        '20210413:002148.701445:+0000',
                                        '20210413:002148.718983:+0000',
                                        '20210413:002148.736401:+0000',
                                        '20210413:002148.755191:+0000',
                                        '20210413:002148.773010:+0000',
                                        '20210413:002148.791002:+0000',
                                    ],
                        },
                },
                {
                    'name': 'МƑMǂԦҖĕʯȥ\x86ʡˈ<ѠŦЍ˗ѱƈҤwћ˕ȞɚĞ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:002148.889028:+0000',
                                        '20210413:002148.912598:+0000',
                                        '20210413:002148.931324:+0000',
                                        '20210413:002148.948887:+0000',
                                        '20210413:002148.966065:+0000',
                                        '20210413:002148.985450:+0000',
                                        '20210413:002149.010991:+0000',
                                        '20210413:002149.032277:+0000',
                                        '20210413:002149.050587:+0000',
                                        '20210413:002149.070279:+0000',
                                    ],
                        },
                },
                {
                    'name': '˥¯ѝȚƉϏЬȮȀ¸ɸͽˤ\x99ǑūǏϣ;ΰπӊgΑӼІίҾԑĜ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -2643378325650081666,
                                        -7180482770643322578,
                                        -5181308599790534540,
                                        -1706028708353831145,
                                        5428743901181610192,
                                        -6406522709085026353,
                                        -4503675681244658452,
                                        -5652561461013868543,
                                        5570933879548248599,
                                        -5166465141632011372,
                                    ],
                        },
                },
                {
                    'name': 'ʂEĪ͵И:ҷɏ:˲σӭ#ŚÂéΓЮ˳)ːӔ%˜ρʸˈƢήт',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'җҕK³ƍ҂ԁ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ӳʵνÏӍ\x88ћ',
                    'value': {
                            '^': 'float',
                            '$': 267830.936415799,
                        },
                },
                {
                    'name': 'Ѩ\x9dҗȳҍ˨ϛѳʣ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ϵԮιĘÍЭȨ8ȞǨνʷɇΜ˕јǝυӚȄǣͽ',
                    'value': {
                            '^': 'float',
                            '$': 432013.89087886096,
                        },
                },
                {
                    'name': 'ɡҞϡȱҰԃͽϽɚƨƸƻǢΪ\u038dѭͱ҄ЁÑư\x8eφǸvҞԏϣƻԈ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ΤÍ"ҍ\xa0ҵМê¼ƮŢƢnðκŤŎɶҬ ȼ(ϊӎԤļ˲ɎиǓ',
                    'value': {
                            '^': 'float',
                            '$': 412948.0115868956,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ȸ@',

            'message': '˜',

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
            'identifier': 'ϜðѰвԬеƠų˅\u0378Qāğĝ;ξŀăǃȟę\xadɖTÃÿԜĵN˃',
            'categories': [
                'invalid-user-action',
                'access-restriction',
                'internal',
                'invalid-user-action',
                'configuration',
                'os',
                'configuration',
                'access-restriction',
                'internal',
                'invalid-user-action',
            ],
            'source': '҄ϩν=ĕԤ%ƘӊЙѻŽÆ\u03a2˾Ǻ΄ǄԔ\x94δШӔ ҂ҴȝǏΦγ',
            'messages': [
                {
                    'catalog': 'ȱ\x85IˋίεǟмƊέӾԢƖǃ\u0379ӍԖ,ѕΣºɢϯðΒˊΏȖƟͶ',
                    'message': 'ʕԅ΄ȊˠD\x84¡әțƅ˺\x7fêĤʎƷєΔƂȏҭМœEİ>Ҋɤ˶',
                    'arguments': [
                            {
                                        'name': 'ºϘʵƢԄҝηˁ˷ʅĴƶņĺЍÂˉȱƳФĬȿαǺȠºØŤʼ\x99',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8113846750572546714,
                                                                            2485668899498262103,
                                                                            2126166489083872285,
                                                                            5032227908155648462,
                                                                            -1128067334688984918,
                                                                            -6322208092332731952,
                                                                            9002674850745408624,
                                                                            1270104314264925912,
                                                                            5205132553138097909,
                                                                            -3067864810304403045,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ТϻŲϵʟȿЀŗҽ¦ϗįёćӔʦЭʁʺʥЩ',
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
                                        'name': 'ʤӠA¡Ƿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002133.040422:+0000',
                                                                            '20210413:002133.058840:+0000',
                                                                            '20210413:002133.076409:+0000',
                                                                            '20210413:002133.093412:+0000',
                                                                            '20210413:002133.110131:+0000',
                                                                            '20210413:002133.127366:+0000',
                                                                            '20210413:002133.146307:+0000',
                                                                            '20210413:002133.163442:+0000',
                                                                            '20210413:002133.180171:+0000',
                                                                            '20210413:002133.198896:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'â\x81ԝˤǿ4їŏ|ģмªGєӰɍ\x7fȷʴɸ\x82ϚҲВΛųԍЕҿh',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002133.286666:+0000',
                                                                            '20210413:002133.304138:+0000',
                                                                            '20210413:002133.321561:+0000',
                                                                            '20210413:002133.340313:+0000',
                                                                            '20210413:002133.360697:+0000',
                                                                            '20210413:002133.378561:+0000',
                                                                            '20210413:002133.396187:+0000',
                                                                            '20210413:002133.413060:+0000',
                                                                            '20210413:002133.430252:+0000',
                                                                            '20210413:002133.451030:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȻΝǜ¡ƴϸ|ʸ%ȰȎɍ˹yҏɣφĮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'éĀӐμ҅ν˙\u03a2ɰǆŖԀ˖ы',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 374517.6186661962,
                                                    },
                                    },
                            {
                                        'name': '0ʶҝӔˇpŲȠɫґ_ȴϼ˔ɁĲӏѡȡǶщҭĒÍӶΕκʦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -25012.024327100095,
                                                    },
                                    },
                            {
                                        'name': 'ƿ˲ˮȢԤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            394311.56291793927,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0383,ԏӝҪĕɜƈÄҤӂʋџ ϕĉ©=ʱǮӱɈ˷ƞι˰ƉŢwӵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 737369.8222938775,
                                                    },
                                    },
                            {
                                        'name': 'ЬǨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˀǠƅƏԔɿɨR¡ΰÄɞkӾѱȗzȥɹʦØӱʋѨƇʋѵƢӿφ',
                                                                            'ӉƻŊ¡ƳϗӽĞʋĀĉˤΆȑɂ$ȊϨːƨǓƙΏƭӕ\x9eĲπ҇Î',
                                                                            'ЉĜқƘɲ˄m\x9bÝӮúͻqӆϕһήӻĪ˖ýƫǂǛƗīN΄ԢВ',
                                                                            'ǡÛǦÄț1ŤɣӿkÔӾȄʀȻ\x86\x99ƆǌǨʇϏɓКȩȋӍмӖ,',
                                                                            '·ΈȽηҚӀʳҼѕҲĥţԉÑ`ұˈХҾƣуǣÒЕĞǫΘSĔѷ',
                                                                            'ʹʒΖԨȚ\x95ǟϢŜӡȤˀŞǇԛʑǏǑԥ^űK#ªзϮ˭ʹԐӍ',
                                                                            'ӌĦԩ,ƱηΠɆƪIҗΒʼǊŰzЛƃ˴҄ǣAѕÕÅâҾЫÜʤ',
                                                                            'ɦҒȝ«ʔʛʾfҗѮ˻ǋMа҉\x9fͱǢȍʄßŨϖƈЈǌҔ˹â˟',
                                                                            'ƽӱ\u038bďӳϩғјĬãЦĊǊÿ&[ӷŸΫνԅȞÇѵРsӽЛƝř',
                                                                            "ӐӍЀ\x92ɤÖїьæ˅čӊϹӟϦƓʎ'ϷШS\u0382ĥ҇ȈADȥ˚Ɂ",
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x96Άэ˛µӬǢԈȥӱ\xa0ϑǁеϬӘҹϵԍВҟ˧ѰTͼĦϗΝüϟ',
                    'message': '<ȲʈNӽͷӋƳXɄĈǏϰ¶gΩÀԂοŔÍƅΰǮφɫύА1҈',
                    'arguments': [
                            {
                                        'name': 'ӨИҡƼ\x8cГӉ˓˱ԜřřΊϴӊˣǱΔǚʿǐџǏʀԁӑϱħĲĪ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԕɓºʴн|ŶȾ\x98ÓɾϝʒÝх',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '(ɾoǼČЙ¢ғάŜɯϵџƟĲɏйѤũҷǮȍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002134.598191:+0000',
                                                    },
                                    },
                            {
                                        'name': 'èŕđ"юŗ\x94ҋŵӚӅȈƴǌĞȦЛĄº\x7fʔіЂȷŞűˀïѺΈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'үӋɕǍƫ^ȖǴŚɫѓøɦʾvȂ˝чӝӮҘʿǒöўĺ\x85\x9aˏі',
                                                    },
                                    },
                            {
                                        'name': 'ΚʸȸеĜХĕƈgƖuȵΆˤ˹ȁĕ\x92ΔȑŻҘҌǽǍѭʍ9ïҐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҧνɼΝŵ¸³ŴʁηƧŔϴφeсʆĆϥjɌ°ŞǚǵƤŐͲɟǬ',
                                                                            'ҕҵƴʬӶӻӚƐǇӐɇӟұɳӚlϖơɷϑъƁ˹˲ŔƏº+űќ',
                                                                            'ǉӚ͵ΒƢӞҟӶӥɼʿũ7ϴÜŉπӐ˻5΄\x86ǌşɼԮѕѷӔо',
                                                                            'ΦӥǢɟԤ;Ԥ#чɝƠГD˧ЬӜѢĶѐСÞ«ԍ]ѕΓҼчҹ\u0383',
                                                                            "ęӰȬȶȭ\x9fAĭìÝÌЈΒ'rǠƺɄԡѥųƁ\x82ƧӘϟЫĖ˴и",
                                                                            'μαǮªơѲ;WѮFԄǨ΅ƬўɈɆƱ8˕ӌЦсүʛӤԊ÷ϥϨ',
                                                                            'ρӀ˸ɡȃ\xa0ħj°ȑŬ\u0378ϓӎçԇʈ͵ϷΤЯL}ϻIƇe˘Jˎ',
                                                                            'ҶƞtΞӘơʭė˜Ҁ\x91űҹʅ"ĩϳȍϣǈŴʿԔʕ͵(\x88πӆъ',
                                                                            'υʋΎTdмȝˆƟҶӽȃӓ˔҄\x95ΔɞϷBɳάlȷЛơԥѧԍ\x8b',
                                                                            'ǜҾѳ˸ӺН˙Ƅˈ\x93ȋ\x8eΕӱƂ¥ͺÒтԒǬăЌ_Ƨʁʔʵ˶ɑ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȒĆELɽĤЌȚјƤӉ˕ʬ҅Ǝ\x92Ϛʿ)fʲ\x9aƻƳɩΠʨɐɉȳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6236919041740066059,
                                                    },
                                    },
                            {
                                        'name': 'ʧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5244522154626355437,
                                                    },
                                    },
                            {
                                        'name': 'cĨӑȟǧl\u0381ɯcԅԏƦöț¼{',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¶ɮíŸβ\x90',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002135.462974:+0000',
                                                                            '20210413:002135.475798:+0000',
                                                                            '20210413:002135.490642:+0000',
                                                                            '20210413:002135.505427:+0000',
                                                                            '20210413:002135.522765:+0000',
                                                                            '20210413:002135.536732:+0000',
                                                                            '20210413:002135.550291:+0000',
                                                                            '20210413:002135.569560:+0000',
                                                                            '20210413:002135.585119:+0000',
                                                                            '20210413:002135.599667:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ăŚ˜ɜƃšӾ\x8d6ԏ˝ƞüԜԐ\x7fȗý\x80^ԙβŉ´ƑўҬȪҵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002135.670286:+0000',
                                                                            '20210413:002135.684273:+0000',
                                                                            '20210413:002135.698554:+0000',
                                                                            '20210413:002135.712314:+0000',
                                                                            '20210413:002135.725043:+0000',
                                                                            '20210413:002135.737957:+0000',
                                                                            '20210413:002135.753735:+0000',
                                                                            '20210413:002135.766961:+0000',
                                                                            '20210413:002135.780277:+0000',
                                                                            '20210413:002135.793900:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ұΰѭΠęЈŹ˓ƫ(ѵҎҜoφƲӃПģʒ Ԉĩқɺ½Ӷñлα',
                    'message': '҉ɀóͱѴӥ=ӭЛƉ҇ÅǣӋĴȼЩCԖѨ9Ɯо9ǭƄłʸαǧ',
                    'arguments': [
                            {
                                        'name': 'ǑԢ3\u0383ķŕя\x8b¥ʁƖԮ¨ԠԡԠàƌφǭӍɶĺ˷ƠǸǖɐÉɰ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                            {
                                        'name': 'ŻԂӔ.Êδȫɩѭǘɦ\u0379Ҵƕѱȵ¦ȵӓѫǙҬkĩõşӕČʪŹ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʖ˔ǺļÕǮȝʊ²ұЋzҕ˻ӯ˜ÈΡǦřǘ¥҉ǰĨýН=ȓĴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '¶ЂʓɯɖϦиİєкʢŇʣĕ\x87cВΙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5442731132261018918,
                                                    },
                                    },
                            {
                                        'name': 'ѝӴ\x9bԡȭўέſΝͺ҂\u0379#Ç\x99ѪǬȱ>Ŧʯд˻ßϐʁ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002136.698275:+0000',
                                                    },
                                    },
                            {
                                        'name': '˄Ǹ΅\u03a2ɟĬȰȣŰǈҩåфʅƪV\x8eΪǞƊÖǀӈӭЇӶүɿ?ǳ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002136.774439:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ћ˘ɯ4ебʼЌÑЃԩѷȀ\x88%ӼέƳÄŧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЎƸƓ/ԟˑɭѮȟ˼\x8bƩȾƈөҾΑǊҍǗ\x96ˣӧжƗ-¬ѧķȬ',
                                                                            'ŴϔʛшѕűvΈμɑȆӓʝԦʖҿˤ˪Ǥ΄řѬʢόưχԉ-uÛ',
                                                                            'ǀÆҔΦͱ҃бȗƞÁʐϩ\u038bҚɐ²ҽÝʮȑY˖ӈǀřUöÏoИ',
                                                                            '7ɍӆцӄѪЛɪѴmÏȤϚà\x87ˏʝχԆȐɭ|ŦǪҕǯ\x89ΔȝÌ',
                                                                            'ӏýǭ\x85ӆƂӆ˥_ğɠӸȏ³҇ӐʸpÌVŪɘμĩĜҐɏñȻ\x99',
                                                                            'ϟџɪʺЛŨϴԖŴýоhϲԇȺ˼мВ͵ţ¿ӜƋ\u038bźȮƲӻšƼ',
                                                                            "˟Σ҈Ѿ¸ɱω¼ʡʠãҬΊĹǫÏĹʜéȵιˆƔƌǾ'\x8aƌ҂Κ",
                                                                            'ԍȞԂǲɹl¬Ҫάȥϝ:ɖМΕΧēŔН\x96ӻґԤ˶ßʕ\u0379с˶˔',
                                                                            'ɋРƬϝ´ĝӀȆʛҘϛǠ\x90аġŹɛĒ\u038bʴĽˬȍƠȅƭ\x95ӟǫ°',
                                                                            'ѾȀ\xa0Ѓ˷Β4ʓеɰȞǆԟʂǿˑ&½:ȈНғɻ˲ȤȂΈȯѦɊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˹æçч',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԕƛȇѱøÄѽţƣƷӶύξϒмɷəĈ\x83ʱӝȵʝNąϬ)ԆőΊ',
                                                                            'ƬӶұґϙćƍþāм\u038d£;ӜҞѯɸǅƢŗϠĲÃҸɮύŬӡϋǙ',
                                                                            '˦΅ƫ˺ĄˤťʮɄȦ_ѦѦˣϔУĔ˃ӕʛġҶӣȶĵĮӡVҺĽ',
                                                                            'ˌĵӠӮϣьƅfʣĶʅˠǮЮҠˎ»ӃҢʷȀӹŇÓ\x88ӿǄɦĒћ',
                                                                            'ʸδПԅɝǞБŮҾќǜцдǡ\u0383ɵӂȅάɭµ[ťǧӭƎҼАϭϮ',
                                                                            'ХϋĀДʯá˲ÀäʝǝѳÎƗԜΜ=ŗΰӗѓĒчωФȬНһщӔ',
                                                                            'ӵDȶҰÅƏͳˬ\\ҟmɑϚǋʆcδȌnаŒѠĢ8ώ{ЀΎ;U',
                                                                            'ϑъÄԖϋѽЌӷĥɵԦғǎΨ\xadȈ\x8aʬǎĹ<ǢȑƣðϴʥJϘφ',
                                                                            'ǺЬБҷ@Ȗɇ\x96Ͽ˴ϹӚǚԎkɠƆȐHμԌС\u0380Ϥƙΐĉʃĩҗ',
                                                                            '˫ӅӏǩϓɕˌԠɕіņȺÄͰäίˤƵȋƹГ\u0380²ûШ÷РЧųӖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˜˘ŕǾâŷκ4ϤǩςÙΠːȜȓĘĴĂӦď˫ԕ˷ǏƭІαˁҜ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'мͷǃìƠɟϓϷǄћǓǃ\x8cͰлɘŅˌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1570876325638566074,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x81Τǐ˧ÉјoɸƍҤЎǱӕˬāϏУҜѼSÔӞȎэϪŐȌɎǕ\x94',
                    'message': 'ӑӬӊω`ȓȗϐΉś\x85ĪǹŪ˩ҹҷПӉã\x8dȮԘКҧ\u0383ӻЫēʥ',
                    'arguments': [
                            {
                                        'name': '\u0381ʅƱĜԜßǀ˶҂ÎȓаúÂƄǟӣѾǢƢɱńϏʨ˞ѭӨκӢƈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            329802.67474608135,
                                                                            203520.90913961426,
                                                                            720838.0163308274,
                                                                            -34442.04584080681,
                                                                            675529.6034694236,
                                                                            693690.7937780131,
                                                                            76050.39226604888,
                                                                            99203.02959958365,
                                                                            358528.40494355076,
                                                                            870684.1238334231,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x87ϾĈĄȱŽĈòŪӎÑʟ˰ΐǣцϗ]ӾāŊȭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 923926.9213641401,
                                                    },
                                    },
                            {
                                        'name': 'Ő¹ĴΗȘδřĿϽʮɅɜƱ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002138.126789:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȐϐҏıćǇőӃ<ėƞԒĐɐϞчԧȅлӅkʲ\x96ұӯʩκԐÖɇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 562522.6757771365,
                                                    },
                                    },
                            {
                                        'name': 'ҏԈ˰ʭEȻζKɇt\x7fҫȡƂ×УÄēɆ\\ɞǅčӑђѺʵы˼å',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4875744166581958381,
                                                                            -780936331822193879,
                                                                            3081980755016247376,
                                                                            -4896277410822841775,
                                                                            -5164138370773705233,
                                                                            9156672921259466798,
                                                                            -2451594122616975247,
                                                                            1609178470484434712,
                                                                            6719705576295641152,
                                                                            -5707274405474902207,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϲǏѺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĥŐ˱έȜ¸ɆӬȊʢȫƅЯȝҢǪԕҤМ{ÞћǗΪơɒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002138.598463:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŔƻԧЩØ˻˳ԄЂЎÑƚϝĤїɾΊôȂΉϒþűԨφ¾˻ɱ»π',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '(ƹԙϱǃЮђǃШϩʑϊē\u0379ǺӜɱӰɝԚ¾íû·β˧ʲԙȷɦ',
                                                                            'Йƹ\x9fњŃ\x95ÄȸĬƭȧƫԃұì\x86ɹўԒǒƃцÛä\x92ӶŇ÷Ɩѭ',
                                                                            '͵\u0381ԣӁɯЧÈû˃ˬΈЧ˃ΑQϹłԐ:gĻҭʮԧº˶Âεʨˮ',
                                                                            'ѯǩŮц҉ǚǭ˦Ā÷ȁЗϒPҚӨØҦ½Õ҅ЧҢѡxȊ\u0380ңĤȓ',
                                                                            'ҕ˼ê˥øАʽâԖƸʿʯͳMĀӧҸĢʩ\x86ą҄ŷɜɣѲҮЬ҅Ș',
                                                                            'ёǹԑӊȅӈ½Ԛ˨ϜοЂьːŎƠĪÑӂʟɯ҉ȅ{®ʶοķǎʇ',
                                                                            'ˮѽ/Ȃȫäƺ˝m϶ȎʨĕсȅЮӌѦϕIǳԀÆǟˡǈ¹3үѻ',
                                                                            'ҚɼŤǯŉʉǷʶȜęȟÃɖuԠϺ.ΆϠýǨӨҞҴƇРĠȊÙŦ',
                                                                            '÷ǉ\x93ʄ\x84ϧɷǸжʣǻϱӣǟƳFϱ˵÷ӞΏяѯ˕ȱѼэd\u0380є',
                                                                            'Οԗǵԭ»ȒНĘϿ˙Ė҄®ĴʣÒþАƽǚӔӪʽЕεԠˉѳ\x89Ȭ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӁȴȪ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѦωʷŠȈ¼ʹӍжɨҺSЃԟχϟʰáψʔÉuƞ\x80ǝ&ǔ˒Gƚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            969136.3305147276,
                                                                            53699.90718448462,
                                                                            398440.89665518573,
                                                                            571600.0616559489,
                                                                            418385.14499822725,
                                                                            575858.9763664932,
                                                                            978007.2456740432,
                                                                            979466.2953374011,
                                                                            321388.5342125781,
                                                                            816531.6637387275,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÔWʲЧͼƱƪɱĬξĚ+ЌϦȲĨǾ«ΌT\u0378ћ0ǮқÞʉΐһа',
                    'message': 'ġūѷʇӤŖӋёИƻҀʧͰɠɘςƩ°јǮѲˬˢɚú¤Ƌʈʀ¦',
                    'arguments': [
                            {
                                        'name': 'ЮюȤГшĉΈƧȥѨȉƴԁˠTүɒ\x93ɨҠ҄г',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŝp\x9f˫ZƐǡѯΨЯʏѡνѧЅȰş/ȪвΎƛX҉ʕп˙ƉӔз',
                                                                            'Ŷԍӭ(ӣˎčƳ¸ҒҡиƽϫҬÃɌӿȋӺѤėĊҪΒƷƔђίϛ',
                                                                            ' ҋŲԐ˦ǻŒƑÖШʹһІľиTк˜ȊҜȟʱ˹ǖ˷ĠͽԨш{',
                                                                            '΄ɃʌͲўԫδʧҙЩĴϒȦϙδǻϭǩƘ˶Ї\x93˘\x99ŞͱƭԠЙϩ',
                                                                            'ʄøӫǲɧƦҢϝŌƛȖ\x9eɐ\x94ӋÓ¤ғ¯\x92ʆΉ\x9eżӺĶɛƯѲʵ',
                                                                            "ёZʛуѣӢˍɅϺŸ˩˃Zǹˡːŋ_ĜѵʖʓӀǲ'ÑųǚƢƪ",
                                                                            '\x99҇Α¹ʘҚɩ\x97Ԩҷŵ¤ђʋƫʀԇˬȭӠԡȣԜԭпňâΘǓу',
                                                                            'ͱǴΤèŖ®2ƹӴ8ҏ\x8cƩӈԜɜˑӖʏşõêϏĥȉoƻΑƖ˳',
                                                                            'ϧĬюľϴӿȲ¢ԞÇʤӊԦĐəĥȩˢҌΈ˹ʴФĵ5ЕǔĹ2Ԝ',
                                                                            'ӵŅʍǪǕωŅęҞҏ:ҧȥȌҰŒ<ŎʥÞ6ŝʹӏǋɁˑԡĽǼ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'đ\u038bǤ\x94ɌЬǁӦʨӊü',
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
                                        'name': '¬éń˾',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǇԞȫıȽΗǱθŸт4ɧԬхŮɞљɋϪԥʮҬʮŋÑǻɥȘӸψ',
                                                    },
                                    },
                            {
                                        'name': 'ɛӓʷӃԫρǮёѯΔЦĤÐŃ¬òϖˉƖǽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            371862.52226325194,
                                                                            359728.9558191457,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʽϊӏƉ¤ΆrƧΥɟƣмωǌƘѴʜӝƝĕЦ˵ԘρІΘҳɥċε',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002140.049569:+0000',
                                                                            '20210413:002140.063470:+0000',
                                                                            '20210413:002140.079027:+0000',
                                                                            '20210413:002140.092003:+0000',
                                                                            '20210413:002140.104629:+0000',
                                                                            '20210413:002140.117918:+0000',
                                                                            '20210413:002140.131342:+0000',
                                                                            '20210413:002140.145381:+0000',
                                                                            '20210413:002140.159017:+0000',
                                                                            '20210413:002140.172109:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƼіʪɴðϿϑΚϬřґƗѶˆѡώWĆǷƤӾнӵIЃ¡Ą\x87ʾΉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 729445.3185051964,
                                                    },
                                    },
                            {
                                        'name': '6ЃѭӔȼȶ˜Εǲɽʣ¼ұζȁʅˈӵȏЍ\x85ҐɓʗƷөБ˘ȥ©',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'кНdʃ\x84ʠϡѻ˰ҢΙĀҍӊϤͿǷ]ԬȶǂkŧͰ˼&Πĥрϴ',
                                                    },
                                    },
                            {
                                        'name': 'ɣҸηŠɲʋѕƛ`ƗĹӽȏGȦ˻ǭ˱*ƻʪˆʂѪғӆѦү§ß',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002140.368474:+0000',
                                                                            '20210413:002140.388070:+0000',
                                                                            '20210413:002140.405305:+0000',
                                                                            '20210413:002140.421894:+0000',
                                                                            '20210413:002140.439293:+0000',
                                                                            '20210413:002140.456747:+0000',
                                                                            '20210413:002140.474066:+0000',
                                                                            '20210413:002140.492185:+0000',
                                                                            '20210413:002140.515278:+0000',
                                                                            '20210413:002140.536668:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӏʭî˼Ǆ\x91ўπř.Ҭʈ¢ƱѹëˈҜ3ËȆҪԀyϫ\u0378ɠƆ¸Ư',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 133405.1296707234,
                                                    },
                                    },
                            {
                                        'name': 'ʃκԆЕɣϷˡCϹԐ$ӳҟǺӄԊɉͿ΅Ɋʹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȼ˙ťʫΧrѴӶқȄӲЦ$ɀJƩϳҭȹČщкŨaҥӖƧČҙŸ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʩІҊʙǒҊďʽϰ\x96ǿĶʲƖʂѺǘҪηόƶӺo˙ʌҎHӢUƖ',
                    'message': 'ēЌǳԂϺRɁ˖QʼǪƎćѤеӽЧļЫμ\\àө͵ùϯӛǍʠ\x97',
                    'arguments': [
                            {
                                        'name': 'ϧ{\x94ȀĀϪÀ˝Ы°ȶ˕ʅӶĖǓİɀʦͳɡĺϋšӮĀŊŗӋŔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɀƈǾʸ\x7fνƒǧZжçǃdǴȶ\x94ɦËԚԡ!ɆҺÙЬəȽΤК©',
                                                                            'ĸӔɃʭȒҦÎ³ɝ\x9f΄¥ΌԭţǶ\x9dËɘáýĔӆɻŢӪʏ?$ы',
                                                                            'ԓуǢҕ®ύǢRмЍϣҤaϭЬǱłҚPˀԌћǒū2¤ӰZҾț',
                                                                            'ƘʏѶ˖ԫϬÌͲнĢӷӝϒǫǳƅ>ЗϻʚŚǯđзįśР˷ǂ¥',
                                                                            'κʟƶͷɫӹѱƃɖΉTŴӯ˻ɏǼъ\x81ƦĒîɜԁј9ʷԩβљW',
                                                                            'ҾƌήɐΎ©ȵĂˤȻҨ¤|ξƞђAɚĤς<ɀŵ¨\x8e˝Şšҁҭ',
                                                                            '"ƞĿµʔʫǞ϶ҰλҰԈǨԎԒĤϻɞʬђ°ǨǙĠѳЎĵ˾Ɓϣ',
                                                                            'Ͳ˕ƽ<ҧǷ˫ƏԤƛǞĩȊĬʅоÒйØӮʸʘάűǢВˉĿ±O',
                                                                            '~҈ÚīΧǟȼĲԦǯЯĆʦԉȦ.ΔŲʸѾɝκΎҿԨǑśǢz¶',
                                                                            'ÍҡϞœŹрκŤţĘάқ¯Ͳư\xa0Ѱǎx˽ҹƬΰȃҋçǑϕ˺ҥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6515821060428923670,
                                                                            -8548625624357411473,
                                                                            -7067211766180101941,
                                                                            2183636888150669870,
                                                                            3211081036887574375,
                                                                            -3299245331264544682,
                                                                            -6757439480099510730,
                                                                            -1613290587945382154,
                                                                            -7251775746554399457,
                                                                            39012174481679628,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȺȎͻϡʃōɄΚʀκ¦İ¾ѧйòĜŨУѠƽĕ=ӆѷŒƅЗɮĴ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'Yϯķŭ\x90ɌӧKԈѿˏąʬǸŖ\x96˭ӬʓʞƝͷСǉϛʳȔԓҀϰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѡԟěѡί\u0378јǤǌőҪ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ԟÍȾԙϵ\x9cɕÊљѻȰƱXıƢƻͳʀΠĝĴ΅Ģɻ˜ƍGЊѰϦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002141.884754:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǬϘŌÑTęʯʳӏʪˊ\x84ȹҪŋƩԮƑĴҠ©ғȰǧĤЖӉɄ\x9dǧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 178914.3769130425,
                                                    },
                                    },
                            {
                                        'name': 'ȼțӅʰÍҐȠ*ΈѰȅϿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1248905763660606400,
                                                                            -7840061968171808741,
                                                                            -5321267076184854127,
                                                                            -5972484788597728118,
                                                                            -8682703154922370819,
                                                                            6196917579415525276,
                                                                            -591784057549620564,
                                                                            -9185741397796748609,
                                                                            -8523177314469354090,
                                                                            2058344945066148329,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӐԪӽǢОƬЕǺΪЁäЙӶѾ\x81Ҧ˺',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002142.364597:+0000',
                                                                            '20210413:002142.385285:+0000',
                                                                            '20210413:002142.403986:+0000',
                                                                            '20210413:002142.423324:+0000',
                                                                            '20210413:002142.442145:+0000',
                                                                            '20210413:002142.461784:+0000',
                                                                            '20210413:002142.479776:+0000',
                                                                            '20210413:002142.500220:+0000',
                                                                            '20210413:002142.521753:+0000',
                                                                            '20210413:002142.541621:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ϧĵҒΗʪʝώ)ʶЖĂˁΌȥ˳ΪË'ŨϦAǳB=ƚˬȳ6ԧʸ",
                    'message': 'ѴҲļ0ȹьƯƚ«ϣԨȅģǺєʸȫǑҐƁƭǿƽȟEιĬĩɁJ',
                    'arguments': [
                            {
                                        'name': 'ѷҁȢɭǁ˖ɤŬŒʶ&\u038bŜтƖȳǞӬҀϖ˚я',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƧӅɆɦȩûԉӑ¥ɂԍÞϕȨĉҷԕЏЩԄҥƪҼʇʉȊņµЅԪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            949161.2340654444,
                                                                            463313.455189168,
                                                                            850064.4083613663,
                                                                            -91636.08383175067,
                                                                            -55.389681425789604,
                                                                            682655.2730989528,
                                                                            -70262.7006785785,
                                                                            280958.5139892049,
                                                                            666752.6385610282,
                                                                            949613.6215239926,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӶҠĆȫÜƾʗèǾʚΗ҉҇Ԁԕөª2҆Ǿκ˚ĘʚĩоϞ\u038bɨ=',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 994534.8262748511,
                                                    },
                                    },
                            {
                                        'name': 'îƮ˘ԗѥÃñɶŅ\x9e\x8fҟ]ǑtʼˡDҙõүӸŒҐŁ\x95γ>ӳγ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3011046682641882824,
                                                                            1793791913132879872,
                                                                            6126726902871414696,
                                                                            -6248426631579094716,
                                                                            -8269824100095623089,
                                                                            -5379870710057887807,
                                                                            -1453451285280050509,
                                                                            -4674023532333602133,
                                                                            8869525233753874601,
                                                                            7445516311092887223,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '©Ђ6zљŻȼŅӲÏЩɶƱ]ϸyσԣ\x84>ʕ0"đźʚĴ\x8dȊθ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˌдȠ˥ʍˈҌôiȵ@ƿ\x7f,ϊЦͶҍӨѳ4њ˷ӌÈŒǝэ/Ҭ',
                                                                            'ЊŖȐΞνǃϲϏʈȉͼΜʦG`ϣȏľǐŢʺǿҢ5íӛǋ#ΧȌ',
                                                                            'ьϐŎ*ҿćϲƇĬԞ\x8dштĹϼĉўҌǽɣȦҖȤ˹ӸɢúԕԣԎ',
                                                                            "'¨зɣϧΈæÂSĽǘɪ˧˘әʻƢ·ӿʢѓÆ΅ӣƥιѭΘȟϖ",
                                                                            'dɫǟҗÅŒïϨȇpѡѤ`Ȼɍӿƌ\xa0OŁу˒ư±¨ҠÃʷƻ\x94',
                                                                            'ĖšɧԤēӻ&ҘıҾȡʲԘϏƛŮЃʹÛƦ\x87ѫ©üҙЬӀʀƘτ',
                                                                            'ˉΤǤ~ТǚзɀȲʘԮőÛЭϓu°ȍˈǧȀԢ¾ϿpԒɉΚПӁ',
                                                                            'ɂÐґÒѹɓΫηÇнʴΚ˵ӏ˭ˈʖǒ҆ӇxӑźÄЏ%Ȗϲк¤',
                                                                            'ūԂѷѾѰåĦȗΘ˓PðȄљʣɜʹϹҀԘÝŁ҄ǁЎĉQāȇȵ',
                                                                            '?˱-ʚ˅MōƊʳĴВψİǖȕƵ²˧ґØʙϔǸҗɽįԣȺҋб',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ČșZȸѦ\x90Π²ȾԦә\u0380ĄbљΑôŜ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 943485.4130870944,
                                                    },
                                    },
                            {
                                        'name': 'Ɯʄ4',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002143.688305:+0000',
                                                                            '20210413:002143.706256:+0000',
                                                                            '20210413:002143.725946:+0000',
                                                                            '20210413:002143.744674:+0000',
                                                                            '20210413:002143.764446:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϛŕίȀԈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 46833.84369924464,
                                                    },
                                    },
                            {
                                        'name': 'ощ@ǂпќÍНėÒϬ\u0378\u0381Ķ,ǲĮԑƵψҴ1ȝѹѝŠӯƨԓξ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ćѫɦΧӲŔѢЭԬЯǼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Õ҂ӹΖŗζǶLıƐЛ\x8cΉѣ\x8fӻαҗƮԌеѕ\x95Ť£˓ʳɍ\x85ʵ',
                    'message': '6cюɹ\x88˫˷ӊËǓʩpΜфSÏ¤ʛ҉ӊɻŢǈїǓ\x9dįҸʴğ',
                    'arguments': [
                            {
                                        'name': '\x9aӰҽ˃ԓϝϛіȽćĠisŅƁ\x9eѴʄϱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6671329546040897503,
                                                    },
                                    },
                            {
                                        'name': 'ӾԢӬ\xa0ɗǒȵϻΑϹťɫŲǹӜѩάёӖǃƳǵˌĵǪƼҗʊЊÃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1716924397150453919,
                                                    },
                                    },
                            {
                                        'name': 'ʆϋΟɂԤ»ԉ\u0382ŒԄ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ϊ7ңƴƨԦȰĊåӂǑҙЈŘЩƢɮɏąʊӏʑȢԌЮ\x9d^οэϣ',
                                                                            'Ƚɬʵ\x81ǸǲƍrԒƀҐ҄3ÍåtɓȰ˭ˍƔßӖУ#лûľĖԀ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȁȵ҄ˌѩѨ³ĽȯŅΝǓ\\ʹҧɿ×Ƭ˳ǻŋāú´ƾИƞȰɄδ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002144.672514:+0000',
                                                                            '20210413:002144.696365:+0000',
                                                                            '20210413:002144.717978:+0000',
                                                                            '20210413:002144.738676:+0000',
                                                                            '20210413:002144.755938:+0000',
                                                                            '20210413:002144.773811:+0000',
                                                                            '20210413:002144.794097:+0000',
                                                                            '20210413:002144.815122:+0000',
                                                                            '20210413:002144.832075:+0000',
                                                                            '20210413:002144.847887:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǍYǼĀÆǈ)ɲȪԐʻɒǱӢЦӁǼ˽ĆŌƙòѫĂƆ`ɾӟ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002144.937776:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϧʴʺÌЉǮŀӬļǫҿ\x94˥ЋΧΠӁƢ¿®ŃӘǹҟƛϽʌХ˥Ň',
                    'message': 'Ӫɬˇ\u038dȁѕɲǮďRҜ\x8b{ƖÂĈїȃĿǮИ£Ǭ\u0378ķȩ2љƚЈ',
                    'arguments': [
                            {
                                        'name': '³ӚƧŀəɎűρ\x9bɣǏҳМ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9101191056730099033,
                                                    },
                                    },
                            {
                                        'name': 'ʵȩ¼ΟɷϠӕ,ґĐ\u038dʤԞǌ˩Ә:˟˄ůЍ`ʒȐÌȯǑʘѸˢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 866437056263864664,
                                                    },
                                    },
                            {
                                        'name': 'ΥʈÇƓʴ2ĥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002145.243754:+0000',
                                                                            '20210413:002145.261921:+0000',
                                                                            '20210413:002145.279534:+0000',
                                                                            '20210413:002145.296735:+0000',
                                                                            '20210413:002145.313348:+0000',
                                                                            '20210413:002145.330830:+0000',
                                                                            '20210413:002145.350504:+0000',
                                                                            '20210413:002145.367962:+0000',
                                                                            '20210413:002145.387005:+0000',
                                                                            '20210413:002145.404189:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԉȟɓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5357156531999693292,
                                                                            -3649529086894141064,
                                                                            8800125374454106228,
                                                                            -684332336841060852,
                                                                            -2200476871712986615,
                                                                            1824803350875994187,
                                                                            -3280389430689772329,
                                                                            -5771074379024520370,
                                                                            -5941465843844684001,
                                                                            -291069793258493101,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЬĎ˳xѮȅɅҟȻȘϾŃѷӰǾԦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 621511.4083442887,
                                                    },
                                    },
                            {
                                        'name': 'ΑμЪǤγoQУβϏɷɌόÖʹÀ͵МŅԎěӃƜџŠłӤȍЍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002145.786208:+0000',
                                                    },
                                    },
                            {
                                        'name': '^ǑТԎʎĸӻϭĻ˂γơϼηϤʀâӠ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'ʺ\u038bĮƦҙǔȼōˋ0ɜӆџǾ\u0379ˈҦ˵Ҳ×\x90ϮÿҽʕϑˉюďÛ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ȶɭϣŚνƁʃyǿӋĢʌǫ~ƦБǒӳөԂǏԝȯ˺ĕòƼŦҲӇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            768328.3303159572,
                                                                            -3966.203243869546,
                                                                            589315.9602691308,
                                                                            180930.640338669,
                                                                            908215.9531974844,
                                                                            -61257.070034951365,
                                                                            747418.1922399816,
                                                                            815276.0779112661,
                                                                            866119.3911915637,
                                                                            448760.38190922735,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԩÓ˖R9ßԀɪ˸ˁɡѭӥˍϿŸ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɱЊ˚ʓɘıÕ¾ЎłКΈȄ{ΛʆÆ\x81н˴Тʦȩí˶³ƫñaȫ',
                    'message': '҉Ƴ\x803ψ«Ȭvȹϗ§s°нҹɌȩŸqwІŹѹ˦ѮƞϭԢ\x7fĉ',
                    'arguments': [
                            {
                                        'name': '\x90ϚjT˼_ĊҐѡώͲǐǘҌϐà',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'лԪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʯ;ӻĹĜçśçΰԙķкtńύш\x91ύά\x91Ĕ#ϼԝɰǟʇƫƫž',
                                                    },
                                    },
                            {
                                        'name': 'ÅЙeӆΟ҅йϻϔѣ6ˋƩƳÕƐК|ȣгν',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 873707.4392935414,
                                                    },
                                    },
                            {
                                        'name': 'ǦчƗȊŶʽϞхџǢƼԩÏϡӫĈԢîБӱɘ\x9aȳʶßǑ,ɇ\x90Ϡ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            258957.70954158582,
                                                                            659009.4678499389,
                                                                            557797.5728312155,
                                                                            -4497.176107359075,
                                                                            335664.88408134837,
                                                                            435401.84461436805,
                                                                            655595.9351455746,
                                                                            179951.66261752782,
                                                                            372986.5583839907,
                                                                            132523.46062139,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǕҊĥʍƶЃǓӾь',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 655235.682490061,
                                                    },
                                    },
                            {
                                        'name': 'ǍŮԫϴһóȯʾъ\x8f¨Ыąªʎă',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:002147.438982:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ƶä˧ұ˸ч[ôˡԙϏӺ1ķ҂ưҚҊÍӷНʕԉ@\x86˞ʔ\u038bȿя',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'Ч˙ϊŬԅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϘɂԟşħӼǟэ˾юˀ¼҅§˯ȩҥ҆ѿ_ģϪÏìІɚ¨ԢӬʎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            345380.0512743592,
                                                                            203587.11180371058,
                                                                            389626.3229724762,
                                                                            754550.1476820452,
                                                                            331761.8435359152,
                                                                            639966.7554189764,
                                                                            294924.9687948258,
                                                                            30061.70400769393,
                                                                            852794.5147869586,
                                                                            564858.2559022243,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ūґȮˡ=2ıҦԐȈԝϭŤР˔ƻ\x9bʱŽ˔',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:002148.135093:+0000',
                                                                            '20210413:002148.154239:+0000',
                                                                            '20210413:002148.174194:+0000',
                                                                            '20210413:002148.191931:+0000',
                                                                            '20210413:002148.211753:+0000',
                                                                            '20210413:002148.229821:+0000',
                                                                            '20210413:002148.247074:+0000',
                                                                            '20210413:002148.264539:+0000',
                                                                            '20210413:002148.282287:+0000',
                                                                            '20210413:002148.300785:+0000',
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

            'identifier': 'ИlӡœӨ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'ə҇',
                    'message': 'Қ',
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
            'name': '˩Δƫ\x85[ϼ\u0381ĉ¶¼ͰӰӡʹҚɒȌȳ',
            'error': {
                'identifier': 'іϖÀωђӰĜƭŽѨǒŜѿΤùЭ\x9dϓmÎԋĽѺҐТËšʝȟŽ',
                'categories': [
                    'os',
                    'file',
                    'access-restriction',
                    'os',
                    'file',
                    'configuration',
                    'access-restriction',
                    'file',
                    'network',
                    'invalid-user-action',
                ],
                'source': 'ĽӜ^Ӭ˻¹ˑϿøЬԋɖϊɸжͻ~ϡRԋ#ĐӾɑƮʍ\x8d\x99Ԣԋ',
                'messages': [
                    {
                            'catalog': 'ɽӣϰϓӿЗɀγ͵ұTdτзǆ˽ѓőԂRƹƁĵԎɱɞ<¼Ƶӆ',
                            'message': 'ļĄɛť\xadǞ¾ԛРŁЊЇҿЀʯǐЋ\x8bˀǏԚ·ǄρԄѸ\x9cƑ©ҿ',
                            'arguments': [
                                        {
                                                        'name': 'ŧ\x82ǹŔŶΗҨªөɀȴʇÒИѝ҉ƪԆϟśǯƺʮδǺωɳμɴϦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛүŞԡϘ0˥оϺĂҽʝƮȠƀ˝ҷХ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀ3U¸ɿ;ȵ\u0382ǡ\x96ȳƭӷ`űĪϖìŝƘњϴʴĩ¬Ίӛɭѡԛ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȾɲǂúʖҿȁɁȀʋ#řȇĈÅǀəCāЍΰȠ˰ʇƴĝ˜ТЋς',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'įӖӡ5ƗҠʲȗÞͲŹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'јӳͿԭƆОǳӿpɎãȵҔȽ(ҿXϙ҆īѣħǺύƻȞȴʽяξ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ⱦэ\u0381Ԗω\x83ІϧȍȠ^ӈЍˮǀѽкԛϯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΟѬćǗɴǢĘ½',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002124.306670:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺ\x9eӀѫɺшΥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŚϔЌoƼϸ͵oɸ˂Г˂įӯ±ԖҡʶÕπȷбѤԏǟʱˈχʵʡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8658780398580049025,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŔѬʙGϨȿˏԟɬӌЪӗϑϚɑźѬŜӶÜϋζӚ"=îˆЏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'дϳо\x8cˠ˕ҳюĥΤΰêŤǊǬţç¸ūčʫĪƠƢѺʇʗ7҆D',
                            'message': 'Ć',
                            'arguments': [
                                        {
                                                        'name': 'ΰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 486261.1009431005,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0380ӵнШƞӋԌѰÕ°ɚЧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002124.803256:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '¦ԮƻˢкȗУq\x92ÍƿɍϱѭƽøX\x95\x99ţѴϻÐĄʪaӅџҤё',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђΨ˦Ɠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93ϼʘϼԇɪњö\x92śЍƿфʐɢǣʏ҄íņMąБʳ9ХύԂ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣʷδˎȑқ\x8dγŕȆξùtǞˮĲ¦Ό҄жŞϹϰǱίƪȠģҽ\u0382',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮҾЎθӗɄԠʱNȗӁіɞˍΓϜ{ьқЯɒǟìȩʃ\u0378ѥæίɛ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6365252086314661281,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ãмËηϢͰ˙Áyʾ˃Ҝ͵ρϨĖп\x8e¤ИʥʀŦǜ\x94ÍΊ˃҈Ӳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6398961382936631201,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŭĶĚ¶Îƃ\u038bΉӚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʊŃɄ΄˃υтьØȇ˸®ƏŋŞķȷѨƝӝԓƿ¢',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȺθңŨӜаȻυƈ¿ŸĔ[Ɛ҈ć[¢3ԋ',
                            'message': 'ȑ~Ԏ˒ƊȠɁƶƤƛȿњϱˈАԬȎԡԏ©ƖћÚʹЂª˩\x8bЯ˟',
                            'arguments': [
                                        {
                                                        'name': 'ťĄbʗЍɬũӾɫǮηˆoЕ˼ƣКϏȀÃϴċȵŽϿĚƈĩϟ;',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002125.501649:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΉϓĲĴѨ˟ѦӰӉ_˂Ђ\x8dΝтһЫęн\x8cϢΛΪѪQǍ˂ÔӵІ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'йӋҦʮǏ¦ΘǻÿʲШĻȳЅЯǭȖ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8cҦӞsƼ\\ΧǌȫŤʙłΐƚʦϑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7172419939051395304,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԖȢΪȘϭ²Фˎ\x99АɡӹˍӋz©ʛǏƔM\xa0ŶԎӿÁҹH5Ô',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 733064.4987891588,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɽаŐӃ~ěӊßҕвæуʂҀˬҷԌǨƭϭЭzѦ˪ʬ˴σɺԇ\x9b',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002125.972331:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÚY£}˨ɼã',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӏʀ˵ɹГţӽԏǫЇк¿ǷɹgˆʡЖѪųʊ˶\x93śʀÁéʻϣ²',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЄĠύ˦ÿЏǚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȟύБӍȌ\x92ƢßĶ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2763088719763028614,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƽ˽ƲҖђȈ˅\x89ҭ«ҬǶӂěˉƁѫʗӌǨϧŨ¨ѣƟˏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŗŜ"ЩӭϢȥhǂȃȵαԊΰԨóѕąѴǶӗԝϞЩԇ΄ȼȈηƩ',
                            'message': 'Зıȿȣʋęĕˌͽ\x99\x8aěˁήϫ®ѳǽQ\x88сǴϒÓӂЮŹǁäö',
                            'arguments': [
                                        {
                                                        'name': '\x97ʍêӪЃԥ˻ϑʘжƤ҂ͿԮɂřƜϑǵԚțɱNĬʚǺuǀǪӰ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'rоЈÞӌgҏuѬцњzυĂŋɁēѥȫΪǬ҅ƈϋy˞ɟԓʻɁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 536129.4278044398,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɓϕӭĪЗV¸ѢƣбÏЅȟʳʧŝŔçѨǱѺѵʍȅҴϿ˺S/ŧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȕѮǰĥ˳й',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002126.617513:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˂ҘУċǯƊƕǩȘĞƩCԃɷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002126.686891:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'êԐƇƣӕ¦ЏƴŻA@ЁŊóѺϚíþʏʄîāѐ˛ęĤ_ǡԉƲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' §ȦҢө§ĶЁƍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɩԪʓYkЊHÞӐԍъйeŔƇ˒ӞǢ¹i\x9fįΡ.ʦĪ\x8b',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ô(ˮăĪӿπǄͰưčŌɛ˒ԍ˭РϴΗ\u0378˵',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣɎѧ{§żēÃΟЙìȾ˺ε¿ǀТ˂ǨϲǇ\x8cŨũļuɞӻÇӱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƙ?T˼ґŲѨɘS\x93Ȅϧε˫ѰΑԍ\x84ɃɦΆșǝǖęԙҗȪсӅ',
                            'message': '˻ɼċȋ˲ŷӱôǶШʧȆˈ˾ӃȋӵˏÓӑȰóҟѐė˓ԐӦԫʆ',
                            'arguments': [
                                        {
                                                        'name': '˳YϣƁCȚc˯ʣʹŢӻ,ωɨǜ\x81ӌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'őĮcĊȺ;ϠʛȬӔĜʞѯűж\x92˨˙ĆҀӓɤζ˻ɪ˂ʱƐηӟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷďјΖҡӆж\u0382ÏȭȚǫԙǩÂҊǮӫėӡ\x82Ο\x83ǞҬѡ˘Ӿ˜а',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 77945.12385399055,
                                                                        },
                                                    },
                                        {
                                                        'name': 'жѦȫ˔ĭXŢȘōȘ˳нȯҪ·CļǃԖ˻˛ӑōШԠ\x81ˠł˩Ȗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѺǝϾҾȶȼķÙųĕ¸ˬΊ˫ҎŻщϡÝJуӯĠҵԎU˶όϋğ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΕeK\x82ęæ¼О',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ы\u0380Oҍҗҿûѫ\x85ǩʅА\x92¬\x92ǫ0\u0383҄ЎӰnҤȈӊƓȤĬ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002127.534143:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'āϊ¨οнǔцʅβfҊ³Ƞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ВǊӎ˩˶Ƈ˯ņ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3083024937808235278,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƑыƏºьPƣˊ˕',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵЊЍƺɝū˾ѫͺªґљŧӃзȘˁɨϘԦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɁǪўӥѤĎ-ԝΏϲВӶоɢʜǤϫ{ϑѯ\x8aǩԜƯҬʘ\u0383Ѩǝӎ',
                            'message': 'Ԑ˸ʤʺǣkȵӁʹιƽеϚȬȭǛŽɮУ҉ˡζθф\x8eŏӷӌǨϛ',
                            'arguments': [
                                        {
                                                        'name': 'ԟӾǙϓ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˕ӌΤʃʑʠ\x84ûǟξб\x91\x9fԚφµǜɞʖËЯɱѼŰ˚Ȩŝñ҄Ѐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņҸɚɣ3Ɔʯ˪',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'μǴԙ´',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆʔƻưɟЕ\x8cӉȵÚϯʌ¹ɀԦʏӴÌŇàɖӡƆÅʑŚԄͱљ\x86',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ųԑť§ʙӦʱõȾғǨūç\x9bьrǴӢʰʪĬəÜŬő\x9cǁԈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŝӓ\x8bßԍƼĈ˂ȖҒтВãԈƗưƚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӉԦýȅĶЁѧȚϳӚҝȌŎͼmb\u0378Øđèҽɺɒ"Е~˶ʴųd',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5454984006351136148,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɏĐːʍӼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƒдɒ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĥżӸ˝ÔϪӌʊДеҸȺԍ˃ƈÑ҅ʳ1ƹҬ6ˣŎԆϯƇ˽ſǐ',
                            'message': '\x98Ͳ;ŞԬΘϜˑĔrƭĺŐЧʀұęĪѓӧǨɿΛͼ˙ԎŪǏʝ͵',
                            'arguments': [
                                        {
                                                        'name': 'ԉ\x9aёќ=(ź',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '»ԨБĴĮê?Ӏё¹ɠԪrɃą¯ŐɆƤƒˍg«',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5228906519196738100,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗʄ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐ\x903ǏlˤİŶlǣñǴύɺӕǕԊŗȹīș҄ҦǴʿǛ˗˙U\u0381',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҫѶťԥɗȆ?Ɵ¥ЯѨųҙ\x90ƢΰƱɪ?ɅůμȆĳάǎy҈ʄШ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӇěRӋƨƩ\u0383EʰńġĺϴJѨͳϛäŉˌ;ĸԠçѽ\x93Є²ӪĶ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6249902445027807826,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȞŕɶĩìƆćҝȵҥöɩԬѽȽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '!;ƼɊΒίЈζѧŗǝ\x85ŢȆȒǔљÌҔ3ƛħ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Đʂį',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˸È˱˩ǚҶɧʚ\u03a2Ƹќ\u038bΛдϫȘѭșƪǭςϓϼϩΛ҇ɎόƁǥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'CȶɌÔάӲԝɴˁΦОÕͳ\x91ǜӼȴcʖɋŉȠҩǠµɌӓȓӓϋ',
                            'message': '˫ҳҫĨʓ\x9cȹİβѓΥч˾ԂaϹ;ΤǒǰƠ\x91ԢʍԟϵțΗÚ|',
                            'arguments': [
                                        {
                                                        'name': '}ʰӱőʪƹÀŎĥPĹOğҩұĈǈØʯӹӮsƬϐǕε6Ǝ\x8cЃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002129.450379:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҠΰϧɹáĠȂǪ҄ұͿδRˀԂØɪӇˈΩɭѺӿҬƾŵӥӭӠĪ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6183406454360506320,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8eԖ¯ǡȏҐőóȳɯÕԇϹƹ~',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9fĨҋèѽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'N\x9blэ˙ЊвɄáɰ˰KϠԅԀϰДãd÷ȠхҕӽoʀώԓϠĈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒѤ\x89ȲѢűƺǣВԇӒ\x8dŋŚʙûшͳǂɃɴƾӇџÈɧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002129.844112:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҵǈ\u038dˢǕϏʦô˺ʿÓ&ӎ\u0378ɽʗϬ@ɺŬđ\x81˗ϤȪƣѻԞɂҏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓNȥ\x88y҉͵ΆǟͳÌȦΖoӈ\x8f\xadҲ˩ɆӮȘÃȊωԛɕͳ˚ɨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɡѯAæɀϹ²ć˘˻һŠόčƽ¿',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŊҁІ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӍЌΚŝϸÁƟ\x8aɫÖŕҨj?ðоɞϹЎ¦ʸҷȧɅ`o4ǑΘɫ',
                            'message': 'Ѝ^řјТрØɰϺҋĞ˦vеБȇ§Єͽ\x9fȫŷĤ\x87ɩì-\x82рҖ',
                            'arguments': [
                                        {
                                                        'name': 'щҗ˪϶ϴҲʧßϛŰʳȒFɅ\x8eӈƴοԓέ;ʴȫȒȲħGϷɞҵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʜѵɘԢҧϥɶ;ȄЖ˥Ʊȝ9ϨΧ]Ϸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǸōƣԈʑÞʓΟɨʬҏΆБΨʤŶдԮ\u03a2QHČǙԐȥf˭ӚҽȢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǐ˔˾ǋNϋϼӦϰҫ4Ѹαȶ=Ҍϒʫѫџː˟҅',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'цѴhůΦӄӾθЕƏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Âʼ#ɍѰҀ˪\u03a2ƦɳΪύeϫũδǅˍÙǫϣƀ1ѾΉ҉ď',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽɰŠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҩȢĤǰәΊЕ˪ɊТҘʯчoȡ˭\u03a2ĺǨŦА˹äǯĜϖʼаѿO',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȒҼԎqЯ\x97ƖƣƤȿàƵǁҝƇˇӭφϻϫҖӨ˄ĜɢžЩʹƥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'рcɁǭичұ\x91Ǫ҈ɬɤϔŴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЎʃыåϕҒ\x89¾ȝӦ×Ŧ§¶¹ѪȫŕøɰÈĎζůɕɡӯ\x95ԑЏ',
                            'message': 'ԃпcǢϖђԨťǹhҼӢlȔΕéԖԈϣɐƾēӔƐ&Ȧόƨһĵ',
                            'arguments': [
                                        {
                                                        'name': 'ǒϼ˚ŧΰ΄Ʒ¯Р¹ҤǛ˙Öɳα˾',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ĶΟʋ^ѡήėԌƉ¯Ԃǂ¤ӗϊФȧ'ДӲ҂ʬЋŞИŅįɩξӛ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002131.250199:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƥ®ğàŰ¤ЃKũΦͱɾ˘Ò~˝ÓӓѮƦ3å7ӹϩҡ˼ͱϔΏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ăѝϚӑ\x87ԙÂӹΘ\\©ĝ˛ʎҽϩǁƏЎǘЅćΈŭĺȪΘƤ\x85ŭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ԣãɳ\u0380ȤӞƔƖ\\βƪĥѬӓϏӐЉɁɳǳʡÙŬζƄėƄ,bɪ',
                                                                        },
                                                    },
                                        {
                                                        'name': '4ͺÂǕʊӛĒоԦǱʶΟăη»ʭ2ȯÿ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:002131.465348:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅǓԝζ±Đιˀҽi£EӧεԣȅԄΚ϶ȝСВɃҁѿҹŻʵΖĮ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϟĔʞɴ6ӐɇƳѠӼҢΓϗÎӟ·ѩΡҰʚƇơ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˯2ϔò\u0378Ďʅ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋΉʌҿsΆɹԭǄŗҧ˷ӨчǐӧͳҫμɱǺȲˍŉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʠ§ȰѹȌðɬωʩǫ;҈˯ĂɞέȚӏȶ\u038bϥі˦Mϑӽԓȋńȉ',
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

            'name': 'ŶԙP',

            'error': {
                'identifier': 'оǯɟ|2',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': '˕ϫ',
                            'message': 'Ύ',
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
            'name': '˯ŷPɫӀǄϳʇϐ×ӧ6ǴȗƩ\xadҌʷ\x93dӗȃŻÃЁҤЬέʝȐ',
            'version': [
                -3380812395162097044,
                -5344660301401669528,
                -2401629260155289315,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ưËƍ',

            'version': [
                -7284837763150318657,
                -8640315416086708859,
                -5719589816738860391,
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
            'event_id': '˛ȬǤǄşȄ\x8eľǚ5ѨϫБ\x9e˂ŶԄȼǆæ?ɥȩȋӴʸȨѢƥŮ',
            'target_id': 'ԫζ¸ɄȡͺӴӃóʆξǕʙȄĬӆ˜ǆω$\u0381ɍƶūџөˑˋђƋ',
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
                    'event_id': 'ĶbʆOѺȫ\x99˨ώôsȕˍҹϯʧιǋώğκ˴ŘƔ¸\x9fēқ3ԥ',
                    'target_id': '\x96ΟΤϺѹˎѩi6VʊϗǤʋ˾ƂǕʫĤȪѥҞϔҎ˒іŧÓũŭ',
                },
                {
                    'event_id': 'ʩɨԭӗǵŧ\x9eŘƨȆÙˍһʿԧϾǮϫ\xa0ΣÓ%Ϧ\x81ƇŴŏҵӤþ',
                    'target_id': '\x8fʟδêȄǮȫняѨʐʡżŪɶЎǧȰ2ЬĀPƩɁĊǩҁʲБƓ',
                },
                {
                    'event_id': 'ԩӃӤʼːҿĭ`ˇͳĽєŻĎɫУѦŬìԔԃžӊʢԀͼǴëăǲ',
                    'target_id': 'я%ǽҾ\x9dŭщ?Ηɬχa҃ԪҨǺБЂйϊsĦǳǙƢҿǨyϰĘ',
                },
                {
                    'event_id': 'ƒːƺ˷ͻǭľѕɬЪҹY@ԐƓьʳаnĆлҤфßҴ˱Ѥȗ4б',
                    'target_id': 'ªǪы¹ϋЀΡˏǳfԌҕǴ˄ԬͿǁъ<қѥ\x92ҝɒәԮŅĢԗť',
                },
                {
                    'event_id': 'ĉΤ4ҝȉβìӍˈ\xa0ǭϑƫå҃θɪŬЈғɃ:˨ЭɪȸъΚϵͳ',
                    'target_id': 'ȝɧǗǨ|ΤљǄά˪ͺɷȔıғŽЏӴѼ˽\x8cċFPĊώÕɟМʶ',
                },
                {
                    'event_id': 'ҎùӐd²đҋŲÇчД˄ґӄɟź\x92ӸʼϚ\xa0ʑřԉѠɂʐФО˪',
                    'target_id': 'Ųŀˏ>ȿѸӋÄѽʆșϘδΑ7UƕϚčμʸğԭƟъŖ±ɭǷͽ',
                },
                {
                    'event_id': "¬ƶɯĬǟʻɶƄȋɕѮνQԟ<1Åǿɘ˕¿Ɍ'ˏπĉŐ˹ԥӓ",
                    'target_id': 'ʞ˼C:ȉΛĄǏθʌŔԃġƾ˥ҰʏĴ˛\u0381ԊŲɽ"ěŷӦ¥ԧЇ',
                },
                {
                    'event_id': 'ТӡmȖęΏǰŵ˲àŁªԀʓӵνΒȸɷԆ\x89ÏȎɍ¹˔śόƏԚ',
                    'target_id': 'γ˞ɇїДƒӝЯʳǬųʠnņ\x93şӺԭțŵ˵ҚĢʶҴ˾ҋŊďĺ',
                },
                {
                    'event_id': 'Иɚ¬¬ǈӲψҫ¡˃ȳ˳ƈʙʓưı±ľɜӮßΚˑʆƀ\x93ӜӺʏ',
                    'target_id': 'ƺǹΈʬоСͺҁ(ɽɃǬϋ:Òȇ~ЯȨřӼsοģˢӏȕӶˌ¬',
                },
                {
                    'event_id': '\x9eӻˣȨ¥μǌϹ',
                    'target_id': 'ЋбƅƬЃγoӈɷуϫ#ǣЍҶΩŴ~˷ҊȲЛԂњӑǮˬџʋϢ',
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
                    'event_id': 'ƦǚȖÏʍ§ǙΧßȜїɮžϡϵɼǕȓӠǳˎ}ǒǭԜ.ǒˋӿȷ',
                    'target_id': 'ͼΰ:аŦѺͳΘ˧ԂŘǵȦӺ\\ƂqűǧƗέЗԋԘɓЮ¬Η\x80ԟ',
                },
                {
                    'event_id': 'ǖ\x81&сАӦхʶϠĕɓƉʳ-ѣӟϜȻÒʢƀȲƼ',
                    'target_id': 'ɏǏ˵Ҷ¡ϊгǉ\x8aϸƑʭÇϒόϮ˔УŗΚІʤʹΌԒȘŅӊѧҝ',
                },
                {
                    'event_id': 'ƞЕѿƬ%ƴщмӓѡ˕Ňű1ǌ\x84ȃӱĔɥѦӠԐǯϻКɍǫΗð',
                    'target_id': 'pауˏҔŞԎ\x8a',
                },
                {
                    'event_id': 'ɀŝϕ±˛϶е˦ȜΨ҉\x80AΊHőХŇЦɡ˱΄ЕΫÛɂǓŰ҆Ǹ',
                    'target_id': 'yҋΙžМǦӝǗϛДȕ#ƂӽȴԍŖ¿ӺƨϋŶͱϮƫόԝŁ§ұ',
                },
                {
                    'event_id': 'ȯ\x84ȟѝˏȀԃ҄ňĬħŕәưǁ>ȋБϏǩДɳ({\x80-Ѵɣϊȅ',
                    'target_id': 'ǀʃĩԦč˷Żˡē˾ƭԁÀɶ·ѭČӼȵϒѲF\x94ĸόѰТɈӦҽ',
                },
                {
                    'event_id': 'ĜȵЃӍvãқХҪѨ\x80ǈϥ«ĆŅ\x9fƂǚˏӭ;дщ˼\x9aȓ^Üą',
                    'target_id': 'ȂДȈˣƙƜеΏȌÛȏƼϩԖɺнӲȇðҾlÎӽϱ×Ͱϲʴ˧Л',
                },
                {
                    'event_id': '\x92ŅЍҦЩˆΟ\u038d9ȤËҥщPn©үơ˵ű0ƃиĆńʶˬϹʞž',
                    'target_id': 'ζҜɂ\x93UʩʍϗƐκˆх+ˊ\x8fӡЛíϒĚϲǚӕ¤˚Әƕȡ?ʖ',
                },
                {
                    'event_id': 'ѯӱȗ"ΡɼʁńǏӕԝєøƅӘϰф°Фˤʪǟƹ\x89˝ȍЄΐЦĕ',
                    'target_id': 'Ìԅm˟ΕȸŇҊȧȰ˹ӽŃˆʡKԔӨŏѲψԐ\x86ГųΝα˼Ѐѡ',
                },
                {
                    'event_id': 'ŬʓĈŞĳɘ˼ƗŕT§ҌsɈŀƃɠѩˬϬˆɴі\x8fȑͿҁΛŨȁ',
                    'target_id': '˭ɤА~ɲЉ˨ӒƊϏɒʹǊϴԌҮɂƈɦȯ\x9aŌǶѪϕų\u038d¤ʱҞ',
                },
                {
                    'event_id': '˛ҽʒʤŎƤϙƗ',
                    'target_id': 'BÔñ˫ĦүɬƈыŁјƦӓѿϛԍӬÈϯΧβėԐłϿ¦ѨɴǾҫ',
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
