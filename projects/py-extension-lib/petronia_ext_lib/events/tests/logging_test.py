# GENERATED CODE - DO NOT MODIFY

"""
Tests for the logging module.
Extension petronia.core.protocol.logging, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import logging


class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.MessageArgumentValue.parse_data(test_data)
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
                res = logging.MessageArgumentValue.parse_data(test_data)
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
            '$': 'πqǡŶÜJӡƭIε˖ϷΡ.<ҩƊęӜϪǝ&ʩĞȧQϬωºӬ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 8799669317342449772,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 98821.19750952031,
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
            '$': '20210327:032354.863355:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Уӣφԇ¦ǟĭIԈͱҏԋŽҜď҂[ÂҵɿϘ£ӥȃ_ж0жӺŷ',
                'ѕнɚ΅ʰƄ2ӆE˩ˋђǒė¶lôҭ\\ŰѮ˷ʓ&ɾʎԩ¡ҼǬ',
                'ƺˮǻ\x9c]˛\x84Ѽнϩϟ²ŖҨԞ\x9fжєţȠ˛ǡМŚϯԞ£ЬϞɁ',
                'Ţσ҇ϲ˵ѮϢɉǝϩŭƺ¥dǔʖǹό\x8dѢӢÑҊKǊ˨ĳʿͼͳ',
                'Ɉ\u0380ΠЪϪΣӾ=Ƨ.ԃΟţүȸĦӸϱ˵ͻ˺ϋјŸǩЋҕӕˆһ',
                'Ǳ\u0381ԐƑʘҡϛʉĊ\\\x91µ˧Ĺ˖ΦˏÜȝФџϳ˜ҬȮҦH˫Ѯu',
                "Ȩȵŉ§ԟԟҍɕƂˢQЍȌƗ'ϡɵɏ¯ĒìʝǠь҂ӏ˅εјʹ",
                '\x9ds˩ЃΝɫŨĹЎƱКȊÚĭɡВǨϪƱŵ˞ȨűŌҒʩʒɵ\xadɝ',
                'ӓ˖[ғơҒͼѐΛƱʲӖVϾҔ§ˬОřOԙӨĝӕĜ˖ԔҴӳ\x97',
                '¢¢ȐǅȝΫǈѥĨ˃ϤɣѽcʎĈʐρ®ȍ.эçʦҺΣ\x9fьUԚ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1286581432095379900,
                274083479553630714,
                24619714061830985,
                5864078133019244300,
                -6157699042203617993,
                -4993075955700431461,
                8211924452098887148,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                452788.3613219784,
                -23768.907214256848,
                -39194.93372848587,
                389531.82356060436,
                918405.646242942,
                141186.7205929479,
                748263.6932625106,
                254296.423975036,
                233248.8979200431,
                954705.1807372065,
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
                '20210327:032356.463759:+0000',
                '20210327:032356.478989:+0000',
                '20210327:032356.499678:+0000',
                '20210327:032356.568582:+0000',
                '20210327:032356.592506:+0000',
                '20210327:032356.619236:+0000',
                '20210327:032356.644978:+0000',
                '20210327:032356.666367:+0000',
                '20210327:032356.687186:+0000',
                '20210327:032356.711646:+0000',
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
                res = logging.MessageArgument.parse_data(test_data)
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
                res = logging.MessageArgument.parse_data(test_data)
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
            'name': '4ƞYĉØǴвɇȩɰļӷ\x84Ѭ9®Őӡҫˏʗæb&l',
            'value': {
                '^': 'int',
                '$': -5124183361355105977,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˚',

            'value': {
                '^': 'string_list',
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
                res = logging.LocalizableMessage.parse_data(test_data)
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
                res = logging.LocalizableMessage.parse_data(test_data)
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
            'catalog': '˄ƭȠНĲΝчяΡѲ2ӓȇҨҎӯԣ@ăɽũЧωƿ:ǡ\x9eʪɑҨ',
            'message': 'åɋϣʹ-ƈ4ΏΖţÇ?ϿǓ.ԀӞʌǀȞԪΒÄήʰžц¨Өӑ',
            'arguments': [
                {
                    'name': 'ŢŨƱЮÑ˘ɤ˟ԔɡĎɛiɞψ2āΫԃģťѿ˅®#ϡƃŐɽ\x8a',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:032352.293558:+0000',
                                        '20210327:032352.313498:+0000',
                                        '20210327:032352.334045:+0000',
                                        '20210327:032352.361221:+0000',
                                        '20210327:032352.378410:+0000',
                                        '20210327:032352.394291:+0000',
                                        '20210327:032352.409841:+0000',
                                        '20210327:032352.425359:+0000',
                                        '20210327:032352.440337:+0000',
                                        '20210327:032352.457931:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Ȇ',
                    'value': {
                            '^': 'float',
                            '$': 807200.6680312095,
                        },
                },
                {
                    'name': '˻ʹɩγĳˣ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                    ],
                        },
                },
                {
                    'name': '=ƎӐʠʤUЕƋɀʿǕͷүƚǩӛɷш#,\x8d¾Ԕ¬ϮȇҩКíԕ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:032352.710607:+0000',
                        },
                },
                {
                    'name': 'Ӽ«Ŏ\x86ǅĨ?ɮ\x8bƮљìˡʂļ϶ЛϏȾŒ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        522776.05789575854,
                                        354749.3844919452,
                                        695110.5025116893,
                                        200692.98972385086,
                                        401987.138142333,
                                        843153.0954695746,
                                        710562.1208500447,
                                        460248.11342297064,
                                        348075.3221089863,
                                        349142.04867542395,
                                    ],
                        },
                },
                {
                    'name': 'ǰƘȘź˫ǎʪÅр\xa0',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
                                        False,
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ɵǆUΆӳ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:032353.281109:+0000',
                                        '20210327:032353.298200:+0000',
                                        '20210327:032353.315640:+0000',
                                        '20210327:032353.334130:+0000',
                                        '20210327:032353.356794:+0000',
                                        '20210327:032353.379509:+0000',
                                        '20210327:032353.402201:+0000',
                                        '20210327:032353.421828:+0000',
                                        '20210327:032353.441862:+0000',
                                        '20210327:032353.464344:+0000',
                                    ],
                        },
                },
                {
                    'name': 'đɻˮЍĔҒƌΑˣԏEʧɼ\xadҗȶΑӐƯTńêʚҩz',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        908065.6012825508,
                                        588126.2511771715,
                                        543984.5463749156,
                                        431896.8010102387,
                                        430956.4740499534,
                                        354505.24363991973,
                                        785701.5603062243,
                                        109305.48068308702,
                                        865174.2313566027,
                                        250082.37115806277,
                                    ],
                        },
                },
                {
                    'name': 'ƌԛҞ˲ó¬҂ˮҴзȃѭӻӀЕϟɒѿ\x87ƲʢϽɐϩƻʟĔ\x88æc',
                    'value': {
                            '^': 'string',
                            '$': 'ʎrӋ.ͰБăЏϙ˷ЄÏȝoϿϦĊ˼®ȻɽȵτǵȀ£ӘƱ˥ɿ',
                        },
                },
                {
                    'name': 'Ňҗκ˘ľˢԅʌŮɶɉKˇπ\x84ϵʥǪ\xadæºƂӑȞ\x83˷BŔЋ¦',
                    'value': {
                            '^': 'float',
                            '$': 226298.9354739978,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Зϕ',

            'message': 'Š',

        },
    ),
]


class LogEventTest(unittest.TestCase):
    """
    Tests for LogEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOG_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LogEvent.parse_data(test_data)
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
        for test_name, test_data in LOG_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LogEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOG_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='scope', name='LogEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='messages', name='LogEvent'),
            ),

        ),
    ),

]


LOG_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'scope': 'info',
            'messages': [
                {
                    'catalog': '(\u0383ġƜѸı˧8öʺ\x8dEӑȫƪвΏвlΕˆmʮƴřиǯMҭʊ',
                    'message': 'ŻǑ\x8b÷ĢĶ˜ӮǥɏʌɴʱņƽшŇʶÓTˊϦŐѐˊȂӕϸȓ˴',
                    'arguments': [
                            {
                                        'name': 'ȸ»Ι˺ʍƗƕÕ\x9fҕҙ_ιíҼΔƘťȖ҅\x8e½\x8fԟ\x90ϛ\x8d҅пö',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˋÛЧ˳ҠÓɷӁİÃ!ǃЍΘƘϒұϸƂҳŀ\x89ģǷLЈуҪҥ˱',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8449281213164644596,
                                                                            4650891730603113446,
                                                                            -3502020283673502202,
                                                                            -4212332749350882738,
                                                                            -8433769623990772364,
                                                                            -8727852488925823431,
                                                                            4281418784893460817,
                                                                            -6696420825856290771,
                                                                            1341445778271425686,
                                                                            2026572018201978358,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŴҟùĊǡɗzӃȑȹӌʐćƵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032334.399048:+0000',
                                                                            '20210327:032334.425206:+0000',
                                                                            '20210327:032334.451004:+0000',
                                                                            '20210327:032334.474827:+0000',
                                                                            '20210327:032334.494750:+0000',
                                                                            '20210327:032334.515787:+0000',
                                                                            '20210327:032334.538330:+0000',
                                                                            '20210327:032334.559737:+0000',
                                                                            '20210327:032334.581412:+0000',
                                                                            '20210327:032334.604392:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΆӢēƿȸԪlаȥӯж}ϐʚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'FŕűɏѱĩɐƈÉƓϥЗ РðХ˼ɹР¯ʊϔåД',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҲӚÚz˂ŷ˒ėLô˧ӌĀϱҾӊŔɗӓЂÒŦĲФȷˉ\x8dÚiǭ',
                                                    },
                                    },
                            {
                                        'name': 'ȽʸαҡηÚțǝЃҭɌЕЎҶſʱИ˴ļӇƟȓ҉\x89ήԎϿηñԒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʮķü˾ċ\x9dʮÛҺǜɵêĬż0ʬɑĎҷĢ®nɔǾś',
                    'message': '«˞\x9fɅɓͷ˖ľϩԎǚŀȇɂϹνĠ!\x9eяƋʣ˓ҒщѳƯӐ˺ƍ',
                    'arguments': [
                            {
                                        'name': 'ƐЗƄ1ɧ҈ŧŵͽӌɍƒˣϞȖυȁƛɓųđħ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032335.024098:+0000',
                                                    },
                                    },
                            {
                                        'name': '¬ѿíʟ\x98ТĿ\x80ԤΣӤɜõϲΥǺ˓',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʊΔĶ(˯ѐǟȃĬ˖ǮȚȤΡ\x94ƽͲөӽȁϮȌΙżԓ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΞЄŪːϪʋĩŜŧuВȵǟѼêͺҝˇñ˳ľǾԃȟӛσÆõʇ²',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -69763.6213635818,
                                                                            468697.7706578354,
                                                                            258386.10920421506,
                                                                            502926.920375434,
                                                                            153227.53292504395,
                                                                            944307.9279451197,
                                                                            863955.3538666104,
                                                                            360896.6731148618,
                                                                            890121.7093514993,
                                                                            -77586.15983163906,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x86əƝŧћѽ˶àß§ӇѪѱѣfǍԍӾ УԞѯǢ²Ɲ2˕ŀѥŸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            106060.2272160323,
                                                                            49567.56543041786,
                                                                            879888.6537838762,
                                                                            200792.47535439744,
                                                                            475373.6928836014,
                                                                            223695.07534212532,
                                                                            177671.68256916985,
                                                                            620808.2735474536,
                                                                            397798.40229114325,
                                                                            54667.891615902365,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'łtýȣґīԍŔ*ʺ<Π',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǙЇѶӝĪ\x8bɆ_А\x8dєˤȭɊ§Ѯҝ±ȑ\x88ʍ˸ϨӮˏҪʺŅФŝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҌҘҰˉɶϗŌŦ3Ǘ0ғҘΕȒtȹ×ǚН\u0379%ŀŬmҜȰȡɸË',
                                                                            'ԝќ¿ϒЗʿʱˤ\x91ʡƃÔлғԒНѹҒԝБЄϢIȜĶ҆ѪƝҼŅ',
                                                                            'ͷ³ÍҨÁŸхӪƛɆ˫˺;ΟșįűӹŽЊҺȬχƼԄŤőʝǠЂ',
                                                                            'vӴʲɜʱγќ-5ě¤\x86ӔżԂ®ѾƸϼͺӽ˼<ӴƇ¡ʇӟ˒ʭ',
                                                                            'ŅӼϕοǒрϮέ¯¢҃@Ȧԩ×ƭƞěԄÙԐʭˠƣц·nɔ\x97T',
                                                                            'ǻȰ½ԜG(ȍҁƬ˽ŌΕɊ°ɇӺʯ ˯ШǗӂΙ&ѽ\u0382Ӆå·î',
                                                                            'ÿӔΧɇϖԎдʗȋшƓΐ˒ȤÀӷҹџҼЙβǊȿǞИӮfǮ˒Ȧ',
                                                                            'ªéғԓ2ʔÎĪѤĆȔɘѢӡ¼ʷɰʰí9MơFǜǠҷĀȂȥϐ',
                                                                            'ҍѴPĂӀţЙ˦ ԗȖʔЉԍǫǫԦӸЛҴÔġǘȂȉҸçŎȋѸ',
                                                                            'ϠǇɂȖʹϕv4ъƴќǰDʻɵǌҽɚŒԥжPŪ<Đ¬ǬȄ˻ȵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҩȭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8103164565066390925,
                                                    },
                                    },
                            {
                                        'name': 'wʑԭҗψđ¬Ӧԗ\x94ƚ˷;ÛhÖƍŢ(ǺÊō\x93Ʉ\x9eXō\u0379ęˈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7854797059769232876,
                                                    },
                                    },
                            {
                                        'name': 'ơӽҦƘϣƲϼ\x9dŒʷϦƑћѲĥǍÕΛѥӉėҠԃCύΎʢƕԛҪ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǣԆƬВ8˻мºÆˀлӶƣʼιǹáőԔƀφƆȾîtȧ¾^ŪА',
                                                                            'ЯӁƐкξжōɻҬ˳ťΚѢ҈іƺǔvɲȥЧфĀĪҠµӁƃΊɲ',
                                                                            '(ΧɞƬπoͶºѸ\u038dϥȞъʋԤˍŶǃ˕Тєӄā˘˲˪Ԓɟ<ˍ',
                                                                            'ȯҫʘ3œ\x9eӾˠǀȎȤεʁЧϔ³ЮϯѥŊ\x9dˊɤÁΐǴԋ\x97Îу',
                                                                            'ÛӓƼqԓԠ\x8eΔ\xadɀΦӉфԃƒʹњʨʨĭӀΤ¥7ҭОҋœѝԎ',
                                                                            'ŢɉRè¦ó¶ƣůǎӻӆŁѕԚ˻ˡRʬɷӡдëΎǛ9ЦьЖv',
                                                                            'ǜ³ʖϊĢɐчеĭɡƢȧϙŉҒĔˇӹʏґԟƍȅǎіĐY˱^\x87',
                                                                            '9qқ¿Ӆєˋ΄ӽ\x8dӭņћ&ʾ:ЇûǦȊ˳®ӰƸÿҒηÜɟӆ',
                                                                            'ǹÏфŜгԮ[ϱȩɕȺрӦuǦļ˲Ǻ³¤ĵş˹ ¡ÕˏА\x82Ǽ',
                                                                            '¼ÙϞʽыӛԓzʌͲǲŠĳӔҦ¾˳ƜćӵҾʮӔҠrĴʞ΄śЗ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӶȶȋŸ˾EZʳMлƌШЗʬģƂėŦźџԬʛҀ',
                    'message': '\u038dӐɪˍΌӭɘҧʞʬϘξѥɅҋҎƺǲѓ\x9aŪŐǑÔΗŖǇϨҤP',
                    'arguments': [
                            {
                                        'name': 'Ђ˺ЀУ҉ǱÓʹȂ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ǹ²ƃӉРιͺĳϼ^ıŋӿȃɞғԮЫӓӟǸԮʩ[ÙưϢæ÷ʡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ӪřìʍÉҥķϹƦϊͷǮƾˉǸɌʟґʧȽŻx£\x88мî'ɐǔЊ",
                                                                            'Ƚ\u038dĘʖ0ӋƤ;ϑ˨˞ҿÅΒķҴӏόӀʄiϖ\xad¾»ϗʻȳǸԏ',
                                                                            'ϧȜɤß˝ʺǞҢ˴вӽåӠ³\u0382з˻ũѣǞɽίŖ\x9aюЩĂſëν',
                                                                            'Ԇƪ3łɴƽ`ţȧχҫѮƻŮӻȑЗӨƇ^ěФÒȣ\x9fԋǘɋǨҜ',
                                                                            'ɱǔʭ\x8cƁŋΎ`˕Ԍßˆ¾ȃϤbĖθӾ˟ȕÝƘåΙԦҥӖІÎ',
                                                                            'ţýЧӨҧĉҬǒčӼɻǞƣǮʧө%eϪӇɽƒ¢ԛКԀҪӝψñ',
                                                                            '˝\x8cʉ˩ěϘAɾǱПIЕό҃ԅŸԃʀӨΏϻДӯǩˬЄˎϔɫ\x88',
                                                                            'ã˽Ŗ˾ÅӘНяИƐͱʼȂТŋeϨ0ˋʯiřпΉҺɺĽǱϿψ',
                                                                            'ėĤˁk҉γǌѦԓÿŒѧ˶ɾҦҁ˲ҊÀɚԊɵɼźӌVпǺҽǟ',
                                                                            'ØΈΞYùϻ/Ɂ˚@ºʃ÷Ԏ¢;Ԇν\x99ɤ-ѽČzìɍˋӹЅы',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȸoӑΪ\u03a2ǂÙɱ<ȷ¡ԄÿɘΝŪǛΉ˹`ʫȡӴϗΨİѿ\x9aƉҹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -9146888606666510189,
                                                    },
                                    },
                            {
                                        'name': 'ÿμőƉӝɑ½ūӟ$ÛѻСʾƥʑƺт˥¬\x91ĺӹЪ˒ːӇßϑӭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ä',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԪÐ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032338.585367:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҁԪ/ƪԋýԪȱ÷hӺŧԑ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            460893.8568202723,
                                                                            864966.7725735093,
                                                                            625261.7500436278,
                                                                            3789.740488571697,
                                                                            181127.92462061316,
                                                                            431207.8871968286,
                                                                            787830.6030164129,
                                                                            2809.9685342155863,
                                                                            339182.605517321,
                                                                            672814.2010002604,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѻʹŒˡ˟ʩɱѠϏˑйʎbșȌÙѳѭƲЇʺɆ§jƂБϮ²yé',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЈƯʮ×ϪΗѥˏȷȔȂПǲҬ-σġʽíͰӟԪʁ;ǸζҞҹ\u0382ԛ',
                                                    },
                                    },
                            {
                                        'name': 'ƙuǊаˢЉцĳόǲԆӕĒЕӜłLźĒѮɹȵǃԭśѦԅƓʐΏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 992971.602154922,
                                                    },
                                    },
                            {
                                        'name': 'ǔҳӉɒ©ǀɏ˸ŖǴԬʨǑҔƧưƎğёģȷ¯πǟͳŜ¾ʕЀǃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            118200.30384741345,
                                                                            401529.30912413995,
                                                                            462427.0916696795,
                                                                            -72478.64193652224,
                                                                            342986.96580526105,
                                                                            624106.746119434,
                                                                            -34975.17691747981,
                                                                            70123.67302525236,
                                                                            502384.479954137,
                                                                            -39026.49003026212,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '҄˜ŲΣȣÄâèɔƕKʑFԝѣѧФɁºǾȼȉȷȶˉɻĆƍzƗ',
                    'message': 'ÄʜȥȌɚőN*ȷϏ¥˴ĒǧȺΉȤȚʗͿƍÍͳɝ˥ċSlηѵ',
                    'arguments': [
                            {
                                        'name': 'ǚАʰŜҼxͷîØλǬęӮКɋ;ʒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032339.421269:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Æ\\1QέξЊËѪΚȯʚ˃ȵϹщӤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӷDķɻА~ĄÞģ]ӑηǧ\x8aɓʮć˭ǽ\x96eĔǎ˺çǎÐƔƪԎ',
                                                    },
                                    },
                            {
                                        'name': 'јŐpΊѼб\x84ʃŶ˱ǃѺѝƑ˕ė#¤VZǊÀVɁɅŌʴЦД4',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'xЯů˧\x9cӃǜϤƄëǇΚǋѨĄϱчŚʨƈѵѫûЎŤϱȁϡӔƑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԋĴ҆ӺYϺϻĨѴȞθ}Ȥʧΐ\x9bCιѦ!łβȵ3ĉwъ˺Ş\x86',
                                                                            'ӴԅǬҪȮҒǹĕĢǦɊ\x81Ҡ5ΓԌӖϭ`ǤǴ:ĝҊϱҞщǂįǙ',
                                                                            'ȷϧѴ\x81ʽӘ˅ϩƘˤ2ԫ|ʴŤĿȭ҄Ǖ\x9aƘƏƂɾͺĘjԛεӞ',
                                                                            'aƂÄҌȡüԕǫҢӡҿ\xa0ў$ĻǪ¢ÿú\x94Ďɜ\u03a2ʪ\\ϏϬӾÛ<',
                                                                            'ԣьύΠɆӮ5ʧDŵɛǮ\x89ƞΊġôoИ\u038dϺӪǄϏ˵ǶșĪǢϤ',
                                                                            'ҩΧ@ȩҡԘ\x8eĚØЗƟԏ@ҞȲʂƒuǯ\x98ˏК!ȡмПÄѨʔӓ',
                                                                            'ͲƯȥЀ;Ā/ĺ\x86дДưǹɰΌӵҪ\x8dӤ¹ҝʾҷзҔϟɅЅґɪ',
                                                                            'ŊͶÈӮźɋșV\u0383ΔèңԂǤǧЍƝ=ɽ^swʎ!ƥѳб\x8eȸд',
                                                                            'XoҞǔцȳʙӲ~ϵІͷҸƃЊСĵɉҹ҉ƊϘ+ǽóюɂ{Ŗѹ',
                                                                            'ωҪƇÖŒϹÂʹӛ\x95ʻԞѕԝƾθήӜ҈ʲΥɔХŊƕΆˊřűĢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӮïӢÝӼȽ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 843371.7683522108,
                                                    },
                                    },
                            {
                                        'name': '҉Ğģψʴϥɕԍ˧Ğ҆φϣƼμÞȱхѼѰÊ\xa0ӫšǊ҃љ¡ĝˢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7956759876613191425,
                                                                            2681274294655920280,
                                                                            1568193025065859682,
                                                                            -6277756156624434496,
                                                                            4680623741084592814,
                                                                            6156390254181083074,
                                                                            3993603107103389750,
                                                                            2626595268984746021,
                                                                            -4945266138831684223,
                                                                            8356235096186983129,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҙļϮ\u038bĺ\x8eÕХӫή§сΙɘ˰',
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
                                        'name': 'ηв±ĩO',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϋȉΓµӁư\xadŀХӾ˷ϚÖ˄Đ8ɖǹĝìǯ\x9fҪôɀ³˳ɧȶǅ',
                                                                            'ԧ¡ǷΎіŌɇƠĚΫO϶ðϙӅћˠŒʏ·ΏEȮĐәǾˀēѫD',
                                                                            'ɵʟŵƶßƳέĢǴЪȇ;`ӾәƞҐѵÀǯśҦ»ҢǍǛѠđšж',
                                                                            'Ѥϰɋήѵ9҂Ÿɍđ¥ȠűĤЫέԠǝǐƌΕĦnəășČNӰǚ',
                                                                            'іΰΞËΒĦńɲ9ʘîɫҬŀѴ˫ȁǅĆ:ˣĢļҖǫͱњȋÊȯ',
                                                                            'Πԑʠ>Û\x9bѷªͲҏ\x8fԏ\u03a2ѱТɞ˹âѡ˯ʫЮǨҟҢƩѴϖӻӾ',
                                                                            '҇ĕ\x8bҜČʟNԊӸҘƵϱӱ˥ӚѤƐƦǈǰʶ\x83ѽĜcʄɁԃîɫ',
                                                                            'оԉЖϽѨʵʬмªƸљџŏ)ԪӳΔǽˇaɤ«\x95Ύjγ@Ǎϫҟ',
                                                                            'οэƱǤѺ+ȃ\xadÊƢ"ʙŢ:\x89·Ѷҏ±ÈŶǀԎıѳìӭƦýѱ',
                                                                            'ӚġʀƥĢ˔©ЙÈɹͿiӊɈƽˮ¥ɷ{Ǐϒ\x81ԏŭĵ\x8eϠòΑӁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8f\x87Хʣr¡ÑŦӲϨʲțҡԐɡʮσȝЯŮǞјӮ\x9d\x8f˹ʑК˛ϰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ΘνάѮvýǜƮʯɇӱΝЂļΦӧº/ħҒZ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӷϤȱʆќ+ʜÞƉϫ\x82ŴȽƀӷЬЃ˸Ҩя\u038bǚ~ąҊ&ԞԤɢȓ',
                    'message': "'ƆƎԒƇѺҹӴԜˑУԈŠǽɐĿӬ9\x95ӛɅɩːϠξÞʇκ¸·",
                    'arguments': [
                            {
                                        'name': 'җΚȏJʠƔԐªʔʛŢН¯¿øһӋǚхe(Ҩ˺ǭƛŧˊ˯ЇX',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032341.120838:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϛВ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4814098729603970969,
                                                                            8312691373428223100,
                                                                            -7620547952754642138,
                                                                            -111419470918938887,
                                                                            1385835547454954033,
                                                                            -4060820576489726404,
                                                                            7253531447229986956,
                                                                            -4095678687642782841,
                                                                            -987590389574680840,
                                                                            -3924471681411767412,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЌƁƬӎ´ԙƒǲϊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032341.429054:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǮвäҕľμЅɘōʡВāԈ÷yǹœΔěʖņѨŴϋłİɌϨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -475663652784135866,
                                                                            741180267062251342,
                                                                            -7566575267192916779,
                                                                            -5325570581995513596,
                                                                            6791910797417074954,
                                                                            264049825481776533,
                                                                            1060084999541828507,
                                                                            -6242376502604621863,
                                                                            6817471375815742704,
                                                                            -6597025019459571056,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'әӶʵeүRȵ¿Ҧɸ\u0379ąIӛ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5627239013251207553,
                                                    },
                                    },
                            {
                                        'name': 'ɉϛȧҩΐӇҌǀοʠ˳άΌӣɦɑĚЊʴdȿдԊҚӼǠƩ6',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'υҌċҴҒҏŚ§ϐčԌӯŻȯӀӕϱϻϵЮѹÒ²Φɇ?řÒΖҞ',
                                                                            ',bӥÂҶѷǊʧĹDÒΡĘʳɩԁϣ˂eί˜ȏχϱмӱɵ\x96ԀĶ',
                                                                            'њɨǮķɧȖ˔ю¼Ӈ\x98ũӟƔϻŬƀǎƴһˍfƿȺɊάņ\x80Ѭі',
                                                                            'ÄƱťǤÀ\x8bʠι¼ΡўΚɟͶŭӓгǮдϞƖȨ\x90ҧŻҙMυȉС',
                                                                            'ДȤԌªƂȝǡɎǬʋǾԭƩȌĳӁҷӧȴȤʐҧɂōʍʓʇǸωɲ',
                                                                            'ƈЪȗˠϵYɪʴҁ+ӷżѢϹŊƋm\x87ωëʜɓưþe©ȷѥ\x81Τ',
                                                                            'ӷҋԂȤ¾φʝʔ1ąȣЎÃɪħԂǢϭɦĩҞƍτʍͺιҘгĥʪ',
                                                                            'θӿƅȕɗˣɩȜȽÍQğ<ʬʻŋŭ/ŋηƝĩϾțPɟƊɃƱȰ',
                                                                            'Ӊ\u0381\x98œÖҟ$ȤY\x96γԄԄĈӗŴϒ˃ЮѱÜȎӺƍŃĶɛȿµY',
                                                                            'ÍǙɢЛŦʥTʼȇƳҥХӂīˑͶΈjƤυ\x90ȋдЩВ4Оϴ|ŭ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҟԖӨЁŀæ0ǭʟˡ˖ӌπʳϷМĝ\xa0ÒǙȮӧŪқǘΪΚòű˄',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1049105873670275997,
                                                                            3458372222007704697,
                                                                            1705010034057892919,
                                                                            -5175633134432195327,
                                                                            5865429793190172703,
                                                                            -7264896079730453688,
                                                                            1205076046490737970,
                                                                            4963175173661066513,
                                                                            -7809135076116324899,
                                                                            -3895133284422515787,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԇ\xa0υą¢ÁϧӅ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʩҋϟɄ˛ϽҒăƝȧιơϘşҿρȯԍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032342.387167:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѯԏù¼ʦȥɔwɗŭȃXȼ˓{ӻβҩѥĶӣȻľһƬƖҰΧˣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8784835717987033492,
                                                                            196383689021185846,
                                                                            3439678520734655073,
                                                                            6080241519528247193,
                                                                            -6797940334375429424,
                                                                            4473772779715343109,
                                                                            -9122996410160281076,
                                                                            3882863561211670274,
                                                                            -2072966505559600178,
                                                                            -6293240497648432178,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '{ӤʨҐϭӮƝǽό\u0380ėɔÕ\u0381ǰțwbʹ˗ӯсŖĔ!Ж\x9fԑéſ',
                    'message': "ĪYӠɻωȠЙ'ɢʃÚӎüўςӨЫӟɌȿϭǗÞǜŞƕ\x8bʶHх",
                    'arguments': [
                            {
                                        'name': '˘ƂǼē˃[ƂÞҚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7702309373971980892,
                                                    },
                                    },
                            {
                                        'name': '\x8b',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˭ȣˊʿϙӿóԃϸˈвԁͷηϗĉүҿ˗ȦČ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8094887107574457623,
                                                                            -2679030310222918922,
                                                                            8632300978800790948,
                                                                            -1147285972633394547,
                                                                            -7710649188087323921,
                                                                            5551431801555597475,
                                                                            -2010622804964209565,
                                                                            -1885888207268511113,
                                                                            -2626949422429996936,
                                                                            6781640575360767176,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'àpҢĠºέȓβʎɱȬѨϱȜƹȥƈʢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ºҾʀȁąΗʷφѸΫӬɔҙʁӔɽѺ\x85ºǫºı',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'νƫýː§ԥΔɬр˱\x89ǚ\x90ŊȍϾŅɋʑͼɲɖΈƞǄɱǱоѿʦ',
                                                                            'Đƀ¨Ѣʾ(\u0382ćҟΑ«ĥȩËʝTƟĽϘԎ%Ҫ¤áðϕAÜ§ȣ',
                                                                            'ϕͿǐчŜǵÔȼ\x82ΊәЗºÛnйǠЃ´ӊǛʶʖİϟҳӉĩʎϝ',
                                                                            'ԝɦúżɦɭʍ-ĽѹīӂϜȕΊáÖϘԣΤƕTēˁčÅԀѾʛŅ',
                                                                            'ˁż}ӏӲ\x8dŮҮϼǬƤʧ\x83ÈЗvǈyʨÐΞɔHÄ<żҵƚǸʾ',
                                                                            'ƥˈÊ˭ҼğƠϕµȁª˙ĨҨΰеųYӬюі¶ėȨǽnҎƶˍҗ',
                                                                            "ҫĂƽ˟ŐАѕЭʋԑǝŦҚˉЪϜűŝĵʶВŬ'Ī\x85e҂ɋϒÆ",
                                                                            'ӱCµĀʇɑɐ\x96єԃơĜƢ/ɬΓƜʂҎ˳ƇİԊ±Ѵωɟѳȕȝ',
                                                                            "ǭ˵ӺƻʘŴĖę1ҧ\x8bǝǠыʬɂļĈǮͽϲf\x8bԕ'ƩϵЭUÙ",
                                                                            '\x96Z˦ϥĶЊΌɝϴӔ:ÞћƄǱõҵӄ\u0381ɌùЎʽ҄ϘЄ˃5ƼΆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϧη˄ƞͼ4ή˹ɄƑЂҲɒåʠͺįǃ±ʭȬïȯԮÒ\x99ɀҦήƸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3387693724575215301,
                                                    },
                                    },
                            {
                                        'name': '½ӷӶʓ˳ǽΘʭҹΜ\x92ԆҹԈЯ˅ǔ{ШsӦƷ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӎ͵˕ɮÈϼǡʻ˳Ƭãӹңőĝ}ИԃcƌīľêÖȆnıï˟Ώ',
                                                                            'ˈɭʸȀʠɧʝūҖƊ}ƩσгешȂ¨ŨȓǦӼ˔ĻBƄĺîыƳ',
                                                                            'Ŵ҅ΥԚµҧ˵ˡкÆĿπ§ЍǖÌ\u03a2ҢҪpŉôŎɥǹ\u0381РŘїЋ',
                                                                            'ɵƚ¥ҟʸɋǬćϺćʥͳhΣ˗Ӄ\u03a2ʻŎćɝŏ͵ѲĹ҅ʠɽ6Θ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ș˕I҈ӫnӄѠʺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ÈΪƗÖʲûȷͲІßǧʑ˺ЄҦ×sƗ³ӈъҦ҈ʖƻҷѓѳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                    },
                            {
                                        'name': 'ѡĬåҼƆ\x88Ҧ)ȎȶрҝάƷʖӰГϖɖкɑǵԍʚӕʪȮπΉѦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            538682.6085838407,
                                                                            74863.08077321257,
                                                                            -33940.42066087754,
                                                                            714979.4108120558,
                                                                            985574.0262438708,
                                                                            524983.1938499192,
                                                                            639249.5006442814,
                                                                            645669.6042744712,
                                                                            844204.7764214134,
                                                                            545723.8070462159,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɹƶ\x97ȸŌЎƥџыϧЀҨh¦ԑtƽңҎ\x95х,ͷПƤѻ҃ȼέÜ',
                    'message': 'þ!ͱŨȔ½ǧιӍÃӶʥԂɡɼƨÇўѯŉǭȧ˸\x93τÐЌŀѱι',
                    'arguments': [
                            {
                                        'name': 'ǣʞϕʡʂѸӭ\x83',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\u0379´ƻ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ұvǁѽʒ˜ˋƅͳԟťŽ\x96ȗ˱ķ"Ƶȴ¹',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 659373.0756146979,
                                                    },
                                    },
                            {
                                        'name': 'ϡ\x95Έ\x81ȆʴãɯƦ˹Čɔ\x8dĕůΡȑ4ŜгӅÁĘҴͲƪŝ!Ӹͻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 587223.3977098584,
                                                    },
                                    },
                            {
                                        'name': 'ǈŎґ˷ʻҳӰѣДǋɽ˒ѺIƬáϣ˕OϠћƓƠ˗\x80\x9eƸ8рǌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8130938428195251410,
                                                                            2551356661624021407,
                                                                            5968664372658924903,
                                                                            -5068826167144656510,
                                                                            -5813212863914040056,
                                                                            7370685557891114117,
                                                                            -6594602188772322959,
                                                                            7535845281754009132,
                                                                            -7637748204085201827,
                                                                            7815435158320996070,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΫĐ]ÔҮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032345.077360:+0000',
                                                                            '20210327:032345.095245:+0000',
                                                                            '20210327:032345.112361:+0000',
                                                                            '20210327:032345.129426:+0000',
                                                                            '20210327:032345.146677:+0000',
                                                                            '20210327:032345.165104:+0000',
                                                                            '20210327:032345.182112:+0000',
                                                                            '20210327:032345.200787:+0000',
                                                                            '20210327:032345.217873:+0000',
                                                                            '20210327:032345.235349:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '»ˢӁɩΤ˓ҐǒŅȐ˨ĬKь˅hѴʞΐŘįʂ\x87ʦȆ\\ϗǥМȑ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            860692270857797002,
                                                                            -3224919089070232263,
                                                                            6225443183414691291,
                                                                            -9084551776172181657,
                                                                            -8957750346063689765,
                                                                            -1122662897764613199,
                                                                            4856856108334850970,
                                                                            -6662993717702981967,
                                                                            -1327625196843138307,
                                                                            -1854581908499652889,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǷˌΐŇ˄ʥ\x87ЍɠoѪȑǋCŨ&Ƥ¨',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                            {
                                        'name': "ǈЛ'ϷʆǜМҘʼ\x9bќ!Ӛ˽ˏ˷\x9dğɧħȟӪʨЊ1ȓ˥΅4ɢ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032346.538510:+0000',
                                                                            '20210327:032346.558683:+0000',
                                                                            '20210327:032346.650117:+0000',
                                                                            '20210327:032346.908629:+0000',
                                                                            '20210327:032346.930359:+0000',
                                                                            '20210327:032346.958511:+0000',
                                                                            '20210327:032346.978788:+0000',
                                                                            '20210327:032347.008711:+0000',
                                                                            '20210327:032347.031608:+0000',
                                                                            '20210327:032347.054000:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˥˳ŢτJͰǰʓ¢φ¦ѼéșҞӰɦӐǧͱȋ\x8cȟɫǅĝёΥӤˆ',
                    'message': 'ЮҴ˧Ѹҩ#ŐΛVŜΖўӜ˕OĝQͽ˄ôÞμ˽$Ѹӷеʜ.ǥ',
                    'arguments': [
                            {
                                        'name': 'Ƨϵ˄ϗȚǺжɨźͷԋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 305930.1095060376,
                                                    },
                                    },
                            {
                                        'name': 'әγâ\x95Ϝ˟ǳŵǩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¨ʇϾǊƦϣȡʞɐʹӎ¾жѰȥйɷȷgÈΛВɒ\x82ĔОʹƌӴǑ',
                                                    },
                                    },
                            {
                                        'name': 'ȩÞЀΟ΄ǿǚBБϰӁҪƄ˯ƿӍŠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032347.436806:+0000',
                                                                            '20210327:032347.461907:+0000',
                                                                            '20210327:032347.492371:+0000',
                                                                            '20210327:032347.639173:+0000',
                                                                            '20210327:032347.657506:+0000',
                                                                            '20210327:032347.679641:+0000',
                                                                            '20210327:032347.700720:+0000',
                                                                            '20210327:032347.720163:+0000',
                                                                            '20210327:032347.741603:+0000',
                                                                            '20210327:032347.763930:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'СѤΦɋƩŢĿǗюīЖвҳʫñW_đҼΞќʼǯˮťˈÇЩє0',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3445629319988326500,
                                                    },
                                    },
                            {
                                        'name': 'ɋʅΌƥӖȩƮŨńqζĞŅҎȲΨwˤȜáÛњ\x86*ưВ©',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ѹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            6354.409440320203,
                                                                            821574.5889512701,
                                                                            268228.15499106667,
                                                                            807913.8519051239,
                                                                            991213.9196222858,
                                                                            450232.9502311329,
                                                                            302946.8430701826,
                                                                            708185.2682035053,
                                                                            557274.7891095415,
                                                                            -95290.00554902444,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԫ˺ɋӓʍȋΖӭҶŒgfīаíƛĿȧϒԏӊʁɮíҦҕпϘχϒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'цӣͻįϤПͰ\x9bnϫɟе2ǤÃӺȱΘϨ¨хͽ\x82Ђí÷˵ǆȎž',
                                                    },
                                    },
                            {
                                        'name': '·ĽҞɤǁϕϞĘȢ\x87',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1607714812871060740,
                                                                            2729663012704342937,
                                                                            5079681578732955101,
                                                                            -9037969326127491804,
                                                                            4592754521103057228,
                                                                            1804323134685815670,
                                                                            -551950406375406677,
                                                                            2006042131680738176,
                                                                            7024061121318423473,
                                                                            6888811624002422055,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'рīŷ˚ÌFӈȁËϷҘîɔĭȮҦȇĐɈ҅˕',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032348.604086:+0000',
                                                                            '20210327:032348.626890:+0000',
                                                                            '20210327:032348.653419:+0000',
                                                                            '20210327:032348.673608:+0000',
                                                                            '20210327:032348.692601:+0000',
                                                                            '20210327:032348.712029:+0000',
                                                                            '20210327:032348.730620:+0000',
                                                                            '20210327:032348.749805:+0000',
                                                                            '20210327:032348.768281:+0000',
                                                                            '20210327:032348.786957:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '5ĻΏɌ}ÔÚˁ\u038dΏѩϖŪΓϰÎѾь',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2013355197616354962,
                                                                            -211325329810591518,
                                                                            1669808191457440702,
                                                                            -9005549298439526393,
                                                                            1591074363318443445,
                                                                            -2635333870913381026,
                                                                            -7503175110627206446,
                                                                            -4773966256094167391,
                                                                            -5853159169900128038,
                                                                            -8019893627969417801,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '{т ХVϡȈϓҢЫ˝Δʥϱ˙όŹĄɝÜ˃ύęȾӈ\u0383΄jͶŵ',
                    'message': 'ȹʐ϶ҙdҕŵɭŞыˋƝώšЀ\x9eäӀƟǐȌΘҋтУǑʽãқɞ',
                    'arguments': [
                            {
                                        'name': 'ɵĸ®ԍͲù\x85ʤЏѶƔ˭ĕΝ҃ʤ˽ɌǏԕŞƶюЭǱˡÜ\x85MҌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2768658236806179872,
                                                    },
                                    },
                            {
                                        'name': 'Ѯ˷ɨȕϙĮυӽı˧ΪЀ\u03a2άɿnĉǂàӕҦ҉҄ȥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1624943440040333340,
                                                    },
                                    },
                            {
                                        'name': '¶δçȯʣӷŮȲҒđˋïǫ˧ŊƁǔ·ýįǸ«ŏRʑȼоȇП',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'dϊÌˤʏȬȇ˳ŹУуϢҡƦǂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 769968.3282906653,
                                                    },
                                    },
                            {
                                        'name': '˰ÔѦƹ¼ғѵOÎАʺ҄Иͳӳōĉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 331055.91656595597,
                                                    },
                                    },
                            {
                                        'name': 'Ϧuұâĕƞ˾ύċǭoҶɼ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -348445004369089699,
                                                    },
                                    },
                            {
                                        'name': 'ß:ɖʄҠ΄ͽʌ\xa0ƫɁǮσȼ¡´ĽѢϻ˳ǰЄγӓԍʣʈKÅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032349.841069:+0000',
                                                    },
                                    },
                            {
                                        'name': 'эΤŞVԤ ϔΆȎ˷ɜʀψɲ϶Ϭ\xa0ţČÙӍ˄ɛɋҫɚΰ҉ͻ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϳʅϮӳńԚDǩћΛӓсċҕнσӕǓɟҴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032349.978087:+0000',
                                                                            '20210327:032349.996676:+0000',
                                                                            '20210327:032350.014121:+0000',
                                                                            '20210327:032350.032545:+0000',
                                                                            '20210327:032350.049972:+0000',
                                                                            '20210327:032350.066944:+0000',
                                                                            '20210327:032350.085991:+0000',
                                                                            '20210327:032350.106881:+0000',
                                                                            '20210327:032350.126299:+0000',
                                                                            '20210327:032350.146993:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӾѡϡӌíþǘЍ0ˬӸл^pцӶȶľãʞϣӘˀĊ_ˈÖӕԢ҄',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 965612.9038495976,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѵkƟØԐΞԠˮ˦ȼԥԢϿѻǝЗʇǙɐћѱ:ӣɵĎŻāǋё>',
                    'message': 'ǖĦԈɺ˰ҽɫюĉʾĕҊѢɞÃҳWυȖ˭ɰӥʎѮӏƿʐθďͺ',
                    'arguments': [
                            {
                                        'name': 'ǁΒӦԂɍɐĦɶˣ×ÙkȲƨϊαǰəɊĺӴϲԌԛ3ӝѝқº',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032350.400327:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЦԪŋ(įÈСȎʋȿš',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            243213.95543301507,
                                                                            576713.6196711075,
                                                                            42045.2948826105,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӓӕȅԩ  ҮÆ˴ΠуùƪϸˌãǌЬTƍξȓɋ++ѤưҥƜǆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -71560.0214520879,
                                                                            364128.8351670775,
                                                                            40072.12972332566,
                                                                            634386.8746517965,
                                                                            938647.9107294942,
                                                                            164574.0110810222,
                                                                            277867.03272049455,
                                                                            714870.542825504,
                                                                            669623.7752163835,
                                                                            -67438.50990332219,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƆVѮŶŴϞƍΈĜȻȳњҫɗӵʊЯŕ\x7fŵŌΒ$Ӏ+įǍԂ҂Ѫ',
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
                                        'name': '҇ěsnѓɴ1\xa0cɷɃWŅ¦ʽԋÇĹԅŀ¯',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʕΌЪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɔӞӘеҍаǪȭƶȘƀȘΡоʎρӸʬsŨνƷ÷%ԫű»ɞӀӨ',
                                                    },
                                    },
                            {
                                        'name': 'Ԍǌ\x92ȗ£ʠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'οёьϫʝȮΡƌԂǿδϝħȁӱ˚˲ĬʅΕǤΡĜʌӐ\x96г°Δ\u0378',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032351.540483:+0000',
                                                    },
                                    },
                            {
                                        'name': '×\u0382ӼƜҶύpÆӨŜˡҍdŇԙΓƉВԝƦ$Ԣ=ӕ͵Ȭd6ȉ ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˈӞЩΊʧŕ4Βiҡ\x96ӳ\x91ōѡӗůӥǦʹϑ҃Ø\x8dÓŤεѴȪǜ',
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
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'scope': 'debug',

            'messages': [
                {
                    'catalog': 'βΌ',
                    'message': 'ö',
                },
            ],

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
                res = logging.Error.parse_data(test_data)
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
                res = logging.Error.parse_data(test_data)
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
            'identifier': 'ä҇ԎϜèİδh)ЉђǨćǕŢέ˟ξĻɣ\x85ͳʴ¤өǪӔʌԩЄ',
            'categories': [
                'internal',
                'internal',
                'os',
                'internal',
                'file',
                'file',
                'file',
                'os',
                'network',
                'file',
            ],
            'source': 'ѩƾңɝǬͻ\x9b˧\u0379Юǟ°Αӊ\x85ɧіś$\x91ƧӖɅʘϩΧԡԀҋȆ',
            'messages': [
                {
                    'catalog': 'ғͱʠϦӄϯϞӵқòʘɜʠ-ŊƲŉԓȤÈZɺ҉ǾǕɾɶĒΒɓ',
                    'message': '\x9e²Ɇtχǰǝʁċ4ȣО{-¼wŏЌħɛѯЗɞźƲNŠɮɺʧ',
                    'arguments': [
                            {
                                        'name': 'ŖӯĲӥ˫(Ɨу\x85вǘͿȺu\\Ğ×˜ǩА',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032405.954953:+0000',
                                                                            '20210327:032405.971299:+0000',
                                                                            '20210327:032405.985960:+0000',
                                                                            '20210327:032406.000876:+0000',
                                                                            '20210327:032406.019093:+0000',
                                                                            '20210327:032406.040940:+0000',
                                                                            '20210327:032406.062325:+0000',
                                                                            '20210327:032406.092906:+0000',
                                                                            '20210327:032406.113501:+0000',
                                                                            '20210327:032406.133057:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˬəȅˬʭñş˯Ʋ\x80ёǁӄҴ\x8aȩӾrČˊϬџƮѩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 888246.8422098215,
                                                    },
                                    },
                            {
                                        'name': 'ǀҌκɼӿȝΡӺζɦÇԢċɦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032406.328055:+0000',
                                                                            '20210327:032406.351520:+0000',
                                                                            '20210327:032406.372257:+0000',
                                                                            '20210327:032406.391420:+0000',
                                                                            '20210327:032406.411466:+0000',
                                                                            '20210327:032406.918272:+0000',
                                                                            '20210327:032406.943731:+0000',
                                                                            '20210327:032406.966306:+0000',
                                                                            '20210327:032406.993118:+0000',
                                                                            '20210327:032407.011624:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȁЂϨЇ±êћѫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϟ҅ϬǯӥИĲòфȢĵŞӐϡ˭аХԞџӹμƅȧƱ\xadĳɲȝƌӕ',
                                                    },
                                    },
                            {
                                        'name': 'ˎʍɫØǕӫ\x9fǞÞȊТƥ_\x85ǒҬȏǾ\x8e˾ηƐ˥ȯ҇χʀʡΩ\x9d',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032407.139717:+0000',
                                                    },
                                    },
                            {
                                        'name': 'єGӢҿлΏЉ\u0380Κͼ©Ó˸ԮНцȦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032407.195317:+0000',
                                                    },
                                    },
                            {
                                        'name': '¶ÿǜbǾġЯυȋ˻ҳȽƼɚśͲoеͻȣǚ£ŻͽСɔɋ\x85˴ʫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            84514.78006035724,
                                                                            -47000.37458954337,
                                                                            555025.1259725227,
                                                                            97751.2187038968,
                                                                            663823.4961010531,
                                                                            439827.7093408827,
                                                                            454680.4226860757,
                                                                            601276.7374338396,
                                                                            240423.19233238534,
                                                                            327305.21220637613,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʆƁ\x87ӷ¾ʨŨ4Ј˼ÍƝέȊԆÅԮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032407.606730:+0000',
                                                                            '20210327:032407.627831:+0000',
                                                                            '20210327:032407.649982:+0000',
                                                                            '20210327:032407.670918:+0000',
                                                                            '20210327:032407.690794:+0000',
                                                                            '20210327:032407.710123:+0000',
                                                                            '20210327:032407.730313:+0000',
                                                                            '20210327:032407.749089:+0000',
                                                                            '20210327:032407.768060:+0000',
                                                                            '20210327:032407.787198:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӜʑʹΡʳЬŀҒǹʤҽЎЋΰŉʎҗќѲ˯ŰƞƤɫҬ\x8dŚýėǨ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˖ÖΜÅӮĞũăˀӗ£˩ϝӮк¦ЄƑ˺ˇҢкфíåʥѥѐ\u038dѰ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032408.143614:+0000',
                                                                            '20210327:032408.164863:+0000',
                                                                            '20210327:032408.183041:+0000',
                                                                            '20210327:032408.200154:+0000',
                                                                            '20210327:032408.216927:+0000',
                                                                            '20210327:032408.231825:+0000',
                                                                            '20210327:032408.248586:+0000',
                                                                            '20210327:032408.266878:+0000',
                                                                            '20210327:032408.284193:+0000',
                                                                            '20210327:032408.300452:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ӎ˨ăɔӘ%ŋʂ˝ųìϿю!ɓωúĆǶƦɳ¤ϱƣƙǻ˯ΕΰƂ',
                    'message': 'ҀԫәϬӰϐȨšиЃƸ¯ѓʊԬǾˠΆnНƎ9ԫϢµȣȻɬҔ;',
                    'arguments': [
                            {
                                        'name': 'ōɟĜԫ¸ҝ˞ƤEȁ˙ԚӯĠ]ӿǘҊαӆó˾ǛXȄƱɪкɔÑ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĠǷҽΛɲʑɼҵƍƠԇϪǎ"οԊГ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 739080.9664266665,
                                                    },
                                    },
                            {
                                        'name': 'pʬѯРʋɝТɓПБcSΖӆĤψф`Ϳëʺћ˨ŕɀюнɴѦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032408.774790:+0000',
                                                    },
                                    },
                            {
                                        'name': "ˌЎӤşӕϺȆ\x90η'Ώу0˕4",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɝǒΏΆӜӎɤҭκ\x98ҁĕȤд\x9bΪϸƆǆĊЇрȌɨƯȤӶɢȊ¾',
                                                                            'уŤǹȡѹԇˮԪɀɈƪҢɗŁƶѼӑȠώˬǡӲʝƏȟlϠñԑ˳',
                                                                            'ȈӷĖƶ\u03a2ϗ˵ŊÙӏùŇЅ\u03a2ͰɽţγϹɞ˘ӶΥԞǴʗͺӠɬτ',
                                                                            'Ě,έǬÊƽѨőʤ»˖˱ћӇ\x83ʎνƇʴžɃ×ѰɪЈΙŧǦ(Ƒ',
                                                                            'шΠɖǃǄĂвʻƒЊȍǦɽàʈƻɚʀӔ6ӕΗӦӼYµѷȬ?ȱ',
                                                                            "ŝӶɭϔѠɥЦЅʐ˧ǂШϝɄɅģ\xada[IӇŢԩϕ˜ĨCϸ'ˎ",
                                                                            'ѩ˭ˆʧӒ\\ɜѰΜXҡӄρ˘ԡǲӻœ6ˇԨ,ŝ˰Ζ˚ÛДÒƢ',
                                                                            "Ǿ˫үûŵŐƹGʱāҳʬǅɠƌʄ\u0383ÕϹʶʌɍӂƐ'ǵʳȩѷȣ",
                                                                            'ȡђȒ&ţ\x9bҵαʤɾϙ\x9dŐȯƩǺΎȣҔƹΩΞʷϿɌҩўί%ɰ',
                                                                            'BĥɽТ\xadɏT˳Ǉ\x8bЍγ·ȭԦˬχԕ˭ҶΟĽŲμ½ŔКԦΘԛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԏҟ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
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
                            {
                                        'name': 'ӺΙšȴΩҌTҀªкӖƢԭӖ˖ΜƑɯǼȭϸʡø\u0381ȀƦїΐͽƦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1426971095853075617,
                                                                            -6869522264084863931,
                                                                            2048173842786759861,
                                                                            -6494928449167722470,
                                                                            -5030516494985578410,
                                                                            5818870301999200479,
                                                                            183394953817012126,
                                                                            -8904655212228721014,
                                                                            -42846763275584809,
                                                                            2905159864059435639,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Pӻӗ\x85ƷāYˡāÒƝİ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'μӳķŁ\x8d\x96ăËҁѵӗͻӋаĚϪ\x82κѰҍϬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 437004.9237128247,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǩѣʍ΅шĸǭŕ[ɤǰɒ5Ǆ\x8dщӿˮх¸ҜԈ-,VѮhπ˝\x8d',
                    'message': 'ĴЌ\xad±ҶśѭÕĤџΓǇІĐ˥ɍӲӾʊé|Ƃ˶Ӳ҃×ѹºʱȥ',
                    'arguments': [
                            {
                                        'name': 'ťϣЉʨʺ˝Е%šғ;ǻʾԥ]ǅ\x8eÓʩƤҞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032410.552447:+0000',
                                                                            '20210327:032410.570578:+0000',
                                                                            '20210327:032410.590161:+0000',
                                                                            '20210327:032410.609324:+0000',
                                                                            '20210327:032410.630939:+0000',
                                                                            '20210327:032410.649626:+0000',
                                                                            '20210327:032410.670551:+0000',
                                                                            '20210327:032410.690925:+0000',
                                                                            '20210327:032410.710568:+0000',
                                                                            '20210327:032410.729056:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ʌúњm}\x88ǎĥǲʯ,ϩŌѹD',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5397106324885994680,
                                                    },
                                    },
                            {
                                        'name': 'ƤЙ˥\x8f>ĕāêӡʟĐѫȴˆˌЄӨӂ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'bƞêϾˣð²óƜ\x9dȜҿǝӜш˫èΗ\x97ǟŘʐǍȑɝѧėΣөҾ',
                                                    },
                                    },
                            {
                                        'name': 'WʙǍ\x94ǜί˄üѣЯƹʓŋь¢ŐԨȜъӨʖϝÔͻɌԞǟЯů\x95',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЯJĄ\x9bƻƫ\x87ļÜĴʱνʃӱЧ˅ƀŮφśӛɌƒVǈưƃǺ\x9dȴ',
                                                                            'ģƳэ§əӱȉŐšȣǍҨҩԡʩøǱĞʴ˧ŧӕǆƳƦҭǚŖƠǬ',
                                                                            'ǁϡFåʵëωǴ2ȸŨЊŲEҰŰʻӦŀĬƨȫΗʼԫƉǺώėˤ',
                                                                            'ιӱŞȆʃΐёPæČҺVϖǵʆπ˴ˁїǄ˥ʂǋfҽėϣЈ˾Ҩ',
                                                                            'æД˧;ϙȬξŅɤўȓԋǪҐʉÕϡҸϦbÇǓìϠЬìԎ˅Ȼӽ',
                                                                            'ɻ˕VʚѩɡΙωТҪNĜĦíӈ|ʔƥʘɋӤô˺ԣϪ҃ǫԥϫӴ',
                                                                            'Ў2Ϳɾ@ʒȽƕEшʢšŎ҉ѵѷ\x87ɸ˪ȿяԠɹƂҊşÌ¶ɆΩ',
                                                                            'сļǹПǣŜɝǚԏĻƁВԐϮΖͲĊǑȄƏjɄГͰßƂąÖӆƑ',
                                                                            '˰ҥƝśҞўƮP\x8cЉƇȖӒϧώʅʷúàϲǦԦԁӪҭ˚ʩɾƁƩ',
                                                                            'ȘӸżҷҴźĺĮs"ʳ\x9bԊÍʇϔԩϑϢšЪ\'Шȏ+HơõӪг',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'άŮƙғдҡOʅʄϘˣЮ/ŤžҨѭĦǉüҰϥǦϾ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032411.279737:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȔŽȂϠԗӭŝӊ|Ϧг#ѡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ȾħƖȃ®ǋɾȦʨƇԪΦ'Ϳ\x81cȘɒǃǩȸԝұҌvϝɒѰȢҗ",
                                                    },
                                    },
                            {
                                        'name': 'ѤȈΓʻԤÍg\u0380ɪԭʇʬŕŎĤĕCӴˌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˮҵҺɽќþϔˤɑͰȶҹɇѵ҃αȹңǎŮѦɺæƕѝҭʦԞΧ\x81',
                                                    },
                                    },
                            {
                                        'name': 'ҎʷπɌϚƺɒ´ÚԭʁЦǑΉ\x8bĆѐŏʙƧŕѣǇʑўӵԗǱȁ˻',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ӱèωӤƫźŘсзʆÝİι˞ϺͱɎŴΰŨ?µ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ÝӾµҩŀѧϔǸîg˧¨ϤΔΨΈбҋΙ˫',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            70255.52039530958,
                                                                            267866.71236048517,
                                                                            479008.815860818,
                                                                            631005.3703383678,
                                                                            882050.0477479051,
                                                                            830423.9874390722,
                                                                            555962.5089543754,
                                                                            660046.7722794639,
                                                                            938622.5666656914,
                                                                            921656.7638401447,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӓʞ˄˳ʼҤʐɌØӲʏÙÏĄǣΆȡӳÝӸψԆиĽҤxДӺu\x91',
                    'message': 'ûΆˈҕǌɸrĻҭ+ҧÂŴӃÈÝż˯҇ɊEØɫƚϟ,ũɚʔȨ',
                    'arguments': [
                            {
                                        'name': 'ũЁӜԦϲԛƸƑҥϊƫN\u0378Φ\x7f´ȸϑԎ˄˟ɝїîǨĵ@',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ԡψʟȕ˰ƕʀɥĻʧϾ¸ЍʹқХʃŸŮŧƧų×ŦОƽˀʮȞϞ',
                                                    },
                                    },
                            {
                                        'name': 'ΗƺÔŗYҼˈɜ,ð',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ͱϜШ,Ļѣʑ˕ƌǠ-ƨЧў7\x9b\x92˙ÞǄɋΈǔȎѵF',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7467864859490825753,
                                                    },
                                    },
                            {
                                        'name': 'ʔұª=Ȗ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            557623.9289706387,
                                                                            306656.7478028325,
                                                                            51316.44052073563,
                                                                            70410.29902280952,
                                                                            499718.7309136373,
                                                                            347474.645945278,
                                                                            715746.2404112072,
                                                                            568113.9587649466,
                                                                            147680.26894360423,
                                                                            69335.67487215999,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʣĕ\u038dě˨óȷ8ǫP\u0383ˡ˚MƈηČĖрϻȽ҄ũҽ\x9eҀφÏЙљ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5537013952829453164,
                                                    },
                                    },
                            {
                                        'name': 'Ŀо\x8f˛њӼÔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032412.703202:+0000',
                                                                            '20210327:032412.722262:+0000',
                                                                            '20210327:032412.741236:+0000',
                                                                            '20210327:032412.760136:+0000',
                                                                            '20210327:032413.106328:+0000',
                                                                            '20210327:032413.122921:+0000',
                                                                            '20210327:032413.138865:+0000',
                                                                            '20210327:032413.154828:+0000',
                                                                            '20210327:032413.168089:+0000',
                                                                            '20210327:032413.180967:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ўԮʓԞҳȽЅŕ˔ԮȒх¿ƚʵѼӓЖcØЬ˲Țʰʷϋɴ\x9cХϡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4653031027821191177,
                                                    },
                                    },
                            {
                                        'name': ';űȉŎӬκβÌϵķ\x91H',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϷԟƗ˗8Ǜ˝ȓЭҶҢŔǻ\u0382!ȇǵŮŷΠzҫƧӓ2ťМ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϻ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032413.887112:+0000',
                                                                            '20210327:032413.901862:+0000',
                                                                            '20210327:032413.916755:+0000',
                                                                            '20210327:032413.934367:+0000',
                                                                            '20210327:032413.956463:+0000',
                                                                            '20210327:032413.977311:+0000',
                                                                            '20210327:032413.999743:+0000',
                                                                            '20210327:032414.021330:+0000',
                                                                            '20210327:032414.042002:+0000',
                                                                            '20210327:032414.063672:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȢQ¸Ȁԭҙ˃Ѝ\x88\x8dԥ$ϬНεʙԛĞҌћǼӣɯQϬ§ɫǬҭ2',
                    'message': 'Ԭοɶɽ˝Ҫ½ҮËԉȍɲŊϰʝœjǋѫĀɒļΓԗǰӺɉŶΘ˺',
                    'arguments': [
                            {
                                        'name': 'ВƖ\x93ұӢˆӀą^[єȘšʛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6876821859198000049,
                                                                            -1340661198276872299,
                                                                            -3357854459826811270,
                                                                            -6298166541358901022,
                                                                            5346057180132797439,
                                                                            918090634117150628,
                                                                            7698318674137800104,
                                                                            7668481415264066498,
                                                                            -8272235090119332952,
                                                                            6361846308426990707,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'й',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032414.532393:+0000',
                                                                            '20210327:032414.555733:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ňЊͼңōԋǾ{\x98ԑcηԀ¬ξǆʥȇǽЦȥӒªˮбÈȰХŜʾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4231786151557733489,
                                                    },
                                    },
                            {
                                        'name': 'Ӥ˙Ԭ\x80τƲЉˇ¾ԉrġ\x8d\x94',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 15859.172776181746,
                                                    },
                                    },
                            {
                                        'name': 'Ӓԃ˖ѧªŖɬȯXҘӴ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӞιЮɯĎƟԕʓʲҁӞnțО0ѝҝźѠеЈlȚ=ЯƽƽƱҏǎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѸƒǨԑНBŢЁɐ·ĭԪő\x80˂Ƃŵǎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҙӱuɢφώģɜƣƒԪǀϻκyќķɸɋӤˊʩæˢĚЅεEȚÂ',
                                                                            'ƟŚҿϲԕώȌΩҚ\x96İ«ѼċӳκˣɮӈéǑɇҺƀҋɾȲŋҍŚ',
                                                                            'ĄɑϦТàȮͷ˽\x8aϥԖǓ\x9aаŏĿÙҎȚŬΝУөǅɍćø͵Ʊ`',
                                                                            'nѯ4кYхЦȴΙªœьƼʥŸʻƂůόͳ#Ħǋ\x90Ԡ+ҮԑҋƧ',
                                                                            '˨ι÷ˈ˞ԜˈԅU˜ɣóǪƇɳá Ĩĝ¿ӶƴҘυɸԧǿϊɮХ',
                                                                            '\u038bĕЍӃɿɢďÓԚӽҫƾƐώƴÃÃȇԛ·ŶĠǩmĀċ^\x89Tȟ',
                                                                            '¹ƞ@Ԫъǯǂ7ɉʉƮαÿ҆ҒѮжɒļ\u0383ļƢѹӂǷΏФcχӻ',
                                                                            'ˣˤŅɌʚξȼӚҟĺ<ǲǀ\u0382ьȩϴĈsȓʖϮгýˤɞÊҦȮ˩',
                                                                            'ˑǁÚɽӴбȷҋϕÓȵύԛцΆȻΐωψĩʷˋ˒\x8fЁſѲ҃\x87Ȕ',
                                                                            'sŐɊǊзќҤYĸć®áșǼȻ9ʖǢʎπʖ\x99ԃά]ŪғͳƆǱ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΠΒѼÌ\x9cäχńOǬȢsĒƋÄ¦ɶhȖ\x97Ңҥԥ\x8bɨӚΣЯěЖ',
                    'message': 'ǐΫ:ȗμтA˯Ύ\x9bʛԈǊŨеɁ˰ʱ˴ћϟǲĀƨ%×ǤǠŠċ',
                    'arguments': [
                            {
                                        'name': 'ʕΉȴ¨πXʁøȹƘŝџԇÅëǀʹʸГнıɫϲψΙюīɩˤи',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ѥɼˊƅ=ˡMј',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032415.583189:+0000',
                                                                            '20210327:032415.605935:+0000',
                                                                            '20210327:032415.626703:+0000',
                                                                            '20210327:032415.648101:+0000',
                                                                            '20210327:032415.668530:+0000',
                                                                            '20210327:032415.690131:+0000',
                                                                            '20210327:032415.715908:+0000',
                                                                            '20210327:032415.734738:+0000',
                                                                            '20210327:032415.755374:+0000',
                                                                            '20210327:032415.776130:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ćҏȡʜѳӾ˛ȨȨӦ˝Ԯ˸tƒнωǂΨ@ȔɬΪңƏԍҰƼͺѣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȡЁ˄ǉίȪЀ¥ёѹčɅRŖĳɠŝНƒoǍɋԒÈѕƳ"ԅ£Ζ',
                                                    },
                                    },
                            {
                                        'name': 'ϫϝϧӰČǕ˴ͺ\x89wŁʫЍȨÚǇͶǦҭˍˁ˙ԥӱVҔʯŽȷˤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032415.964883:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x89Ăʪϟ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ԏɑ4Ʊ˯ЗȻɦpʼȲ/ɬʀəЎѪʰсɔǺǰӖƬTªϗͿȀ\x91',
                                                                            '˫φ{Ƭ˄ŝԤ¬\x8dɇǧӲįǜɳżĦɑªŦӑїơà*ˇģÏĎӵ',
                                                                            'ɮ˞ŇƌƀɎŅMѣƬǋѹĎʜ\x91ύ\u038dτε\u038dˬʠŻ҆ŠԞȥƓҸˬ',
                                                                            '˝ɆgĸȽѿϕԅƒŔ\x8bȽΛŢ\x82\x80҇ˊҤƀ·ȇʍđîȔlЉʭӋ',
                                                                            '\x9e\\ǰËĶŭĝǐҎŵyѡüҒ\x87ʧȁ\x8bǤĬ\x8cĸɎǳ҅ɢø˟{ԋ',
                                                                            'ϻӀĵȤԫQ΄Ӏ£ɒдxΩ);ɰƹ҄ǠȤηÂƓƴ\x9bӯʏΪ˘ŵ',
                                                                            'Ѻɍϫ4Ѓ˻ɒêёϚθǢųϸɦ˭ЄŃЯłϗԂd1ã˞џηɈҷ',
                                                                            'εШˮǇθʑΈûȊʉӄȏʅȩȹ˫ҳѢТӸϚłʹ˔ϸɕ\x8aƦԛɕ',
                                                                            'ˈģǫźУȭÊӭҶįıʣVǻЀӭ\u03a2±ÂԁŷúƞHŪηϏǶ\x8eŠ',
                                                                            'ʚШ®ȳόĶ´\\ʳӺ/ĻƕƷʇĎ\u0380\x95ȼͺıƷƏЀԞZӄĸǞȍ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɐҧȶ¡Җˏ2ę',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɳǩж',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 456250.6669102089,
                                                    },
                                    },
                            {
                                        'name': 'ȡҡʋ˵ɤzéŵƽƊʉ\x7fϹјÃ\u0382ƧϼʪӋʎӵkΐзt\x97˘ЮЭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032416.448527:+0000',
                                                    },
                                    },
                            {
                                        'name': 'яӅѳɈȷ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3201869524580304639,
                                                                            7428681788243350464,
                                                                            7596832426711526250,
                                                                            -73559651733658267,
                                                                            -6385768336427217177,
                                                                            1564758247017538312,
                                                                            -6267677101035645703,
                                                                            5839399385268712787,
                                                                            -8234694629249414718,
                                                                            2955704990376837748,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӻ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032416.790119:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȚΌԚͽʃʛ\u0380ŒğƌɀӒʛ͵û?ЄʢƞʐʏтԡÎԕўVþԉy',
                    'message': 'Ҷƒŝ\x80аѧXнĂȠǃ·БСѲ˕ŷƉ¦у¢Îњ˽³ǝƿKĥҒ',
                    'arguments': [
                            {
                                        'name': 'ɐϔ%ǆЪҺǓȾƭʔНhӨ¢ůĥȦɹʇƀțȓ˷΅ǫąӒěſž',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -50406.08560376263,
                                                    },
                                    },
                            {
                                        'name': 'ΙБȖҭƢԝЬѳŭʷϲéоѮѰȩƮҔΊűʝіΐɆcɉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            764979.7634136572,
                                                                            673084.7780352317,
                                                                            369723.3354181591,
                                                                            926841.1273741745,
                                                                            105843.60160084354,
                                                                            574871.7328313309,
                                                                            448674.9766212024,
                                                                            730146.1517429899,
                                                                            22461.593672634146,
                                                                            283607.9260489482,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "҄Н;ҎϘšˇπMɏĿƆӃƘӗ\xad\x8d\u03793Ǎ˱˺'ΔŚ",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            192830.00559053913,
                                                                            212753.30015347933,
                                                                            538879.2160082195,
                                                                            -52533.24377167861,
                                                                            354863.0252306811,
                                                                            214812.87446659373,
                                                                            -72068.87341998654,
                                                                            616785.98740688,
                                                                            330647.2416093992,
                                                                            108184.96957606977,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x99ʑĢҰɍ·ìҢȅԔɰĉə\x99ӌжИѬГƱ҂±ßÆòϺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032417.507785:+0000',
                                                                            '20210327:032417.538176:+0000',
                                                                            '20210327:032417.575158:+0000',
                                                                            '20210327:032417.593802:+0000',
                                                                            '20210327:032417.615794:+0000',
                                                                            '20210327:032417.637136:+0000',
                                                                            '20210327:032417.657799:+0000',
                                                                            '20210327:032417.681759:+0000',
                                                                            '20210327:032417.706293:+0000',
                                                                            '20210327:032417.729930:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¯Ӓɴʱʈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ſήӋˀǤŕʹȼïѩшǴɨԍʆȽ˭ÚôӸԂϷǮӵˏ\x87ȫȢԮ\x7f',
                                                    },
                                    },
                            {
                                        'name': 'ΕϬВҰЁӬҖӽЩ˶¼ǶѮϜӋǯΡϭѻԅȳ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҷäΨ¦ӞƢѡßǱɅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǳAҒÇƖ·ƱњуʐǷĿɇҚČΚҸƉkɸ_·јμ²ǊɥҶ9ɸ',
                                                    },
                                    },
                            {
                                        'name': 'ŘP\x81˥ӓңԄ˖7ĞΟƅҦɾƮ˜ØЖѶǽˇӌǰʛɊƨφ\x7fϸʮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032418.035169:+0000',
                                                                            '20210327:032418.055202:+0000',
                                                                            '20210327:032418.074894:+0000',
                                                                            '20210327:032418.093782:+0000',
                                                                            '20210327:032418.112824:+0000',
                                                                            '20210327:032418.130996:+0000',
                                                                            '20210327:032418.148949:+0000',
                                                                            '20210327:032418.167539:+0000',
                                                                            '20210327:032418.185345:+0000',
                                                                            '20210327:032418.209807:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȮǚȰԜƢјѱɥϢίȝpҷDðĬύЭƏͱļѷ\x80ʹǢȭѿȥ˭Ɔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҘßŮ\x91ͳѬ\x8cş˒SȞғψ҃ƅ˸Ε¿ӃεšĀƮНȞ\x92Οвѩь',
                                                    },
                                    },
                            {
                                        'name': 'ŌȯѲӶГǁӭĿīźʈřŠȵƤǗ£чО˔õȝ˰ǮӞʺɑʉƐҟ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȲǘɹΚɣˌǾ\x94˱ѷҏǠɼǁʸǴӂǴЄ\x9fʙĽʁΣΐѪәԙőÀ',
                                                                            "ӊAӮʹɧǎȩΤЇ¾ѣ\x8bϢǛҪ,ѩÓþ\x88ʼÄ'ÐȉΧ7¼ҳ͵",
                                                                            "Ś¼ÙΎӏǷíϦŏɭÀѹʯΘЋ\x8báΎɓҀʠlɼȿѡƛϢŋ'Ų",
                                                                            '.ʾϐƲ҆Ԡ\x83ƶюљĴϧӸĄÝɕϊԠϢƆʐȥϺϾǑϵяыǨϡ',
                                                                            'ԭΕҤΒ˧åȰ˩εӥӡˌļȟ«ϣЂĞɢĂĽц˂ǚӁĚѬɠҋk',
                                                                            'Ēǻ8ȡƂуʙËˠԣϨƬԐkïиȅķ˫ҙ\x90ӻвϦ¡ɟ°ԌΛư',
                                                                            '\u0380ԁUƍҚιʁ˪ɲҜыĀ˶\x9eө˙Ԝbзэɐɼ©LŗŕũПŗњ',
                                                                            'ŐѧάԪϮ\u03a2Ű%ȟЎԣџ/lӥΦӏƻӔɃŁӰъФǹϵƆĨҲт',
                                                                            'Ɂѡ"ȇψДnʅȯʃ£Ӏ\xadʢˈҒƃǵ(ϮƱʚțӁFμсƞʃԃ',
                                                                            'ǒɷ˓тЇŇŰЍɃҽȖxǞ£Ԋ\x9dɋžҍ\u0379\x9fгkԓŢp˂ǩǍɅ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ų˱тñҮӦ½юǯĒȚʊːȥΞӫșʀԕɥЍìŕɒɉʳϊˋ\x88ʀ',
                    'message': 'ΠΏúѱԇƎӶǢҒĊųʤҲҺҔ\x97ąǒϫԄƭȝƟ$ӶȆʶΦɻν',
                    'arguments': [
                            {
                                        'name': 'þ˂ŹӻԟРӋѣϚΏӳЉ*gϑхʹĻÎȗ°ϚɣKѻĢˊσʦͲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʞͰϗӠ\x87ɟ\x98ұӠȩӓ˕ҨńɌȹʔԋЖɮɂѯ҄ҊΣԄԃѲɵ4',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȝʷˁǩік¥ϻөԋ\x90ˣ\x8aЫˎӊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1371644411308726090,
                                                    },
                                    },
                            {
                                        'name': 'ëħӽƌįсXдΰқʧDV;6ӠĐҮȏǿѻrϵͷӣǬɢţ$',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            704471.7654409923,
                                                                            899749.3414267853,
                                                                            582889.2458221369,
                                                                            297393.2977481794,
                                                                            345160.3918518031,
                                                                            625275.5657272204,
                                                                            339110.80749896297,
                                                                            617737.222072238,
                                                                            11569.67448664701,
                                                                            587510.555365077,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'җЦӸСвɹѩÅİɮʃқɤȻƔ"ҥ˘ЩÊɱδӨѓ÷Ѧ҇ʄԊĈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 331242.94475006626,
                                                    },
                                    },
                            {
                                        'name': 'ҡ\x90ɏϛˠʫË',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϐƨʊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʘɽГ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 176495.15023449465,
                                                    },
                                    },
                            {
                                        'name': 'ԕӁɡǙ³ϔԑŏ˚҅ЖIğӡαhҀĦʦ˝',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032419.990437:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǼǾŏņɲBӀʅǀ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ґӁǇ½њЊȂħʱī˺ϰΛſƆζӠƋǦёъЇϭƉӲϽԀӧ²Ğ',
                                                    },
                                    },
                            {
                                        'name': 'ʟâӺőƾũƦ¡βԗΧș˼ӥΟʇъʍ˞ʷŒȧ*ǝЮçј\x91ϫĶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            65499.477174687054,
                                                                            706461.80783792,
                                                                            80266.06971291255,
                                                                            284847.2777909155,
                                                                            176776.36646190612,
                                                                            529146.6224872476,
                                                                            986824.0441341407,
                                                                            49135.28038468599,
                                                                            130588.56951762477,
                                                                            -77463.13234662541,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˒Ι5вȱƱӦdĉƹИłíΟӎв\x97ϙŝŖӣʂдϫăǑЋ`Ȃɓ',
                    'message': '˜ϢċƐɾѶǝǔԁά¨ëĮÜԮҧʹũԭàɯƿЦӍҘɲѹʆøǧ',
                    'arguments': [
                            {
                                        'name': 'ıһžѲˌɣé+Ĩӯ˜ʱŶѨȏȌқĹмÀŀ΅Ғ\u038bdø˟Ƅ/ö',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            352849.767526913,
                                                                            604167.6232907055,
                                                                            231511.47978801862,
                                                                            311423.19166978763,
                                                                            634028.275396025,
                                                                            607031.1821899081,
                                                                            852961.10774587,
                                                                            589415.9774802036,
                                                                            181419.55597146665,
                                                                            19067.27075075038,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'йӊĒԐҩԐ÷ǲȮīŪўщάʭѹʮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 235816.53214518738,
                                                    },
                                    },
                            {
                                        'name': 'ƙɰй5ɦɐ\x83ԃɏĦЧŨ΄ǢȝΪǫ£ΪǮ¡\u038bȀ\x83âӏˀϟǛĎ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032420.900837:+0000',
                                                                            '20210327:032420.919579:+0000',
                                                                            '20210327:032420.936757:+0000',
                                                                            '20210327:032420.952111:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˝ÍǘЧʋӚżӰκλφĭhϨH',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 694741.3071078688,
                                                    },
                                    },
                            {
                                        'name': 'ƬŀƠĬКʭȦ¼˥ǁɎъҊɐȲűˍÀ˘³LtʻТș8ɡðúѨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032421.100056:+0000',
                                                                            '20210327:032421.117328:+0000',
                                                                            '20210327:032421.134550:+0000',
                                                                            '20210327:032421.151432:+0000',
                                                                            '20210327:032421.168369:+0000',
                                                                            '20210327:032421.185509:+0000',
                                                                            '20210327:032421.202445:+0000',
                                                                            '20210327:032421.220686:+0000',
                                                                            '20210327:032421.242635:+0000',
                                                                            '20210327:032421.264152:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЖӸȾӓʬΨҚˑӹȠ&ŪЇǋ®ɜȈɳ\x85ʭЈҰ˲ȘȣμĢϝΒȢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 911385.3977127103,
                                                    },
                                    },
                            {
                                        'name': 'ɴȌԭʂǭЕɶФˊĒϑÃԪų',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΄øɫќǜϣŨʝϵRѹɩФŌɆđɶ\x97˃ƸƪSѵϸԎȤцЪêι',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032421.680376:+0000',
                                                    },
                                    },
                            {
                                        'name': '˸Ϟԗɂ˗źɿĸ®{¤ńҎÜ·їʘ¡ôʹŗɯɮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4908421028363295778,
                                                    },
                                    },
                            {
                                        'name': 'ŵӘ³°Ǜ.ŶɅųɾ(Νύā҆ċʹӄ:5ԙO',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8392189767079232458,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҤΤǤ,ϚψɵgǚƎ+ҿæԬʄљʥǤ6^Ǥс˻Вåχˬàѽ_',
                    'message': 'ʲˈƠɩԂǐ9mϤҾӚȿŢεiӒщӼʎƴ;ɐǈœόԨʩЎˮӝ',
                    'arguments': [
                            {
                                        'name': '±?κǨ>ȏǺʟˁˎĲԏŎӫß½ȉ³ҰϹ~ѧʷȺˆϥɪӏÉǲ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'КԐíӲ¬ʄǿģōǔƧӟƸb',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 706967.126706544,
                                                    },
                                    },
                            {
                                        'name': 'ȫȶp`çѓ˨ʿʧǵȜӷ˲ųνͳΫ¤0lɔğɋǝŤģș˛Ϻʭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032422.292708:+0000',
                                                                            '20210327:032422.310218:+0000',
                                                                            '20210327:032422.327780:+0000',
                                                                            '20210327:032422.802528:+0000',
                                                                            '20210327:032422.823962:+0000',
                                                                            '20210327:032422.844180:+0000',
                                                                            '20210327:032422.863867:+0000',
                                                                            '20210327:032422.881614:+0000',
                                                                            '20210327:032422.900215:+0000',
                                                                            '20210327:032422.918153:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǫǈˆ˧ŵ\x96ΘϵԅɺķΧͺӢʜеb?LȅƇɽǇǳ˕ϧƪġԒʠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĤѳɺňͽюұÀɁÓ\x9fŌŕ?ΔͲи9ʝҎŧĜbϢϐ\x8fɇͿҙ¬',
                                                    },
                                    },
                            {
                                        'name': 'ϾѦŞ"ǚɪϨ#\x8ed˫ȶĆ\u0381ªËʨƳǧҚÀ(Қ˳σiűЩgϳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŵÊċӍƞӂԧͷԍ΅Ϩϗ!èьѶрԭɷϣɔҝɗņʓȄ\x84ǇϚȟ',
                                                                            'ЭҒǵÞʏǎЩĲʈ£˒ήΛͷÇНˊҤԧŊԂ4ϭ\x86ьĮѼΊбҸ',
                                                                            'cîʦ¯Őӹ˸Δϭϴȉ4ΎТҡ\x8aˬǁӿͰ\x8dfȱԃ\x9dДɨÕԜϻ',
                                                                            " ĐҘɼȎƩςÏϓŵϗǍƐԎʛҦȭÁǶуѹ'ӶĄԔϝµѲΨǊ",
                                                                            'LǨkóǁпǒ\x92ȐӗoӄʃŃјūʴ\x85\u038bžʌџħʴɗƾʁѣÕ˗',
                                                                            'πèÄϑџ\x87қƷқͼƺɪΎƏкȴӨќɟӕ^ǃəǫɀưǆѮ҉Ʈ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɜͳĘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ωDρςoǖȳԀʶǔȑԝЌɡȆϞėίǹĿǐϲӭǔΫѪӑѐǿ~',
                                                    },
                                    },
                            {
                                        'name': 'ϺϙԄҁҳѱīҐΚͳ\x83Ƶȳϱ\x81ϻӳɾPʧқŧ:Ɲȶ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɊƪÎȣбſ˾ӱ{ɎùžΙȿɖΫɐЙΰΖɣԚʢňİЋԃɺs\x9d',
                                                    },
                                    },
                            {
                                        'name': 'įƹƤÐӴғΎ҆ЈɔςԮɁĮӫѦцSÆȿ|ȣ\x96Б(ҸŒǶёѭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032423.404185:+0000',
                                                                            '20210327:032423.420592:+0000',
                                                                            '20210327:032423.433920:+0000',
                                                                            '20210327:032423.448892:+0000',
                                                                            '20210327:032423.463372:+0000',
                                                                            '20210327:032423.481348:+0000',
                                                                            '20210327:032423.498180:+0000',
                                                                            '20210327:032423.515880:+0000',
                                                                            '20210327:032423.535158:+0000',
                                                                            '20210327:032423.556800:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'uлӟĖʗȬәӴҿĠ\u03a2нĴǄԋͱԮ-ӐɌʓȿɉäҿ7үҙĞԬ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032423.641362:+0000',
                                                                            '20210327:032423.658325:+0000',
                                                                            '20210327:032423.675389:+0000',
                                                                            '20210327:032423.691885:+0000',
                                                                            '20210327:032423.708926:+0000',
                                                                            '20210327:032423.726911:+0000',
                                                                            '20210327:032423.742957:+0000',
                                                                            '20210327:032423.760497:+0000',
                                                                            '20210327:032423.777050:+0000',
                                                                            '20210327:032423.794449:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u03a2ѳˉќ˹¯ɨųS\x81ˋÌţæÚ÷ԟǋѹǟǑć½ӨʠȚƨz¸ʗ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032423.882249:+0000',
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

            'identifier': 'ʶˀþǩɁ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ϙɒ',
                    'message': 'Ƣ',
                },
            ],

        },
    ),
]


class SystemErrorEventTest(unittest.TestCase):
    """
    Tests for SystemErrorEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SYSTEM_ERROR_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.SystemErrorEvent.parse_data(test_data)
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
        for test_name, test_data in SYSTEM_ERROR_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.SystemErrorEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SYSTEM_ERROR_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='SystemErrorEvent'),
            ),

        ),
    ),

]


SYSTEM_ERROR_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'error': {
                'identifier': 'õǓȖұǨ҉ȌʮʹźҾ_~ĢZǾŎəÝϤӺйȊ\u038b˓Әϸүʋȷ',
                'categories': [
                    'os',
                    'network',
                    'configuration',
                    'os',
                    'os',
                    'configuration',
                    'access-restriction',
                    'internal',
                    'file',
                    'internal',
                ],
                'source': '˞˯ūĳɘǰдДӄˣϨԙбӔΡēʟӵθɛĔŏ~ѸŜҷәňϣ»',
                'messages': [
                    {
                            'catalog': 'åщȦƆʴʢYŷLɃƠωŌ\x89ђйѴ\x80Ʌſŏɂ\x8dɮϸǇ²fǄ¨',
                            'message': 'LƻÂȉӗˠĵ\x84˪\x83ҬѬΈnʬΣӭĴюɹԣ~ȄͿхƨӇǇҐȁ',
                            'arguments': [
                                        {
                                                        'name': 'ίѻʂЙĤԍӀǦȸʵŎˡÓì˦ЏęėSԙ˗ſ¸xȤĖӄΏЅʃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '7µӾ7ϔѨɃʌɃ!{ˊʃ˱ſsϞůǃОǷҜȞҹȝŅġӑ@z',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3198102585198479295,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϿϽʂӊϪЁĮҳϞΎŚǴɴѝƙӐɅ\x80źлĿ ÃʞèʣѦǅʡ\x88',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ģӆǡ˒ʻǁΧśʾɳӊҊѕèȆѱ×ҳμƃˏӬ˒\u0382ӥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҷȢԜȣƇ.¦ϷŚCϜɮǬ\x96µҶùПΌƍƼɨŬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷ*ЊȁϬ\u038bBϾǴč!Žƌȇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'nģӄЮюɽƊÖіÒÊȇљȢɺϤįτԂѥĴ˲ȉʘȜȩнÅСF',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɞ˘ο?%RϘDǳŏÀȯʗЃɔйҍЩʭγϐЪÙƸ¼ȼŕϋԮԋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳʥˎǾӣĹĲͷβьģȣșңѦˉĘǩâʔԁҟk',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7259089459769506142,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɗŕ¤ҾЋʴ\x92СӨaάHƶt"ҔſԖԫȊʑΤʼƈφьѧƫԓX',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 182127.71336718835,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ц\x87БӀƷΉϴʒɽı\x96ƛҢВƖźЙſдŬɗxю¯ДxҜ҄Ӧr',
                            'message': 'ȨЃԂǑјϝĬʒʂӫϯι˔Ӯ¤ɩUáăɣЛʝԑӅʛǝѲʝňΛ',
                            'arguments': [
                                        {
                                                        'name': '\x84ɹȄɌӭŲͷϡΧƝѣҘ7ư˚ğŶʂͳÑˇĀÛʛȏΫŢPҟ˅',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄iLʑЭś>ėңMɁƳ\x9aӞПKJԧŐԔ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ư¢Ϲ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x82ԭȬƬķŤɾȑÕ\x86ӨƧЎҕςaˎͻʫĵӆ',
                            'message': 'ĉ\x95ʝЌĆâĚȎÿȓƧϼƔơ\x85\x7fĊӧȦȸЯÊϗǔїҀϯgʴɫ',
                            'arguments': [
                                        {
                                                        'name': 'ӪωѫȢǎ˵жŚϹЁЪǩµΙӉžǁξζҨ\u0383аӀɴίγͼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΤҕҗˁǮYҢǦöʰΩǏпɴ¨ǣԫӳȘѐʞǱаĪҽҡ\\ȥȤо',
                            'message': 'ǖ˘͵ˈȳцʽΈƊŁǭӰ«ʰҌʟÌΑӵǰϷŏРɠӎÿƷǀǉȉ',
                            'arguments': [
                                        {
                                                        'name': 'ч\x9eƺǛɁǹԊǋˁӡҢЉ˪ҩǉ˸ӂξҮô2ΧÜ˱ȰɞŜċȂԙ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӱ˘ȈʑȾʴЭϭŷ¹Ϟ¾ǟʥ]ωѬƓʪýːЏԀ\u0380ӳ˂ȘЫøÇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʺŨɯʖɝЌ˸ɝҌ҅¨ĳҲȺ´ĚΕŲƬôÍѻђŹɯƥԆФ\x8aш',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6169292477614687236,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˉӹѺζʇӷθǤэеI\x9b',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÖƟѡËΊƏ^Ŭԙԉ˘˧ʓſʀӝ\x9dғ˴Ƕ˹ϙЙƐ\x89ӤȣҘ¬m',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϾӅϴſÁ˱ЇЛķā\u038bȽ2˕Ȗ=',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8154945095446209974,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔʑӜԡ\x86ɩʍȌñϓƖʫԏӔǙНǏƥӑӪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚǌƜű΅ɧɆͶϑǋͻƫƾUŚӦǃƳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǜī\x89ųȄʬÌο(ƞҙʉӯӠϓϻɔ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȔГҨѺϪ¿ɯǣ¯Ĺϑѽ\x8bԚŴEɑƶӽΊлԠĊ\x99ƕÍĹϨӔҕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032359.536762:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӦƝˏұПêŬԙϑŐюԃеǤƦȍʸżǩӻȽҪ)',
                            'message': 'ɕ¼ԕҁǾ¯ѥǼȖɑƸàɭΪɔŇŻǿƻȿnĲϓ҆ɷЕ΅ӡԓȕ',
                            'arguments': [
                                        {
                                                        'name': 'ʹƓφӉλqӢ˝xƴ¸ĉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032359.679519:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'КŵŁϛΓǉӜцʹӘɏЭ\x83ԇƞʳ·',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȫџƿàƷǴ˕E϶DŵԀţɛZ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032359.845925:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҲȮʆēĭɣǫөGӉ_Ǽӯɭԫ£ĤԂƟЦЅ\u038bσ©Ўǣ\x87eŎ\x82',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓԐ\x9dͲβ#Ƌ˄ĈԠϘѾрĎˊGӑ©ԅЇɔ҅ƃԇŴмˎϰӤń',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032359.995863:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӣȣΟƒмNVϧ҅\x8cԬþ\x9dƾΖxΕS\x9eɚ\x81ӳɕҸśƟϫģͳǐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'αƺʿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʳIśːĪˏΘǙȵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӆԂԛǨѓĵ\x96,ɒ\x8b¶ɆK˶ιԄϨɯʚöǝǫ\x82ђk˞К³ȅc',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĉэ͵ɞáҎĪµVӸĸҧ¿Ȍ+ëŝ#ѭ_oӲǢğƳΙǬƭԟӉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1001896989351849717,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˠ3ǉɌĀͱäҤƊȑδĒґėƐνƺɳsưԊϗŪӽƽɨЎAԍѓ',
                            'message': '\x91·ʴȡЖҿҺМp¸\xa0ƵԖӌªԨќ¯ϚǓӆđԪɢĵŗȫÐŪԪ',
                            'arguments': [
                                        {
                                                        'name': 'Ѓ/ʗɘƖѭʫύҙnͼ˗[җп\x89Ϙ\x9a×чǔҗϓuΟų ǯ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032400.498298:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '.үʈ©é*źLȴƄΐҷ\x8dˬчԊеǫуȰтǳΪϰ˘İAԮǇϗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҆ŬÍ҅ϯИ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -62873.72830025833,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĩԑ\x91ç ßѹѡƇĄƺŇˤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˘΅ȉɠ\x94ǇӊȥƟˑˋϟƃ®£ҐмĨǭƎĆǭɝқӇƑěMҝԙ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƊϱХʕʃʊԩшвƼѦʑƋμʶ\x81ÆѡӜЦȓђ|',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻɊ\u0378ґԆǡӻďŲɳ\u0380˽ϻōӂ\x96\u0383ƜʦɫȎӵ)ʢŮ£',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕȥϨĨμϠ\xa0ɢвҵ³ŬĭrəӊƲ2γĦϪ~ϚХɦƗĬԙ?Ĩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǼɰˎѴMӴъѲ¸ÞŮ\xa0ʗå',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 152623.962759968,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁщ=ЧÉȣǱÔİʴ\x8fęƤʉċМπӛæĽӌ?ťϣЂϑü',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɵƳжӦԥ´ʉӹǒ˔ӐǷůƧЌkÓ\x91ƏýOɩӷšӗ{ҳ{Òԗ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԙ!',
                            'message': 'rŷȻ¥~ԛǽήKӼȝRϘѥ°ƃéǍǭωϹΩҬƩƆƬϧǴ\x8aЈ',
                            'arguments': [
                                        {
                                                        'name': 'ӍƲ7ĎҢќӼΊTƸȬs\u038bǽ҅ţ;ʼüɡ\x87ʀ\x89m',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȒəҶ^θҚ˯\x97ђǙͶΙαΈüљg9ѧǛ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʉ×ЍşӲɯFѬ϶҄ƲħӝŞϲĺƸʘИԔˎӶǶЉŕɵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ũ˺áʮȘлɄϰǺ˧\x95ѵʕʒř',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɐИƃȍйɟ\xadğăŀ˼ɧǱгXȀĚÈлЮԒƱŧ˘ͲåӚƐюǻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 233853.28670860955,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɏ˙ĩΤбǫҔ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҈ΎΠĔƮϑºǟHƉԑ\x88ʼӱԮғѣΕңȣʃͱ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'і~ěҭѳÛƯŦХ҉ƁҴʠњ\x9cѣ\x8cǁ;ɣ¶ǡʌȧɼ˛Ȯс²ȋ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΡΆҞȫˁŠԅʓˢȄӊŰX¯ԨĿǺ°',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032401.823797:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'įвnԐŲ§ūПԓͲʴӄĈεƩ)Vӽń\x9fʼΧĚċϑƿ˛ёɥԆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԅɋ\u0383ǭҸӢгéˬȀԌˈ\u038bҭĢȅцԏкȒȜȾCғƟĸčΕ\x8eѹ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '_ԣo¼\x8dѫиЮ&ɟ϶ƊͿƨԃsΈҹҳGԝѸʐЫОƁŪɊϷv',
                            'message': '˨¼ҩђ\x90ȼѫҭʻ[ѷƑξҾȇ\x8dѨɎŽâ"юĨȟȿƬмádѓ',
                            'arguments': [
                                        {
                                                        'name': 'TтKǭǶǰʎɆ\x92ɭӆŶʓǿη˾ɖɆ˨ϯԟјƊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯƦӘɻǈVΧ˻ΆŐŐɷӪѣȿŉԭΝЁČҾ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4578846299503965886,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȃå˵Ό>ĖԖFšқˊƻҠҔʆЮνǖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9fʖſҋƢҋÍǜ\x94ʢ,ȦѿЏϛϨьMˌќɓø',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032402.254145:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǳ¹ťʂ҄ĤΝ(}ĻӊĐϫ\x91ʒÅϒϙшǾ\x91 ŃũƼΰӶ¦ȑǃ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3130226691642432079,
                                                                        },
                                                    },
                                        {
                                                        'name': 'čԝʐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8137357184106300095,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʻȿĂ*ғԐЂǈœ¥\x81ϛѝο˖ĜӍЇì\x83Ѿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĄƋɔ\x8bŚΏRˀϪħɰΤʮɷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ơҳ=ȈңЌKӱνԥȑÐҔрϤԩŚĦ˛jїŝҘʰ˴ƳʤƴgX',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 11189.352107616767,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆü҆ԚԘ\x810ŕЉͶфńϏĀѸɖǴҙϴΤ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƙԬēόϗУêǉÃ~ȃ˝1·ˑӸȝǖʔȺŮǘÂӠƗҼϿɶΐš',
                            'message': 'ϼƱҨΌŞʬˊőũŢҀǮԍ/Ф]íˊØÒɊÚσ&҄RʵϱϐϤ',
                            'arguments': [
                                        {
                                                        'name': 'ɚҾѺԤΰÎÒİNʑӆüә҆',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032402.894763:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '҇UƏɑƠɳǌbɸԚҒӘǸѥПϞ®ԅЩɟҼͲψˠº˼ťƖΑq',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ěȐҍɵ(ʼ¹ñʉԓŒӼƽŋԨҲɾΚЍŻϗºɈƠȭƁн¦ӽŢ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŵJΦƴυɃХ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ūѮįӮƥҋZǲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'лԝϚѥ\x8dЖҩғïɒпӐӧӺȪǟƉҁԐɨ:ƸHɔ\u038dǆ<ԝźΠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϼʇʐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '=ȝӐƙdļȏӮĺĳĽχnψİÿȠǫǫʊӉǯ0ϷуUOƁȃҡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΚƜɲȣʕԩҼ҇',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЎǬ˨ĬłĘůԉϣǠІĄ\xad϶ʋɮʈǰ\x83ҥÏͰt\x87eΪǈӗтК',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӵɥƙNɣȲκɍ2ˏӣӞͲáӒÅГϜϾŝï҂ǂ˜сTȻʡ«в',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '`өҞˌvҞ\x85љVɷѢҊ\x99Ƒ˘FʎʪɁПĘќҥԋ\x97Ϥ҉ˤԛҪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʖ\u03a2҃RεǬˑиưäʕԣ¼Ŝӄ\u03a2ƢȉŞǽʤΗ\x9fБӾԚϒ.Ʋţ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˹ϞǱĿʅʅҟ;ҏȕԇ·ǒˊɮmЕ?8Ǳͼƥr˰Ëǰ¢ΖɁА',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôԣҞşnʛʨѽ¢öʽŹǵΠƅˤǧЯђ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032403.614854:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԏǥɐƨĳΌǡӭҁȝӋˬɻЌ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '9˂ѣǟ½ęʖӋ¡˃¶ωЬ-Ρ,υЦŹȎΛɍѬϽOãʙ\x9dҶԣ',
                            'message': 'Ӎ˪\x9cǫϱț\x81Ϝ҃σ˂Ʊ҉ңӮ¨ơԛɬӪ×ҴÄ\x9cԎЯʣȲ\x81ԗ',
                            'arguments': [
                                        {
                                                        'name': 'ԉŀίȖɍЪўWҌƵʞˏԇǮӼ¥Ρ\x89äw_xɴ\x9dƽЎçʷıѨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӟКβɁ¿ș˘žЫϞɓɖɺ\x9dțʏęšùɝʧ&АΨĒˀîϊoœ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8638093683568017403,
                                                                        },
                                                    },
                                        {
                                                        'name': 'àɖөː˼ԍɸ˝˱Ʌπκ¼',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϺТĕӿPºGǺʥʣÅīŒʿƾЧԨ\u0379Ϯ\x8f\u0382\x9dĮǶɰѵȨпǌϳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǨԨȸŇщƿêΆY˹',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӵǉɯˍ\x9dЙ\x95èɔΰˈ#ůЕşĤʺɘΓԀ·ǺƘ^σÛͱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ρβυ®˭˛ԗÃŝԑƯïҗΒèǐʚɿԞǗŕɀΈРƓ˟вǹҙ°',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032404.616953:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԡ\x83оîΑƙ£ӔĀˠ\u0382ӯђŊ»HǬ*ÄΌ˼',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҞХӈО\x93ĮʶԬɗ%ДɈwіʤО\x9fȨЉυѓÚ_ЕƕˬƛРіθ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҝ\x8c½άҳѧηŦЇӰӕәӝȓ1ϵƀő˄˨ω˃ҟ\x9cυˤ˸ɑļɾ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋѰèщȗӂͺɤȒ˗\x7fчƌjșЙőһХÚϾPƲύʔjƸŗˤϲ',
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

            'error': {
                'identifier': '˂ӠϭÚǖ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'ŽZ',
                            'message': 'd',
                        },
                ],
            },

        },
    ),
]


class UserErrorEventTest(unittest.TestCase):
    """
    Tests for UserErrorEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in USER_ERROR_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.UserErrorEvent.parse_data(test_data)
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
        for test_name, test_data in USER_ERROR_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.UserErrorEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


USER_ERROR_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='user_error', name='UserErrorEvent'),
            ),

        ),
    ),

]


USER_ERROR_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'user_error': {
                'identifier': 'þϮ¦Ȃ/ҚhϦԟϲÚ\x89ҼʿǥcÖϚǦΝǒӒҮĞΪŢMVɯK',
                'categories': [
                    'internal',
                    'internal',
                    'configuration',
                    'network',
                    'network',
                    'configuration',
                    'configuration',
                    'file',
                    'internal',
                    'access-restriction',
                ],
                'source': 'ћȸFɟβæОǒJωŇˍȉȎШɧǿŪČcϰψ´rsӡ\u0379ŢìÁ',
                'messages': [
                    {
                            'catalog': 'ʰѦˊqȢвӮĂϵȗƩЁΜ\u0382ɭȮԒɆӞӷѣǋǁ²ϛżįͰʟ5',
                            'message': 'ϭʯȝęɂʴЀѲƄ˴ĆqǲǇ¡ͰȕƘǺ®ÁʍTɉЙѯӵʝƌʓ',
                            'arguments': [
                                        {
                                                        'name': 'өԠѲOΨҳǗ˚А#ĳoϱ˽˗ɸŸ\x96ɿƢԛŅiʲʀήϷæӀà',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǵ\x85ԏlüȊʐȩˉKǋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'KøĈ˼»ҩŸʴˍðͽϢʸʚϹͻŒǼ\x89ūŨĊΟñȕӸɕԨψś',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98ԢōЦKуӮПѠЬ·ЄœΎÉZôБŀ¢Ȳԝȷϗͼʸʣв\xadȓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 507682.7126776355,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƜǖoǐļǅΞӬΧđ˦ǏàԮФ\x9eǠŨ0¢ў\x92ƯқρІΌʄηŚ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȺʦȳВԚόЯ˧πԛ±Ϋ˔iíƻҴ1ʇЯξîŲΊɞɄϲ¾ȥɾ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˜ұә\x9aʪ\xa0ɛѳɱęЈ˒\x8bМ҂Ĳ½ϵPq҆ˉ¬ŊŷӆʅϏҷm',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾѬÝΣ)ǫŎƽ8ԇǴҳǑˑȓϭĘФѦњ˫ƒ˳ӀâӌȖǭdɉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԈЧҺțŎ6ÿϜɆɒӣηŪ%ШѹөęгŸ˖¼΄ÄƴƋΪΖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒʙЪįʏΏɾňϟ˂ºΧΕŒĹ\x93ɠï˭ȆϩȑĀҾҮǴʊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 321598.0997599654,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƇɵΟ\x81ʰţҏԤюӎʼ\x9cơԂʭǽȚƛÛɾҒɈƐӨѹȪċȟΰї',
                            'message': '+ɚ*ɔɍȃǷүΔƤ\x93Bΐȋň-ǽɝԍ¥£ƱɭķȔͼʳ˰ɒʳ',
                            'arguments': [
                                        {
                                                        'name': 'дϡ΄Ҹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032425.225477:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȬǠτΆҪϳѩɟ\u038dqһȏςīΙŦÅ˱ƏҞǹПʍŕɆǘsҐˏʵ',
                            'message': 'ƻьǀeίýȍϴpЮȴFѤƸӞʴЗԂƚ˷ƾƩëȦвӘHeӣʰ',
                            'arguments': [
                                        {
                                                        'name': 'ŧŚƢŝЗͿĥӵқҖʓҹƏ½ԁЅЀżǻ˯\u038dӜſҀhԖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4987747400219993719,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋаʹƒʾŞͰʉʀƀŚɈДɨљӟϜůԐρǮǹȪмьӚҠNǹӸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 518770.605464539,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛζGŵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8740353781669821594,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԡщĹѥǆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4701957825891994224,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϝ\u0382ĺǦȺɜҐȄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032425.692600:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǿҘÂɆǘʎӠҲʠԙғмӻȘȯѧ\x9bˀŸ©όzЯ\x8eȔқ:˝ҹ\u0382',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -1248.2924198833352,
                                                                        },
                                                    },
                                        {
                                                        'name': 'gȜȟΏɭɱɋʂϲƬѼƐĢȌϥ˧\x84ƫʭ]әʴͲ҂ƻόǢʻ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ĕ˳ҠǸϩғEƆԢӦ\x90\u03a2ƻɪa\u0380йǈȼҊƹʡζӺ\u0379ҏȈƟѕӎ',
                                                                        },
                                                    },
                                        {
                                                        'name': '҇ёԝȆŭƞғɯϲůԔƇȼ÷ȭΙѳU6ԬДȴǂʺɴэNÐƶţ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032426.339614:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'РѲʪÕĪ˧ǏӜѯ˃Ҧ\x9aԖŐҷ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '¨ÑћĦуːԍĠϽɗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 787948.0311685409,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϷҦϣ',
                            'message': 'я˺șɀŻ®ǔ\x98Ŀgнs ´´ĔҕɱʝœѪӸÒäʣĤaѶˮĊ',
                            'arguments': [
                                        {
                                                        'name': 'ҤӍHϩӼʏŦ҉ÿķ҂ʉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032426.585513:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŜƶŌêĜįиǮƅӱʴǻлĦʉțȌɄ|\x99ԟхƵԭЖЍϏƛđŢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Z\x97ʺ\u0383Īѯj?0˟Y®ΧƨĻ?ĀÉӏЊȐϙӣˉ˭ӛſŗŸĭ',
                                                                        },
                                                    },
                                        {
                                                        'name': '҉ѻԞb\x8dǫǈȭiLϢǾƒʑӊŻґČŽϾѿˉƀ˨ϚĀȖåúј',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĈұпƚûΕĭЏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'űȚќ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1765051771944941617,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹǟѨӮÛǸ\x87ǄŃƨȘї',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 625837.5610833635,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ěЦƕřɩӁνΙѬŞ\u0379ĸϨϰƍʣЈ\u0381śȧɡʿƀτϟϖƖǍƠѵ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032427.147462:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƸˢҦχǻŦŵɞƛʏҒӲų\x9e\x97ѕƈ5¼ԘхȶʺǛӠʁǼȵѳψ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "ҖԘΈUѭӔ»ʠ'ɈЬԬȊíÅіGюg¨ϪǔŏĂĕЌĤЁûɶ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŷЦ/ӊŶɔ˛ŁϮӁƇ¤¹\u03a2˜ɖʋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ēlʙ¥ҀΏŹӍάHôѓŻΏ\x85ӈÀǼ\x89ʸʄ®˸ϭфˋԣɗźÑ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƩʻȯtήќВãɴѿϵϪƢȢЦԥˍ˛Јȣ˚ϬˉǀˋƃˁЯʂӀ',
                            'message': 'ʳŘ]ȸ%Ơǧ\x80Οˣ×-±ȅºɷΉƢǚ˛\u038bɝŋϺǓϴԭ˙SF',
                            'arguments': [
                                        {
                                                        'name': 'Êӕϫ}ĒҎʢϘЬϬYÖ\u0379ӻΙʣ˨ϦHÞĨŁĘӉÃɬзűСӀ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƨСʿ÷ԫçAκӰķǥςѳ˂ϒŸцǐʛǮԛ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˳#ůҀ\\ϏóӪΕìǲˉЌɡȣӭŘ˳ΩˊЊ\x89Ʉˏmӌƕư¥ĉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032427.665770:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'û҄ѽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032427.742115:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'àȸƫǺҾϚıgǷN×áφɶӲǁҤʅҽɽҮ\u0380ΔӃԙѷȁΓȝƪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Шʸ\x8eɛϩ7ϛƓʗ˷ǊЖȠрƝÞȖü˕ȃǞϳЫ«ҽÔʝˮʷĭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲ\x97ϼѼĺVˉӫӾÎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "âơĿǮ\x95ą-ǊαѦˤҒļϤxӔԀӃ'Ĳż",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΰӤɻĐѤē¯δμ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '%ɹņѢʾҲʺЪԜѩ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 832749.6594007418,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'οƋʸɝϖδҦǶǹǓǷɡć҇ϑȔk˅ɰƯS¡͵«ѯԪ(ȞԂҫ',
                            'message': '\x90ϭɩϡԬҺҔùӒԅǣŬĞĬǮԑ˼ŐlӶӌϱǂĬŇϿǾ-Бː',
                            'arguments': [
                                        {
                                                        'name': '<ʪüќ˅Җɹϣ\x8aϋǉYLӱǰҶ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ðđȐбɟӎġʳʺ\x86ȅмɞΑʰjʈčƈ҉ϖӝŤȍȦäϯɫýò',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032428.397147:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʊѓɡϏԆҊɧʼѼǊђѾΌӍšέŶ˂Ϗ˽ѪҔūŶ^ʋ\x8b\xaděǙ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ćϼ´ǑҏϢԍæΠ¨СЪόΒΪ¦ˋ ćԜϩǙĬʸΓĄ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƫͱˈ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032428.614347:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'eϦŝѯϾˬƆÜҎƮğѳJϞΆƌķơΚӄďѭƤӋəʨõɸɣȿ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032428.694265:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҫȮĐӫʣʺϜӄʧ8\x9bŇ˂ζˌѶƓł`ƤżɊϦʹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅҵɈҗХјƈZɇ\u0382ÑфϷҩŸǠÛҭ˟ΏYа9¢Ⱥȼ΄ЌĉȐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ø',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'vΠ˙Ì)чqЍʅӄ˟ҝǙӦͲɔĨɂуɐіʅѹʗОΝԊϐq\x84',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '<ŽґĘ\x94҆ĸǻãǼ˻ȮΥ*±ŎǯǺʁȫԪ˼ϤζσÈг9˝ў',
                            'message': 'ԎʿnʘƔӖӢ×ȷğԞΫȴIʡQ¶Ħ\u0380ȺʠЮʦΤΑȧӎ҈˼ǝ',
                            'arguments': [
                                        {
                                                        'name': 'ҚEӞӊȗðəƭѣÑ˸Ӳԁͽ҂БИӯƸϾÒѺǳƞđǅŇφέҋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҃Ϛ°έүȞǣίÆӻɷψ˅υƿȃơ҅ӎƌӐ¹',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3118446898526782167,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ß\x93ηLŕĮʭİ¨ĦЈΐғӽÒȘȉɩ$ӐЭζνʭ˷șԞˣő҈',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'øūĮ÷ӽһͰǳǽϪ®',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚSɲӦňɣͶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɉҙŊѸӂǿΨíаИǉ˅ʈϨģђʞЗȂæͱətʣGÓőэƒƷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ўǧ҉ɹǐ˵ėS˼ʣНҋǺmºϪβĉάӄŌϜϗѷɟϰț',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¨ўԏǾĚˈ¤ʨҴ½˂Ǝ\x93ԕǑãȝɛŰǶŲԍãϾĝƲ:Шƚd',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȢâԦ!ӔȈƩԧ˺ÞϊǶȉ1Py˧ȨҀ\x7fѽ˴ʗɁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3410544933945250243,
                                                                        },
                                                    },
                                        {
                                                        'name': '϶ϽŊ;ÚМɸsÛӵΖŜ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԂϜАîɕӢҒȺ˗ūџҐϹ¥ўткěȋæͶĪҵй˷ȑ˟ɒďƘ',
                            'message': 'ņĆï·ÄǇƚƞ\x9eǒŭΠŀʶӜʟÅўЍɵГєȮԩϿŪˡҝΆǳ',
                            'arguments': [
                                        {
                                                        'name': 'ɼɝ\x87Ōϕ_˻ȐĔ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'җȪΤӋѳĹYңЙцͳҦҰ˥ͳέϑǞʫЉ~ΨҦЅ\x89φ?8φî',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈȱЊįʕҢͺ4ƏѶ÷Ԓ\x8bɕҤӪɖХXԕÃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032430.131430:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˴ʁȸʇҙÓƱƎҬÓƤΆʌνΡɻάЃΤĒqϙɪƚğ`ѴԢ\x82É',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 26687681820043401,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѼMгǻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8990780246578567198,
                                                                        },
                                                    },
                                        {
                                                        'name': '>ҟɭΜMЪΓҬƑςƤÊ`',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'áȰŘ!ѿɒÒ£ʸх˘ԢͳŞ\x95',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҾĶҺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǡћґɖˣΡ˴mɅϳԘɔɳ\x9aŉρjԂΧ¤эĴ\x93ӆȂ˴ƽçɅʂ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐȟěɃǤgƥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǙңŖnъ\xad{Ǯǟ҆ºѧȻСΨŕȌʐό˙nҭԏê(ΝѬџÑη',
                            'message': 'Ү˕ʯůӁΕǹеǫƥƸţǑЛřϗʘȞ˘ʱŸӓƪ®ϧʵȟѓɺÖ',
                            'arguments': [
                                        {
                                                        'name': "ǵzԅ˰ӱ\x93Üͷßòɾζѽ'ϹȡöҨȖĽŚÔ˱Ȉ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΉɛȆƊΘФłɄЪGӀ¿сРЉѩΐÚȀԃŚ\x81ѩ҅˹ȞŬϊΖΟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032430.872646:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'îʿӭґȕҊѮ˦ԞђеȢЉʺϞύүÂɘ˳ЧҋʬԂҲϾ\x87ԎбӼ',
                            'message': 'шѡʧҚԬкӗȥђȣ),\\ɯĳfіϔƇ\x82ǈǣÕȊȱ\u0379Ӷȟ҄њ',
                            'arguments': [
                                        {
                                                        'name': "ʨŞϳЌͰȚĒĒľ\x92б¸ɺ˕ӗӶBϧǖŕ\x8b·´ĸżšӓ4ʴ'",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǟvɅĦǼү',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ëmȣΥίӽ5ϭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -729411372559999978,
                                                                        },
                                                    },
                                        {
                                                        'name': '±ΆѠӠӰʡʧƄ{ÛPɳҿůѫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'әЗ\x95ȚѰʄʋ§ҌǼ§шєӷԣӴΨɍʖʹʴЀʏȐXȸėĕұί',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2976568408163420835,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԥĩȋĺ{åЦϫѡşʲ˷ɵŠsѷR Ǩԋ\x9fŵÑƫĸҫĞӯAα',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 787463.4032692538,
                                                                        },
                                                    },
                                        {
                                                        'name': 'M\x8fdɕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'wYġǳ˫ͷǷӵӢʇ/ȮԧԠdήбѰƬðοѿɺцɰ¹Fćɔ˦',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "Ƅ'ŚЄВɐ¿Κí[\x95ЙP˕ԇ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɐs',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1427693154422805553,
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

            'user_error': {
                'identifier': 'ȥа[Ƥǻ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'Ćӆ',
                            'message': 'е',
                        },
                ],
            },

        },
    ),
]
