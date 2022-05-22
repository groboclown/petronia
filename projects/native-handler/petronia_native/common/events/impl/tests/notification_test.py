# GENERATED CODE - DO NOT MODIFY

"""
Tests for the notification module.
Extension petronia.core.api.native.notification, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import notification


class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.MessageArgumentValue.parse_data(test_data)
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
                res = notification.MessageArgumentValue.parse_data(test_data)
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
            '$': 'Ɋǰ͵Ŗɯ\xad´ӯѳɗȦ\x83óυҟIǢ˯ѲΙǶϏҶʟĥȏɻˤɩы',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5737829349476478988,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 229855.34738448245,
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
            '$': '20220522:173214.548062:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'HɹӦӻƯōҫ.ĻяwĖĺѣļÚԥșɅ,ϊǅʙëÌϜ\x99ɷΙĺ',
                '϶ĬΒŐԏώ\x82ЛıŶεԨӐҴȋDΦsϖ÷ľԀȭԉ\x87δʬЄăŊ',
                'ĕҹԧŠѨŅȪǾҲНӜƦʋż\x8eήϞΣϫϣͲĘȹӏЊǗӸ¢аƀ',
                'ӍŸȻƓΤmȮũěΌɻǩÓʖҼԐӥ˒ʟεƣÍƌȂɠsèҺӸ҅',
                'ӵ;ģŲ¿Υ\u0381«Ӛå϶ҠԠ˔ȠǱϱǗȘǥ҄ѨҪő!˖Ґ\u0380ӷɂ',
                'Ͼʷӏɦ°ȿTԫБĦӜţ˾˭ŎόçqΓǷˢ~ÐȱÀкÒſ˫Ӡ',
                '˵èΧʶҦŞɎķϬǵȄǻâĥœΣӾÕӊʓόѐĩ3κ\xa0ơƨƘǎ',
                ';ΫŐɓвѡʐΞԣ\xadęЁҌƴɲŠŏҎ\x8bĺԊɗ\x8cҏŏ҈ĐɼPŇ',
                'куtѻіËЖŐ\x94\x83ƬƇϢөÍǰˏҌ\x9cҗĄӿΘм©˭ȟӤñȎ',
                'Ķ!ψĖɞЋќΠΠξ\u0381\x8eѿˇ˔їƫϏӧ*ΥʏƦɎȥҸŢØˠ˲',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -1743614643441215947,
                8272229602523767438,
                -9180364510403144721,
                2941236853159586567,
                4788763301527733438,
                -7262081460833283120,
                -2878168272118838735,
                -8366544943157410752,
                -3290475680216894580,
                -999103523483632580,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                829868.1702774714,
                946940.6987450946,
                754718.9966491039,
                437829.85784915055,
                120673.30518644757,
                645620.3107669728,
                934605.7601016545,
                -45720.14514969569,
                168937.36003150843,
                624335.2481481349,
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
                True,
                False,
                True,
                True,
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
                '20220522:173215.033413:+0000',
                '20220522:173215.041501:+0000',
                '20220522:173215.049507:+0000',
                '20220522:173215.057459:+0000',
                '20220522:173215.066250:+0000',
                '20220522:173215.075547:+0000',
                '20220522:173215.084803:+0000',
                '20220522:173215.093034:+0000',
                '20220522:173215.102170:+0000',
                '20220522:173215.111529:+0000',
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
                res = notification.MessageArgument.parse_data(test_data)
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
                res = notification.MessageArgument.parse_data(test_data)
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
            'name': 'ȅԛҎ¥ėѯǤœҚѶŸɒˊ9ҠǬ\u0381ĮƝһɭ\xadмщrȍȆј҉Ԛ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20220522:173214.325188:+0000',
                    '20220522:173214.333584:+0000',
                    '20220522:173214.342080:+0000',
                    '20220522:173214.351654:+0000',
                    '20220522:173214.360637:+0000',
                    '20220522:173214.369626:+0000',
                    '20220522:173214.378819:+0000',
                    '20220522:173214.386900:+0000',
                    '20220522:173214.396550:+0000',
                    '20220522:173214.404755:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ñ',

            'value': {
                '^': 'bool',
                '$': True,
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
                res = notification.LocalizableMessage.parse_data(test_data)
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
                res = notification.LocalizableMessage.parse_data(test_data)
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
            'catalog': "ɔ'ũÂŞț\x8aЖҳӘSϩŕʩʞÖïȮш˘ƐϹ<ǵǙҬʈɷȞå",
            'message': 'ΥαūԈĴȡĢʨӼҶõĪьγ×ѡϤӜÕĺʫԕѵɗvȀɁԨɃх',
            'arguments': [
                {
                    'name': 'Ŷ;ҸЮȮη¯ĔŞĉОѽ\x84ģȼʝѲԥƌpϮ\u0380ļȅЀl˽ɕӅω',
                    'value': {
                            '^': 'float',
                            '$': 103862.67653693806,
                        },
                },
                {
                    'name': 'RЖͽǍȘӛhҹɸĽèͼ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -22832.728788028224,
                                        910172.8242869166,
                                        -85774.75350430209,
                                        973714.6020841566,
                                        552833.7700067932,
                                        405035.0106653498,
                                        524490.7522080288,
                                        214611.6516734106,
                                        153769.2503011131,
                                        441305.99752075225,
                                    ],
                        },
                },
                {
                    'name': 'œϋѦʴͳɑƪ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ȐģɦʾйͼĉСƋűļ˃g?Ԧ\x99ċċBГЦ˥ԩʤź\x88ʰƌκȱ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
                                        True,
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
                    'name': 'ɻʛČўσ˝mɫzбԛǛϡɢĖ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ɸԊРʼи϶\x82ƛȽ\u0380¸ǱԈҿͿφǺҒƄOÚӡѽ¡ǠӈŦе΄Ʋ',
                                        'ƒìӥCEǀЦɴƙ4үϋĀΟ\x81ƍÇʎNƗŌŕ\u0383ǫÃñғŪǵŨ',
                                        'ǡͲӑɬѸΨîɳŵϫӼ˹=Ӹ\x86ʽӌƘӺċӐςëƖÕŞƛ_Ϫń',
                                        'Ѫ`îѲӇΚҠ/}ʣћǺǴԕԓ\x8bԀ\x9aƟҨПҾӮӏΡÈа˜\x89Ő',
                                        'ѠӠ\xa0OҠKЀƵϋǺΝѱχ±϶ȈʔӨԥ\x88ώôЎyӅѕеҚáԚ',
                                        'ûǭωǝωʖҚÏҴԅϝƾŜӌ\u0379Ƣ1κәϺѱǢȑҏ«ӒɚǒҳП',
                                        'ȓїұŢ|=ҌЩō˲Џ?ϴ`ρǈï¾ǍүʿԂƾ"dZñǉЩҠ',
                                        "Ҭ¡ȟǈĦu'ȴϲϮпцƖѐҷӕҙу҅ɏǗȏˍ!зˋƅҶlи",
                                        'ȋȦǲ\x94«ϔ\x99ʵŉ¢ĬëѲѾʣɼɲʯҐȣԂϰΫüʎҠÓ͵#Ϊ',
                                        'ɕx\x8d,żÐįѤºǌêqͿǇҵҜµŋѕԦȬіßОȈʞDԙӰʺ',
                                    ],
                        },
                },
                {
                    'name': "Ђ:ʵ\x8aÅ(ʽϚͼ'Ɗю¢ƷϨԕƹƚәʫҵŲĹÝǼaƊnˆЌ",
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220522:173214.018793:+0000',
                                        '20220522:173214.027200:+0000',
                                        '20220522:173214.036843:+0000',
                                        '20220522:173214.045246:+0000',
                                        '20220522:173214.054773:+0000',
                                        '20220522:173214.063427:+0000',
                                        '20220522:173214.071418:+0000',
                                        '20220522:173214.080725:+0000',
                                        '20220522:173214.089893:+0000',
                                        '20220522:173214.099138:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ġˈAп˦ºƂԌӥșŻǡȍȓØÕÈšӔɫȪɛӪϞЊǭ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:173214.143961:+0000',
                        },
                },
                {
                    'name': 'ɒÔdЫǷǓԀʿƧԝ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:173214.179290:+0000',
                        },
                },
                {
                    'name': 'δī¼ΧѠϧƄ©ƚŤ˞ȑӉɔɛʹRа\x85ʮȬǼѶǼӯƭӱxƀ\x94',
                    'value': {
                            '^': 'int',
                            '$': -6067480718498828369,
                        },
                },
                {
                    'name': 'ϧƺlżǡʙɌɗţӔҠҐŖАԊŤҢi»е4ǩͱϵƌÕӷѪІ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:173214.254688:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ȳʦ',

            'message': 'ѐ',

        },
    ),
]


class NotificationTextCreatedEventTest(unittest.TestCase):
    """
    Tests for NotificationTextCreatedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NOTIFICATION_TEXT_CREATED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationTextCreatedEvent.parse_data(test_data)
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
        for test_name, test_data in NOTIFICATION_TEXT_CREATED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationTextCreatedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NOTIFICATION_TEXT_CREATED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='text', name='NotificationTextCreatedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='title', name='NotificationTextCreatedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='icon_id', name='NotificationTextCreatedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='sound_id', name='NotificationTextCreatedEvent'),
            ),

        ),
    ),

]


NOTIFICATION_TEXT_CREATED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'text': {
                'catalog': 'ĹȋŧRҜʩɉΞȒ©љԑƪɜƞʌхśѐ˹ϞƇɎČ˖ȡɩßèǓ',
                'message': '\u03a2ɝ\x99ǦȁĴЍƇҶ˰ˇӈĪʳçӯȇÝШƦŗϤŐ½ϪЗáԘȝʳ',
                'arguments': [
                    {
                            'name': 'ҞŚӣѸĜЫ˾ĐƴˁÉʭŠǳҷ˻ѬҝBVʆ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220522:173212.780234:+0000',
                                    },
                        },
                    {
                            'name': 'ȺД;ξNώȏ˃ɻïȭѼжӫΛƭϮӈѮ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ƏΘ\x9fѪúɲҏɋЂɎɦăϭJĘ\xa0зɽсʄĽξ',
                            'value': {
                                        '^': 'int',
                                        '$': -6347230395601024805,
                                    },
                        },
                    {
                            'name': 'ҹŏ%ƒΨ˅ÝKӂӃѿêӐȆ\xadӪѹϼLɎɟʹǌ˩¸ԛϐјҥñ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220522:173212.888344:+0000',
                                                        '20220522:173212.897310:+0000',
                                                        '20220522:173212.906094:+0000',
                                                        '20220522:173212.915323:+0000',
                                                        '20220522:173212.924684:+0000',
                                                        '20220522:173212.932939:+0000',
                                                        '20220522:173212.941280:+0000',
                                                        '20220522:173212.949222:+0000',
                                                        '20220522:173212.958388:+0000',
                                                        '20220522:173212.966045:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '<',
                            'value': {
                                        '^': 'string',
                                        '$': 'ҒџԊԖǻєƃƎ҄ԇRưȸñȦҎ˦ıÐϩÕ\x9c҂\u0379ͱЃϛӦί´',
                                    },
                        },
                    {
                            'name': 'ȀƔѓƸŏdѽÑӰˏȶԃŢ˃ԪӃҭ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -1026815671664387676,
                                                        -1984507720891092195,
                                                        -7977406390780971741,
                                                        -2960135121011491171,
                                                        7944350882981144511,
                                                        -3444574695617444025,
                                                        7421455385411744063,
                                                        -3297597623014372272,
                                                        -2168121941729644821,
                                                        -8928893585044052101,
                                                    ],
                                    },
                        },
                    {
                            'name': '\\ˏhɃ˾ѭ\x91΄҂ʿCԓȾΖ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ÐȃΎʐđP',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        6877913563174052432,
                                                        -1965407839746770262,
                                                        6375419086650945666,
                                                        -5924485366524396543,
                                                        1129360725124890552,
                                                        -4434166548348722609,
                                                        2575138540003318046,
                                                        -8477890531369998016,
                                                        -322114723138131991,
                                                        -1724078477305127321,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ѝȰОҲßϣˣǥƺ\x88Ͻ\x9bӪƋʕ',
                            'value': {
                                        '^': 'int',
                                        '$': 2067921953572169586,
                                    },
                        },
                    {
                            'name': 'ɮй\x87ӚʝʌΜáѝȉ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        -53489.51424882432,
                                                        578570.5347615804,
                                                        983619.9987573789,
                                                        859158.5702488062,
                                                        504622.3163699631,
                                                        904582.1582122841,
                                                        689027.6748883686,
                                                        531217.4116386821,
                                                        36494.488247800764,
                                                        -23569.159052451418,
                                                    ],
                                    },
                        },
                ],
            },
            'title': {
                'catalog': 'ŽǟΤӻǈȊƌãĤåŃņ\x99ņнƾћÝȟ˺ȇӹƌſЈș\x81Ćȿĩ',
                'message': 'ʿʹȁ˧ҸŦ˰ϡӂŦɦЦ×҃\x822ҐӞǫɺƈǪʍƬ¶ɢұǉʼō',
                'arguments': [
                    {
                            'name': 'ąυŗҌԅǖƇјюBɚδĕϣЋυxŦҼűВԜ\u0380ԓΚƋŵӒÃΙ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220522:173215.238905:+0000',
                                                        '20220522:173215.247515:+0000',
                                                        '20220522:173215.257228:+0000',
                                                        '20220522:173215.266205:+0000',
                                                        '20220522:173215.275799:+0000',
                                                        '20220522:173215.284977:+0000',
                                                        '20220522:173215.294417:+0000',
                                                        '20220522:173215.303801:+0000',
                                                        '20220522:173215.313233:+0000',
                                                        '20220522:173215.322030:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӏŎʌWˬɨŐƭρɅ˘ȩϨ˄',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220522:173215.364157:+0000',
                                                        '20220522:173215.372664:+0000',
                                                        '20220522:173215.380740:+0000',
                                                        '20220522:173215.389372:+0000',
                                                        '20220522:173215.397262:+0000',
                                                        '20220522:173215.406334:+0000',
                                                        '20220522:173215.415278:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'џѓƺƍɫӻҘ½ȴԣćʡΎȞĘřƘӈыɨћӡŃϭİԢ7ʙлǱ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ǇӯʑyʭŸeɌˀΊӉƮ\x7fŏΧǭʏуǗӵӳƠӚ~ҌΊИ\xa0śğ',
                                                        'ɛŐʗ\u0380àM©¾ԨхҨӀǤǥɔӌѠʘ\x9bіʗÛӓӶǝʩԘҝͰƄ',
                                                        'ĀёƧņʛƝǷƕȿЙňǅΚҦћΜŗưȍÞĈɅÝǨˢVҤѣǐϜ',
                                                        'ȻкѐɄ˥ǬϞгƲĬСùyҐũ¹l;ɭ\u0383ϴŸʅϔˀó-ÙƺѲ',
                                                        'ƒŨȟIšæНϘаĺɍЂԙʧzѪήӆeȾ\x8dɺɝŶщĝȴӸɺ·',
                                                        'ѨЮǽӍ\x87Ȧԃʡͺ_Ͼαęъ¾ʩӄԦLŎάũǞӕʹňƔ¢ȉш',
                                                        ',ɞEõӱ҃ƧʌȡÊȓˣκϔύ:ʴ¾ʳĦӹĠʸԙѭΘ©Љˍċ',
                                                        'κŚǂϻϴĥɂʵVҸОЋ´ΦΕǱͻ(аϼțŰҧԬϥɷƺѪŋӎ',
                                                        'ŰѷϼԞϊˋƑȇĨϹ˘ƠʷÊDëҚˬ\x86ԁ[ϬĽÚԃȢƼëŖl',
                                                        'pɶЊɣƒwɽTюɨˀǘ¥ϳƭҠóΥЍǲːԧǠΫҵʢƗŐӱű',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Vϫʲ=ŋϒӂƊΕ@ͼҫτƑψɚѶӞ҉˲ԫÿƫӨ7ʅӮЗ-!',
                            'value': {
                                        '^': 'string',
                                        '$': 'ҖǤǣκƝ4ϹÁΑӇǯ±h¶ѧԐ\x97ϞƋтSƞĕ\x89çƖшʰгȉ',
                                    },
                        },
                    {
                            'name': 'Ǟʟ\x96ԇŶԑԌӭΙ<ҝ\x9bþϹ˙µņʮұȘʻŶЈɧšСԧʌϲ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ήƔА',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'Ʀ͵bʡĐ"ԏnÀϻҠȬѱ\x98˛ǁѹӄэҔʧӀѿӠǱй˜ȹСc',
                            'value': {
                                        '^': 'string',
                                        '$': 'õɾϜ±ŖԘάϯԁͼШΗǢҢɳǾŧ6\x8d@ӑǥÐȍђɒϜͽΛĄ',
                                    },
                        },
                    {
                            'name': 'ȏӏӻͻѪ^ĂéǓыĸZ\x95ϋˠЎˡÎѵԭͻǊÐХŝǯяʪȸ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ŹǄҗîɌŨlЋ\x80ԂǺÍаΪǤʢʽɯųʾ҉ǧʡχӢҌӌǼƧʉ',
                                                        'ǚћɒӊɨΘͱĠԓƚɵԁƣӎ\x8eˋ\x9aшAZдϕń҃sɗ\u0382ʹŸҍ',
                                                        'ҍ\xa0]ѮƈƆ˭ȺϧɺŸ©ɺÁţ\x93ҶĥϩѮ˛ĭ˞ɩ҈<ĬɒɔŶ',
                                                        'Đ,ʾ_ӓ;ѨɃũͿȁƥōψĺԈӗУўɆǝ.ұ»ƃөϒӞÏ\x8a',
                                                        'ìӒˆȏmˆʡȾӜɮҐьͽȴǢжɒ˂αʪʲƱϢўʶæһȤҗζ',
                                                        '˒µѸÓƹĨǒǷäȖˤȷwȱɆŰ\u0382гԎ\u038bsΟдΜƂƀĘТÍԗ',
                                                        'ʵƌҪɱì˼ʧяĊ;ӷͻëİȿЀ%ȎŇøҽϝěǒѤцԦȉǨ\x9f',
                                                        'ΙĲqȵ\x96ӡŴǎҘӒБƂοɩЌÆĜŌϔ˞Ŕ\x8fƁљƁςƊɵϤŁ',
                                                        '3ӋӲ˲Ύϴʎѷǭӌ6ϳːƶzŵ©ˊѾ҈ǁЁЯѺÙѾѣǂΧ\x80',
                                                        'ε\u038bʬʆƧΩÐɓ§\u038dӁ#ΈѮÊдοī\u0382ÐϬrѭϜϘȪЅ£ΖР',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҽʛМu¼ǬӨʏ\x9eҴʙLь˃ʀǰϵӮʛʦȖȺˁЊ®ʂɘљӗ¶',
                            'value': {
                                        '^': 'float',
                                        '$': 580279.9469580459,
                                    },
                        },
                    {
                            'name': 'ѹҒƟʆ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        42878.8758531519,
                                                        587739.4762067329,
                                                        184938.37020106654,
                                                        867076.4663996437,
                                                        910133.7449138949,
                                                        948326.8386722757,
                                                        724712.5877542141,
                                                        306923.9176212643,
                                                        769800.8611131595,
                                                        609753.5437640226,
                                                    ],
                                    },
                        },
                ],
            },
            'icon_id': 'ɨ\x81\x9aǅғeǓмϝñėƳØȢ\u0379ĐΞŋӗʵlЃʄ*zˤȻǇŠǵ',
            'sound_id': 'ēΣԬŹȕĢπ¥#ƇĈŀʓʫΑưӡǵǕǂˬʢc\x83IϧӼȇӥM',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'text': {
                'catalog': 'ǆѣ',
                'message': 'ϔ',
            },

            'title': {
                'catalog': 'Ϟŭ',
                'message': 'Ċ',
            },

            'icon_id': '˘ƒҖџƵ',

            'sound_id': '³цКΔ˵',

        },
    ),
]


class NotificationIconTest(unittest.TestCase):
    """
    Tests for NotificationIcon
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NOTIFICATION_ICON_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIcon.parse_data(test_data)
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
        for test_name, test_data in NOTIFICATION_ICON_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIcon.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NOTIFICATION_ICON_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='icon_id', name='NotificationIcon'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='title', name='NotificationIcon'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='hint', name='NotificationIcon'),
            ),

        ),
    ),

]


NOTIFICATION_ICON_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'icon_id': 'ʝϨԝʷʄ«\x9cǺǭǀԣƜιѾœ҈Ŷΰ˽ӳѮУӕˏͲƿˮʀѽȳ',
            'image_id': 'ÏʛҚιά^ԒēUԆȻВѠΚńΑVÜηсĉɗ˅ΰÑ¨LǅǹҢ',
            'title': {
                'catalog': 'ЗƲҷђθʬ¥Ә',
                'message': 'ϴίeʴΞɋʼЃæȰϋċԢͻRǺVƠŹԇӕǑ¿ȿ˯\x90ŽҐǈÉ',
                'arguments': [
                    {
                            'name': 'й\x9dɕ\u0381ÞҰ҄ҔǦ҆ʢȤɭɑņȉǜʌѓėÙ¯҅ˁ\x9cшρɗΤº',
                            'value': {
                                        '^': 'string',
                                        '$': 'ԪɮʹƎǭsοȒЪŹmήʟЈɈƨƵǯxaŒŀɔӔÃTϐҠȕɞ',
                                    },
                        },
                    {
                            'name': 'ŏѷͻσĽҲϻЦͼÇŮ7ҞџòɯƿѕȰѲĜ\x9eǀƻЩçħϲ¥ɺ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        85562.90818394787,
                                                        757630.9937414683,
                                                        920603.8609324704,
                                                        918700.3762210212,
                                                        907906.160863359,
                                                        247433.2340770678,
                                                        679000.1764494663,
                                                        55587.45513748759,
                                                        283023.7636742409,
                                                        -8706.573449128453,
                                                    ],
                                    },
                        },
                    {
                            'name': '7ӄǪɖìŴƄʀáΘɀĮѫΏώJĲ˻ťĴːƿ\u038dɇĎѥѿεńѪ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ҌғΎҚĒĜĐфȱȃ҇³ӫӼ˪\x84˺ƣǖŮХ\x92ķҗ¤ԟŉӔɧê',
                                                        'çǱΣ!ЌòԘѐƸƊCΓǰί˧ɆθɪÂЬƚԌǇѨʢӈҽҐ¬Ж',
                                                        'ȯʸƽӲәҤԗԍѨ;ŞϛӹĲҺǸϟиƕiӮƨЪҷÕǭӦƏã:',
                                                        'ĦӯƥљЛ{ʤʇǵȃƸƘĳǿ҄ȍ#τёѹūЫ8ТĐjԧΑ¦ĵ',
                                                        'ӀгƚǏòѪCОˈȹΏҗǵǦьʻ\xa0\x9f˻ЯðӷÈЖ"ǽԣŘӾ(',
                                                        'ΧϬԙϝӕǁêưЧļΛäԐњɛİjĝϭ˱ǴӪLɦȔҷƶ\x9dóU',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҳѠΓԫΟԤəǺǫŘɂŭмŐņRψî˾ŋōƜǲ\x88QȯӘ!śқ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'Ŝӟœ˧цέσɲO\x8a˚[ԎÀиФԙ\x89ώʄһãŪǐŭęºљʯɦ',
                            'value': {
                                        '^': 'int',
                                        '$': 6256725306665153027,
                                    },
                        },
                    {
                            'name': 'ȀYpĳǤϪˬíʏiΜ˳ѸɖƯŃˢʅŊлÏϛӦĽʬĻŢôʅρ',
                            'value': {
                                        '^': 'string',
                                        '$': 'Ñ˵ύȢоϙ¸ԮŘʲEƍǀÎӌ\xa0\x90ìǰϢˈѫΛзʾӼʋɔЋλ',
                                    },
                        },
                ],
            },
            'hint': {
                'catalog': 'ƙГ¹\u0380ʴӂҚĠ\x87ƈºʋ\x96ĲңíԉЀq\x86jӫЫҍ3ҢӲͺǴё',
                'message': 'ӴǌіЂÜϞɦŜ¥ĥ\x9eÒɬǄʾ#άȰ˞\x94ԫɮÒˌoɐȃΞгǴ',
                'arguments': [
                    {
                            'name': 'đ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        284997.0460215289,
                                                        533223.3156082937,
                                                        485170.37820847344,
                                                        933170.1160879591,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΗǂǮ0\x9e˛ƸȈ¬ΑԟĶȒҠÃЉ\x93ΡԘ˝ƹдɆϝәʫЄż',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ѢpvǶơŗѩĲƾ\x89y\x91ϹЗлѮӵϬ˸ӱŔMηʄϢЇÃ˧ԫԪ',
                                                        'ȒҳŅʌӑʊыÇâʎѝΫӥĚÿşҹǟˏϟԁǖ҉˦}ǝħʾΫĝ',
                                                        'ìeβʴƽϲΈƄlȖÀTҮЇӒӐ˄ќɁ/ɧʘжɫɲ҅Vԍ¤҈',
                                                        'ʽԂì˺ЍӏĸƗͼԪĮзȱľȵƿ҇ӋБϸc҂&¾üьϲ\xa0ȵœ',
                                                        '»ˌʱĹəѷĲƷĤƟ҇˳ϒ˰ңˤȫq˯ЈūȐÞʡĝѡƁͽī\x92',
                                                        'ƴàʓƲҿе˘Ҫ\x97҅ѸɏƨҚđͳÕ[˥ɾxԎҐñѺ·ăɫχԁ',
                                                        'Ƽ˞ˋϩԧЯůѹƖćʉ˨ŐʘȾʨ˳ʲĸǓɼǹФѵӾҙѽϑӘƅ',
                                                        'ЂǨûǃΎ@ÁMȓśǪɉΟŞÍ@ɆƦҎƉ_ϻХǋ$ɂΠԇЇɽ',
                                                        '_СŐȒʟҳϭ\x81ŅɍӈҹƢҰ7űşȖƅǦ_ȻȫѨŃɥˁ\x9eǲȆ',
                                                        'ɕĶğɚΖɺҸãӿҦ\u0380žżȳρΞƆʡŵԊ0ȈΈǮɣѣʈŶŮʤ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʇ4ϨнȯƓňԥΒƊτƺӖƏΐ\x97ɗPÞΒŗNʭ˰Ιǿä',
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
                                                        True,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'TʚɨΪ·\x8bīwǱχхҗе\x89ԪȜê_Ĝ˝ɂļєΒӴѼԪЄʌʤ',
                            'value': {
                                        '^': 'int',
                                        '$': -8002446343287684205,
                                    },
                        },
                    {
                            'name': 'ĠηʼϣϲυsνÍƧʘ¥ȍҪ¿҈ӿʷҠҹŻϳņǮɈЄ\x8fҟӊɭ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220522:173223.391312:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'οʨҒ\u038bȭ]!ϕǊ_ʓˍ²ΚҾԝωɰ?Ȏ˶˨Ñ\u0383Ņ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'Ϫԙɡǿ˴PÍˇʗҐǭƕøʁƵ}ȳȯѩ\x97üƳǢɫɞ˧/ϑ΄ι',
                            'value': {
                                        '^': 'float',
                                        '$': 361228.3119947513,
                                    },
                        },
                    {
                            'name': 'ġUĩσȸʝˊǎǄŌÐԍʛӮÜҌƥԦơʓӎųľɚΠǛԔÛѥю',
                            'value': {
                                        '^': 'int',
                                        '$': 3519058667967025677,
                                    },
                        },
                    {
                            'name': 'Ҙϯ:бʧēЈȘƽʀνϭɝƀԕёә\x96Ľ×ΏФԒΊ^)Б5ηŧ',
                            'value': {
                                        '^': 'int',
                                        '$': -1365309531314355196,
                                    },
                        },
                    {
                            'name': 'ЇӸГ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -1903276084150847057,
                                                        1055745905046692010,
                                                        8047980474085928954,
                                                        -4118880545229809625,
                                                        3445311847990281964,
                                                        819802580588126357,
                                                        -7404281735644556738,
                                                        -6816933426793788015,
                                                        2715140972600015064,
                                                        5847021655920983195,
                                                    ],
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'icon_id': 'ŃϿʃ˃Ӣ',

            'title': {
                'catalog': 'Ͻҵ',
                'message': 'ҍ',
            },

            'hint': {
                'catalog': 'ѝƪ',
                'message': 'ĥ',
            },

        },
    ),
]


class NotificationIconsStateTest(unittest.TestCase):
    """
    Tests for NotificationIconsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NOTIFICATION_ICONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIconsState.parse_data(test_data)
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
        for test_name, test_data in NOTIFICATION_ICONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIconsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NOTIFICATION_ICONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='icons', name='NotificationIconsState'),
            ),

        ),
    ),

]


NOTIFICATION_ICONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'icons': [
                {
                    'icon_id': 'ę~юŃƅɩÒ˴ǭ\x8b[,\x93ҥÊ¯ѩ6Ɯӎ˖ȯʕϪщȅƝԉԉĎ',
                    'image_id': '\x96ȣѯʠё҆ǯaŀӛʝɽŝƵý˼ėϪΫgɴĿ}\x9e˝§ȐǞǣő',
                    'title': {
                            'catalog': 'ĻăˁӺĪĸŧǋʜɨЦɉя˖ŀȻ˱Ϗ\u038bŵìԇÿǆōӗΉȞ3ˬ',
                            'message': 'Ƿ"\x9fПƗƲԂǚьʼéǻȜԃ϶ɠИɩԛϢԆзӚʠ4ʻĦ"ĐŒ',
                            'arguments': [
                                    ],
                        },
                    'hint': {
                            'catalog': "Ǜǉ ǔҒʋ°ˣÙfƵхѸ'ϙԚЂƄEԧ\x80*ʻҵǼΈdǋº\x91",
                            'message': 'Ӿѧ{pϰЉƓȀʗ»ƶұwμżå˥ЍȫȨőͽϬԩ_ȩѣàɌƭ',
                            'arguments': [
                                        {
                                                        'name': 'ŵŻшѭĊϢӫēƭĪԡӊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͼԥÖǠ\x9bУӘƑòţө',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ':ǔϳrǮғѲcʉчʥÐҨ˛ɭϢԟÞяW¶=ǏюǌҵӫϫĩȻ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΌʞłƻҽѨ˱δɔʃČӆŹКĀȶθ\x87ȩҌ¬\x9cόȄǑƘШЋº҂',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŨCόέǏӱ҇ʔ˪Ŵɪ\x89ςЍЂƍzԁʫŞϠñ΄',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'wτɤϢaηԦɋʇή-ĉǀÔÍĄсȅҐќϼӯȕ˜\x88',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѩ҄ͷԜҟŻĵʉ;όЧ\xa0ʙΫϘÄѡƢ˓ÌγʭőšʿąëȏôΩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʋɝɂʳȱѦұvӴӵԔɨӎjǞſ˛ӎƝʍҩ\x8cɖӣӧμǔҽҗŒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 611125.907327455,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ПƺͷȝÁôҐά6ӚƦԭҾɟʃ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'BŤҬҝ҇ͲþʚӇǒťˋϠβĒ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȨЫɏº½ɋѣȳ6ԎȘϋ]Νƹξ:ΗҙɬĪΣȤϽԣуAӁķѧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173216.265144:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'όҘʪȓ´&ӬԆѐȦĻ&ƴɍȄ\x8dʲƜ\x82õ*ϥϻƦѷφȼѼ4ă',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7658845630816369809,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ēȓ.ĘӫǙҞŵ\x81ϣιÂ\u0380ҨʋĄƻƢϙέ=ґŭļ\u0382ăˏΓƘþ',
                    'image_id': 'aɏӍĞ҆Ė£ɓĽºiѕϽ˕žŵʒκ§Њ/³ϣȳŉƂƃǥʰѽ',
                    'title': {
                            'catalog': 'ũ¤ԫѪѓϊˢ˾ϺçϷʤǄgγɛŔ˵ϞɇǈũĞѭ\xa0ԥɠǍ϶˒',
                            'message': '`÷п\u038bë0СЎ\x98ʍхүʼҊŹȢřѸx\x97ʀƣɱ ʋϡʝȤȸӇ',
                            'arguments': [
                                        {
                                                        'name': '˝Ӽ˭\x92\x9aϣϒßƁǩϧȏʾVĎƊØ«\x9c\x9bӝ˭ɏƭψΚоĹξė',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4917064945038146649,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѧæ˲(ƑƙϦӮ/ȅ҆ƣΌƨǖɹϹŅɆ±ĝЦӬѕWģňԨɪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 989402.955656773,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ìĪ~šȁíύϻ\x90ȪÝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173216.401241:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'żϷƲšȒҳƐƹͻӨΈǃͺҡѷӝʑȀϡƖƫбţ8ʇǟʨȅͻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 82167.20215768841,
                                                                        },
                                                    },
                                        {
                                                        'name': '˛IɰшΈ¢ϴȴʺҀʽЬѣ>ЊĆ˛ΕñźΩŝʙөʧ˄ƈӲͳm',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ł+Ǡлǧϯʄ"ВKʬĈ$ӚЧʀӿԪCĨûʔàԜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5055411431896215915,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ěĠˢDůЎӆ©ϝʫȱҙCȴĻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173216.496253:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˺Ĳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'оʞȫԨԕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĨўͻѸз*ќŗѳȳ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173216.567288:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ɢYљҬā|ØʆłҤІдůҵʃЈϿƒϧψΩ×ǂĂŰP&£ΐƧ',
                            'message': 'пϭ×˄м\u0380ӺŀŞàέȶɗԃ¢ȷӎђìԣАӁł¾\xa0ǩҿˆ*ʈ',
                            'arguments': [
                                        {
                                                        'name': '\x86\x80ΦҼƩ˂{҃ɰǺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɊϽϊţϲɾѴ\u0383ɊЅΧɆЅДϺԤDɮЩƽαѷÌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4102358710194908204,
                                                                        },
                                                    },
                                        {
                                                        'name': '˙ӴFɴΘÆĔč',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 876937.4523969104,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ίќpÏ\x86ŤǖO/ȺѝĖ\u038bˏ\x9eɢñ˓ĬĉЫЖrƓэӄ;ʳя',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϘǠɀ\x80ń\u0379ΝƋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɺǪɸ˜ʳυο©ιҙ*l˱΅ЄȭŝdgƜȍϾЯƯԃυйӞƑо',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔԄͶėÏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173216.732328:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀ§üʭʠɋҳË҇ɰʸƟѦPΐ\xa0ɤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˉʾΎџʴȃБ¿ȜчƋў҉ǠЩôԦÁҿӍǆ\u0380уѼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˪ɂ£Ф\x9arӈʱшĄʝæǊʁǤ¢ĨìÁǿΘȚӎĐΐɽŴ\x89ȥY',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌȏĖˁƻҥɟ1ӹѦԦê',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ӳΨқӘəьάѪӱƊʡʛƣɢҫϺʱҌԩǝʂϩşÌѠĄ\x9fêѕ<',
                    'image_id': 'ҽɋƆōȫжĦαČ\x88ʃϴΔҬǄ>ǓЖҩȈƁӳ˚Ŀ\\ζȷԗŦʍ',
                    'title': {
                            'catalog': '\x87ǗɜˬСЮɕѡĹς˲\u038dŝҵÿDƱÐɠïOȦșȕ¥ȝґϸƈ¥',
                            'message': 'QѶ\x9dϟČΤѿҚ˻ħϑԊľҥ%bƂ˩ì˻ÆғДǡu҈Ďeŋʈ',
                            'arguments': [
                                        {
                                                        'name': 'ԠчͱƋçăŻɗÎωǸęӬӆηΆÂ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '´гTƊoӒаǐϗέȂʰҞǎιˠɸ҄ŀřϸðѴǻэ˪ \x8dпΨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮǰðŪĿůԏ\u0382ёε¿Ǜ˱ҵ\x9bϛÌƸMӁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ыæİҕӡĤӺǝĉÿĂĬӑȒеȈ}υŜϴǈϩ˂áӘ\x9aưЩãǔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔčΈŜĖθԒo4ˎԎѣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¼ƀҔӏǔʬ˯ˀ˅˞Ӱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ģ˝΄ĊНˮє:àОђҐ˓ʙZſȲқwԝЪǙȝʬ\u0381ʟʙ˷ɹ҇',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁÝЮŤϴΌĹiEҕͱȞѭЦʳ\x8eƐʹԖНƤӍȓпʚīԣĲѕì',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6584287863854362278,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱűӹ˘ә˥˘˰ҤȟХëáçфE˖ə<¡ȄºȥGĊхĊӿ˹˯',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'γáȤ˷ɉÖǱӿϐӤѤʣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ăƚ˧ӘXԁÑǡ҆тӿǫăȵ\x92',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΰiϝđŚ˚ҤĭІ˳ɇɂL/§Ӛк[ҜýUȒεȲ˯Φʏ%ɣ1',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 640473.3038107828,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ĵéϏјџѠȈψ¹ɝ®ŖĤʶΰЭńƱ˦˗ЄƻŨŭŪɳ¼ɔɅΜ',
                            'message': 'ӋˆԌýŤX˴lćɸәˊԜђЯљĥѣбАӟƽӸɹйɿ9\x8c8ϊ',
                            'arguments': [
                                        {
                                                        'name': 'ʶ\xad',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŉ×ƯĸǫĪ\x93ɶѥƩѲԦаπԪұéЭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌȞюȷԖƍӺwǱƆŰ\x89ǘϯϳŅ¯e˹]рȐϲӭЀόЄдɰƂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4834985122342133327,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔàӵǇȝϧřѼɉĸ˳wёëӣǕƨ7ҡԖңĨгuԜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3079988296830359475,
                                                                        },
                                                    },
                                        {
                                                        'name': 'дőάсőˋҙ\u0381ωƖ\x90ȖĔʷƷˈƛԆ˩ϰȐ\x98ϐѼ0UǮ˱щɧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 426149.05631790415,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳϯ¿ȬΣΕ*',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͽʶ`ɯĠΙѦGʊѹӄ&ŤϥŎϭ˚ŵθǎɵӼʶâȅŤǕɄĔŤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4632584143964973803,
                                                                        },
                                                    },
                                        {
                                                        'name': '³Зӓ\x9aӎӁùԋŢƫΉȝʩЖϖ¥Ѵ\x8dŧ\x90жƮïʏǛdӖǊӃv',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2229132232574449154,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӷїYɌċӦ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 313883.73026282835,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӦѡφńЌˌʅ҅ǻђÍӯʹ\x91t˷Ĺ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ɥȾύ\x97θĩÝҟɒVͷ΄ŕԮɉԘJĔ¬ЄҔԀÇǓĊÎ%ʲ˭ɬ',
                    'image_id': '\x84ȂKЫЯфԅȓӇĨȌϜӍҿѠǋˋòԕ|ԪǇѽϾϝκИѓĜԥ',
                    'title': {
                            'catalog': 'ˆϰҸȸ˒ʟЫ\x8cƝӒҍÜǮѱȍЁнҌȌԖǡʇ˵˹ΣѡAǐfȉ',
                            'message': 'ӟ!ƻ~К@ĨϜȪĿĦϝѕͻԇʆʍ*ʝ\x81ğƲȎHƭùÅŞΒӇ',
                            'arguments': [
                                        {
                                                        'name': 'ӷΫӌǭʫ΅ǜɟʚѣϒʝʁҞÈ0ţȅ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '^ˊĀȱ˼Č˩ғѓƽļʓɊIĉ×ΐhˈΛȒG˫ØӴϊϦАΫʵ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 265771.81386926945,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵOβѕē$ʐϜҧîʢŨcəÔèɰØ^ǨİʍʴŰM7ςͼӆɒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŅЏγλżƨʫŊâdμҮѴʡҎϷĹ˼ȈѝƔûӟ҄{Ӏ}ъХ´',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŵ2ƗįŔȬƠχȀӑˡ˞і',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'bͰˮɞųӤ\x98є\x8bэʘǾȓӁNʇyŝѼʳӎԊ\x8eԁхęēbЎʥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΊΈӷҠǡ\x97ŖʻϮѓ]ȥǪƬǃ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2227761025713288457,
                                                                        },
                                                    },
                                        {
                                                        'name': 'BŁɸűƐәΪȲыǏƟԂԨʿ˃ķ0ϕӧ%ӠʈѷŝԔӭѬ*ĚŚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ýwǏg˹ƛΤSӸͶRÈËўłǕƒÊɷƍƖҶíąƣԥČιΊZ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӡ҈ŀӯȇɫAÇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¢ȷԃưƜLԭ˧ӃϜʭěǳπεƳ˽ҒϬĆȬɌǿǽźŖЁчSȱ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũʚɹѫѩɖшԆʆϣǽƮŋ\x84ʸ\x91ƾ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ȞäŶěүĊЉʢȖíśÚ\x91āǁҨ˜ϾĢłʛeeʪјʔʭæˢη',
                            'message': 'ǒʹQԌ¹фƴ<ȘǨГɲϥϋ\x98ӎɜѐȣŸPԇТҎҋ2ɴѺɴj',
                            'arguments': [
                                        {
                                                        'name': 'дoνԀǇëԤлԄɱſ\x80ȦªǓԛƮĴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173217.755920:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԦҲƥсЛʺ!ʴT©ϔÝЌ\x9c\x80ɂˎ˱',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -10209.655171962993,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǅƇƿÿƮǔɔ\u0380ŠŖ˔Ï¬ȝɇµϔ˼щȴǐǜʧóėΙ ïбï',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 470866.14023151563,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѱҁ͵΄Íȅ\x93҉\x96\x9fӱÎĆЍíǊ˭ЄȩҵϊȆσԌʼʘмȠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҘƣĉɌÎŜеа<Ïʰ˛AÊȢɅȋ˸ǤĖ˹ʗħșȴӢ\u0382ʙȐ¦',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɰǍÒƔWΝӂɿѻʫΤGӜΨѡ˹ǕȝѬҜĤĴ(җЫҽĬːΥP',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϤӘˡʇ˫ԢʽΖƚхϻøʀƇԥҼΐɞȱǆ Ы˶éˑӧԙH҆ϝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԫҩʒɺɸńЌєĲΰ1ǶŰҼUǔϗʀѸқȷˮ˵ςЮӪËÓʶƓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˑŨǰϰeŴȰԓЖͼӦąˌoГˎȂŭɏҚÛӑһđź\x9dfèǛĚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁҸ)ǵˏʫԄŃ\u0382ӲēϑϓŹˈjӧ?ŐÎ\x88ҰќʓѡΝМɪӳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȻÓʻӀοӌĩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173218.067044:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': '\x99эҍǣÅƸѴ˃\x93ĔԦϕĖɌäɵȀԃ¼ȱҋЧşϚʊɡȕϔ²ȇ',
                    'image_id': '¾øЂŒЊӌńћԤʳӸÇʧļÌȕǹъŋ±đвƆεθҷšӻȞӦ',
                    'title': {
                            'catalog': 'Єƴ\x95ê˂YʁэҿԁsǞȮԧͼӘǳɓ\x8eĞӸҙǫȊyРŲˍѪр',
                            'message': 'υӐƔ»¦\x9bқÑɍьϨцƸğЌúӍˎϗǮ\x93ԦͰ1|ƔѤӦɾ˸',
                            'arguments': [
                                        {
                                                        'name': 'ʽ˄rԖǨҲʐέ~ѿОǭʁǎÀp¾ͺĄΰĈƪqrßӼð˕Fą',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 836349.0590553083,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʞųɊĞɩƄιʱэ\x99\u0381Ƙƿ\x9dʏǍӔƁЈѽRġƖ\u0382ʝΑʤѴȗǡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƒʐ\x8bҳ¤ɛǌɩ.ŠЈыӭŇɟƹǥГ«їõˠΟgӸ˺ķʯsӿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˚ƕɪϼԧƔάһƯҪȲŮȪ\x99Ӟ·ÿѯȀεʥ¤ǡԭÊ\u038dŬȄľϊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8d·Һɋ¿ǨʵӰИɅΊͿʾ¸ȉӒɀӄԜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9153954337598967535,
                                                                        },
                                                    },
                                        {
                                                        'name': ']ÛʢӺӺхɨɫvƒґΧÛѵ7ĠɔĒŵҪ˞ЃҊҍ8ьuñǡ˽',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3468771392401434377,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9d\x95ЅʱʡūҋѸǁ±ǣϯǖοԁѪґjƢæǤҲƒȒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƁɤТɾσмʒɜЀLхġβ҈ÂȃӱmɀŏƛΠ)ǕȐźʯĕϻ½',
                                                                        },
                                                    },
                                        {
                                                        'name': 'îԍ¥ɽΦȂƲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΜĐτdӬԆðŌɯ}ǬʯěȽŠӤUˁјͷиȳ҂ΎQІűҁ˦Á',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԑŰâҶʒαнΖʵțӃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɥŽÐƨžχʪ˄\x85ȉάʍõҳǿʢʥ҈ƞĕɐΚЬƭćƃϾƾŞԁ',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': "'ƚӣóТƸԅԈƁ:ʚǈɂ\u038bĘωȈΆЬʣԥдЅĶƁԀƼʈŌǃ",
                            'message': '˓ȋҒʞ\u0382ŷӞΏѓàѣԒ˝мӫªƓȃФĦԐ˒ƧФ3ԢÕϱԫȠ',
                            'arguments': [
                                        {
                                                        'name': 'ăһVYųŝ\x92ɗж\x9cS˓ϹδŏԃG˅Ëƴr',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɋĻщȏgԉҒŅʒɫȕԗв§ҘVԉӡͿʀ¬Ƣ¥\u0378ϲȵ\x82ϣ+ѿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϮƍϘɱƿƣɋѻ˸Ɓÿ҂',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǻ˙ԖΕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173218.646459:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '-ãș',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x95½Ũԓųќơǜо»ĆːӔѠЍʭϯ5ͿʀԆʱźȪʞˎ²ʗӹș',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'u}ȽЁLӔɲĚǇˎΚҷɰ\x81Ńďư',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'цƶи',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 793664.7196556915,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƵʁњƅWӃƢƎĘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ωƆ1',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173218.854409:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ː%đ˞ÉΝÓʕ\x9bԧɩϰԜӭΕлɘǮ¡ɪοΗп×ҨΣѮ\u0379Ϝѷ',
                    'image_id': 'ΉҽŕҸĶӂүzϑȑϮȫŎǫ4-^LɨϩGuƐɿēĿІʷжƐ',
                    'title': {
                            'catalog': 'Ӗƻ\x81hɑԮɍ\x94ɗĲҤҸσĩЈɂ˕ȅЛżҹϑӟȈ\x8aԪ\x94Ǘɏƃ',
                            'message': 'ÝʉħӦa§čӖŃχ4ʯ˛ãÈɚмȁӳQŊŷ˼Ƙ\x86ϪƉϡ˻ц',
                            'arguments': [
                                        {
                                                        'name': 'Ϩԇʼɇɵʹԡʱ½͵N\x87±¹љɧ\x8cԃГωų҇Ƨφ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2695728097236275558,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝ´ϡÌżçÆɣԛІӌʿŁ²ΉBŭςŉʻԤÈɐƎԨ(ɭȲİ&',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ρĆȒӀԮǁʙӊԀϡxʺ\x8fƇɇρʎŚŁĺŎŶγ\u0382"\x8aΆЦ˘ȓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ңɫќǿɑњƄƁϣʦчÌŴķҔĕǼĝʪŬƜaɕϡ\u0380бˑъȸλ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘÁė\x91ôĩĦʌҾEöǤф\x94Î\x86ǕҖяȎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173219.049797:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '!ŅӹˊѕŅͳȸЩ\x9e˄ϥβӳѿ\x9cìĜϒ:ώƉͶоȓҌŷƑбҡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ıˋӫ.γ¬˳śDƑí\u0380˸ĄƣȔъɱёϬkʻȄʙˍӄɪнǑȕ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉ©ʸҜԉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Жj ŔӼŹǡǢŻ҃ȠϡˍȺʾʏýƮќɢŮԪӔƗŦӴƢˮǂȿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'f÷ȕҋ҆ιˑǅɧȶҖˀơǉŬϾԣʨFċ˹Ѥ˓ͼ\u0381*ц',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'μ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҥǄ˖КаʤҦѰҔȯΰƀǨlˡԔʾɥɽӔԦӛƕɶ˯ϨʮΖƾȄ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ћŽɸ\x80¥ǯƿˇ·ƸǮǢɄȼ\x8cҶdʱ˧G˛ǩ\x98ԓ+ǊʣƂеÁ',
                            'message': "ԏӷЛuѶȣªfȕÓƲ\x8fĐŗǹƛζԑԠҠ'$єċãɠыG¹ ",
                            'arguments': [
                                        {
                                                        'name': 'Ȱɕφ˹șĹv҇\x92J\xadǋťϱӪҞҽӸȖΘdǘҾ˧ƓӘæɅŜƨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÿӠɣΓĶûǶȪïŅҸƕӪҶЩàƓ\x97Мˈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5433042952560161678,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Έ˜ЂɼŚȩŞʛ/ʐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĽГϖɛʛŨϮѹ˹Ҁɷ4',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173219.432538:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŎɲȭƇҬǡǘͷԦŧΊ"Œɭ¸˅ΨȕiǥγˊjˌΡ\u038dҙûӒŀ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҶӋʽƯӶuƔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'π\x8fЄђɪQȨͶφҰϵɺǸѮԈǳε;Ҟ˪Ԟш·Ғ҄ϸʫĩθә',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѐůÙѫb˄Ңȇ:ÆȴΨƂӚȫКÇǺʿzҾΡbєɍ҇лōϑ҉',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ːǕǩǿ³ˇċϒƛͶǬ˷Ϸ)ĶԛǇК',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥԒǍ\x8fǛŉ½ЦȡōĝԡӖĊфɏ҂Ҁɫ˙ҲҺЛΐɆƞƯǇƵö',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϒрΪʽёh`φћÇӃVҾȝ˩æ˞ͶҹҚÀӓɰEʬҍõʵӎĊ',
                                                                        },
                                                    },
                                        {
                                                        'name': "ϿƂФтÎˬУҦԭӡȡǾ'ɐэ1#ſό҈ЭɱîΥȺêт҇ČƇ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'АϫƻҒ\u0378ƀ\u0378ԝΏ"˱ȕѳϘ)\x86ѼӒūȉҪήҿǺҰ˔ǗʓɁԋ',
                    'image_id': 'ˡӨĝɔϋȼɑϡȤȊѢα\u0382ŻɝѡDȲŶ6˜ɽƓuԮ>ȎЬǤ\u0379',
                    'title': {
                            'catalog': 'ч\x89ƼϲɔÚľӇƠҜǓ3ђƠѦĄ·ɴʏȗćԛάϻQ\x8eɶʑгӣ',
                            'message': 'ϰ\xa0ԊɘѹǝȨЪǯҒŀıϜìʖϑƣmƋĥӭбƜίŽǐÔɫS¡',
                            'arguments': [
                                        {
                                                        'name': 'Έҵ¸өҽȰМ҈Ʒ\x88\u03a2OĝΞÅ~ǓπŉɼŭрʎЏ¯ƘƛÙԫκ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173219.736112:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x91ΎѿǋцɐКňӘĹč˸ңԔ\u0383зĀӁÑλИлӤȡӣΏԘЗʐ!',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҴʺȁƬÏƟǹǣˋѓӡʰҰϴҟ˳ɺɻáŜȇǛƪȻũɷâԛΑǿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǚϯμŭ˗ƆċǸҺΟӳþ*',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¾сɯʰѦǏǷˑ\u0380ɞн',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥɐҍśΉϭU=ͲƷŁҢҬǏĝvԞӂŅ(ϢύȠͳɹФŇʛľɭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Π',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉžԃɞƮΉ\u0381ęÐΚ˖˺΅ɃϖЗğ;Ȩ˔ɽǐɯˋ°ǹԦҬȞЕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 813938.5883829189,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯ\x8dƂ˲ƊƉĝ\x8a˼ʨҧɑНщóȁ\u03a2ħѼѶMɽˬǔҊü\x91ҧɢԚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Άǖҳ\u03a2ǸœƩԣBЇóĊŪ˻',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʞ£6ŵϫнƼĊFʄœɬӃZԄČÇҞňӊҍ·¾ЬȑσаɐèВ',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ҡɎÐ\x93ɬɂɌΚʊģӁҿԂˤʴĝǝŪуé˚ůĦфʯ.ϳӛɂҳ',
                            'message': '¸Ϙ-x\x9aԞwʷóͰ\x92˱ƶȲʾƖԭʅѱʦēɤːâÙũѳʩ¦Ҏ',
                            'arguments': [
                                        {
                                                        'name': 'ȘλͰӠ{Áӕƅŗųöåӭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǞҚƾǕƋȊƁŻȁȫĲÔĦМ\x9aȮάĸΰ¾ѵºѵȷɌыȊп҄Є',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŨѸрԔŎ4±˗γδţŭΪ\x85ЧӲеˎˈĎԒźδȟĪ\x98њͽƛ˦',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 437620.45576723514,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂĊmԬèɄ±ʟƪßȡԊά',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧɗŪ7ǜԙԎԜȫɜͰǔΛŨT\x91ƽҙϑ@ÊŹ\x90ѱ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 280494.6125289366,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƆωŻȩέ˭ϿЖӘӽØҦԢѲήɻТҚ҅ņƷñ\u0381ƽѴБ>\u0381ԏ®',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȁœʉҚʸć҂КɎɒȍ˟˧YxШlԖŮĸ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƯķȲƛКģѫыʭʻϴїĮîϻҠŪ\u0381ўјϯϴ\x88ԗǚͼΗ|ʸø',
                                                                        },
                                                    },
                                        {
                                                        'name': '˗ϾsʓǏͳҶȓȅȷԔƺѵȧƙπ&Ѡљ\x98ŘУĄ0ȱТǿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗƑȡɨÑʬɉÅʫĚ!ÖgϜĿ®ÁūȌюϭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'х?Ϛ¶ΛCѩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͲƿƠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ÔԍͱςƒOΣǯǦĜǳɐќɁōǿŌȹƜƑеʳʉǕȒƺcŁʨ ',
                    'image_id': 'î"ӌԈ˵Ԏȯ£άԡóҵɅȟѷŒzɸ˷κΓЦԡҕ\u0381Ӟϲυкȼ',
                    'title': {
                            'catalog': "˕ԃ«6ĢȉĊАìhЛŮzƔ+Ӈ\x7f\x83ԁЩ'ž¬ԈԢʭϽĲϞϡ",
                            'message': 'ʺŐ҇ǠĔ\x91Й¦ŴȏŹҸПȜβǆΰɞʪЃă÷ЇǒF ϪȸӋŶ',
                            'arguments': [
                                        {
                                                        'name': 'ŻЦ;ǿÅŅЎИЎ˗Ѱ³H²ƫӖ\xa0ԔɣÛ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҜƅÇŊĔԥρʸϐØqÊɽϓüʹʭʜǉϏҵҹ҉ȍ˝ԔӺʽΘҍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173220.555837:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĀlɡԞ4хđ҄ªĠ¾ȣǶʷΧ¼ғƇΐ!ȨʾƆ\x94\x9bͳƨѣĝȢ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173220.591325:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'šȏӤǖϛƘј¡ϩ\u0382єɞönåǔu',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҢӘ\u038bα¹ÅԋзąɁƘhѕȥԈɏȸӟǗяБΌӌϑǵӺԍө;ŧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u03a2υʻśЌūȝяŅѽÅҙΘǄȲĚȖʱ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊɃЫčǧȋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƣдиÎ2ĈΣȰƾɝџ-ӹŘÆđȰȁʏUҦӉĥќÖҽʻϏЉǰ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЬƻϤŨƄõЇƶ\x8eӢĢĔͳϹʘș˫ǱĮmѸ҆ϚӠäĒԏˎŹS',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 988405.6686761035,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯą]ǉ\x96.ʹ\x99ćöŘ(ϦԬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'АƛʟeʀѴѮɌ\x84ǶԭΰȱƨŢðԍƂҲ\x96ǱԓĨʖÕԓŪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ʑѭŪZˇҔʨǉ\x9cϏвāJòɌĤХАǁʑnƅ0ѿԐåҺ0қʭ',
                            'message': 'ԚɕΩұƦˤį\x8eʭ/яƳ;ӠϜ\x8a˞AȮԟ\x8bϊˀͳ¦ƫӨƯӗѺ',
                            'arguments': [
                                        {
                                                        'name': 'џјҚļύɟцƐɽƥĚҹɃӿʩԒƴė¯ԆѺb)Ϡҁƀϩ¡őο',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u0379ɏĵ½\x8dȯΰˊŊēҥɫӮӰˣ@ĥɓɒj©ё˦Òͳͽ˂t.ԏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӭ˾}çˬ\x88ɧŗНɿҴӓ\x7fĨƤëďǐĊƱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҇ŧ&ґĴԫKԊѪϋ˂ԉ¢ѠɿЕʨɂ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'sύ\x8dћ˯\u03a2ҍ˅ːϕãŮ\xad',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3237406387216299889,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶȪž˜ʏ\xadΏþХ˘ӍҟҍԇMʔΒǾ¸ϐΰ҉ŲZƵѯ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ωε˩ҔҮʂȂѵӸü,ӍKő˚ Ή',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8249995390576412154,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟȤ˱œΥĴŃχ˶ȷςɀѡҮԖƷĘԔΓ?\u0378ѭ\x9cӌʜ§ĭυ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˴ȖȗΖʃ\x98t\x91Ƀǿť+ϖˋк΅ʑʘЎɰΊͲтѪНɕӢʌӋǳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӞϦȹvǾƯĲϙȩϭӲӝˡǁȏØϼ\x85˝˴ԮŮD˜Äí0Ǔ/n',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 673204.7567727902,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʕ¿ˠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ā¶ʮ7˽ōʄGѿǱ-\x8eŜƭѩ\xadȫėú˷ƩÂĖҾʖňɀǫΫŗ',
                    'image_id': 'ʱЪƿϲЯʫÈʜњ˔ЪʏπΐїЖҼӰ\x9eҭËӱbҟuű҅ŗK˨',
                    'title': {
                            'catalog': 'ƵĜӝßԏ7љːӴĤАĞĭɌF\x95ʦлЦĊ\x8aҢ1ԭ§εɶМʢӫ',
                            'message': 'Ӓ\u0383=ӚԏQϽӍϣΧLɾȑӗnPǉϠ\u0381˻Cҽ˪ɐKӢʎȇҐω',
                            'arguments': [
                                    ],
                        },
                    'hint': {
                            'catalog': 'wΠ\u038dϘƿgΰӜģȢԜŜӹ\u0383ì\x9eχҘΎьíȚǚФҨȬқӴàǵ',
                            'message': 'ǽγÛ¿ϿѵɺŵƧҠқҩψϗБͼϠȘʰҽÁŷǈɩШȌΪӞӎϷ',
                            'arguments': [
                                        {
                                                        'name': 'ӫΚƽʧƖǥ\u03a2ǸŎtϼ˕ƺý6ŮĔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʮԉưѸį˧ѡɼӟѪӈҒŕɬˉξŁΤǶҭȢԇʜҡŋ)\x7fêбĮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1953469352043755664,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ή;ыҀɡǺΐ¶Ў˴òȜɤŅүøχƞљUĆϧҌƜ ƵȪƟÆи',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȇъΉɭƨAКǘԁˊҸǟþƯЙńſňЂĽ¯ҬљɥǒĊԬƝϙ˚',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽǭHϽμĀƾϽaëkȤĖɍɓȈйΤ҇ѺԖǕƣüȰϘţЧǙĆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԐяŀӖè˯ɡŶʸUԁέÅʾЊӕƳˠ҄ˍ{˽\x9er3˯]',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2319681749233813345,
                                                                        },
                                                    },
                                        {
                                                        'name': 'сϜƂԣǪӛ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӈѹҁŨ\x9fϠĎȂ˴Λƙ҄ŋŐȉй´ӱԆżƀˏАȆƍёǤԦτŖ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x97ҊŠƟѤǌѝʚďϲÏƻƷȰˋҜЃĪΣҥġ҉',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 938655.2965807653,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŢʍˤɽźŽ¾HѬҙǲ҃ҘyрéĢԋR.ĪȬȖʟѯԘǭȳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ȋȍɞú¤ΖѰòĤԚƈтȹԜõ¶ʭ>϶зЇ'ϐĒЩǓԇ8ЙԬ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ΥσƯʆƦ˜ӱƲ·έѸ{ÅԕŷǿRϜΚӱ.ʌԅЯŃԍөʠʩ˼',
                    'image_id': 'ş˕Ħʸ˼\u0382ԑˏɫĘ®Ǚí\x9bҠÏó"ĺ\\ԖүĎdÞĖзËýƃ',
                    'title': {
                            'catalog': 'І6цŝԦɉї8ЄʻƽΊʼƑƱˑҟԜ×ЄɃȜϥƞÄӤƜˍōɎ',
                            'message': 'ԃ\\ʺÊʓɉǛ˵ΩɆ©Ƙϸ҄дήöσĻĒsxȤҷoѨɹƄґÄ',
                            'arguments': [
                                        {
                                                        'name': 'Ҡӣ˛ѯɘҭěˀ\xad҉ľƐ\x9e҈ȲԀϛħȬ\u0381ѵ\u0378ҎŪϷ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3233171863288058566,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŃԑЛKё҄ûΆ\x8c-Ή½ăɬȣɻӁқȦʴɿǨ˲¡ʘŘƸʸʄх',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173221.788777:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ς\x92ӏΎʃϱƅ[ȚϩͲϽIˣȮӮƉĆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'f˲сƫлòɚËҘƻ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʋхƎɯ\x9cÀɹ`\x91ǛжïԅƕЈ=Jɫʆǻђв',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˒\u0380ƢΔΫӥϼńɡЉϫ\x97ύҩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦŋǥʨƗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173221.968090:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕɱǟҦѴ\xadѴїîԞѽEҡƈǏǁσλҐ3jRɲ˹ĺүӓФә\\',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '&ȠǫĊʊůɈԎ˼˵Ρɺɩ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐµʟ˧²öǼĤVʮɸΛɞΑƛɖƶмþЫхҧ\x9eӪǺtȊǷȭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 934997.3165744155,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ǔͿςǲĹĽ\x9eЊʳ˹қάΔǘ\x87ɀʈɓǧǧƹĠ@ʄ҉^ǖο·ө',
                            'message': 'ʌǞӀŲӁѾέƯƖʷӣ§ѥÞaƀ˻ХәûΗĬ\xa0Ιȿ\x84ƀ&Ӊҡ',
                            'arguments': [
                                        {
                                                        'name': 'Вμ?',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ίʧΧƎɖԕûǈ\u0383ƈ¥Ѱ»ɴʆĐʦ°˽Tȏŝƞ˱ѫǃǁѓȨµ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173222.177674:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȐёүҲϼśȄħΫўm˒ӟ"sԥϲ˴ʡǒÀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѥюϛ°ɵïΈǯЖүÂ˨Ź\xadЅːҿȫҰʔÃΦԩѳѵ˘Ҿҝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'І˫ЁϢҥӣǈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĩѝăç',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɫÕǕĠϒЭΣΦÂƑ¼°Ц×ǃЫԤŷҳǇҗԔέǧǀлǈÊŽɍ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖөē$ʸÂ\x9cϵω\x95ӝΑǥǾïĦĈԣɂƐȑȦ^ΜЄČîąŷ\x95',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˼Ź¼˲ӑΜҒĲԂҚ˔ţʼϺ˞ĕɲ¬ĂʊϩϹıѱѸƌȔʵÃ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 72756.90131147549,
                                                                        },
                                                    },
                                        {
                                                        'name': '4ĲӮ%ŚŚɸрϦǋÙ\x95ƅHӹӋήǢ/ĠĥњƨɾŇŘнŵͳŁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7956708835806488375,
                                                                        },
                                                    },
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'icons': [
            ],

        },
    ),
]
