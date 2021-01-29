# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-29T00:26:22.801718

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
            'name': 'hǁӉʨȦǷҡёŘәŒˈaωOÃȡ˽Ŧҹϭ\x84ϢхіÆз¥Ԅҋ',
            'minimum_version': [
                -5251661190455937626,
                -3815400327556622533,
                -7627161847107930735,
            ],
            'below_version': [
                -6571034124724362354,
                -3850534874209459207,
                -3154070745556965098,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ѭǭĉ',

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
            '$': 'ЕʨԜÀΒʆѿŎ\x85ȓҋǷɕîόϥɸҶl\u0383ҴӦȣƠǩé\u0381ԒΊщ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 5409197908256484193,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 963867.1355766477,
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
            '$': '20210129:002622.721410:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'VԬ#ҟғé˵Ǵ˗ԪĤӠϛƅʙwô\x87ΑxǤĳňvŒѽŮ\u0382Ɔí',
                'ɱƈΘƂˁӹѤ\x8cӨт+ɼƍɄԑͰъŚ1˵Ё;¢ʶѐÎǓӥɋĨ',
                'ҢʘҒƱǋ\x9cǳӱʇɛǊӓǒLāѪAɛŭԝҬȴЌM¬˩ҕēӵО',
                'ʬđζƐΥΥȧϸѨƲéԎɹԝÑДДӐŨǶƢѶȗș˳σɛǷԞ¾',
                'ԘѓūȾʽġԃ²ƱɳϤŷϗʪЮɡп˂ͳк¯¶КƹԗͶƻүʘƼ',
                'ÜǭΙ·ϊǖИÙjĈȎʭΞ÷ӿŠ\x8aƩĎ˴ǖɻɰŶʘʡţЉώҼ',
                'ƭu{ǊǪҠӝǰʺ˛ʕΫԇģҥG¨ŊǇȵԃӏ\x85ĄЬɶƦϏљƥ',
                'ƹ\\ѲυŹΐˠёȷMʄğǬĂӼ\x8bʳÀІο#ǅԭ\x87ȯgʾїÄй',
                'ϰЕŃɣϘ\x9cʄ\u0380jаĞǇӭӯԇ@ȇQƹҜйƠļϺ4чȥȟŜѱ',
                'оĂƸƛϾİɬƼʜȩǓӋǫ]ΧʤxѦɱǼƤɮεơǯʜǡԬÙԎ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                4264848724596568832,
                -6317823282200281679,
                3265229179591519192,
                -4863298168263155415,
                7262911305872823227,
                1518190593154143276,
                -2020217544729858504,
                8632034096142716145,
                4634862091959826312,
                411182677534051987,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                68903.6906950532,
                -34638.048568183985,
                301986.0492394595,
                534503.1701296783,
                484562.4257304998,
                807086.0792387401,
                21347.487649987437,
                298116.0503228886,
                237471.480267038,
                992254.0782077538,
            ],
        },
    ),

    (
        'bool_list',
        {
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
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210129:002622.722233:+0000',
                '20210129:002622.722242:+0000',
                '20210129:002622.722247:+0000',
                '20210129:002622.722252:+0000',
                '20210129:002622.722256:+0000',
                '20210129:002622.722261:+0000',
                '20210129:002622.722265:+0000',
                '20210129:002622.722270:+0000',
                '20210129:002622.722274:+0000',
                '20210129:002622.722278:+0000',
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
            'name': 'ďăȧțϹ',
            'value': {
                '^': 'float',
                '$': 127536.21582234529,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ţ',

            'value': {
                '^': 'datetime',
                '$': '20210129:002622.721279:+0000',
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
            'catalog': 'ϝŤŵϏˢЈǙԫҖΡǊѝђñɔԜʊ',
            'message': '¥ʚǛĘϧʎέĺƢƐɶΗӻгҕÐΕɂżŕƟ[ʭ\u0378҃ʸПѐϖń',
            'arguments': [
                {
                    'name': 'Ԝ˘рѷǔρӨάȧќģѴĪSÀ¹ϼɍ΄ZϬrζ¬ş?ϼ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210129:002622.719049:+0000',
                                        '20210129:002622.719060:+0000',
                                        '20210129:002622.719065:+0000',
                                        '20210129:002622.719070:+0000',
                                        '20210129:002622.719075:+0000',
                                        '20210129:002622.719079:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ѹИΔҟ˶Ӯʇσ¶ԬÛ(ēŊԋƑŤ',
                    'value': {
                            '^': 'int',
                            '$': 4612836649859384516,
                        },
                },
                {
                    'name': '5ŢʤƟЀөћҐķԮɝd`ƶёɶȞȋƭҍӓɞŪЖ΄ӂӏʉʞɇ',
                    'value': {
                            '^': 'int',
                            '$': -6878902731979784363,
                        },
                },
                {
                    'name': 'şΗŮÏ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210129:002622.719535:+0000',
                                        '20210129:002622.719544:+0000',
                                        '20210129:002622.719549:+0000',
                                        '20210129:002622.719553:+0000',
                                        '20210129:002622.719558:+0000',
                                        '20210129:002622.719562:+0000',
                                        '20210129:002622.719566:+0000',
                                        '20210129:002622.719571:+0000',
                                        '20210129:002622.719575:+0000',
                                        '20210129:002622.719579:+0000',
                                    ],
                        },
                },
                {
                    'name': '«\x85ȭ\xa0ˬώҼӊQČ\x99ȋɂžȌȋϕŪɓŪȈҽʸɐԇцӱǫͲΟ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'K£ǎɲМʋӠ~ĘʀÚǸϗZ5',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ΪÉčóϦȆӏ\x87Ћˉʙ˳ĩӯϘύϽŵӐƊΟьγԉΕȜʦˮѠˣ',
                                        'ЏÇȡӶƐԒɿύ(JóëʱϸǝӟŹ`ҫԏΧȥCӛǘԂϽrшĚ',
                                        'ďƻЬȀĲʖϙжɘϚ_ɌŗĝҨϠθΌɅφ˜zϕԤҘӒƌ¥ĥэ',
                                        'ºˏ¢҄ЗĜßlĊĔԕӢρC:eƃԙЧіŠɎӻáȨІКxЎȴ',
                                        'ǐЏ\x8eȡԈӠʯ˰цҠнôыүƲȄô#βЏѭNͷƩ+ǊсŇϽӒ',
                                        'ПȫһǺ˫ΈǡǷɭΝIҁȦѴөԤǚȴСΫÞǆάŴɨëӞīƢξ',
                                        'ȲΔϻŠčґӐўіʪƌɳǦɦĴƈņČѧтĹƱ)ˎЎɀΏԄС\u0383',
                                        'ӱ²ƒ\u0383ΧΖɟÖЙIÿːǆ¶ԭψ˦ŽʪɵвΩñÝқπŎZϯλ',
                                        'ѩӫǔôϏĩʎ$ѼǳϦˣmʮӓɈöϔӺԐƫûǿŝΟȫĕɤЭѿ',
                                        'nҵЎώŎвԦȟȌƎȔ\x85Įč\x8fϪмǽĿɧƔ\x9e\x9eȓŴʾŎɮĠǒ',
                                    ],
                        },
                },
                {
                    'name': 'ϾðǀŌƬuԁİˑɿ\u0380\u0380Ћ˴Љ˲×ʙӔ³ξУɸҔ˷ǳ',
                    'value': {
                            '^': 'float',
                            '$': -91381.15771737862,
                        },
                },
                {
                    'name': '˚¶ĴñåƏҩҢҹ˅ɩҁϪ5ŹĎӺҧÊβû\u0382ŗχХǠŤοµé',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -4477045917215587465,
                                        -8645812787162339431,
                                        2814448116044034863,
                                        903711551734479178,
                                        189163081794493388,
                                        -3584441446820763813,
                                        5237933443988801872,
                                        2577921362924010510,
                                        1687693863387179344,
                                        -4386976093194803023,
                                    ],
                        },
                },
                {
                    'name': 'пͳӏʀ\u038dԒȥåԝƿåɅʚğƸĸ\x8cч',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '΄ǳϸƗӆšțʉϭǝϡԊ#ġŞЬ˻ŌɃԒϒ¨ǜϲƭϵƱϷӫƑ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210129:002622.720772:+0000',
                                        '20210129:002622.720782:+0000',
                                        '20210129:002622.720787:+0000',
                                        '20210129:002622.720791:+0000',
                                        '20210129:002622.720796:+0000',
                                        '20210129:002622.720800:+0000',
                                        '20210129:002622.720804:+0000',
                                        '20210129:002622.720808:+0000',
                                        '20210129:002622.720813:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'һѬ',

            'message': 'Æ',

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
            'identifier': 'ӗԡǛԚ\x85»ǯɥƅ!λΑԝĈħ¤Ц:ėɢʕfʘuʈģЩъȕԦ',
            'categories': [
                'configuration',
                'access-restriction',
                'access-restriction',
                'os',
                'file',
                'os',
                'network',
                'configuration',
                'network',
                'file',
            ],
            'source': 'aǱӍEԑɡ˩ŭÂȉǆЫƥýΈіµϏϡƭӎѕϭƘªљЄĂĬ;',
            'corrective_action': {
                'catalog': '\xadԀĠ\x9d~ēύȝƜͻ\x9f˱ά\x9e˘шҠј\x8eȘˊÆsζǹͷʉŚƛѐ',
                'message': 'ԪͲÝɹ©ɜʸ¯ƷϮϸƦÛϫũĪİ˶ʮˎһȅɒ°Ɂʗȱɦȥϝ',
                'arguments': [
                    {
                            'name': 'ϥ¡ѿȵįϠҺ˥żԘβΏ\u03a2ҕйǃ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ȿːҶfĉtƊΎçђǭəŅΩ_ҲІ˷ϽļԖўțÔԀҷĢğĐΫ',
                                                        'ƁӞџ[ˋΏˍ˾ȦΓԟʦʭμɁĶˆΣǤɧ˲ˍ\u0380ÁȾƂɽдȩŊ',
                                                        "Ȝōԋʃóΐ'ɅΪ½Ȉų{Ʒ\x83ŮǺʂǘѨϖɟ҇ˊӑ#ύˆƆȻ",
                                                        'СơҫΩŝǦƚѐΟɔ˶ςłæѵǠťӞԞɶ\x80ɪƉƔʔҍΧѧ\x82ӷ',
                                                        'ĩŠЙԞζΪɃФɯˁŶȦȪҤϱįɩϑӛɡæӗƮÀƫѓΜҦ-H',
                                                        '΅\x9dŤĀӡĔҽȕɑØǯļŌŞƃȍƬʲЫΚӹԛǫŽӸƎħăϣϯ',
                                                        'ȍʅƌývвǥҘ҈ъȎ[eўļϜƟɿӇˠΏϾ˙B<şώ×Ĳí',
                                                        'ʊrǤÇԡňŊͳʠÔÝнƛòцˡζćƲƭϩ:˾ѿӂƾΎúμʍ',
                                                        'Q\x90!æϣȠνͿŁˣǴʬɛȃƫǤŵaɛ¾ʘ˪ѲӍђӎP¨Sʠ',
                                                        'ɞ\x84ѳ˟©αԙʮԄԢ\x8eΣӇԔƔÎӿЪӄǟӳǍӑщԊ\x8fѝÝц\x9e',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ǭǃ˶ΛъϼÍʗǣұ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210129:002622.716924:+0000',
                                    },
                        },
                    {
                            'name': '\x87ƈɇӃгƞǭΖőρÍ˞ŪӵųЍĭɴҘʆΊϗɎЎ¾ɑѤʓʢǛ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'яҺҥzʮҠϫε`Ԭ9ϮǊƃƇƋȝɤҥǎʰПÎѥˀİϓЮϐˮ',
                                                        'ӧМҝЦԥɚԂɓçơź\x84τĖϨŹ˹ыʸџ§;ťƽǴмŁаЏƝ',
                                                        'ҞñʁåԥҐӜǚǻ4ƵĺɺϫƏŵȬÝϥЪʊʜ\u0379LϺƐʊг5$',
                                                        'ү#ԉʮťɲɼĨξӤ\x85ҙǊ\u03a2ɣΨүʿǓϣϥЩѣѼҲЈĉΪgO',
                                                        'ҜĸqӶӹ\xa0ǹ\u0383ӱόXȔӖɾΧɨʥ\u0379ǉυÏƯӇȴVȪЁԙѳƹ',
                                                        'Ȇɸςνµ¨пʿϗϞĽµçȄӿͺϠɹƙǧɟԖŧВӓ϶ȽӛǛή',
                                                        'ą\x86ɈγюТ˲РӱɲưͶҹÚĊ\x90˺&¼ΉҊщőɚ\x9d`ËʮϞˮ',
                                                        'ԔįƓʺǈÛɇҺϜϸɮvƙѿƤͱӨ\x91ԡ^\x9fҠʞFŘϹʉʼʴź',
                                                        'Ş˛ȢÆ!ŸӪнБɧʑŴˡсͰʭİыN«ľĭ\u0383ԍűǒЉс&ȏ',
                                                        'ƥȀʴʫșλ½ύȼ˂Їе_ѸʛϡήȐͲËƣηĈΰөłƏԤW6',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ѬāʏӓӺƥѠӅĊ·"ӎ˔ЇˣZɦԆÖѾЧԚɊɠ˄ʫ',
                            'value': {
                                        '^': 'int',
                                        '$': -5651987422578203831,
                                    },
                        },
                    {
                            'name': 'ʞǾīЅsԜѐԆΎʹΗ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        193920.62207219936,
                                                        844185.5383817499,
                                                        655986.6044032101,
                                                        862396.484629415,
                                                        589042.2208121951,
                                                        -69049.78306955239,
                                                        942745.468911848,
                                                        145900.4516328072,
                                                        525823.6699854222,
                                                        877719.5354742784,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʬȕƳ˃ǃſѱZµ˝\x9bëɅΫ\x7főО',
                            'value': {
                                        '^': 'float',
                                        '$': 546667.0194946841,
                                    },
                        },
                    {
                            'name': '©ǄɦћŹӅɈ\xad»\x92ˠź\x97VҾОɉϐѻҖ˨ƒɭђҥȏͳƨýǫ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210129:002622.717926:+0000',
                                    },
                        },
                    {
                            'name': 'ŸҙΆғƍεЙŃ³РӋŇӠΐϯ',
                            'value': {
                                        '^': 'int',
                                        '$': 4312291360227461956,
                                    },
                        },
                    {
                            'name': 'ʃ\x86ѝϢƇɥɠЂǎ˻ăɥƪɡэґƺ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': '˰Ɖ\x8fʑИЯɦĄ˳)ȝЕƃƂœĴƣǮҸ_ǽҗɈωΈԜғǷУĨ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210129:002622.718330:+0000',
                                                        '20210129:002622.718341:+0000',
                                                        '20210129:002622.718346:+0000',
                                                        '20210129:002622.718351:+0000',
                                                        '20210129:002622.718355:+0000',
                                                        '20210129:002622.718359:+0000',
                                                        '20210129:002622.718363:+0000',
                                                        '20210129:002622.718368:+0000',
                                                        '20210129:002622.718372:+0000',
                                                        '20210129:002622.718376:+0000',
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ЛWύĥ5ɇƘɞøЊǘϞŐўƓһǠӷʐˆϩ8ǔŅ¤ϷóƆɌӏ',
                'message': 'ЍάҘĐǖĂƱԠɅѽÿĥķƯӐÅŷˍÓ\u0381ȢӥĶЭ_ïǨʌɮŌ',
                'arguments': [
                    {
                            'name': 'ȶ˃âЧ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210129:002622.722487:+0000',
                                                        '20210129:002622.722495:+0000',
                                                        '20210129:002622.722500:+0000',
                                                        '20210129:002622.722504:+0000',
                                                        '20210129:002622.722509:+0000',
                                                        '20210129:002622.722513:+0000',
                                                        '20210129:002622.722517:+0000',
                                                        '20210129:002622.722522:+0000',
                                                        '20210129:002622.722526:+0000',
                                                        '20210129:002622.722530:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʜÚρŦvяŞЭ',
                            'value': {
                                        '^': 'float',
                                        '$': 74194.31898987299,
                                    },
                        },
                    {
                            'name': 'ȍ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -7387999937971514475,
                                                        -1103972706691536778,
                                                        2159218001768988224,
                                                        6055509087830267763,
                                                        1637288519174910873,
                                                        -2915758252156139549,
                                                        1207182138030299341,
                                                        -1454342103025598611,
                                                        8718663170696551614,
                                                        9221522200604500706,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӲƍҶƜˌѡǁ\x83ЄԒɻӮŃňǃрͲĂӶ˝CϑΠϰǵɁſȺɦĺ',
                            'value': {
                                        '^': 'float',
                                        '$': 705948.9031384933,
                                    },
                        },
                    {
                            'name': 'ϥʡñø:3љӼĒʇӺ\x90ҷѨϜɋԝŞЩЙӻԩԐʘϛȋ)¯\x87ϝ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210129:002622.723236:+0000',
                                    },
                        },
                    {
                            'name': 'tćАɈ¢9˦ġԡňͳΑ\u0380ҭʤʰЈҲ˜ԚͼϞǨ҅',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        24852.546201496094,
                                                        298624.6306692724,
                                                        805458.9940759421,
                                                        865408.4246371514,
                                                        312947.3526850703,
                                                        191010.07340664894,
                                                        386219.0740355151,
                                                        587788.5799314985,
                                                        615105.5000702038,
                                                        -36858.24181565334,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ōϵ˓ГѧӜжŻ˧fҼϏþ˖ˉϘЯƀϝͷñɦҨ+ҷǠǩ˶ˮϭ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ɋϏКƵӚĭȭѝσǱɰʽɛǕӁҢϞˬɑȎԮɕѮҟԈSÞҢʙС',
                                                        '¹ӕѓ҆Ϗ\u038bǐ}ШǕďΌԨž ѢҳАÚʞǀԔć҇Ƚ˒˼ʠӅӈ',
                                                        'ɸԁԄШЖƍˑóÝưΚ2ƸӞ\u03a2ǋǹȢƑĜ˭ùɜϏđҤѬκ˺Б',
                                                        '2ŘȴΆӎŸϪ\x83ɽ6ʽҀƟЗqūɚ\x9bΙ\x9aǩƃϓѫϝΊʶʉыȃ',
                                                        'ӝ˅Ȉ҄ƜðȔ2ϋӲwʢҒɔáъ[/Ҹ˔¯Ў˝\x86kԟŬǛ[Ϟ',
                                                        'ƧǼϏӶѐϹ-øЍҎºʯѽϲŻӵ\x83ԂˋúɅ\x98ū\x96˭\x83ҞűĭϺ',
                                                        'ҒЕˁÏǧiȤyÿɀϫ\x98ʰˬă\u03a2άɗҴɭӌơΜњʹӭƉÇŤô',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ξ˖Ŭ}ӏӉȉʈЂŕѯȰyŽʣѦЅ©ԦϝŗĵÙƩŹƊϚҚËѨ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210129:002622.724002:+0000',
                                    },
                        },
                    {
                            'name': 'ɕŎҵυѽɣǡśƀȓnΨęӎӇԅÜɖЭáΖïgäβό',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԗƁźPĺ҈ð˚˜ɪƄΟǱь\u0383ԕŜϙҖĊÍӺпͰȷ˽хʗ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ЧżʤȀɭƥë4\x85ƚȌƍÒƢҳϫ\x8cЙʈĒŠ³ʘΖп1жМƕқ',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'тϓʭɋҲ',

            'categories': [
                'os',
            ],

            'error_message': {
                'catalog': '\u0379˸',
                'message': 'Č',
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
            'name': 'сψɏ˒ʭÚoʧѺCϏӄƾǾ˝ЛǮÄʸÕб÷ƙΗȅ\x85ϗÝʕÆ',
            'error': {
                'identifier': 'ΊȇĉȭӎϗȦœҩĠŪʬāƆӺГbʥϽЙжƼ˖ͲϸΰĈүĭӑ',
                'categories': [
                    'access-restriction',
                    'configuration',
                    'invalid-user-action',
                    'internal',
                    'invalid-user-action',
                    'access-restriction',
                    'file',
                    'network',
                    'access-restriction',
                    'os',
                ],
                'source': 'ʷȭЇΖӕԠϬԑ_òIʶ˘˪đөyԚŶʝЇʶϜʊʊȍҽҠĤp',
                'corrective_action': {
                    'catalog': '¥ƮҝϷœǥɓүȆϽϫþћɈȆÞĘʹČӄʠƚҖΦʸĭoοÀŕ',
                    'message': 'ҲţъѨɸϪʴƈΝԡɩҙҡ@ʖʝğqǯγԂǔŭəӅё\x9d\u0382eΗ',
                    'arguments': [
                            {
                                        'name': 'nѨƴoҊКЉƔǶǊăǶÊ\x9dȀԕλ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӂӣȏԆҞӻ¨ʋχʅҢƦ\u0379ԑUϕѫӠΒ\x86ǳθʸ҄şΘКϗ˼ʦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 926510.1244638962,
                                                    },
                                    },
                            {
                                        'name': 'ěН£ʚψľǫÜʚγ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\xad0bʫŨȪďѼϐ³˛ĩȶΓɔѸχî\x91ȦҬ˾\x9aҤˉȳƨЦɍʊ',
                                                                            'ТГɰҳÌԅűͳrȪφΒԢƙҕЉƫ҂Ϝ1˖Ń7ĄĬҾǰѸӸȳ',
                                                                            '\x93ɆСƦϑ1',
                                                                            'yŅ\u0382ҨȨƘɓpƾѳѡҞɀÀ˸ɤѐȖЁȰŃÞƎѥѬӣΖȨ£2',
                                                                            'ХȠ˭ŅbǑõƣɷϗOţȃːȕѫɱҠǤәӒ»-ȸʂǁlЎȄ\x8d',
                                                                            '˸ÉƫȘRȱưƼԔӚҘXʄȵǝ˜ɰӪùѷӰҖɝді˗ϊū\x93қ',
                                                                            'ĨíĻƤԀȉ\x90ɏ¸ΚSæ¾ҾcʁŚјDµɑԃРѠƾҭäϙѸϛ',
                                                                            'ωѓѐӰǌƏƘѣ(ƣѺĀАЛƄΣɁӲɖΡ҂ĽѰȋϩчķРͼƵ',
                                                                            'ςíҮ§ˌíԊΞğbϝҖИұзѡĶwˮѡԢɬɷЎԖ˼ÅȌŀѫ',
                                                                            'Ѭϐőƭ¥×Ƿϼɥlκԅϴ«ӶюŪľ˛ҴҁѽV\x96ɩEλґưj',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŌӨʂѽɩəI˳ȎUϮÍǚɡĨ_ѳʗ˺',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȦхɝƣɓìʩȌʴȝŨƅԈȸŢ˩ғŸӢù\x9cϬˀʅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'р`WԥùҨԫϾϲŉϒ±ЌYĐη½ϐ\u0379\x7fƴÐʝԥ˷ЫǇəѧЍ',
                                                                            '˼~˹ȜŭƹĚëКËϖȈȐԧɂƍό˫˚Ѯ\x85ſmІϢƸζĖԑˆ',
                                                                            '3\xa0ʸ\\ѡˬŔOðȺǕėηԏ˰ӧ2ԢϘyʭWȨļϞͺÀљɝϢ',
                                                                            'ũ˸Űèϫ¾ȮÏрӕƿϪŊҪ¦ȐʧǨ~ӂ³ôĪԇʁʥķԔʎˌ',
                                                                            'ҩφțТ.ŁԢЂӷĦǇϚ˪ǼΔʘǙѰÐЍҽшƇÒҢȑƚJųź',
                                                                            'ƮұӚȟʦêÏҒԘԖɌͿƺωРԆƞԗȁ˶ӧɑɫϭǻĻά҉Śԡ',
                                                                            'ѷ˩ǈƜ˂фԅђ1ƀϭѭΧİԞԞ˺ȂϚʃѮʦшȴŴŴɷ˫eˤ',
                                                                            'ӤͼǗʥ5Ǧ˾ԜĀÌ҂ŁΊ\x84\\ЏĆPəû\u0381\x80ʴbȷΕĘԑӹȨ',
                                                                            'ȜȤȪɘьŢϰȠȓτӊȊѧӅ\x8a`ďƺɶΉõгkĔϻʙωʂӷΣ',
                                                                            'ǚϫІѫνүԜХÙσȂŚϘäɼ˲Ɓ\x82ʎ\x93ǥůӓæȇÔĖԋ\x88ˉ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '=Έλ҃ϽˇƳϱg\x93țȄ҅Ӑѷ\xa0Ωţö¦ϟҢӵȪӷƻӷċΨӕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5442903853568963447,
                                                    },
                                    },
                            {
                                        'name': 'ϹŵϒӖȲ˭ӞƥƄδƤ\x89ȾԓπːġԕɗϤδϮWԚȨÊϠфûȦ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '4ζɁ˙˘ˢӭдXӔҢНƑ%ΐԆϡӚȏ§ѯ\u038dϮӃʖϿԚǓɽŒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǖûŧʩÓқd\x98Ȋθȼŷ\x9eSԬ=ːуљʡȻӛ˒ɲĩР\x91V˨ƈ',
                                                    },
                                    },
                            {
                                        'name': '˞ʾɋƐӣƕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʫќɩȯԂυƂǝԑū·δͺԒκѐDďҶϼ˨əλŉϔfѤɢ\u03828',
                                                    },
                                    },
                            {
                                        'name': ';Ίƺ˝ȏҳѬĐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:002622.712763:+0000',
                                                                            '20210129:002622.712787:+0000',
                                                                            '20210129:002622.712793:+0000',
                                                                            '20210129:002622.712797:+0000',
                                                                            '20210129:002622.712802:+0000',
                                                                            '20210129:002622.712807:+0000',
                                                                            '20210129:002622.712811:+0000',
                                                                            '20210129:002622.712816:+0000',
                                                                            '20210129:002622.712820:+0000',
                                                                            '20210129:002622.712825:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'λ҄¿ϳ˴ҠŰѲʃȥДɈθʩˋҮĵϣгʫԈ\x92ʽмЯТѫǻЗ«',
                    'message': 'ѣԓę±\u0383ǣңˣφɛѢȾȃϹ ˺ʛɒθϐɄӖ{ȹΨȥҏʛġƖ',
                    'arguments': [
                            {
                                        'name': 'ŌнɪљƛÿČɻҫɸšЕͼԦİƁɻɱǠҌрǛԍ±зԠȔwĔƝ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -875747321981698179,
                                                    },
                                    },
                            {
                                        'name': '˻ншүÏаҳ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 688438.4945267423,
                                                    },
                                    },
                            {
                                        'name': 'ȿԇӎȳԘ¢ϋźIӘʯƻ}ѼɠȷȲʘ҄Ѹϸŷǡŉɱȸ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɀɪЫ\\Ř\x93ÆжkȩǉƿϧήϹď˧ªʠѹȓʲŎ«\u0381ϤġɳɼĀ',
                                                    },
                                    },
                            {
                                        'name': 'ąΎ]ʓĈξź@ɍ0Ȅƴ\x84ØǝáљZӰʍ\x8dǄˇςшȦ<и',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѹͺȆĕŜ\x88ʺ\x88ӗ˘Z}ͺϔ.ʬͶГҕ\x81ӕł8ɏÚŋ¤ԌöɃ',
                                                                            '\x86GʣˮҾФŪχяʙɚδ!ƤŒȮŐЍȝҰ҄\x9eıƕƎӷČƧЊj',
                                                                            'ȬʓØ#ĨŏМӏ¿ӤɁ±ԮĩȦƿɱҨҭӑбҮ|ӝĥəΎ¢҂Q',
                                                                            'ƲċǮ.ƲҽHʅςʻʄŮðˈԠżӇ҈bαŨԉÞͼǴжŋˎƖȽ',
                                                                            'ҏҩϐţҒ`ϴȄαôÐФ½ҘѢ˪\u0382Ϟ\x80Ԯ\x97ίНӵĻʅӻѹĺ¦',
                                                                            '\x9eY˚4лƥȺɍʉȴęҐõţ¬ƯÉȄѺŝӁ˵ΥˢǾĊ\x8dʍ˄#',
                                                                            'ʜVǲʰΚȼсşþӛҶǺXǛήϴκȑĭŚȌǉϱӣ£:ҋɛƵɇ',
                                                                            'ēӨɔ!ĔĈԦǥǳБńΕǥҴψɈFďšŸѭø\x8cΒˎʇǏζȂ\x88',
                                                                            'ʸԇϧЅʶγIʤǈΈОĊȺʒөҐŮҝéͼΊɥæɯƣѼϬТѥŬ',
                                                                            'ϳҴӁНČŀȥƟʈѬΣ˧(ɇĒЬʸŔ÷ҘÁƥƆːΡņ˲˰SĘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȯ,єà˄Җɤǭ҈ˬѥԜύwȀΨĈЭӿǌ˪ǜφ~ʊȰq\x8b˞˫',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            173768.55566012912,
                                                                            681484.8099931822,
                                                                            540265.8236307197,
                                                                            710093.9387450308,
                                                                            297718.5198975625,
                                                                            102017.5165147912,
                                                                            766865.3958178004,
                                                                            479693.1807243263,
                                                                            260213.57152708975,
                                                                            639437.7414908647,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϒҡ°˓\xadμäЬŞШŇĢtΑ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ԗș\x83Ġ¯ƎӤý˩ҒêƯǎǺХ˔ŠǉϐǱʶԐßϖԟĔ¶Ǒľδ',
                                                    },
                                    },
                            {
                                        'name': 'ɂŜáȪƬґŗҠһŬǒΝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:002622.714510:+0000',
                                                                            '20210129:002622.714521:+0000',
                                                                            '20210129:002622.714526:+0000',
                                                                            '20210129:002622.714531:+0000',
                                                                            '20210129:002622.714536:+0000',
                                                                            '20210129:002622.714540:+0000',
                                                                            '20210129:002622.714545:+0000',
                                                                            '20210129:002622.714549:+0000',
                                                                            '20210129:002622.714554:+0000',
                                                                            '20210129:002622.714558:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƕ͵ŅΧäÛǣ\u038dσӶšΩŠњΝѷЬɉͱҶДЍҩәĩυԝȑжċ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:002622.714774:+0000',
                                                                            '20210129:002622.714782:+0000',
                                                                            '20210129:002622.714787:+0000',
                                                                            '20210129:002622.714792:+0000',
                                                                            '20210129:002622.714796:+0000',
                                                                            '20210129:002622.714801:+0000',
                                                                            '20210129:002622.714806:+0000',
                                                                            '20210129:002622.714810:+0000',
                                                                            '20210129:002622.714815:+0000',
                                                                            '20210129:002622.714819:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʃūøʑ]ͺŊϑӔϒøƔЈřЍö\x860ɺԆɲɇʇǰ§ÚԮuƭǸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8821451896746713291,
                                                    },
                                    },
                            {
                                        'name': 'И҄Щğĳƺ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2906778990086953401,
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

            'name': 'ΐүƦ',

            'error': {
                'identifier': 'ˁƧҸϫɃ',
                'categories': [
                    'network',
                ],
                'error_message': {
                    'catalog': 'ʊǬ',
                    'message': 'Ǝ',
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
            'name': 'ЖXǵȳӤēƂΣԙȑÐгνȼñяʱʹ˙řǒĞğҥʄĂǧҊҫÄ',
            'version': [
                -1158471598537474442,
                -6722101322929702675,
                -4876258425678948457,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ãˈϓ',

            'version': [
                -3242326470211381366,
                -8896857504883983107,
                -3710648303805013719,
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
            'event_id': 'ӅύфԞԪˢɖԚӪÕѲЛѿԥѾǜѨѶΩÖʓѫԐ/ˡˌ4Ǆˠ˖',
            'target_id': 'Ɓϝӣ˛ĹǎʒϟǌKɥ˕ɕϮΕ\x80ӴвϜŷӯҰжʧƶƉdĂËɄ',
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
                    'event_id': 'ԔԒϨˉƧѲ˶ΝΞ͵˺ӯˬìΡӟўǾʜʵx%ɏ˷˼?ԂŘШϹ',
                    'target_id': 'АѱȀѴʞŬҽиƐӷñUϿ¢ʂȸЄÛ˂ƘǀȢϤЌ',
                },
                {
                    'event_id': 'ǲŒǫŨǬʾЋϪϫόѣ\x8b˂;ӻȎģлЛĜ˥ĕȒƣƋ˭ԉ',
                    'target_id': 'áī-Τύŝ˔®ι\x85ϐIҠŊΜɛ$¨҃Ӗʰ\x94ћ÷~ғҵÃƭБ',
                },
                {
                    'event_id': '˞ЍȑωöϤêǸ>ŀ¯őФз¼ѲɟѺʲǫăˉӖːȵȫÉɚҿԚ',
                    'target_id': 'Ћ˨σѼͼ\x85ҩЃīȁȋ´Ə\x91ªӰáӿĵ@ϣĽ`ȽtʃĝЀϗѐ',
                },
                {
                    'event_id': 'ʿàƜŉʼЧҁ˰ˊѴɭæΫȪΣŀĳΝҖŉõÏö¨ǄԖϷÆӳ(',
                    'target_id': 'ϴҚұŎЫŒĩŕДӍоɰ\x93ƗρҴЇԘԞúĳЈȁʙκ\x99нԛԥ\x8b',
                },
                {
                    'event_id': 'ŋɫѝƐωϲ>ѥÐТsȼʕЏΘԡьӇӗȁnǀ\x90ŴҵÒiŇƹѦ',
                    'target_id': 'ĄҷήǩţˈϷȀӊ˂ģϴβѠаҎµԐŤ҃BƵϭőӯkģіė>',
                },
                {
                    'event_id': 'ҷ¢čDȳӥћϞ(Ũ˹ǆĚ˝ΫԠȌҢ`ƖȲҩϢƣVɼЗ;ŖŚ',
                    'target_id': '<ќБ¬ɶ°ǣȋ҅4rfûŀǖžϙїνЏӮˊͺù\x81ɭɰ\x9aӂ±',
                },
                {
                    'event_id': '<ˎĭǟЗΖŰΔɑH{ʔȎˊÈ\x9bԣɐÇȏɖЎ<Ēϧʴˌɯĺ{',
                    'target_id': 'јËİ\x9aɺə\x88ǬԐʚȋOɞƀ-ԍ˅ЯɟĸƆɞɠʔԓß\x934Ҵľ',
                },
                {
                    'event_id': 'ϳҽċЕʞˁš˜Ǎň˪Åˠ\x9eīŚѧϲ»õҷ˖\x98Ņ˽ϯЩҍ¡@',
                    'target_id': 'ϩǉ¥˯ɜϣʑѸMϒ\x9eɺȫÅcεƥ\x95%ʈ\u0379=ʑƶʍ˹-βԄӴ',
                },
                {
                    'event_id': 'ҟΣЃϷưºГӖƧɥԡƟƕҜˎҨǄҿы΄ϡJЖәɰθԢҁɘϞ',
                    'target_id': '˱JԓЁНǟǈϤҔĆkƒė\x86ӒƁ\u0381ëʂӋTƉUwǽѱƾСŴ~',
                },
                {
                    'event_id': 'Ч҂ʇƾǖæЧĢȐСѬƵžȠңʿугȅѧʻҿʾѿϛСǒþΛο',
                    'target_id': 'Ўŏ±ЁΏϳёwÙӳ¸ц\x86ŦκǱψĸԃΠϜѲ0Λϳ\x7f҂·\u0379',
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
                    'event_id': '6ΜʓǙҭǎҠсˑkNϾÇƘеʆӞϐΤȢԟпȠЖӏ{ЬWīͿ',
                    'target_id': 'Ӌj¼\u038dԗӞɡȮΡÇųЙɢǸ\x9fѾǕ˦ʙwҢԈ|ϢƃЮÒʾτʝ',
                },
                {
                    'event_id': 'ɢɝаɸў\u038bĕĳӽbȆƷԑTҥԌʧbα\u0378¯"ԓ˕шɾӧ·Бŋ',
                    'target_id': 'üÀNѤ·ԍ\x8aϥĨσϿČàƥҔΚǥбτɢ˵ǔңпιүДǙʘ҃',
                },
                {
                    'event_id': 'ˬ^ӀʟѢɵȡʰò1ǗvÙǸҬ«ſUƭРïµχĚӔǕ-ʶȽƚ',
                    'target_id': 'ƷԇȯƀҒĪ{Њҫ8ǰѵ§ˈǽƨѾ˹ϟʴíҠӾͲӚԬʟ\x89Ѓė',
                },
                {
                    'event_id': 'ϪϺ\x9c%ʻą˙êŉϢИГҁѶǑԊǏħcŷȼӵ\x9bЅxŔĈǉӗғ',
                    'target_id': 'Ё҈ȰҴ´ÕѥƂǒȇԬʍć}ЮĒʢϊϐl˲φ˴ɄәЈЇȺЗE',
                },
                {
                    'event_id': 'ʘˍңȁǀgʤƁ´˜ҢӒȏPԓÓĠɍČʹïŒǓǀYʣЮǘѦƼ',
                    'target_id': 'ЋԌûһǝлƠȭÀóͰƼȎī\x93ьӤ\x88ʤŉșҼȥZӃœōĪҷʋ',
                },
                {
                    'event_id': 'ӮǛʋҝĹӨϥԁŞȾƷ\x9c҄ҊѹȦщҜΪӇųʼˈһӅˢъűͽƌ',
                    'target_id': 'ůѽŢȑǩúӥΝӤғșÜӋ0āîƘӮɷɟЄɤĠрҵПƱƯĥɚ',
                },
                {
                    'event_id': 'ʞÆÊxɓ˝˭\x84ǘȰ\x87ǅΕǪΐȠЕқ¤ǹ˃ҳ˭ȭΩėӱˈʚж',
                    'target_id': 'їÞπîĳΆКɹˉ+҅ѽҳƻ˚˔ʖɂˀʳʥUΥȺƯЦɏ\x81ԝɱ',
                },
                {
                    'event_id': '»ԐӇƝΜòрˡŲϒâ\x90ϗ¸ǙƠɪѣȱԞʞυтҿӷ2П\x87ϖŲ',
                    'target_id': 'ÎɭùȕƁϏmϠȊаućи',
                },
                {
                    'event_id': 'țŏŗѩCłńӂҷԕƂёғƾЗȰöƓҔҁÖŉ~)İ˂:iһǔ',
                    'target_id': 'ĬѱѭбСɍƇѵǋõАӗǱώȌӆƣÙЅÁȂÎϊΚğȽʳɩњĄ',
                },
                {
                    'event_id': '\x9bҮԂͷĹʿǎɔǉЖʥʁΰԦǂŷуаɬȒɊĭÄЬΌȩBҋυǩ',
                    'target_id': 'фȯԄĹ˔ҟÔɱȅ˦ӹGťʱ\x86ƈϖVʀ-ʜfҀƣϠȵϷϰÀñ',
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
            'name': 'ďϡӳԒʌĿʰǈƺƏӾȒҎў˄Ċ\x9dиȀʶ\x85ƕÖƗëϼ§Ƭӓƃ',
            'version': [
                -5606802088791280785,
                -6154441736060688797,
                -3472125350708897433,
            ],
            'about': 'śӽʎɚé\x98żʄŚmЅǄХң˷ϧµѠĺƏŏƝЩÏλ˱[ӖǺѽ',
            'description': 'ĝųɩМ҅ƭԂқŌÙӸb6χOǘÅҊœ˴ǜιżʀʶŹԢ˄ƕԂ',
            'authors': [
                'βƂǚȠʃ}4eΜЂňԈтɱ˝ǉʚĳƇȒǽΣſԑϋϑϥҾƛȺ',
                'φ͵ӧʎӉӺƆÿԥǝΙȓҵʚʝԡʈ#ȪŁԮйԁƀϊ¦ҡ+ʞŠ',
                'Ċѐð\\Чµű+ɲɇΒμӝXğň˟îбʗŇѠԋ³өÈɒϩ\u038bˠ',
                'YӤȮӻԠő|˵\u0380ƕоƗ~ӷƧφ;ĂȶOʄëŊгІӌӯǒĻŅ',
                'ʂʂʥԢǌԂϑǢőҍƍl¶ʌŧɷɐĞɲ\x8eѵÔ(˃ʖǜɬɣбî',
                'ǭеБ9Гˬëŏͷ˞¤ǕˑÿԛŽɀԋɁНӯʈ˗X˛ʆRƈ\u038bÊ',
                'ˮƐҵέ$Ŧ˰ԇXϓґω΄ϳԌΟóȡĘǜʟɡąΐĘҤӬƁѸɲ',
                'ңȎàż\x89ӑǑʩƙϟǟ\u03a2ʞ\x91ɯŤȢɘ¾˞ĬɑðзtϑƷʁѓѵ',
                'fшĲϺЬʡԉɌ¾ҫȵʋʢɁЕƆԦʠȚŧɋͿˬǣĬӕϪҘҡ\xad',
                '\x9b҆ЂǢѥӠȯȢƽНɤǯӅūЈ\x91θʽMҍΧčӴĒј˶ҞԜФӀ',
            ],
            'licenses': [
                'ˑԍ\x9cšʩѣĊԣĊɗʎАĢ˖¤˥ѤϫȘȭϚ\x9aɶϏģğǄ˞Ҁӹ',
                'Ү˳ɝéłǦҢĂΕΎƎǇÒǑȡ',
                '˺·aϴϝЎд\x89ӿɣҷÃďɛԭԭԑĥŹбÈԀѳΦ\x86ǈϚűùȮ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʐĳԬ',

            'version': [
                -421679235214853405,
                -6263473695819880053,
                -5444389157250605669,
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
                    'name': 'ϝԜ\x81Ǔ®ČɠԡÉҧ϶Ԃ\x93ЯĿϼ©ңMɂʔʄВƩɨ·Ȃʸãҵ',
                    'version': [
                            -8761752619560937963,
                            -9164591507535475717,
                            -3410267888670321490,
                        ],
                    'about': 'ԑСуϊҬčǮǚӑԉԬƽ\u038bΓҠȸʣåƂӤØҽˀѵΌǆ%àӻǊ',
                    'description': 'ǬȵjɢӐμ҆ŴØɗȁʂŴȧȼʟʵӡΆȡĭԆǼΑǴƿȵϮÇı',
                    'authors': [
                            'кƣϦΗˎϳΰ\x9dҠΛщʑīӀɍ͵ǐӧĖҟɧJǰԅɂŁŶ\x96˔A',
                            "ĳƨλƳŔ'΅Ϫ˄ӚЅΟԂ]+ǌ)ƺˑžȂӛȺã\x96˗4ųΝЮ",
                            ':αҦʸƙʴǲӲoċ^˂Ȏǽċ¯ЊɉӶġԅӈКŚϷȈşәґɡ',
                            "4ǜŇŬǊ*ƕԮɆȥɬľʝ'ɋœƄʜ¿дЙх\x99ǂԜǫЖԥǔI",
                            'ʓȴȒïɽɵɬĒ¯ͲέƠԖͼńϙҎҼȜȣàɝŀĆǫɦϮ¬Ӫ˘',
                            '@ǥεϧƥҰǍŮʴӑДξȒҝ˩ɇʣÑìɒ҃ғcƸǦӆøƜʱΨ',
                            'ƾӫŶǓэԥԏŚЭɌŕϭǏŰ',
                            'ĒȄGˉ\x80ѵUʼʪБžơȞɤ\x96ǺĨЅӛƖҷμêÄЧӌɐYɣМ',
                            'ÖрĆ=ůǡϩϢçʢɡҏ˔ÏѤɛ˚ԤЙǄʿέʛѝÀҺ»ӓ\x9bǚ',
                            'ЗѧΓѕϐƼɝΦ>˃ϝɔśʿΆʘΡƽΧȱ/ˠÚǵίȣǂѨ˷Ļ',
                        ],
                    'licenses': [
                            'ϭҟҪÙӹƉʿǺɚçˬШв΄{ϓ˴Μљyʶ\x805ϱ~ëƸõҴß',
                            'вшβȭƇЖΗ˫ʭԥӜíɥƻѰȹ²ý24ĐsҎӴϬƥgǱǹȫ',
                            '\x9cĄƤϻƷѣʬʣĿǼԏř˟/ҿ§½\xa0śήЋ¤ǻԦņ,ѧÐˑǑ',
                            'ǕńĨĜΪѼȾĩǳӾɶӌмиɤįӴ\x92ðӟʥ˓ԎгҡмчȀˇЊ',
                            '|ӔŵϱŰvŤѓϳβʦЇӃҪТŀÉɮȪ\x92˄§Ů˞ƙ\u038dB®Ɛϙ',
                            'ьǼӘʦЫαsϽŢ˺¾ǷǋĘ(ŐӡηˆɢjÔ қjɕɒ$ћ\x8c',
                            'ɀķ±˼PҁĐń˵˚Ġ\x91ŉɌˆˁȿŐӴù^βΏſkȨϡʈɥņ',
                        ],
                },
                {
                    'name': 'ПŁӆІԫöТʤҜƘƛПď˙ωŀ˱ƫșʄ¬ҩӃ҄ӼԓӂҳȾƎ',
                    'version': [
                            -133837310224902661,
                            -2816048094104780011,
                            -6858861671240354897,
                        ],
                    'about': 'ęŧʙӫǙȰȻɢѬɧӽǊǭӌǷźǣ}őΕ3Шƛҫўɯȓȥɰ˭',
                    'description': 'Ԝ¡\x95Ƹƹŋ\xa0ҼºƐϒġфΔ˻ԅĄɔϱьԮƧǇȮƻˆîķÚȞ',
                    'authors': [
                            '҅ŻϸŘǪԨ´Ԋώ3ϭӼҚѹɗ¹ʓϡé©ϬĮŅԓҫ˶4͵qλ',
                            'êϦʹơy˒ɁмӶ҈Ɋɚ#˫ƑňӰ\u03a2·ѾˠÌȬӁҪĝfΟàʚ',
                            '(ă]ҶԬƢҵǈŎЗӃˣźȔ ұƟŉĀŝπôӅƔƑ«ϴǮȚɏ',
                            'ŔтʕĻӚͱӡͼϒцŚԣʠ',
                            'ťİȘÙˤƈͱɍěԐȮӹÛǇԃʓɩʈʭŭͶ˳˜ɛǫ§ǑмǻӠ',
                            'ŝзѭӨѶĚϦ/ӤŹȒѡ˷æ{Ȩ¯ðĤлǛӅϷƝʎ\u03a2ćӌĖԟ',
                            '˙ÏлgϻʣǗҎ˘Ǎ\x97ҿ\u0383ɺŷľЂʭ6ʦͶ҈ʩƺ©ȬŚә.ȶ',
                            'ŎtӼʈđ˕ȓû¸ͱ\u0383Ųüʇɔ\u03a2ԥƟäȟʉɹӏҔҧωäƏƼς',
                            'ӌͻƔӹƍƄƥé8ˏƉ\x87яõȨӒǁϽñΏȧƔĢԄȼʇŵĲ',
                            'XΑu\x9cɅƅ\x9dȮΏжҨƩήoГɚЛʛΤЅʓѕ4þԉˮϽ{Яă',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ȯΪ˥0ŧ@ɎǾĥʠіЇɮԔǞоΘǽśСӏĨÍυѕIŢűȇӶ',
                    'version': [
                            -2959238958153597374,
                            -7713763589660079587,
                            -3723393377886431897,
                        ],
                    'about': 'OѸŠcƿǟŌ\x99ӪǮbƅȖЧˇˈгҬť˘\x7fɥÉʴÜV£ȸúÁ',
                    'description': 'ÎɥϢʬƯˈÇҬƏµΝΰ˝ϡЗƼңýǺѸbƍ˒ēɃǄÅɏɕB',
                    'authors': [
                            'ƷΟз$Ǭ`У',
                            'ϝǁȞѓԤԏŸѬδòѱЊțΗҳî8ѻƧԏ&˹ίЬεɦƢǐ=ҍ',
                            'ѪǤơĶ`ϡ\x95˂ɏȜΤǒɡĳůҙȥԆҁќɮ`ΔˋʬУʌԔºь',
                            'фȃ&ƕоĶʬаҗҫҝΝĀі',
                            'ɾӭҴςʞӼΞΖҴлԈƂȵ¡ː²ӸȈϵ˵θ˒ѯԥ;ŲҔƠ±ù',
                            'ԠǂқЙҏɲўѵʰ\u0380ĤϨȒԆҋƷǁЮϺӲҕϒˡӠӱΣӧȃÆĴ',
                            '0ƷӽΤӰVπu\u0383ͰǮǵƪDʷɃ*ɼcƸHϵ\x7fшWǊԜUφм',
                            'Ϸεόȅ˼Ҙ,ȻҏĐ$ЈƱЬʭŃ˭ßţʓīN¹ȄӾͼΚʽƉù',
                            '˜ԛÕɀԕ΅ΉŶҞœȈiȠǷҏ¢ąαηʳėԋÈƅӞѭɓĉМĽ',
                            '\x8ckɌ\x9a\u0382şgǁэΉƊfÜқˬ\u038bρѱҙәʤƄLˠ¶ОȁӟĿͿ',
                        ],
                    'licenses': [
                            'ѺÉȧʟ;\x98ÝƍυμΠ¶%ƮɏϰϲԣpʩҔ\x83ӏlˈ˲ӫɪ˯ȇ',
                            'Ƃ\x9bȐƆ\x90\x92ƿнӓΨɝȈ}ŜϢ\x8eӌȷǹϧİҶƄ#ʚ:Ơηʘѩ',
                            'ʆϹ͵ӼӬʺ\x92ŴӵʉȌĐŢ˧đҋԐĭγѣѿÐʁӈ{ʷΔѠīÊ',
                            'Á\x83Ü\u03a2ĆăĂФҲƴχЪQƶјŘмˌ˞ʞʌĭΤӅӃυɋ\u03a2ѷ\u038d',
                            'ҙˍԪǰȨ˔+ϦԃͰȟɧɁψ¢і˙ԉȸĥ˂ʂƓˁʙϗɾǸČѡ',
                            'ʧ\xa0ӲѵȺơǢˡȶĮŭȅǾ\x9cԚʘƣͽӆɂzˉ˘еοìӾɺȤЯ',
                        ],
                },
                {
                    'name': 'ð®%ŞZκԁ}ѷȒ˱áɓ$ĿǙǟųǅ¤Ǿɛlӭ\x8d49тƕŰ',
                    'version': [
                            -2160403955755775617,
                            -819242220668101762,
                            -1820262155578681467,
                        ],
                    'about': 'ӢΏЂ+ǅǊ҄ψŹә¨8\x93¹˰ÅѩѻѦĠ\x9dʠѰhҙƟțʬơî',
                    'description': 'ӇǥӾͳўÀʴ˟ɑ÷Үǚƒɨ˗тΠyνѴԉÛÓΜÏÂ%ήƪȅ',
                    'authors': [
                            ';Iϰćȴ',
                            'ҏљ\u0378ΟµÔåţәĜάɱŴɤˎɱ¿Ġлїʯϳ\x7fĳ·?ɂɆЫӺ',
                            'ʞӶʨѶҕǷџǳΔƖйĶΖѱVԟҦј©ђҜ\x86ɆýÃ~Ŗͱƾɕ',
                            'Hӊ˟ЖѽӡÁeήȵӧ ӖӍʊĺ҉ǯĐȌŁ˥ѾӢ\x933[ТĀ˪',
                            'ǆőˀĖȇԩіЕ÷eʲaˍ˓ҿɒԫӨưλ\x98ŗſǁʶҸʓ',
                            'ԃ\x8bòɞ}ǳ\x99ώŅģϯɎӐƍŪh\x9cė˜ԟΉrˌ˅ˊË\x8cîϪǈ',
                            'ÐɣηҠȤɉΎЇKΙɐеɒáuɣшŌǑɁΉӳvǅјA҉˹ĺң',
                            'ѰĢҼӷëȋɌƟɱ\xa0ȽхЌǀΥӫƤɘǎРřɊͿ҂Қˁǯϡʞ\x81',
                            'Ȣ΅ӂŖʟїГʷΌɉϑťǐòыϘȲrΞжͰЋԄΩºӉÜ\x80ώɢ',
                            'ȉ@ВҍĠӈĨ˥Цǵʽň£сȱԗʦÒ·ϦÛ\x854\x8b\x95ÂȜǾǐυ',
                        ],
                    'licenses': [
                            'rˑȲť',
                            'ӿӮˣЦҡͰ҆ɳčЏҥVʼ@œÅ(\x88ĩӥЎŁØFΘá\x9aΜϷϡ',
                            '\x9dƿTвԆʮļԓӞĶƔƟ҉ѧҭőŞҾ\x8bͳQѲϹ=îąԡӊ˪\x9d',
                            'Ǚũѝš˻ҠʷʤѭŜġƉœʽјŎɴƱƧȆǬȣοс\x8fʌҦZȍ\x9f',
                            'ȊЪӊԙʱͺҏǸʥʼђьȄiΚвҖǀʹȓϠɷǔѡņʵȲɇrƦ',
                            'ШΧѺÕҳŷʲΐЋΆ9ƟƆÀӧϴԏɍȄt·Ӕȱіğ˸Ĳ\x9eɓ8',
                            "ͷǦӁƔԃϬϢίҶКůɳ'ӜʅĪğƤӂҰŚǭӝȽӏӯ˷ɪҿť",
                            'ČԋƲϿʞ˱ӕĒªõƿѕϠ\u0382ų¢\xa0ʑҳфЖ\xa0ԐΗӁμѥ~Ϟ@',
                            ')ɀʡˮnƫԎɨ͵ǹҤώαȹӪɍǋǨ˫з¼ǓbҖԗӦѾҠϊѤ',
                            'ύ\x86ȗ|ő-ύͺȞˁӭʈŜΐννϵžӤŧłҪ`½ĔΓҺџÈϧ',
                        ],
                },
                {
                    'name': "\u0378ӀǍԊȊԁ҂'ϠŜƪY\u038b˱ҩơǶǠoѤǺ\x9eӀÁУӚʭ˥ȑ6",
                    'version': [
                            -8728416400488376875,
                            -8962728576661710227,
                            -8566110337522116011,
                        ],
                    'about': '˼ϮӜæҴұԖǓŋФđŮѶæȂϲVȨ×BϊŝΡȕĕƵҝѝ=м',
                    'description': 'Мѳ҇9Žӛ҅ťėϋҷMȑƹђқ>ΝĺһʙЅϑʖ˓hąàÐǶ',
                    'authors': [
                            'ǀ9Ϳ˺сΑўēĝЙˉȡ¾ȢЄơѥɻƏӾ˃Dş÷ɘЃǁ«ïq',
                            'ȧЋҋĔ!h+ƪΒӊSΦ\x8b˩\x8eԃϴuʝӓˠӜϘǄʳÇΗ½Зϭ',
                            'Ц˷˥ЯӁʾг£ʹѶьϯӭЦΈğʷќēŮCÿΡôӤƻɈцʗҺ',
                            '\u0378ȿɰˠΧѥɀϜӅǮȣ_őǤǳӆæʳʁʭ˵гƣΠВҮ£ͽғ˪',
                            'ʻʵӘˉ3\x89óıƊԪӂϙўơŴѺƀβʊԃԞСɜ¢»ФȰНȌӆ',
                            'ÄoɞѧÔˍӿĆIúҩȎǓȐЙ\\ҳ\x9c˸Ǒ^ѽмξˈԬǯJƝ¥',
                            'ѭÜťžʂ\\\x84\x98ɧ˦ʪˈƃё~ŞвĦΖlϦûӑϷя˽ȸˡÙĖ',
                            'ƻѪ˪ǝɝҥͲǚӇqŇӣȁƝ2ŝĵӵƕӡǤδҖԨȉ˅oƜȕӽ',
                            'щlСǋЅԅĈХ\x9cƒЂûʰƺ˻ƉǳԎОƴʑϚ˘ǾИ˒ɭÐǋő',
                            'ю±˷ƗӸϲί΅в\x87ԖϤԑδҵϴͱ2ǫ\xadБ˰ˑb\u0382¸ƅӋ¬ӌ',
                        ],
                    'licenses': [
                            'Ο/ЋÊǒWыȪИҥC',
                            '˫ŠșμМʻЄ',
                        ],
                },
                {
                    'name': 'ӚſͳõΧʡѹǦȐˤͽħΏʥǮлчУǕʢ˷Ɣˌĝǥ\x98ϡŅđĐ',
                    'version': [
                            -6954929908242575946,
                            -3403095521568766915,
                            -2585150998904078761,
                        ],
                    'about': 'ÊӼťѿJƨǁïʘÅѫĩӲԈȅЉĚŀƺѼөӮħ\x97UĚǻҊƦ\xa0',
                    'description': 'Ӝ+ňʹѵŨçƬΑϣ3ũʜǀёƧʹǿÅ\u038d\x8bʪѤ˒ЄЙΤȶǴƣ',
                    'authors': [
                            'ϼFӆʷʂԊϕˀПҠǩ˶ɵϥȽЗsӦҢǖͻԍ\x82\x96ŐѕÍϸʝД',
                            'úсўδгΒĒԘÔȇɖĩĤҦȗµûģĮэ\x98ӮþăҿȟΖƒвÕ',
                            'ɬϳɝƹӵǒǛ®Ӏ҉ɲ˱kȎІƮӛȉiКªʓÒ',
                            'РʣǶЏѦɧ³Ѯ϶Ӭӱɲӵ|/3ҙҩØΘŇʉвȕÇӑӎ\x9aӳԓ',
                            'б\xadδʇǲΐӟVžϬƒҡħȑȲҍʓŨȥțӔѹ"ӊǫ˩pѴǃ˭',
                            'ĨӨôdƑqȓͷԖŹŧƟѝʁǡ\x8dΖҴьƾҊ\u0381ȔYǶrúйǥ҆',
                            'ƾɱ8ŻԎ§ΛϏž҃ԤǘԉӼ.Σʩ/ƣəѳǇфȥѳƓ²ɢˣÀ',
                            'ӨΧĳΑΰ',
                            'ԆԢԦѹѡ0ҟ6ĮӳӖ%ƘšϏɋĄ\x94чӁϚŻʠƦ|ɭΙÇEQ',
                            'ψԄʅɻЂˁfԌÍƩɊĪ\u0382љҢһƘmӵďӝԢхϿśѫξѠØɾ',
                        ],
                    'licenses': [
                            '˷˸Ίυ\x8eŁӌ˃˴ТҟϔçȢõŲǂ¨mϜȮƒȈόȷuťȻЂË',
                            'ӣ\x97į¼½ξɖƯԝƕΖɢMѡPӵңϷÉǶ҈Ɂʫ˹˵ǹƄƽɪΠ',
                            'ʉ\x9bӋî˽Ά\x90ΖѐʡÛŦЎʐѬɗʧ£ѝÊɃd˴˟ǫȗðïțѢ',
                            'φ@ʝІӼ=źұÀˑʆ\x9bãƦҋǌӳɟ҄λɂȦˀλ˄ΛΠȲnӱ',
                            '{ɟpӳ¶ʅűӌϦUɡƲƺРЕ\x8bԗυВΑҪűĶȂԝŦǤѤΈĽ',
                        ],
                },
                {
                    'name': 'ɘpă·ΫТƧԖŸҢϧЇɿәĬüź9ĽЋɟǔԭȬ\u0381ЩS_\u03a2a',
                    'version': [
                            -5111191243386750115,
                            -6185501043472238233,
                            -6611195362681084275,
                        ],
                    'about': 'AϓɐͰ҅ӶѨÕŏϓǉњ\x89Í\x8aΈѨćʖɏҔЈĦ˫ҽӂĦԛȏȠ',
                    'description': 'bȢ\u0378˵бɑГɛԣћӀΑϴͼaҦƶʱЀÒ\u0382\x8dƱΚƞϔ˾ʓȬɼ',
                    'authors': [
                            'ŝɓĜɦǰˡёϴӗêϡŨʀČƿԨσƶÑуĻͺʿǢЯ%Ϗȶ²\x83',
                            'БɓǜŠЅЄÖѥŏľνʔҍΘΤ˽ƯÅȵƛǇhСǾόӵсʹÄΗ',
                            'РӷBҤcȄæĺȞϪСӎΑťќÔɡÞÍ\x8aѹűđʃéѐøΫЃƌ',
                            'ԃқ˂ǪȀϼѵÍ\x9cƧѺХȅ³\x96ʃʥхǒІȺͰԛәŉӆшťXԬ',
                            'Ȣǜŷï˫âȝҬʷëȎĸҀǧɭѿғǕӞβĵЮ(óıȶѯ?\x8dԭ',
                            'ҦΝɞĀ¸ȩǞϼм˗NәħВԇɕϥčΑнԉͺŏίƳϡǱўЍϿ',
                            '=ǌʼìâȊӞƢǽĸ0ɲʂŤѧЙƝķğ\x86ҝǲéĆąďԄ¯ύє',
                            'ӶčϸɃα҈ɐΈ\u0383ȮȣǎȇβϿѣԆ1ɔ]ˏ˫ѹԭѥ\u0381ȳʖԊğ',
                            'Ǖũ҈б ѯõјȩΐȺŁӥ_ѽĪʗï¸ƂƋʜȟƎŅԡǵeѺΑ',
                            'ŧɿ˕ːˠɂǌǳɥżƬǋӆϊȊƥѯǠǒǬлʝȧɝ¤ʟʅιůl',
                        ],
                    'licenses': [
                            'ƒĝ8Ǳ҃ǵ\x83ǫċϬѳqхҧȤβɒƋԫѹҸӖӛ˛Ďƪĩŷј˲',
                            'ҀΆчΆȥҹȵѮĻΝƐhǡӹ\x99ɠµ´ɜȣĩδρƴʷnĬ',
                            'ӄlɫϤĽΝӚcĎσĚңǭҾæӨȑѶӑϼÝŉΑȨѱŸˀĤȢƊ',
                            'ӡƔęƂːÒŻԭәѥҵωˡϝǪɾø˖Ѽ˷ԇ\x89ӟˢΑ˧јĒŮʧ',
                            'кc\u038bҸoƦΏ\x7fӞЀĎƤʍ˘ӴȒΜҵ˗ѩѢω˃!ωԫҧ˵ҵ˵',
                            'ΪƵЯ#\x9aǨ',
                            '%˭ѧɥЇĄ-эҩҢ¨ɽZÂŃЍЧúXĂԨαԘ˄\x92Ɂ(ӈʬí',
                            '£ƻɡНCӣʷӐǵӗƢɑɏʟӵÔˡӪȯʾĒƋõʇÝɳӷáϔƺ',
                            'ȸϽȶƤʚ\x85ƪȎҞĊίʺǥǠV\x9dȂϭȿЋò¢Ƀч˨Ӷ4ĥϷø',
                        ],
                },
                {
                    'name': 'ͽе˒Ėˤƕä®ŠǻļűҖLŧ҅\x8bӜΑČõϠƠdśˤЎ˓ТϺ',
                    'version': [
                            -2007931791429609057,
                            -7908444395267375325,
                            -2263302883436556683,
                        ],
                    'about': 'ΐǁϱоȦЂ˻ұųљĖʱʳȁß͵ýl7µ҆\x87ѵƬѪ\u0380ǗŚƠˡ',
                    'description': 'ɎȊωŴŌ\xa0˩ԡÈ0ÔвǸιűзѵðԭȯԂȚ³\x8aĐńʄ˷Éҗ',
                    'authors': [
                            'кƻ\x9aƸԨ¤Ԧÿ˓ӡìº˘ΥξӳÓή˃Ҏv˩j͵ӹ҂˚ǰƃ˖',
                            'ɒŇIԑɇjZƯǾΐӴȺɭȳόɌΩɳʧ\u0382ΔɻËχҷΘʾƄѭı',
                            'ŭˇМӊʿғуҹϬñŀ]ó\x82Цʪ˪¸ѤϫƐ˝ͽ=\x95ӏΣßsГ',
                            'қ\u038d˖ǆ˞ǈЋȐƣVȷŪЩҠɖҦυя,GİƟɶȶj9ˮɔǟԡ',
                            'ƔԇȆ.ΝƤ-ŰHВėȵˇǇɏ˛ӹΗɛǿҾ˓ԧыҪ\u0383ӄΐӖ¼',
                            'ӳßɘśȭö˒ŝʢԘ\xa0śǅȹȁ˓ǼȏΟĹљϟϘәèşYʐÏǀ',
                            'ԝϣŏϧоӈʺȲOąŏҊë÷˒bќȀ˞ӓηΔѳQЬȴӓťǢȾ',
                            'ѲɑӠѩοиΛˏɪ\x8bɖƱĲ\x85ЇƙñéΫʅɣԜѽеͻҷšʞñȱ',
                            'ӀĴͽ\x97\x9c\x9fͺŖΣɣ\x94É<ƬŊҪ«ʅέĪ9$ȱÂ˛ʓάʵŜɲ',
                            'ѴώŠŌӪǇɦòЧϼƅԝЖǼ\x9eӬH-ȗZ[ԗf˓ôçʒȈƴӵ',
                        ],
                    'licenses': [
                            'һþǗҹ&|ʰ˽¤ƭġͻУЈʇ\x9dԄ;6ƅУîқԙхԤΝưŋϺ',
                            'Ѿŋ.f',
                            '˜бǑǲҗ\x93ņƝBҝЈӗēǻƚɥȂϊɖĦҢäϔԍɠѽôѰȶΑ',
                            'ÔКҊɀїĹƳ\u0380ȞЏɏӷжȉ¨ʔȠТwʆ˻^ĩPΉќĦɋ\u0383ˇ',
                            'ЊˢΛӝĢÎɭъўϟΛƹɒē>ПΫ\x9eԋѕɛĊσŏÖԑĒɦѡ[',
                            'ƐoǨïŪLҊΠЧѢΣЪϱҖÂ˴өΧ5ʫӑțӲŞ$xɦγΘҔ',
                            'ΉԭĵσӅϑf\x91ǍѬ5ҽЯШŖԤWťřȢɊ˳˽ЊŒǘȩ£ԟм',
                            'àķǛТȃѭ>щʕƵȆҸȸɑҿđǎșƥȆ8ƞԞ2ҪϭѕɮѢӆ',
                        ],
                },
                {
                    'name': 'άϩ˩šϝуǤԩƲʑȺQԁùӠ§șΛʼʿԝiƌ˥ńŴǄѱӨ˕',
                    'version': [
                            -2792421329449228383,
                            -7143996430643114572,
                            -5027712528057809918,
                        ],
                    'about': 'ϗʴЬ?Ǔɫéԓː}ϙζĘ\xad˲ćƧҬȊӏÖӺ·ƕӇĒʟƅΩь',
                    'description': 'zԏˤǽԭVȷƴÛңԃ˅ƽȽƯϡϩ˴Ķ×ɊʯïɒȌӳĐǄϸɯ',
                    'authors': [
                            'ѮŀÂдͱüεЙȾƩӧЀȎ}ɍԎҒʘŪuǰÙúɈ˫ǵ҉-ȹ7',
                            'ƸGӔҫȫɞùӀɍ¤ϯǞÚǅˌ°ŦΞĻɧɃέɰģɻӲȓűΙƊ',
                            'ĖϩѐԌ}˚ȏҰʇƶтӟξљ',
                            'wʟǿӬЭ\x9bųʷƺİȫ҃ˤAҩҞ\x92ӅДĵſϲƞӏѾӺȀ ɶɇ',
                            'ȩÚñτқӣӅËЊғϻƫ˽6˒\x91ѳNȵ=E¤иX\x96ЂȨŇˊѺ',
                            'ǫÎĪȲϊЅĹԍȯЏʈκ\u0381ˬό£²xɲˡèӁåŗÅ˖ʖ\x85ЛΦ',
                            'ɓʄǏEӮГ',
                            'ΨǿоҶ҂Ƌʮƕ7ǹŶUˬϟ\x98\x82Ίӝ˵ŨȂv\xa0@ұƣ\x8bɈљ+',
                            'ŃʄҐˍǛбΊ˛ÎԖʞ+θǥҏtԐ˯љȃ-ǲ´b³ё˳ɒÈԓ',
                            'ҤģѯÔB\xa0ɽþôʍhӇџȒɬȻƗΝеҞĿɲμ^ԪТ\x90Gώ`',
                        ],
                    'licenses': [
                            'ЩͶʈƈÄц\x8e͵ǎїŎƓȟԇâɶȉˀЖҿсțơ˾Я>Гǲʦǯ',
                            'ӐжаǀƼͻųɶkƃӯљˀɑԗʂiʯ˝ҹFďΕǛǑ\u0379Ӂǫŏʁ',
                            'Ȩ8˝ȐţНҋƒЊßR±Ø`ëԈƱ˂Ǔԟæ\x84ΞѳѓϖǼJCҩ',
                            'уǛa;űҷŖǗҟİƃăĹťÑʏŀÉɤɱ_әwɞȫι˛˅ņŷ',
                            'ƢңЎҹҪ=ҭʦé\x9aЅȐӾѭ·\x9cĨφмώ÷ώӯҨÍƆʓɿӗƴ',
                            '\x97ϻҧӝóьЍϷüҡѥΟʖŕx҃ȹȀŭ³ʮƮǷιǒ*ɲўNȊ',
                            'зґɻęʽԘάҜɟVӻӄʝÙÓωмȯǽѪƬіӕѽ(ƃe\x8eȋӦ',
                            'ʣ˞ŵƂʰӑˌǝĚȜӑ˫зǀͷØε;±ˣ"ϪҜКԓƌ\u0381ƙѠԜ',
                            '҆\x91ϳ¹ϢǺϰȋϞѐӋʺ˜Cˍ˗ǟʛŅ"ȩѽƺϔѓʭęņȂñ',
                        ],
                },
                {
                    'name': 'ę˚ГɯӵӍЫЭɃ˷ľŹρ\x98´ЬУӀШΪƭʚάĊ˵ͰЙįŭż',
                    'version': [
                            -6224381375999909591,
                            -8125799470462679868,
                            -4210222161636134543,
                        ],
                    'about': 'ԙɊˋǨĢǽ¬ƘγͶȉɡȔӭђˤĜŒȗз΅ȼĴ¼ͰύϯǃΒɧ',
                    'description': 'ԢȲ˜ɯǼ@Щ\x94ȀԩȹԬʝȓÒ˛Ŕ҄ӼҠĭ˪ɠȖԧ\x9d˰Һɸƒ',
                    'authors': [
                            'ɶť˴ȨǽƵʹ͵ŃRԎȼžʯƥʬʇęԈ\u0383ÐдƚǰψԗɬѳÃѓ',
                            'ȺƈŌÑǜΥŰςɳ˰xISĈЍıɇϋσǣыήËǳņŞϿӺ˵Ǵ',
                            'һȘɞĂμÛβΣӚȶÏǴ\\ϟ¦ɃͰϸ˗ҽѹƚǋЁ\u038d҉˩ϞǋԦ',
                            'ҙɠҚɜңϞòʲˍʹ\x88ľцɬҘ˾±ĵĊƐy-ϓ·\x8cLZĿΤҳ',
                            'ѦǟνАȺһҸʑ',
                            'ȾŃ¨',
                            'ƍͲǡŻӍǵļ\x8cυϓ]Ɨ£ЫǦ˓Äѩȟ;϶\x86ƒɴȄȴɪюΰˀ',
                            'ьнΈUϞӣԓγt\x8cʒŏŶɶԖǻh\u038bӈћÅʕϨԓTµƆêȆҕ',
                            '¹ԗɻĉѳɜŽżƠƙ˗ǉPƊϸЩѴԊŪ×?Ψ҉LϚȭɐŴ#ˎ',
                            'ϪķɍŌɷ|Ȱέͼ\u0383ǻ.ȌĳԢȊȥԌǿƻӪњɽȽнːǖŵҹʌ',
                        ],
                    'licenses': [
                            'öƄʫϛɈɦ\x88ҠѪ˰юˁZ6ǷÛɠĝǎҘǹҤˆˏ#ЊOȺȽà',
                            '½ԋϳϪΟǥĮǯ\x95ǔǾˍȉ˛ԟɀǔλӺφSΘÈѢ<}\x85Қкȧ',
                            '6łˍ°ƒ\u038bΎ§Ѧϓ\x9aāȋˈѧȍȰȀ϶ȑϷόȹƏɷʮƱĿ²˚',
                            'ȫn\x86Ԭ>ĴϽҳº\x89ŮˋºžťӜǟԋŰ',
                            'ĽǠҜЖƶӁĳÓ˟ʛɴ+¶ƅsƘέυâɜЅǡȼԄƟϩ˾ҐΓ\x86',
                            'ЎнЈΊ\u038dιʞlϏk±Ćԝ\x85г˚ǏəʭƥɗѬ¦ЧӞ·ʓǩӏȰ',
                            'ԝƳǁӐÔͼӧώǺrˠŲʐüȂV\x81ĘŶҜϋǠ`ДΠСӜԝϳԒ',
                            'Dǎ˅ˀιōӹƨÖʨŠʮŞʣÎз˚\x92\u0379',
                            'ğʿŨϦбѓîùʕϟ¼ȠːԧԐÒȜʩWѱϔзҙp±нӠϺÁů',
                            "Ʈ˕ƍɧǥó˰ΜϷʨΈɥƄѷƝʾТ\x84ηΪɎʽʂЇƦēȇÒ'Ʒ",
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
                    'name': 'ʼĉԊ',
                    'version': [
                            -9107876560234981516,
                            -878078248690280824,
                            -7880758661875145587,
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
