# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-24T16:41:01.153178+00:00

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
            'name': '}HӠ˳Ѫюӌ҆ǡψѸφί»éûˆȑϡć§ԉĞýɘĈƶɓ\x95ș',
            'minimum_version': [
                -3275057071908012531,
                -8155137089347926192,
                -3427987983467490591,
            ],
            'below_version': [
                -3942346692171921533,
                -5048852152142170254,
                -4221341976594355948,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӴЯɕ',

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
            '$': 'ωJǙЗƓ΄ƳϋΊЈȎ÷˭ǄˀťνƠɰǋҴ~ʄdƔϗί2Ԫȥ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4051222402216275797,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 734310.10200256,
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
            '$': '20210224:164101.069004:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Ю4ȨĤɄϬǂЊʉ\u0379ϊŃѰ¡ѝȦдɀò®¾ҟķąΈˌřĽɕź',
                'ȧʤеŰƥϏŽ˲íűʉʁˑΔТĤɼͺψ½ǐЛüˀԤщɻΪɉѯ',
                'гЀѡǄѕǰȟФӇƅλĖηǇØɼԧѠÛOŎ@VЩȒЕȹʇȽ\xa0',
                'һБơӼϪǖўŌӁКkÌɾ\xadϸüѕчθӈ%ɟƌƂDˢʑ\x99óä',
                'ʞχ˽ɔӟϑ˂ǳòԞʹѸǃѻIвӐ\x93Ƨјp.ɦӊǴ.А\x8dҭ,',
                'éǩҷѰө˾ϵ~ӆïҭ҉˞ÀȲşρB(ӠϑӑҴнЧȒ˷³ёƳ',
                'ȧϋƉŀԀǏżӐԦ˚ßʸVçɲӧʢуϯƊƬԨДΔƃκԃ\x90ɑҊ',
                '\x87ԚƴǽÀǔԫËÛīѭĤɢĠĚĤ~ӮԣѾțϫҿ\x88ҤȘǧέĮØ',
                '\u0381ƕƚύzүƕӍͺˊ˩ȨԨϞΔλNӆ˖˅πȣԛӒσęƔȜɰě',
                'ÂщŤȐӚňϹŲЫӊ\xa0Ļ¦ˎȕÜϗԬ\u0378\x86ӥѿΌŕǡǔҊéʡԙ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -6287150960718017277,
                -3204418462372254256,
                2311715568029637248,
                5298752923535278437,
                4431727200162248976,
                -414519700480833136,
                3805240662092303923,
                7417316190539248641,
                7197334654236441938,
                -5070431500797658690,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                811569.5578180715,
                475650.32451960223,
                899248.3690058119,
                403347.0581342898,
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
                True,
                True,
                False,
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
                '20210224:164101.069893:+0000',
                '20210224:164101.069907:+0000',
                '20210224:164101.069915:+0000',
                '20210224:164101.069923:+0000',
                '20210224:164101.069930:+0000',
                '20210224:164101.069937:+0000',
                '20210224:164101.069943:+0000',
                '20210224:164101.069950:+0000',
                '20210224:164101.069956:+0000',
                '20210224:164101.069962:+0000',
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
            'name': 'ͱ˹ǋ÷σȳЛѷʔ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210224:164101.068622:+0000',
                    '20210224:164101.068635:+0000',
                    '20210224:164101.068643:+0000',
                    '20210224:164101.068649:+0000',
                    '20210224:164101.068654:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'α',

            'value': {
                '^': 'datetime_list',
                '$': [
                ],
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
            'catalog': 'ѥǺǍԁƈί¼ăXō÷¤μ\x80\x91µԅ±˱\x80ʽΝǫьʌŉП\x87ļÈ',
            'message': 'ıԉЬȀξcԭĈȤ˜ŽΘŢ9΄nʫ*ј´ϡӐŔΧlʶßАФļ',
            'arguments': [
                {
                    'name': 'ԕӃˏÄŜѿPѿ˾',
                    'value': {
                            '^': 'int',
                            '$': 7640125520294838351,
                        },
                },
                {
                    'name': ')\u038dřΆƆɘm',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ǝѹDƿ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210224:164101.067052:+0000',
                                        '20210224:164101.067078:+0000',
                                        '20210224:164101.067086:+0000',
                                        '20210224:164101.067092:+0000',
                                        '20210224:164101.067097:+0000',
                                        '20210224:164101.067103:+0000',
                                        '20210224:164101.067109:+0000',
                                        '20210224:164101.067114:+0000',
                                        '20210224:164101.067119:+0000',
                                        '20210224:164101.067125:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ɐ\x96Ĝ¶]Ʋ¢ƖǻϚąӘȚӅϝqˊӕеʜιˇӵɻӨɤȠ\x90ΘЇ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210224:164101.067354:+0000',
                        },
                },
                {
                    'name': 'ŊԀПїɸģźǸǮБkѾӍʅԒǗķŻhЋόϑʗҖЎʗʈɍˆɠ',
                    'value': {
                            '^': 'string',
                            '$': 'ŝԂβΧԡѐǂŦԧŽåʙȔǎ\u038dΕûԦςԜͽ\x7fÕӣԇɃʚŸ\x8fõ',
                        },
                },
                {
                    'name': 'йҮǀЛƈϝşӣƻĶɍɖʋ˶ȣψ\x9eΕαǕĻǠԛԑ>',
                    'value': {
                            '^': 'string',
                            '$': '˩М@ƟŧɂKƳʋӗŉ˔ԛЋ\x9fǓȺäƫĶҰˣԃǼǪѷϹá\x92ͻ',
                        },
                },
                {
                    'name': 'ҘJĸƖʆϳɡƱǣŁǖь\x98ҎкʢǞͺ*ƤϽÍǙ˾ˏìV҃ΣŞ',
                    'value': {
                            '^': 'float',
                            '$': 986685.3480627325,
                        },
                },
                {
                    'name': 'Ȟ\x94ҝͱÄĀȮ\x83Ȳ\u0382ƎЦɔ҅',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        ';ȀԚ˟ϓҲʬöɨJƟҾįȴȔǾŖ˅ǣ+өǦҸƊˆĂΙьƟƔ',
                                        'ǂ¼ɍҺƖR˭ԣχӮnˇӭԍʡɃѥʤΰĚӃáΊФΒƤѥȰɧҶ',
                                        'ǝӰҋȏȽȚʈπǹ¬ǲSҀҵԇ`ɔäΊΡʡǂѪ\u0381Ӂ\u038bʔёǖņ',
                                        "ɼԥ\x83ǪӞԮԤſ'ҋˎоˎˆϽɪŌђʰʎɣĐƓ¡ПӈˎǕÅǇ",
                                    ],
                        },
                },
                {
                    'name': 'ЈҤƪ˴˺\u0381ӅXǇǿұԩʼ½<ԙˑƝКȣҖÓŅҀƘѲųȈȞȄ',
                    'value': {
                            '^': 'int',
                            '$': -7199700042425125396,
                        },
                },
                {
                    'name': 'ÏǢ˨¥ʬӗ×ʪĀҬ°ƥςΩ˖ӾϡóʰӀ\x86Ǭd˺ԑԏÀɴæâ',
                    'value': {
                            '^': 'float',
                            '$': 630644.1795063049,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ѓa',

            'message': 'Ƈ',

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
            'identifier': '\x95ΰǃɽŝҽ%ŧӴҿԌGЕĮʰӘò7ԠɷÂÓɮЖ5ŭ¼¿ßɧ',
            'categories': [
                'internal',
                'internal',
                'network',
                'network',
                'os',
                'configuration',
                'file',
                'invalid-user-action',
                'configuration',
                'access-restriction',
            ],
            'source': 'Ȓ\u0380϶ŖǉʸŮʡÕЦѷɇʛ¯ΊʲɨͽǊΌтƖԤχˡÝƜͶԉp',
            'messages': [
                {
                    'catalog': 'ưѿǟξѫϷĢPƱϒ@ӐUѱϖȶЛ˳ҨŰĜu\x7fʑƥЀnǥǨŵ',
                    'message': 'ʉɭ;əʉәѥÁǠсɲĦѳȷ҃ҫΜϚҷ£ҨÄЭд\x9aԉȕͶƿˉ',
                    'arguments': [
                            {
                                        'name': 'Ҹ\x9aοȏˀŕ[Â',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЍΘ¡ˎʏpӫǂǏӟӄѭΌ\x93nȄǨҸ\x91ҧӿŁԒ\u0380Х˯HȀ\x9fɣ',
                                                    },
                                    },
                            {
                                        'name': '\x8bɇϟɸ˖αĤ˃ɾɐňĸҩǡŹӶƋĴ˔yʐʢԧ˰ҟEʻȟѓˬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.036974:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҟƶϫжϱ˶ʮŮŨȞϙÍН<ȀҚБņ\u0378ˬϔƢϽƝ&ȥĚəѿʦ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1978981369778055520,
                                                    },
                                    },
                            {
                                        'name': 'ƍϋKƿʺɭƁÅӑԑȔѳɰɒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ІʗʅӯϥBӥƽŤȩ©0ıȟŏơöϑε',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.037380:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȕįґΑԉʺxӥƎЌȮ҇ǜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.037511:+0000',
                                                    },
                                    },
                            {
                                        'name': 'їǰǮψœ^Ľ´ŦӷѸё¶˛ӵпδźўȲϡəԠĬǠʰÊƺƵ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'úҟ5á\x95L\x7f²ϜjόЁӓβž^˽ĸÌδ\u0378ōǐ˳ƖӅƗѬʓʊ',
                                                                            'қǬÏęҖͿ3ɿwǝӋƃĪȞȂ\x84οώ˪Ń)Ƀ(˂ΰʈŵǈǢÜ',
                                                                            'Ѽ˘Æ˪ÖіԘ4ȊԤĲö.γ¹ΓȈř˦\x83ϟέīɨΨɃǓμǼώ',
                                                                            'ǼӀĢӌ;ԣµѫћØ©Ty˛ˉҧȋĳěхɱȐȌԄŰ˹҈%ч҉',
                                                                            'ŵ˻Ԟ˚ԙŭӱзɇȠˆƁȇҫO˗ǢΖңΫİĀʂ§c~Ҝ6Çӛ',
                                                                            'ĈïС\x99ĕvβɾСæāӀŀʑƩ\x90ƬˆǛżҾɬ}ʸǡ\x98vцΙ˔',
                                                                            'πѤάGϾԮ\x9fȵ{ЭүʉÂ£ԋƑˁɒčøµіĽԡѐΑ\x7fʤȜɰ',
                                                                            'ƹƀɢӶɰҰȀŬɑԡѫҟûĝԁŕˊ˔3ôεɪɨȪųώѻˣÙѳ',
                                                                            'ǘ\xa0ƝɓƪǀҦšӀˮˊƣñèįɒѨˇʏэˈĹ˵µԫ×0ӣǨǾ',
                                                                            '͵ӧОά»ԢȟǢƔϨТӍìҵʍˎΣ˾ǧҺԁīŪʸӍЁǪԗĪȾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȵvт§юЄϑ÷×ѣϻ˼Ĥӈį˩OƖÅψу˒ÂϼEŌƧ-v\x9b',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.038071:+0000',
                                                                            '20210224:164101.038083:+0000',
                                                                            '20210224:164101.038091:+0000',
                                                                            '20210224:164101.038097:+0000',
                                                                            '20210224:164101.038123:+0000',
                                                                            '20210224:164101.038137:+0000',
                                                                            '20210224:164101.038144:+0000',
                                                                            '20210224:164101.038151:+0000',
                                                                            '20210224:164101.038158:+0000',
                                                                            '20210224:164101.038164:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѥ˟ςζǓ+ȉү\u0382ӣʶͳ+ÜΪÜą×-ȔӪљҽ¥ŻъєŲÓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x9b¹Ϩ_҃ȨҎǛɡԓ\x86BÖ˧ˡњȝ҉ѠȩёѣŊɪáЉξǅ]σ',
                                                    },
                                    },
                            {
                                        'name': '`ԭůёϹиI\u0381\x82ˌƵĦòʑǩ˓˃˵ΙFœҪǋƩɠƭDµϒӑ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            820905.3005459352,
                                                                            489312.97011658945,
                                                                            785580.1943708577,
                                                                            140084.49413474332,
                                                                            501537.8235515391,
                                                                            712418.9185950813,
                                                                            95925.1562783836,
                                                                            27964.576046400267,
                                                                            -96023.85520407795,
                                                                            883484.4388812933,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѷШɼʟŻЕҟԛΐђ˸Ҿϡƙ\x99ɡџùʗœŜʢ˻ŪǑǙŔůmӗ',
                    'message': "ʴƏTҘpȭεʤ\x8d\x8aGĎʸÐѯļ'ʿЦ5άdҬҦҝ\x94ƜŏЋΏ",
                    'arguments': [
                            {
                                        'name': 'ҭӔȤūƘ}äк\u03a2@ƣ-ˌ˸ǽɺҲѸ;Ŏ˱lƅ\xa0ƁyΆІϟʬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6619683696326726629,
                                                                            -1267993402060606045,
                                                                            177200603794637372,
                                                                            7886959462990148791,
                                                                            -5608598080240574902,
                                                                            -4590909013585425292,
                                                                            -8131390642498628949,
                                                                            -8844558627060081972,
                                                                            8576649180520469979,
                                                                            -2423202845932956076,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԨňÆǥ˘\x85ŀӔ[ǆъ`˹ªŘƒļ5ʉӕ*ԐӅџǦϱҗͷʭԖ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҧ\\ѥϜƗҲ;ӿˡ҅ΓØціȾʲīǸɱԠČĝ͵Ƭҁъ\xa0ƌȤƙ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.039824:+0000',
                                                                            '20210224:164101.039840:+0000',
                                                                            '20210224:164101.039848:+0000',
                                                                            '20210224:164101.039855:+0000',
                                                                            '20210224:164101.039862:+0000',
                                                                            '20210224:164101.039868:+0000',
                                                                            '20210224:164101.039875:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȼĬĘ\x87ËŹħǱÄŬ³ȻΏʔϭҽҏˮͰӋ˹ǃƧвϋΗɾϡԁ˶',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.040115:+0000',
                                                    },
                                    },
                            {
                                        'name': 'βИЎĚQ\u0383\x88˓τ=єǒ)Йʵ\x85ЭǖƲɍº!ԖϟɯуȗȜħ*',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.040279:+0000',
                                                                            '20210224:164101.040291:+0000',
                                                                            '20210224:164101.040299:+0000',
                                                                            '20210224:164101.040305:+0000',
                                                                            '20210224:164101.040312:+0000',
                                                                            '20210224:164101.040318:+0000',
                                                                            '20210224:164101.040325:+0000',
                                                                            '20210224:164101.040331:+0000',
                                                                            '20210224:164101.040337:+0000',
                                                                            '20210224:164101.040343:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ь¼Ţӯʄˊ˜ϨƼǬѳԬ˱ΪȑӄŪȰѪҶОћѪɈƨƂ˄γ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.040602:+0000',
                                                                            '20210224:164101.040613:+0000',
                                                                            '20210224:164101.040621:+0000',
                                                                            '20210224:164101.040628:+0000',
                                                                            '20210224:164101.040634:+0000',
                                                                            '20210224:164101.040640:+0000',
                                                                            '20210224:164101.040646:+0000',
                                                                            '20210224:164101.040652:+0000',
                                                                            '20210224:164101.040658:+0000',
                                                                            '20210224:164101.040664:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЙОɽTÐӧёˁ\xadы/ǵҸĦГұyϨƽЩƹʭԃȆ҇ѼЏq˞Ί',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƃuӗϳӂɂ\x9aȷӧȒѼƥҚʟǈ"Юϐ\x87ϘǬĬЖқʼĠóΚZѥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            338401.6542027632,
                                                                            993308.4016229706,
                                                                            857121.1846684822,
                                                                            230546.0413965006,
                                                                            124162.69113597646,
                                                                            53654.463073885854,
                                                                            78017.79143524054,
                                                                            796672.8309473579,
                                                                            192400.42299707595,
                                                                            682693.6339744526,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'SЙ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -18628.331507305804,
                                                                            324039.7493460295,
                                                                            247954.01370952046,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɗ³ĀшǆôǤÌʸ˨\x83gяӚ¹ĐԊм4Ȱ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Μ3Ϝ=ĜōǬԜǩпќ͵ͷQǝРĿɍ\u038dĂӻЕѧƘѡ9ΚѳϽӦ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЪlӚė\x80ΤҵνӁAМБȈӋѢӊwψżӺǄîԗ˔ʎƬ˽ĺ˘ɨ',
                    'message': "dяƿǘьɤêɱ'ŸĶΎʋЉǾӪœϐϞ{ÜɏČƓˀUĜÚΨϬ",
                    'arguments': [
                            {
                                        'name': 'hҴϫωӡƺҋƷ˩Ӣ¥',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -61187.91722701976,
                                                                            624959.6370283552,
                                                                            143859.51148829155,
                                                                            25407.618867834797,
                                                                            87874.02450036383,
                                                                            15158.082990842347,
                                                                            -30663.30670844829,
                                                                            905353.2112241897,
                                                                            466013.66825762787,
                                                                            671300.0881540457,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΚĶˉÆԘҬƪŜŞ_Ż\x8bïŤҏĬΨТϘЀȹǏόҩ©ΊӃкϖӆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3370252103187126184,
                                                                            -5548407646492962231,
                                                                            3823650054586700702,
                                                                            -3502838734512404154,
                                                                            6968256292882910721,
                                                                            -388402418892410064,
                                                                            9138539555456165695,
                                                                            6505874779667679204,
                                                                            1516200796257077599,
                                                                            -4335359060973888176,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѓȿœιЎRҿóʗΒΡʧΗԘÄœőΕЯαѸ҈ʶ˹ɧȆïβɉſ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            222166.91042504262,
                                                                            614115.7585377174,
                                                                            811259.3390556916,
                                                                            70188.71734080263,
                                                                            854071.4668346973,
                                                                            610737.522543445,
                                                                            984916.9403957948,
                                                                            442115.7119678076,
                                                                            541657.3534727554,
                                                                            736883.2824274373,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҹ:ҤÜʣ\x9aƆ҄ͲƏǡҘ҂\xa0þԢÁųʵðͻ˴',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4596733952768815671,
                                                                            3430413253335586550,
                                                                            -2052334461116196073,
                                                                            721745591057713045,
                                                                            -2562375406789448241,
                                                                            3298275325987276366,
                                                                            2416047496768092663,
                                                                            8920778658762979824,
                                                                            -3587012615998478016,
                                                                            8389713572944302838,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÜZ˄ǚϨȉƪΪ$Ƭɻԕ§ǹž҅ɯѢAԏĲΐɣϾɢȥȬɽ˻',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.043229:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƣ҄ɀθɅҍ\\ƠӮԇ¯ъ¤ˑόϩΥȽ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'γ¦ԟȥсӏĜȖѿǺ҆ӕoSȬƴ˞ҰΘ˯Ŗ®ěӾ\u0378ǀĜb˅ĥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.043678:+0000',
                                                                            '20210224:164101.043694:+0000',
                                                                            '20210224:164101.043702:+0000',
                                                                            '20210224:164101.043709:+0000',
                                                                            '20210224:164101.043716:+0000',
                                                                            '20210224:164101.043722:+0000',
                                                                            '20210224:164101.043728:+0000',
                                                                            '20210224:164101.043734:+0000',
                                                                            '20210224:164101.043741:+0000',
                                                                            '20210224:164101.043747:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÖǰŕьϾŐҖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԏɃ˹Ǯґ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            592965.6509385105,
                                                                            457539.40038825735,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˶ʅ˼ͳVӯ°ƿӓȓӺΕ´БőğĴĞ¾3ӎΉёѤÇϽ˵řĞd',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.044378:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'žЦ\x82ʎҵʞȳËūŊќңƥǿώүɡ\u0380ɅʏϤȦΰĂͲ\x9aԙŦŪ¨',
                    'message': 'ԃøԏҚOғʊѰԂƕ§ʓҲӅɳȏͿ\x87íŹ҂ɳε˻ͲѤθĐHʋ',
                    'arguments': [
                            {
                                        'name': 'ӁЦų\x9aңÊϤŁύˮɩ¡ɵ5˴ŤķȘĨǊӾŸϝ\x84Pп®ťΉЃ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 216641.2499221281,
                                                    },
                                    },
                            {
                                        'name': '˭ЬȼԨ\x91Θȩ҃EƉϋȯþǆěI)ŀƠλˆGİxĤZ˱ϪηT',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.044971:+0000',
                                                                            '20210224:164101.044984:+0000',
                                                                            '20210224:164101.044990:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĽņƮҝЫǢņßɅƟĄfϮɸǘƪ³ӱϫΫʘʃǟȥҬȰôϨϼȚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'Ŏ²гӝʯ"ȊçvӍǎǖˠǠĥғƯĬ ϙĎѷRїö\x9fǍīͺˠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6193884514706235272,
                                                                            4407364061902562950,
                                                                            -3528135457030842069,
                                                                            4861936054997987364,
                                                                            -3310576681492545581,
                                                                            4303572974930310964,
                                                                            -8130586225043470228,
                                                                            3517249926173796122,
                                                                            -3455399872578979080,
                                                                            -6501234579313370946,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΜƾũwŬɻΗЖΪɶΦß÷ɹƨ?®ƱVΆԔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˹Ͻʆӛ\x97ĀʢЪ҉ȩҟԘʼқϩƃx˒ӝк+Νа\u038dҬВģЗv7',
                                                                            'PǹчǹϺǾҖɭν7Іɬͼь²ŮİƜˈiɗȦñƋ-Ȗǜѝԃʝ',
                                                                            '\u0380ӏǚȣϊϴõҎѧпц³ϮԆüӴҵƗѨЧİфȝԀӜǄҭĄĘ˷',
                                                                            'ӅɫŻȠš\x96ϊСӗÌϔˁɾǻ˧ӻӏĳ˯ïʾçԠӲԋqȺǰʞɳ',
                                                                            'ĔĻʯјɭџƽϩǴơҪѧƟĲѬӺčѤɀǌʺɯҌ¹ӬťƆԄ\x8fɸ',
                                                                            'ϴ˙ǲȣͽӃѭƷɂųÕ˃Ʊɢҡѯ^PϛƺϞɽVϚʊ£ˣԬȲɭ',
                                                                            '˼ϩрѥ³ӝɰіƬŔ£ӿ˗\x99ſƹƻĒwКɪɪП\x96˳/ѱЩ\x91C',
                                                                            'ҚПѭɝŐɦʷϧюΚǫ҂Х\x95οϜŁƟԄĖΜ<ʹÞЀǞǱĽïg',
                                                                            'çíԅȞѬȝǻ҄Ҙ~ʝǮлҜϿŵӪƥÑʾԅ\x83ΥӖƜ?ƲНĩє',
                                                                            'ђЫҦӀǌÆƳ\x96ΈǧġȄӶӮêƌϒȮjċĠӋӇƋδͽϺх¯Ъ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˸\x82ΜÈʜȿƼŎɱ}ȊNԕƹ\x8b҄\x83Ӕ˻Ñ¹ȕǓȲŭWʓ5£ñ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'оΫϽȬʒˀԉҤű3ǛˎȯŘч˗ѭ\x8c"ˣ\x92ĺžƐαēϗÖȦď',
                                                    },
                                    },
                            {
                                        'name': 'Ҷʊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.046220:+0000',
                                                                            '20210224:164101.046233:+0000',
                                                                            '20210224:164101.046240:+0000',
                                                                            '20210224:164101.046246:+0000',
                                                                            '20210224:164101.046252:+0000',
                                                                            '20210224:164101.046258:+0000',
                                                                            '20210224:164101.046263:+0000',
                                                                            '20210224:164101.046269:+0000',
                                                                            '20210224:164101.046274:+0000',
                                                                            '20210224:164101.046280:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԕ×MøϘɱοȅʗ»Ȋ˰ˆӵβνĥ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˕©ӦʞЇ˫sԧԏЖүҝ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8765622394286656134,
                                                    },
                                    },
                            {
                                        'name': 'ɭ˸шŚBβǴ\x91ұ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.046846:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŐϷфŃ͵ӠÕП˼ɗʶȍҋĿȞˬÕԜɻɸȻĚӋ\x9fμɃĞӷΙϓ',
                    'message': 'Ŵӡŏү¼ӏ\x81к˵ҒɲяͶԇþʩ˖ǱǐƢĦņҬҊ˪Šͷ¡ϢƊ',
                    'arguments': [
                            {
                                        'name': 'žӕǆɆЇԙΧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΛεȩǙюΣȭвϼŎιԔȇ\u0380ʷT˾АȦ&Җѓ˄ϥѾвǹŬ\x83Ҵ',
                                                                            'éĕˍӓЧюǌȒҒҖ\x90ӣȊϰ·ϞɤѾ¥ӲǝīѱέѴˣұČЩӛ',
                                                                            'Γϣ\x87ɣ҆ʎȖԕϟ˜+]ШʠgVƅѓ^łЅĦżϳϰɸΒŴ*Л',
                                                                            'ǅХӐʇ˗šϯн\x9bãʰǠȡʉĨщϞӄϢʝǐ¤˂\x7f&ɬ\x85śɿL',
                                                                            'Μ\x9fҌӢĹșϦ^ŊȀ\x88qβЏԃǊ0ʔʩ˶ΔǞȳuҎɣʆȳɥ\x92',
                                                                            'ΙUӐѴвu˻˕ǪҏȤӊϝшǩeʒĚ«ͷѸЖЃқЙʫˊӣԦ>',
                                                                            '[ȨЪλӼεԬŬ˙˷ϥƪʒѓƒϕ[ɛȠćѾȲ7ϦїЇɰYǐԔ',
                                                                            'ȴÔȅϲ˕\x92ɘЇ£ϭҵҽͽhφ҂ɮ©ţυɎʾSςŗҗʉàPϥ',
                                                                            'ѫБưɲе·҄ń:\x90űɠľȉʜɘƠɣǪzwԍƋĘϗӬϬþǣэ',
                                                                            'ȗʨĦəƆĒʷ˙ĤѺ˙Кȍ҃ԧԡ\xadɮԄЛ¹ĢÃƇrЩΕѶơц',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'rʋz˦AδšŇɁb\u0380ʖǤΕѺ\x93ēҚǾŠѣԊˊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.047694:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x97φˍԙѓ˴ȴО',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7476423878824582640,
                                                                            6978328244126760586,
                                                                            -8130361649761948775,
                                                                            3273775526552409973,
                                                                            -1437469233515260092,
                                                                            -4106680574723530538,
                                                                            2866473878995386338,
                                                                            5909337152043105251,
                                                                            -3120884483811871894,
                                                                            -6476899607314717398,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЏĒǳƳ\x92҃ԪϔϨƖH%ȊɺȏԋÄˆ\u03a2ԬĴӥǜĊϡϴѦҶ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'бԩӿ˽ǪˈΚ˞Ѧȵđ\\ǱqȄǴӪԘ÷ҸˤɍɂћˉxƎ˴ØĞ',
                                                                            'ˡƵƄǥŰӣ·γĕϡѺϝǗϰɻËÆȭε\x82ȭЍɿϱ˦ˬҠǁԝĿ',
                                                                            'ӀϹыϾх\xadØΎǇҹɦȓюòǄЌ?ԥҦс<сǑϸaэѮ5ΞБ',
                                                                            'ĉĩĦЖ<ãÇҘЮФ,ǯӓƷԝФšȆЎ²ԩѾёTӓũʞĦħɛ',
                                                                            'Ϡǅ³εяvĴЖȃСΡΫѬȓϿ+ϺƩğ/ŪϿoκhīôŌƋ\x85',
                                                                            'ȄȃśƨГïϮͻš΅ƂӽҋǹΥǽ\x8fǽ˗Ľ°ȦӃ˳ʰ˼¿KЎX',
                                                                            'ђʸϝѩоƓõѱƪâ<Ī˹όïҕӥ˛ŝĬǱĨIѻӮ҄§[ƌδ',
                                                                            'o)ÄǼ4ɀɮβѐхϷԡȎƝ˗һƉƑͺӡϕԇ΅ȲщќɫӦŔϋ',
                                                                            'ġ˔Ǉђαµˇ\u03a2å¿/ӗΤĤɂǬ΄ԑªќRʑŋȣӸºʠʝķ҂',
                                                                            'ϭϘѱǃǘС˾)˞ζǴƑѹŅĦάʥƓπΡӼƭԃ˞Ԝϸȸˍ҃а',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˈĐȾӲr˚ƇӰǉԮѨğҹĜ˖ȴԧԈVӃѦŨkҪǏРπ\u0380Ćϯ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ӆʐ΄iϋљˏ˻\x8fžɰPǷɩǱҌ˽ѱԒƠӤF˳ȹ˛EӬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7658658259710216618,
                                                                            -4206310196610551931,
                                                                            7538950259812136584,
                                                                            -7721215103613246911,
                                                                            -2578196389739911716,
                                                                            3504972720286959849,
                                                                            -8854364723047652588,
                                                                            -2409636774047339370,
                                                                            -3906132113662386861,
                                                                            -8621631925245240796,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȓ˹ԫˬFԃ\x8cϤȇ\x92ͳÅĦUԌɨÃΑӒŃlԁǚϟƐӜϚΡґȓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            92.90283856574388,
                                                                            933697.6157816221,
                                                                            756183.9538047317,
                                                                            711282.1877899377,
                                                                            751557.096699525,
                                                                            92468.90270894315,
                                                                            674834.3024831921,
                                                                            23696.10514464001,
                                                                            778578.0884074501,
                                                                            -88118.17179982037,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'TÀȢŻiӲnΏ\x8cǪЉƫӿ¹Жњ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.050831:+0000',
                                                                            '20210224:164101.050859:+0000',
                                                                            '20210224:164101.050866:+0000',
                                                                            '20210224:164101.050873:+0000',
                                                                            '20210224:164101.050878:+0000',
                                                                            '20210224:164101.050884:+0000',
                                                                            '20210224:164101.050890:+0000',
                                                                            '20210224:164101.050895:+0000',
                                                                            '20210224:164101.050901:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Żϳ˜ŔğƘƨTӨɃ´ύΪʳď0¨\x8aģZӿҥӕж UȠœίЊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϦǆąƻųqǤұĩь',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͰǾȓçћӋ˨Гǌ˄ҽҦǼѐϗӽЄͿԌ͵ƽ˧ʹƓǶΌƬԒ£Î',
                                                                            'ұ˨ǥýøĴƹŮȣLȗÈˑƮǃԟýґԊĨǂʳǼ¶źшx˸ŇǕ',
                                                                            '˨ɶ6ˊΔŚʒ$ţ¡\x97əӨƝůӵΉſϭτ8ˀÛ˒XġЦ>ϺǾ',
                                                                            'ԃθҨƲɛƄ²ƤΌѫ#Ύϴʪǌć¯ēå˱ОĄōϰι©ǨɆѷô',
                                                                            'үϨщǂŹӯӌοǳwŀFŲс˚šmσƘ\x8a҂ȧɑŕqȀÈЛͼͳ',
                                                                            '³ΡʤϡаþͶˤʍïʩĵƄŲԦʀčʾ´ņԦԌʀӥάƑѰ_Ӈԁ',
                                                                            'Ωƕ<\xadȸшŗҕǩćͿ¨Ŋəɟʐ\x91±ԒɫΌГþţȖԡ΅Ҡөў',
                                                                            'ɞɷεӢԮęөƽҍ¢ɡџ˦ǒŌǳΜŬÇˋΓ˝ɌƳ˓Ɨťǃԉʬ',
                                                                            'ĪΉȝϻ,ɒʘǋʸ®Ӹ\xa0ԠɄǇƱȟćœŖщЂʊѧǁŁΆƾӈ»',
                                                                            'Ζьǻŧ_ɌɏκΚƕͰȠȗΗԞȝβʉƄ\u0382=ȏЖ˒Ԅ˪śλ-Ҭ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϸкДΚӠȯ˦ʏˈҶą\x95ŗ6Ə\x8dԏ϶ζЁ¾ˠґ;ƕʦԋӄљύ',
                    'message': 'ұѬʊӈŏЊщͰåˬɥǛЋҪƿͽźшƺԝȁӠ÷ʏжȴÐϤкϔ',
                    'arguments': [
                            {
                                        'name': 'ƒíӫҖ×ҥŴ"ȰǓ\x95ϭӦӱσѮǆǿȑ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.052255:+0000',
                                                                            '20210224:164101.052301:+0000',
                                                                            '20210224:164101.052310:+0000',
                                                                            '20210224:164101.052316:+0000',
                                                                            '20210224:164101.052323:+0000',
                                                                            '20210224:164101.052329:+0000',
                                                                            '20210224:164101.052336:+0000',
                                                                            '20210224:164101.052342:+0000',
                                                                            '20210224:164101.052348:+0000',
                                                                            '20210224:164101.052354:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĭ±ΖΘɸɽțι;ԩԃʳΧ˧ѠρԈӖ˗·Ͽѫ\u0381\x8bԍĘ\u0381ϋ˞ԛ',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʮňЛșɓȐđȬˮӃOԩ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.053487:+0000',
                                                    },
                                    },
                            {
                                        'name': 'κʒʚɛҐǥϡδ\x85\x9fįΩΥɣ˃ˋǕˇĔΔɘʶY¢6¾#ӔҲϖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.053650:+0000',
                                                                            '20210224:164101.053662:+0000',
                                                                            '20210224:164101.053669:+0000',
                                                                            '20210224:164101.053674:+0000',
                                                                            '20210224:164101.053680:+0000',
                                                                            '20210224:164101.053686:+0000',
                                                                            '20210224:164101.053691:+0000',
                                                                            '20210224:164101.053696:+0000',
                                                                            '20210224:164101.053702:+0000',
                                                                            '20210224:164101.053707:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǜõϝʹÁѼȀТȃԅθ£ӗϑ\xadЅӕØДԌԤҜҝ%ȏҥɵƹЦӒ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˓',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            577573.533997044,
                                                                            11522.04288701668,
                                                                            588080.733347976,
                                                                            585261.3202573316,
                                                                            521754.8489682829,
                                                                            558927.0083562436,
                                                                            297262.3171102592,
                                                                            668342.7818978388,
                                                                            97549.25731336005,
                                                                            336048.3561604623,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϱǎӫѽԐȡüȄĞΏƂўēʦǩkЗή2Ì\x83ʪԒ˶ȎȊǰ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -273636653785003021,
                                                    },
                                    },
                            {
                                        'name': 'đѺɭĎͱļҢȣƒʣŉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϡ^ӯƘ˲ѧǍϹPÄԍǦǕǔʨԔϠωǮɖ ưӏΆɱıȓÓ˜˳',
                                                                            'ʈËʃÐЉ˕ÚʗĈҊʎȿНгˊ¿ǖÁ˹ƠҁӹǂΘөuԞҌÎȭ',
                                                                            'áΖʹҌԟҌԕы³ɬ\u0379ˍЩþũϕӼԚșӸ4$ǌɛͱΠχ˜ʳЫ',
                                                                            'ƴҏ˂ӥſĳ\x86ʰʌ˅ħˑүӻϻѤѢƧJΛӴӲȘȏЄȭĹƎτҺ',
                                                                            'ӣѧrҏҫɉƔʕ\x7fŎǬ¥ƻúƈ˶\x9dƮʳΕēʡĿȚԓ˵СҒūŏ',
                                                                            '\x94Ƥ¿ſϱϥ5ЕșҒɷҷȨ˃гдѰӁÖ\x90àШʪȗɽԁʹΈчǠ',
                                                                            '˸ó8ɅӥěĖҳ¸¨șΑȒʇҀʚjѭƆсɷҒɑӟҞĦƚȟҦЙ',
                                                                            'ƤʱԣҴƁ҈ˑʡα!kąɕѝRΥfĔΞŴϦʍҙɝ»ԌϺŜƀϓ',
                                                                            'ԪʬùҫƐέUӮ{π˜ǾƆȝԁїԐňǀŧҗ\x87}˜8ǷҘӭí´',
                                                                            'щ\x94ǭPƛɦˊäǝƺǧԗǲλȃї˔ҬiȇӀÌȢɉZƱҝβЩΞ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŀȌɠӉɍƲ(Эƛԕ\x9eͼЦҪӫȞŞïaʇӈƐ~Ȗ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'Ĕ£ɟȬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.055282:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ėÖƤ\x91Š'\x83ʂLÜsϵѸçҫƕ{ѵɌŝǩĭěϞĢū˥ҙԖA",
                    'message': 'ǥсϴΓԛЗŮѿˈҬѬ˦ºɧǂȣͺĳȌ˼ǁşő\x82ϗԮŏξƶӾ',
                    'arguments': [
                            {
                                        'name': '˹µЧǤȘԐ\x9eǣҎЎpīʧ\x8d\x8cϠǕΠĩӘеɥӇϛȇАиĲȓɽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɿæӉγìөȴԜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.055915:+0000',
                                                                            '20210224:164101.055929:+0000',
                                                                            '20210224:164101.055937:+0000',
                                                                            '20210224:164101.055945:+0000',
                                                                            '20210224:164101.055951:+0000',
                                                                            '20210224:164101.055958:+0000',
                                                                            '20210224:164101.055964:+0000',
                                                                            '20210224:164101.055971:+0000',
                                                                            '20210224:164101.055977:+0000',
                                                                            '20210224:164101.055983:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Εʜϯӫ$',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            781632.9406308391,
                                                                            -76453.7482911378,
                                                                            825941.3716873516,
                                                                            66656.93031888045,
                                                                            747325.366756995,
                                                                            337427.02193929156,
                                                                            513417.316848265,
                                                                            422947.65277226816,
                                                                            521784.6924856311,
                                                                            659348.7960969495,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɥϙϦɈ[ɵϒΪȔ˧О҃ɡбG¢+ȕŨü',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -467346320360672600,
                                                                            3792762142834883049,
                                                                            3923764706280406910,
                                                                            -2065692262611897232,
                                                                            9191291035793536360,
                                                                            5742530567746004193,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǎĳΟҖƬ҈ʯŜѷÖԀǵęвҰɛɥӣªΫȪǑʔdǗȝʛăʤ@',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.056721:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЀÖǻɇԣƪqȓtɔ^ǉɩɞȿёʿˮŅƉӿʇ\u0381Ҍ\x9b\u0379ϒĒϭΗ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5180007596816247531,
                                                    },
                                    },
                            {
                                        'name': 'ě\u03a2Ϧɞ"ϷixĀԜ\u0379Tʲ¼ʎǸоʅҀƙи˖ԥςƀѡ\x7fʕф>',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ƿš˅ƾōǨØəȩ°ѵœȽҬʽˏÙkăΰÇÂɨǃͶ(Ԉώƴˡ',
                                                    },
                                    },
                            {
                                        'name': 'ѾȕЮFińò͵VáˇʞϯъЌ˯ΜԊ²Ӭ|łƹƚτƥ\x8c¶ʧƪ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˪ӟ҆ҐjŸО~πéɭǇ˨S\u0380ƃӘӷȮɮë˒ʵʿӄĜˈbȩť',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.057451:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƛϗ¹ѬÔçɈǁԜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'žSӉȍũ\u038bγ-Ʊ˭ϸïɮʫěɋĳRƩҗҖŪєɶąӦǒ+Ê+',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԅȏĺŉǞϰǅĻLϓȍиРɚjҰғӳ¾мӚІƪб\x8b4\x95þ©ͺ',
                    'message': 'ȧњĪŮǳîӼԛҾǅˎûБĦэԄоӼцӲəτІķǧýȃӀѿӆ',
                    'arguments': [
                            {
                                        'name': 'Û\x82ĿӞȻÉӖѪŘëӓ¬ʨSūĭɬʋƂΖʆѱǩЫӠĪҤĩϭҺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Νʎ9ϭŞԬҝ(ϩҒǯƐѡϊũƷʄʹӹƑЕο\x97ӴƭÔԜϻĵι',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɤӄǟəуԖЙͰëŒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.058456:+0000',
                                                    },
                                    },
                            {
                                        'name': 'åˇҰѼȲȸgƽgüːӚĶƝ6˰ȡӰӫHƪŜ˯Үҍź©',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'чԏϤλÓѝ˭ɽӄЈɛįƶҘȢԘԫǄ\x9fԘļá\x8cȼʉæͰȜƦ\x80',
                                                    },
                                    },
                            {
                                        'name': 'ĜȜGϤίiύ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҖӌηϾɇԋϫϹ˝ǃʀτ8ғʉ˺ѱЌÐѧªíEɏœԅʬģѼέ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 925185.7403951631,
                                                    },
                                    },
                            {
                                        'name': 'ΡІÕСԝüҶʾɎ˲ƼƓТӦˢȖĒνˊϲ³Нϑ͵ӧÛÇƽӅk',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            823443.2000228125,
                                                                            62859.91850366519,
                                                                            572970.5066677158,
                                                                            40555.82809899887,
                                                                            936903.4731267062,
                                                                            -9914.246251040284,
                                                                            888826.095618927,
                                                                            424225.01059288986,
                                                                            18193.521494840737,
                                                                            899587.6741980771,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˗˫Ѵńӓѡ¥ΊϻɹƕԬӉˋѝĆǡђиŋĹ¤Ӎ ɧǝԫǱćʙ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԃŌұˢӘȔϭůǈíԀƲʹԗɥ҆ѓɁ¥èйêľǔǺŇˮȻ˘ê',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1169648512130844932,
                                                    },
                                    },
                            {
                                        'name': 'Ǘ}˶α˽ɬ\x94ҖԠҍЮӆηώЩ~ǌɒʸ\x82ˑɩ˼ϝR\x9aƾȳ\x92¤',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ãΊПú®ŽËϮԬɈˍˋσěɘēӫïдЊʱϼĩƀ˔õӈƁΤ)',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˨Ɛӑ\x96=Ņͱ\x86˙ЦǜΛɈΕ\x871ôǚфƀæЉӢхԐʗɇԪқ˅',
                    'message': 'лЏȹӑɣǹˇЭҬuɎɾZdѭɥǈүϼ:ȳʏÙǣеì˯ήƷԎ',
                    'arguments': [
                            {
                                        'name': '˴ǛϏ¹ӐŸӖnϣǼ¢ŚVĘ8µϒɐʪºΞ\u0382ɺĮȨ\x83aņÞŲ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 888670.1757260406,
                                                    },
                                    },
                            {
                                        'name': 'ɞώˌʨЩˎͰӤϔ˜ӎɨɇȯĉέУѿӖӒӄʘӊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 918694.8500177055,
                                                    },
                                    },
                            {
                                        'name': 'ʽӮ˺ҁГ˨ҵ\xadǧȦǂŬʖĥҝʴ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѝ\x82ǁŊфƴʛǚάˋɮƷͰ˘˽ǘEϪ\u0378ɏʤȼ2ƽЃŖιɍŶЙ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɐ\x90Lǜ\x9cҧӞˆƘβȜ24]ѥ˥ӳϘŊȸù΄\x7f\x95ƲψΦʕǏſ',
                                                    },
                                    },
                            {
                                        'name': 'vĪʟϨϤĹʐţӶӺԬʧҝɀˠӻсǍϊ±ȸІǒљEԓʇЂņı',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5326834350057316930,
                                                    },
                                    },
                            {
                                        'name': 'Ӣԇ˺ǀɫ6ǇɾӻѳĦªǍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 696849.5958551813,
                                                    },
                                    },
                            {
                                        'name': 'уȏӔŨ˵',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӘѶŧȦѰϛͽˤҕƭƸχ\x8cҌˀˀ˝\u038bɉӼѿɑŷʢ˼ľġˬ\x91\x8a',
                                                                            'ѝЭƍřǍƾʷǐ>țԫԒͻϤрӶʹˠȡХсʔǜˡэЦńʷāƻ',
                                                                            '»)ҦʛɪǛԀҋǗʠǂśңƃĨАϘӋ˷ҵɜŤáο\u0382ɥVο҂ǝ',
                                                                            'ϤСɵβцӣθʔɗ˯Ԝȸӄ\x8e.ĄĶǗɑɊŻ6ϘȜӑԀϽ¸Ӎÿ',
                                                                            'ɒɨȥҞϼ¢ХвåɋƱŴϘʝΕȫӁʃˌɛκƧŅɨĉɁӛr}¬',
                                                                            'ˣεƭʹӎк\x80ϯЗ˜ȮОȋϲŢǦԋЪѢǭϺÐťũϱңϡɜӺȠ',
                                                                            '\x86Ьʹ²ɍǈӿȶΆÓЯѧѯҌyψŊѧļýЀξѷҲʜСċӏÍϊ',
                                                                            'РдӁʻĚ_ǓȝƁÉӃ˩ƎӣĐǮŝɾǮσñȴϰɘɕŘóԥȏ\x93',
                                                                            'r#өɩņď\x8aƴ%˧ɼˏɹʏψҧӗԄʛǪǾʁϨɪȶџǂϪҳˊ',
                                                                            'ԉϭ¯ΞԂҍQɀĮ˳š˫ɍŨDòĞжԣˍƁԠӹӇˡŉԘ.1Ȩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'jrиӻȫҭsʝƈŰűЅϬѮѕȜiǗ˶!ϐɒ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.061375:+0000',
                                                                            '20210224:164101.061390:+0000',
                                                                            '20210224:164101.061398:+0000',
                                                                            '20210224:164101.061404:+0000',
                                                                            '20210224:164101.061409:+0000',
                                                                            '20210224:164101.061415:+0000',
                                                                            '20210224:164101.061420:+0000',
                                                                            '20210224:164101.061426:+0000',
                                                                            '20210224:164101.061431:+0000',
                                                                            '20210224:164101.061437:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˵rˁ\x8aĕəĿæǅΥбѓӟÍūϭƂaӽɿΆ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӗǍƫѵƽş\x93ξΓ<ɬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            422706.71945574373,
                                                                            155015.29832684132,
                                                                            736909.7105868974,
                                                                            370629.9129376734,
                                                                            982242.6869290252,
                                                                            118711.74991661301,
                                                                            785479.4532931843,
                                                                            377178.8594218842,
                                                                            16108.914177326456,
                                                                            684734.1958911697,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˤ¼дŬГРǓĠҢΪFЌĬҥԁҒΡӛĐ˘\u0380ѥɉȯнĨȖ˻ʭϼ',
                    'message': 'ɝѮʋŸԪƤѭʒ)ύÊԬӨȐίǵФӥѶǑˈ\x86ɽƜˋξҲȬФӳ',
                    'arguments': [
                            {
                                        'name': 'ňѽʭͿ$ʡɯĪĤѧѩÉыϹҎϻʷҫ˙ɕƍŊѓȹҤҠƍȘ+Ǳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            897903.5540661883,
                                                                            307514.7510287618,
                                                                            746170.177440067,
                                                                            356603.8571644276,
                                                                            -89214.1608739066,
                                                                            170215.60908488295,
                                                                            670077.5811614026,
                                                                            211586.18657230196,
                                                                            306522.9913853501,
                                                                            832411.2790568355,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '®rԚѠjªłˊȫŞǯǘöŌΠIξǣΩƽ\u0383ͱмԄuԔȂӈ҅ǆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3312438957944051097,
                                                    },
                                    },
                            {
                                        'name': 'Ғ˪',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɦӑԣȁσg\x92ӳłάѳҕķЏΔʿʆҫЀĖΝѣʉǊѿŲϸ¡Кˠ',
                                                                            'Гӛʹ}ѝЊӠӱdʝıĕʬΕʑӥӛģѳůчUӓҐòʵġǶхϘ',
                                                                            'Ӱ#aбѣz˓ЈÆʯѤʌʁþáʒłǯŽϡӛŜǾvӽňʯīхҡ',
                                                                            'ɷίǋАƝʤýɳ¬ЖΚOĆǏȘȏν˗ӖųҞˊЏƼɢӭłИķȺ',
                                                                            'Êт:ǃЂ˗äϽſɧˢџY΅ԉԁ˻ϻі½Ɠѫѣ<ǞȖԊϱƣñ',
                                                                            '\x99ͰӑѢR£ΛͲӊƧũѠÁѷ{ΪɁǋFұӋӻÜ6яƉ\x84ŦˢΖ',
                                                                            'ÌƨθѨԉλьʧƻ_ǰЕɶ \x86ιʀκȞ˨ϾƄԏˑЧǤƁ˭Iˉ',
                                                                            'ťɇæɒюmӁěɨ,Ā\x92ғɗ҈\u0378ɴȬΥɧÍ{ŝƓ˺ЀȣƁОì',
                                                                            '\x7fэŌɷǭǣӀǤÔĕϳЙѴɜtĶЛǂ5ΗŃП\x8eǄȞЌüʏҽ϶',
                                                                            'ÇԂҋĜӿ.Έӊɱъ\xad҄ǬɿŠʥżɁʐ\x7fҴϐϻżԀʆЗ˂ЃҶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЪTƃ˂ǥſΐ˶ȤϡĮҩIʬĮǗȲîүȥ\u03a2ɖʂΒЈ\x9eɱкϽf',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҡȶӱΥƫʈӡɴ\x80ɩʦӯҐȉǸԗªɧъЪŵɚĤËЛŽӻͺˌҺ',
                                                    },
                                    },
                            {
                                        'name': '\xadɽΗҵʍĄȓ\x9aʭgγȉŞûI˴¦ɦƀӱԒȴМʿҨoϗǎĖω',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 810725.3683872386,
                                                    },
                                    },
                            {
                                        'name': 'ů\x99ДȝƱɈűÚѸĄϖʘ\u0383șϟʥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164101.063558:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x89Ɇ',
                                        'value': {
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '´ȾE\xadϟ\u03a2ÉԉӃͰȝξσЧȔʥȅÓϠƆмĳĉɔϨĖДÇųӣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ȂҞÜϸιɃ˽ãpªϑǮбǰҹ§Ӯ\x9a\x9dƿ\x8cnѧɍͺΑѽԖɽk',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            95942.80138287653,
                                                                            520797.3413125932,
                                                                            808804.8509813986,
                                                                            407054.999699815,
                                                                            754900.9764254185,
                                                                            276195.08519874455,
                                                                            -30331.62227795113,
                                                                            488396.21378629026,
                                                                            -87715.62039000026,
                                                                            368497.5770360501,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ƦƷϝŞC`ѝɬц'Ӆƾ(¤σӚћҠǵ/пѶɐϦtЎ\x89ű+Ҡ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164101.064417:+0000',
                                                                            '20210224:164101.064431:+0000',
                                                                            '20210224:164101.064438:+0000',
                                                                            '20210224:164101.064444:+0000',
                                                                            '20210224:164101.064450:+0000',
                                                                            '20210224:164101.064456:+0000',
                                                                            '20210224:164101.064461:+0000',
                                                                            '20210224:164101.064467:+0000',
                                                                            '20210224:164101.064472:+0000',
                                                                            '20210224:164101.064478:+0000',
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

            'identifier': '\xadӔǣǞҘ',

            'categories': [
                'file',
            ],

            'messages': [
                {
                    'catalog': '¸ʇ',
                    'message': 'ú',
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
            'name': 'Ɏ3ǆΑɭȳƫƻШËưȵǦΚЫҨьѽŷŧɃɻɚGЦӁ˚\u03a2ªΪ',
            'error': {
                'identifier': 'țˀϘǪȿȈӔȟӓìҴƭԀ\x85fʖŉ½ԛΦ˫ΙƱɅ˭ǇԑϊԬԄ',
                'categories': [
                    'network',
                    'network',
                    'network',
                    'invalid-user-action',
                    'network',
                    'internal',
                    'file',
                    'file',
                    'invalid-user-action',
                    'os',
                ],
                'source': 'ЦěϹ˙ϱԬЈȻзƋы\x8dΚȨʶŽˆ7ǫʩө˺ӳЅÈӋҲӔøϗ',
                'messages': [
                    {
                            'catalog': 'UƖȷÂȳчҔɵÚŀɓȱбӽķЉŃ˦ǄþɱĔúɂϩȳŏ§ŶЁ',
                            'message': "чɫӴɓɜӜƜĊƽϠȜϱ\x97Ы˩ҧ'ǵɆǧҘ\u038bʍɽЍτҕӘ҃Ӛ",
                            'arguments': [
                                        {
                                                        'name': 'ƀЀĵӽɸMίþXÛŌЌƮɓԗϵŪʤφˍǊ!ŸǍʝȁӯ\u03a2ħΞ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2724575519571195369,
                                                                        },
                                                    },
                                        {
                                                        'name': 'όԢªЊЕƚӳԉƖԣјȓʮκʲϜΓƀς!ĠT<Qϑѩѫԋǚǩ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŲѪÅŒһƠǁˊ£ƨΎɱҊ\u0382ȭӪĿɞ\x8bѨԁå˺ǠŚJѫҷŤŨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'êɽΎцǪaԕ¾ĊЌÊˢђċȺӕÍǨƀɈʂǲȵQʻǞѠ_õƝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164101.003848:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆʌҜɛ˙ũȬҲưϦӣвΨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱ҉°ł%ѲԤ·ȣϜĥOʻӭґ˚φ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4291761512313524899,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇȱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'υРθпʁɾȲӋ9ćʋ\x8eˤĆȏǭİƞѯӮҁӍԆўª}ÈӦцԎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '<қ˃ŹӍyÄʄʢԬԟȭxŶȉϷǍюјԁǬӇόҷ˂\x81Ș\u0379ŲѲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382ѫƥǥѴəΕ¾ƤʃǦÃûǝѹǣƌā',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'kĽԄöǛԈȋͼϏϖƑʫЋÕɀɤԖԬŷǳΈ˰ѳƏȷӚӹÏўѫ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĕt=ӨŜČÈÛМŅñµӫƴqĸΘːăÕªȠӤǪԒӲŋ\u038bѨl',
                            'message': 'řƷӒғѼĝʑĳĠȢw҇ӟщԐӯѭɏŖ˔ΦԪʘóÒÁƅѐҁӂ',
                            'arguments': [
                                        {
                                                        'name': 'ϟΧƚǯ˘ɏ˩ҙRмӫΩȋŸɤβɺˠV3ѯ·ʑІʫΗӞӕϖʲ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǥ=҆,ΥóɄΛuɿšȻөӼӐϸɥˡ´ȊėθƨБį',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϱʛλť\x82Ůĳˎ˲ӄԆʘˢ`ǗɋϪӀŇŶǺʓȬǳ˖bʍƚrŖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '÷y-ҫȾȅΔɘĥǍďЫɤҿӵÜˑҏΩƴHħï˲ѐ)ϪηѼш',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7072051820234109958,
                                                                        },
                                                    },
                                        {
                                                        'name': 'θǜҍ\xadîùΫåƦïі\x9bͻϴ҆Ńʽ˖ҳѢΙϵЈįɔƈςҿǞÕ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΐoӊΨѠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҬϯϜȺӱҜ҇ҥȁϡɵʩ#ū˫ǾYώBɮjйάćƪӁҺҬΣȄ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¡ƄǕԇɠ´ǔ\x81Ʉ˭ȘmČņЙԖȄƎδȭȭӡƩ϶ɗąǏњˣѭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǙɆΝƿԝЗӯØƫʎʒʽİ˦үΈă˕ƫ!ǹʄ˱˵ӖԢӶѣªϼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 692760.907031181,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӻë\u038bγѓΧňģĵӺӖ˝ɺ@ąʠǉŵҮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4457358620647055249,
                                                                        },
                                                    },
                                        {
                                                        'name': '˱ӭЬ˞iɕμԄù˷ƭșЧ\x90Ϝ҆ӕӀЄɔ˾Ġ1Үşɦѝɦ¼˻',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'РĽʍԛ˷\x8bĈ.(«М0ĥēŃ½σ²ùχώʼѓȘÁʇϔιεϾ',
                            'message': 'ɰı8ɊǝВпʭяΜПƟīʦ˳ŶƬ\u03a2ϐФÿЭРȏΧ;ãʇҲͷ',
                            'arguments': [
                                        {
                                                        'name': 'ÚÙǝдшω¬ƱùɧɻҍƝOÙЁjŅʒΞҜӸ3@\u0382ˌ_ʃʎ/',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ª¥őəÑŘŪƀȞѴԆÔȺȳīʗѪʬ˝ɘĬňϭЖȣӢѹƤ9Ų',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164101.011796:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ХӅДϛӾȉƐǸԝρ¦ώŗȰԞĮǄϜŏ˅лǵӌêʵ˗ÒʎɯÁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϠƷnԌϪØɶ˻ĥйʐʉɝ]',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȩ·žҼϸĽӣ˾ӹѩŧʈȁѶъ\x84ȭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҦӪԦϻ^ЀδŰßϧҬÍϢԦˀ<ΟɘМ°υ˪ƍǶČΊҡѸƎӷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'üѱ>м¾ʒԪԤ˖˥˹ϝħǒ˥ʯӶˇǒ\x7fº',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƃϣZRŖӇ\x86ԕшԙßɟϨ§ʗȀаԍb˥"ʫëщŴĬɴǫûϹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164101.013652:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʪIΙȄҰ%Ǹ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'āǟǕи˲ϖÓƊ\x99ʝґсïυMΟƆȶƙȂǧƕӼѷӽϓȼ1Ӥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '©ƸaǦӛȭͲԐ(ưȲɄίԦ\x97У§ϣϨ\u0381ԇȠʵԤУ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5945159398621488952,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҥҩÊƱИҪȏ\u03a2˳ȱňу˲ԕɉԪġ"ӄѣѼʏɸ½ҙʹɜźԪ\x82',
                            'message': "YЌѽͽЯӟ\u0381Ƽɯȳ'Їİ$ɵ˯ΠўɕŽнʇ{ĆǸŅϫəʀϒ",
                            'arguments': [
                                        {
                                                        'name': 'ĻƁˣԌũҢҩȚγ\u0381ϗǥÈƕ/ɿԖӞϨ.ǫʨÙ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˯ĭĽ;ύ\x87',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 923057.1618004169,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Гϋлƥʻ¿BϓʊÜŢɑ˯tϤƌ˞ҎʈӁĹŦҿāĂǂ¡',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʍѨӵŲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԍʿž\u0381QƸʷŇŞ҅ϩԞӆǛѧüȮĨơϭɣѾɢӉԘȷȁđĺĿ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -303055694378886930,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '%ҮвϖūеøĔŗsӖʉҊfӮҸƲԪȥрƜǧΒΓƞɛωԓ¾°',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÅzщȳϻȂˎʇ˲Ϥ΅\x9fƴΙgĸɎӲԦ˙ɧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮϮǢĎ˛ȞԙȠ9οŗ<ԆΌÖϩƿθғʽϯ|ѩɻ˲ԬUͻй˷',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҇',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164101.020816:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ơ0БϤʞΎƢѨԬϱayϷҌϞўǶğФƸ×˛ҊԒЮƟǑ˛Ѹʚ',
                            'message': 'ƙϜĐԎɺКʀԤƢѴȿě5ʢЖȲŤ>Ѥu\u0383ǇԆůRȭƞҴ4_',
                            'arguments': [
                                        {
                                                        'name': 'ʈȀŦ_ӋŬǊЀ\x87ЮͳÿͼƘw҉7;ǰҵȧ¾ΘԜ{ҙЇҬ˄ͺ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4564684249208247,
                                                                        },
                                                    },
                                        {
                                                        'name': ' қįƛϯƚŤʩï¸ƈĢΕnȯІǓsʦϱHüԇȖɌљʯƘö҅',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎʐűҸǦƋұԕͱǀԄРԍϼ|ÉІŚÜϴ)ψΞâ¢ĚϣɐƈÚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 704015.4348884597,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΥƜšӈǖЅDSе¼\x83ĴĚ£f',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164101.021957:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑ϶˄Ė²ØƥȸƅϠ2è\x9fɜԀҙáʭ\x9aʆћ°ťˠȗŅĨҬͶ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '*ĬщɵÁɼҰ{ҕʜGӫHȓμčσГ\x9dxȵΓ¼Џлú',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȸ˭ʘ¹ȣɂϦĕŎ×ɃԒҵѩǷƁƞ˔ѭȦįāăǅɭѥȏcǪĒ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Йϙ3ŮşŚĸ(ŋɻïǯНĔӇ\x95ӰϩŘȤġ5ȿJͳİƆϥȢʵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˩;ӵȘŒńɏĴɶП3\u038bʧӷФԃӷ~Ǉю˷ȿɱȫȺǬɯ.˺¿',
                                                                        },
                                                    },
                                        {
                                                        'name': 'çβӋ˥ŅŸěхϞ\x9fƍQȐң˾ʤ\x9c\u0378ʍ1ǴёͷȤEЇԠȂͿӤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˦Ȱȡǉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƂԀƬÛȠǃѠӣЏЊğã\x9fжԥ¯Ă˭ԫŤCҪɜňǕƣϛ ϥC',
                            'message': 'ǛӜѕ˸ǥřƗˍҵіˈ:Ȟǽŏ\x92ȗŠщҲƙ=Ė˞ȋώșͶԟѴ',
                            'arguments': [
                                        {
                                                        'name': 'ϟȂԏТɲ˩ōҞŲHΦέ°WˊӡȳО˭ЃӑƘԭ˯@ӨŌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ĹʓΠɁҷʟцĴNñϣµĴȷŴÔʠGʹ˘ɢ'ˌ½ӕŜ˯ÆˬЉ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ъΕɖȥáаϭΙТĕ\xadΠҾ˟ӱɹpɯԒɅ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӊўө\x84ʑ\u0378_ēΦʠɪӺшÚΚ÷ϸ˪˫\x88ŗ\x97ϹɴαК͵ӥɻѱ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƵС)ɵʄřƴǠΛʩD/ɻˇƔƙʵӍХԩȡȺOȗƂΨǕć¾κ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӻǇǇˉÜɑα˲ʙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 752312.888583999,
                                                                        },
                                                    },
                                        {
                                                        'name': '˫Ğɼҟ³ǒȇӠĂȬσáĵҘɗҀжИ¯ȜÃĞµȉԚќРӸ˙ǁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'KƸuʊϞƹЃ·ŎƋ΅˳ͰӾϠҸÝĸБԈ|ȵĦϱʽѽyϔц\x95',
                                                                        },
                                                    },
                                        {
                                                        'name': 'eΎӄ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɃəзѐʬҋǴđɀ˸ϊɋ˸ĠµƬҖˆːȔŽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'yԈʰζʩɄVϫǵZƏ¹',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7786224403002642697,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ťҲ˪ͱϤɖһƳЁɒƇȝňmК\u0381σǋȧnàSӂʊ÷ԢĲȦϪ¨',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164101.025271:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ДіƶѲЂЦϴ¯ўgԣύʾԌĎҷĜȧӃđʦǯҢɏƏEàÁЧ˔',
                            'message': 'ЛȞщχʊʽˆÄʆπӇʫʣЄ:ƘοɎxǎͿɺȢŹлȩёȬ˹ӷ',
                            'arguments': [
                                        {
                                                        'name': 'ÁǆɟΑæћηɫǐЁԎҠ¶ϱ\x94жʕЋԟȶάґʒхΊxΊ\x7f',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7823837155890177745,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊϨUԗČȱЋĂƙ¼ңǘH6Ε҉ϳŵЊӴǽӈӉχǮȻȧǩȝϟ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'è҄ɐ°ʂЊʬŒǀxǻʈůέɟŇȝÎr΄ºʗ˲ϖǿí\x96ϼș',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˴ø\u038bΩÂӍ\u0379ȄƝ\x85Ȅ¦ƼӬ͵ЯӷŜԚǐˤĴҧΓ½ȴĢĂƅģ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʡlȐόϹʟ¢',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϿΠƈȂС\u0382\x93\x93ǡȂŤ\x8apҬ¢Ɔæûҝȇɫъ҇˰ѯџʛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164101.026476:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ш',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8aĹҟ˨ΘİηѠ\xadȱЁ-Ȳʂ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'SʻšƀЊφҜλϙʟļɀǿ?Ҝ\x9aƬІ˹ÅǙű\u0380ȠǵʄêÛÔɕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʯΉʶ\x93τђɥŸІ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԭʖԋƴˈň˞ƪ+ʵҙԩȢŒ˸',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʚɂ˃<ɯήõȕɄêѻΛгėӒҧ´ρΝяӍЯѨ\u03a2ƨ?ȺӼäƋ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȥ\x80ҽ˹ȥɍɛζӋɘɧѨ=ϧȊтЪќĸӓ҇КĦȁɕ\x92Τϔʴĝ',
                            'message': 'ӿҝѸљʌίшɴȤӦ˄ɝZʳˉѢˑˮ\x95ȑҼϲɌнȬȏǒ¶ȇщ',
                            'arguments': [
                                        {
                                                        'name': '"¡Ϩ˦˸їʂϠǌӖΤɯI\x89ʴ.ǙĽ˸Ԙҽ!ʸǺē\x9cЕŖʏϚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ιĥˈɊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŋǵ\x7fʼ˭ѮƴѤūɸɭƺҪȳĸӕ˴ԅЖσȹǱåʱӾĒŁԠӏв',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'DШéçǖШô´ʀțǊʻŊʸϺϔπЈрӱʝҖƣԘʵʡȢŮìƞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԄλųȏӘ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǦƵˇȟ˴ū',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 68665.48309648165,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӎȡ˽ǪĵԒ˹sˇӘȖˎ˥ͳΘǳɪϨƺҬŨӉĳԚЅбОƐњф',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԣʝςǃϔԩșӥ\x82˔ĵӏʝÓϋŶɃƯÒѓíŚҼƷ]ѹ¤kԬų',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԀʼåνȡkũϧҦʸӜǲɭԐұȩƛϻʖƓ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԘŸƢŒʈ\x88ĩѣϢʫԂʠ¶ƶŜ˃pҀ7þϳͰˌψҨԞɧĪ˪ѻ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԎȈˍʇӭԌ˧ɎњЪҮů¥ʋԓÍȉҙƲåəʼģÑˉΒӠɍȧϻ',
                            'message': 'ϟґŎҬΊǈƤΦƳÀʮѰԡͻл\u0380ҴΦΡĶ"ÄǤӬŞ ӍԠȓƺ',
                            'arguments': [
                                        {
                                                        'name': 'ҬȘ)˜ǞϤ0ǳԘŇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӶPβǐ˜%řǰʧʠԐ¸HԡΝԘLӫƷ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 416242365512670806,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҜȓǓԫЏӋǤΉȴCҕ¸\x96\u0383qάΟʂҟ˴ѷ˓Ϲ;ԆͰƯʔϫǍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÕȗӮv˄ɕůśҕ(Ͽѵl=ǴѺԠ˧ɉÏȸũԁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ήǢϒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164101.032258:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌdlԗĈӵӡҪаčǕȩŪɄʯӨѮʤ˒\x87҄˘\u0380ŐҁǍȃϬĲӠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 129728.48687337467,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƙǀ˰ä\u03a2ˁ˺¼ĪϬƈ+ʐǵ«ÞŒМʄɁЪӉ\x9dšґP=!ĆȊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 110559.22553357968,
                                                                        },
                                                    },
                                        {
                                                        'name': 'яȖÉ\x97ȽѽЌĠњŗъЍήǰǃ¦ŕȿюȾȪʹ\x81ϷbшǜȊʧϣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1655814535974981948,
                                                                        },
                                                    },
                                        {
                                                        'name': 'пƲĔ\x7fҬƳɫxϫʱǽɋҿđȫѦдy@ČÓȢΎԬмĈÙȟŇ´',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ïÚʸb\u038bLɯЗǴđ˘˂Ǟʱ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϲЀÃȌưҒǅĪԋȭЏɖͻϾҝʢʎёȍ',
                            'message': '\x98ɉӭĤŅŊƭȻ\u038b#ʕЮºǈȺҴçȍ\u0382ċ´Ԑҁd˙Ĥ&ӺʢӐ',
                            'arguments': [
                                        {
                                                        'name': '*\x8bɻŅȼҪоɸǒď¸Ҧǉo-ɐÍ҉ʥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϿʹÑΖÞǖǵvà0ԂԬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8036985347299440771,
                                                                        },
                                                    },
                                        {
                                                        'name': 'íqτӅ\x96ɂΛo϶ΦĎӇŏѠΰ7ĿЛлŝӱʫ¯ȏ¾Н\x8cɈņǨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŧԢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷʄϟÄʕΣͻȲά\x82ɨǸŎɆÉƬЍѻκҼҞȺѦʿάȫҥɚŴ3',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԜĤŢö',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ԁčũ%ƴˢԋɓҼǳҰƗË~ˁӃǥӁԕϯХÉ˓ŒȦKҠ˻ɷҢ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕЫȖKϟԣҁȀȗѡǀȎεō˛ǖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʷЅϲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164101.034738:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹʇ¾',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύӓˆŤ§ȸ\x82ӁљθԂɐϗΔҷɇƢ҅ʘ',
                                                        'value': {
                                                                            '^': 'string_list',
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

            'name': 'ВѤȠ',

            'error': {
                'identifier': 'Ǎǋ˂ɿă',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ΠƖ',
                            'message': 'ʓ',
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
            'name': ']\x95ӆѴ˦ԫÓәĤӪʮɶɴȺϦäӔĕɥÓԮ\x85ƮłNńѹ˸ˮԒ',
            'version': [
                -1084859777166914990,
                -3296432301025547609,
                -9142165859011326138,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʓ҂Ԃ',

            'version': [
                -2514637027687953452,
                -5601410379425286533,
                -8910786703095524095,
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
            'event_id': 'ЗƈȫǭɈƔīͽKϾʥǒ˝ТŒҼҫ\x8aԎ4Ď˲ѼÛɄsʛƻԤ˰',
            'target_id': 'ļ˱\x95ɸӡÍҝ@ϥ\x95ҐΤƑʥϛȎŁєωϡ©˄¢ͰȕҕǱҁКԮ',
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
                    'event_id': 'ѼĐȒ°ϪϾƕǌǥԝϿζŵΈĚҩ˧γɏȧi\x90ıѿbÙʮһȥç',
                    'target_id': 'Ӭ$ˤ\x86\xadÊщôȥǟż\x87˵ӖɒΊĎΫåÍģɝЃȣсӭȡʺі5',
                },
                {
                    'event_id': 'ҰʧĐÄҏƱƞҸӷoǃżйǔ˄ϘĢЋЈɃǄEӪ˫âūêŞњP',
                    'target_id': 'сőțˤů^ŪǍѯʾіŇƢωǮѽÅі΅ѩȑӽ҈Ɉў\x813Ƈæӆ',
                },
                {
                    'event_id': 'ӁԇŎÈςΤťс¹ĲҵЗӝԋƖ\u0383aŮšÔżүɍΩʹϫgͶԠř',
                    'target_id': 'ԠԛΪAʍıФ˹iԈåo¸ÍǪЋAǸһΗ\x95LĜϨӀĵͿӬϧƺ',
                },
                {
                    'event_id': 'Zϲɳ˼ʙǕϲUˈΞȣʍш\x88Ӆ\x98ђʩаԀϞɤğȞƆϲϏP§{',
                    'target_id': 'ƴӿкĒćðɇўɁƟȖǱӂʗǽИӯŽúж5ю\x95μĝΏӨɉԮͱ',
                },
                {
                    'event_id': 'üЍ˵ɥ҃ҪԀĠӮŽӝǋƿ˕ԣωДƈԊӄ\x8cƄʸƯ\xadϋ\x8aѤȪ\u03a2',
                    'target_id': 'ƞΐӾðϟϖϼțѲŞËQǔɞϼΣШ}ԏҡȵrёςQ\x84˽ũ%Ͳ',
                },
                {
                    'event_id': 'Ѻ\x7f˹ĝ¬ȊӤʄɕwʟƒҳυ1șҮ҅ˌѵĬȏβǳԘҙTЏÄϷ',
                    'target_id': 'ŸƌɓʴӬɢз\x9dDüѻʛȿǭѴΞιŤӜoœĸѻЖБґș˷ϕЙ',
                },
                {
                    'event_id': 'L\u0383ŇҼvлĀпζ\x84ԬƂТƴрΝʬȜҺɑ\u0383јϯĘP8ӲʽϺŬ',
                    'target_id': 'ҺѯВƉͶҢȎȸЉϧŵ˵˧ɷǺʊʰʹŞNӮJҹӋƢϯӛǬ¾Ƞ',
                },
                {
                    'event_id': 'ǅϕӒʉөʱ\x8dȰӮё¶JԘԔҞȐĎĸ\x8fίʂʔĵ®\x93ΡŶӨʃȭ',
                    'target_id': 'ӑСьȔѧӀǾ҅ɻґˬĻаèăΪӳЉѫ˃oӕɻ΄ͶÃмʺːҘ',
                },
                {
                    'event_id': 'ř\x98nͽǿȳ˞ǠPˋ\x9f˾ϐЈȰςӾKБϷС,ÏϽΡ˾Х\x83ʺǣ',
                    'target_id': 'ҝ·ѾG_ϠѤɉƉǺϟƏхҙ·Äӗmϗňћ:ĉ˰ΏŇ\u0380ěƉĠ',
                },
                {
                    'event_id': 'ʂDʹĥµҖϼӫǥĭcʹïğΎԡԝЭɪɫћєѬǦЎѡɽҖËʳ',
                    'target_id': '^ȑh¿ωԋΘб»ԋċϢԤѨƷƜŸµѧґ%˹уkțϯґԬѡт',
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
                    'event_id': 'ӢԙςԢóé)çҐʴиԣҗҋΟʠѻèѷξ`кŒǝљԚрƐȤӃ',
                    'target_id': 'ƣҲɵˇʯtʩǞυОǪê~\u038bļŀľˍӈӓͺԆˤʛĞˆнϷµЯ',
                },
                {
                    'event_id': '\x81KƯϦѠͽƀοҙӤŪÙѬϱҞд˜ϱƜҮҬ6њňÒǁǐӖ¾Ԝ',
                    'target_id': 'tҠĽ®ëԛЙӓűFŅƕĪbǺʇØ\x85ИҷϖǬ˾ɍͿāȠԒ\u0383=',
                },
                {
                    'event_id': 'ƧӚҪʑԎԈЇΤǺ҇éÜѻЂΌҩƜėээ½ɬõӚǛɼϴӋҷȒ',
                    'target_id': 'ɟіΡůʐ˭ȲͿ÷˲кǝЎĳɷθϼʌνχɠǦβϰĈʿъΩOƇ',
                },
                {
                    'event_id': 'ǇӯҴƺ?ĸȽ\x96ЀeѯԞпǝ8ԔĭºǠԢѕе6ς\u038dþʢӼь"',
                    'target_id': 'ΤșǓȟŻϒ˭ȱʻ¸ҹǫǰiΦƠɘvԑˇŶϕŌЁå&ù\x9bɓϣ',
                },
                {
                    'event_id': 'ʿ¶˫øǷGιӈȠϑϰЏǸґǋюƸϤŃҩɴΩіё¬ǂΖԫЙȸ',
                    'target_id': 'ʏɞ÷ЊÖЦϓɷɧƍҘíюcӻŅeԫΐͽɩӌǿìӪϧUʩΥϮ',
                },
                {
                    'event_id': 'ǹȎӷƷÝҞŚ|ĕԦȕƙǋ˱ҥһƹĭʎ¼ZŝīſÖ[ãЬѝϤ',
                    'target_id': 'ǅI·£ǚҕĉÄȓ?ȱ϶ƝЀǮӐņżΌʘǾЕ˒Ǫ˙ǁ:˺Ԓ˄',
                },
                {
                    'event_id': 'Ѳȵ˶ΐҝͻЛΚǥȅʍӥɫŻӱʽǯǶCӬòŹȨϩƦΖʧĄƒʂ',
                    'target_id': 'ĳƲϟҷƽ;@\u038dƹЊ˦âv^ѫȘmʛǣŅ^υżϚǒԗȳӄΏɧ',
                },
                {
                    'event_id': 'ӹӋȠԎ\x8c\u0380ǼӽƱǈҡϘŖ&Ǖáċǰ΅λʜҗȫӂɯҘƴŚϟӾ',
                    'target_id': 'ϒŏŏʝЯ\u0378Ԭ\u0381#ǒtƪҹгԎЧϜѷÅ˦˚ӉэnЀǗʐ˅zī',
                },
                {
                    'event_id': 'ȵҶĎΟ\x83;\x94ƪ˩άĴłƣTã¨љʐ˫ϩƚƠѡȄBĉӍЉĉɨ',
                    'target_id': 'ҏʿи˼Ӗѷȁ˽¡фәӆ®ÄŗҫNӡ¢ëÃΒ\x8fʶƽþɾ®«Ś',
                },
                {
                    'event_id': 'Ǖǵʗьзңɲ%sġўɀfĻƁȏˡΞˑƉtҦȎj˯Ӳ%ƪÔӲ',
                    'target_id': 'čķһϋʃǘŝȸλˀØйшѨZĠԛϩԔСƾ˝əǟόàӥҹѠЅ',
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
            'name': 'ȑȑśϖҨ\u038bú',
            'version': [
                -1049328835584255020,
                -7107230650874495438,
                -7041084895680535095,
            ],
            'about': 'ĦїҔǡÊӑԥƚџͱʇ˝ԝKϺҔæɸЅ¦ǒǅŵǨǳȓéÇǕƄ',
            'description': 'ʟǌҍ˯Α>цʯǋ9ľΦƆƟŵϋҧȆnÚʘóĺə\x89ԘӷɘϮƗ',
            'authors': [
                'ʪКʦΕєжΎͽ˝щƵʄԥǧӭҶѮʼӗыŬӺdǯ^Ԕáϴ',
                'ЋѶϭɗȢăȕӊϲԃ§˜\xad ǼɞŘӜˬǓ³нƣʣβѱԃтҶԤ',
                'Қ˔ӃʻЍʳɝʦƣőȤƭȃҾɯӈQӪķǮƍθʶғȴѡҳʋȣͺ',
                '\x85ȒƳYҧѰɕȍԖ¿ϧȧԑту#нȴƂ:ҰħӦƎœ˙ωΛƱ',
                'ԗƭӷƠŋҵ`ßǷɅæɸыҎΊȠȓmΨɗӖϗ\x8bӼƈˬÚ7\x9aБ',
                'ŷŨɍӑǹʡÚ˨Ҹ˳ɻǚųŭαϫѠФŘēƕĊ³\x9fԐȆѺϒüԐ',
                'ɚ®ǢЖȟƴԀ4ӛвӌԖƨӛёҿЌÚɒɸǿȴ4ϗғʬÎʷͼY',
                'ϼςӔΝΒ*Ɓð˟ԅńͲ\x9a$ɋƈʑˣХʯʘʕλӗӕ˾ˡҁϛƻ',
                'ɬŰˢДBÏѤǢ°ƁƸ-Νԛ˽˺ēƏʰ˔΄ʮ˚ΪŊԑĂėαǞ',
                'ɥˠЎҴȦʋŎӔıGԊӀҪӒŬ҆ǃȪőɉ$Ӱ¡šʨȃԭѶϮΗ',
            ],
            'licenses': [
                ')Č)ȉà5Ҹ©ȤԩѮȒϻңʝûÁoԤŶ˺ɹɓfϘɹ\x94\x93ӊȎ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƚɛÑ',

            'version': [
                -4161212631587104796,
                -4040712552788828785,
                -4762819188661963340,
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
                    'name': 'ӫʹͳ·ӕɡĹѫύŕŹԥčš¦ҕΩѵȃŵĤϱҽӜԗɄčϏ',
                    'version': [
                            -4699068536097766738,
                            -3694891869601047023,
                            -5277819037668832621,
                        ],
                    'about': 'нƤϖŹԇԭΐϟ^ʍƿϻǺԝЀÆƹȬ\\ʚѵʮ9Ûˠĝҿ/˹ľ',
                    'description': 'ԔЃfҺ\x87ʬНȍǜ˼ȫɆ¬Ϳ\u03a2Ӫ\x9eÈóҶӟǸƎɈƣэȍ˟œЕ',
                    'authors': [
                            '˚AʫϓGѧȯĒ˲ӺŞ\u0382ϏĚҭŪŋ3ȯ\u03a2·\u0381ˤˎəģЊ˒рĤ',
                            'ӉӾʼĶёЕʠŐǿЉ҄ŖiÊȶͽ\u0380ϾƣК˄ˤӖ\u038dҷÿqˈť=',
                            'Ɉ¬ҸΐԬŢʔÁWèԢԫԀõIRĸŐ£ŖΙ',
                            'ɥӶŭβԇɤɱΤњԅƒȯĴĞлƅůԐлнǮЍ\x9fѼĤ\x93ˊůϘƼ',
                            'ƆϥћʪʈЂ6\x8cßFʳȻӉɃϓҰ˅\x84Ǩ9ɄЩğdԛқơɖǘǮ',
                            'ɆϴȖԙǚ©Ūĥɑʫ\\ԬȘʙ·ɼΠ\x98Δш3\x94ˣĽӑӐϱÅăѹ',
                            'ÉǯζΐϺȓŶȨƭ{ǟ§Ľ£®ʾ·~ү\x98щϸ˝ɇѦѿԂɣƏ˴',
                            '\x81Ƶʏə',
                            'ƍʦύǐҽɕζν\u0379ѳģàÅ(Ԇ<Ñ',
                            'ĘC˫ΰȡ3˭ȈҧҫͰϜњŦǎ\x84§\u03a2YωԤЀǨ\x97ʠǖ\x92яƃı',
                        ],
                    'licenses': [
                            'ΌΓźѳŨÑҏ?ϲґΪɽв$·ËĦƒȋňӻԋǛЁŶɶ˻Ϻԟ³',
                            'əƾьŨųēǚǱĘτӟԪЁӨˈƃЁѰΪϤɞʦȤ\x8cʌϭĩâƊǙ',
                            'ɔ\u0378ŽɾӼѓБ¡ϋ{żҮÖј˱ɞ8εȍR˛ЩĿ˛nЕĂɷɃØ',
                            'ӹʀ҉Ȃ˳ԔϷĐʐіҾʁԩҠϢĵҫ˽țͻϦ64ΉsǮΔСĄĚ',
                            'к|ƕҥҖMҡəʨǑңӹ˳ΔыҦCԤԛªΛʊЫȥ»ԅʧǚyϸ',
                            'ɲϱɹłƫɞǯѷȧ˶ӎЁšҤӹ:Zɩ}ѺǌȪ˟ӟύČʼƶŪó',
                        ],
                },
                {
                    'name': 'ĿԆˉƿгΧɴԔşĲϊζҌԕɿҜ\x90˷ԮʾϵөYȎWĴ¸ƶJѕ',
                    'version': [
                            -5312351712188027285,
                            -2490335263442769792,
                            -3101868852126348522,
                        ],
                    'about': 'пїуĦϥƲǓύĜɻŔȠи¥ϛӾ_ʐĆȁ˱űŏǬφӱȲːŦɨ',
                    'description': 'ΕѯϋԔҔұȸһμиȥʌΐǇҖ˪¾˦J˷СʯБθʒʡȓʌȤǍ',
                    'authors': [
                            'ȥҝЪǆǌӔΣ{®óЁȬƦξҼДɅɃļaȚ\x94ə[ԌӹΔʄMЇ',
                            'ӣȌԇg\x93ʣҦôQδǞƺĄȜ°ƙĭ˲ǓlʊƜґNªόƑҔӬŇ',
                            'ũʝΙƟšâɄӛʵԕɍ˾ӀўƂ΄AˇƜǎҺįUѬˢΠĹóΤȃ',
                            'ӕЍ¤ӾҊŌŋȆBɌĵгѵìłШÓƒИzWцɖѹ[ŽdŭҀ§',
                            'Ыѽ^´Ȋѻ\x96șѾšΙӣϺ;ɾӦ\x90ϬѯEÛЪӵɖҥ˄ͺǲw!',
                            'ѦиŅèľр\x85ϝĥȕӞ\x9eȊҧǋʫċĩɓĺʾ˻XԐ˦ĂĎˉɉȉ',
                            'Ϭ϶ҧöĕʐԊрȽ¶ÜҒÈǙƖӆQө¿üΧśБŔΚ«vā?Ũ',
                            'ѻĦǝ\x94ϔ\\ǯȉ¨ӈϚɐΐΞϼČͶДʺήȬ\x8aąΧТȽʹ\x97=ζ',
                            'ҔЌǋˁЩԋѦ\xadЅщűӏ\u038dʧƹɛӃëɄȚԞƗЅȄ҈¹ɖĘǒϲ',
                            'γȌ(єԧʋҕȀϺІ˥Ȇ˟ΚҌѮXɹ˦ӜӧʤǩǻɝОκѓъŨ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': '\x94\x828ǣʭ\x95ԄK҄ȉҬçʌʡюêɛƢžũҘ΅¨ʖʡʲ²ӹĽŮ',
                    'version': [
                            -1226167075105691477,
                            -8837932843437934634,
                            -7317453122713882707,
                        ],
                    'about': 'ƻϣҷΪӍѐcϏΰ',
                    'description': '$ɩɆǖʹǢǛƘ˨ɯƼƻ˵ҟϰӟ˔ӐϥĂЁѲʷӹӷʸԫϨұ˜',
                    'authors': [
                            'ΠүйżăөƊgƭǁўӬ.ǜϜОόύůЎĄâŮʬΚĄ\x83\\Ԇʢ',
                            'ԩʾԝБŭƘǰǗϟŧӯʒ˲ԥ;4ŗӨҊtōƴʼӂfҹÁѦŝΗ',
                            'ǌӸȯ;¨ɰИҩҁǠ\x89ѢͳѢϪˠ\x80ǅɃNґ\u038d¼ҞĜԡϺʑЈП',
                            'ӍTʾɈЫѡʭǺήҏҪʘţʾ¾œҵáƝªͷj\xadǜкƹƊŮʇǧ',
                            'nƝŏƚĆǌԨŃԤǿΤʀʢˑҐΣΨĖ\x88ä±\u0380жˈҦľɇӗ8Ǉ',
                            'ͽŃ\x84ɷ˄Ũχ˖ƘӗǱσˌǞЉƬ\u0383ȊíǥѼːΉÌöέϿӂγɬ',
                            'ӑΊҡʆ¹Еì"ű˕îèˢȞҋĢØҰʄҡ\u0378ԧ\'ЪӆѨҌ¯ӊϰ',
                            'ɔʁ{їƛ©0ŷƂuƔ',
                            'ƼѰӸʂǒΝ mєƆЭ˥ĤЁØγ\x8blGӒĚɄà©ΐéƬBɌι',
                            'ΏӄΈʢǉљґǻYʸѾǖӀνΚ˗ҒˁϸϋΠИȜď\xadǩ&ÔƧƆ',
                        ],
                    'licenses': [
                            'Ɋˬ-ŗ3ĈҮԇϾϙĻ}ΑАĖʷŜ.zύŃȜïѫıѨИŜвʫ',
                            'ѼҺɠƣ4ɜя˱˞ŽɁӺҵ\u038bwwЇԞѣҢлʯΉlɀʕӢ,ēƩ',
                            'ÈL˕%Ӆѯж¥ĽϜǯ˭ʒ)ВӘЁхĎŃÍĚΔԡȩȹĢҥƴǽ',
                            'ůө§ʏӉĵ˼ѳ\x870ɵƧϓƐ˵˱˳Ƽӆsïƺӳψ˓Ǆ\x93˩ɒʪ',
                            "ɂǘȫΩėʞɀȝQӦưĜǛϜǲJЁӼԑɨȃ\x82ǴҲ'ėȼħƞΉ",
                            'фҾ(҇ɽŧȝƉЬĵɅáȖųÄеʊ˰ƘȢęӊШǜԈżѯʵɱɖ',
                            'źzíӉŮÓ˲ͺР\x91ђCѥкFԏӛØ:ԓťӃ\x99Ϭƴ͵ϜÁӎϪ',
                            'ЎȥθʆԪѾƼѼʃϱαɰЂΟ˶ͲºέСӿѠüϖǚOӓɘЃ˸"',
                            'ýǡϔęÏҲƣŶɉϰȆžƼîϹДҷΞθԣȱŏϮʈӻΎ˓\x97ɢĲ',
                            'ʓyºDÛðήƋӒ"ϳȼϸvіƜѺƑԟʹΙ\x86˕&ԤЏ}бbб',
                        ],
                },
                {
                    'name': 'ΒȊ˩Ʀ/Ԓƛ',
                    'version': [
                            -6101215701584608064,
                            -4597184127110518048,
                            -4420445597160321081,
                        ],
                    'about': 'ΟɭЊϖѥӠI',
                    'description': 'ѳ\x96ȋ½ßóƁ˯ԑ%ùͼǈɓčȋӞɑЬӉӰʹфδѺáœЄʯɧ',
                    'authors': [
                            'Пɵɼǀӆ',
                            'Ƶĝɟ\x9fѺ§Eī˖\x9aίЙÊŬӯ·ѰͿќѡѠԔTāϷȹāƮ\x9fȨ',
                            'ϵӐ˳Ӯ΅ВƬįËĩӉzǵÐԥгγˇЄԌVǪŊȼ·ζ˽юќ\x92',
                            'ʐUɘЌΌʂɱ]ʳԦϵ\x9fɭӉVеѲźʿʸԚǰŁDÜșÄŭ\xa0@',
                            'ѥňpʎó\x8cnι*ä6άԏǶͰʋUɬʲυӬΙwèѧ¦Ңłʆë',
                            'ÑʼjƴͻɒLӉD©âԆ˛άƊѶȞӨп\x91ЊΆ¥ЌɩρɵƅхǇ',
                            'ŉˁӕ\x8eҮʵ¡ԥɈщʨхқǤŨŭҿεʊĎzjγ\x8dh\xadȏҗԍƵ',
                            '2ŒˌţԂŁϸѫʧƧӔ\x8ekɧљЋɶӎͽвăÁӄÈјɠíǤ®ǝ',
                            'Ï\u0382˲ҢĶĤñ\u0380ȣČLΌûơќì¿£Žİ×ƝɾϑкT\u038d\x9fįѦ',
                            'ŴŨÎϝåСΌӸāґǋҽԝļț˛˜Ŭƭ˱ԙѶǯИӍĢԣŃҷʲ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'd˻ѣѶЕ\x8aψΤƘƒE(ϕ\x81şʫbӶӠҡʞ˩˷ŠXʛԑ',
                    'version': [
                            -9087424094236059949,
                            -2025347247903742760,
                            -9099972611607951788,
                        ],
                    'about': '²\x8bǥЀƚ˟ǗϦɖΖҁŬɹΨΖОϔgν͵#Ϝ4ŧɞɬǛf]U',
                    'description': 'ҘҒɅɶϿҚԨ\x91ȽǏӂ\u0381Н·ȃDkЊǗТɶsɑɏч/ӗȡɔƯ',
                    'authors': [
                            'ѾϗԀ.ňӥɦŞәkšơƾɀ}@Ǯήȍ£œπԞԍʸкƜѸ\x91ά',
                            'Ʋӎ΅AϪİÑēЈŞ˓ŇсқҬCҔ:×ǑӥǷҰΑǹɩ΄Ϣ\x85ŵ',
                            'ɷĔŚɅđʖԟȧЌ˛ԨǧƲ\u0383tϋʔͽǚƧǐϋҬҰçȮǄĺ\x85И',
                            'ϕ[ěėȘ\x8e˨Ľ˱ɴ˃ΆŐȆπѬŬķϛɛщûЕȶϓχš&Ԗů',
                            'ҕҗǏŽ\x90ȑɱėĂÚ˷hȀŗŸ*ŀϢʈnԠɍèкȮԥɎȒˠȥ',
                            'ȝΙöàǡɽƇŘӗЋКY.˘Јrҩ1˕nӗ˪VԆXƛȏɏψʞ',
                            'πɺΡrЬӃΎЇҗќїƪӀȥıΜØɕƸʹԂλ˞űѳ҄ů(ҋɝ',
                            '³рˁŚϖ#~ƀj_ҿΜȊƱԠɌnǢƚǲğĚ*ԭǝЄӨɚģψ',
                            'ÂȥϊƲÛʱĈѽӽϹ\x88ӟñƊ˓íɗџȕˀΥϹǧѢ»ÅҗÝŁё',
                            'ȀǴĻф1Әϩɮ ʗžԇӶɳMɯɚƏÐɂňƵАʹȔɐÚƾѺΦ',
                        ],
                    'licenses': [
                            'ǡ¨ȑÙĿ˔\x8dπȪҠWIǩ˚ƓΟőˡɶҴψžŲŇSƆºɌӯĘ',
                        ],
                },
                {
                    'name': 'ȦěȜѪɎкƗΣɗѝеџЦn\x94R®Ӎ˹ΞѾūˀʂúв;ʭԭ\x88',
                    'version': [
                            -517965519017197290,
                            -5187748076479131471,
                            -787325430035539385,
                        ],
                    'about': 'ɢ`ϕʱԅПˎ°ȊǣĘÿʼ$ːēŖƝǡ¨ΫѿȕBԮʘŕ҂ʬɢ',
                    'description': 'ƵȾŜƭ˔ԪВϡˇмşΪҐʼƱκЗǯЦ˲vǝӈΒŔWʎˌϋϘ',
                    'authors': [
                            'Ȥ˩ԣǖƒȄӲЁŦˋƬ҃ωӄԂѿ\xadȐҪ\x91ӝΫею\x95»϶\x9b\x81Ӷ',
                            'ʓϬԤȗƴɘϦԞ\x87ɠҞΔǜƀǿĴЃŊԐʗβʮΈЯБӷÊӥ\x96ʳ',
                            'ɇÈɿФøи¦øίѥђǐҫȥЛȒ"ʫӝўƢЁĊɊήӷɕѬυӅ',
                            'ĄҜӦƵ\x8fӖЪϒÙƄâǞŎɹўΡϖ҉\u0383ϱӘ\x88?¾϶ȮԡǷbƆ',
                            'όʀĆǭҟδ7ѼŉɬЖшӤάĖ\u0379ÉӄýʦǴǟиɽĬЙҐζҷ°',
                            'ČǨӓòΔƾӂѢüȵұиlГԅΫœïƬӀеôȤiѭҁǆΪă¡',
                            'ƇӼƼʨȏЪʿНѣϸȆΐ˦Бɦςŭљѕ˾%ğ\x8dҠ\x9aΣƹǆӇϝ',
                            'ċtіРԛɓŏǓ',
                            'ÖпǹɠǆϮķŸӅЖY˩β\x88Ӿ˕ƞɔɻōϳϽ[ѮƸΜǱˏϩѻ',
                            'ςԟϹϡˮɽȕ\u0382ӏyјÿƪś҉ϴȏCзɶ˕ȉіĜ\x8f\x9aŦͷһĎ',
                        ],
                    'licenses': [
                            "н'ˈѨ\\ʶȕÄʦʶď\x8eϰҀЦΡ˴ʛ\x90CӎŢɲqξʠЌʥˀQ",
                            'ӗ\xa0Ūˆʦťϼ\xa0Ǵ˺ҼȿĤѲ.ʁӜǉȷԟȚϢӅŬ¯ǭĞ\x7fs\x91',
                            'űôϗԌíӧгȹήԋƕǴЀˡÞѿеѭүȳD˫ϸɉʚɇӢƴоƑ',
                            'ѦѿŤʂћԆʨ\\Äį>þӪȣňпǌ5ȍǽԊԓӋ;ӼŐ>ҩɜȐ',
                            '˗¨LпȄǗBьʈʜȷǬǵƤоqĳLvώˁȚӲZ˅êɨɐґǠ',
                            'Ӈ˅ΥǓƯҧė^ˋӄѠԕɢ˨.ąôȀʐЩǍͶϤӦί¯¹ʩǶΖ',
                            'ȭŤҴǐŰȻɈ˹ŮЅҨ˚ƵȔNʃȄ˵ƝɬɫEє˾ˋ7ӊϦǈǐ',
                            'χ\x7fƐ˸гөΓņȍɠπȘԝ>ң&ԦĀΖӥҹ<Ƕθ\x7fŸ',
                            'hӧq$ľ¢ҦͻƘů\x84ɗ:ʎƜR\u0379ѲŪ5ÛͷϷђүԩȊυäͻ',
                        ],
                },
                {
                    'name': 'Ǩёӏ4ҎѨŸѱ΅đƥ[ɖƃһūλ¾ȶȋϩ\x8fǦУϯtgƌˊы',
                    'version': [
                            -7298691792282186484,
                            -7963098601882863086,
                            -6180104815359498676,
                        ],
                    'about': 'ʉɡãϊjÂŀƐΖũ\x8eȫԘˍϡɄԍ',
                    'description': 'īпÄ°¦ѭцҼІŞʮΛĽ҄\x86ʗ\x9dɿŐÓʀɞĤӄɀϺԦʩ\u0381ң',
                    'authors': [
                            'ΧѱǾҍɥ÷óΒ\x99²ʗϤΩëÔˁûʕΙͽǢǄɇѥǏɋϟҷȨ˾',
                            'ԚȲƠɚѴΝ\u0382ǉɨˇ`ӞϖϫȒҷиÝΠóҞuĹŏԐѣγDЗц',
                            'ϛϸ¦ŉʱӶеѾLϓǏφњ«Ѵ,²úдϹҁ*ͽʕǆĝĳʠƘˉ',
                            'Ì\x8d˱ϻНĿÝ҉ƍǯѼѶvŨϋͻǨЈҙσƵæZψԉˣı\x89Ђ\x91',
                            'ґĸˤ˜ҿӕ҇ǉþŒɅªΤ\x8cʏʔͽƇɐĔҘŧ¨ας҄ǜȠđӄ',
                            'ƳЕƍķæԦøˉξyԏ',
                            'Ԣ°ɯǗ}ˤ6҇λȞғШӭԇқɝӜЕȒʿ»Ϻź˝©ɞȏǰȸɜ',
                            'LԘ°Ǌiӥz˗2ʶЁɜëτ/ΆǍ\x9eȄ˛ǻ7¡ŝÔŵǧѝğЃ',
                            'Ϣӷ\x96aʕЉԆúЫΔϭϢҩҶŔqԅȲˠʬ;ԕŢЇØʿӗĔϽɘ',
                            'Ѹ»ɄĐÓΈưÌǂSĨхʇλŽϻώͽǯȣɑ¬ɿɔˢχȮ®ʳГ',
                        ],
                    'licenses': [
                            'ΖƲ˳Ś˷ʞɱɂ\xadΉϺŢԘ˯ĵ΄бɫŻɧȻʇǬɊŗΉϻȐ˩ˡ',
                            '¾Qýт΄nǥѵƋӐŉϠʎάͲƋ£ƹ@\x82ʥͶĉеϢęɝŵΘǵ',
                            'ÝȣиЄϬȷϝΘʀкŪʞІ\x88ѧ\xadўȿҶ}ѴÍtƈɕӓʕɒӈɦ',
                            'ґȈģʟŒˁҊ˪ɮ˖ŹŖ0ϪёAӦőʜŐ(\x98ˁǛ˧ЭυјŚЫ',
                            '1ûĭʉҤYěȺɀʛʡӢэɌɠVʷ%˥Ð',
                            'ԆιˍŏϧϳВʀŊƄĽԝϵ5ßˁϬʡ\x8aԁ˯ʷɡϰȦ3ŨԬчʙ',
                        ],
                },
                {
                    'name': 'ҖӄȨύɜ҅ȡÍҩʳЀ\x9dôͷҍʍĊͽ˺DЃ.nВäǻĲBɖÎ',
                    'version': [
                            -8752348500713807438,
                            -7022521027086545928,
                            -3756770614468203614,
                        ],
                    'about': 'Xɳ˥ʐЦԠŜ\x86˃Ж\x8bčϨӀͻЍЙϯj_ɉ҇ʻǗϩŹ˅ȿӗĜ',
                    'description': 'єӱƢƩрóИʯ½ʊŗ3ӊвǅ÷ĚƕðҾȠοΏĆŖƨ/ƋѹĀ',
                    'authors': [
                            'ĜӘ҈ҴѴПĵԭϸÉ\x93Җ҈ӥƀҙϬЧ¨РѝĕԗǹƑԈȔȎԪǲ',
                            '\xa0ώØƷɨƁēɭε(ӭјԂѩϫȆĀĩɡ¢Сsˈ¥σҰùɦӘΩ',
                            'IӜͱȁǘʹѤēѵ³˰ťɴaɢїОưİɐӣҏ+\x9fӹҋӘ\u0383Ȼʹ',
                            'ϮŅҋκЇ\x80ώȴΨ+ːȤҮԨѰқɞʋēģǶưĒҁӱϪϝʑΎ҇',
                            'ĞʻǞǟΝȪӣЈɜxȆcљϭΪėδΫǔćӓɂѹƒЉƹȶÍѶϏ',
                            'ˣ¶ƽșɋĲЍӶ\x89ʥũʵŤȾ˨ԊίҬćҀΞμʍϝõ\x88Ťĵќκ',
                            '=ѓ;еκԝгӴȵΫұԫӟʔƱӌъЧȯÅpɐʃʯòĢʶΏɾΖ',
                            'М\u0382ˏҳȵũɲѽȺBӓΩѧƣЃéƙҀƾʑ˰Ķ',
                            'YħŒǓéĪðȵҍθǃɎɔԁ˖ӫǇōƉюǆĠɏμƠюˁƢѪg',
                            '~ѱ\x91ίҚ-ϧ;҂˃äűҕ¥ϵŐ϶¡ԃ:ѭЌԦʒŏȲѦɕİŚ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'țѨчОԞǸΗ˔ŔњАǫϳҭԜCίðѼĽŤ\x89ͿƑϙĚԨŭɛʿ',
                    'version': [
                            -1507537602882650899,
                            -5239465189088219014,
                            -484944310251194761,
                        ],
                    'about': '',
                    'description': 'ίΓϥ˼ΆƄĎѶǽҡǔбǅύAȏƼΑш\u0382ҡ\x87ε(ϘёӖĵϳƺ',
                    'authors': [
                            '˨ϠɖìЎǤ\x7fͿ8ӡ˖Ιŕҧȣ˄ѼȩˈҗЎѽʺēXѢȱəɲɟ',
                            'ǫʴϹԐɣˑSĚԊŸУ˅сʸɀьɉӱ˳ˈɄȗŜѢһ˻ċƣ˽ϲ',
                            "Ƭď·ҹҵϾȃжƝ,yϋL%'Ï˾ͽ",
                            'ԐȭΡ;ǥť¬Ԉ\x91˒yŵУԑү2ѥǌ8ʵԣɡѸԑ͵џЍŕs\u0380',
                            'ўˤѹϜ϶ŲÎrӈǊяɼƮІ¸łŐ\u03a2ļëɰɶĐТIǱZЎȼò',
                            'ϕӭǽѐϷśӷɹӢĹ˝{Ӝć^ ˊýҀ˝όЬŚĝ.ŕϛɚƻђ',
                            'ÛϴԚqāЂȐҸвϡʯUǒˣŲʒʮǀŝǀΞdϱдɵƟɉʟőφ',
                            'ˣпԬԮϲɉȿĊ˩¯[ԃɑdd®Ę¥чѼȗƞӷĲʊ˥ǹҌƌҦ',
                            'ǝÚˏϤʼдӚӂʹʛцҫЯ˾άǲǢьҡтȋсÅːȸƑɡєŵ?',
                            'ņƴʒǫ˭ɋԙΚǜĕʻȏ˹ϢŞѠĔǣ\x8d<ϏȔЅˌοFԟѵȖ\u0381',
                        ],
                    'licenses': [
                            'āϣϽƙӤY\x98ĵΛзń\x82ԕɳēɔƇΊҘ˥ʝDˋґΞʄσpL¯',
                            'ǝф·Ԥύι҃ǀĻǛΰɑԫÄˑҤϚѣ˛ǵu÷Ӥҿ¬яӦÔÅļ',
                        ],
                },
                {
                    'name': 'ΑåЈ:ҘҮѶӇ˦ĨЪȲ҇қȅȤȝʵéӕԭƞӌȗǖӍαʝΪϖ',
                    'version': [
                            -202610049644746785,
                            -1559688696511078637,
                            -381337222869798016,
                        ],
                    'about': 'ɅѬίμʷp0ԙƽɼ˃ʛїǬϗ˟ӭΕ\x86ÁɉǥѣΤɬƯԢΈΆҝ',
                    'description': 'ǏĉÙèΚ:ǆǳ\x9fǃϷ\xadŎÂźЬ\u038d«ҡϢ НȉǡâҖį˼ˢf',
                    'authors': [
                            '˼ƙāĝɷ½ӬǤɴȑƸ˓ŕŻ7Ѳ˙\x9dԪ\x8eԢȟѱëТñńưāĥ',
                            'ɨÉǦŵǋ\\ѷiʠǝέϦΏ\x7fäǚÅҟǻҎ«ȾѺ-ȷпрâţʴ',
                            'χfрӅđßϐѧЪжɫӌŔȸƎ)ϡüƶϒƲФҭe\x81ɼαȘ˰ԥ',
                            'ͲŰȼhĵčəƘʪO½ϓЯѸӧĴЄÖΚјӺęŴÿӆǕѴӕә҃',
                            '\x83ǬӠлǣдÇяˠӼſϗӁвԜóҏͿʚƇ\x8aČǡ;ϫŴñѮƺƺ',
                            'ϖǔ˥ѢšЃƏʞҲ4\x89ҒҡϮҳÑԚɍʥ˛ïΥĆӞεѸΕҔʡӘ',
                            'ѹγƎԁaėʰӚԢȀȂе\x95ԄΡØËКԅаƦ˷ɈɰҕǛ˂Ϭŝщ',
                            'эԬ¬ʙƁƺƖѶˁnŊ˴ЃѪȶάˎьɐɨ˨şτœѿ¡тӑƮ',
                            'ʗѓ˝Γ¿ƗȞ҉вцňĂ½ůΦȔ8ӗ˛Ɉӫ©Ʌ˽Ƿθɲǚ\x85ɇ',
                            'WǪѱԜŴҁȥɆ҆ΎƥҍƃÅгɬӥˌӎȢ˨5ӄʯȹѦғӹʡĆ',
                        ],
                    'licenses': [
                            'УɗȼǓυϧzɺÞȫ˯1ԈÈʗЍƵԥсзɳӑџÃ\x8bɅĖ˴ɚԬ',
                            'ƄӜæǘĦљπѝɞÅąβŤ\x85ƵeӏöϻʱƊƦbÅǦІӊɤʺϛ',
                            'ʴ¾ģEӼл˚γeEϤέT΄ѶʪӪҹԢǦΈĈϴȩʶʂw˓ʸҶ',
                            'љ%m˙ʚ\x9cĄǑSáѐύɉсӖ\u0383ÁΟɜϨ҅uЪ\x9fϚб-αҫˊ',
                            'ɯΝѱǞȃӰǍǒю=ˑԁŘǙΝŕUϾȮʭ˹ѣΉГѱ-иӾЀҨ',
                            'ïӭЇ;ҀħӷƢρ\\ȤK\u0378ǗŃēȢȩőӕƫ«γ¥¾\x85ƓƷʪɩ',
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
                    'name': 'ЁȝŦ',
                    'version': [
                            -8158616947291278527,
                            -5468593841979669047,
                            -6124983000233413305,
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
