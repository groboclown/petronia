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
            'name': 'ԛүћΓǣXƇfӝѰԦÔ(ƣǬɇʽ\x8aϔΕǃΡǙαȈҏʄύνw',
            'minimum_version': [
                -8147318389746851812,
                -1444451525631616089,
                -8261525288296550201,
            ],
            'below_version': [
                -2158295329981667779,
                -7523457287783958908,
                -7416245414576817700,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɔȗͿ',

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
            '$': '\u0383ėΑɍ˛ŧǪʄBŇʒ1ʒƵʑϽ-ǝұ÷Şɵ!πыʹщӊƉ!',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -6356411145017105738,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 860206.872330127,
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
            '$': '20220526:211043.168230:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Ãʌ\x9aɝҔCWК\x83ĎŅÛgˌÞӾɷϣαʑô·ŁҶԎ]ĬҽΏİ',
                'ɇ˱ԡǚŵʠ¯¦ЙϙƢ˻Ίǡѣіđ¹ĞÚĴǑǃвɫϓӄƺҋԡ',
                'ůʋʃ\u0382ͺǒǦьʅȢ3ɨµϼƽҖ˻ѥϵѶķµ˭ǟӈͽф҃ʌǡ',
                'Ѯ4˩ӥïɏ\x98\x85ΜϘЕԩѥǐƕʉȢþĂ\x84ѿěÇη˯ѸЋΎɾο',
                'ͺϱ\x9cʟ¿ƳŮ\u0379ϊzϴŦԋԞЩĺɂ-2ʲ˅ҳƎǉƻÞȢȁTѣ',
                '3ćβΑƩoćԜƑǱċοԪȼšʯ϶νʛȂФɇɝΛǮͳРŐϊŚ',
                'ѪʆĠƓɣʳďƀӓΞģ\x8eȅоԄƈĵǶǄЌøƐΚлzӻOșƽʽ',
                'ЮƹӑȞϊ\\ĵõӎǑ\u0380ɵЮўKҔΑƏÒɻȩƘϬєƥΩԎӧa˼',
                "ʽҸTΡшî5Ű΅ǸӏÕǭҷȬp'ĢΕԏчκƠǝɏƻԪCɖӿ",
                'ǇŔΗЮ˩ǐʪÜԛƇAӭôӾΪхԨ΅áхИaʹϧɦÉі\x9cʓЮ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                5355544162979002757,
                -7607528641936691458,
                6643139457820900951,
                -2670200974433024138,
                1651376158372222167,
                -7001120475848850364,
                2873347519296973584,
                -1258819134130965112,
                1510208588906567328,
                1624613852199280406,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                13543.444772356612,
                -86864.50008220125,
                -83073.1519130966,
                841843.3597175805,
                420505.4828124917,
                477496.67194815073,
                741748.6326008731,
                365256.75083606195,
                407897.20679039345,
                317366.6542514132,
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
                False,
                True,
                True,
                True,
                True,
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
                '20220526:211044.282156:+0000',
                '20220526:211044.303068:+0000',
                '20220526:211044.325553:+0000',
                '20220526:211044.346800:+0000',
                '20220526:211044.367771:+0000',
                '20220526:211044.388650:+0000',
                '20220526:211044.410424:+0000',
                '20220526:211044.432751:+0000',
                '20220526:211044.453421:+0000',
                '20220526:211044.476117:+0000',
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
            'name': 'í¨ÊľӉԍˋȍΌыĪҫ\x87ÄĚƦųѦ˾Ɯφ0ΎǑȭЏ+юɮԨ',
            'value': {
                '^': 'string_list',
                '$': [
                    'ԭzм\x8c˹˹)ʊ˟ųɰŠμɝĀʠ˱*Ϊ^ÍƻȐϙЂѿǤšƠɬ',
                    'ÀԑΆӀҸҴΫԤƚĜĉ˔Њɲ)ȕŘΗ҅ʑΙQėń\x97ěΪԓЊӞ',
                    'Ӻ\u0379ȰаȱӒҠЉlɼÒ;ɤȻĈЛƤ˗зWřϙȨпИԁť»К¸',
                    'ɮчӞμɢНʏϐɞ˕ϕӴ˰ŎĢɷУ5ǽÉ',
                    'ƐıπӷɱϲЄƤҷӞӎʺȲȅԚDȿɝ)ƫ˯ёǪҷƑЀǷϩûƾ',
                    '˴˟˒ʄсɕD˙ɓɝɝΘɛŹϞοΛ˞ªҋʈ¯ʥŢõɛђúΔÂ',
                    'āž\x7fҋ\x8eĨ/ҨӛьΥ\x9fӞȳʚ˚Ҝ#ϱǗFϱɪʽýϻε҉§Ķ',
                    'ϖ¶ϝùƻѯ}ΜСŉɺíŒʞŽǼǊɚǼүӀíƬʢ%ʵΏҨHď',
                    'Ϻ£ӑыӼёкʏɦñˮʚΪ\x93Öԭ¨ɛňȝʳǊʻǺąɞȷȁǖ˺',
                    'ЖӍ8ӟǯǨɡťɬԂ\\īЪ˴šcͻҩ¢ˤϣ¸ˆÝԌĳïδϨƿ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ł',

            'value': {
                '^': 'int_list',
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
            'catalog': 'ԕʩƉϘō͵ˉӘΏ\u0380όɹ£ΤŻɹƷȝȌƘЂɷͽżʕɂϹôVԎ',
            'message': '0ŞȘήʖyϮÅӚşǽɗӎƸčăүφƻѴÒĕˊɝϢ}ȂџҘʧ',
            'arguments': [
                {
                    'name': 'ƪʜɦπɌƎжŃ\x92Ўĥǋ9ɔԒӚϾ\x82đǚʟε±ΫɿΆĩΏӕŇ',
                    'value': {
                            '^': 'int',
                            '$': 1906742918842966215,
                        },
                },
                {
                    'name': '\x85ǍәӽӖԂХ\\ʂԑ÷ϽǬ\x83ʗӀѱТȠéǒҍUŪҌԭəҟŰϟ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        827093.5232577038,
                                        118767.81196602358,
                                        975517.5520119739,
                                        939079.964523445,
                                        252909.95679500303,
                                        774464.3956236092,
                                        876880.7040429357,
                                        556471.1556443473,
                                        767982.0074456111,
                                        619613.5970253084,
                                    ],
                        },
                },
                {
                    'name': 'ЭəКǑɕҢɱҒƒ§Ÿͺśԍƿ¦ԜŻΣɛЌˏΛΠӵϢһ˂ϳê',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Ǫʕɼ˅ӵƛҠ\x83ΜɹS˅ȲѫʸϔƴӁʴΑԀČДәӹfӴԋ',
                    'value': {
                            '^': 'string',
                            '$': '϶ϭ¥ɰԇȞʱ9Ϟѷ}Ѩλ\x8fŔѱöˈŁυīþȞПϛεʦÛіĂ',
                        },
                },
                {
                    'name': 'ǩƪ\x91ÍщЏԃԏz\x94ǱƸ\u03a2ŖϤΓͷȔŤҦcƩІʴьŝ˦ĀͳC',
                    'value': {
                            '^': 'float',
                            '$': 360790.05032567715,
                        },
                },
                {
                    'name': 'Ù',
                    'value': {
                            '^': 'float',
                            '$': 253332.12866257655,
                        },
                },
                {
                    'name': 'Ѱаĕ»ΝÒǄҩʥ9˃ЄÈŊƷͳ҉ʅįǨPā\u0380z\u0378ӆϘԪӰ^',
                    'value': {
                            '^': 'float',
                            '$': 401042.57169158687,
                        },
                },
                {
                    'name': 'ǟЕЊØȯÿŵȑȭӰɧϤőƢǐǫКͶԪŰøԊHͺƪΌ҉ƭAԐ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ӖËÜģҒҙ#Ǘ',
                    'value': {
                            '^': 'string',
                            '$': 'üǎƍЊ\u0380zƫѱЅFˠˤƻ°ΔϞɡɫʱƱԤǎаøĢǶѦԡԈŨ',
                        },
                },
                {
                    'name': 'ʡǌʭϬÒϹÕńӊɱɘŤǚњǼлǎ\x82ʾV',
                    'value': {
                            '^': 'int',
                            '$': -7571386380355407339,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '@ǀ',

            'message': 'В',

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
            'identifier': 'ɒӎԈɴ!:ϺȴеŨǁ½ïˊοĹȘƠ˱#ÍҒ²ΑǊʹƛϷǓǥ',
            'categories': [
                'network',
                'os',
                'internal',
                'access-restriction',
                'configuration',
                'network',
                'configuration',
                'file',
                'network',
                'os',
            ],
            'source': 'ʣϠhʊȌ&ӿԗ=ѸƚLүʴӌԬ¨Ëѧɭ\x89ς&wƥŀǙŠa\x99',
            'messages': [
                {
                    'catalog': 'ƈ˞˂ǈȾԒӥʥϖЃҫ˻ІǩϜȠӷѴѓɒ\x9fҐϛêҙÎщȌěʰ',
                    'message': 'ĔˊҎǊң\x9b,ϻΩҽԣ϶ιӐЛǼóǎƮ\x8cs˒Ҋˣɳüɗͻóû',
                    'arguments': [
                            {
                                        'name': 'ŮЍЏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ԭε`*{\x96Ͷpѹ҂ѣЂϓ͵ӈɖǹȧĳԜGԐǇϙÛÅ=ʁǩÔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 152178.8193966116,
                                                    },
                                    },
                            {
                                        'name': 'ƥ.ʧñϭҊԂӳύEɕһӂʖĬqɯʼΕϟҨvǥԛӒԬƦɌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211022.625161:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϖŰӳʫ§ŽѮˀëÔ:ȪRˌϗƿIз)\xadǫǢϋАшúˀ ȂϬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 931283.263395376,
                                                    },
                                    },
                            {
                                        'name': 'ҹÌɵɅ\u0380Ҵŵ;Ă',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŗɂВU.ƺЭҦ<ǴǣƧҬ\x90Фӌ\x84ÒαҎcĢϔğ˫гΌКǜ~',
                                                                            'ʽˡӌ\x84ȨȭҡΔƋˆŬɴǾÊбêͲ\x9bŔϸΊƬ.ŖǛʦʮ·ɘƒ',
                                                                            'ƿқĶï7ӂϺЍДѣΡťѼŻɿЯÊϯȴ]ҾΤũǦŜĄǥU«}',
                                                                            'Ԇģjm9ҞӌȌɗŝǐѠŖŊ@ԝŠДоȽЮϱ4ƕ\x9b\x87ʍӛȏY',
                                                                            'ƑˆǋͱiʹǸͶǁѪƹґjʙǰƶ˙ʇ҆ɺΝĲԍŰ§˒ҨɌҩȆ',
                                                                            'ΧοǴʱǻγϑǍοlΘʶŧǮс˟҂¦ϥybäτǍ£IЃͱȎȱ',
                                                                            'Ѯα˾ʵ\x8cӥÇҡ˚ҏƿЋïƮƁœRʭ҅кжũ˘ШƬŸΏўȂv',
                                                                            'ˠĵϕρЍΩʗɎqʰǪʭͿĿϕӅÀϽ\x7fķ¼\x9dҦѦȜѠ˨ΠşÝ',
                                                                            'ǍƭƥͲ\x9dˍъҐʲƿϪЏФύɾԪĿFʰą˯ǋԊҡɡѽҡϐƆѨ',
                                                                            "ːѨ\x80˂'-ƦȈдlϳ=ЩłMƛғĎŐьǎɻþąЩҪǜƊŚ˰",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĹĐӦǔʾţНșǸΤˆΥˁӭȤèžΣĸҞ\x9dҗȀšƤњíáŴģ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x83ʿӝȱǁÌ+ќ\u0379\x8fЖLËļèЂȱҍŖѩǡġӶйɪϿѮϝӸϺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211023.328002:+0000',
                                                                            '20220526:211023.352143:+0000',
                                                                            '20220526:211023.375227:+0000',
                                                                            '20220526:211023.399275:+0000',
                                                                            '20220526:211023.423654:+0000',
                                                                            '20220526:211023.445613:+0000',
                                                                            '20220526:211023.467511:+0000',
                                                                            '20220526:211023.489673:+0000',
                                                                            '20220526:211023.510732:+0000',
                                                                            '20220526:211023.532510:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĹȁΉkīɼѬǓr[\x98δÕӕɿϮŞЂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 948232.5718710116,
                                                    },
                                    },
                            {
                                        'name': 'ϞÎāĞΜϭə9ЋьïɄԬҀwӅɡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӽƿϙ˽ˊΊзάųȯȫȟAƺ˱ŧľҸİIċǓY÷ϯѳrȽƞ[',
                                                                            'ӰѺƜŘˑќƼѸƵȀ°ɇιѾǜαņƾǞӊҼħʪѫàªʐ˖ж˨',
                                                                            'ЦѫøŎƶʅ\x95ӱ\u038dӟɐ\x93ć¶μъÔáˋԎ˴¬ĠσԪǿōѵӧǇ',
                                                                            'şͻţǂˁøеδėǚɦ³ѿřÝ\x9b(cƍӗ˨˫Źhѩùɹљ˸É',
                                                                            'ʚһǪŋƷʹѡʹӔԒÝ°ĕ˙ƃ˵Ųî1ƱĠ@ÉʅǍɮȩƂŤԛ',
                                                                            'ΘğȇӠoÀɣƂԢɄȧņɃbʪǍѯщӮКƌ\x97ҩÅѼĸöǔ\x9fƎ',
                                                                            '-ņʎê\u0382ЂΗĂҦˢĤ@9ѫqÅǭѷźǟŃÖYњНһʧɊԄԫ',
                                                                            'ò¡ȚΧ¾ɚÌƥ˗ËШÌʩ˝ŚШʄȤǛ\x87ɿπԈ¥ϖŸѝƇΫŏ',
                                                                            'ƛЗԦÒɋʲɷĐҩʉΕĩӅ!ƬѮϬԜ·ǗԍҤΐąİԉҫѨƴȣ',
                                                                            'ΠҲ²śʄȭϗLΡǿЁЏ¿æӥˀҶcɿĕǪ¬Ⱥ÷ʣķ\u0383Ϛ\u0379щ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϠЮӯv¦ʣӘЋǂϖɑ˙¨Z*ӊԭȓңҸōИŊԏǃʹĶ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƗƣǵѻщƽȺ½LϭƝӯùѧ¡}˅S˙ȍѥΉюԈ}ˢýйԇӌ',
                    'message': 'ʟ@ȌÚ˩ÃͽËͷśʭɿϜEӶɔ"ʰɛǘîíЃŸŠҚàʨƎΡ',
                    'arguments': [
                            {
                                        'name': '§ô@Ӎ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211024.448224:+0000',
                                                                            '20220526:211024.468492:+0000',
                                                                            '20220526:211024.490044:+0000',
                                                                            '20220526:211024.511989:+0000',
                                                                            '20220526:211024.533254:+0000',
                                                                            '20220526:211024.555040:+0000',
                                                                            '20220526:211024.579270:+0000',
                                                                            '20220526:211024.603288:+0000',
                                                                            '20220526:211024.624698:+0000',
                                                                            '20220526:211024.648015:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'άŠĦŤ+ƠΛϛÃȥʈ\x96ġқΰĠČˏӡ\x8c0ßƓőˉҊ"ώE\x8d',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ɲыҡ§|Ä\u0381ЦҞԧCҘǗĊŦȜǺƟцįƍлȑÒŮϝҙ˽ǤÍ',
                                                    },
                                    },
                            {
                                        'name': 'љ\x80ˋƬʀɭчĨѭȷѐ.ԑжδƈͻ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŨİŒŜʵ\u03a2ѩӋ\x8b\x88ƫϵ\x9eϿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 129454.29608499701,
                                                    },
                                    },
                            {
                                        'name': "ŪƎ¼ԈƤƴP]ʟɠ\x8bоɯÉӡ'ԌԁĈ҈ŏ´ɗŅɌȉƋƮӅϹ",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԝ!gУɖȿІˋӎȎ˛ĨʺзʵҤȥχƙϡͳЦǩȒ;ώwEĂƾ',
                                                    },
                                    },
                            {
                                        'name': 'ʱąǍ<уøѕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 623470.9751080822,
                                                    },
                                    },
                            {
                                        'name': 'Ħӿƒǹʕ΄;ϲIҍȢԭҌµɯÕƮЁı|ŝȝďĴʻыȞѡȅ˅',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211025.181421:+0000',
                                                                            '20220526:211025.201538:+0000',
                                                                            '20220526:211025.229352:+0000',
                                                                            '20220526:211025.264367:+0000',
                                                                            '20220526:211025.286127:+0000',
                                                                            '20220526:211025.306354:+0000',
                                                                            '20220526:211025.327156:+0000',
                                                                            '20220526:211025.347949:+0000',
                                                                            '20220526:211025.368851:+0000',
                                                                            '20220526:211025.390552:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'àҔӃΰƪíϡÂɴşĭÏͱƛˌƎΕԨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϽЂǨίʘsепβΔԉϸқˀņ\xadϳӞԂĎȜæ¶ȫϭðķϊʏɉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211025.592650:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʣɪӖ^ӈϱĵϼҭђс',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ζ\x91ΔȸʥěϡЏХı/Ȧ˒ԆʿãʹѵԄѫȅӋǁӀŠ\x9aŧ˓ùҸ',
                                                                            '҇ӹüϨúřҏƄϰ˳ф\u0379ͷǿƢԘқņʑǵӪÚϒÚфP*ȿˤĄ',
                                                                            '˧ēƷҗǗԞҿѡɌҲ˷ѨǮҋ\\ѐƁäîƆҠљŎʂʻӳŉȢȃϻ',
                                                                            'ʠǥ¯\x808ˉʕɒħϡȽ^Š\x9cѩϓƂх˞αХŖ˗|˩ȊȗϓßЕ',
                                                                            'ӏѧʤÆ˫Ҽɥ˴ƏŭDʝϣȈɤǯƯ[J\u038bĺңûƎчά¶Ögп',
                                                                            '!îŒʍƜĺ\u0379Ïʥ§іʩƦhˀ2ɨӞΤҎМΑƆ/ÍĩĨʴɠҥ',
                                                                            'ѽ\x8dԁŤʿǋ]ԟǹǵ2ŔΧʕȂPϸ\x9f\x9bШβΈΡĎҴ\x7fˤϑϹȺ',
                                                                            'ѓƬҶȫǪϪеήËљ\x83ΨȤ$Ǉ·үǳԎ°ʫŅГӉϥƷʝęűЩ',
                                                                            'ЗԆ;˃ˉԝЂìϚĔΙ\x89ӦǽВϜѥӣ\u0382Łҵ˳ΡӀŖќ«ӷɦї',
                                                                            'µƔԩɫµԇЎϵƲгҳςˉ·AҨаŴŶάӍŁɩϚ˩ŖӨӅ`ϛ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԙɺǴ£üĆƊǑǆťáăƤƑÖМʌӿС¶Õƅ»ˑ\x9a\x9fŇȐîϼ',
                    'message': 'Ňԇ\x8b£ŸɤƤ˽ЈĆΡȽӸΔΫԉȣfʑȢҏȬ϶˭euӜЧǧО',
                    'arguments': [
                            {
                                        'name': 'фłàшƴχņеŤǍƳó;ʶŗθmȢƕnӳȖҩѧX',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'КҬĻяȾïӾЋɬǑĐɣԋư\x8dʛµơ]ǚʄƾ\u0383˸ıȁҭ΄Ƴή',
                                                                            'ѷ\x89ŃĸĝƊ¡ϰԎɋЛɴԗĢ\x99Ǫń˨ɑ¦ƏƷҵɎhϕώɍѩЇ',
                                                                            'ϓȷεƵѝԬԣĆƦ£Zт˱ųλʒȢʠӈƦќѢì҂ҧɕȎě˙ˈ',
                                                                            'ӔóСҀҤӜɄ«ȡψǿäǎѦĝΉӆʚ\x82ћϳϦùѣŧƘɾȫΤů',
                                                                            'ѶɞңĜǺѓ˛,г˖ˣȨϞʓȯΊҵÍͲÌѯɿʐÎӏԑǅƎЖŏ',
                                                                            'ĩҪѡǉѰɗӴԫìǽ˫ǣ҈ÍƥɘҧŪʊʙ˝ϤПˮXʟȠʸλɢ',
                                                                            "ŉϢŅυΩԔϢωȾŨ0ѓŞQ˙ǦҀѳĔ\x99'ϩgӌǇϵʅӬϡ˳",
                                                                            'ÐʎѹɠɼăԘϪ&HǭçƗҨŷςȶťNĂϥѰĮʄƛ;ƤӼɢѸ',
                                                                            'ԇΦŪąƺΩԉґƌȭŠϸа3\x94µ˥/ƀԀ(ӫƷǡӴģȆх˞Ӆ',
                                                                            'ŊºɌРōΔƬÅǿñœƙɿΨЙŏΘɄЩŨ¦\x9b˞ǉǿъЫ˩ÈΧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '-ΝĶíçϙ¢ԉС˶˛Ӣҍϡˑ\x9d\x87ŗťӶ\xa0εɶê\x9cƄϭ¾ϥˬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ίͿаʂЭδ\x91\u03a2qɨͲ0śКĎеҨŋ˒ťɉѭǤΥ0Ǉǁӌ˱ϋ',
                                                                            'ɫ\u0380GгɈˀǚȍŷψɥб\x81ӆɓȖÎɎΠġǠʸϦǿʻЅɜҼнŢ',
                                                                            'ϧɠĻҞʢƋьҳΝ˹ʽɵҩЩơйкɖƹɚƑɀ§ҌɚIūˎŉ҅',
                                                                            "'Ñuũʽ'āͺѰǯķū˝ƻɎЩϓơ;ðˀЂΎżǠǓ˖ԥɥӓ",
                                                                            'Ҁ\x87lȩßŮøϬXҋǢƾȇÁΖɛ\u038dԍЙGщœƙЮ¸\xa0Oκӆȶ',
                                                                            'ĊǘȪЎ2˩¤˱ǫΫԉѠϡ¡ө\x94ôΝŗȨ#ʰϰ·Ƃ§ҷÔĕɠ',
                                                                            'Q\x97Īȼфŏ\x8cʁǱԌϹƼʑ\x90ˍθʙƆ³ł#їԌűȬєГ΅ƒ¿',
                                                                            'çЏͰď¬ǕӼÊǼ˗Ɉ\x92ɩáɂΗƀ˥Ã×ԙƃĩԙŜĊϐƇͰɇ',
                                                                            'ȉҠәGӗ\x96Έ7ǄЧʣêϙ\u038bǔ$чƫҜωԡŐzĽˈƠ˫Ɉŗƈ',
                                                                            'ɲ]\u0379ѺʍC˔ѿ\xadӌ0ϙϓʍԝȩų@ѰԢyi,ҞлњȚƝϣʞ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ìώʳœϴΉʚèΨҷyɏâсɺўѥşЌƖĎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3974712718893242075,
                                                    },
                                    },
                            {
                                        'name': 'ˍѥĥϭӚǂ˳ôȎĊǋ˙ŪӽǑ4Ǐǭ\x8eґϬ¥ȵOƪӦɦθ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9154325670669135341,
                                                                            -1405199010132642295,
                                                                            -324525356840265567,
                                                                            9010978302959546765,
                                                                            9108944200088912853,
                                                                            4464474377680830872,
                                                                            -79146932380494227,
                                                                            -8064236428434320534,
                                                                            1972900204931589544,
                                                                            5009618724131902986,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʏѫíǏӘȪѢľсWǆĝúѶҔĲήҴ²BέĲЮλЪϴʸΆЄț',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211027.081727:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ːΩĜ\u0382śʙ\x8eĜγӇӂǖu',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4526406318223409864,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˻',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': '҅ċlβˋ¢ˮѸсĀӚȦΑɝē-ɜȩΦ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƿ7νʔö6ďʬȮĵłԝ\xa0ӖƛúKıҦʻÃѿȝЬƁVzȲԔ\xa0',
                                                                            'ȕӞέǔЈӛԥŸŞ˳ԀǗдӛɈ\x97ԐӃȲ;ǷǁŤФёƤ;ǔɇǌ',
                                                                            'SEÇϧ!ӇİρӾ˗χ«ǄНɕ¢yΤɰƚˡǔ?зσř˕Ɔ˪Ҵ',
                                                                            'Ɵˆ҅˶Ǯº·ЍЋǃҬԚҞ:\x83φÐĲĳǂΡȖ˳ϲ\x8bĪӐɈϘĔ',
                                                                            "ʀҐ˛'ʱʨ҅\x95ҜȜʩѝŜǹѺƙ\x8aӶўƍʛѝ\x94άʑ\u0380Ԇű˪ʹ",
                                                                            'ɉÙŦÕϙǞҎ\xa0ǌԈžȡƠвҜʹȄŁǡτǖԗŋÈʷĊѳOΈ7',
                                                                            'тʯʅ˸όЬϩɷ\u0380ɧьeҽȄ\u0383ŸԣӵÒӡ}ʾέԮӖˋ΄Ьʚφ',
                                                                            'ǸŎкyѴȁӘȿԥǢНȥɓgšù\u0382>ԧ¥ЀӾİc˷ːɦĞʄŐ',
                                                                            'Ȯ˞ÒϨ×чӝŰӗʧƦԆcɴ҅ʿόЧȤƺ¶üòƬēΥҋìĎɑ',
                                                                            'щɭŻŗҳŹÍγԡȣƋӟ±TԔʺȻŅϿ@őȾБɮʹǭӋıʹҔ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԉǆòϷðɏāάȲϷnɃ¨Ъʒ7Ġ´ІĘČGԃǂΓȎǤȝŌn',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5970636045902533442,
                                                                            -6881754383695301036,
                                                                            5251340849950720093,
                                                                            2394516025374714523,
                                                                            3185160109338403057,
                                                                            1324297284968771803,
                                                                            -4262472961293698237,
                                                                            -8549624009143045237,
                                                                            -532065999689446514,
                                                                            -4514985750374278482,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɛΗ\x92ƥϾ£ɃƓc˧ĖʈǙҋɸѺɉʛЄʪʗҚп·ΦԪї\u0381ūǂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ϣʼЦϐƻ\x92ӶǳÇυŉ\x9bčɀ϶ėϹÊϲӌʉɜR'ɹҘŊǇ¦ʼ",
                                                                            'ŬҿʝͱǛщӓǷĺ΄όɶǹҵĨͰʢǔʅIüʫҊʛɧȠēґ˼ϓ',
                                                                            'ԐǭɅҬȝԋϭΥ?NŎúӱŽ£ìŬ͵Ƥˇ^Ė˂ԤǩǑ¹ˀѪʸ',
                                                                            'ӄǯśҟ¥İѥm˦ʛтɬΆɘȄΛλʑӗsӴȡѯǝҔʹ\x96ìԟȰ',
                                                                            'ϣˍѱɦƂȹǾȻԞȱņɆы˲Ĭ_ĩŇū\u0382ҹ5ɤy͵ȹƨӁ÷ӳ',
                                                                            '¬ӨЀȁҜʌŏϡϧԤӊЫɛԐҺɮċǷӏ£ʩʣԒԒћ˥ӵҘʹҶ',
                                                                            'љьʓΒʆά҅ÿ˞ҹȳȆ\u0380ԈPҁӪкȌ8\x9fƻӓҖɒ˔\x91ʰ»ǣ',
                                                                            'πσ%ǁϹǩιƍϢʤҢԒȤ#Ω¯ĊÙϢɓЂĲÆǬԈ˂Г¯OϜ',
                                                                            'шΚ²ƅҋоӏνЛŤҧҕґôĩąϬȈгNҤȚѣĦŸˬƖ˖Âř',
                                                                            'ǀ(ßê;DŤ©ӗ++ŢцƩTĒґnћ\x86ǇȫēҜa˙ʜӒҫʄ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǽ÷ԏԢηžΦџӡ˅҇Ý]ϝʏ&ȴ\x85ʁѡԍ',
                    'message': 'Ԧ½Ηÿҩ϶˸σňĩЄ\u03a2ˣжɡ˭ϜƉǁʝɕ\u038bҷіÐǀФ˸Ĵȧ',
                    'arguments': [
                            {
                                        'name': 'ҥȷЌҭʇʮĬҿӘеlʾїóǤĈćń˗ʌď¬\x95',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            254073102954061743,
                                                                            4680300310397617557,
                                                                            -8973611826108513487,
                                                                            -1532983896941274148,
                                                                            -6634076483646239541,
                                                                            -4044978110059818395,
                                                                            -2335610482272153576,
                                                                            2481657111119955160,
                                                                            3275319220156449229,
                                                                            6657945469544319184,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƅ˙ү',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211028.909860:+0000',
                                                                            '20220526:211028.931649:+0000',
                                                                            '20220526:211028.952044:+0000',
                                                                            '20220526:211028.973878:+0000',
                                                                            '20220526:211028.994709:+0000',
                                                                            '20220526:211029.016854:+0000',
                                                                            '20220526:211029.037979:+0000',
                                                                            '20220526:211029.058756:+0000',
                                                                            '20220526:211029.080499:+0000',
                                                                            '20220526:211029.100537:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȏѪkǁŚǂӇǩӱӆʡuǽǶřʍ>[Ƥß',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1980409358530319339,
                                                                            663461295803534549,
                                                                            -3484526909670647434,
                                                                            -6368624871383165271,
                                                                            -7626880219177330928,
                                                                            -7472927753759075913,
                                                                            9135055783061608774,
                                                                            3819698453268928992,
                                                                            -2686357532435946432,
                                                                            -4228633780433385629,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'пȉʿњӃ҅ҙӼːΒa)ǃˤćǃHǋuЬƷ%ƃɠÚöŧЀМ',
                                        'value': {
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϙ#ӘʌʓĵȧƘɋ˸$\u0379љӵȡÀƒϫæ˩ɀǄ҇_ǃґåҭԔƻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ȝ\x82XΡήʪôæĩώŖѰϐЕХѐѲӆʛô\x95ǪҭnʖdŬ¹ѽʫ',
                                                                            'ӝħͱłύśǂ҉ǻƨǨǧǂ½íǤÒMȥċѴŁʎgĈʎƆǵӊ»',
                                                                            'ӻùǩɐXÌŽԧäηӝ\x91ǋΠӮ×Κѻȟˍj˄ФÌĸċʻŽŤƋ',
                                                                            'νǎ \u0379ǆƒЕҹѾԆƭǜȇȶӀӲıͶǸʢ6ɢŠѦȧŻѰIƜӮ',
                                                                            'ČϥœLāȫǦ\x7fҫѷ¨ԂȞʅɕʇƫ%ё˘èÛӁԂ˳=π\u038bžю',
                                                                            '˳ư˫зѸǥĴȻҖΒΌɝӅԬŞЄԋɩЈ҈Ǎ\x91ǧьȾǛԘϜřŴ',
                                                                            'ӥŮ-ςϮԣŅѝѺʓӇ˅ШŋÅºŹҢһʗȤ\x84ɄСȿʟ%ЈΰŪ',
                                                                            'ͱˏћˉ¡ãċʽϬΙАƗӿ҄ѻƙΔ˖ʻˡʃҳћӎÝɝɢɰɠ˰',
                                                                            'ɣţĭ͵ԅƷɅʴâʏʢϞϒĒɁˠ¬ùҌèǿǢ2ͷ@kҖ±ʡӦ',
                                                                            'ԟГǤЭЬΞɳӉÅЩɝɶϞ\x9cɷЀȶƇϟ@ʗ.ɱӹΘԉɳӭÎĀ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǧɟǝЈҚ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 479614.94916842703,
                                                    },
                                    },
                            {
                                        'name': 'ơ˼ĉĆùǿͼ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1699539632352793610,
                                                                            3050140357283787970,
                                                                            74330713488317126,
                                                                            5524910791932212508,
                                                                            7530918145659742697,
                                                                            -9169105597799122845,
                                                                            6665910271987231861,
                                                                            5810902431076823762,
                                                                            -5428316135467842485,
                                                                            4219260195837441578,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ļĤπжϒǙǃȳǐ\x80ӺǣƂŪĎѼӫʁӛρШͰѩӦ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'οƸːʉЊŨʏЖķ\x91ԜѰ҃ЪÚЇŁ\xa0>ΖӵqлζРČ/ǌƝЃ',
                                                                            'ϧ¥;ʋ\x87¼ϙȴȁƵΎЎżțăƵԚϨϫаЄˎԐ9Чӕғԙłи',
                                                                            'CΗʦёʱĪ\u0381ρ˃Ⱥ϶ͼƠŦЦԨåɰн!ǓǀƏʹͶČєо¥ĵ',
                                                                            'ɬͷŜʓˁƤȞ\x9bԬǾϐϤpоҜӗÒςιˀ±ѹԦ;ϘVʉӻ˭ӊ',
                                                                            'ӽθӦ<ɳÍ˛чмɔмƭʓϳӲĪ4\x8c˧ьԬѬǅʨθӹϡӞzƢ',
                                                                            'ɓ}mͲǵȐѳÖAˠʐ\x91ŃΦǋȍɫC¼\x93ɵԀˈȘƌѲȪƮϫб',
                                                                            'šɳʿÊȊȘȣC҃ͺȼΓ˯ѬҐǏĥeºҡȯɌԏɝћԫYžƽƕ',
                                                                            'ЗЫǥ)\x9aŁǶŪνрΧȼƓƥќýʏŶǬƲːӇƛǙǯЕòɌȢŬ',
                                                                            'ŅѧÞďɴsξǄ£JϞ˫ɴ˝ƲѦȣӏʭĀѷŃЁў˜҂Ͼԗɝ8',
                                                                            'ЋːϫʬNЄУȗЃʻȌȩҼciÆƖϾԬ\x82ΫaӆЩ ĵƲǨω\u0382',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʛ\x8fʳZԕɘͱǕýбΩԙ!ρϲԉɦԦȆΙƭǓǯƚĜ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            482147.9322297614,
                                                                            141372.05619530196,
                                                                            161528.74518098027,
                                                                            257221.31987846905,
                                                                            17269.415879376218,
                                                                            369962.5321228347,
                                                                            651134.8538665954,
                                                                            38754.66332952454,
                                                                            119394.86664520035,
                                                                            413422.6346207359,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƕƓŶŷΗ\x8b˶ιʬɿěϛˣȝŁэȍLɬӪWʭǂʚĚŷȈαƔa',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7585069578210080601,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϜÄƶѤ|±$ʺ¦YӰԃѥ¾ŖůԀćг÷қΫΛĲϭŮʠ\x99ʀ»',
                    'message': 'ϊȑŴӍŖúʦΞʗǌϙʂǿƞǌɳϖƜêԑʐȆŵʂϩǲʻˊӋШ',
                    'arguments': [
                            {
                                        'name': 'ԬX\x80ɠуӐЬЦƔɪîфΒɷίūêʞХΈǱ˓£ŗǈ,ŦɝĪƤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211031.296362:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x86Ԯļïҿˣâ˝ԗĄҎıĚԫҗȡξԢ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '_ɜӯӫ´MԪƿʩΜԜ҄бѤˀɟƕϖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            750683.4734689983,
                                                                            -8824.313419005994,
                                                                            262893.60391093115,
                                                                            626377.4066120572,
                                                                            235996.08555209357,
                                                                            -74976.04637320543,
                                                                            220990.01185274485,
                                                                            555192.2997473937,
                                                                            2358.277608314689,
                                                                            986208.5312215306,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Č˽҈ɤȹ\u038bĠǁʹҽÛĦҮƑņRÖµΥįҝȠ\x90śoҵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5554851613086706451,
                                                    },
                                    },
                            {
                                        'name': '}Ǽ҄ԁǲŮŻԞѐǙȍʲѧІÀɕǶҺǫԑЭƸʈӉ!ϧǑζxԝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211032.088061:+0000',
                                                                            '20220526:211032.109248:+0000',
                                                                            '20220526:211032.130598:+0000',
                                                                            '20220526:211032.150876:+0000',
                                                                            '20220526:211032.173055:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͿģɘԐʆΫüҤӨԈŭŃąɭӫʭɑɇҾ$\u0383ҧ\x99ήɇқʪӞ˜ј',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            965053.859401094,
                                                                            756732.5257606778,
                                                                            310442.93178364256,
                                                                            -65181.885009863174,
                                                                            954458.0726384441,
                                                                            441011.9017783117,
                                                                            455605.6223794983,
                                                                            -13730.502453871813,
                                                                            857903.2209548007,
                                                                            -26105.231169937964,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ',҇g',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '^ΙҧïUɗϒǼ˃ǉdИѻɶAϚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ψеВØΐƅ˓Сŀ7ЁȀӝɢ\xadѬȐƭȐβǔʠϑƕǸʗɣɐʊƪ',
                                                    },
                                    },
                            {
                                        'name': 'ѥŊŶ˕8ЈŨșӒdnż˽ĳЊĺƼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӡ2ƁѸƴŐϵʶțȒʠȐ˲ƐК˳Í˕ȇϮпЂȝÆŮЊėӫԜĉ',
                                                                            'H\u038dζƉͿϾҒɪǈqʢũԡͳǝƝҺ\x87ΆnņˢԢĿ˽ξҲkѷЎ',
                                                                            'iԜοҠԊėÏѤȻԦԒЦ?ьƲλũԌ¼ǋџ\x90ҞћŏϗȂʤχ˙',
                                                                            'ȭӑ°ΤҜΛIʡ\u0378Ѓ¯ǠӸǟђɵҲųʨǒжΫǜɅǬȱƘ˫ǌ*',
                                                                            'ʖҸǕӀҝԊ\xa0˦íŁҴĵȫɜϠҎ˷ѮŝƺƁџйǡā¶ƜѳŲϸ',
                                                                            'Ӽ\x95ҺͿ΅ҕϡρџɨŨǭƕƚʳ΅УΠҴƊĲТǣ˖ϡčǔέҐ¢',
                                                                            'ӢҩòûӘšʳĒӒ\x8d+ˇӅÈ\x92αoʷѕ˔ǗɌÀЋłшξ·Ƅӂ',
                                                                            'ѮΎɘȨсҷ«ϸɓϵҴȝӥͽʔеЍѰĔǾɫʌӡńЯǣϕ)ɪɟ',
                                                                            'ŻԌƗȘķьp\x7fӖԙĎ˦eӐīÇmͺʶƄȂøœǒ\x7fЂї¶ɠU',
                                                                            'īǐɼɤМoÉˣӂɑԚ¼ɅШĢǛˇͻӏǋƛ<ύ·ËҘǦʲɊҠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԞğŞфΥѫɄȞɡҸѰ˅Ԡӄ˶ҞԙɄӻēɓԪƛοʉȔÜħǜĘ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 949298689752950136,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƄϮϓ4Ǩ˛ĚĪʰʪԢ÷Ȕà҇ЦΚȒ}бΏh\x8eȲÓWčűϳӾ',
                    'message': 'ЏϋЦȐʀĶиBƨVɲТЀ˚ҙ҅ƞøКӰΈąϾΨʎϾϋΓˏą',
                    'arguments': [
                            {
                                        'name': 'ӾƯӄȹņÚʻӦӗʗΜŮΧ\x7fҏθǪžĤǼüθĸǨʐɷĺͳųԍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɣԆЊϙϒҽρÅʢļ˯lіӈιϸϕьʐѐśǓƑоŅѕǜǍԚz',
                                                                            'ʣҪƽӇ¶ιƜ˚ȬĉӅԨĥҖ»ӾͿ˱ʆǝɈƄŉ\x83ЛƴƅWόǱ',
                                                                            'ɶ˨ɼʣϽȏ\x8fĽȿ\x96ǄĬԨɴÓӡƽőłSсɿûζψĎĤ*Ζ3',
                                                                            'ƜϺƾОҺС¢ӞĩшӴǑ˚ɳǣЂȢЇуԩӀϤȻ\x88ӛϰȢŏɃɅ',
                                                                            'ɨΖ҉ƾʅɀɖФuƮƗϔÙǳӋϽżŵʦ\x9bӟȅԜȒĥɿ˰ԞӺʱ',
                                                                            '˦ПʮҒ¥˔Ʊ«ɜѣʭƇԙɼ˂ÎԎχϢΈ\x8aǫƠ£ѺӉѲЦǇи',
                                                                            'ȌˁγÉʝ\x9dʽԫҹƿϏџӣ϶Ԇϒа\x83ɇǷԬѭɯɯΌʩ˱ыӏƚ',
                                                                            'ŷЦ҆Ϗǐ&цǅҿzÓˎԥɅÅʟԙÜӵʉ˯ҏǱȟӣҀɾџЧҼ',
                                                                            'ƄȖƦсɝрӔŘŌӛԅǖΰОŻƎӴϾάɴӔβɻĸǵҗtϓѧɠ',
                                                                            'PIɏǸƓʭӈǎɚ6ҧȢѢΘԒχƜĴƈήЊ˫Ĺŵǽ˘\x9fÄ˖Ѿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȍÂԢԮθǯ\x9cźǶǶԦǒѢʎʞŮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȌԃʡđĮzƐȨϜɍ\x8cuUƝҹƨϧÃǒ|ŠǡŎŋƟĭί\x97ѐ˹',
                                                                            'cѿǿƓ!ŧνҹœηΞĥƜņǗǥǏβcƎԋΜ\u0378ɯëȶʐҳĪU',
                                                                            'ɱù\'ϐȴſ"ĺıøѩѵƟɚԫĀͱßǁ«ʀȰӼҎЃ;Ɵѡиļ',
                                                                            'ÁĬˉƙɂЖȋśΨӪÜ®ņŶɲќ\u0378ŲɡҺϾɏԇˁɩӒҷЪƋ\x97',
                                                                            ',˩`гѤијô¦ÇшͰһ×ŚҦ.ƖӉЮʦʽ҉UŨӲʻ¦Đ`',
                                                                            '˾GƚѲϹ³ҍӛӬоƲàҫ϶˵iíǧѢǎѸӼԁË\u038bɽoΆτţ',
                                                                            'NǶȇЩǟū\u038d\u038dŃԭɾӡ\x95ƏȪѾЂLä?ʠ_іÊЙЯĻ˾Ɨԕ',
                                                                            'ҿMʐ;А,Ψ\x8bȅƉÎɥɠҰəһıÑМҎǑɑĺƨǚ˝ɥ^ϳÿ',
                                                                            'ĵΛԠΌz\x9aӜǮǛôјǧ˲.ķŶ˼ЍǟԭӯițƏ#ѰΌӛ-И',
                                                                            'èŰùӮԊ»ÞRΆbɸDǄȌҠƧΫǕ{ќДrȟȱŒʹǿ©ǹ˹',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЉЏИfәӫx¦Ȋɕŧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5271148038323728576,
                                                                            2578279161240827666,
                                                                            -2256403269435509557,
                                                                            8294708458036567129,
                                                                            -6431636673287255628,
                                                                            -2839789448184279643,
                                                                            1548899753555342024,
                                                                            -3660966731116435601,
                                                                            -7663729003076048103,
                                                                            1457921205811505701,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ζȎ»˭ԉӜȀÌ˞¹ϥȐɖĎǛѫŰƖʝΓˎºЯӚύɴнȺ ӑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ȑ°ƮĹǊEϚҪɃӐǘǇɀЍîϦ9ӳʵŶȣóһʟɢϊʍȔȗȋ',
                                                                            'Śʁѳԑ˸ÖҌѴˡӆΒҲ˞άϓƊºŠ±ʡďƚƕˌȏ,ϳňͱ҅',
                                                                            'ĶѯǛ>³Τҙ˼ҟэͳɧƧӲƧЋӌ¹ќϯɋЄƐÝ¦ŠͽϺòɭ',
                                                                            'ҥƅ¿ĴxѥǷϽcʣԟþɫƀ;Ԥʚʴþ΄ѯЬ\u0382ψ\\ǍҡɇŞʴ',
                                                                            "ƕɢʥΧԈϲ'Л3˃Ð±ƲàêӲсʨкȎдHȤːЊ³ÏeäӤ",
                                                                            'ơʰÈγү\x9bƭҦɴҼҴ\x8dҙҐõĉԬкʞȚǆ˻т˛ʈ˞ÆĨŖ/',
                                                                            'Ë˥ÈùmϱԚҊǶțԚ҆ПɜцҪŴȚЂД2\u0382йυМ˟ʓǓԗɔ',
                                                                            'MȯĩɥҴʈҚӃҎ˨ЈÁ-ɰɡlɻ҇ƒНίϢǔҒĤŋ\x91Өɿʺ',
                                                                            'èǚ˰λ!Ъ\x8fβӛ\u0378˸ȹǛQˑΨǞЯʼ˾Ɇ°ӕŐб³GěѽP',
                                                                            'ѡŋÓǢӟüÂ˞:δʽӎѺ͵ɋɘÔԩЁ˟˱ǌŎӼ3πʧˬȸȃ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ӘТƺʇàĒҫξфʰЧsїǭ'ɺͰƢǥԂĞƤˍ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÒЇĂɨɳͺ˩ûİƚ\x96ʼØȜɿҳê5ПʆÉрʣґɻwȼƀ\x88(',
                                                                            'ɰ3ǧԂưԉӁĪǛ˻ԅǣĳеԒlĠͼ\x8c҉ʾˍԙÆɩDȠZлɮ',
                                                                            'Ӷ˼1ĈԂƝѠwӵǼΙĺZԀө\u0378\x84~Γ;ѪӃӱΤÀӒȗǼGg',
                                                                            'ɜϦ˸ɑņҘĕҨcŮ˕ΟѡхšŸűzǫíƈѡɎÿҸИæϦЍ\x80',
                                                                            'Ĩ\x94\x81ҌġXǱǑĖǅ¥ɍ˒ѭӔǷȦͶΐѫƹɎфɁҡӛɀ=Ơʣ',
                                                                            'ЄІΝʖϹ]IЯƧҢƿʏ˂!жǉɣƒӲÕśŉԚSƃɀџТŎҰ',
                                                                            'ϷӱΓȜŉқԀƤ\x98ίΓȉŗ÷\u038dǌђЦԚÔƶΣĔʻӶѱƱ?˵ǒ',
                                                                            'ƢЋôˀǠԥҼ¨ʇm®ĖĊЎVΆԥǈϑԬČª\x9cҫǥǶϧԫĸÞ',
                                                                            'ÉƱʶɻ¹ϛԋˢȲnϟǋ\x94ʿÂЧɐƦϾ\x85§ÙŚ-ϯŕuʋΖο',
                                                                            'ԒeѴӬ\x81˒ƷςiԓƤɨƃЧЄǙϞRĈǰCʋԪϵбĘѭԀû\x94',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƅˈ˰įʧфƁˌȠˎ$ʟ\x8dȼӰƝͱ˳\x96Ćња˓1ʋѽ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 313942.3198429088,
                                                    },
                                    },
                            {
                                        'name': '\x99ːʀˡʪѯиЩôԭɌ˷\x9eƛӿmľŦˀǝéF<ϘǧӀʚƽӜ˶',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211035.109617:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÑʹǦŤγѽӴюɅſ˝Ѥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211035.207983:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ū6łøϳt{ʔŢ÷ВӪԨŋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3606888644284251394,
                                                    },
                                    },
                            {
                                        'name': 'Ӆö',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            98156613825310253,
                                                                            -2844265193187929198,
                                                                            -441481024714220225,
                                                                            -1284873482927155439,
                                                                            -3101834108120870567,
                                                                            9088482179535302740,
                                                                            -7691386303277302730,
                                                                            907813843547458656,
                                                                            4190330802809802574,
                                                                            4723486185887974080,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'şØƫɢWú8ǥŦЗŵƑɢěΙҟΜƚ%ŊşΕıǍӁͱԫҶŔː',
                    'message': "ρTТǩŽ'ĪӃұłҭӨӛҔŹ$ҕͽђƕ½ɗДʆϵ҄ΝѓӾȓ",
                    'arguments': [
                            {
                                        'name': 'ҜÊфƲƿ\x89ʥ˗gǌ&ÆМВвƇЈʊϼ\x9eǦҊЁ҄ĲYԜϤhƟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʣґ˒ƂЛʽ˅ϰΘŴΝҵɄɼѮǬͰɩʂԨåȠɓћɩѯȀɼý\x8d',
                                                    },
                                    },
                            {
                                        'name': 'Ϟɾǽɨīϸ¬ɸĐöҪɹǃʙĠȾ§τŐÉŰʺщŊȌ@Ǭ˴ƿ¥',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȉȴԍȕĞɌ\u038beΒԂʪǵЖϔáбĊΆтӹɾȕϪŅШτЙʢҶɫ',
                                                                            'Ǽģȝ˅Ӥю¼\x96ѾšƙʺƂƅŪ˦ɸƖƶɞЭѸ\x86ɈȎʋƽРƙȚ',
                                                                            'ӞƟθˆԢǏѾ˭ŅԏͶʹƀěˁ½еҽҹɂ%Ӧ˭ȐδιԠЎɑȚ',
                                                                            'ӆϴђņ.хѱҨсJėѸϢʐϣюΤҐӚɴιʷӖҽɦМųѫĐҎ',
                                                                            'ɨŠЅΉӰΡԛÔжѮʒãǿȳǷˀуͺԥϧґʚìҦŽ@κ\x81¤Â',
                                                                            'IʝӭһþϴƝɹѡϷȴĩŪϡˣӟɐӞ҇ԦϧÀȵ\u0379ǸЫѣOɂ҂',
                                                                            'ƳԢÐŭρ¡ӧȢŰϘώαϧÑƂƫÏԏ\x81ƽÚʴ\x8cКȵ˖˪\x9a¸$',
                                                                            'ԏŕ¸×ûҫЙԗǔAԗŚӶУ\x92ɠïυҴҨ|ƢǫѷFϱɊ÷ԅ6',
                                                                            'ʀ\x9fÄ³ОòƝ½ĆԏͼĄʨДˣƀ\x8cũǾȝeƬїΚԛ\x987ԜǣЦ',
                                                                            '˥\x82ªѱ͵ӱ\u0380Ĵ½ÆŹҋԜˠ¡ӕԎƞМΛпҊ\x99ԜǍǻƓƊԛѪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¥ҕɚЄġƏǀŞȀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 985639.8705744073,
                                                    },
                                    },
                            {
                                        'name': 'AΉÐƦ\x89ʲǽкęǸβű˰ӫϣƣŷʿǜΡİʋʯϕŜƕȇӱȋǇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211036.365440:+0000',
                                                                            '20220526:211036.386727:+0000',
                                                                            '20220526:211036.408748:+0000',
                                                                            '20220526:211036.431165:+0000',
                                                                            '20220526:211036.452829:+0000',
                                                                            '20220526:211036.476355:+0000',
                                                                            '20220526:211036.497302:+0000',
                                                                            '20220526:211036.519933:+0000',
                                                                            '20220526:211036.540588:+0000',
                                                                            '20220526:211036.562022:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '³ԣϵѶȳƔϛϤɦ\x8cȣπԈ͵ІķÎЇĆΘзӽƝáЦmŀĦµœ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -99734.12725429915,
                                                                            564507.4243645079,
                                                                            293908.29563266877,
                                                                            624806.6309190097,
                                                                            885021.1076373466,
                                                                            -97199.29206996674,
                                                                            839389.8440132658,
                                                                            10245.293933599227,
                                                                            804652.4800298825,
                                                                            144737.88376415856,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԇ¹ɻêɅǾ\x9bЙʷɢȉӵ˼ʸâʕʸʺϵʏǵǟӏÎǵԣӃҖǝʾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 963289311151249189,
                                                    },
                                    },
                            {
                                        'name': 'ӶҐ©ΐʌё',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϮȸδԖҦҔɣсӚǃЦΚ\x9eϗǠɂӄԕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211037.160555:+0000',
                                                    },
                                    },
                            {
                                        'name': 'öѮĤđyħǀƶCђʞϵɏïņȇüí҇ӄâ°ǜЎԔϷʹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                    },
                            {
                                        'name': '¼ϰ;Ƿˈ·ԈЦȺ?˾ҩ±|ƸǣӔӲԧȃˈ˖\x9euΡԩøӨ\x92ī',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -801454178152921640,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'НƽԝÐΕɽТԘ?ȟɫŝ#ʊɒˤǄƗŰОúĴǡØҞԇǒ\x80\x8dӢ',
                    'message': 'ϨȆӳϣǷΫęЫ˵ˊŗÉώӛʳfȏ ʌɁƱ1ǰĠȥřάЈŬɪ',
                    'arguments': [
                            {
                                        'name': 'ǸƔşˑї\x80ћȩԦˀӊΛыˋé>',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211037.750007:+0000',
                                                                            '20220526:211037.773477:+0000',
                                                                            '20220526:211037.794465:+0000',
                                                                            '20220526:211037.814884:+0000',
                                                                            '20220526:211037.835477:+0000',
                                                                            '20220526:211037.855518:+0000',
                                                                            '20220526:211037.876296:+0000',
                                                                            '20220526:211037.896832:+0000',
                                                                            '20220526:211037.919461:+0000',
                                                                            '20220526:211037.942687:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЅЉʿԄӟЉҭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 71554.34457208417,
                                                    },
                                    },
                            {
                                        'name': 'ȖѤ³Ȭǒɵ˝ùяeǎȾÚӃͱȌÇʎ\x93αӄȀÌǃëʄψɅѩ#',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ÛǁƎӮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211038.228322:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɾПΈǉԗҾ˳Τ˭',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǂȢČЦ\x9fǐĻˋƪӰǟԑǿФԥϼɕūɤĭƗҋº¸ƾē',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Čɚ¿Ėǽɏƹϧԥã˼ʨҚхťɓԪʕΚʼҋЊҗҐˤƯʗѪ\x85ˊ',
                                                                            'ӵϒӟæͰԭʍǪΰǼҐԛĶ5ȩɠȥˤцɞίĝӄͿԍҞŬΊҭȔ',
                                                                            'фɌYˏâīNƭǯ\x97ҤЙЋŪʤÿЫʊ\x9aƿҮʵӢqˑц;ѫӔǆ',
                                                                            'ξЛϗ˶ӏɚʯυǙƕУŽDŕҶѩ\x7fáƁ˰ζǄрΆȲαХʗĠˈ',
                                                                            'ʭ\x7fҤўɛÊȼӵ£ԃͺYҖ·˸ϊҊҩŢƶԖƫFɮϽԁӌ\x92ϿŌ',
                                                                            'zӎ:ĺɅȞǥҕɓϚѡɐƍǄӎǭΰɭ\x9eӍѴĹϫʠɷɷÇ\x8cTϬ',
                                                                            'ЦÆν¹ҷìƆŜɺԇòҧήϐɨɹüΜǳīȢҎΘӉӗШȨȗӑǢ',
                                                                            'ӼɹҮ҈ĜŽҬсK\x97ǬŻƳñǺӊÝύºǦѹ!®\u03a2ГƳ\u0379ǳԘû',
                                                                            '¢0ƋɓƘ<ǅ&ӀΌʹň϶ǽ«=ǃӆ\x8cÕĽηʕԞ˜ʏɿ͵lϟ',
                                                                            '\x93·ǍυΏ~źȇǦԧҎ΅\x9b«ƺΫΗǏЊˢΔ°ԣ\x92ʆìţȓҳѯ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǭʝſΏǿţȌҿрȗͽė¶ϛčÆǷΎӴ˰ºΜԙǷʲÃǏ\x88¿Ʈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211038.716305:+0000',
                                                                            '20220526:211038.736655:+0000',
                                                                            '20220526:211038.756685:+0000',
                                                                            '20220526:211038.794148:+0000',
                                                                            '20220526:211038.814155:+0000',
                                                                            '20220526:211038.834454:+0000',
                                                                            '20220526:211038.854446:+0000',
                                                                            '20220526:211038.876597:+0000',
                                                                            '20220526:211038.900986:+0000',
                                                                            '20220526:211038.923855:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΧȺԟКȸ϶ÀçāԞǥшʭǃ,ӮȀǀ\x8eéʜӉЧĜ҃žƯʊƇȐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211039.070871:+0000',
                                                                            '20220526:211039.093950:+0000',
                                                                            '20220526:211039.117020:+0000',
                                                                            '20220526:211039.139083:+0000',
                                                                            '20220526:211039.159701:+0000',
                                                                            '20220526:211039.181340:+0000',
                                                                            '20220526:211039.202154:+0000',
                                                                            '20220526:211039.223327:+0000',
                                                                            '20220526:211039.244012:+0000',
                                                                            '20220526:211039.265818:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ηЉŚƧȿˋɇӐƾÛˢΑΊѐņԕķԤȲК',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '=ӛѳˇŲяɛ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1590371331368813866,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĉԥМƍѠĴҼˋτǨмɺѭʦ9ʗѳҽʿΙжψѺҨҴɍñϟͽє',
                    'message': 'Û΄˭Ȟ6жӜΟԞΚҢеôΆӃΟ˛ӕѧіΥĺÏʴνɊˁНОƵ',
                    'arguments': [
                            {
                                        'name': 'ʮåŭ4ӻĂqɛӤóɑ\x98Ę\x94ƎεǳӝԉƥE˯ĳÔȫĪʃȍǓw',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 848153.473781143,
                                                    },
                                    },
                            {
                                        'name': 'ȄƉöɕӒʺJηƗ_јџìрp',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˌљѼĽʖ\x91ҿ\x99ÌÐϝδΆìɡƭŭɌȇҁϱӼĊφԥбȨżìǛ',
                                                                            'ϲ˒ʉΖ˟ʙӠԑŪʙ¨ɰğȔpç˩ŹǫԐςЅȹ&ԒˇԦȤҬɕ',
                                                                            'ί½Ԥˏөαбԝ΄ːǄĤȫ˧ǏÝΚ˥ͽÅȤ-œЅáƗцӽЃ\x92',
                                                                            'ӟԩƷԧɄÝʡӏѣ Ľģ˱ȿԫçØ+\x9dѤɠǠȣĞϚ˒Ðʸ³ǚ',
                                                                            'ʱʂŔΧԐxӭƜğ%ĤţεɝӨ˰˟ύȚҌͲɇêĲ_ǉПкԠԜ',
                                                                            'āԡťµɎđɛ˚ˡ˥ΊȘƱȷβҗӥѿ϶ϰÀҰčȀĕȎΨȬΚЕ',
                                                                            'ˌƓѴ®ґðɝÅЪЊîɧŘõχϘ©ҝϚѿϬӠ\x8cΫÞͼùʥӚť',
                                                                            'ξ¬',
                                                                            '¬ӵ"тԞӪŶýÈīƏoСƲʛуǗɛПIԆĨ]ƃö˦ɐԑĖĽ',
                                                                            '!ȮԎμǖЮͼǒѧ<ƩҫҀǙԑӻЯɥԇƏϴǨΓћӕǉЉɆФ˪',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'dkΐɭƼnҫɍϲȖɤ}ȪƴBƚӭ®ě\u0378Ǥ\x80@ӧ°ї^jǤӵ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƕҥмАǨˣСЋѡŕƖˋσɊӌĘôВYә+ƨʈҁԫɽЋǼĄ˻',
                                                    },
                                    },
                            {
                                        'name': 'ȀMʴ\x9dɦćѴҏΗŝԄʿŕͲΩňҶŌȋƁ\x85Ɖΰ҉ʡЊźËъ¯',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211040.323466:+0000',
                                                                            '20220526:211040.342830:+0000',
                                                                            '20220526:211040.363003:+0000',
                                                                            '20220526:211040.382351:+0000',
                                                                            '20220526:211040.402671:+0000',
                                                                            '20220526:211040.422893:+0000',
                                                                            '20220526:211040.442472:+0000',
                                                                            '20220526:211040.462495:+0000',
                                                                            '20220526:211040.485192:+0000',
                                                                            '20220526:211040.504880:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҔЌǅƆӲʭ\x9aΆЃěʗƜԑ\x92ìͷɂ\x9aoʻŞĢˮȭѴϣŪŒÕ\x9c',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Δ~ʼŋʾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7963379312318614615,
                                                                            3834041608590012605,
                                                                            -7492100915217271415,
                                                                            -3114677573158195396,
                                                                            -731921556025560378,
                                                                            -1510542561139072472,
                                                                            -1478118450305351990,
                                                                            -3928971913684314734,
                                                                            -1238927779246256902,
                                                                            5129314328335616579,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϒ¡ҳ¶ԂлčʼжѶƉŚҾԉŸѵѧƂБ˝+§\x94ЖɂӉƟҐĹ>',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѮÀШƟҏśҘҵ\u0380ưЍ\u0379ƄԖѧ|OЙɬŧҕĶĖĳԏ!\u0380ȖԌϮ',
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

            'identifier': 'ǵƳźƷƽ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': 'ơϙ',
                    'message': 'ȕ',
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
            'name': 'зįʽļcȯȭūuǩΕȗĔȯŖ˻Ƴ\xad½ˑҢсϰǨԑʦЬʗȍǖ',
            'error': {
                'identifier': 'ˁԩǴDňːɧ½ӬǲиǴӯϬŉΔѪǍ\x89ŉý\x9eʇȿȘΚɬ|ҠI',
                'categories': [
                    'invalid-user-action',
                    'access-restriction',
                    'internal',
                    'internal',
                    'configuration',
                    'invalid-user-action',
                    'os',
                    'invalid-user-action',
                    'network',
                    'access-restriction',
                ],
                'source': 'ҔϼǴʉʲ ɦԕѬUϼуˆȨɀǂʸʈ҈ѼΕϿȏDľºɅ˘ķӰ',
                'messages': [
                    {
                            'catalog': 'Ϯˠʿ\xa0˷ӚͰӑλԮɦ]ʭqƜ©\x88\x92ɠǉԑУԥɋϨЍď\u0382ʋʼ',
                            'message': 'ȗʒʔыƧˑƆŽƪєШҌʫԆ¥ɩϣӥΌҬźͶČǞ΅\x91ØƋĬŋ',
                            'arguments': [
                                        {
                                                        'name': '\x9bÊԟ\x8bɭӪǹФЉǻҹԘȲǢƖɩΣãgȪģaɅԧʈǁԁЙө',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3162640560046198831,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÝПȠӯÞȎΚǰˋҗơѪѲƮhƵˉЉǷĎQѽΦ¥ð¶Ļ˥ōĥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀrύұ˺]Ȳ΄˚ÛȺ˹{˟ЩɃʟĈȡƪ<ǆȨ:ҶĒãʙÜň',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211012.425850:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɲʨƦçȮŔϹæф˹ķүӻӸƬƺt¢șȑöԂѺ˴˫˟ҵʟtʒ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԀĦ·Ү',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '-}ɨrRɝ`ĬѤŜҜB¥ҀƗѵĭіâȿƃ=ҎĈϽȚЏʳļЫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҝцȏҴϩƫɢ\x9fӪĀØǦʫΐúbʳԤɻϣǇяԗ8ѥƖ»ɉäԓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǅûŇʭÇʙBƌӷюãӨЍ;ϤΤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 752024.430227297,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԢˍǊӖxÑӚ°˷ӬƦԢqΥɷМӘϾͺԁúŉЎɼǔƛǁƌҞе',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҋp/ͷύωПυŸÿн҂Ҡԋ~ĿԗˈԜӒΨӬÿ\x7fɏɥƴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ªĖůҧҸʨƠʎ˒',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ұ˲Χʭ˻ϠĉӬǏ΅ΣД\u03a2ΣăǕñϾΑѺӬ#!Όһħψ˥Ϯʅ',
                            'message': 'ȏҮĂʎʩƙǸ҉;ǕňɿӚÑтȳɱҽjƾ[Břƹηӯѕ}ҮΥ',
                            'arguments': [
                                        {
                                                        'name': 'ѹ˓b\x89ԡӂЊǗЙƳʫўΘҦъјĽѯç',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211013.191790:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'мhҺėиȩªηʂż¢Ҁʥę',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԔӶұǝ˚ӞϛĻϷɋ¬έřİˡ2Ʀɋǡ\x90\x9c¢ϼʸБЬѷǰΔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211013.364160:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ăυѤΙũʽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211013.450419:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥßʥѨcÓˀʻŶö\x8fȒ˳ǣͰƲԀVċӇŒ\x8eΒƇʃ`ɛ˔ñР',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 729388.0264571233,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅı',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҩԈΗˆϽҮкϏԅǹȣКΘÚЋҁƣźβ~ŶϩǐÉŨƨƋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˢЧ\x99ϕʕіԣɱɋҡ)ӰƸͷɁ\x94ÉѢ\x9aЄʵҲĪhХ˄ȍEȱĴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΰη˚șøҹЅӸҷΒ´ёȽҹñҩНѰЫÉ\\ԉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁϏňмɘȷΕϖ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԃƦɍɏψſ\x8f³ίЖѬƬȘ˓ÒԆҕԗ˓ːȻɤgϟ\x81\x99\x80ǮϻP',
                            'message': '˶ȜʀȮ\u0381ɚʃƌɷɺєTλµJŒЊсƞŉžáˊƎ˙ƿˣԨďЗ',
                            'arguments': [
                                        {
                                                        'name': '|\x9bOԛÜˋƅΘϥΛӟʛ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6173103751891907661,
                                                                        },
                                                    },
                                        {
                                                        'name': "Μтç҂ɘȓ'ƩȠѴҡŧҀŖεƔƕãϏƦˠǋǳԄҙƜαãƀϛ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҍϽţŀɏɟôĠЉ\x85żϞɠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 847825.6341367959,
                                                                        },
                                                    },
                                        {
                                                        'name': '˟ʹͳɂÎБÐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ш\x8eϻҧУʁŅӫƘ2тԁĨ˔',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫϭaӴŔ˃ЭĦӭ\u0378ԮqǠГƐĮǺШ˘',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ϋʜ\x91óÌӆʰǏ҉ɩ#ρùˢ\\ÛȏώЈοÊϷțcһѶɛ¤Ʈ˰',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԒҢĭʂцŸʑΫи\\Οzɟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'nĤвǖΫǴ$Ǳ҅ɕҾʓǱƊΗʃҫҴГȻ\x82Ӎъϳ΅đɵ\x9eňȦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐάſҴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƻǅŶGɄ\x87ϺӾŅŵ΄ΟϘˣ?ĤěŵʹˎѦýԡҌʤҲ\x83Ãċϛ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǝ˶ʈʼȤόǂѢ͵ďNϤ;ǀıŨҵʘʞ2ÓǫТ϶ƶȳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӊ\x87ıǁȞ<ĕŀȣ˛ТƳφfɮƅȵ¾ɸӃӕÀԋ´νћÚť^Ȭ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˫μϩÎԗһкŔcˤÎ¿ɹқÎ\u0379ö\u0382Ѕ\x81ϪŌ?ϛҼ\u0379ΐÆԀǙ',
                            'message': 'ɶ΄ɀЈŃГԚӛɗԑѣA\u0383ɎʶϘŧžӮ\x8fˬKԮ@ÒÜϰ˳Ũţ',
                            'arguments': [
                                        {
                                                        'name': 'ɮ5όǳɧΙҝлɿ6ύғǶԈƹЙӀǊ˗\u038b8\x83҂Jίϳԗ¢ɇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҚҺɏ²ѡο6Wωʘ?Ȟς˜ìJ¨ƚȺȿӖưћόѢȲҔǁȅӳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀψҔӛԁëʎѐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǪԦǡ-ʻ¶ÄѨѾƃňҨҤӱ˼Рg',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x90Л˓ƌřӄ˨ӴԇфɉȼęӊǩώϞ\x88iǶʨȒѥ˧ǂ\x8bѨϨƶz',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʫdɾѢ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 977225.5397063079,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɝҜѮ;˄ʲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĥҵ\x86ѷƲʺ˃',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'П\x85Ǜ$ĻÔџцφ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211015.756115:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ͻȑÚΉüӥ*˱τν\\ȸĲΎǁϹɞњ'ԍҿԑĹ\u0379çӺɸ˘ѯ˨",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211015.839177:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʋǯύΰЬ˶ʄƺʚu\u0378І\x87ӎʢǕãˋćʁƴĲíɤʤѨʑǹʄϧ',
                            'message': 'ƛ\x8dff˝Зѳ˓ГҸςSƭʡϵäʨ҂\x80ʳ\x8aˀυyũ҅]ϠƴŇ',
                            'arguments': [
                                        {
                                                        'name': 'л\u0378ʥУɯ²ЫʶΥɏʏ\x81ωбßӳĻЯ\x90ă\u0381ϼÝƇçɌ҇Ŕą2',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϧѺgѝƴʺРĕR\u0378Ӓūѳѧȵҁʴ0ҊԥёȁW\x87ģ҆Ȼƅ\x80?',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ìұòlѦ˛\x90ҲğáԊѽԠΗªĽƏǇŤÉҦјɆͿΈ[ԎВ»F',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҉ҼɨÄ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'љʈϐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7811898633902125124,
                                                                        },
                                                    },
                                        {
                                                        'name': 'πΖǦį0ςǻ£Ӊщˍʲˆ·Ͷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'íкʤˆɘќų˭|Ț\x85öӸȂκɞ΅ƈџɦĒΙŨ˪ԏũ;\x97ɌɄ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'îõűЫŐжǘO©ϜɳѽɬȍɛϾÑϫ҈҆ԇȔӧξ°ɘϛŗ\x88B',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŹӦĢ˸іϵӮǄФAƇǉÕg\u038d˵Ū\x86ԈӔÚȶҟ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 989594.5702240975,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѵ+§ɂåͼ;Ҧ¢w˪\x85ɺҾĘϰ\x95ѱӗȨ˂`EÛƛҁĒЪʀЯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2126961740405888298,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊЈЪ\\Ѯ,\x8fʤѲļą ˦ϗ˲ԕØŮ˸ŕĸaÊǘвɧ{цā÷',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɑ*ʷʟԘəƮĞΌӢŮμҕԔ5Ǵˑ\x9dҵχĦɲˀˊʂºʵčӗΧ',
                            'message': 'ӯΔ\x8eƏʰɂǼԨԐ"ҼғŷѦγЦτ\x9aϩŗқͻĭɊѧDсȫ\x90Ƣ',
                            'arguments': [
                                        {
                                                        'name': "ϋɰ'",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 457914.88763322623,
                                                                        },
                                                    },
                                        {
                                                        'name': '˭ǷǕŻΪȠͽǔҩӣсќԮʪʈҫJȺЕԓвŰ˳ŭŧūδHϟ³',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ИбεʧǠʈǳˣɹ\x96ӺĆƏʮѦԔĂ\x85:ԄΞǕˢɭѼΎĉЁΎӷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'șК¼ɹ\x82ʕʎБ϶ѯɹл\x8c\x92оɳҌϰƃұÁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҽҭɣ˛Tͺ]Ϗϰ7ΛӦӝċІӈҠ˪ɂǄ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґРϓԘҖѿʊȚӀѠЖ҈ʾɘ\x97ɢԛŗͱaɔЄʠyʟ\u0380ĐԎԘШ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉԀӓȇǚ΄пԏůХ\x83ɑї˻об˽ҌŪ]Ĺ>ƹҾΘμşȔfʐ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 550575.0961880467,
                                                                        },
                                                    },
                                        {
                                                        'name': 'џӺĤьΙѪBGвϑĤ«щ\u0379Ļʋ\x90ҪѨƪíǙwēҁǵɧƸÐǢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x99ӣ\x88WџƇұɔɼƤĵēˈτgĩˏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 971682.1058414828,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԈʛлύГЈ\\Ƕ#˘ҾsȞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝ&ċ¸Ź˼˘ҼÝćȰǊʑ7',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӾЈ˾śмйȊԂǿѰҴǉčКϫȱïȸ˷ÁΞƢtɔФΆµΔϛǫ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '϶ÉǜŢήϝӆȦVˮΩҔHɰЧΟЫDλʮìЦƊˉ˻ǫſҙ˪o',
                            'message': ';ΐʹĔ˽M\x9cԐԬң×ĤҘŕƨпϠɴ\x8bȋ8γŐξҜѾѨӤǳá',
                            'arguments': [
                                        {
                                                        'name': 'øòӭȐýС9ƁCмʉϞŌԬɶæýʎ4ϡ÷ʽΑ҈nɅԡӟ˲˽',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 916962.1798999035,
                                                                        },
                                                    },
                                        {
                                                        'name': "'ǅÛάơ˻íȵHҊưŸԮѼʆʜ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211017.977403:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЇƽγӪȯҖ\x95Ő϶ʡǑҹǯÆğ͵˸žѾǲʴıԆŰʏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҐϽŚǸз\x81\x98ʤμұʪ\x91Ų\u0380īѺԖ^dȥ˘.\xa0ŴΪӮ}ʝ\u03a2Ӯ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦ6ôǟȝҥɢSUƓψŧśѥ˟ʭMȤϹӏбɗˠƃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɵεŅƱ1ğ˵МAуԒϮ×νӎѓ;\x8fƄԂ\x94ϕ\x8cϭВӊԆɯӗԫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'īVͳїûĪҢӾ)c',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7556552890791437310,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЭʁǸЯ\x95ӈāӄƖҾkʩҺӤl',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˚ԑϪÖËśѻǀˬĠǾό˓ŋąȧ˂Ў£ӧʌКɊϺ˞ӢЍƥɼʓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 301723.5837485921,
                                                                        },
                                                    },
                                        {
                                                        'name': 'yЄҳыΉңŋѤƓƣ˙Ҷґ¨ʒ÷ɨŀ\x8bңѾŔǞӍ"ҪʚVŖ¸',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĸéƱŊ·҅ҭƛ\x9eΌɍʲȇ\x94ʚųɨʅ\x91˺˜ȗͼʹXĒŉԜɵ$',
                            'message': 'ŶɠӇɍsǮƍPӂȣ/ÂϾŢ§Źį»ń\x8a˓)ɥ§G\u0378\xa0Kʵ=',
                            'arguments': [
                                        {
                                                        'name': 'Ο*ɲ\x8cƘɫAĚ\x8fȰ¤˱ĭѨѤȿԧ-Ōʏǋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԊȖ¨ŲĜ҃ƄȬΙɜŵɹǟıβǩӬʼʴκIψĤСɓƺŬΏVԂ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐȠű\x9dƕӀłĜªȼ¬OЃɁ%҉˧ȉnËǮ˃Ҝѧўʅǫȑś·',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƁɗҸ˲ÊȿƼÍыӄӨǥŮʇӄśːƌγ.ӈмɉёϮǗ¡Ƌ6ʲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '~ɞJŒĄүƃʝ"ѹ\'Ԏş҄ȲǯˁωRͺѰTʃ˵ӎċzѮӯˤ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӏ=ʚÝԗΗ\u038bҢ\u0378õҧ¶ɮȎ\\оÝҼԡӈŲÇрʭǙΨӑϒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'l˓ãȒĝǛӋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȔïȭƌӛώƪѮƋх҉\x84ȝѠϱó¼,ɀԇѰв',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Йa÷ЯжɲɯǊΓȢӅлΛǉԣȤг\xa0ѳȚ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˽Ůħ˩\x8bҿÔôОɁұ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211019.556029:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĨϦЈӌ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'nόǑΒòƒ˖ǸґǯHЪЛdŻʋӂëҺǩљτĵĦʢϷ7ўҴӏ',
                            'message': 'ȀɃ¡ѶĂƔӖƿ˛ΗʂаЇǤ]ӇԧɐέΖȞΈɒΒɸѓĽѮŜӘ',
                            'arguments': [
                                        {
                                                        'name': "ϳκìǗϗҘɪ'ӄ˭ϭ\u038dˣȐʣ˜ϐСӣÅԜ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξ\x88ċ\x9fȝÇĂǏŌШòҪϼͶӚʉǗӂѰÕӂɕ;ЦԃŠîͽŘǄ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '»Ҕԓ\x84ҘсðɾÓ\x9dˊɉиʻYԩ/ʾĉɊҼʩψʢŜӂ.яϞƂ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'sĲϛ˄¨ҌƭӏɧYνǏǲІ\x88ϰͶğʹˉЙά˕ӳ˷ӣοЫ-n',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211020.067405:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȍôŔɁŸǕƌāʾӢǁÚě',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Е¤ªRúϋƢЁĊΆˉʓŤĚӁȋѿӇуӮ\u0380ɟªԥBӫԞċė!',
                                                                        },
                                                    },
                                        {
                                                        'name': ';ĎњŮѬ΄ͱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĶРƊŜȥІçĆНԑӚǠēgIǴөѴ$ҙōǦЦʠѯ҆ɾȲZӀ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅљɺш',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҘcӤČќûȦƠԍƃʶ\u0379әˎђfɞӎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϡԃЕȷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĔƙǸȗʳԠϽҠϖBǋ\x83҆ȕӽҶáԡ˂Ƶ©ЃҨΐӗĤ¢˯Ѯѭ',
                            'message': '\x9eҽ\u0382āԅԜsԁϒɆԅþŜ˜ƚĬhů.БÍũćéӴҼǠɰśĨ',
                            'arguments': [
                                        {
                                                        'name': '§ŵҦäрŋƵʲ˺ǒиɭƖԀ˫ыʿ\\Ϋ\x97\x9cĚ\x87',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϷЄ½jЬƐźƲΫţ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x97ϻHӕԐƧΧōˊɔћp\x8dϯ҂ÖԎʺ;˜ͿѾԖʑJΕŪĖӝk',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӆӂȀȋχуƧϒƓƑǨЛMΖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 235427.35686087725,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϗƖÁѫƔȳKǘǽYЉԜЄÄÝѽň',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˭Ӿ˃\u038böϽԗѯ-ɔӭȷȼs;Т҉ãϕäéʟǯ˷ш\u0382ĖɄɎҏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǫÝҾ˽ʨģԨϛϊȆŷɹŒŜήӊ4ˑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 92193.58679083965,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӫƅĺř\u03a2ōΪʽmφԦîć.ŒŞŒĶȶҷƙ˽ˈ\xadô',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211021.426443:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҹӸƎĭԅ˞ĹĖӝzϢӦȰuáӽϐŏģѝȧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύ\x94ĳĤ˽қϯʖˀҋΆł',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
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

            'name': 'ĲȖѹ',

            'error': {
                'identifier': 'ҮɁđŪƦ',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'Źí',
                            'message': '8',
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
            'name': 'ʮļÑǩӴȨӹԒɔǌƩǂѴͼɈ\x94ԡ¯ÍƜȀĳÂ|%Ԉ\x7fȤ7ɪ',
            'version': [
                -7627821886405544956,
                -4082043514381683097,
                -6657430595881576233,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǶћȤ',

            'version': [
                -1359169461845709952,
                -1837322159410408204,
                -1181877741115274553,
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
            'event_id': 'һƌĞӥvľѤͺȥԝĘΗi½ԄмĄuѽϔŊǶȐνϙ˹ǐʷɀ˾',
            'target_id': 'В҆ӌʜЌ¸ӆǉɥɰÑҠăǣɬÏĻʀлѧĀǮɂφӅɠѴԉSѐ',
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
                    'event_id': "Ϳ^Ǽ'˟ОúÖђҡǔ\x95ДĭÕ¦ʀäɪФȞčōчǪȯʒɽŖ½",
                    'target_id': 'ɹN>ʋДɋҨĈ\x97ɆƎɝ\x85Ќ»ɻҬ˧ӿ(Ǣň΄ȤЩʙЖӉԤĆ',
                },
                {
                    'event_id': 'ХÞĖ\x8cЮȃĻŦλċѡҠӾƬΔҧ˖ϥƳĤϛ7ɻ¬ͱǷ\u03a2MÀː',
                    'target_id': 'ӏӘҴ[ъʑ¡ϷĄΨǧɅӍßӒȱтӍӪðӁй҅қɼÌϺǘƀĭ',
                },
                {
                    'event_id': 'ԨɐϞƼϞ©=ΞŤǭLѷɱҨǊѡЭʉǄ|ЫҗиūХȂҙĊь\x8e',
                    'target_id': 'Ϋ˟ҀƦŽӉȝˍΎɎĄƱӰɘϛѕΊԒϓӺϤԁÑƜŝʹLӯɆЭ',
                },
                {
                    'event_id': 'ˊнˎ8ɩюĨΪӬÑӴǷ"ΡԀʖҼńǶͱƷϭδѭПӼ³ƋϒƑ',
                    'target_id': '£ǏΒūӤɆ˃κӻăȥԔЁ˒ђЎǶӅʥWǬӻŋÀŝѥΈʘщ\x85',
                },
                {
                    'event_id': 'ɡϻɦǔ҅Ϲýǌ\x96]бб\x97QŸ˵ʨ˞@ɈҎɭĪlϞʽɎǯϨе',
                    'target_id': 'ý~ωңņωԕıеͰžƄſȍҝɳ΄ѹĵøƺʟӄ¼ԆωƅрËŗ',
                },
                {
                    'event_id': 'QȎɩȤȷƎɞͻԨÆɈсņŉЈʋæ¹Ƞ(ˤ5Ʒућ¿ȳҥPư',
                    'target_id': 'Ѧҏ\x7fÕЧůρȣѩӘӎlȧц`ИȋƂх˦ʆͰӱƟӑÞХԉҽԁ',
                },
                {
                    'event_id': 'ÈČ¸њ®znƏɤњòǐ*˸ɨÿÝťpιийƠúĚc\u0380#¾ǽ',
                    'target_id': 'ϺUϩӔЈ®\x81ó¢šɘлÀjȖӇKѕҢĨҌΏϫЮ«вƃ×u҇',
                },
                {
                    'event_id': 'śåʲ,φѽɛāʖȆƶÿ»î¹ʛҍɐdpɨǇԙˀԏɿǴǌvʙ',
                    'target_id': 'ƍȱʘүнț˲ȡʭļʔɌûͶȬǲMˑҡďƻȨDҞȷġòԍөȾ',
                },
                {
                    'event_id': 'ǯ\x93ͲƺƘ\x9bвӉΊ\x9dɄǨǅΒΝƻԬƇ®ҹƑ\xadԃϵ²ϔϖ13љ',
                    'target_id': 'ϲϛÇӽdζӹҖŪıǁϸċԬɧǃШϼҤЧ҃ԇ"ӔҊ¨Ň˪ɡξ',
                },
                {
                    'event_id': 'ʙύʡ˘ǉʱљzțԁѮƜĆӥǮǁ@ˉǷ˃ǱǅÍˉҞӝϧŀϊΏ',
                    'target_id': 'іԓ5ǋИʼƕάãʡir˪Ϫťƺč¨}ǜ˚ƑÎǱɭҁ|Ӧɒǈ',
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
                    'event_id': 'Ҳɚ\u0381ΛԩҮˏȷ]`Ҵͻã*ǉҰβѸƷeϘĔSѡȍӺbʘЭб',
                    'target_id': 'ϲάҩӔ\x9aþwӀȼҳˌʂʑӮǶĲͼɘԣнӤ&ȖѾЛӲ\x8cËèʠ',
                },
                {
                    'event_id': 'ǒЁŅȺ΅ʞĸʽ\x92Z¤ǰȫƴ\u03a2ΐɔƹӋèǶTΜώќɴӢɟ¶´',
                    'target_id': 'ӅιˋθƁƑС\x9dΫɪԈŹξҿҊʴɈÕňȻƊȱӷщŕěðʆ\xadƊ',
                },
                {
                    'event_id': 'ҡ§ЋƝĐƎұǾƶ˗õ@ýϛñˌɘОɹ\x89ǋʎ΄Φɚiʉҡđ$',
                    'target_id': 'ѧ¾җžʏʻͽ.ωªżśϽȿǸŅ˖ҦΦƪӨϲӒҨԧɀŃo\x83ν',
                },
                {
                    'event_id': 'ŹɲϘaҺ\x92ҜΝ҃Ӊе¥\x86ˠ¶ÅΈ˨ҥЅϨͱȣƳ\x85ɫȅ˧ȸј',
                    'target_id': '\x9aΏ/SˏɨԄ;˳ӂЄȠΡƺмЃĢßΦǗǕ«ўһØȣɑĬѰ҈',
                },
                {
                    'event_id': 'ˎ\x84Ț\x97ϵǽXϮÈĽĞbǳȬœҸˠ{ĕÒ҉рȻʊӽϳŷŦңϋ',
                    'target_id': '·:¿ȨЮ\x92ѩɂҶêȅĲ=ȩԜԥƭҬȦºʔǛπ|ũӃϠLϔȲ',
                },
                {
                    'event_id': 'ňԈίΛ6ёƷȫ҈ǎɶŢғʁŊɘʸuıίʀJѷ>Ę˂ʭмŖȮ',
                    'target_id': 'лҟʍÈѶɆĎфĀҖɲӛǊ\x9fӢƮ҇Ɂ',
                },
                {
                    'event_id': 'ǒǣjʄy\x95гˀɸtυѽмJɮӃʵˏӀʹƐɱƶƼ˄ŲϦ4ґƂ',
                    'target_id': '\u0378Ѝ\x96ɍʪ`ƫ',
                },
                {
                    'event_id': 'ɹʈ¡Ĝîȍәσï˩сá\x8a˯÷ԏтԖ7ʱόΗɎӓɽȻ\x83Λ˷Ò',
                    'target_id': '°ӗЌƘǯЪûƺɀʷɓʤ˂ҭ¦ͼ\xa0-Ё˱ʭЌ^î[ѩcҳƅ˾',
                },
                {
                    'event_id': '\x8dĸťŸԎ¡ӋȓЖ\xadЉťǕ˴\x86ΦөƟҶŷƍӢˊů§ʲŐŏȓ˸',
                    'target_id': '|ʧƟƎėшȨŪŉЩȣĉQǫиƁʮљƋßԐԍдΣ˪Ёˡİ?Ż',
                },
                {
                    'event_id': 'óɉÃNƊĜЉėdϪˍİЍΪHȨ\x91ѵеѷΘːÂĤҟBt-ԫʂ',
                    'target_id': 'ҿĺ«дѯɠȩɁɀɳƭȆɡ\x8eίϗЯ҉ɟԨҺɡŭΰʿԟ\x8dȩƾ8',
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
            'name': 'Ö\x86ЃƏш¥ПĈäþɀʆΞɑ\xadƾʗ6ſ1ϲ\x80͵ǞiѲİҳʻ˕',
            'version': [
                -2855751171096218079,
                -160846873558164711,
                -1168335055536844621,
            ],
            'about': '»ӠԗԈӈSâӝϵԫȈƷũȞxԜ}ԖűϤӌƥȝѣǢͰ6ƝΈƜ',
            'description': 'ϳƛеȞ\x91х4ӟƫҲ"Ԇğԓԛ§ȿʸɴ¡жλЇϺKĄЁшȩ¹',
            'authors': [
                'ō¶УƬ¾\x9a˵ԝϯ_ϷǃĤϸʙnʖȝʬǀҀԣƅҡЯǒŒɈɠ˅',
                'ȵƤѪ˒сҗΪɊĄӎǇǍÀǜůѮɈӤˢ¹ŝϫҖǆѐчіðʌ˗',
                'ƺҹԮԦԀšΫТюҷεƇȁɧǺʧȔùƮɧʔƥηђοωͱԠѩѓ',
                'ѥѪ\x94ɹЏȋɪĤƼϕďZaŋ-ę˖\u038dӀ҅ȩӛӱΏȝѭћ΅ßˡ',
                '1ҩȕɃԐ\x88 ϒӨ˫Іď\x8fǮϺϻƆƌСУЕӈŤΤӕ',
                'ԐΪʼǎ"пǔǤǑ\'7ёwɂƶǠĮƾo\x94ɒƗәɵǶҀǷДѫʅ',
                'ɫäѯųƌѵǝҒYɠŝźBЋ2ŵњǗĮ\x83ĐщΘǌ¥ɏöδηƒ',
                'ϪЛȠ\x90ѽȬϜɎčˈǊӛġȷʵӏŚəӤ©ɴҙɞԥɴėʢϬѯȊ',
                'ɏƓˈǌӝӅΫʝ\xa0ҨԩˉӰЯǙѹѾҒǪʹїьсǑөϢ½öӴĶ',
                'ǱѨ!ɄŁĈҷʜЏĚʘǴџѥЋʭʲ҇ѡңϬИήuʘʞĻÏŧɈ',
            ],
            'licenses': [
                'ɇΎѵǇқňлɥƙÆÔź3ďΰƿнҬýЉƥԩτʔ˷uУČɹµ',
                'ǂȤЖƥwŲ\x9aӃťİ\x8bΦ]ϏƦʌșXҦ\x8făӰӒόƖΐ˛ϡ',
                'ʶȹƓ¾fʻ)ь\u0379АƻŹҘąlĨƇˈκӃ\x9cϿњΖѢɐϰȡ;҅',
                'ʹɝiҲԞç\x98ҬǘȸϬӚЌȢѪş¶˜ϴѦӺPхɾ®ľȔųĦͱ',
                'ÇȦЬЬϯɺȅ~ʛIό´ққ`ŤΖHǾ¨Ćĸ҅píԄΜѽǞg',
                'yϧϺcȝŒ҄āȒѕuӍɦƮӵ\x81ɆąȣҼΘǤʣ˘²ǀΐĞӮę',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ҳǱǹ',

            'version': [
                -1811953688408688263,
                -985309331049783127,
                -123449117477986726,
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
                    'name': '˒xʶˑϭɦΰ\x98íԩӽɶʮɖÜϓ]ŲeαͰǃǃ˛Ǖ\x9cƮҺӒϝ',
                    'version': [
                            -2150623542478265515,
                            -6316170232602500624,
                            -4606032894174261019,
                        ],
                    'about': "ɆҤӺɉƚȋį'ԭ:ºΦϸĸŲ҆˵ε҂ԌǿǼϪЃѹªîщӋҬ",
                    'description': 'ʜŚŪђщPĿĀ˒÷Ԩƥȗ[΅ӹȱħǳǅɆɩ˫ķԢ˫Ƕȵҥӵ',
                    'authors': [
                            'ćɺѾð*\x93ѷƄ-ȜҟǰȃϦɒȳγɹ(ѳ\x94˒ɭǟʷ®ɣǹʈǮ',
                            'ȾɢϋгӨьPʽΣāUVʌÅžlϿԪƽŪ\u038dȁʪıўƒ\x8dʳ9ɽ',
                            'ҺǊ®F\u038d˶ҎӗʤӀɸРȂ»ҌÛŭǠвǞѦ˘ŁΧŁԌÐ·ԍƋ',
                            '5Ș×ΫʱÆ\x9d˃!ѦǚѝƐƪōϠƞǺɦӄƅƁԂҰƜɃԡϠťѾ',
                            'ОžҀΜÎɫ\u0383ƵǙTЖ0ãЍѦġ˷ǴĀӟıÄϒȃίòҞτˏҾ',
                            '˫ΙϋȒϨĨѶίԆʸƫΥΐԙƐжȢǛ¦˼ҔѢЯʚˇԔԠôҲɻ',
                            'ӧɨгδ2śƵơѤѠ˧ѩƔ³æ˖ЯōԜӂeӡɺʙҶѸҰɓϔŇ',
                            'ҙȠЩԮΏbӟĽĹɀǈʝsYǰņʟ÷ѥϚľǌҶ\u0379ɌʔĽПñˡ',
                            'ȃʯƻλѶоӮѴҡ\x93ċÅҥʞȃǌȹԒ]Ωÿ\u0381ˢђɔXԊԧҳƞ',
                            'ϫӇɩʲŀŚ}ǧЏѡҴȠѢþïӊϷԕƢŌǙάњȺʴĈŤϱϦΟ',
                        ],
                    'licenses': [
                            'Ӻω^въtťFԤȷҿϹ\x82ȼӭ`ԝ˶ӓȴȢóʸϮUˀŜ˒ͽ΅',
                            '˺ЈȆƀƀʚ҂ǞďƋWĮҖŁЯʹŶйȀљάɇͺɐЛƘϋα҃Ŏ',
                            'УҔҁњŀĢű\x81½ʾǻѷįІ\x96Їђ\x7fӂ҅Ҡɣ¢²ӹƨlΌáˤ',
                            'ҌŦӒнҥ˃ɐģзҿԡГϫ˰ΚяǇȈśϢΥǱƾ;ŊȤӪɣ«ǔ',
                            'ƼҴѽɗ҉ϼԋѷşõҪΓÃǼ\x86ȜÁӥ˞Ӏ#ҊEʑо',
                            'ʹЎъ͵ґ\x84ʌƴΚЇҿƎΑþɢȻʾАʎøʑȒPϑЧ~E,ȰѢ',
                            'ċşЃ\xa0ʄýӗĊ=ǛЮȡ҂ʸʞ˔ƦˡҥИѪ\x9cʡǺŭΎĳˎӋ',
                            'ʴȇíчɴӷç˲\x82ĬФ!ΚƝȝã¥ͶѫΖ(ȗԪҾǋǄ\x8cӍϭſ',
                        ],
                },
                {
                    'name': '˚ʢĠĥȜǧ϶ʱYʰΔϷ˟κˎ¬JìȴθӞĢŜØωÃа\x89\x91ϵ',
                    'version': [
                            -7920024879383666326,
                            -4626485032503875992,
                            -5908958475689363107,
                        ],
                    'about': 'ƤѓĥŖĖʗҿ\x86Ō˨ӵʧȖƴøƦǮǦӘʄȭʓȄшУɡĴÀщǂ',
                    'description': 'ǏɃϳ\x8dƓĊ»ɞĭ<ÍҔҳçŚʵѣxŊéԨӻʙʄƄkǴαrҾ',
                    'authors': [
                            'μӴю÷ӭѷѮԐԀɬѵʑ˴ѰǿԏĝʉǓȲYҩο2ĝЛ˝ɖǢT',
                            '˼ӏОԝԒҟƾ˱πԦ˄Ыȟŕťˆ3аƝ~ӢϞԤĔʣɒ¶ӴҲԡ',
                            'ƣńȖСŷśςяЯ\x83ÇǮҐҦıƴϛЖĽԃŗӇІϡʋϵĭ\x94âӸ',
                            'Əˍ\u0383҂ǝÖÿєӲг\x97aʛƸəύҭ\x90ǗϽҽʗɁþπˈӚEԕ˹',
                            'ӪɆAƅӱХĔCǽǱȕϪҒ´ɛҒǎЫžʒ\x8cҋļϴřΔћ¤њ˕',
                            'аʊõ%īў\x9fͼВϩ2ŚϽˊȰ҅ŃǢŗμҗά×ΆТԉҫMýԝ',
                            'şĂŏӃŲ΄тÉєƛ˸ӹтӡ\x9dɆӥWӦԎѰrǟ˗ŒԣѦĚαԋ',
                            'ΑԎƸѱʹĔ΅ͺŢÎˋή°·ѬĪȍеˎĄЎɏΡΐʝÛѱǲ]Ò',
                            '\x8eƿϓӮӖΎӇԜ«Ϊ\x9cƌƕūÏǝƂԈ¯e\x8a˥ɺРļʆЈɶЖӉ',
                            '!ʪƬƤ҈Õʓαқq\x82ãӏ¹Ǫä҆ōҁΆGƃΟɅćγĩӢ\u0378ҵ',
                        ],
                    'licenses': [
                            '¶ҩģϼҺϺ_ĎȴΟЁԅ&ϋƦȳǶΔУԮόǲԨʢӤ|ˇɬӷԌ',
                            'ӓʁɑ\x9eȣŜэƂ·˲ǔжfĹ^ɈїУ÷ɧ;ϒơЋʨӋҴȱԤ҈',
                        ],
                },
                {
                    'name': 'ǃ-aƼӢˋĞѮϟċƩҸќǄ^ǊɜΜѵԙΗвǏіȌӗȊÀ π',
                    'version': [
                            -6238031427744898636,
                            -5299999932744490810,
                            -5447990618052074497,
                        ],
                    'about': 'ДͺΗÈɴͱѶʇƦʠʑͰĭϦɏГQŗɼ®ЛʣȈS\u0383¯ϔ¥Βʍ',
                    'description': 'ȟ˞ǽˇƙ¾ʊҒ"°¿ҡæ5ԈʵHŒƌȔÿγѯŅëԬӨ8\x87ͱ',
                    'authors': [
                            'ˏӹaχMϋˉȰЮѡ±ãʛӝÚϻȼłҥȸ\x99˻ˆəԮǞʷà6ԑ',
                            'ȗě˙ΏƓҢȑǻοɠҧ VЇїȀ˚ГʞҘŎњ˘¶Íȓ\u0381Æϐȕ',
                            'ȟFϳöҴǏͿ·ɋ²I˗ЖѼςN8зͰàȿЀ˫U±Ͽ\u0379Ҵ\x83Ͻ',
                            'ѻЉɰĄӓҁɛ\x85ǻˑˣȗvҺΊʆʲҺϼƽГԁŪť(ȠҭʖƝӸ',
                            'УðŃǹӑƧĵyшƺ\u0378ȵѵӪʜωҤĭÞ¢ҪҞɫΨ\x88ԝ\x95ʢʹ\x86',
                            'ºˣϽˠҐū3ӆ$ĴʺηɼԚŴȄSӐÓɩz^Ƙ\u038dNȫ˃Ęҕ\x98',
                            'ÕφoδɦѩëΉɔ/ћŎΒʇͱĠѝůԥѐО·бĞ\x98ŪAǙ΅ƻ',
                            'ɉɣзƤ˩ѐʵѼ0ǅΖΟɲ\x84ΥɲĔӗҲҒͿǜѵɇ˪Зϰζдŷ',
                            'ɹùӘľаѴ҆ДÍϑĘvyċĲӣɮΤ\u0382ЍƨŴÛßȈƃ4ҷƯ˟',
                            'ˤŀÐ\u0383϶ɾó˘ӳǀȘѥμӭMԬƯŶ\x80ӘǕǔ˧ԟXΐВ˥˚ļ',
                        ],
                    'licenses': [
                            'ŏȣ\u0378öwm¬ǏӤŅϞēˏΒ³\x94ƼŖƠŃ˔ŴѽŅΆxļŷ˳Ҡ',
                            'ϘƴσӨĉ³ѥŊҘƱ˓:Ϳɧ',
                            'ƭӏƀɬϫäŋǕɲҤŋƛ҉ϷǇ]ȕKҵϹÞДФ˯Α¯эĿѡđ',
                            'ōĸmѤǧʣɶ˔ʟĵʖԖ\x91ǥǄСΐˠ˴Ԋ˛ȐMʸѽĂɼΗ½ġ',
                            'ŕ˓Ћмʁǚ¤ŦĒǼºҾˑΪƿƮԬѧǥÂ˳ŐЇ˲ƁӥͽϥǋϠ',
                            'ĭ~ŚӁҊϔĉԔǨǸǫҵǑʬ\u03a2ȏưż2ǰĸϔ˟ŃΙ$ӞȘƪх',
                            'Ž΄$ʅҫÀгʤЋӪǤҮԔąΨªɣҺΠȊͺхѫ¹ɺԮżǯĊȮ',
                            '\x85ȧә4ƈƙėɽǷӟǢ˼ȷϏΩӂɺéǕûΩʄǎͼρаʪ_Φӧ',
                        ],
                },
                {
                    'name': 'Ȥ)Ԗ÷\x87ԛȬ˒ÏʵȺVȜ\x96ÙҋӜɉĬǪΨˢȖŪϣԥƥċНǀ',
                    'version': [
                            -1234911806176476012,
                            -7765483383051971838,
                            -966939640591903055,
                        ],
                    'about': 'ҨȐϓԇɢŰӄќεÜŤʡvŨÆěԁǏ\xadȝΑȎбɡԠѺΌƒŕѯ',
                    'description': 'ħϒ˞ӧÊǊϧԀÎƿѠчяԝΊԋǘŃӬɕԕǒѽʘЇоǉ$Ĝʊ',
                    'authors': [
                            'ԈŃȂʥkȢ˴nѼŴϭϐΘԟƎ5ʓvӅĂȓŉώÊԡҋʙΧƯ¯',
                            'ĂѤʂĽ҄ʼнɜɻDǽ·ɿƛǍԬɒǝƫ҂ÉŐ˒ѩȃΏ˅ǯ¼Ѽ',
                            'îˇȰ˓ƧϜϥ-9ǯςΘŢϑԘ¦ǫȿ϶Ń',
                            'ЎǆŵǿɷѩӸĭɒҥřšÈ\u0382ƜΪʭɝКĆĲǻǫşӁâ_&ƎŸ',
                            'ԢȷйÄԩԚΊρьēӱŚƞʓȰǆƐ\x87ħʵƮ˰·Ş',
                            'βǨĩͳH˦ǽԃЁȿέϴɲҫǮȺғˣçɃüôεδźʽ˞Ĭѱ°',
                            'Λǳe\x95ЎǅĽʈÿΆӴʮίЯÄʉůsjхЀʁ\u038dѮÝҏǝĥ˦˘',
                            'ԇѻŬŘĐʬȞçǣӞDУȊΫѪɰԄͻǙ˖ʰќ΅ÞƄѣpӾѺҜ',
                            'ƹ]УƶΫqʗ˪ҌƃʔQӇƾÃȼȱӑƭȇĎЕeΘ˓ŌƎȶɠԓ',
                            'ԁğӦȻЬѾςӕœɈұͲʁdЮˠɮÓɒȚѸԒЬ\x8bĪxϷ<ȊΥ',
                        ],
                    'licenses': [
                            'BқƤĔŻԪԒǌ8ÈĠЙ²ϋ\x96',
                            'ʺÔʦ¢ĒƉǋƹˑĭзϩʜ2ɧàҺŅƄ"ȡϾˀG#³ğǶВȖ',
                            'ÿ҃±ĨʑҲ\xa0ì¡ȺǮEΦϒЬȺѺʐϟƉyΦȡƲӈѫɼ\x93ӭь',
                            'ѤˬȿоϚɐφ\x99ēϥє҃Ȍe²ɯѯͱʤŝȯЫуϖ\x98Ⱦј˯\x81~',
                        ],
                },
                {
                    'name': 'Ƚ\u0380ĬЖϬԔςɞȗʿԩӵÁɦʜѭчǇŉɻғɢНżӷϦИΔEΝ',
                    'version': [
                            -8912161394298538959,
                            -8099299792224999839,
                            -6073640841726898722,
                        ],
                    'about': 'ϩŔĄǥ\x80ȐƷĈȘҼɆɍËæŖļҝñЁԃͺ',
                    'description': 'ƀΟ>ѫ&ԔΨɜѡˮ˼ԨθіŞԦˆΧƚӤśҠҭӛл\x87Ʀԣӂɼ',
                    'authors': [
                            '˂ōыǣĠʾӇ>ŭҰ҄ĖăМ®˙Ķ÷2ЁĸĠσͼщYĻԖδı',
                            '\x85ӣĀŠ\x97ғν϶ǚ-\x92ȃŋʉРʳ\x8aЄo͵\x93Іғ\x9cɓÙɣҧ}ɟ',
                            'GĸˌʇɷȹѰЄԓӒӥɹyǵґȂʳҿŵŏfŀӮǨÎΝ3ΉҥΠ',
                            '˻\x8aȋЌΙф&)˜ӇĢATЁΊҼȶΝіҷɮрƜDȗƣѯСԮγ',
                            'Ŷ[˫ϒΌυķόǘϫΝ\x95pԇ¦ԂʫūЄÇǶ°ʌõÎÈɳɞö¯',
                            '˴¾ŧȰ÷λğƳʨˠ\x9bӎʕͻʫԚ³ǈȾŽƷïͰǼǅŕԢ҆ńϢ',
                            'ɂ]ȹ\x82ѷ\x81UʛɌфǷԮƠϔєϜӭÙɰIьƓƷ˂¡ĵ¯\x84ʸϮ',
                        ],
                    'licenses': [
                            'ʬǊïњӆėȳΓϛЎ°\x8cφƅʈ˜ѵЍɓDŨ\x9eăɓǘͿĲËηӇ',
                        ],
                },
                {
                    'name': "˄ȱü^ĵģ·ϩκˏā\x9cӔӑȟϗǹɩӸϹ'ʤʦη¨ǅͷҮ҈i",
                    'version': [
                            -4231036261048267946,
                            -6304900166644506703,
                            -5417518292769925568,
                        ],
                    'about': 'ÈƭҏɗӇ#\x8eЁ҈ΊɇǍŀμщĂȾаĜɠúȜԗj.ɲˉ1\u0380ǅ',
                    'description': 'ͳÇ¯ϔ]Ʒиĝͱʞ\x8fƾҾ¿ӋϜΈɹ˨ȇѽҌәˏɬҏҕҽВ\x8d',
                    'authors': [
                            'ā\x84ʕĞǍƾԚЍ¿ȻЩȰ¿ǵϮҗ\u0382уίʝϋCQ˗Ϩʥһ|Қƈ',
                            '2ӟԝ_Ǭѽ¬ҡѡβǾ4ʈЬ\x90Ƌ˘\x96ӕɶɨȦģƦԖЅωª,Û',
                            'ШӡƈťȄǤͿQыæӿ¶Ñϐ',
                            'õͻƭˣʋσ\xa0«ρʊǌ¾ϵ%&ǝĎФґ\x8cƘǛʚђö\x7fĪóʁǄ',
                            'ȓѐɻѪɡҁ\x88ǩùʲűȞѰԩ˧тáKɂ˝3˺Ǉƪ¾КԙŊɑϟ',
                            'ПţɍİɊɥIԌτλҭȃǄШ˩ӍɊȵʃЪēҢȰοӋǭ\x94ªЦҡ',
                            'ϻP˱ήҎϡѕʽ;όџǛчùҊŎǢ%ȱ©ҫĂψèʱșƏӬĝϧ',
                            'ўƿʈʲӼlчÌʽ\u03a2ĭΜøŒċɑЇħԗRĈʱùƤΏ˴ɟѼ\x92Μ',
                            'Ѿԧʚdǃɚң˵ȞӯБнȿͺ\x8cҝ΄ОĊţmİʤδÌуѯ¸цǮ',
                            'Ρ»ǼňЯӹ{Ʉɹ',
                        ],
                    'licenses': [
                            'ĤЁІőʝΌьԀΠöŊȗȫƨӨДҮˢένԐŀȳҝΚӜƃ˰ʺɛ',
                            'ˣ϶ːКÙƊГƦƱț\x93ЙҮʀΞȫÑīɎ°àŃźэɧȂԎ˚',
                        ],
                },
                {
                    'name': '\u0380ėĤƬĠԆкˆ\x93ȼΰĩ\x98ϻѶLɟ\u038bßǮŶˎĠȣĻІʻ-ÑҺ',
                    'version': [
                            -3920542431601783972,
                            -3269334363691087092,
                            -7937562447791764028,
                        ],
                    'about': 'ŒԆϋʸÉϺɧ\x92$ü˱ƚЫќŽеĪĈÜƗάԔƟʧǛ˫ԠƔӘǼ',
                    'description': 'Ķϯ1ˣ˺Ί\xa0ǏвɛЗǵБˤŨˍŚг\x8bvχӇ˨ԧȴ\x9b\x9cƟ˝/',
                    'authors': [
                            '·ΔťȁÓʜˁÃ˄ěyјoŖӁʐϧȣBɪǩ×\x87ŨȧӯθǴ®ȿ',
                            'ǋəɝȸłϱˈӷғѫíΨÐΗӹθт²Дɏ',
                            '\x91ηBtį¤ǬȌ·ǛˠυӑЅǯѵâeӠчoоͲ/Ư!4ҖʍĮ',
                            '«+ϰ΅ХΊˠÉČϥͱ˷ƬђXѬ=ŵ',
                            'Ԙ®4ʚҦԣŁΔͰʲ\x92Ȧǟ¿˦ʐǰɾŘ\\¥ĝҺǂŋχʓÁҫȊ',
                            'ƈηhŘ\x83ГĊ.ѦԗżȳȀŹɟүċӔѣΦӬвӆƞΥũН-ˌȯ',
                            'Ԅˑ˷Ԋƀ\x82Ĭ>ĸĨƱÙѨΝʚĪОͰƆ\x8bǼϪӄƙԦĆҏï\x9cȞ',
                            'ȂҼʡƲÆҐҿƵ\x93SӆԈԁĹ˨ҺQӿǌ¹ҳ\x8bȱʤԁ`Ӑ,\x95œ',
                            'ҼԊơϋɅǕκĢӤŔԌƣʬǪĉʴ4әϙʩ\x84ԀǢΩӡŭƟŜφδ',
                            'ěȭίʸšƢŒԊğƩ¬ʫŐśĀӗο\u0381Ѡ˞ϥϹǵ]F\x97ĨΈќˠ',
                        ],
                    'licenses': [
                            'ÑLԦǭOŘ\x8a˲Ƙϰųņϻӽ',
                            'ƭʥϼнżѧśľƇͲ͵ɸҺǩǈњƐ2çқҶ˴ǜ\x85ķɤǕӜшӸ',
                            'ɸԐωʯǡϼƸ\x9dЋ͵BĄɚӿͰӽΝʪӭƺʎyʢȸťШӓo\u0381ʃ',
                            'ɰӣŢʶйоŧΝӪɒԁƐSťҭкғĎʭȍӱĒȧǈԈɠѳgϴT',
                            'ӂ³ǧŉˈǷȈOŎǁԝŭÒÏѣҡɰѹǇ|ԣďȓOQˌϛо)Ĕ',
                            'Ŝŀѭ}ũѫ\x89ϡâѝǨǮ\u038dĂ҅ӸϦ7ҌˋÑЏ˂О˧ʤĝʌŷɠ',
                            'Ѥ¦ĥ',
                            ' ʪjƈЃͰȄɕяМʿ҃bşĪҜѼĂƖʊǰԏдzӎ¨ȩΧ҇с',
                        ],
                },
                {
                    'name': '˵ˀƽɷňYʓƕ˵ҧÀ\xadƳʓϓƻԓҖǈȗ_љEʕҫ˶ƃɲţh',
                    'version': [
                            -2921338579073685736,
                            -3364100202544167448,
                            -2002073443998808930,
                        ],
                    'about': "ҁ!ȐʹʙʦԃǻÀźԫ)ÍәDŎӶҼͰʹԟŹ'ѲЫƏсѷәʴ",
                    'description': 'љƢğɃϩǀɿˢԙłͿǘ͵ģʳΨϡʟƿʛӕϑå\x82űŊϘƹǕ+',
                    'authors': [
                            '\x96×ԍҪаӖ;\x8cԓӲŧԅȴgˠƉƿ¯˞óӬűRʔäЃά\x86ȒԜ',
                            'λɊͷ=ϮɈԉĄϏҜ8ƇѾǴĊïĂʉӫč˓èΨž˛ŏõȫΖŶ',
                            'њѫԞҫɁ˙ёΠýСǔˑϧӬȳԌƺ˘ºɀiҙ\x9e\x82ӃV\x91ǆ҉ǅ',
                            'ϬԔĐʝҒѰѦďƨȿȖϡɅΆԞʤʈ·ӚʳћɏНȬʠJIϜķƻ',
                            'дӥґƎӡÙ;ȄϣzîÛ]bą\x95Ϊ˦HBЖҲŕ<řĠŉǪӅĲ',
                            'ҏɃɖˉΛЏȕ˱É~·ɗȶGʥƩҢϕÐǞĝΤӍѧϴѼԛɗГϘ',
                            'QҠγĭĿ\\Ȋѕɪ]ˎӫҾїyÊð¹ĂѻϦ\x91ĲήƭˌêЦȻó',
                            'ϝЄ',
                            'ǪéКӃӞӑҋӣЪԛʘƺ¶σў"ƵʀąΨӷɕȝÀɄДŕkˠd',
                        ],
                    'licenses': [
                            'Ʈ&іѺȴӳԀ˓ƶӾѿͽӸӡήѩϜϤϽşțҒ\x93ѺuϼɈ\x9cɳ͵',
                            'ȶßΆϐ˔ʈĤɞʢй\x91ɣȞʬчƣˉȊ\\ȒʷϢ0ÑǝȲԩϱ}\x83',
                            'm˩EϜɜіżĄŚ\x94ʡǡʜҚǹϜȣ\x83˛ΓЎ\xadӌˁ;ԋӳˬȰb',
                        ],
                },
                {
                    'name': 'ΧɎyJ˴ʊͷƥ',
                    'version': [
                            -1447698403651329375,
                            -2704706971116315546,
                            -7540448953482825840,
                        ],
                    'about': 'ҏĶΫΒśȑҋĊɫƎȉàʊǠǕј˅˲ľjҷ¹ȄŬ;Ƨѡ\x9cʭѻ',
                    'description': 'æDŃ\x83ɘҘҾºѷC~қ\x88ǋŕʀԟpѯԔχȵƩBӗЏӔұıÁ',
                    'authors': [
                            'ɎπƉ\x9bʒӍöĉϽΌԗ\x9eȄĵɌјɷ«ѢE´АΎψUƯˢȡӞ\x83',
                            '\x96ЍˌЄÜiӺ\x9dɤԡyґԒŶȂљȁqŜĐӝЏŐѭЋȔƠӟƁɃ',
                            '_\x9dŘԗèɿΟˢ¸ÕҒŃȼǗĆϊĎФНϏϲҵԔɧȱҐӤ÷˫Ȋ',
                            'ѧ2ФŒƻŕԑҵďгͶҢ·ÙɹηĂ£ӢʙŨ"hŻƗʱɄϬǏѡ',
                            'ϔJȿɎǓпѱ;ҶΊɓŁó˲)Γǡ3уԛχʦҍʐʂľϕʅǴԂ',
                            'ϝʩӖɤǕϗľІ',
                            'ԘӇÁÈȕȰмԂѲ˓ŒǎǠԀʿľЃĮϬөˋƳҽɒӸǹå×żҔ',
                            'ԜŔҝ¾ҪǹƭN\x86Ǒ\x83ϿˑɥǏįфНBӭԁƨӾĤûǗԕ;öŮ',
                            'ŦџĲǓбϲƲŨͻ_ԛʚ°\x9dȝˈɣиƑғʩɻϩώӓɄзǋ¼˴',
                            'țȚñ҇\x9aôľОψѻĜ϶ŻԠԓųˣԎ\x7fҭӎ\x80ϥȫԅȕэțÑѱ',
                        ],
                    'licenses': [
                            'Ӆõ˱ɂɥƸϋԀ[ęƒȶÂӫ΅ѥъĝҀґɪʔǕ҄ϜŐ҆ǚ"ÿ',
                            'ȥǺɸGŝԆҷƼѤƼі˒ɃУԎpчӡ¸ɽȋѩɞʢŮĎкϐɤĽ',
                            'ԦǾϽęuʑβЇǰƷ¦ʌʻʰȨΪ\x84Ҝɘ˫!ǦƺƜЫqΩ×įō',
                            'ǷȳÉ·ƅŊčƏлΛƳŨφԏƱӃΩĩˏÜʙýżӴӹɨŊђɤŗ',
                            "ŵĖgȝωǩ'˷ц˂ƩĂҡƐύǊʺӈȞѬЦНк\x90ģ˂ԒҼѤĤ",
                            'ӔǈɷɜȻƜҞ³ƊȢǌϯӾȏŕΌĠɏ˂®φ\\ϧУϷǭýҀԝѪ',
                            "Ǎ҉ʱĴӏF'6ӮǁЦɠϛЃƬGƝ\xadҤüŵɟ!ψπôҔʇ¶Ĵ",
                        ],
                },
                {
                    'name': 'ÏϏGҦxƊѴ',
                    'version': [
                            -5253110925840340657,
                            -5765632341316152404,
                            -2473363680144654331,
                        ],
                    'about': 'ŮБɰɞÃˆĈѕѐO¤ΐƊǙˉ\x91Ѡ˰ϴҠӃOĽҘ˝çƛƷģԖ',
                    'description': 'ӳΫĸƥǨ\x88ʐ˭ҢǙԒțҠyǂ;˚ϛѫǠÇȸȘĪ˂ϬҨГˮǹ',
                    'authors': [
                            'ȅӈˤҁͺжΒʸԃĖĎ\x9bJ\u0382ɹЮțѨʟ]ȟȯєǮΏˮѥОįĵ',
                            '×ūţ\xadǔў×ǓĐðň]ǮάȃЈԊɈŇПϔȊõӥŶї\u038b',
                            'ϕĒԖˀƯŰĴΩUЧ˯¦ĹqɠåɁˁɌ\x8b~ȩ\u038b~èDτhɜǎ',
                            'ԧұӡͳĤɲ\x86űQǡȓҨӇƱŲПΐŹǒϾĐ»áhѱɚʠҡƑ=',
                            'ЅªļѩįιƈŧŔùҙ˳ȇŁωǚɍϲҊǧԒʌǹϋԜɱ˼=ϰӽ',
                            '\x94ͺ˖;ћӢǓȯλνïǈ\x92ɈǫʂȊøċɴȕøјΰ',
                            'ǋøXΑ˖хÀʍч*ӮмԎàÔƴƋΑω˽ҞpɇŃȕŴÂa\x93˾',
                            '˷ɉű`ҾëƆѸɋӳє˫ҕ«\x83ӊØ1ԋэ\u038dǐŴΡąϲü˜ѫ8',
                            'ɍϣäҭʫѺý%ò˝ä\u038bϽЅЅǨʶȋj\x87Ҧ\x7fώqԊӿϙƄͿȧ',
                            'Εʑ\u0380¾ŚʭХ\x95¤ʱMɀѾǐǱɼșӑύđɟ҇ԕăƆ=Ňф±Â',
                        ],
                    'licenses': [
                            'ϩˬĬɗŢЖIѓ˕gƞɘΐȍƾԁϭŴҵ˔ć҆ȭʸÙķԁŏϢҖ',
                            '·ϪȝϷԖԣĖԨФxɒşԪǭРȬɠԛØ9ɡŌŽϥϷοè7΅ư',
                            'ŕɞʯŞ˂ŭʮϤӯ ӡǿįѱƅ˩¾ԧˋŸȧɔ¬ɼУԙǔ҆wI',
                            'hkǁѼĤ1ǈјƧԦӗƉԗνůӹʷõʾ7ŮÇ҈ғQѓΝўκʮ',
                            'Ӵˎņ«ʇŎβLΨ¿ˌ,ǣʔγ¢Ɯɧɰд7ёŞȑ˵ȝČġ1Ȩ',
                            'еϺüęƂбş\u038b9ƶΦƬЍǔωɸӟˡ˓\x945AǊеÛìşϩԮΓ',
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
                    'name': 'ȏȐб',
                    'version': [
                            -364055668082820678,
                            -1034317956662088893,
                            -165122505419239132,
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
