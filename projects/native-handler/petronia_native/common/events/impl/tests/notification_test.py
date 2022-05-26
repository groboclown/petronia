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
            '$': 'u@\x88˙ƮԪЄ˶ԣ˷kʠοђθ˗ΒÍҜʏķɼτǕȽƴиԑѪɥ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 3645807108261909730,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 596737.1913574907,
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
            '$': '20220526:211932.644084:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ʤ\x9bю\x85ĵԏϓHęҁaƖɫҔ\xad˚ɐÊ\x9cԞ"ҪÿÛсӯ\x95ɠ\x8a%',
                'ϬʖÍȸńӿɮҙҟгʅǀ¢чκƛˢϠˎ˼У\x92ǱŚϯѻҖ˨ʝ˕',
                'ĴͿȆўψǰŽЫƇĀŷӊӂįʎҦɀȸõưŰ^Ϡϼ˹ШɽӸȌ˧',
                'ѮÄĳċƠҞü˟Ǡ˥ЏɒҽӢ\u0378ӊțӽңǁΡǄǆăϒȾȷjďɌ',
                '˭ÊӴȶäĆƜӀɧσƐƖώɡӁӌӗəȸÑƭʁѦ˱ø\x8f˞ɴǟʵ',
                'ˬʘĞ¢ϋ«Ǻ҅ҙӒ˭Ɩ_\x95ΦƪȔɛA\x86ЮþƖʴʃĖ˖ȇŋµ',
                'ʞbѩȌƞ˷ԜȸϰΉÔ³ΜğёĪҜ΄ѨҠ7ˡԐǍĶҨӲŁѤӮ',
                '\x82ʦӫŕȸźǣʮĦļžǂԏғʡȐϨȿ\x98њόʣϐĨǄƲʎƄƯˍ',
                'ɗß˰\x8dϷ·[Ϩ\u0383ĨŬєƈȐÇˣφƃ²сЎ}ÝɓΔħ´\x99ӊԠ',
                'Ҟǂѧ^ŦѷђȂсӺʚЍƜŭʉƚϋ\x88£ǛёƿțӢö˟ϪƌƘҹ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -1245963848332949195,
                8294650160740191557,
                7689846046960897979,
                8883686758826407965,
                -9135620089393098756,
                -8997299361793220636,
                -5987385540741560233,
                5999675836298713557,
                1614138585088623910,
                -5239575924073005338,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -82588.40139068011,
                153504.9859880228,
                736907.6952915984,
                400249.9108378485,
                901484.8340883572,
                -37317.89237917649,
                864932.11142293,
                239795.0512996447,
                -27081.85128240814,
                761406.6971587286,
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
                False,
                True,
                True,
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
                '20220526:211933.560429:+0000',
                '20220526:211933.576200:+0000',
                '20220526:211933.592213:+0000',
                '20220526:211933.608665:+0000',
                '20220526:211933.624463:+0000',
                '20220526:211933.642835:+0000',
                '20220526:211933.659928:+0000',
                '20220526:211933.675765:+0000',
                '20220526:211933.691467:+0000',
                '20220526:211933.707376:+0000',
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
            'name': '±ϝ½æˑșǟø',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20220526:211932.200134:+0000',
                    '20220526:211932.216849:+0000',
                    '20220526:211932.233799:+0000',
                    '20220526:211932.250509:+0000',
                    '20220526:211932.267220:+0000',
                    '20220526:211932.287106:+0000',
                    '20220526:211932.306201:+0000',
                    '20220526:211932.322839:+0000',
                    '20220526:211932.338943:+0000',
                    '20220526:211932.355798:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ĵ',

            'value': {
                '^': 'int',
                '$': 4449296637135459069,
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
            'catalog': 'ϓƥĘåѕĥаƗɭЦǚ҄ƊтӏӃνƤƟĩϯŃĪӽƬƷǋө3Ϙ',
            'message': 'ԧǁȔƥбƍӕȔįƁǮǀҗƗĈŷҁѬӬςĜҡƶɢӋӤŎ÷ÌϏ',
            'arguments': [
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ǸÀ',

            'message': 'Ƞ',

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
                'catalog': 'ɉˏĉ\x9fԪφȫФjɩϾЗƔɂǸˮƆ˱ǡѽΪŔӫʣЍΟ˰ǺУ˨',
                'message': 'ӇǿħȡԈϔΗʄ˟ʉ\u0382Ӫ¢ӾĝҶʮʬ>;ǵǓŋ҆ȭȿʰӉeǝ',
                'arguments': [
                    {
                            'name': 'řĀ\xa0ʎҔéʖҧ×ɚƂӨϗΧĄȰѥȯϚú#RųĒȿȨ҃ϡťě',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ӏȄԮ\xadʆưȠʪШğøϫ˦ȥԊ;Ҳ#ʪƫˍƨˠ΄0Ǣ˱āъϧ',
                                                        'MɠͽʣЎϋȽ÷κɕμȤɝĬàҫϔҷϪ\x90ǸÅ\\}ʙɂÍϿ*þ',
                                                        'όˇ҈¬\x9dƪɅȲήӦ\x89ąϙө©ȤҬȋЏñŏȻÌΚŭҌ˂ȆҨ\x80',
                                                        'UķЗϾҡАϵǱɤӒӈԏϸѳљ˷;\x85Ԥ҉\x80ōҫȨŶ(ϓΰɻі',
                                                        'ԗǖ<yëˀȳʤҎȩОÎǠ¤ɆԢһ\x99äɋq͵\x81ͳ҇ˁÕϺʹӊ',
                                                        "ƻɲÖӲƓӈМȔϙX\xadЏԒȚΞȏӮ'Ȱжïӣɳüɷҩ¿ϲӒӴ",
                                                        'ͿàɦԠıŁϳƼ\x84ƃˀˊǤҦȎ8˭џӡҍоɯӴʸ\x8cӀƾĹ͵ʤ',
                                                        'ȪɗĵƌõΠĽȧƝуΉϔ\x81ʱѱƺȆˆϥѨĖĈ҂ĞjϝҽңϪУ',
                                                        'ϙӪƚӞ\x98ɳӱƚNĆĐˋԜȇҚрʴuʭ§ƄĆҤŰԍҘώPϧÙ',
                                                        'ÂȽŖԫʦӂˮîΦԪғӹːю\x8f\x98Ъԙ\x88ļ¯Ӊ«ɩƮϛ;ѿ7Ґ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ѽǳŰ˅ʡӷѓƄãήϐǣҸ\x98ˁҮǼȧԤÈԡ˺ńɂΣɯΥˈΝ¢',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'һʴê˝ɻһìǥ\xa0Ǥԭ\\ĢȫŒýʦ\x9fƯŹɈǵƵǃȊ˵ŘĎƭČ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -3640286602264034398,
                                                        5366289360403581384,
                                                        -798401325485350760,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƏƂϛʟȸҰƖҖʛӻФԣàѧɯȈғ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ϝŨ҈ƊйұӉ\x9eȩԠԩ÷ҍǦǍȰҕźİѹшήԧ˶ȷӳήϼҤĲ',
                                                        'ʄԠЩŎǎñϭ\x86ӰÔȌŮʌЃńġǥĬʍΐÊЋSŔÙѴǄƚѤԜ',
                                                        'ˁčǙÅҢ¼ҲψŠʚԍ҉ː\u0382¯΅эɫцôƒêďȬ1Ǡ҅ҊȚ\x95',
                                                        'ȵԠ«с5ƯȟĮbȆZeƖԢӜҙԪ¤é\x89ҘϦǎҫ͵Ε;ԕұθ',
                                                        'ɤˈŒ҃ÌͱȹѳоΌȴΚИÿζ0ҜЪȡDC\x81ʡ\x96дăЍǠϻǃ',
                                                        'БΩԕӆѢӆԋ9qũǖ\x82όʠКӒĆ+ō˽ʉÄȜͼƨҐ5\x8fѼԢ',
                                                        'ɦҫĵҟɃǪθ˞ϥԒҙαʖʾХтȸǖŔǳɝØŨÝΊԭȹt˅җ',
                                                        'ȓͺŷʕ\x85ĦȳӱăөśɒÌюƭҀǵƠдЬ2ƽӟĤȹӰťҕǉұ',
                                                        'ƈΘԝ~Ǳ5ζλ˝ǻΉȜēçӟ×ǢēӗƔ˹ͷ3Ԁė\u0380ҬȐэȯ',
                                                        'ԓ˖гŔӝЮÏbʵĒČюǘĄȳÍƻβȾξĂçʭôġӜǿŊӼԥ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ЫҾɨ˼ҙɳԙȒϿèиЦϿƩíҪϪĿԎİХϏǰӻҐ[9Ą',
                            'value': {
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
                        },
                    {
                            'name': 'љІȟɇʿԩ¡ҊԁӤÅȪȲʼ҃Ҙҥɟ҄ҰнØȑȐ³˚ѣɥϢӚ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220526:211931.123895:+0000',
                                                        '20220526:211931.139821:+0000',
                                                        '20220526:211931.156981:+0000',
                                                        '20220526:211931.173889:+0000',
                                                        '20220526:211931.189829:+0000',
                                                        '20220526:211931.205675:+0000',
                                                        '20220526:211931.221575:+0000',
                                                        '20220526:211931.237497:+0000',
                                                        '20220526:211931.253671:+0000',
                                                        '20220526:211931.269566:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҙƏɃÍэÛψΥưǂϻǴʢ˪ĚŤ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '\x92ɛɚϗӺƵҵʩмƎʫĒͺȑĲɇ`ӌÁВ+ɬӿԖіÛӱҢϑч',
                                                        'ϴћѧǤėʢťϓˎƲaϿѝϟ\u038dėǻԖ\xad÷ɣӐώʈŀĥ҅үˑВ',
                                                        'ўаĽįϻԦźτəЎΦɽ˰ŬĀͲМÅmÙџ\x95ʲƿĄàɻǈҟѻ',
                                                        'ĸѕƦȧѳJӈҶ®БūгȲӟШӿǷĄĀАǞΘПй,àɻºÝg',
                                                        'ƍɝvќя\u038bƅԃŃLЌƼɪ˖\xadЫʾϏĠ;ɦӊӓѬ@ƅȓȜǂǭ',
                                                        '`щEȂōΗ·Ƹʝȸàӎȴυӷ\x9aɠŵĳа¹ǌҝĠΞyϠ˺ʹā',
                                                        'ΧʙӞɁԂȹЗƔѥӤΝÍɁĠԧǽϺʖбϦȹǏƊɋɪїÿѶũȑ',
                                                        'ƓͿ˲Űõ8ÑūƽЂΘɚ+ƠɶԎϚ[ό\x84x\x92ЌзҸӊԟЮøі',
                                                        'ŲƦȲЌѰӥӎ®ǯʠͿҼ½ʐěȸԧҭş,яԤЮ϶ŠˌТΦʃò',
                                                        'ċ΅ѩəϞЎʡϳΐːұҙŻƜTƞРÙӓąǞÈþƘыЙåӪʹA',
                                                    ],
                                    },
                        },
                    {
                            'name': '\u0379ćϔĉ҃\x8dΌíĜʚЖĹѠɊ˰Ǥɷƪ',
                            'value': {
                                        '^': 'float',
                                        '$': 507128.1027307686,
                                    },
                        },
                    {
                            'name': 'мȌβʷӝĊǿɉæЗ˪³ŔhɎ\x94ɻǙs[+бΖˠ˳Đʊƙ\x9bо',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ԡɑύπҪĬӊ\x8bùӱёͿ\x9cϾьӱk\x96ґ²ɕ¤ϛТǐˣԁϙɛύ',
                                                        'ϳϧͻӐɇӞńʰϾ&ȩhӒħĠǟϞʛ×ɍʚԓԒǶιʄϞʠȤТ',
                                                        'ҍίŤѴƷȨȆ͵Ǩ΄ëƏŀґҐΔ˞ǓãГңʈȰӋÑŹŏþɚȬ',
                                                        'œϠưȆÜǨšԌ\x94Ɏ*ӆħĘȎŒǚɐΥΣϿǑƄ8βƽдͲʋҽ',
                                                        'Ĭ˜дC˼ĈÜöÓϣӤȤ2ǾȜǶ˅зwΝŋ©´ŪǎxŤ\x86ƤF',
                                                        'ĥɄΌӬɻҧїƳжѢ«äǜϱԙγǒϖλ©ɹК\x9cӱЃŔ˂Θıƻ',
                                                        'ɪûÃл҉Ĭ- ΕӕΨʸéΎцǣŵϻκζҔŗťˣŻϨ˵ΐ2ʬ',
                                                        'ӟӬзźψΣȊ\x91źęԕрĩdÚȟƝО¡iĚÙϕŖƅӄeʥŀĺ',
                                                        '\x90ŧȢӒӂ¸~ÏхԘѩǽOʅǎДώĎ¥ΈɚŢҲѬǕʉ˪Ͷĥͱ',
                                                        'ΆЀϗĕGˮϚҐʕȿѱ˄ĵ©ǵǋŴ\x93ӨʅΠúЪɭԗÂĳʱ\x84Ĉ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǂŕϠΙ¯ӺĤƛķǩǍū\x8dҎЇ`ã¥',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                ],
            },
            'title': {
                'catalog': 'ɫҍĀӚȡϣ˸ďӲ\x8aҾыËЖϮ\xadљìΏǵÁŴǁǰтÉ/őɇ\x99',
                'message': 'ɛϪъҋ8ѨǞҼʠ$ǎɩϔҡԠӳϤ҉ʶȍþő\x96\x8dĢЩюԠ\u038bŊ',
                'arguments': [
                    {
                            'name': '˩ϒˏЏƐɻ˻ƭɍ˸neÁφėǤӑŜМ҈Ć',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220526:211933.937653:+0000',
                                    },
                        },
                    {
                            'name': 'ͲbĚлǨҿėǬϋԖξӌǱ`ѝʅȌϜǕɼ˻æ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220526:211934.000566:+0000',
                                                        '20220526:211934.016619:+0000',
                                                        '20220526:211934.032306:+0000',
                                                        '20220526:211934.048102:+0000',
                                                        '20220526:211934.065016:+0000',
                                                        '20220526:211934.080855:+0000',
                                                        '20220526:211934.096642:+0000',
                                                        '20220526:211934.113196:+0000',
                                                        '20220526:211934.128871:+0000',
                                                        '20220526:211934.144653:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': ';ËŐŨœѼԦŵςҬӍ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ŸƒԆтɬ\xadǽƸ±\x82ȏ\x998ǛƂȊбΜpWȩWʸ\x98ӓ\x9eʿĄğ>',
                                    },
                        },
                    {
                            'name': '&ШĕСŚȔÖ҉ʞɧɶȁÕɹƞ\x8f',
                            'value': {
                                        '^': 'float',
                                        '$': 532379.429050268,
                                    },
                        },
                    {
                            'name': 'Ӓœɮŏ{Óͻԋ`ǱԚ˳ŽɽʠӅӽŕˌʋ˨ʓ:ԭƥ*õo',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220526:211934.388426:+0000',
                                    },
                        },
                    {
                            'name': 'Ҧ\x97ƛŎΡðƨΗ`ψ˽ʰ҈ȯʪɎŭǐ!ҚȌ͵ȣΖxWɻλѮϔ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220526:211934.457372:+0000',
                                    },
                        },
                    {
                            'name': 'ΘŽʌ\x95ɩӸʝ˪ȱҎʨʧŷͻʴʧĦ',
                            'value': {
                                        '^': 'float',
                                        '$': 755900.6935444355,
                                    },
                        },
                    {
                            'name': 'ԁşϭҩȇԒˋyϗ҆ºЃ_ǵƷӕ£ʭXԄσ`˥ö',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ԄVƾ˘\u0380ҾƱÁǡΒǍʞӘ˹˴ɪŝʕƭƍɯӁЃ¡Ԇ\x85ѱдɗª',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220526:211934.653700:+0000',
                                                        '20220526:211934.669443:+0000',
                                                        '20220526:211934.688712:+0000',
                                                        '20220526:211934.709611:+0000',
                                                        '20220526:211934.729599:+0000',
                                                        '20220526:211934.748598:+0000',
                                                        '20220526:211934.765368:+0000',
                                                        '20220526:211934.781131:+0000',
                                                        '20220526:211934.796717:+0000',
                                                        '20220526:211934.812623:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '"ƪϦԨLÓЗŜѵԗϟſҳ\\ϛ˸Ȭ˭зЇщ϶eӢ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ɜƾȾҭӞƁʵҫЦµàʭüƏӊ\x81ÉɣӨъ¤ğȨӗˑ+èďϘɐ',
                                    },
                        },
                ],
            },
            'icon_id': 'оɝ\u0383Êĵɞ\x82Ǎpԧɺɞß8˦\x89ǦǠÏͺʟӳƿČɑϕÓѧaά',
            'sound_id': "HȫӿԜρġĘԬЪɊŭ΅'ƍӪƼоÏŢǁӕĪ\u0381ĺЉШϧɥЗΈ",
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'text': {
                'catalog': 'ÒӨ',
                'message': '©',
            },

            'title': {
                'catalog': 'ʌÀ',
                'message': 'ʾ',
            },

            'icon_id': 'ӯϘԘӈʺ',

            'sound_id': 'íǲϚҽԤ',

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
            'icon_id': 'лƓҍиƘɥ=Ѻk\x8aϰŦӐȓ\x90(&ҵʿøϯ\x93ԕӐԃҕɲŋ¿ɂ',
            'image_id': 'ͿýΊΈΔĤѽȕ*ǩȞәġуά\x90ǡȖҮΛēŀĊľд˺ʚÛHӎ',
            'title': {
                'catalog': 'āź¼ĸʚҔáϙȔɨŉƏʠӻę˄ɳԬźӸŕʹԠĎ˘а¼ғҦΔ',
                'message': 'ԞǥɋJϋqſſƫɌԈˌҗRΣÑ¬ɓǃ§ο϶ԡӀ,ȺΟɛɗ¹',
                'arguments': [
                    {
                            'name': 'ЅԢ5ėԞԀңҢĀưȖτĳŊíɌԫӈȁnâʪȃȽ\x91¸ŗԄƌȄ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ǐӄӼӿɦѾȲ2јϕ¾Ŋ0ɳƌĂʌL҂Є1ƗǤƀƷƧĪƪǹ\x82',
                                                        'Óʢ\x7fĺЬȽʋɛҖϼˮǻʙɽԝǴġÒáɉ<ȼԉɼȀӡďҥ˅Ʀ',
                                                        'ӡ˵\x99.ŨԏʄӼɭǘĖΝȢѓ»ӭ£зúӘя\x94ϑσ$"\x9cZɌH',
                                                        'ˀřɿ^ӌдϑǈɡгԒ҃ӤKѸèǖϏδɳҘψʆɮƿ˳еƝЗ\x87',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Αŷ҂dү+жΉԔUňȅӜѬ˻Iȱz5î',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ЂԨſ\x80дȁГ÷ӏн¿5ǊЖњÚʿƹ³қϺȑГÄЩҍĝqΊƧ',
                                                        'ʣǨ8ƲӖӞөсʪ[Β¢XsҸǿɆ˝ɪǭϓΐѴѳςԌǼɋùU',
                                                        'Ǻɣϋԋʜ¼ΙĿˇɀʸ˃˦ϠъэŒþƫʖǕϳƵѽΛſϋǚƩɲ',
                                                        'Ū˧ɪңиμǢ2˹ЉҿŉµҕԖɑΎȆĠ˪ʿǥǠϵɸŮѨƜǢˏ',
                                                        'IȄʲơͷǒάĹΔBâѬҚέфˊżʅʇǘҽ˦ѵͱß|ĳфɲµ',
                                                        '\x93ʗƪѵĔрɰũ?ƙοˉэØµЪěˣҝԖЧ\x8dŘĸ0к˹ũԔ#',
                                                        'ӲƁɒЄΞâ˸Ҋ"ԩ˵ЀϬĶvɧŴӴĭȒUжǚӷŶƟЗȽ˄Ω',
                                                        'ƊƐˎêΰʹĀΊҧɘ`ή˴С˂˄˕лӥ\u0378ȏҗӉđFlǁӘǵɆ',
                                                        'ԞîɌӾʡƱͳɨԂżȔ˔ΘŞʕˈǾɬɴϓƼ¬ɹԑɦψϤӝϢȶ',
                                                        'ʽ\x96ҺnҴˉɘǧўӜѐ˛ǐĒΎÝ϶ȯӧŕ˕Ȩ˺ϮΰʼʦΧТc',
                                                    ],
                                    },
                        },
                    {
                            'name': '%ƚεΦφĚɸ_ƝĞΨϱğ?ӄş\x9b\x81Έ6ĂӾҍ«Ҕ\x85ГAr',
                            'value': {
                                        '^': 'int',
                                        '$': -3423387282339561767,
                                    },
                        },
                    {
                            'name': 'ʚҰӼӕφɃ˥3νŠĆѰƄӀӧҭѥıV¨Ȑ\u0379nĐԘō΅э`æ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220526:211950.918286:+0000',
                                    },
                        },
                    {
                            'name': 'ӟªӜjԃĿӸɄ˵ӾϊԧāŴӏ\x92ϹԄΐύфуûÏ҃Щҫłeк',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -5165691951191844095,
                                                        -3960143309778785503,
                                                        -449875168927539999,
                                                        4913954412693196185,
                                                        6637888182994825442,
                                                        -5886872648287274216,
                                                        6640813377871709075,
                                                        1279359348627577242,
                                                        -2259644631185022273,
                                                        -411293204729079065,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʼφ¾â˄',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220526:211951.272818:+0000',
                                                        '20220526:211951.291132:+0000',
                                                        '20220526:211951.309750:+0000',
                                                        '20220526:211951.329451:+0000',
                                                        '20220526:211951.347002:+0000',
                                                        '20220526:211951.368195:+0000',
                                                        '20220526:211951.391407:+0000',
                                                        '20220526:211951.414970:+0000',
                                                        '20220526:211951.436481:+0000',
                                                        '20220526:211951.459763:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Йˣ˯ϐŵĭĜsЁ,ъAИѪλDɼ¯˗ʡNήʩю\x86АӆԪä',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        -49340.16162785817,
                                                        852010.0991400933,
                                                        726001.7076506468,
                                                        559797.6295453811,
                                                        140247.57019793405,
                                                        682069.3122607354,
                                                        927215.6333797245,
                                                        -5689.568155755609,
                                                        718423.5949338485,
                                                        188604.71788413764,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԧːȨËҴΏġ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        177689.9031539107,
                                                        167837.3815414951,
                                                        408274.0401508801,
                                                        798681.2083225171,
                                                        973517.2258633014,
                                                        -68991.94361695035,
                                                        413205.266708261,
                                                        575984.749807992,
                                                        478902.6021064867,
                                                        188440.61395024805,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŃčɝӋҝŽφĠ8ǀΌæК',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        True,
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
                ],
            },
            'hint': {
                'catalog': 'ӘĊoεˁɳÜѶ˅ѝНӵǠσŬČҸÌ҇ЧύǣŕϔӣцЪβҤ\u038b',
                'message': 'ÅɻȈeѩĒżӿǸщӏ3lџϚȰˈŪ˃ѤƚʚßƣűȗζĠ˫я',
                'arguments': [
                    {
                            'name': 'Иϣъx4ȼɨҥʞϜˣȰɋē',
                            'value': {
                                        '^': 'string',
                                        '$': "ȡԁάZ@=˭V;ɁХΟÁ\x9aԣƿԥӢʡùcһīüϤƉ˂ҙ'Ҋ",
                                    },
                        },
                    {
                            'name': 'ͺɳбăѻϛşˮНџ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220526:211952.560590:+0000',
                                                        '20220526:211952.583610:+0000',
                                                        '20220526:211952.604912:+0000',
                                                        '20220526:211952.630666:+0000',
                                                        '20220526:211952.653507:+0000',
                                                        '20220526:211952.674503:+0000',
                                                        '20220526:211952.695534:+0000',
                                                        '20220526:211952.716046:+0000',
                                                        '20220526:211952.736642:+0000',
                                                        '20220526:211952.756928:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǓƩ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        True,
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
                            'name': 'ǢяƃCғȪɸԍѡˣэѶӋϗÒċԁǃǀѹӿ˼ԛɅ˛ʨłӞӴс',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -2370157198049993251,
                                                        -6556606247035640402,
                                                        -5984248522396223952,
                                                        -2335458929773447677,
                                                        -428423599991592293,
                                                        -624833571408455796,
                                                        1853178874746787835,
                                                        -8339729917838687581,
                                                        8954514649726168999,
                                                        9000137465504861924,
                                                    ],
                                    },
                        },
                    {
                            'name': 'åЋµғŴśѝ\xa0С',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                    ],
                                    },
                        },
                    {
                            'name': 'νƱ=щʎ<ΟʌʩǩȳM˺ѝҫƥşΘΊʼҰȿӓ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ϓ˪ΑǉƲ\x97ϡµʸêҜĞϧʩ~åЧȝǾ\x85EʉΝϛģ\x96˩\u038dřʻ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΕϤӑ\x83ԓ]Ϙϯ҈ǖɂ',
                            'value': {
                                        '^': 'int',
                                        '$': 7131750439400747319,
                                    },
                        },
                    {
                            'name': 'ʹҜó',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220526:211953.854897:+0000',
                                    },
                        },
                    {
                            'name': "ŋшҺϢӈϼˮήȥˤРͽɗˆGɭӎªϜ˘Ж«Î'Φ˪ƓŦρå",
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        414784.6379987543,
                                                        72414.3989691537,
                                                        808363.3124231293,
                                                        998316.0427077264,
                                                        960054.654893354,
                                                        46026.942781228834,
                                                        429440.83735947614,
                                                        528460.8972031905,
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

            'icon_id': 'PӹЌɝ#',

            'title': {
                'catalog': 'îƳ',
                'message': 'Ǖ',
            },

            'hint': {
                'catalog': 'ˡĺ',
                'message': 'ź',
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
                    'icon_id': '\x96ѶĪТЌϪ\x97Ǚ[ǔìȋŤүˤϩˬ˻˭ԫĐÝөñŰĽÁŚʥȏ',
                    'image_id': 'ɢƫІɴ;ŵҝԙЍ˚ͰΏƱѺȄøƑ7şΉǵïɬϳӬ(юƄђǼ',
                    'title': {
                            'catalog': 'ϰɀŗɽȎѯB˜˚ɃӹͻɎ|ɮƬʷҝ}*ʧɕǫϮ\x89ç˱Iҫś',
                            'message': 'ХГ˽Ϥ˦Ԫәˡϥ΅ԣƗǣԛЃȝѷϽÞОĚ\u0379ӉӞчКˉΖȹΨ',
                            'arguments': [
                                        {
                                                        'name': 'ŽʬŶɘʹʈŃǨHȆȠʆȹʕʞȢĝǡθŮ˾ǃɁӅ˻ʺӃƤ¯Ҿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ЇȽƅ2ѕϪЀž\x8dŝĆө¡èǜĬƚŋҺèħŲΚʊˈęϣâиů',
                            'message': 'ȜԢЄ^ŮȑҟӻɀǟɪΈϜˇXԨÿʄkӀāϦɯЛѴӺԃϴӚƕ',
                            'arguments': [
                                        {
                                                        'name': 'aøēĞҕźǰ͵ʮҵǜϑyÀӣȀ>\\Ɉːǘ˂ɊҩƽΥ\x8aӺȒȉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϷҥɸАˊĭƔƽʻʌʓÊԄòԗΒŝѿºϱΣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˗ɆňƻӓǢʵӱƵŚʑϐђɕϨҒȆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɀiΫ;Ƈɚ\x91ӏǮƅ˩ϾÚȒϥ҈ғ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϢƃʱҽχĲˍʹіŭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6749537026376507399,
                                                                        },
                                                    },
                                        {
                                                        'name': 'тϋɼԪȪȕʹɢ˚¨ҵŗýɖѢҀҷŵ·ɁԞͶƓıԏУ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƥҌңѝΏʉ\xadʲäїĆҁŭѵΏÁT\x96ѳϮƁ\x88çȲѺ°Ǯҭ\x8aϧ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1708512136741786975,
                                                                        },
                                                    },
                                        {
                                                        'name': 'AĕɟƘlɒǰϡÍǬԁÎƢǊBÔɅ҃ñQň',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˮŜƷ˳½¶ȚϲтĒ˷ϐŒ¥ɉϴǠϕǳͽшПõЊȪҜҰÕĴ>',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧͼȽñĺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211935.917526:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØƑёϝǗŶ®tÉŸ҉ϷԪƟΰěӉύԪɏƗђϗŕйͶЅƈ?ĳ',
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
                    'icon_id': 'ɦԗ¬țΎӁĬĉһöŦ\x89ӌˬIњӮѻˁ0ǨӠʏȮĦ\x90cϔ˞·',
                    'image_id': '8Ƶ\u0380æeҷӢŮǣƆԨѾĭҩπόҷъҸȲ¨ԏƺÐ\x87ȱѥԠΎǀ',
                    'title': {
                            'catalog': 'ԘΟìǴƚˍŲʹΦȵŴ\x8fӵŁÄЋĮҎ\x98ʠʸДÝǴȎ\x9b7ƤÇ˕',
                            'message': 'ÞĢҷêΤȸəǲʣ\x8eĊ\x80ζơȀѸÅҜǏȂΖ-ӓȣƴʪˍȷǢэ',
                            'arguments': [
                                        {
                                                        'name': 'ҌĵțΦĲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƔɼɌ"ѴÈϲ¢бЊэ;\x8dâяȖѥd¿fǹnʱʈŦԕƛŹʘă',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѧ»νӂƋ\x80ĩБνѹʯːΤɗćӞʉkȰ:ʉƇǊȜΣǳ¦ȍѝӻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЊɔʔƘiʈũƢȵðҽҳ˾ԁƉ\x97ф²ȵŕЍʂĘҼӤѡnЩϠ˰',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾ$ԗұˡѺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ċìaȯӟ¬ȜԔkӾʫ˕ʜЧ˄',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˙ҔȨϔ˞ѫʼȔѿˎùɞԋοĞēӐǂa4Ïӝ˚ʏƔұŲķ2ɞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƐҽʌͲǅɭЕčăӏ\x97Ҷ¨ҭȠǾ˭ӜӘϋҘ~ôҠŖǲѰӉҪȾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҞҬ\x9fǴҤŬӕkќρϒӨ\u0383ť<ɰӶϣÏΦ\x98ςԆϻВûӷҎҬt',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƕѕĨĂ\x99ƘǛɉ&śҊ*eKЮ÷ƧͽӄʡʙȸҧŌpšűԍǐǥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёUәʏʈ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҴԭӜ#Ę\x96ʵRĺ\x9dś\u0378\x99ǝɫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ʪƸГƟÙͱғŃҭĝɸķʲƎǃҺŔˈӶΥˈѡԀϼЖV\x87҉Ѩ˨',
                            'message': 'ǾҠϊǧRŚѝѸЙʷƝʹӧлĵǽҎʚ¡\x84ØªȟÁǓǔ\x96üҌχ',
                            'arguments': [
                                        {
                                                        'name': 'М§ѓƎʲƈƔњωǩв',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '§\x88',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƪ\xa0¿ҔХʢrƵʒƈҴ|ŭЦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9095859594966090744,
                                                                        },
                                                    },
                                        {
                                                        'name': '!ʸϳfЃˊƅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'өβǱЧЕÇ=ĤʘԂ\x80ҒίϫƞɖЕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƈхё\x8cΖˌƣ\x95ƞƝΟͽʞСŅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϸəӦʇĲĿѥ=ҺӍȟͺʦ3Аc°ϩƶƋäѷǮɝ*Ӷ϶ĴĚǅ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȩ˗nŌǎ£\x87ȎīХѡƳѢȯНЄƖѡШȵ\x8bɂʯęǐ*ҘʸȮ¨',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚԡMƄƚĜš',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211937.492551:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'YѲ˦и',
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
                    'icon_id': 'ùЇìӍϞϲԕϵΧϽŨż˃\u0381 ѯԕʸQ2ҐiÁʔӨӷӋȡĩV',
                    'image_id': 'ҾԢцϟɣͻҙŢ\x98_ΗƢτҨӠӬϳҁҪȗѸʝҪѹѓηϱσĂĖ',
                    'title': {
                            'catalog': 'ɅïϰȔɖ6ŴƂϠǥșԡ˧ΥȣѫȉЮơÂıѢʜή5Ѣ˃6ЋŨ',
                            'message': 'ɈƯƎчӰɕȟΈѤĠzɩʫuǞѳˑxΔУɅǏʺЕƍʽ´ˁĻǩ',
                            'arguments': [
                                        {
                                                        'name': 'àŢԨƱrљØ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϽҚћŦǱоǂĄΜ˒ϭԡȘ˟¥ΡƓˌ²ѸЪɂ3ҡIɆǗͼƒč',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɓbӽ˱²ǐʕͶˮuȘɮɭţϴʤ(άȶ*ӭȟ5ÊŰɘĚ\x82љ:',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӸǼӎȵҰlɪҰЛТ\x93ɯӪ?',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʁfŵ@²ЧYО\x87ӟ\\ȰɦϘɗѸĎӑӎȟėǂ,ԕЛÓFƕ˗8',
                                                                        },
                                                    },
                                        {
                                                        'name': 'nŚƗŷòӷ˘ё`ԗƨ=Ğ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/ԫƄȶſƠɽȊ$\x8fҖƜϗΝơǩ҄',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷʘƃȀɿɦԔÑī˖ȮǕȷЎˉýǿВǦӄˑȂˀ˯ƀWʠ˝ϒĜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'şʐ\x89˗WΙMş\x9eП\x82ȳѪ˷Ңʁȗ(\u0379ӊϰɨʃÃÈġŇΪĤʵ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǸԗǛҧ´ȶȕȦùĻŭǲēЁϥʞʣѷҫ\x8e\x800ӁȀθĽǀȭТʔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŕǂÎbȓԪˆюʉΞΜпә΄ԩșʝʈđɽĭ\x7fћ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'КƚźāǒӘœʍҪ\u0378ϪƾʇOŕȷˆÇ҉˸êΪʲ\x97oŜϜ҃ʫԤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'Ⱦ×ŖΣŷԨȞɢ҉ġˬɷÊ˪ĴԗЗɧěƨ˚ϊŞˇО@ɛ\x95ȁȗ',
                            'message': 'ь&ЦǨ҉ѿІÅ\x9cг\x8dѝĖĿˠȋZЪķˊʀѢс±Ĵϴ˜ȷǖį',
                            'arguments': [
                                        {
                                                        'name': 'ưӝʹČ-1˦ĞѷϺ:;ôĂϓɃ\x90ĨŅǈȸʘйӔȵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4838160081722513785,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ФŽёѥÉӱ7ϯƁчґПŏGƗw9ŤƦ˜йҰƉĶˉʙˠҭ˹Ӥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'þϵźʙƊʰξȼˡʽѮӇ;1ƙɄҭ.ĶĎŅÖĽ;źɵϛƪӨЬ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211938.636687:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǲщԕò>ƗіĽʶȻĈ˶ϲȡѬǡȉğɠĴ%Ӛi½ǅѠԫ˲',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ČSʶϫʜÀŦȡȼiŦ¶˕ӷΗ˷ȺЪԁҟИɡ˕ԨȲҰɸʻBž',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҈~Ş\x9fԤϵ\\ȀӦĂβǍΓαҠ҇Ѿɤ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'лƇªʀʁμϨɸѮūĐΧ\x81œϐʝƱʚΣ$ȢПʤϟπ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԑɮɝї˚˂ā',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԝʶm˴ԃ˼ǝΥʜ\x9dӃκǆҨ˶RӠϝǞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211939.067112:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'я\x8eϡχ\x9d³ҏӚϔ%ϝƥ£Ʃ˪Ʋ;ΤĢ\x84ɊŏԞɊÛӚÒĮʴR',
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
                    'icon_id': 'ĢӄɼȺǈjŖ',
                    'image_id': 'ʗ\u0383ƇўňȔӠʄbЧŰԌ͵ĵΔьʔåǀŠъiҷ;ɚҝӅ˽Ů\x8b',
                    'title': {
                            'catalog': 'ӠƷͰҖѳӡgƣȎϲє˽ȏϨÕԫÿԕŅƿҙКɨǖȴѺ6ʱȆ»',
                            'message': 'ǿЧϴōɱpϢƀŧñŮЪáӱҷЩ``ӔʜķsԔǥĄςҽOϨ§',
                            'arguments': [
                                        {
                                                        'name': '˔ŎbӿƎӽɘ¹7ĸ˹ėџˆ\u0381',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʚÆϥ҇ʤ҃ρĈ˒ðiŗʢҊȸøѱьǳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'çäοʼ҇ŗɈģӅӼ\x8fϫ^ćŎщʅλÞƳʹoΨǈã˷ѡːϠ¨',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1306482648253838525,
                                                                        },
                                                    },
                                        {
                                                        'name': "˩ȢʖëŸɫŸˎäƧóű'\u0383°ď©ВđåНƂЧ*ҞźˊŊ˥Ê",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧEŭÏºл\u0380З˟ÔƤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΣȞτƔłЮuҺɑʶάɦʷɓǝψ˸ʲŹ6ѝɐ\x82·ņ\x90ʿbƍг',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЉˠĞ÷ɲʌrё˙Ϣѻ[ȅʳЯǳϦьȏǪKȝÜð:\x8aʤ҈ȱš',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211939.763408:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'îʢʷуӴǦĉȬĞѵȃЯŲ\x81sΪԧΐϘό,\x9eӪ¼ƨ˨Ŭ\x90ѿȥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211939.851388:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵ˼.ͳЎʓŬɳϽѐʰʪуΗ©ΞЗĉΒʃ˶ˏ5\x9bєĢ2ȸĪȔ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ßħRНɃǠͶŜѿ2ĸӈǗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 917776.4862954973,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': ']Ћͷη¸ѭɼӧʛ΄Ӡȿϣʂʭ˔MҐԏŵ˭ΡȐƲϡƊȗĚ\u0381=',
                            'message': 'ҷвʩbƣƇȅɊϤθĂŋ¬ˊŚɔКȝӨӟČđѹɆʓ҈ƍTɫ+',
                            'arguments': [
                                        {
                                                        'name': 'x]fό\x89įԠƉӴΝʰȫȵÈѥ7пýҎīrҠŤ҂ЋѽÃǙɫ˜',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŕȑ¥˫ƿ˯ɓǗȁϖʗ\x8cͽăΏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '6ȱǬҮˠ˞\xa0Џϴԝςѱʲʧ;ďεӟĝÍĄĥè¨ЍИϭӊԅХ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚÒľς;ǑЬǋɚǤ§Ãϓɋŵоѡ¤ĐǺŀӭɋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211940.323562:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯŎƓϫμĝοԁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸʩŵȞШǤάʩȠӦʊΪκãс\x9bȣІÕ\xa0Ʌ\u0383Ǐ7ԎőшϣЃ\x9e',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˇ&[Ȇɇǵ˓Ǹǡĝ3ɊČ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĆͼЗYʹ\x91ĪΎǮѨΝѰþμȅǞͷΟJʓϯːРђîѮАџıĳ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211940.594796:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'øбȃЍˠšέƗŃфưԁÈgһʜѷWўШɓ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ęҚ0XӮԠÙʍõůιǓȦģȥNθȥкҞјq˛ȥ˞ԑʕžÒO',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 963010.2966308221,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ʜҬǧˍ˔ҼƬdʅ͵ѠάƺÙӴˌźʧÌνtŢьҳϓˠΠЄ°ɳ',
                    'image_id': 'ϓǟ˶ΘΉǀљ˅Ů½ΎæeƳͿѢʜȋʂǽɂNˏç҆ǏӪƀʈ~',
                    'title': {
                            'catalog': '.A²\u03a2ȋċɆɀҹƆǎ)>ҥb¹Ǽŕʍԧұ\x83з\x9fΪ',
                            'message': '\x9dϘeϬTϟĩͼГåąҔ\x8fҚõӆҨƊͺ\u0382ͱưλҙϜ®ʈѱĒǷ',
                            'arguments': [
                                        {
                                                        'name': 'ǼŌҳʏ2¸ϊӽůưҲԌĊΒĹҿџϘɮϓ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'șșĘʹƻĔHІÎϴ\x87\u0379υvÿԪϼӦ\x93Їщ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 376248.67562705657,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚȻԄѢϠˠƩʬņě˥ͲҾÖИʦîǭEǏΙƾɕѤ˰ӟʞӺŹ»',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 470937.2588859529,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆƍӈыԊ×Ҷʔԅ²ϫƟңуЋgϚƜýŅиˆŹʉϼíóϤŐ\x83',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĐəȲԋƑʙ(ƊЁŮώÀưüϭӶƫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣ˻р˛ȈȐƙƮӕӚҼѠ|\x8a',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѥ\u0381ʅ]Ң6ʅЬҍȅѯˎȳéųʴЋʿȁȼсұ¯őƔΔ»ʢҐƃ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɉʑ·¬щΊD·\x9fӣԬ˰ɕøӅΝ\u0379LԐļ\x9cƟьɁŞʪԚȓbċ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ίͼŵ҄ƘȺͺ'Нʭцʼɾ*\x80˭ѶƤФӎŁŌΖ\x9baŝӷɃб\u038b",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ШϻԢĴ¹ϥ\xadH',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '{șţŤ§ıЈeͷƔӾщʔʭȓªĠŲϮˑ\x9dεҙƟƁκȤˠƶċ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҕqϐąӥΔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1190956744572896651,
                                                                        },
                                                    },
                                        {
                                                        'name': 'tϛЏ¥ȡȰЭ˛єѝʴHѝħ6ʹFWЭѐǌ˰ФѳԗдԘwÈX',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ʯ\u0380Ą˖ϪʗұźκóµʩŲɆ˘«ӱ@ӨϐӋь˓ɇřnÿǚĵϑ',
                            'message': '҂˸1ĊϭcԫӁ\x8fʝӦĈϛȺǏӤϣ¶ӺљϕŀĤWƤНӗɵ˳ÿ',
                            'arguments': [
                                        {
                                                        'name': 'Ôχԥ˾ļҔǙĄű²ȸȝüҘӳďľɎУƭ\x81ɜ,ЄŻʍɲĚρ ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӾǕ.ѲˎùƩOƟΖƩíųÎѦʯɼǘπėӺƵОҰ҄ѸĻ˲ƕ˂',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҖÛѴθʺЩ˳Ǎ5Ô˞ФǟƾЋҊѦĝϻƗ҇\u0379ĵȢЗ\u0380Ɉ\x81ſē',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÄƿMşú҄ΐʄȁӌϬȓΝґЋτƺςѭĽѝǜǶӉoƔƴğŻņ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 808904.1143081303,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳ¨˦Ьӓѽˎ҄ɨʛǆÝ˼н±ŬʒΆƳɥɽҐŋʉÑĜ·ɣ˞ʫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯьчąƻŎɋċҝǴʑϨҏĕжӺwҕȣ҄|',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 854961.3675037622,
                                                                        },
                                                    },
                                        {
                                                        'name': '˞ԌƁψ˨ğƗǶσǼȼУŉѝѲɏӅҕӘӣĪ5ʵϝЩƸ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʥ͵˭ȦȌő\u0381ԑɃ5в[ң\u0380\x8eǚ@ǧӕƹɆú\x85һƲŁϡȊЂЯ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ώ[˨®ˌЙǸςÔΖǼДВэЧԤ˅ˏϺĉɐ˲Ƣ˵ҏѢhӈϚŊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϬӰɌυʡȯ\u038bÏǍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϚϪКɻËȯɔʕÑ1ˡ˽¹ŜǐϜȘԅԥǆӚ^ʤŁǭϹɮˣ~ѓ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ʨéȪӧ˯ʹΉƤƵÀ[ԫ˓#ÅѨxΔк\x80ǞҚә\u03796ӨǢҸʩȈ',
                    'image_id': "ћǭԫOϖӍ¼\x83ѿØ{8Ȕͼ˞϶ΜэӺ˥Ļɨмöɜ'¤ΝƂ}",
                    'title': {
                            'catalog': 'ˆƂɴӦ\x85ԠɐêΟѩӪĬQҿʖҝѸXϟž˕)ѶΝПγôɢɁ˼',
                            'message': 'ϨŤΓΗǢeƤɗŁ\xadΖēŪѭϺҴ\u0379ƢǯƚȖ©˽ӱɫʸQÃǭж',
                            'arguments': [
                                        {
                                                        'name': 'ѷǴϫŃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟɰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'οŢΓӅӵә\x84Ӱˈϰûɶɱ\x87ÍѿΨ2ȖǸʨгњПȹΉôȏð\x8f',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΣcӰÍ²ƘɶІԝ°ǘʲэ[ÇиұʃϷԔƶӃ$ÓΓɒӇɕϧȇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3487147287922755271,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĳӊѿĄǀ˒ʊ·ςƵϐɿӖO˨}ÆʮѲɚȞҥҾɁǝρèѭ˥ҝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4737463620028975510,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩ˂ΐԧӣŐɑ\xadԆѰ\\ʞȇ\x96ƷȨɨҰӫҗӔņ˃Ǹ\x8aЮ#ϖȂҫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽӤϏǾũˊѽ¨nć\x80ùѴɖɓưˉȃһő˧',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211942.973812:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵŠøңӅƻҤӄˏȧńʢ\u038dȸҢҡũȳʕʼǘʂҕόϟΎҦυҥɿ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211943.041419:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '!уȹ\x81ѧɽіȐϒ\u0379ӄ˘ˆǼ¥Ҷŗ2γӰχ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀ˸¬ɂƁԋÉԣ\u0378ƯҢΒʟԕИȷƈ\x8eԔÓϸԜ~Ӡ϶ȓѧιɷЍ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 82380.2420658833,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'вɶȂΖkӯԧǟϩϳϧԌ%ΘϖƀɬúĚηпƗб\x9cɴȻöӺќΥ',
                            'message': 'ˠʈΔ!ΫώɴŏɪʵYãӏ¡gǑΙʻћԠȴȳǄѺԟһΧØȖɶ',
                            'arguments': [
                                        {
                                                        'name': '^˨`Ğѹζ^Œт҉§ǘʑøŎԖϺǿΞķȭÄ˘ФÜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7434238718172374669,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӜĹ\x83Ϛ˚ɍЉљK\u0383ǐ͵żυӜΕ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷώϣǟˁӾħȴùȟơƕĥÎϥқȇ:ȏӷ¤ϰψ˅ӎӍѝĮҪǟ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 93358.2645934957,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŊӖÏɰΝ\x9a¤ҲɯŉȦǨѭH{ȗ¤ή˃ŽԙѬǆ¬îłĺ˯ġĿ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĥãǎŲЕ˕˚ΒŬѮ˶ϐҺ0ŕ×юÁΆ7˖үʦҸˁ\x99¥ΣȲю',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϧǯёҟrɽȭ҃Цʱ͵іԊңˆјɃƦ҃ţŽŻʋɹɢǅ}ΞϏ˜',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǁ˔ĀˎȡΓ˧˄ΤŶȯϚ=',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211943.652487:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'εҏ\x90æɢЧѮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'èϤțðˈЀřģØy˙Őҡ˔ɗяӣȰéɄ\x8aĎǰŮӳʪъ·˪ʚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӇҷӦļȄȺ\u0379QЎҨʫˑӲ´ħ˒\u0380ФπЂĮԊӓ÷ϿƮĻǻ\x92_',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪǛӢмMӲƭӱҕқ1\x9bö',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ŴīȏȞŰɤҬȈРƠ˾ƷƱ\x96ғоołϥ\u0380ɓƪԄŬĶɑȢǬӢϔ',
                    'image_id': 'Iʞ\x9c1ƿʋґȌͷͲҼNĞʺǝǏʣĜÍҰŊөʹŝǉ4ǠѠԌɔ',
                    'title': {
                            'catalog': 'Ų˩ӲQҢĆьġĴő¯ϑuʞԏƴ˾ÄԖɹO˲ÇňŽĥĒu\x86ǻ',
                            'message': 'ЈӊüДʶŋƺϒǃӭÑǃέĎpƚƻǪŉǰĕϫ¼ƠSͻʲŠӪř',
                            'arguments': [
                                        {
                                                        'name': 'ĒôΓ·˽˵ĳʬ¨h¬ӉŔ·һѨĚҿ\u0380·ÜʚƯ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '$ӆŞƠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\xa0ҟӪ\x8eӜȾȣɫфʉϩűȇƓɞǤľʏʠȂ\x81ӁǨLѕЈ˂MƠȰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 913354.2119968706,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͺɚȤӂŞВĽʫȯ\x8eě˴ÅɅȕЏΆΨćɚŽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'óҀŴԙЏВ\x9cǴ"ã1ΜήЄΕхxѣљɿӴ҇Ċğɝ˜ΘČg˔',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6907616624220263598,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҡ[˻ͺлΛʾЉŒɣϧǎӝ°ϿzǜºԧɩȖÄƐҚτ˞рřɓȜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211944.426208:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϪYȟƎďԉёŋˀäǛѮĄӅԗØưƶͲȒҍU\x81ñʞŷЈǒǏĘ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 851514.2454124234,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Â˝ϴˡƙ\x91ǜĻċњӂϋõԃӃZӧѮɴμǔŠòǠäʢȉǵ˨Ų',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7099222189579551185,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŞƑѳϝ|ȟӅΣ0_ǧӭ\x8e>ӗŻͳѬ˥ӳaƥΏӦȗƭʩӶƱõ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'oũǉԥʸÇ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĮΤїëϯů\u0382ņŒ҅ÔУǝѝƂÉ¥ŚǹĨΰЩ}ɮʾӤ$ȫƝЅ',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': ')ԪǏͼɫ˕\x9eӊaВƓ«ëʻүȦщҤԑȉuϺƤŤʏЭç²Ԫt',
                            'message': 'ëЫȸȬ\u03a2ĽпΧŀˣІyţƯ·ѵЪʪ˳Ʋѷ¥љ˕ҀTʳɅ]\x9a',
                            'arguments': [
                                        {
                                                        'name': 'Ҋ½ӕѴϛЬ\x83Υóƛ҈Ψӵȃȃ϶rϋï˥¸BͼҟŃʳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȔɁǑɐǘͽЗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѶЌcЪͷɨүΐџԙҗȯЋƨѮ`εϱʺ¤ΊӨʜɒˣͼ\u038dȰԖȸ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŶԅËȿ˟ϲŸɤĉҗԧԔǩǒϻϐʸȷ(Ơтӡq˩ǕïɝА}˗',
                                                                        },
                                                    },
                                        {
                                                        'name': 'sư.üÏɶƵ!ύԫ\x91\x93Ѱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ХϙǭȦϴ˽ɫ˞ϚȣʟAĉˉԨҌ6ɬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁшѝǘί^9ąόӇʷЄ˟ӛvͼφ΄ǭȿ³˘ϳ°ӗͲЛȊª©',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211945.215938:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӝȴɰͷɺʊÓЋVǆΕ˔¼ȮɛʉѵϾϧiƠ®õĿǈєΚȒϵѓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϻ5OͼӾƞ҄îæõɣь½ϡŝɖɜ"ÁƙԍƟѼʭұ±ɬǑŚԁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɀϾ҆қ˳ʎҞҖ˻ѾΑξʪΤӃЃҼ¹Ͱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'лȪϰбćǘǕÜƽНľŨzԣηҧǙȳʅOэƋšçʆϹJͿԘȡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211945.484918:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ДýpÓЧҔέooԩŴӹʼӓʱȻу+ǫʝ\u0379ӃԌũ˒òŬτŨ½',
                    'image_id': 'ʶҫТФǇІқȍЌӈӲèRåǷхӍ?.Ԉɦĥ/Ş˸ԇȣϬ\x97Щ',
                    'title': {
                            'catalog': 'пԂȟѣwйȬҿȹ˞âԮӡԘ\x8aÚƭΠȏҏΆхӡAӢōɜcϳǣ',
                            'message': 'ӸϓţԁѰοřƶòԑӬDƘƌY˙ɅǼćԣәǪӃÀ\x8b«ÐŝϠЙ',
                            'arguments': [
                                        {
                                                        'name': 'ѣîιŁȣϑƕԭΪ˄Ӎυ\x96ӞѠҸҹэȧƳƍ4ѳϤϤψ_ʵӱæ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'όÀԧ4ˇ˫Җ¿Ǝ˅ӜǔZ˖ȰЕѸͰξΤɻǞ4',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6670593460337022735,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥÔӗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 296029.69177615567,
                                                                        },
                                                    },
                                        {
                                                        'name': "ĭǔņƛУϪƻ÷ѾɊҰc¥άΕ'÷ѢƁԥ˶ňɤѮΏbѢʌăҔ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '҈˟Iԓ\x80ȲȉàӾțҖЉ§Ú ӒÛƄӽÊԛʎчĻʬϑ|ˢ{ӝ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӐȟЕԑń¶ͺ˲ЉˣӓгΈԙ.ɶ\x98ɆӴʞΞ˸ȯžхaѦ¼ɂ҈',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211945.952426:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҴÀçˣοģĹͱNʣˤȪǗ-Qġԡ˧ďİŶоt ˼ɀѱ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211946.020834:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҭǴͽƲƌѧĽȐȉåÙũ˗ìįӾǍ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҿɮ(ȨƏŨ˯ӹǑǃÚӤ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211946.153673:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˦ƑīΕѥпƤϦϸӞ\u0380ʽԙāȯĭŘǗÔΉçѼӦЭдÀΈāŲʒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϭѿƌǵ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 81991.67022425128,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ӌƤêµʴ\x9aͲîУʑўɻϚŒεȚЫӍ·ԩŏϮʝĻӹӷɝαɻƷ',
                            'message': 'ŚӎɆ\x9cԣ©l\x93ǡĪrƗƙ®αɛǥķǱɊԬƮѫɆʦNθĦȹӄ',
                            'arguments': [
                                        {
                                                        'name': 'ʫ\x97ѰˀʄϱқԁƎɐgĔӝƾȏӿßҧѦԓϥ\u0378ʻ¿ҨԩƧƺĳ7',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211946.422336:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': ')ŪйЩªEԊ˷҅ɪԌкȢӳмĲǻȄǶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽʒ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЉYτөǢӮ˛ƓQƦƙӊūωσȝȝίÃӛȞoӊϷяĸӂԢыѧ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8542415728830839066,
                                                                        },
                                                    },
                                        {
                                                        'name': 'èǻďц)ï½ӃÊӯĽ˲ήJǜ3ʱɑӧѐǨņӢϋςԁЭÅǜΊ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211946.695186:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͻσɴ˱ʔӑBêԓй\x9fϏ˅ǅ΄ԦǤő',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'wT:đЧ]ΦΫɦһЯİķ¬Ԝѩžˁ¾ƱĊʊǛƬϰӌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΨѲ˙βӺƮ&ύмɈҍȌǍĖ\x82ɄuΞ;',
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
                    'icon_id': 'ѺÞʫӴѷΞЫÆ',
                    'image_id': 'ӲƹĲӅŰҼГȰ,ҝƩÊͽĈԋȈTňĞѸˆȵʆŐӿöĂɓӵɾ',
                    'title': {
                            'catalog': 'ªѾЍҍąЯӅЫèѢýTˌƙҚŝ˾ɏȌҤȒӊkKљОøŨԖХ',
                            'message': 'ʄýƘǨȢ°ИįǃЫҏΙЭ±Ҥ˪\x94Ōε\xa0¦ϐ˱ˋѬť˺ѦǂȰ',
                            'arguments': [
                                        {
                                                        'name': 'ёѹǩ¼оǉӦѐӀͲħˁƊѡʾŠɾπ˄ԑ¬ĆÄԠÁʸĖμ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211947.074950:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀıŽ\x80ϮƑҀ\x83ȍъ\x82ÄÛʚľ)ΎɃǈ\x98ʆ\x9bΣʊ\x8cȩΊĦȪG',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '"Е˱Ӈ.¥ȁƎ˨ʪǤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϷȒÅ\x9cԧѼЉ§ɓɱғͻϷǃïɼЉÉӕѫҕĬɼJҀ˸ʫԜhс',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐư˚ЧrЗԮ¼ŁÈљOǌÔӯĩÒś',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'р\x9eǐҗԍɉ·',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'XϻԔӻǌˌϨĳә\x95Қѝŗɨ=ľ˶Mǟˣɰӝ\x95ɕņŀɖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211947.497257:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄɉȶƏřÏUӓðȯ˓ˬͻ˛ÿƞ0҉ӱ\x9cșG˩ӎɞˁɎŠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211947.566244:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǬÞşθÛҿӴҶԥɜ\u038b˽ˋԎɰÎƧƹǒîãʼӫȁğŗĪʻĊʷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҼѪ˔ÿ]©ϱҴȶņхǅȝ\x99ђĮ;Þɷsǰŧдƻ\x8bӂ˥ȮҿЊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Йѡɳ\x95ÏƤ\x88ӖƸƻΔ¬ĖŲɧñѤʦ˳ĀѿÅʓɎЊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ЫìЇ˔ĥΙмԡԫөȚǏпԂĝұμŁƍŇ/üэпéń\x89ѶYЍ',
                            'message': '¤\x89èԤĿ°ɈVƏǊìȶϤǒӥƅВú˭Ԕˇ<\x8fРƹфϔȆӋН',
                            'arguments': [
                                        {
                                                        'name': 'ˈϓŵȅͼӅЙӾѵăлx\u0382ƓȆʠˢ\u0378ɺŠԅҌϏƬȣȵFUаȤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 527364.025107265,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԇʤğĉцСѴϾ˝Ϙǔǣǩrñј',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'kͽĭѭԍ¾İѧɶȞ˄ƴǗ\x8d\x8bǾϏӡȺϼɜȢӗäőȤԧĀīǲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6999757283625387483,
                                                                        },
                                                    },
                                        {
                                                        'name': 'љ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʔҌц˴ѝǘˑĻΓӒǷКĢǚͼȘΠѧʃĪҝөԨӦˢ\x88ªȟ΅˘',
                                                                        },
                                                    },
                                        {
                                                        'name': '1£',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѨùkțĿĬĪȃӖȃ΄ƳӪџζĉȺáу˔êҠƅӏɩҟǼʿ˕Ԧ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưεɰXfйŗɃ=',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΦӑʀʁʝǜҊжʳWҲӘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɫʅĔԮϳӥɕ[ң',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7321799339806965864,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΊϹŒȋĦБӱʇ·ɍƱȊ\x9dŕ×ѳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ˬїҩӑЋϒ˝ΧЪȚƽ˰ùȒьɾҙʺƥûԠŻёԙȥĘͻžųμ',
                    'image_id': 'ȼȋӀВͻѽϨ\u0383÷žɫ<ф˂ξǛҿŮӱǮȯԅͺâÙȁБÒĳ»',
                    'title': {
                            'catalog': 'ɲвʑõÔ\x8cǽҦȮϡĘ˗ĠЮȦdҚɕű§ɈӘήΣ«ӁԙЯҶ\x94',
                            'message': 'ȆȾюŁʚˬľϮѪʎĤԤѯψǜԭƸҌçøȱʧԐԫɇȼʃӀłϚ',
                            'arguments': [
                                        {
                                                        'name': "ɨě\x83RқԦƘĖ'ʲƛƭžӒЗʱ˚Ą",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 406998.7144013317,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ž',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷX˭ŕˈȻӺѰùԐЦɕʱҷЮԛHƒ=ӌԬxƊҾϦВςήãj',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰƍӽ¾ҔÿӍĻɴƀȚģΕ[ˎϷˌϳγ\xa0ϋӛǰȣҁĔńãʧ*',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'АŔϝʄΏԨеˋƊʖƍʩĀʘȝʌѷƲѕƄDɇȘζM\u0383°ȺŵŅ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8eмЁĬ\u0378ÖʐҀ®à²Ќș\x9d¦ûˌΊЇÙȒĒ9ѢʜwӘʹŮ˄',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԉ\u038dЗѾȶưЧΟҹǀʘĭ¼eʹѰΎ*Ԕ¡Ȥ}ȥǍɞƬ˹ØǥȬ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥ¬ɏƾ϶HŨӪҍɍҕ\x96ǫAӶʑÜǫҐѥҩԕē˨Нђȷȱәѥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Оe\'˺\x9aɰЁĭѩĸͿϹÛΣŢ҆Ŷΰȶ\u03a2˹ҽ"ĠýÜЊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'νƍѴԓåғɡbƌļʊϹƀÎԈȷӦʍΆÊŗʆΪń',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˊƨӲԞ¤чюҰ˘ԠљÔʩԄӼșĶʷɬԑÉ¨˲ƃʗɱŰȁ\x92(',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'рΓɣ\x90Ɲ˞ˆʔʽЪĦŻ)ĻвɟӖԞĐQЃʎԪΧš˪ӒѨҸʏ',
                            'message': 'oŴĪώǇ©МϲǫʾˌˎϞӢĚѩ»ԕʟĕ¬ĬǐҌғ\x9dƍԤ\x83ϯ',
                            'arguments': [
                                        {
                                                        'name': '½æ\x89ȽʝǥĕπŬШ+ЪĩǧɛhȦСî˷ÍʲϷLkɾɉů˓Ų',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪçŝŻŊȆҵʗˑѼġɗª\u0378ԂñǉǢȄɋ˻hȂϘƴĖҜÃÚ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒώЛɩƫӖbφˮԣûQіÓΨÚԕԛƔѫŅд5ѺǸaӠϔWƬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȨȭƀġÅHˡm;ЈǄǯǝΆλ×ҵʍїÿѰΥԞmĈšʚ˵Ӌͺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϓǤǐˁ\u0378ӊȭÍҞėśęŲ\u0381ŲԑŸˮư\x8bԙʎӨƝҊăӗςФO',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӮϓС\u0381ҭϔĥÝ\x98νǂʽӁǟŶˍͲӂԘҔ\x86ŖΨӷƟǻӶԙԇʊ',
                                                                        },
                                                    },
                                        {
                                                        'name': '<ʗѳhΪˈƫһ˗NӵϪҟѳdԩКѤÜzǄ\x9b7YǙþϊ|YҤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǣ¯ƘϽЁӉņѩVљΰµ;ӻk',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211949.813220:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǚ˖ͰĞPĲĵƋǓΎHҩ\x8eɁºǿϦҒԜʒРÕˎ¬ʱƑ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211949.880995:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϻĤ±Ǣ~Ϡ%Ŭǂҿú/ÄƘʰīԑΊČŰɬӸΥȨ9ԪʃŬ\x92Џ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211949.952121:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƣʹȇ˓ΐȄaa\u0378ɗΪɩŬў϶ҍǴĽɑ˞ʿΘͼЇƜͱǙ@ʦš',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĐʀɚвӅњOӿӒʧЈ\u03a2˶ɐŏɤǝųΙѦ¯ѵԙӐØȞεYʃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
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
