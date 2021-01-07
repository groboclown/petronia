# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-06T22:34:13.803080

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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
            'name': 'ʇʍʉͶƏǨп\x94ȇč§Ƀөʛēˏ˫ɻșҖūǰƢɍĪ9шĉǶԎ',
            'minimum_version': [
                -3454367222471429626,
                -1398437910469891417,
                -2370294184207791830,
            ],
            'below_version': [
                6773122987217829543,
                -2574429513344043830,
                4346874863868713669,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

        },
    ),
]


class ArgumentsTest(unittest.TestCase):
    """
    Tests for Arguments
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ARGUMENTS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Arguments.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in ARGUMENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Arguments.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ARGUMENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [


]


ARGUMENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    (
        'string',
        {
            '^': 'string',
            '$': 'ȵʊάȂʕ%˵Ӱ˾bĞRżˮʭgѢ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 8222374868242766054,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 221193.0424387292,
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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
                dict(field_name='message', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='arguments', name='Error'),
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
            'identifier': 'ĪљƇϒ҇\x9fӱʑȮɔЙ\x83ʆσįЩ±ƕӚǷШӌǊоϋŹƜяĻԍ',
            'source': 'ÖЕśɵΒӸѫǫӰϝI˛ϼŒӅʨԤÑǼʹӢ˘ҍɹкGƉï\x93ѓ',
            'message': 'ʌΛʃʙôa˱љ´Ρƙöȍ˟ɬТʄЅҶǼχʰӶ\x82qp˻ϡϋж',
            'arguments': [
                {
                    '^': 'string',
                    '$': 'ƮϩѴ˖ɌEǟȿǒǑĬƖӼëϰӛɵōϩyťАĊΙϥҭɪȊЇç',
                },
                {
                    '^': 'string',
                    '$': 'ӻǬńàψtȾӫŹüëӫƑӶҠѯÃЖĿ½βͻđIчƪē҈Ѕģ',
                },
                {
                    '^': 'string',
                    '$': 'DĂƸӢƄʰĽ\u0381ƭΩ°Ǻɖӥ˭ԁǩԂљǺŕȪlΥūяϒʄFŌ',
                },
                {
                    '^': 'int',
                    '$': -7665868723430128542,
                },
                {
                    '^': 'float',
                    '$': -44484.71177269331,
                },
                {
                    '^': 'float',
                    '$': 658723.8040836856,
                },
                {
                    '^': 'int',
                    '$': -9069535465707894026,
                },
                {
                    '^': 'string',
                    '$': '\u0382\x99ϞͶy\u03a2˕ȕўd\x87ѸȒкʉ\x85ûÞӑԙĮƥɅӦҦ`ʋЊˀɽ',
                },
                {
                    '^': 'string',
                    '$': 'Βɺʾøġкʽ8»8ѴŚӄΩЄǺҺƊΧ҇РФТŲѴѠŰǜȺW',
                },
                {
                    '^': 'float',
                    '$': 622728.7006931315,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ĳ\x84',

            'message': '',

            'arguments': [
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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
            'name': '\x8cɦϦ\x94ŀѱĭÕԙɛȇÃ҅ŊŅ˃˚әı^ψ¤áȖ·ΣŜ\x86ˆϾ',
            'error': {
                'identifier': 'ɨėҝǶҬ΅²\u0381ǯƂқdɑҙŠˏӤӳœȫǽȤʽǺӳбŊқԮŻ',
                'source': '¸ʕF(Μ]ДˑӵȂƔЁğŹѭmϼϱƀδɤĻмȿΪǹԘτǏɋ',
                'message': 'Οά˔ѶǭȟƨΩӲWҵёԪҏòvĹəěŞĴʘȽ§τЪÞϞјһ',
                'arguments': [
                    {
                            '^': 'int',
                            '$': 6122536606486119578,
                        },
                    {
                            '^': 'int',
                            '$': -370241960692769831,
                        },
                    {
                            '^': 'float',
                            '$': 436090.299671617,
                        },
                    {
                            '^': 'int',
                            '$': 3907080012208389183,
                        },
                    {
                            '^': 'float',
                            '$': 158593.9916269423,
                        },
                    {
                            '^': 'string',
                            '$': 'ɴёƚýȱ\u038b˴ȓ½ĄԡʈpdʀǉİɪͻǛ˅ÃʽÂƲʴFѬȼÖ',
                        },
                    {
                            '^': 'float',
                            '$': 483047.6184546512,
                        },
                    {
                            '^': 'float',
                            '$': 345467.6116325226,
                        },
                    {
                            '^': 'int',
                            '$': -6207646959464529664,
                        },
                    {
                            '^': 'string',
                            '$': 'Ϩғ-ςʄҿ=ˎJŗԙƾ<ιφϢfw7ΊúѸǘԋŢƕԭтԧĝ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'error': {
                'identifier': 'Ѭr',
                'message': '',
                'arguments': [
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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
            'name': 'ØҖԂƌɭĀҡŁκЮχҳϔϐΛɁβ1cѺúѼ{Єԓи˪ʿ}Φ',
            'version': [
                -676009952653703153,
                7107073299121108418,
                8981710129187912907,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -7414763456603987324,
                -1247886846560216143,
                -7796960990313761903,
            ],

        },
    ),
]


class LoadedExtensionsTest(unittest.TestCase):
    """
    Tests for LoadedExtensions
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOADED_EXTENSIONS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadedExtensions.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LOADED_EXTENSIONS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadedExtensions.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOADED_EXTENSIONS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadedExtensions'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LoadedExtensions'),
            ),

        ),
    ),

]


LOADED_EXTENSIONS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ОԇӍÖʕѫ©ԫԠŦ$ϛӟѿοƂò˼RԤϤŊЀžīӍЊԥȇњ',
            'version': [
                -9218790390618950631,
                5871668151506293593,
                3092142454768662830,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -9203351855494126218,
                204883907530687390,
                -7489544700617361251,
            ],

        },
    ),
]


class SystemStartedEventTest(unittest.TestCase):
    """
    Tests for SystemStartedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SYSTEM_STARTED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.SystemStartedEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.SystemStartedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SYSTEM_STARTED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='loaded_extensions', name='SystemStartedEvent'),
            ),

        ),
    ),

]


SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'loaded_extensions': [
                {
                    'name': 'ĐʹӊèӭBŀ˴ĹϗӦÝɐɚ\x8cϬə\x9eVϝͳѮЧлǇɲтҘŝA',
                    'version': [
                            3454179226097488224,
                            -1052135958582241838,
                            3443724477113656361,
                        ],
                },
                {
                    'name': 'ɲп˜Ω\u0383ÑӆǰŨ҃Ѫ1FɿΩͲǃ',
                    'version': [
                            8689593767921240673,
                            -813116397432331254,
                            -1051357726566030192,
                        ],
                },
                {
                    'name': 'ЏĈÍЂԥԑǕνӖϣЦʕŜ«аǲĮɇʐζͻ\x85ɓ¶ҨȱZŮĥʗ',
                    'version': [
                            2556747915681682688,
                            4504905246432878341,
                            5153774155455570498,
                        ],
                },
                {
                    'name': 'ĞϧȡѸј®сʾãǕ\u0382ʅĊ΅ȕĂ¤]ɫ|ќÍмñƋԄŶV\u038dƚ',
                    'version': [
                            8351588306987350147,
                            5627563952413739356,
                            3244538172270986773,
                        ],
                },
                {
                    'name': '¯ȼŅːōΑӾЏɽ˭¥Ƽ¶6ŧ҇ˮϡǳҧǯЬŪ϶ϨŘӝлǍ ',
                    'version': [
                            -1632674521885933887,
                            4007448146770873522,
                            2372292369606455903,
                        ],
                },
                {
                    'name': "ѩГԚҗȣȒΒԮò'Wдǹ²R΄҆ĲʗƚɺľtеˀιǮǫȻ˸",
                    'version': [
                            5654432197730348533,
                            -8892375532523308206,
                            -3270369073903046489,
                        ],
                },
                {
                    'name': 'ʨӸϟԪӍ*ϩïˡӧƀɨ¯}\x8eͷȧɛȋӧћʀ~kìǊʝéпɁ',
                    'version': [
                            -890234578525121384,
                            2449361141240777808,
                            32561668799545102,
                        ],
                },
                {
                    'name': 'ȤʩԌΣ·ѕ҉êʛ\x93Ǚ˅ŐȪőɲľAѮUԓԬӻͻƧǌȆǲ+˳',
                    'version': [
                            5282221948506087183,
                            -6569991484950011658,
                            -1726999470261740926,
                        ],
                },
                {
                    'name': 'ɱʭXǇǄԗмΩæй¬ϨӃқźжʉвҸΪĔƇӈԉʶÊ~ĲĂҵ',
                    'version': [
                            139656324431885192,
                            -2314380661325160466,
                            437957631524454779,
                        ],
                },
                {
                    'name': 'ҫǟĮЫɑҬӡʾƨˌěΥ˺İĥѯξωȷUfЏОӞɳѩ³ȻԂ\u0378',
                    'version': [
                            8872000849922060111,
                            -1660155946569860268,
                            -2974352778922440624,
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'loaded_extensions': [
            ],

        },
    ),
]
