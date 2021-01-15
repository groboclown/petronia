# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-15T16:34:20.946154

"""
Tests for the extension_commands module.
Extension petronia.internal.extension_commands, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import extension_commands


class InternalLoadExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for InternalLoadExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in INTERNAL_LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionRequestEvent.parse_data(test_data)
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
        for test_name, test_data in INTERNAL_LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


INTERNAL_LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='InternalLoadExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='InternalLoadExtensionRequestEvent'),
            ),

        ),
    ),

]


INTERNAL_LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ʣÎҚ˸ҢжнĊǽLϬŞȩźčƇŧҞҪӟϣγьκўΝʅÈIś',
            'version': [
                7165476837476543237,
                -1012069748334419165,
                8957392099947349298,
            ],
            'configuration': '˒Ǥʨ²ĽӅʂʎ\x8băõÈϜţФņqɾύĕʱҵЬ;ФʒƬǩұȚ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -5277499401506623933,
                7284335794620897526,
                -6722225914444078649,
            ],

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
                res = extension_commands.Arguments.parse_data(test_data)
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
                res = extension_commands.Arguments.parse_data(test_data)
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
            '$': 'ҰʞČзӂƻ\x9cɭɅɂɥǰĤUƌРÒƟӡƟΜZƒЍĵöԙТƌƎ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 448430816850276263,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 967188.5022309138,
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
                res = extension_commands.Error.parse_data(test_data)
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
                res = extension_commands.Error.parse_data(test_data)
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
            'identifier': 'ʳɽşÂǧļҀȔƂǐ£˛˲Ύɹаӛ˥PěȊѯʮ=ʘȟȌÐԚċ',
            'source': 'ȶǫʞŴňù|Ԩˊ}RʪѱɌ΄Ӹ¯Ҵӻ°ÈƼϱчɩ˅ðфӴ9',
            'message': 'НԢĝ˝ʍɂĝΨͿ˅Ɔ˽Ϯҏ\x9fxӮʀ9μǵŀ˪ҌӫU\x8eënϝ',
            'arguments': [
                {
                    '^': 'int',
                    '$': 5786265306585346965,
                },
                {
                    '^': 'string',
                    '$': 'Ϯǰ˸ǕϝˍμʷʪƃəϺѧуԒҵĶïΣҹȟ˔ÚʢƟǬčɔεФ',
                },
                {
                    '^': 'string',
                    '$': '˳éѸƈÝÈĬһύѡϺϟǌǿ8˪ˁуȻΉĤņƃҎľš˓ΠƼԛ',
                },
                {
                    '^': 'int',
                    '$': 2276910971887220164,
                },
                {
                    '^': 'int',
                    '$': -935309565932072730,
                },
                {
                    '^': 'float',
                    '$': 6612.373635973927,
                },
                {
                    '^': 'float',
                    '$': 446452.04532722733,
                },
                {
                    '^': 'float',
                    '$': 136700.67689905924,
                },
                {
                    '^': 'string',
                    '$': 'YΦȮDʯɱ϶ǧԜȐΦϔ\x91ÙPѤI˗oĴƱĀʟǅŷΰȆӳŶʶ',
                },
                {
                    '^': 'float',
                    '$': 653098.493076503,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Åӑ',

            'message': '',

            'arguments': [
            ],

        },
    ),
]


class InternalLoadExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for InternalLoadExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in INTERNAL_LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionFailedEvent.parse_data(test_data)
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
        for test_name, test_data in INTERNAL_LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


INTERNAL_LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='InternalLoadExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='InternalLoadExtensionFailedEvent'),
            ),

        ),
    ),

]


INTERNAL_LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': ".Sêɯȧń/ʥӆЅϰúҖˏŜȋәÐΆғШȯԝԄԆǾ÷'ҿӘ",
            'error': {
                'identifier': 'Чȉ·ō\u0379AĔȤҕіȈ͵σƆŷǻĨпȽŖœʟÈѢȘ˞ӿ\u03a2ÆѬ',
                'source': 'ѷ%ŋϪšНԄǴɧȸ)åÐͳűˇ5ǎǎMѨǄ˷Ͳ˹ʢ`ЁԒŇ',
                'message': 'ҺȾʭƇˁ\x9eďƦȢǟ\x9bӓЎǊ\x97ŸƗӸǢφƭĽèďĊÚʨˋʵˈ',
                'arguments': [
                    {
                            '^': 'string',
                            '$': 'Λ5ǼśˊПғ°ѴĻñқ@ҫāīҿđҋӝӸȐăƬҶұΟƋϠȯ',
                        },
                    {
                            '^': 'int',
                            '$': -6794133561784910310,
                        },
                    {
                            '^': 'int',
                            '$': 2968424919968892153,
                        },
                    {
                            '^': 'float',
                            '$': 105465.34740199204,
                        },
                    {
                            '^': 'int',
                            '$': -4417018705924553338,
                        },
                    {
                            '^': 'string',
                            '$': '˕Ĥƅś҇ʼӫȣˍǼѭ\xa0¹Ȣ˵φīǏτȁǲɐƒĹңѥҎʞ\x91ҍ',
                        },
                    {
                            '^': 'float',
                            '$': 389567.9496350978,
                        },
                    {
                            '^': 'string',
                            '$': 'ЧӥΙκӋтȐϝÇ˄ÏǬȮǦİ¥',
                        },
                    {
                            '^': 'float',
                            '$': 486624.91446526756,
                        },
                    {
                            '^': 'string',
                            '$': 'ţϣıЎî)ƙНȼģ\x83ғӕӁΫЁ®ęЬ2ѽĘĭƫΘ҄ԘұiQ',
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
                'identifier': 'ҠΞ',
                'message': '',
                'arguments': [
                ],
            },

        },
    ),
]


class InternalLoadExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for InternalLoadExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in INTERNAL_LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionSuccessEvent.parse_data(test_data)
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
        for test_name, test_data in INTERNAL_LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


INTERNAL_LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='InternalLoadExtensionSuccessEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='InternalLoadExtensionSuccessEvent'),
            ),

        ),
    ),

]


INTERNAL_LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ЧԠϞȭг9ұˎԃΉț)\x8aʛηȈłëѹĲnӚԏzxǔɷʲ΅Ϟ',
            'version': [
                -5116319522329972481,
                -3751737163528608043,
                -7923711360333667544,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -8764309642214685221,
                -313075146857770663,
                4957136632819031002,
            ],

        },
    ),
]
