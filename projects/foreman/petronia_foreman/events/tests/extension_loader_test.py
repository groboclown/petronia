# GENERATED CODE - DO NOT MODIFY
# Created on 2020-11-19T23:28:00.692427

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

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
            'name': 'ȘµҹҰϣΒPȶ˟ýȈЙ˦¼ϧϪ˅Ŏ\xadƷҾɾȻƓѵ˸ʵЛδť',
            'minimum_version': [
                3669592679142415916,
                1098282265795310724,
                -1441859396520982088,
            ],
            'below_version': [
                8590075817579904393,
                -582714385814659141,
                -1583567990028462575,
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
            '$': 'СʝɅèλѻʉşɼ\x8b,ƠǘԂǆɇϟ˙Ļϭ\x92ĉǏŸПĹò=ʂµ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3856486042124200330,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 619784.5697276157,
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
            'identifier': '˼µЭ˃ҟɰƻӕΛƄ²ͳгŇKкÛԑŢ΄»ͱ\u0380ѷɔԅˡĤйˀ',
            'source': 'Ɗǵą\x9c҂Ґοƅˆǟҁ4ƕξɧјgЍӑǻˀņѺ¾˺ȎӓΤ ĝ',
            'message': "-ҁèѕЊ'ʢѪǤҥǺқĠƍįťϫƊŽƳɆϲФ&ƧҚѸˑɌq",
            'arguments': [
                {
                    '^': 'int',
                    '$': -5514487610252129372,
                },
                {
                    '^': 'string',
                    '$': '΅ȍBĽҁȶțMȍȍȾϛȔžÕѱѮǂӗұϔɡԑǚѹ$¹ǫŗă',
                },
                {
                    '^': 'float',
                    '$': 880232.7468012248,
                },
                {
                    '^': 'float',
                    '$': 696175.9543014616,
                },
                {
                    '^': 'string',
                    '$': 'ŊԚ\x93',
                },
                {
                    '^': 'int',
                    '$': 6043623350905086306,
                },
                {
                    '^': 'string',
                    '$': '\u038dӦ\x8cԆЮú˳ѮŬȴЁɯǷǙI\x8fˣˠАΞФƗ˝ҍӍ~ƻԝĺ¦',
                },
                {
                    '^': 'string',
                    '$': 'ҁá˓ҕƢȋ\x83о˭ėΖїóУǾ҆ɾŏ\x7fӬƨjӋŋΨϡԃӨɑĒ',
                },
                {
                    '^': 'float',
                    '$': 652540.1904311413,
                },
                {
                    '^': 'string',
                    '$': 'КҾĬӛχ\u0379ȪҎΌŘЉϳϦ²\x93ƅǚʓҗƥí8еѽҵɈ\x92҂ȥȅ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Ϋȣ',

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
            'name': '\u0379ҷʾҡ!fӡ\u038dȳʿԃѪʶ\x89όϩŗɾĂÛқ\x94щ0πȠșƽ6ԁ',
            'error': {
                'identifier': "ǆĽ\x9cəҦΤӢ'ӀλȱÃ¯ÇǲƐ˷мϒҬÇĜ½ĀɁѱ˙ȧːρ",
                'source': 'ŊŰͽùѩęԒɹò\x8fġȨʊΙȀλĚӴώƜyËãϺʝÚѣȒɰ',
                'message': 'ŭ»҆ˌïΛʠӗïӃѭԟ\u0381ȕǞˇҿ,ɞWӔәSǮ\x8a\u03a2#ѕƃː',
                'arguments': [
                    {
                            '^': 'float',
                            '$': 436415.7655721052,
                        },
                    {
                            '^': 'int',
                            '$': -7199901072284345752,
                        },
                    {
                            '^': 'string',
                            '$': 'ʜʿǹǃͻsѥƲιWҤÖΓΔΉЀс¾οԡϵҾӥƚʲӃˉԭÿι',
                        },
                    {
                            '^': 'float',
                            '$': 511908.86072570505,
                        },
                    {
                            '^': 'string',
                            '$': 'ǔǯӸӴɿӍϗҵҡġʈƮ\\ɣÊл\\ƱúɘҮ\u038dǛеǥ_ǊǴĻԍ',
                        },
                    {
                            '^': 'string',
                            '$': 'ӼӬѹјj¯:ĹĊӧș\x7fӣ¯]į¾ΜͰҽðɱȈСχΝӑǮҦϭ',
                        },
                    {
                            '^': 'string',
                            '$': 'ǋ˃ɡҀÌˀԋĻј˲\x82ĮͱřƙĮPĶʡʷӜӀӾǅΔɧˊŭӞɅ',
                        },
                    {
                            '^': 'float',
                            '$': 151309.98436488243,
                        },
                    {
                            '^': 'int',
                            '$': 7425396701831761342,
                        },
                    {
                            '^': 'string',
                            '$': 'ǵɬÈħӁ˳L˩ʢ¦ĉӳxʆҋę\x9cĠТĵѧŧέҠҡªӆДνФ',
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
                'identifier': '{Ӆ',
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
            'name': 'Ŀє˘ʚυЃΣеΕɼʂÿԇ®ɮ҇ǡөңşϮŨȌÌόƣʘ¢ÜѮ',
            'version': [
                -1594145504416924926,
                -5776792178785578478,
                5422011026342226264,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -6299809854072186451,
                -276235440341182577,
                2567573602564115569,
            ],

        },
    ),
]


class LauncherLoadExtensionEventTest(unittest.TestCase):
    """
    Tests for LauncherLoadExtensionEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_LOAD_EXTENSION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LauncherLoadExtensionEvent.parse_data(test_data)
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
        for test_name, test_data in LAUNCHER_LOAD_EXTENSION_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LauncherLoadExtensionEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_LOAD_EXTENSION_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherLoadExtensionEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LauncherLoadExtensionEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='LauncherLoadExtensionEvent'),
            ),

        ),
    ),
]


LAUNCHER_LOAD_EXTENSION_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ͲʻO<\x7fǖ˧фąĔ˪\x9cϒҏ\u0381_0ӤȔԑƧ\u0379ɂ˹ӹǾ\x88,Ҥԫ',
            'version': [
                5363464000885738826,
                -5787398476415900108,
                5060376947375141620,
            ],
            'location': 'ɕRԄËΫzĄʺ6iϡ÷ŰͱʒǮ\x8cґƤͰ˸ÿϙĠɴѤ\x91˸΄Ƃ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -1087172980318115509,
                -4619983351441961446,
                3699854622332734354,
            ],

            'location': '',

        },
    ),
]
