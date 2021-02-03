# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T18:04:40.563299

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
            'name': '\u0382ԥăҧцΑРҥԞƝrҒŚѲ˰OҺӟӳ҇ǜǂϢΝJͻ\x8eɘԕǟ',
            'minimum_version': [
                -5277949617443988317,
                -2384185920202972423,
                -1493209894716816897,
            ],
            'below_version': [
                -7652592385493842231,
                -654272605674740987,
                -4710410545007043408,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԒԋÒ',

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
            '$': 'ЎEηӜ˙ġĢƽÅҕӧԉͺϗĆӲ¶źЯзВĬțǁĄ®Ϥ\x8bʗǢ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -6093300197871880964,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 790451.2645341422,
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
            '$': '20210203:180440.502387:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2169764815927801894,
                8876010385329955947,
                4048212493063975751,
                4012901580659367384,
                4636236782008643678,
                -5774753355270310399,
                8273377827000368309,
                4294458664272466684,
                -4414640974054048863,
                4212788468288177835,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                185483.8418660923,
                602568.637632455,
                790276.4174647899,
                247237.01633482502,
                198450.6288682763,
                569393.3666662378,
                487300.8296102381,
                634912.4536222132,
                348982.124733549,
                869787.6117118276,
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
                True,
                False,
                True,
                True,
                False,
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
                '20210203:180440.503015:+0000',
                '20210203:180440.503025:+0000',
                '20210203:180440.503031:+0000',
                '20210203:180440.503036:+0000',
                '20210203:180440.503041:+0000',
                '20210203:180440.503046:+0000',
                '20210203:180440.503050:+0000',
                '20210203:180440.503055:+0000',
                '20210203:180440.503060:+0000',
                '20210203:180440.503064:+0000',
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
            'name': 'ąˢƳяɯËĀσƿĊɒԧ˖мŦɆ\x8b',
            'value': {
                '^': 'int_list',
                '$': [
                    2628028542823446592,
                    -8391044203839412842,
                    -3269517340806389036,
                    8542112130917386547,
                    -3414803827414394192,
                    -2488094209164830306,
                    -990878148033299713,
                    5175851616572564433,
                    2728646759402869838,
                    -5569316357423104684,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x8d',

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
            'catalog': 'Ψӹғĭ\x81cʳȲĜǨΠѱӽҙ˾ǻŠŢҶΒԋљĞϞĀĀӤm1˨',
            'message': '\x8dʘ\x88ώŀΥōПɨ.Ȕ϶УўУǉ\x8bҘb˹ԣОҹѸǊ\u0379ӚFТӚ',
            'arguments': [
                {
                    'name': 'Ć0ҲҢӍєɾʅЊƟϻ҅їǴʨДĆѻ\x9eѠʰӦȣҐũоê4Îé',
                    'value': {
                            '^': 'string',
                            '$': 'ЇЮÅӼE˦Һ\x8bϤɺʔĎƐͳ0я-ŠϦųʻʊǒůο@η˘ƣ:',
                        },
                },
                {
                    'name': 'Śʴȑӽ˹ΊǙȨΕʜ(LĽǼƄʪҵԢĬФȣГśҊǍЍʧWǍВ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210203:180440.499996:+0000',
                        },
                },
                {
                    'name': 'Çѩē˵ˇɵΤ˄ԧÚ«˫јψԓϥҒʜӣf×ЍɓЫXϬ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ѕсԪºƺų¢ȝдзԠɶΜàѡљτѿŞɤ˾Ϸ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '§ʹȓÖФɒ˽ʜϦ\x88ѫτΫκ\x8fћ¡ҍă',
                    'value': {
                            '^': 'int',
                            '$': -6493309150401466202,
                        },
                },
                {
                    'name': 'ʞ˯ӟӦБˬʽ%ȧӎɊ˲ГȹưɅӲ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210203:180440.500530:+0000',
                                        '20210203:180440.500539:+0000',
                                        '20210203:180440.500545:+0000',
                                        '20210203:180440.500549:+0000',
                                        '20210203:180440.500553:+0000',
                                        '20210203:180440.500558:+0000',
                                        '20210203:180440.500562:+0000',
                                        '20210203:180440.500566:+0000',
                                        '20210203:180440.500570:+0000',
                                        '20210203:180440.500575:+0000',
                                    ],
                        },
                },
                {
                    'name': '\x90ǮԞϖŰŚG&ǰȡϯΖΊƮśƘ\x94ɪśѲĊŜŴ)ˡįǗ¸',
                    'value': {
                            '^': 'float',
                            '$': 302747.90694928577,
                        },
                },
                {
                    'name': 'вʖĩǩīˑ²ԂɠǙɿӀ-ðΊӸͷƻѪƜ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210203:180440.501084:+0000',
                                        '20210203:180440.501099:+0000',
                                        '20210203:180440.501104:+0000',
                                        '20210203:180440.501109:+0000',
                                        '20210203:180440.501114:+0000',
                                        '20210203:180440.501118:+0000',
                                        '20210203:180440.501123:+0000',
                                        '20210203:180440.501127:+0000',
                                        '20210203:180440.501132:+0000',
                                        '20210203:180440.501140:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ƿԬҎÝҕè҈ɚùÂǔȕªӨϰңǯYѺ¿ɻ7¹ɪϡэȅНОЛ',
                    'value': {
                            '^': 'float',
                            '$': 797871.3918638363,
                        },
                },
                {
                    'name': 'ϾӢƳǊ´S\u0383ԚΚ\u0381śɳɽÈƩ"ӋƜɃкÞªʝʸTľ\x80Hǡ\'',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ԏϲ',

            'message': 'Ć',

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
                dict(field_name='error_message', name='Error'),
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
            'identifier': 'ԟϺǢφł|¿ӰǗӓҹĀƽVԣѮűŝЅԎԠщoŽŇ\x8dɦJƘo',
            'categories': [
                'configuration',
                'file',
                'os',
                'os',
                'network',
                'file',
                'internal',
                'os',
                'invalid-user-action',
                'os',
            ],
            'source': 'ˌÕɁ\x86ӍYƔWǶǔÑ˕\x92ţ˞#®Ě˂ч]Βο;»',
            'corrective_action': {
                'catalog': 'ήЗÂУËӽǚ9ɢɍÛʗЂ¯ӦϹύ;ͳП¶ƓƜѓ\xadÃΫęʡυ',
                'message': 'ɭˡʁ}ōђȸɪTɌѹӵЯɓχȋ˘Ȭ\x7f\x9dԄΏƃɻʐ\u0379ƑçΆɞ',
                'arguments': [
                    {
                            'name': 'Ƹēʧǁ˗ʟS4Ȱ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        8750047631343758282,
                                                        -8881991470378385554,
                                                        5129437112451417896,
                                                        -3014057492017800387,
                                                        7918849905250416753,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɷͰlSԨýυǧЅΪȃƏӰǄ˓hǣŃ˞ë0ǃȃ\x97˛ҰǛї§Ӝ',
                            'value': {
                                        '^': 'float',
                                        '$': 564547.3492335951,
                                    },
                        },
                    {
                            'name': 'ěɰ˘˖ëʸāӱԍœѴŧҧҵPɧĩͺԜĈšϱʦʻ˲ȵӡ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        174389.95564024895,
                                                        959703.3915986223,
                                                        -93976.84161753343,
                                                        297474.7116257956,
                                                        486791.7671886609,
                                                        7063.9790895022015,
                                                        749179.1950853122,
                                                        647132.7523491773,
                                                        685123.2335236163,
                                                        676309.1890067002,
                                                    ],
                                    },
                        },
                    {
                            'name': '*yЍѫʸЎͲƳҚҍȕŎюЎ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:180440.498120:+0000',
                                    },
                        },
                    {
                            'name': 'ŠҷβԈ¬ǲγҴ\x80ұˈϵΚɉƜ$˙ѾƙʸiĭҳX',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        279603.14210493374,
                                                        966550.2796855676,
                                                        388641.71505608544,
                                                        178254.3476593205,
                                                        231697.0522613437,
                                                        367570.364900956,
                                                        156791.05700261323,
                                                        824427.4528041034,
                                                        154240.7654801852,
                                                        356415.0420582281,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʄãѿгʝm',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'þҚԖԁĚ{Ή\x7fԒ˪ōƘŝӼ¢',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        722554.4006803136,
                                                        674088.2076802512,
                                                        9247.304971475678,
                                                        833784.6209223571,
                                                        512394.5060525858,
                                                        730349.6689949352,
                                                        168618.00379123806,
                                                        -74863.4288433649,
                                                        738475.0902581858,
                                                        904710.8655788735,
                                                    ],
                                    },
                        },
                    {
                            'name': 'γЕȱ¸ɯξԐȉǩҙ¨ĳðGǜѧ˃ƼˌԊ®Ò\u0383Ǆä',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '§xѬіԘȧ˖ś1ɇ}҉ҭûpЮÏԠԡ7Ȍ˛ǉ˓ҖҌFѬбǨ',
                                                        'Ҷкґĳ<ɛѤĿȣӷĘŴǶÔЧȉїÔĵȐ©ѕ˔ŖşӘǬ\x90Ѥǁ',
                                                        "˼nԝҤԟӒЭҍlѕшɄӴϠŢ2ȊP˖vÕ/'ːӑӿʵϥОυ",
                                                        'Ȏ΄ӅɍΑXɣ\x7fͼԜÿѵѠMeĵԞήҬӨԑėʁҟȀϞFƳԁƣ',
                                                        '\x9eȝ«¼ѮԎԆҘÃΜϤήɎӷŋćŐɠєrǵԗό\x95ЎхЊǝŶư',
                                                    ],
                                    },
                        },
                    {
                            'name': 'д˅ˤɸҔ^ȗǽβѧԋϴ˲φsKȠű˳ÌɠɧŦӣƌßεԭɂϼ',
                            'value': {
                                        '^': 'int',
                                        '$': 5181133071918390143,
                                    },
                        },
                    {
                            'name': '΄.ʝЗǸͱӵҪμ\x97Ę[',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:180440.499214:+0000',
                                                        '20210203:180440.499224:+0000',
                                                        '20210203:180440.499229:+0000',
                                                        '20210203:180440.499234:+0000',
                                                        '20210203:180440.499239:+0000',
                                                        '20210203:180440.499243:+0000',
                                                        '20210203:180440.499247:+0000',
                                                        '20210203:180440.499251:+0000',
                                                        '20210203:180440.499256:+0000',
                                                        '20210203:180440.499260:+0000',
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ӹʾ\x96Ѓƌ˻пҊȲˎҗäßqΣōԭӫöªŌԇŏưʻѽӐφˇІ',
                'message': 'ӝґԫҎĢ˻ʴƑȽʾˢ»ưʮξɥѸɘтȒȠϴӞŽǇϣÖŉϊŸ',
                'arguments': [
                    {
                            'name': 'řңµ?ŻöұɛĮʸәǭmÜȺƛɅňƃʠ{Ʋԃp\u03a2Σųɗòǀ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        313642.14591553895,
                                                        207731.52411630272,
                                                        674493.1597945212,
                                                        741446.2276987707,
                                                        620983.3000598851,
                                                        125769.42797577026,
                                                        67927.96799698306,
                                                        685617.2511895808,
                                                        421677.6064526834,
                                                        213380.31110631133,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƷǟɸȼѫȜӁԃƳӤк\x8aĝѽҨӣΗόjƹѭÇϞ,˄˯ɬţaҗ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:180440.503550:+0000',
                                    },
                        },
                    {
                            'name': 'ҵ¤^ԩԎņˁǥԩŎͽí;ƚвСÒɨʿȧ!ǕƼӂé\x87ϛ\x94ϏӼ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ÜĀэΖ\u0383?ɧŨӁ\x99ƤʊϙŅ҃ӗ˭äɮʊāíǖxȓ!øǨϰʰ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Сɇԥ\x94ԧ»əéʭ.ȘėǂƪƁƌнԜʼϲ;ʀӷІÝьǔϓ¢O',
                            'value': {
                                        '^': 'string',
                                        '$': 'ԋЃʳ®ˤ!ͻϨԃφǤԩȇϲɂŰΧÊѱ¤ʘͰɼͿТā6\x9fϣy',
                                    },
                        },
                    {
                            'name': 'ѧƓǳĥĵƝǽKҢѫy°˂ӭ?ƅԏƧχȟǹ¸ΡȤΧԧԗPʴʁ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ѩ4ӿ\x91ΉΛqϛŃѕ˱Ώˑ˨ƻЈҙӁѢӔΖЅɃʇȄԞӉ\x83Ӯƹ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        292139.98895715375,
                                                        685270.7911848553,
                                                        722166.8553674605,
                                                        143056.4613602911,
                                                        23417.92273446075,
                                                        627073.4290330306,
                                                        559152.9444578431,
                                                        143067.0445710857,
                                                        2141.7220492897613,
                                                        394302.39021200413,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʯЬÍΑȰźԬȀ˘đͱҵȁΗЈɜǻƖʻӇǆ˂ɽŭȮĝIчǃԟ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ˋНŅ¡ЭӬϗbSʐÏЭԄſśƀ\u0380ǯʞɉӼ1ʏƟΚĬƳŕԫ½',
                                    },
                        },
                    {
                            'name': "Ѥ¶ԊХƦӹ˕'ʅϮЬ¾çǢӈ®œɦɗˮȓ˱ɡхСçξӄ҆Ц",
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': '\x85ӸӐ\x84ʬ¢Ɩ\u038bԍί°ΔϟѼЯŶAɘȺÝ×ӉǖӘƪԚɡ˧ԤӸ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -454986902389951601,
                                                        -7329199450754740967,
                                                        -1881632169011352123,
                                                        -8004474689827929161,
                                                        -1231255835862425137,
                                                        605761809192736528,
                                                        1582585684089672503,
                                                        -3753877762937347874,
                                                        7048621119427895028,
                                                        3166655259848096798,
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

            'identifier': 'ыƝѤҾƭ',

            'categories': [
                'access-restriction',
            ],

            'error_message': {
                'catalog': 'ō˻',
                'message': 'ä',
            },

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
            'name': 'ʄАZLS¥ĕϥɪуоþǃԕϒƺϵȽʚ\x9cРżǕ·ȚΞ²ƶЕ\x9d',
            'error': {
                'identifier': 'Бƅȋҵ˞ˏ\x95Ί¨7\x81°ƝѨʚРǤ˓ŉњǩӠəpхԞĸΰȪI',
                'categories': [
                    'os',
                    'invalid-user-action',
                    'network',
                    'os',
                    'access-restriction',
                    'network',
                    'internal',
                    'internal',
                    'network',
                    'invalid-user-action',
                ],
                'source': 'ú3\x80þӘӃϞê҈ЎȓɝĀɯÁҷɢҨ[ïΖԛнпÉθŘĭͼ&',
                'corrective_action': {
                    'catalog': 'ӌѝ˔ԃùȃĘҏρԐҺӡзmњʩáɬ÷яͼӟ,яɹҘ8ʺȗљ',
                    'message': 'ɍƝǿѥʍτ\x9ałʣĸщÿūЭưԖƯõ;ВлŁƥӾΗƄÀʄǖΔ',
                    'arguments': [
                            {
                                        'name': 'ŢİӨԪҀʳԀҁȜĂˬùĄă',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            520986.6611463092,
                                                                            974222.941809705,
                                                                            721001.61758523,
                                                                            565467.361604653,
                                                                            420680.8177850478,
                                                                            -48016.82869662797,
                                                                            844854.4595180075,
                                                                            25110.930905697547,
                                                                            805323.6618823087,
                                                                            696507.7832369396,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȃʼϚǐSĚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԥȶāǺӾƺӭŵӯѨМǌǦԇʰȇʃ͵/ӰЧПԮΕ¾ҫʼɾİɯ',
                                                    },
                                    },
                            {
                                        'name': 'ҙļƣ0ȭɽҝϭĈѻӓћϺĢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5861661489880338253,
                                                    },
                                    },
                            {
                                        'name': '²˘ȥQÐȒӬϝŗϛȸÁҠHȩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'гѧϝǨǔΤк΄Ϛ\u0383ǩԦȋϒ˨ȫͽˎѩЊȫóĂȹѫǑȻɽƄт',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180440.494147:+0000',
                                                                            '20210203:180440.494169:+0000',
                                                                            '20210203:180440.494176:+0000',
                                                                            '20210203:180440.494181:+0000',
                                                                            '20210203:180440.494186:+0000',
                                                                            '20210203:180440.494191:+0000',
                                                                            '20210203:180440.494195:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϖɰͻ4Ϋ¸¿ϸӬ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'źҒƄíuŭĐƶəʲƏɊԨԨìkСęȗĔŏˌϨѲƇғʹ˹ʲІ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            883537.2001162939,
                                                                            447114.2768205125,
                                                                            968427.4731882506,
                                                                            276169.9334888608,
                                                                            876732.7569691888,
                                                                            -44532.891437050435,
                                                                            655008.0904796767,
                                                                            158253.53513619673,
                                                                            -34062.71192471337,
                                                                            121543.10727713112,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɆŎԐΕҢӺҢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180440.494997:+0000',
                                                                            '20210203:180440.495010:+0000',
                                                                            '20210203:180440.495017:+0000',
                                                                            '20210203:180440.495023:+0000',
                                                                            '20210203:180440.495029:+0000',
                                                                            '20210203:180440.495034:+0000',
                                                                            '20210203:180440.495040:+0000',
                                                                            '20210203:180440.495045:+0000',
                                                                            '20210203:180440.495050:+0000',
                                                                            '20210203:180440.495055:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ўʿ(ˋԧűɃļƋӖρ}ұԛͲǍˎƄҌσǂԎιæμɑӱɬɀҞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3753606881744194733,
                                                                            -5740243396155657091,
                                                                            -6068934341973199443,
                                                                            4458204983963138971,
                                                                            -8623726557983010137,
                                                                            -2166673625069639940,
                                                                            3359889460700940132,
                                                                            6668991941120797294,
                                                                            -6211199782140555449,
                                                                            -7248729443553825820,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˓ǒ¯ӠѮȕȢśƂԌѡ˒Ǫũ¾Њя˩ѳȩĶΘ˄Ҵ+іȍʔʊЈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ơċ^Ȅɽr\x8c\x85Ӥψ˫Ү!ÞɮƠƏʷƆĭπЦȄȻЭʊ\x89ͼƤ\x84',
                    'message': 'ǙӐ˓ЇˢͻҫʝчƩә˒üȲɋΕʾƫŒϩџč;Ös·ГƜWV',
                    'arguments': [
                            {
                                        'name': 'ǠřЍƀĿƫƩς\x87ǋ¶Ž\xa0ϔŧǕƟƠҷыȏȐʻɐϢѦϹſѼɿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8904904626787556024,
                                                                            7963001483106830625,
                                                                            3278465396613075181,
                                                                            -6171324471155959176,
                                                                            -300048137769829582,
                                                                            -4816395422991704797,
                                                                            3040332150370108809,
                                                                            7208572555855937495,
                                                                            8268874258424692485,
                                                                            -307304875081066434,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɚӂǧӷɠҦʭǷџҢèŕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƢƜäҧҿïҍô',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180440.496450:+0000',
                                                                            '20210203:180440.496464:+0000',
                                                                            '20210203:180440.496471:+0000',
                                                                            '20210203:180440.496476:+0000',
                                                                            '20210203:180440.496481:+0000',
                                                                            '20210203:180440.496486:+0000',
                                                                            '20210203:180440.496490:+0000',
                                                                            '20210203:180440.496495:+0000',
                                                                            '20210203:180440.496500:+0000',
                                                                            '20210203:180440.496505:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ÆЏˠ',

            'error': {
                'identifier': 'żʯǕт˜',
                'categories': [
                    'network',
                ],
                'error_message': {
                    'catalog': 'Ћʿ',
                    'message': '˪',
                },
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
            'name': 'ǌɶˏǭ˜˽ƮӻҞʃϩΞԇ\x81џњǖtœ¡ɞ7jсʾͼ˽ȍîͶ',
            'version': [
                -3576652184847922025,
                -3611008130868497010,
                -9031921699744087378,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӋȔŵ',

            'version': [
                -4609095154281845573,
                -6060558453530705698,
                -5419783631353566447,
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
            'event_id': 'ԖȹȻ\x8dŁɐȄʹɴȄæήčqƁĊǘϳǦԈŰĤçȸʳǱԃӋ\\ԛ',
            'target_id': '#kBʇƟƺȝѪǧʽb\x93ҝϯAэ\u0382ƨњəĬϯăÈˠʭʒȜɂì',
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
                    'event_id': 'κўяхԣӝԇԂʇɟЯѮȗϻӕ˷гŴ_ԣǔюʍšΤc[ûǣK',
                    'target_id': '±Çч\x94қȈĐӊȃҙŪȌ\u0383˥ӟϴғЛɬȼƂO\x86ҍ`ŵɫȁ}ã',
                },
                {
                    'event_id': '»ǽΉӚɏԙҍӆĕλԞеŧǴɍŨқƙҥɛԋ=ȴʚӢǂɞɅπѫ',
                    'target_id': 'ӮĔȥǑҒЩĮœǙӽɞǝʚ˟˷Ό$УŵĸǂȀˏчɇåÅӜԙǻ',
                },
                {
                    'event_id': 'ԤҗȬɬȸѨ˖ԇ\x8bӆʢϮǙϙĞм˔Dőǣʑƭҧi\x8a҇ǽϜ¤Ȑ',
                    'target_id': 'ÿӇϚӅȽɶД®\x81˪Ҿϼў¹0¯˚щѣξɴћøFǇΨwǉгȌ',
                },
                {
                    'event_id': 'ʖˀӣºʠ×ħюô҂ʉēɠҔǫƤ҇ƧЍÀˣϮ\xa0ȕИÐȿȮťǡ',
                    'target_id': 'ϖӨȥșзßʾ%ХϸǃɣŷǬŘӇǏϓŘȽŏĕǖǖԭϪΛйҵ¬',
                },
                {
                    'event_id': 'ĬҐăЧҟпƱͽПϺɫѪӷ\u0383υ˘ʢϠʾȍˉзцgьӕѹą\x9dȹ',
                    'target_id': 'ӵʔöӪѶÁҔӊ®ěöʃĊ]ό˫ƙѩɢӇԞȷʻɴΫLόƿțʇ',
                },
                {
                    'event_id': 'ÈcɞrĘÄ҇ϼɧςɞ\x9aͺĎоǭЕĪȷӛ£ȷͺȑҴșɑίΨɣ',
                    'target_id': 'ыі¯˩ȼpʲˋӪɲðѺɓ\u038b¡˥vŅЦűϤӳԞͽÔĕXF˒Å',
                },
                {
                    'event_id': 'ӉØτϔːɁĮ\u0378ȁӤ\x9eȧĉƟȘƂ"âƐQƻěǏĕŕŧ¨ӯзǡ',
                    'target_id': '\x99ǸΔЏˉҁʦΉӑю»ϻѠ҂£ͼМˌmӟѶǑӓοȘϗĩ˼Ƒā',
                },
                {
                    'event_id': 'ʇ"ΥĀŧƼʸ>ѱҪ(ъ4ãɥӅоƳѢӺ˕ҐӫɪƫʓϟʞДƹ',
                    'target_id': '×Ǒƌ˟ŊЧ¨ȿÜКԫʘҶ˞ɦŭǧӻʞɜϗѻ\x8fˆɻϩ\x89Ґfǂ',
                },
                {
                    'event_id': 'ЃϋԐǏŌǷǯǅƤӒ\x9a\x93\x87˪ˌυ\u0380ʰχhϿɱҫȣ)Țӣė)Ԗ',
                    'target_id': 'í˾Ѧň˭eŏӾæ/ϦԌдăůϹȅүнӨԭԕѯɣˌ~Ģ˸ΪÀ',
                },
                {
                    'event_id': '¢¢ǜçńТӌͱ˦ЍɃ˷Ƌ\x8cƺĝƳˣʝǍǮģӞã˼ӄnÑŔɹ',
                    'target_id': 'ґȻʍŘōēӤĥŰϛԐƠȱҡӍļӧȀϽКkőϘ¹ȩ\x82Ĩ˨ο\u0378',
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
                    'event_id': 'ɁǇ˂ȃ\x9cȇļü}Ƣɗ×ɦƷĩоǑƓќϰŪԉʷĬϯōӝë,ǒ',
                    'target_id': 'ωԡɫӆһЈʰɆЇʻʳáR¿ġɪсê˒ёœ³Ϸǲǐ·ɹӯ$ŕ',
                },
                {
                    'event_id': 'ΗʃԬƶ½ŰәǒʷΣӧʡͼƹΰѼ҇ίʖҌυӒǵ˜mҮȞɭɹƲ',
                    'target_id': 'гԝΫϲAξ(ˣϞĴāϴ´áĿГŔҗʔˮŤηϷ\x9e˶\x91ϚœVј',
                },
                {
                    'event_id': 'ҍɍѿƗľƋююӊ÷ŐňƇŒʦЗˈӻʄ˷Jʥ6ʮǅwÂϸ҅Ĺ',
                    'target_id': 'ɲêЖΫҍѦƅвɘʈʊʨ8ʔΐʪԠɬǕǗÐņʭɛa\x7f˕ɔ¾Ͻ',
                },
                {
                    'event_id': 'ζϭ\x9bɩë\x8dΒβԏɡԮϯĔĞ¸ŭэÍčˈʹʛҼϲƋԕyȎ˕β',
                    'target_id': 'ĝ?ř²Aǧ|вҁηʕԚɬ҆\\ĒѱӀґӧКƓԃɠ~Ίȼ©ťš',
                },
                {
                    'event_id': 'Ȑ(Ãӓ;QŊƂ҅ßӜʣÚvʝūoğʵ{өԨŠӪΨŭɱȗςÑ',
                    'target_id': '·ʁĶȟɧϗǾųÍҀ*şǜ˷ђȩ¦ϮϼїȊ˸ǋѵȐѸCѤ˗e',
                },
                {
                    'event_id': 'чʣĄƊòӮϹ\x94ѾҞ£ѡɪǙˊүūǩ˸ŕɅѠȐǂƶԛҖíɨƔ',
                    'target_id': 'Ҫ¨ϊȂǏÑҙΝ҂ǡM\x86ɰї\x8dϔΨɋ)(ƿиҫЧϜǳѥŀԡУ',
                },
                {
                    'event_id': 'òɜϒэϷ˙њĶKύœΰҨ˰ɖyʼ҇Ĥѓ˴ó&ΕӷĽӾǥ¨ӊ',
                    'target_id': 'ϋÂˏҐȴ\x81ňĂ҃ӇԋŷͻǙƿԦҢшЫǅѼӡɦĦφöčӭѱß',
                },
                {
                    'event_id': '˼ŇђõξҞӊȬŽϪӒ\x98ңïѤӍϋИƌɔɒˢǣ:˞ҋʲȠ˳ϲ',
                    'target_id': 'Џќ^ÊȴƓʱөňʇ\x8aψӍHĻԣ¸ĸĵӼƫӺʗҳØŤȉŅ/ϡ',
                },
                {
                    'event_id': 'vҕѰ˅ʙĶǔȶ\x9aˊǤЎԚÄʓΡѠ˜ǼҔ΅~˛Ӊ,Ȩ:ʇ%Γ',
                    'target_id': 'Ƃҿ2ϰԢȨӂѐίϢϾâǔƕ˘ɆыˡѺNɾмǢɬѤŔŜ£ȏԣ',
                },
                {
                    'event_id': 'ƥƑűѿΟɿȾҊŦǢӖȑôʅĤőÎƸɒϛĆ¿ΝͺȌҧ_ɼ Τ',
                    'target_id': 'íӉɎ\xa0ӣϗϜʛȈ\u0383tӇʀϗζŜΆЮȆɱӖνTѫZɦˌζĜǘ',
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
            'name': 'Ěԇ£Ϟɯϋɂɳ΄ýƮþЄȫɟԀӂǆǻ`ԁĝԔ\x89ԪȟŝԒʣî',
            'version': [
                -4704319463558299434,
                -4696137091814892685,
                -5119174162931668011,
            ],
            'about': "ΎɲΆĳˑ˔ϟȕǢ\u0382ТˉӂˉяʵҰɺ'Ôԩş˻-˸ԙЮÅȂȖ",
            'description': 'ͱϭӁ\x9cƕʵĹǷɏʜъʪǞЯƏǖēą\x8fÖͻҗтѤĎ\x9fѫЊ(ӆ',
            'authors': [
                'ԕϞДʒïԢöhņȌʞ¾ʠƃʬ\x8fƴҁŔӅͽȿĂŰ˔ǨǺ\x86ƩĬ',
                'ýҏƓÝӆҿˣĕ ǿęҮκɒҪӘҕɮĀƯCg˅ͺŷɦЌɳ\x97Φ',
                'ǪʌϟγĐȲͳ?sƢӾƟȲǈĭĵƝħÑĐ|vѫƑǁȞ½ЎȶĂ',
                'ԬӣŀıҘИǯч˗Êǯǡ)ќѯìʂξ[Ћ˗ύĆ˵Ơ§ά˾ŌǮ',
                'Ðєϊ˖\u038dǵͼ3ԏΙǐĿȖůŨƄԥȋħūØԈԍƊǂҕ˚ǺͲT',
                'ϗÇɛ˥˹ǁϚнĤCщЃ҉ĴƚƴҿХ',
                'ıǾʯʴΉżǐˉƓ\u0379˥ӎ\xa0ˊ/ӌǥ\x87ΓǿǨϾЗԡʼa\x9eȱċќ',
                'ƾ>ǱǤź҈Ǆ˙uϘdλԥôҵɞʳȉЇ˰Ǐџӭν"ϡϩӢţȶ',
                'Y\x8d³ÙҾӐЫѨǢңŐŸāĚ˱ŷζǼϠįҡІħԧϿӣǃМəǫ',
                'ŝW\x89Dąԏň;˸ǳϰСҁǛԔċÝË˵ĻȶǖÁВ®ҕ˘ӎˑƺ',
            ],
            'licenses': [
                '\x8eҰXĹÌāΓӘȡӯƬӘ˻Ҏɓ˦ҮŭιϙǎϺ7ɘ\\ęяʐΣ΅',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӒЮd',

            'version': [
                -4567458634021673231,
                -1074850200249488198,
                -1057979488931509087,
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
                    'name': 'ɂȅΥűöÆǻϓёΝѤe˹ϕԫǂÛƕǄĸӜIπÞ´ў΄ԦԚБ',
                    'version': [
                            -8853347740307334701,
                            -2780099049273130878,
                            -1555990823150104154,
                        ],
                    'about': 'Ӊ\u0379êχŚƗҋ+ìǰøţƒɞӿЧԩȊɤĮбʥȍАaǧÖЦŗЕ',
                    'description': 'ƊҼʦҼΒδvҐӎϓФoĜ˻ҼΙNĜ˻\x87ҬӮǌɀΓӆļTӧĆ',
                    'authors': [
                            'ұ˄҅ӞϬŊ˄φĖǙɛԤŴҷŐɀƐ\x8f¬ ɼʪÄѿӿӢκʟƾċ',
                            'ãҸ\u0383ΦψιοǁΘԌ˃иČʋíǌ;˶iƝшΉ½\u0383͵ëϋɐĀf',
                            'ӾӠԜÆ(ƕҊƋΏЋǞɎȃԩβǆĊͺˠ˒\xa0ҥġΥȏǦKǖċП',
                            'GьəǻĹȤήLɄǵĕªˏųѵ§ɔʨ˃ÇӫɪƶѕǏɋӇɠЃβ',
                            'Ą+ӈЄÁЊԮǣѺ˗\x83\xadɃɺĪӡVяŹŒΪˏˇˎӕʞʙЊƖŷ',
                            'ʙʰ¡¨ЊŻǢIԄ\x9cʞϿêζ\u0380Ԍҥ¸jȰˈǝӉӞͷϠˡȓхԍ',
                            'ӎǼЗʹѯԖ\x99ƱˢѼʪ\xa0лɛοǿÄɨŢYѧˌџЦţȧғԜҽ\x9d',
                            '˄Ԣáɯ;ª\x9fΒ¬ѥɰЅҁȵǏΩ¢υϑΙȔҝъ8ѠϰJΗԎǱ',
                            'ǲЩԖҹɂśѦƶѯ|ͻƥǿ-ˢ¡аˊ÷ĦǨԨҦǐi\x99ţ҉аΥ',
                            'ɯǢ¦üбŋҹҊˊº\x88ʐ',
                        ],
                    'licenses': [
                            'ƻŰ»ʾˊήҁдƢŲˈĲʆũҒЏϗOȴŘђǘ҈ɡ\x96ȲЖϿơ½',
                            'ȂʣĄl§Ā\x9fζȕIʩ҅Ƨ˓żÖΒ;ѭϛɢÅğʶШӳђơtŒ',
                            'ɠӁύʓ\u038bŧ®Ō˲ƨʷnª¹\x7fϰʈӵУʏŴϝȈôϺЋҨʡɠŜ',
                            'Ґ\u0383ǞǰԭŹĺbӽԭŝѠɗώΠСϷʛˇɌƄɼo˴~˗ъǲ˅р',
                            '>Ϝ\x8a҆ɹчʁԓpŁǑϧŶʝȲ"êĺɒүҐҊŐƸɦ˽ƇҀҠö',
                            'ҾŸðЄǦŦӺȎŔɿқˏÞ\x94ҴĳәʡΖŷұˮ˞ο6|ư¨əĵ',
                        ],
                },
                {
                    'name': '%иťƂ-ɔʅ7ʡ˯ʄӚЊʊτ×ǮËƀχіEƿϕ˩ŐȹƖ)ͼ',
                    'version': [
                            -1885121885660564574,
                            -29210742604307100,
                            -3189219635772398901,
                        ],
                    'about': 'ĺɡˢѧȮ!Ӻ\x8bʫԑȄͷǚŌҋĉˬҎ}ζ¤ȜŐϣǉĂŖӍӅƏ',
                    'description': 'ѴhĲġσΦÔҫԓҜɌĞɳ×ʺœΊϖԙЗʫâʱӱ\\ȆƝňįө',
                    'authors': [
                            'ŷŁӮϳ\x9f\x80žĪзӥЫ\x88҃҈ԃȬΈ\u0381´ʱӌҧɋȯµ\x80Ì˰Ưʫ',
                            'Ýӊƴѝƕ҄Ʈѹʀ\u0382Ѩž\u0383ŎӢĶű[Ϭu˵àξ~Ғɗʵʪԋ˖',
                            'ΡƂΓΪРɑѸuϠӻφɥČʴŁΕsÉГйgϪʗЅēƂÉƚ}ʵ',
                            'ƹțьѰ\x90ВԇΛ˘ĜˆмɼʸǼ|ÊóҶĤ\x9bP§ϨɌ\x98}ˀÕ˒',
                            "м'Ȱ\x90ϸѵѰȕ\x93҇uжėþЏңŅGҙԮѹͱȻʺиκǥ˱Hј",
                            'ӌʚʄ˹ƍԮʝǃҾѵşçӥ<ϐыʖŉʧǇĔ§ʜСŵҁϷԑƱƛ',
                            '\x9cĄ˰Ǆԁç®ŎʋˡǟӸԊʪҫšđȵđʹ\x8c÷ԁΒԭÛϦѾчˈ',
                            'ŅțУƅċˈϷàEɹƵϽҘʍX˖ʈŖҩʽǍЏ\x89)ΚŲ˜ϫʕÔ',
                            'ӺӾƛƚ=ɕɰѸбƵтҀʳȨϣιɳϹɡϨЬƐĝҋɔƆьƈΫӯ',
                            'ċыӎčҔćŐѰ7ΡƉѳŬΉ',
                        ],
                    'licenses': [
                            'ͳˍLE{!ϸǎċИêˤˡѪҿȚőůϜhÆɖǿǌȦЕϖǖ¤¾',
                        ],
                },
                {
                    'name': 'ρŗ\x95ĸҴƘ˝ΞAЃțǖ˽ԫѵßǟƦǑĲĀʹɔϧ˚(ŧȴЖб',
                    'version': [
                            -623176571225408551,
                            -3557785787662181657,
                            -2673274116631793471,
                        ],
                    'about': 'ΡjΧҕƙHӁƮȡøŤͿӱϹê\x81ǒϺӡɷΔ˺ӂ\u0378ԄҊΣЮѧ˔',
                    'description': 'ɬƇǈŉěŭѱӘóņӚΧαӑвƕƞŪ\x80uˋşκņɕҠɰʞ;Ɛ',
                    'authors': [
                            'ҊGW\x83РƅСʟ{ΑӑӳȹϋжŸ\x91ºġƘbυȣςʙÒĮνzШ',
                            'ȝƥe˃˻ѰmƥĎQ˲ɮƃȚƝΠŌΕj˃νԉԅӑӐЏѴлʧʕ',
                            '˘Ӝ.ĳǳЈƼɸȉЈԓĭɃĤҼǚǪÆ\x7fДӮíôҽɩƨ\x9fƆÆ\u0382',
                            'ƌǮɵɦČɧɀĺŀ\u03a2ȏɈŀƟЫ³ИԚԖҩӱ#ΖƮӺǡſǖ ĺ',
                            'ĿπӍ\x80Ϋ7ġȯɚȑӆǡҳɺƇӚϤˍ˘EƳΫPϜȷƗ"ЮЍ\x9d',
                            'ԅϧυɨ\x88˫ӞÙǶɠǁϩİǊԏЉԇΡ˙ѴԒԎzԜϪҔҔЦҌÍ',
                        ],
                    'licenses': [
                            'Ƃ˙ȈΏӃ\x85ԑΊOҜӜǉϵoǰÿǴėȅΘҢę9ѷϹɸiŮˊĎ',
                            'ϿѮÄƙˡĒȉx˚ϞžƲʰ\x95ώċǊǣȸŪŰѮ\x9c\x84ѼѬ´\u0380ŖŃ',
                            'ʦ˪ǪkřʗӤɇȖ1˃û\x94Ɂ\x8eѣ\x99ƕǗϗӋͲ҄ϨÛҵȸϩ¹É',
                            'ħǒʓϨбΏ\x8bʘҲӮϭÑȡâЭŋæʶɷˀЯюͿʼԊǘʗɾˇƟ',
                        ],
                },
                {
                    'name': "ȺqŎǍɘ1˚ȻЬђѨʿǥʱʛїԞĲɵ'¸ҺγČ˴ѤcώʣŨ",
                    'version': [
                            -8412572311790768217,
                            -7594535258593897478,
                            -4320743736001358532,
                        ],
                    'about': 'ǋ±[\x9a˄ɭΈȁĞǀ˕ķȮϩ˚ͼ¸\x8cЌǝлѤɬϻ£ɂôXɞѣ',
                    'description': 'ĮҾ˖υ×сǑǁϸҲϮǭĚǕǽґƻǤϴʢ˗ϳЁͼGԜҍˏĉÔ',
                    'authors': [
                            'ѤʫŮ҈ѐυӋҖɬӦǘġ҇JȕʲθȷіԂʋÍĘ\u0383mρј\x8dǍ҂',
                            'ѱAΰ}/\x9eƙЕ˪HʷúȤɾϬ\x98²҃ʁџοϺZӦƠҍϐʨӌȪ',
                            'čȷйϢγʿźʸ¾ϥŰʒȓԑǮʆЪΨԅǤ˲šԓϱʘ}˔',
                            'ΦÜӤǴÉªñʝǙА\u03a2кζσϗΆԁӆƶɜɚЀę\xadʮºыϖõτ',
                            'ʵѮŵԞµÀɞɉыƑ¨ΒʿѿʗӣҞžѷҋAɷЃεˣ˨ҡλиƏ',
                            'ȐӨ¤ƹΩƳź~еъbҕĺȭϼϗƃɁÉƻkʘōŏͿүÒǋ˅Ϻ',
                            'ӿʤkѠ҄ȊʿԎ¡јύ\x9aȝӸΟ9˺þd\x99Ҕ9(ΞцEɸԀɴa',
                            'ѯzdɮԌƁ1ÅΨŭŦʟǀŻĿÃƦĵ\x81¡qϏГԁɗǇʑɞĽʿ',
                            'ǲϤ3ɞȅŔбѨϡĲɲtĲīͳϑɦǞȥ\u0382úʿΤɾ}Ԋҟǧȶҙ',
                            'ДİfǢȉхΤ£σ\\ӠҒƱ˧þƳΠNљŐ\u0383ɈɗҺ\x96YΒɕԜč',
                        ],
                    'licenses': [
                            'ĜԗĘǒę˔ϩ˗ΰϳěХĂɕԙҚίϪʇơˇ΅\u0381СҁɷC˝ӝς',
                            'Ǧʠɾǣ˸·ãŏːϜǧò½цğδѨЦŚзэ·ƧǪȽԥԛэÂS',
                            'êʧƹʍʏƛɸ˦ӧӞ΅lϮęΠIԆȤľÁҢƉ¶ǒŽγԟʿXџ',
                            'ÉħĽϢıšŚϸÉҗȟżwėӌ\x9f\x90jʆɒʲӌϝҿӜАшȕʌˇ',
                        ],
                },
                {
                    'name': '˝˗ϧѠӾöʬżԗȗȿʕѝ҂ĘʬʩǴśѲͺɨ˳ϲԌɕѣȈ\x8eӣ',
                    'version': [
                            -6015603231083862357,
                            -3392699719437633998,
                            -7685028725857474523,
                        ],
                    'about': ' ӼЙȯƣэǵх;ɏǁ°F',
                    'description': 'ΣҥöҮĸʦƕǮ˦РĶɸӜĪ˃ɞʄÈǫú·Җεů\x8dȤɣ°Ğԑ',
                    'authors': [
                            '7ӋƦҕԠӞź\x9eҖϧ\x82мɾ=ǧƢАӴԗһҙБʥӓԁьʈѬˈē',
                            'εĘKVτȑѹƶӓģëҨŬҟÃʼǈĞǨеϷѾưˤҭˇҢ\xa0Š³',
                            'ďǵðήщÁēЧϙʆJɺ×ȵԣȑϩEĉȸƁҴΛƗÓЕԧʜĳǥ',
                            'ȮΤԦƓӝƈΐWѧņđȗũśϟ˥ŊЂȃoȹʩӱȎƢ ɸɈ\u038bӪ',
                            'ȋʎМɳΥèjӴ˩ĨХ˛wʌ҂ŝӂΈϵΘƸPѰΖӿŧåǑ¼Ԛ',
                            'ӞӴɷqW0ʅ¯äӐ\x88ƹϺŬ\x8e\u038dĞ³ȋĹɔʁЙɪǳɃƔўЄʉ',
                            'ѤʚˆÎ7ЊʿҌĹʽƭрǉ϶×ʢ4ɏϳЌʊЛǐśǓ˭ŷķҵΉ',
                            'ѼĪɣϯЏ®ӀçĹɎȡgZˊԨӬ-ϱȴқ\x8cɰĵԧ.ô˝ԏϝʙ',
                            'ȤώҭǺƠβԡɒԃӵŃӢ´ÂӴʭɡҍȅӄE@ɬұŉʉ{ɷ\u0380Ɓ',
                            'ϊʿҲ<İwYԊ϶ԂЉðˌʁӑԂ;ɦəȺɜˏЙ˥męʀϗϿϔ',
                        ],
                    'licenses': [
                            'ǄpȩzҚʰғүǐϾŧ²ɛɠž3ӖбЄȞǌĉԔʻђŅ\xa0ÖĕG',
                            'ɂȴαҖӅ˥ƪʹǻŃ\xa0ҎϷ҈ϋΉӫŁгðƘÖ ӳĆƹӟșώҁ',
                            'Ǭ˂ƊǕaʫЋůԝƩϙ®ȇдӦӴE\x9aɰɀǽεӴǂаȧ!ʿǍð',
                            'ӊ\u0379˙óʊŴρģǍ\x8eȘѹҼϯʆˢeӇҝМͲöΫ¿ǫɆƵäėҞ',
                            'ĜĉŢЏȋϨу#ªƖ˻ѲѢҦӵ҆ŭȢˬВдËƭʭѽ"$҉ѽǟ',
                            'Īӧ0ʄЩѼːǁȱÙċɗ?оҁҧƫ±£ȏǍЮˍ˽ΕʅÍ˞ΚϽ',
                        ],
                },
                {
                    'name': '=ɧɿφɅϬÍԞƼΝ\x9bҍ\u0381\u0382uȀɡϸĀɔѧљǹȮәǺωşŁҴ',
                    'version': [
                            -3933475123847181534,
                            -4433585294563821756,
                            -4344920553659116308,
                        ],
                    'about': 'ĕӁӪȂƐ˼kʖѶ\u038dԭ҃Ρɧ˹ƛȶêǢǚӔīѹϲѥҎǾǔŶɊ',
                    'description': 'ΗͳдДdŒԮѽήευ>ȀԚԡˠФԊǭƦ\x9aӘʁȣ΅DЭɏńÿ',
                    'authors': [
                            'zɕԫϸȊήǻҗ®\x91pńУˣƮҍԈjқТϬϝ\x7fƦЎȠ˗Їz\x8e',
                            '¾ưÎΈƠâŜԤӴɧƿźЮʱѰȼƁŏƊΥǣƽǣǒıĹ\x96ɉŅļ',
                            'ԅ\x95ɛɣ0˶їϾǛæƉMԀÛ"єϤ\x95\x8aѢёŤźӋ\x8a˟ƚǨҙ°',
                            'гȽÄhŕԡǭǏʒùˬмҳȀѫdϏĽ2ЇŉŀʔšУ\x9fŁϐźȳ',
                            'İ˻ԙҋɶѭЍҜfѪɷѩLϬɤϷιˮ6éӈԦɱςiΦ\u038bԬЅԑ',
                            'ђϏ˜ϹϥƎ(үɍϱȡǐΥѧϜˢɻÉИзˢԧˏӾȦͻϪϲˎˬ',
                            'æ¹ВԕƋ0ѰĸʥǭȱӨû҂Ίņôſ\x90ɟͲӸÐŠ\u038bѱ\x82ǟκɐ',
                            'ǩǌβԐΰƾçǺɑʃΣ˧ňͿʉǦ°ʜԇϵ¹«ЎΏĮ\u0383Ňѭ5Ԇ',
                            'ʇ˪ŬϪǐȝɫԟ˥ҧ\x88ӳɂǜΏҥ\x82ȅҸТӁɆ5\u0378ћϾ/\u038bЙԄ',
                            'ǷKԈԫѵȂͶϦ϶ҭŨėȏzȥѮӌ+"ƁƈӒѲÿȺ\'ЏǄψɗ',
                        ],
                    'licenses': [
                            'ʐðɞ\x9dϥѐŘѰɒΟŵ\x84ɖțҬśϙңЋʯȷ˒ѫȝЉɈϾƩʐƌ',
                            'ŽЬ\x8aǉ5ʅȢǈͶәúʴǶƇǬ˟ˊrĿɱŋɴ}ʚū0ȌӶȞȓ',
                            'ˣƆҮȅҔĜ',
                            'ƪś»ŴʯԆάƺOҟʼēɭӲłԓȷÆ řσ#ŐηЌԟȦȠˡЛ',
                            '΄ҘʌԪ͵dˬˣ\x95ȯȬϤϙǊÌȞɓȕƨƯǈοӀȋĢјˮʲÌä',
                            '§ƶØԧԆѼϲɚƾʹΞ˺юνğϜԧʝюƁҿήΒƉƮпїҊΤʕ',
                            'ӳтƜŧŵӃΔ˅ҳԪž²νЋћ$ʌƽΑʎƅũ\x92СŋɗφĒҟӨ',
                            'MҸƙԚͺȼɫϺă0οϒүǾȦÄƐЃϲ®Ζ҈ˢfiч\x9eфЊŧ',
                            '\x85«ɒOыҨԫԛћɄˢѷŦȒƞŵЫѕғϦҗɀ˒ʋ˳OϬҁӷī',
                        ],
                },
                {
                    'name': 'ȶŲƗӝѼѶǐԎƓɱ˹ǪȜ|,ɫȁǲʓbΓђ͵ɸĨЭǋ_ϟҵ',
                    'version': [
                            -2451979675302724692,
                            -6357195872072046452,
                            -250310175030803752,
                        ],
                    'about': 'WŜԒʊ˼ƒIHťӎԟ\x9fˠӫƊϰd\u038bțϿΞӀːѝ(˞ϋŝӶǵ',
                    'description': 'ɥДϏƑѳˇ΄Ż˴țȵ;ˑˏԆЧǓѷɚ\x9fӳëɱ˹ϡǪŨǺΚǓ',
                    'authors': [
                            'ʶȜЛHɐЬњſҼ˄ǱӲƠ\x9fȗяˁ±RȆ\x8dNγρΫћҦϵͼС',
                            'ɂϞ˓ű\u038bӔ3ƹҁвʫƇʜÝЊҧÎԑėùńłŠ\xad0чКǜ˛Ȣ',
                            'œ҃ĪÌϗʺ¢Ӟzțˡ»ƩʻɊ˸ȱ˪ŝɶɝǏǢЦСƚΒƣ˹ł',
                            '˳\x89ѧĽ\x8dɕpς6ǛԎǢ¼ȥʴȧɺȁͱʊз¥ΠN0yĭӛùʟ',
                            'ϰЛˬÜѯˋVӻӑƇsΛзʹԇěǀ-ǷÔɝO˝ƂɮˀʦÍːҒ',
                            'ɅӱӪӦŸį<ɷ¡ҡԊªĪ˼ϢƵµБąǪӈƩÖјY\x95]\x8aϜ\x98',
                            'ѻ˂ԛmѦВϥ˷ǘфɯӨ¬ǋӂkӉPbȔɖԔϻϸΆϼηƇĬϾ',
                            'ūĺЮҗéϺBgҶŐƻ˜ŔņϑʎԭчŴӑϟʰǒѻŷĎӐӛӈè',
                            'ҳŷ\x8bЊÄƉσкҡΉȂΥҨʂō\x90\x9dԓϗɀ\x8cƄɑ˓ҼӡӡӤѪк',
                            'ύtӇʌĠŤ˥xʂ\x96ҸˈĶǤ\x8cϞĬЬèɌƎԡ!҂ǲрҍӑ\xa0ţ',
                        ],
                    'licenses': [
                            'ЗęεğɎλГōԅìҰРɀӂɤԆȞȚԚ˷щΑȸджǐ§Ͼɑϣ',
                            'ƥŔţ˞ʣv\x82ɋѽѨúG³Ʈʫ\x98Ȁǝʰ®ƒţĞu¶\u0383ƋŮƩÐ',
                            'ƒƮɴȞa:ű\\Ѕ˕ȃǗğƣŁ\u0378ʀ²їжҲɺњƐjöSѡυ¬',
                        ],
                },
                {
                    'name': 'Ɋɀэ\x8eЖǲѪě\x8fѓƤŭDˁŗÖԉѹȔ\x93сҋΡʁЮº\x88fėƮ',
                    'version': [
                            -991669776806293109,
                            -8806786444464948616,
                            -2411968571507467011,
                        ],
                    'about': 'êκŚө)ĸČƢλȜÿΌϖԣҳŌЩɣ\x91ƯӊÆ8ϸӿ×ЦǎΜò',
                    'description': '^ϴȆɶ˷ɓʸӆ4Ө҃˨Ļғɀϥ˟ʊ˝ɽ?УȏҸwȰˍäΩӇ',
                    'authors': [
                            'ˢΪЖÜʄыԐјƁȚΌϘԎˣ҅ά&ΪƠ)ŪPƗȹɿ°҆ɏŶ¦',
                            'ɻЯΉɨͽ\x9a\u038dȯԬƵȶԂ˪ЗɚϛӇ˔\x9bЏǿ¿_Ҿǫ˭ӘЈľǉ',
                            'ŰǬ͵ǣҴԁʌϛϥʊɒ\x8faÕÎ҈ӪÎƱҸ\x84ɱŎσĩЫϤӜɲӼ',
                            'aÙϪҸλ\x88Ą˓ƩкСʯXĿÅΪԆӎȽ2θSĺ#ńήԮəϦ@',
                            '˄҄iĄх/Д',
                            'ŇǌðϜɼ\x9fΤԍśʄȢӧЂӂn˛ȈϼŘÏʎgҭϸ҆ίȜеéʇ',
                            '9ȹԫ\x90\x97ӶɪϴҠŁȵȯΐƽŖŻʐȊ0˜ҽӴŸƋƮ˄ɽЃШ҅',
                            'ѾǬǜ®îʳŵ¬ϥϐƀǨČhȎLѼǛϹȢԞĵϥ\x96ɂ:˘ǛәĻ',
                            'ЈЕ@ɵȳĒƅәуˈÞЪΎlԈЈǽ',
                            'ǣѐеӖǙnÍͳϺˀÆϘt҈ϗƔɺĞɍ&ЍͱƢƝϕɧԉјĪɱ',
                        ],
                    'licenses': [
                            'вĳȓėʠʚƙ?ˤéǎ(ʫϑƺȉԝȶȀVϮȬˆɠɣŮɩßќɡ',
                            'ӣџӊŷԟԞ˻éȎéƪƵԘ\x86ϹαŌҁªƚҥȼÂ8>ÃȍÜӪЪ',
                            'ÒɛԄ¶ɀ1ыȾÊɎрŰĆΈͰχЦūЬϻʷϮ˗ƯыГαΆжĪ',
                            'ϣ\x8fˍһͺǜǂʁɣčϞɾӦʧδКźӲХǯȣƷĲɣΟҦƿ]=û',
                            '˗˂ǸȭβÒХфđ˰ѡхűұѨɂαŒӄşyԇ\x82ϥɶǈâ;ȩͻ',
                            'ƼƬǹ˖ʰԤ˗Jº\x94ФѝǤԟȿƜ;ԩϒȡԎ\x9bŔ˼țǨӊԝǆŔ',
                            'Æʼ\x8dʛEҋǄãƔϊŏûёΘЮ˟ʇ©ΉҮÛ',
                        ],
                },
                {
                    'name': 'ҊŔŘȢƖëǕԜăɡłŒ×ʫӡɔҕӯѸǝȀÒăǃԕΐҝ\xa0\x96Ώ',
                    'version': [
                            -7096355769351334504,
                            -170193401597799299,
                            -3361148032201866677,
                        ],
                    'about': 'ԧӒțb\x8dɖΌ\u0378ǇƄɴŮǟɲªҎхåˌ®ϵʂ\x97ɖʩ\u0379ǟϿԁL',
                    'description': 'әЮфΔгњ˦Āԩ\x8eèѭʍņɲϓȣΑ˫\x8c˾σѼӴњŅŲʴaβ',
                    'authors': [
                            'ʆҌĕ ȅŶεŖ\u0379ҭĘМğφò',
                            'Ν\x9dϛӼĄ&ɇG?ϝлʇԤEˀ˗ўνɤƐ¿ϋїĜԤ˸ʷцȯŝ',
                            '\x83ʇіʦɸȊƘё"ʛ\x8fʹ\x95ȏΗơƻŔ˹Фʑǳғ˷Ԥвǎ\x8e΅Ѷ',
                            'ǗԊˤΉҳŋ\x7fз&ϐħáĜ\x8fʖϺΞ˝ҪːʱĉҤӄυóʈɧTĸ',
                            'ŽӖƣYɒєІԀϸŕȫ½ų/ĝĄµɤҏʠƠƶӒɔɴǲӁΣԡԍ',
                            'ƺԤϮ˵Лѷé˛ɷқϢЏəҴǺύвɿԣĚȵԣҺȕȵРԎη˗Ӽ',
                            'ѣҍ˓юŇђƌƂӏ¡ʳЊӃϘʸGӕ˂ȦʭĦҁǄʩʟ¡ɉƏԨǡ',
                            'ʻӅĞæҿΊɎ\x84%тҢ\x99϶\x93Â¥źԎ-ϸ^ʖѡЕΔǹϓÖ˺ϰ',
                            'ͲˏфǹƖʨȳϱěΑʃҙ\x8bͱΡýҋʘӆϜÐ\u0381қǿ˔Ňɫ˙˩Ӄ',
                            'pğʸѕѦРʒũαŹϭüƽԄ\u0379űδҽDѐǸ˒ΌƒЉ˶Ϧ\x9a\x96˛',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ʟeƬyƅ»\x96ķ˄ӶYԍȨďƿɭӲï´ɲȠ˓ħÕЉŲěѷʪ\x97',
                    'version': [
                            -1152555180677944530,
                            -2362951904807891030,
                            -7167288236919277335,
                        ],
                    'about': '˶öÔзġϠËǼʵÊұәǢʉɱԂǧ҈˱ԫϿŭӱ~є\u0378ʰĔūҦ',
                    'description': 'ɖӼРǦȜĦTѼϾњҕѤПӕɠǑϣϢλŔѾӯƾȷͿҭī\u0383ΝҰ',
                    'authors': [
                            '\x83˩Ț˙Ϸ˼ßȵϑÏǧфÕғħθ΅ĚЖсÄҙƓÛɥďÓ˹њԗ',
                            'ɴѬѿÆÂÅ¼ˏҼϯǲ&ϐʐȝͱҲǌԟƳǐЉӂ>Źʠ[ƑзÐ',
                            'χƳώʎFȢ\x87ĞƟƫƽř\u038dɱ8ѢȸőƲƳӀ´˜ȹξ҇Ӳγίϻ',
                            'ɅːʺƇІԦŭӌVģΤ϶ϏʔƘˆԑԇ\u038bδůɄхпņ©pρҴ\x9d',
                            'ƴöȪ:ӶɍķƞùƓµǱҸԌʖŦ\u0379ϟȚEΎӊŴп\u03a2˛¼ԜΕɉ',
                            'ԧΡ˺˓ɌȡѼуӚ²£ɷϪôϰǚӑǄҋ˨ĨȻĵ°ǶѺ¤ȔϒҨ',
                            'ŋТǷ®ũǹǑӥѮǙϰ͵ӓʊķÑ˄ĄïǞδƺɔ˭ԩ˫#¥҃\u0378',
                            '˴ð˦ÞԧӊáȖ\x8aɡϐˍКӤԏȚьʍʙĒĨˇ҆ɓƿş˓пȓӋ',
                            '¨đű\x82ʽͶЛƲĕȹц/ŬŌfŔɵ˵ÚÔh˲\x8fĊŋЉЙƲχЪ',
                            'ƪʻԗʨ´ɜԂȚȩñҢӰɵȒѓђÖťѴӳÓώ҅˧Ⱦʕ6QǇѾ',
                        ],
                    'licenses': [
                            'řƷǸ\x93ӨһȦhč\x87ÀƚӰ.Ϡ\x82ЋєӘДtɎΜͽň϶ȝȏ6Ǣ',
                            'ҫΛĤӷɊûĵԅϥWǇȣ\x90Њґ˕!˝ìѝěɃ\u0381ԏǦмŧӽʖˬ',
                            'ȅ\x96ðñҍϡУÁ¦ҲѢёʓŋ¥ʑƨ\x9aғ\x86ҕǔҖ\x92ӔƝ\x9cuǒԄ',
                            'ԏΓƀ;ѐѮœ\xadҵӋҫŗ®¾ϿǱʈѴһvʲŞдíǞӂŚŰϸȻ',
                            'ɘ\xadŅл°ϭȧҳůŔԩʼŹɝ8γұʄČӉϋŉʈѦӥӛғɂ\u0381ƫ',
                            'ĶȍŲƞЧʣ2tƦŦԤÆɯҵϑˋѶɣSȗ\x8e˓ͻÕĩεÐŰοF',
                            'Aż\x86ĎʤʥˠИ҃a˶ȃЮľ\x98ϩɞљͺʩǌlѽƉ˓Ϫˆп˳Ɉ',
                            'ʿb¹ԧśΕӟԔ>ӜòĞƌ',
                            'µοðvđ4ΖƭĢWȖԩˌƌòĴưШŒŸĕКԎӺȖ©иʽˤȫ',
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
                    'name': 'Іҡʴ',
                    'version': [
                            -9040323212733116507,
                            -1205898002122520539,
                            -4346081869649834659,
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
