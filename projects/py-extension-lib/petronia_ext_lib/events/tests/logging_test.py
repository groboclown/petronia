# GENERATED CODE - DO NOT MODIFY

"""
Tests for the logging module.
Extension petronia.core.protocol.logging, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
            '$': '\u03a2ϔεЗűʁ¬ąAƭȝӋŀ5ÖʞƜŴ\x94ц˛ġ˨ȗŦŝ:хѼø',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 6666879634078298109,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -47235.753196645244,
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
            '$': '20211104:183124.683968:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ӥǟȝŒ0˕ԚʢӿӔͼ˧˅ˈƶ\u0379Ҡ¸ǎҕ0ˋϼƿвӂȯɲȥ¯',
                'ҼуȐҟ\x9fʳϛϕ˳ɞӁÌeþх\x9cßˡҡΟˠφҐʡ\x85\u03a2Ÿ˯јҭ',
                'ПӆѯρѧȱɖҌЕ¡*ӎőɣ\u0381ҳť\x88Tɣ͵Ύ³ƉɂɥƎϾÇɑ',
                'ӚƵӞxӻǲď˔ӡǥĶӑАɨӱұϱѻîȾβȪҞʲȒfҘȄňʑ',
                'ņǉȒѾñԫЪʁřîǶʙ˅ǩӠɤԀȑv\u0379˼кΤͿԟжž˻ДŅ',
                'óбǲŗʄɫѧɸԧzĵ¢Ӗ¹ʅƿԜѩÁϏӇɫθOϗӱuȍб(',
                'ԐǛÐĸɒпѭŞ~ΉYԪʙȱӘҔ\x9aȋǯŃĊ@\u038bБȥƚέҏͿӔ',
                '*ÈɁβ®æ·ǮҍɚÑӪȊЛ±ӌϟˀϿӘĹûǷȅѭ¶\x98ҹ÷ɞ',
                'ҟǣĽàČȀÁƗѺǓНҥɉĉИÅ²Ĵϙз\x82ǥΞů¦ʫåvŵ˚',
                '˄˖-AϟmȀȷяώƪѻʩ˝Ԭо˻ԄӵԏЋɸȹǌ|ģϬEȍʵ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -6399054819712616155,
                -3632263650077596947,
                6121886352213069538,
                6164276342454612614,
                -1897259696602196103,
                1237220078986069906,
                -4741558016282376830,
                -8399649463015021121,
                -2851384897173004672,
                9015318758934524675,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                350426.7732828176,
                431943.856659141,
                43814.90395322128,
                877241.4072899921,
                39285.63860826325,
                245153.54096417245,
                168789.2592168536,
                914613.9497473496,
                113308.25186785473,
                783852.9178461718,
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
                False,
                True,
                True,
                False,
                False,
                True,
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
                '20211104:183125.645995:+0000',
                '20211104:183125.663250:+0000',
                '20211104:183125.680307:+0000',
                '20211104:183125.697526:+0000',
                '20211104:183125.714333:+0000',
                '20211104:183125.731046:+0000',
                '20211104:183125.748459:+0000',
                '20211104:183125.765635:+0000',
                '20211104:183125.788903:+0000',
                '20211104:183125.809700:+0000',
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
            'name': 'ƾäÞƺΥʱӴБѩʞĢќǳѹʂìɴӲЦľі',
            'value': {
                '^': 'string_list',
                '$': [
                    'ξ¸вƺŅϻŉŇǳYìʓԟƚȂƎŷİŜëȍϙHRŖ®ϳ˘ϵÛ',
                    'Ͷ"ȓђϾǳи*Оξ@Ȳ\u0379ͺŢѾɆĭĎѲƗ҃К]ŉĵƦΗʢв',
                    '˛Ц˘4ϴϙ˶үʱ|ǱϏі\x9aίȀϏσӮÝƙԝяǇʗQʷČŨϷ',
                    'Ψїȓͽԇ˭Ӄǭ\x9bͻӒцФΉäˏ\x9bӠЇӣǎĮʅҔƓΙβŧ˶ÿ',
                    '\x9eķŵЕ˯ʡGӵŌƐкħ϶ҙӛҐѲ¹µʬˬƫ҄ЖҜЦſВЍȻ',
                    'ɽŵǦΘȈΛΙɅҾѰѴаϟ˛ʳ\u0380˙ʀУ\x8cΜш\x8bԡøЄđқ¢ԧ',
                    'ƪԇ·Ҙè%ӓ"ҵɋЉżώӡϾȣǢɳɶєȀΙϴҐŤξͺЏűĭ',
                    'џðѾĻӦŘëɭφȻ\x95ˡӛŮҸ\u0378ğ\x8dҾʊěџѷΤĩzώɈʣƎ',
                    'ƥĆÅӶƀìĕ\x87Ý¸źό\x80Цʑ0ùÂҵȹʥ=GȥʢǔǶǟЄτ',
                    'Ⱥu4%д˷Ʀ0ƾ,ҹɮМΖ%±Ąԟёʌзnшԃɖ˹ɩÊɵʿ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ҩ',

            'value': {
                '^': 'int',
                '$': -7252331965475297204,
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
            'catalog': 'ʹcЫϰvʂ˰ÍԮȡćϪ\x93ЍΙǋΫǑͷΩʳȨ\x88ƞƊщŹъФӏ',
            'message': 'ˮх҃уŊɨǦÜƅŶҔɞƼ˴Ҕ<˟Һ˧ВťɨӀԒǲκʪϋƔȊ',
            'arguments': [
                {
                    'name': 'ŸǻŴ\x8bӢŐЃϺȷȱʌɜέӺKˣ³ɰҮǑʃąwFǹʹѾΔ\u038bҸ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        702896.0218233855,
                                        -28785.58221865428,
                                        -15845.814117798102,
                                        814578.4970004491,
                                        571073.250616383,
                                        41204.471628365136,
                                        499937.59545596526,
                                        847619.4718196897,
                                        416554.0179724729,
                                        848220.5244731877,
                                    ],
                        },
                },
                {
                    'name': '\x9cðϒОπѲЧʉЖƉ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20211104:183123.604738:+0000',
                                        '20211104:183123.620826:+0000',
                                        '20211104:183123.637818:+0000',
                                        '20211104:183123.653753:+0000',
                                        '20211104:183123.670027:+0000',
                                        '20211104:183123.686271:+0000',
                                        '20211104:183123.702759:+0000',
                                        '20211104:183123.718622:+0000',
                                        '20211104:183123.734773:+0000',
                                        '20211104:183123.750826:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ČȝŐıӮӈŕƶŐȍŉβΌ´үѱ˭ԉϖʚȺԔӈ',
                    'value': {
                            '^': 'string',
                            '$': '\u0379ɞɧˣ҅ƱʮѡeΚrS÷˴Ǽ?ΆӼͳXѾťқêпӺÐѲÍÄ',
                        },
                },
                {
                    'name': 'ΠҟũǗҋЀЄŊЙŹȅǘϙцƼʵΐȷ˭΅\x9fȯҺǐќЌ >Я˓',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        492863.3410152317,
                                        282220.7590977376,
                                        -42050.154535980946,
                                        792922.0717407556,
                                        113581.45369827954,
                                        195172.38309970062,
                                        265795.62534492806,
                                        -69678.57099466541,
                                        534634.9611620569,
                                        592569.7193890895,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '˧˟',

            'message': 'Ų',

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
            'scope': 'verbose',
            'messages': [
                {
                    'catalog': 'ʥʯӲƘȩƛåĞˋƫõ8ɲʧŷʯêΰÌxƼǤĔiΈѭϑîóƚ',
                    'message': 'oӿȱŷ˜Ѫ\x89чżöѺΡƙ˓ЛÐͺčӋ;ĂԒƜЖñ.ЗҖӮǒ',
                    'arguments': [
                            {
                                        'name': '\u0382ԎϬʬҔ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x92ɘ\x97ҷϦÎǾ÷ǬɩąԭšОŴҳŌÊӁη\x81ԏ\u038d',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 642270.8649835663,
                                                    },
                                    },
                            {
                                        'name': 'Ş¬Ð{³тĦɄȦ˧ƾX>ɚʨÒȲ7Ĩƹ4ǐ˹!εґɄşѷӄ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6922308298236955732,
                                                    },
                                    },
                            {
                                        'name': 'ҵȺWԗĬыđƓϗӳϙөƗλʩɬ\x96ųȴ3ǽȜ\x8bƛƅȊӝɇǴʏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183109.037448:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҽ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x7fM¥¨ΔӇßɌϰӅʭ8ҾΣƋĘʝϞЧ¢ΠóˑϦȝȽ\xadΥңɜ',
                                                    },
                                    },
                            {
                                        'name': 'țĵ\x8fΤɀ¯ӀɚzҤʶɞPȱҚҽϲεơҽȳԪ¹ѫ7T˚ȸʑɇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            726890.7446978102,
                                                                            798469.6934858618,
                                                                            432350.42032908986,
                                                                            302308.2452192934,
                                                                            812037.8903540726,
                                                                            128888.86259909847,
                                                                            189753.32936657453,
                                                                            985411.0906308882,
                                                                            405042.96664308885,
                                                                            50399.29537637459,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Î\xa0ĂѼлȘɶƜΌѪɗò²IŚӹ?˱Ѩ˞ԠÕ*ƻǴʆəŢѦã',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϯʖļƷʶǡʪȮƦ\x9aßĀұұĊϸǶ9ˬȀп\x8cͳϱ\x85˜ŕ);!',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183109.492736:+0000',
                                                    },
                                    },
                            {
                                        'name': 'rϸӼˢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѻ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4618444754742442117,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ѯӛ®ȹ˒ЕȗΜØѱΫӇȑҋƈ˯źʋԖÌцƵˈǢʠҜßͷƎŀ',
                    'message': 'ŦЪǼԟȀВӹӽ¤˔ɩƍĿ΄?ӻƕˑιαǨεFԓӗҷ͵ƾǿȅ',
                    'arguments': [
                            {
                                        'name': 'Ԋ҃wѸxÙв',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '³\x96ȒӱĆԏ\x85Ԡһ˧ЀƢɥțѨÜɫχϮνӘάӁŽҙȿƚʠȽΥ',
                                                                            'ĄɽJљ>ӥƅˆɄɣԡƽѫѫӆmʽѭ\x9fɯǖϥөȔΑԛӤ,е7',
                                                                            'ҭԝˡɠ§ҀíтôӖʟĔˮēКҴКθʦ˓ªĻȘщȶĵͲˋɰ˗',
                                                                            'èΕȔŚӦωvƥϖ\u0383Ͽ6ϺаõǑʯǟƯӢҼΩ҄жÕɣɥԡŏҁ',
                                                                            'Mϴʧ΅ɚԀΠ\x9aĕλCνOϕӥƙŐĻИɇʷͽӬ;ԡҚʑѥĴɈ',
                                                                            'ХƅǇέ˯ˮíΈɬҋŰŭ«œs·Ð˫иƌЯԊΫ^Ģԙ|ɆҮη',
                                                                            'ʱӚбţǱ͵°Ԅɢ¦ѵ+КÑǻΒŴĄТΉʆӘǫĺԕƫ˻ԊŒ΅',
                                                                            'ȼ҂ŕӏҳƝîĳԬͽɥƢόɺҘ\x94ԏT*ſƮΧɼ˼ЉλYϡPĮ',
                                                                            'ԟ@ϖïƮύķ¨Ӛ¯ǴҎş˖źµƞăӿυϕӞҝĻҒőȦɯʔ ',
                                                                            'ɺ®»àśҐÏƫœ\x994ʔɍīĊ#ӧÌɱɆ\x92ЦЛƋVǮÃ.ÊĖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Bкԝ¤ǶƺzӒ]ɁŐŇȩɂĊMϬưĶэӄӹɆž',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѬǫοƱыгԥļÇxďӬǤʑэԭЩϗĜԅÔкϞϣćҡµBφğ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6350337108402998230,
                                                    },
                                    },
                            {
                                        'name': 'ϦÿӗԦʣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'жҼ˥ƪ·ŔǨUR\x8fΊU˾˯ɿ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ØЊn9Ê§ƕƸς˸Ўʕ˺Č\x9bǝΨĞɩʣ\x86ɭǻѣʸ/ȁӎӅ˓',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 156840.16078125342,
                                                    },
                                    },
                            {
                                        'name': 'ɧŪԡˑƈwвƥĠӥЪԌƱÜ\u0379ͼӆļ¹гͷҶӆǓǾϽʳԂΟŒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            704303.8624196403,
                                                                            -40340.207213097965,
                                                                            -31290.45814092495,
                                                                            377165.36746012466,
                                                                            434545.87702689716,
                                                                            115567.3448451219,
                                                                            353333.70311664353,
                                                                            595630.9364697397,
                                                                            625210.733165262,
                                                                            163341.87791575165,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȟ\x9fŬӱāǱĪΧĪ*ŷʘ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': '¢əĜyϴ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6060049176393052799,
                                                                            -7015636081059459404,
                                                                            -7939695708825252239,
                                                                            8004345596481817740,
                                                                            -4273845175316283835,
                                                                            -8392193514031798733,
                                                                            -7544754460286471633,
                                                                            5738872119185421514,
                                                                            -1971142344463442433,
                                                                            -1397866103650912855,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѫɇ˛ĀӈǇÁΐżʫȧàȍкѼKϖŗǌĠƄȶȑПҟǪè\u0382Ĳҕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȲӿɣďҶӾ\x8cԦɃĻYƴʦǔǰΘř˅ü<ȤʠӅѽyʿӟĐ\x94ʏ',
                                                                            'ӤΏͳČ@ɢʦʂĠȜɃǸ϶ĠƗůȅýǑĖЕ˳ȁɍƵɉʜϵ˴´',
                                                                            'Ƈǃ˷óĔÇѷ\x9b˂Ɩĺ3ʞӟ˂ҧγӨδɠԋҒɓġωѷň_ŊС',
                                                                            'ŞKǃҴǤИˀ/ƻÅ¼ңĔ:Š9ʮ·°ˎƯѢ:ИэǚÀ\x8d\x9b\x9c',
                                                                            '΄ŜӫĞҸҊП˰ZƄø-ΏѤ|ѥЂԭǈԌîqęèǕѵơƏŅΩ',
                                                                            'лԃaФΞͱςʺΪǀǳºŽ\x9eɧ»Ҝǆ>҈Ȟ¦ͲʍШӉ,ЯϤГ',
                                                                            '°˺ѨǗϾӄFʻȲǅ»ʾҰʌɌʃǐҽěßԩƐđӜƿǬï\x99\u038dż',
                                                                            'ҾΧ«ӪñǟȈæҳԄJ°ň}ƔçȫġЗѬ˗ǐǝњŦ²үԑrʃ',
                                                                            'Ŝˑ5ˬѠңFЖκă˩ƥҥˤȟnɺċ\u038dʵрΑˤƣÈHŪʖϜǘ',
                                                                            'ɳӾΆѠÎ´ǇӮƨξȏԩ|ҜǋͰʑӮÙęџѽåùɋŕîϕʮЬ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЩȐѭӽЇȟŒ˱ğB©ʟǒv«+ʦʼ\x90ϝĶӥ\x80ͺԩ˳\x88Ԡȱ\x9b',
                    'message': "әƕñȣwѷ\x85ϣԅҤЯ²ѷ'ȘшƋΖґԛʲÉˉϟ§ȗ\u0379ɱȖµ",
                    'arguments': [
                            {
                                        'name': '˛УϢ\x7fɔұρӄɝƖǀǚјː',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7407089973203707721,
                                                                            -4704467671886744662,
                                                                            -4261026690627780546,
                                                                            -3109248712769683308,
                                                                            -8806121596054929815,
                                                                            -4434232926227210000,
                                                                            -7422707103571577617,
                                                                            4435939460186312394,
                                                                            6213183418457468264,
                                                                            5739367746512373966,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʠҍɹH˯äрȥЏҶͼÜùÎeʈǐȰȒʱɌʊƑύχϲʿŷӋҁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'PҫϠҒjĨӵơΕʻ\u038diȋǺаʘǷſҀɈ˻ŶǨҚʨԊ\x9eȚƲǑ',
                                                                            'EǹǐΠ\x98Ǵрȑύεʑ£ǃɬ&ˆɤЫŸʍțÜьπͶ\x81&ѮϸŚ',
                                                                            'äȄfŃůѹб\u0378ȷČƭʹĵêɄý²˻ҟ˜ùŌüƺÊԬόӓѰј',
                                                                            'Ӊǌ˭\u038bŇQʡЁΖеǘ]ĆҭƳüͰơÑßѸΎψ\x9aѩĬȀAʽʚ',
                                                                            'ɿτͶŶɭӤәȤЮXƭҎ¿Ȑ˪ȨXɆÖV4ʙ³\x94У˩Άӌӽs',
                                                                            'ӟ\xa0ʦŽ±ǾWƿĂÇa҇"˪3ȿoʿÍ҂ĸ\x83ӹЦ)Ӝԁ͵˻Ԓ',
                                                                            'ϩʜ°\x8cғÂğѿѹѪɔкϳīӶύ˝ҨӐήҪĿԜIȌ\u0378ԧјïə',
                                                                            "ʐoҔƹʲ4˚ΠƞśρȫӜŻу°=÷;ʝ'·tϚӘӿĺŨӎР",
                                                                            'ӈŘƷĵŖАž£϶\x88ëτǅΘҍƍϟĦƠҴІŹɝɼԌѰҟԧӳa',
                                                                            "ǒ·ÔǜίMҫʬʒƫЈƷЫÇʎɢǂɡӮˎΙӑ·'§FǇǄөȅ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӆԇΊ˯ƇÌƾQ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 349343.5781565055,
                                                    },
                                    },
                            {
                                        'name': 'ˁʉȧê˲ĆшʵĤϙȕʈ͵\x8a"хҢШѰÑӀ˘ԛAʅ\u038dӅ\xa0ЭӘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԮӷϿʊәˌēģҤǌ·ȩàlȦ˩ǄԊô˃҈ӿфѾǲάƥĢŋϵ',
                                                    },
                                    },
                            {
                                        'name': '\u0380ѣΉÄ`\\пʀǘJҬќӶԎƅѺɫpęзɑԥɇ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȁųȇҨŘ·ɣɝĐbɃɫðΛΞЍ\x96ȮЧɄ˩:ǵʿŏˢÞǬЈȱ',
                                                                            'AȩˆжMɔͱћ˽ǱΞɭȂƽǙҵӋӠŦćθӀɢςλŞ-ĨƄƺ',
                                                                            'µҼˍΥӑѧͷƺҁΐ¡Ҝ«\x98Ҩqǥ˯ΆɇҙÄǍҳǮϵÕ0Ўȡ',
                                                                            'ʏʗ˹ӂ`ǚ5ʪƠԣϫÆȃĠ¿·ԮȨǥԬ«ìӕÈХѕʤ\x8aɷʮ',
                                                                            'ЎŦϣƱɧԒśӅˡƇѬ²˄ɧzRƂмĘÝcм*\x9bƒƱǏɟĠҍ',
                                                                            'ȰӽǴɝʀϭǤȕAyƞΊȣǌɰυ\x89M˭ҌΗΐΝǲӟϚɽɠʊԭ',
                                                                            "Ҙΐ\x82ßí'ǞҸƷǡŽ\u0379ЌΘϲ+һ)ȨPϭ¼ɒҦϡńΆϊŀ#",
                                                                            'ϛΙѐΆЇƞ3ȩΞνȏΗʩԦʎΉѽʇѾÛʷʬ˘пʈŴǃǰ˄ą',
                                                                            'ĚͼđŻȃϛёŜϔŗèΕȐuǜý:ˮ˦жѾǉϦ"Ļ\x92θЭо?',
                                                                            'ѩī\x96Κœѧ\x9cà\u0382ͲҨŬѼίҌԑΧRҬσнǰ˽Ņԙӡɪ¨ѭԝ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹȕԦǢɜɀӦùӑKѯԑҰҌғҝϺҹѽi',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 279880.5078251335,
                                                    },
                                    },
                            {
                                        'name': 'ΒӷŀÛм\x96ѸН(ĆЅҕυ©Ӆήќŉ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɚǳƽ^¢ȣӜĵІʂmȃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183112.856514:+0000',
                                                                            '20211104:183112.873442:+0000',
                                                                            '20211104:183112.891354:+0000',
                                                                            '20211104:183112.908117:+0000',
                                                                            '20211104:183112.924774:+0000',
                                                                            '20211104:183112.941461:+0000',
                                                                            '20211104:183112.958296:+0000',
                                                                            '20211104:183112.975048:+0000',
                                                                            '20211104:183112.991341:+0000',
                                                                            '20211104:183113.007745:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɚϚţaRаĩÔä˒ʅ\x9fɹ9ɟŭԜΠ¡ƁѺҮǩűқҞӦĝԟԈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '"ϣϴЇνǡΏөńё˂ϹcȄɀÜγ¹˙×ǬJǁΔȌǏˣΉ\u0378Ԕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2343289282087003123,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'nӇEҎÎˌŇĘҮɍΉԒʢѥғƑbõџɃǴӞύÞÇTǻφĳш',
                    'message': 'Ë\x7fҥΔʵǦѵкоѹȭΦʵѝɠˆɪıѪΊӚӜƻϐԜ^ɘȑuҟ',
                    'arguments': [
                            {
                                        'name': 'κͶϓг\x91ʝ)ˢґcōƇъŠāҜğíШ˯ǌȹɠԢѺŝ¦ԗХԛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʒ¡ѭseҺqӂϡΧ\x8dȋˇǒ˷>\x82ӏϝіѼŸĢӖÿģǑF½Ә',
                                                    },
                                    },
                            {
                                        'name': 'Yϐж\x9fдȲƎЭқԣʑ҅ԥ˭ÌԆȪаǰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¾ҥǣҟǫыŝľѺ,ԚŇДйʃǔӪǲȩŃ°ȄȟԧeɮȤѣѭō',
                                                    },
                                    },
                            {
                                        'name': 'ҔΌȘɡѾ˯ɏƬĒǚ˩ɖȧѨç=ʄҔӇǹԇŽ˞сȺ˛ңƱδύ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            642868.3904293751,
                                                                            767677.7718996353,
                                                                            315638.06363529415,
                                                                            536717.7608505402,
                                                                            652455.6588933007,
                                                                            644438.7838139455,
                                                                            449973.12867346196,
                                                                            124824.46563484729,
                                                                            -38467.30575390341,
                                                                            876761.2774221106,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʊĠϬȈłȿѢĽуèɲϑˍɧешƅ}ƀҘΎʋɤϷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɐƑӵɳМÙơŝЇӯуğѷӏ˷ѵӄŧżԨdɕ\x9bԓĭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183113.746936:+0000',
                                                    },
                                    },
                            {
                                        'name': 'łü҅ŇͲÈѮӆǒ˸Ĉǹǆà\x83įʬǍ[ČèĶŇĎȭʹΜ\x99ȗʀ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ņȟ\u0380ҪћΝ\x94ԋӹîҷЕˇËdӗŦѧ҆Ϥ˜˺ϠѰԦʔȴԣˉя',
                                                    },
                                    },
                            {
                                        'name': 'Þ˯ƉŻŭ9\x85ƮωӮɨҶӔh',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2225644566387101822,
                                                                            -8249535631423852177,
                                                                            7676433066559913004,
                                                                            1725401674043025564,
                                                                            -6665905300268423463,
                                                                            -1141548447265513769,
                                                                            6270958275131867343,
                                                                            -1169845767389402272,
                                                                            -6752547431911845558,
                                                                            -6717825457290838559,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӌ\x99ӺϐȻϞƿɈԥåǹκǢʈЬɽäҮԣԓӠԔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183114.172840:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǻ˒ɺдÂϜҤϋΤɉЪѲƕϺʐ3Ӛ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183114.246273:+0000',
                                                                            '20211104:183114.263839:+0000',
                                                                            '20211104:183114.282475:+0000',
                                                                            '20211104:183114.299931:+0000',
                                                                            '20211104:183114.317609:+0000',
                                                                            '20211104:183114.334915:+0000',
                                                                            '20211104:183114.352084:+0000',
                                                                            '20211104:183114.369044:+0000',
                                                                            '20211104:183114.386226:+0000',
                                                                            '20211104:183114.403195:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'љШ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            939538.7596575723,
                                                                            937369.2980022178,
                                                                            828772.1731327885,
                                                                            338437.6349609258,
                                                                            833386.6423715869,
                                                                            745418.5103655978,
                                                                            406902.8525705826,
                                                                            114319.66199815393,
                                                                            379886.79194568127,
                                                                            51572.50173946866,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʽͲȋҼûӵɢžʸӲԗԨүъ\xa0{ƭƨ˺ƇžʂβЛ!λԤ@˹ǖ',
                    'message': 'ңӸӖÔ1ϮԗNÞġBβɘɉɈԦϡȘЈҬΝɼÉɷɃŸŐλöΜ',
                    'arguments': [
                            {
                                        'name': 'ЄɫҫʃѓǤφ˦ˊѓN',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȫʠΉҘӱˉd&Ȱ˽ϭ>ͻ˚\x9cԃƾϞ±ҲǮɪěɅƥΕѴƵʦ®',
                                                                            'ԋҊМǣͽƲʖԞǹӅʉɬJÓX˻ȓΧңʤ˗ËθŬŸѵɚCâх',
                                                                            'ӳȾЌЁ>ЏãƂČ҂˰ȁƒº+˝ƝXŊ©ʎłƊґɫҐ¹ļΕӆ',
                                                                            'ԨőіϓƟӿҥҜӢɥŸԚS-ζƈǠ˴ɼ@ӛѽʔÿфҽø¯ǷϮ',
                                                                            'ӍŠƗéʢʟԊĨƀʏʲõН7˸ÙϣԉˉҒҐĀʉʥҹӥƃǖPĺ',
                                                                            'ЦpԌɎԇ҄˄ŏ\x95ʝmұʟ$Ȧ|ΈÎӧʦɪÈǥΛҢ,ԤȥkǷ',
                                                                            'ԤϚȄ˘ˠѥâɨţΫͿѦǵǄǜǪÉѰέԪԗʙ]ƤɞŷκϏĹӦ',
                                                                            'ИмìόΝ˥ćÝĖɊȄǊ£рЀâʵўӤɉĐҍʜέȰϘ\u0379ƙϣʿ',
                                                                            "ÚҮӀќΑʬѻǇƞҽεԢɨɂӊ'юšXȶѬǁɤԕҮ@ĐЩ˽ʂ",
                                                                            'ɽǿǵǅŹǭǓ,Ŏ×ĩƔҽȬɬʌƂȅмMıɥ%Τœǂϴǵ¶ȉ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǵцΜ=Ȓ˵ƒÏưўӏЍƄЍ\u0382ϒϭˈ҆#нЗɽP\u0381ӟуԨρ˶',
                    'message': 'ƜƖŢҮЧԄ@ěҕÿ\x8fƦɇȄ`е.NʄϯʡЯʹɛŅέϰԌðƗ',
                    'arguments': [
                            {
                                        'name': 'ԬǧѠѷͶďʉΓҍϒξȟ\x85ǌ\x86ԖԆƌƹѨ\x86ɵƘjӘ^ľћϴɜ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Σ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ћϠǝӛƎŨǲԠÂԌҼѽđĬlɥɿКѫ΄ƥŠѡÃԄʻδˇƹϝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɁŹIǫțԥӜϤȚ#ԍǽpϥύʑȴƩҕȁǻƉŎЃɈƛƥѿӮӻ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183115.480244:+0000',
                                                                            '20211104:183115.497261:+0000',
                                                                            '20211104:183115.514663:+0000',
                                                                            '20211104:183115.531923:+0000',
                                                                            '20211104:183115.548390:+0000',
                                                                            '20211104:183115.565989:+0000',
                                                                            '20211104:183115.583013:+0000',
                                                                            '20211104:183115.599663:+0000',
                                                                            '20211104:183115.617399:+0000',
                                                                            '20211104:183115.634373:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӓӖƔηņэ\x80Ԕϣ¿_ȉĉԂî¤҇ǺԉΈŃʡϦЪ\x96˹ӱ®ƺԒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʑʿǩʀƇӶѕвй©ѝԗLяʭʉϔƍɔã\x9eҏѳƍԪǬÝɡ˒õ',
                                                    },
                                    },
                            {
                                        'name': 'XӥҍЩԇǝǳӵԋғ®˝+ĺʉқ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѼИΤґӒӂƛ0ԄÆ.lɀҎŕҀƦɠжΙʽʀ§-Ӳƚԓ˳ɇŸ',
                                                                            'ҋʸɳƨҚjǁÑœʵ˙Љǜ\x8eɓȏ\x94PÇz\x9eBѾƟ?ƧËҔ˹Ҳ',
                                                                            '9ҕÆÝӲсɗŞɊĀřҼÑЪǔˉǄΫ&ӺӚԂяϢɹˌЪҤËʗ',
                                                                            'ƚάѪĠĳƽӮŦɄ(тɀɰÍԔǮøСÐҲЙήЦџƲzůѵϙß',
                                                                            'Ȁ\x81вƾñӣҡƗыDΛ͵ȦϰΚЦďĸ˰ś΄ǷğТ£АŧҋɏӶ',
                                                                            'ӂwÙѽȁŸӘȨ\xa0ˉ&ƮſϧɑPϒãʑψʳѦ¹ʂ\u03a2Ʀ͵ԏѪƧ',
                                                                            'ʥəȋɕʌιʻɀȰОˬeȻƛǂJŉɃћŁ\x86ŐԘәһЊƞXʼȗ',
                                                                            '\x8aƞ>ԤǂЃ\xad0ˊ˳ǧÂЙɯŬ҆ɓ*ŦҾԘάĴʔǾ\x8dЉϘЋҕ',
                                                                            'ȜƸīͰ3ȸθѓӚ¾ΊűĤѢǝʍŢ«ƏǫϡиëŹ\x9dζҬη~j',
                                                                            'ȹǻƺ\x90çӊůɲсӍIæԎӃ϶ӸȤчϪВ8ǰɔ·ʇϭйƲԗʐ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԠӍȞѮƌpÛˮη\u03a2',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8025878900415412468,
                                                                            -3139609046762126774,
                                                                            -6538814060755543012,
                                                                            5516737975303567972,
                                                                            302351584783553742,
                                                                            -2347987951508788556,
                                                                            -3801467358789968514,
                                                                            -6236358558055249964,
                                                                            -4509933751408438556,
                                                                            -3912384469483393252,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'дɷʈȖѾǬÃȴ\u0381ɮήÍǂƚɬǩД',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 36175.81792075769,
                                                    },
                                    },
                            {
                                        'name': 'ÓƑǉÇʴɘ¼ŌΓØ҃λͽå˵ɥÕϘԌāәӷȅř˙ſ\x94Ӎӎǈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÈҷƊʞ²ˌԩ˺ӡſȟϘ˃ÏħЛŨƙϛˣЅÛԝĲϩɉɈтͶ\xad',
                                                    },
                                    },
                            {
                                        'name': 'Õǋǂm',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƈҬԜӕ·Ё\x82ЌӨѩ`ԗԚΔхғ˵ſȨćǺʶƊàȸ˜Ќɛ¼ԩ',
                                                                            'ʘÑԢРӔґʖğύɻʁsǸΊӧºɛzȑѷи¨җћІ_Ɠɮԓϻ',
                                                                            'Ӎ\x8fƢθȩ˪ϤԨϝАƢġŘ¦\x9eΜʔʎӏӢͶǲԫËɺ´ș\x80Ȇl',
                                                                            'ɃýȀŻÌ˯ΦÓʭȃӢѢƎoҴĞǸġбŅĵӤńͰ˲ΰćԏůΗ',
                                                                            '\x9d\x92ǲѶĎϸǾǙǆ0˂dхϩǱǚțСʢƓƵĹɶǒшЕČĦǗӉ',
                                                                            'ҥǼƉѻɧğӰŜԐ¢OӛɧϔŗԪƲâфǃǉÖϽȝӎVȀXmϗ',
                                                                            'ѸȵƫΒ˘ƒƾӽĺȜƔӱƖůĔ~ͰɚÀ\x8fȿɚAͻʼȆïѤʢ˩',
                                                                            'ɗҫыÿβԦÆæϿƼ˶oūѷɌάȇɕΞԍˉ:ӝҿҽԏȻΚңɀ',
                                                                            'ҚˠΜŸЪ6«ɓw¯ТÔȯɣ¬Ғ\xadŴԉ·©ȫŤӓСʩhҸǵų',
                                                                            'ӷõΝöʄϒҠѸ¡ΏϴƟơʳҡӫòΞϭȒάЎӭ2ϨΈΧлėÏ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ɂ³ʳÉɸҞǠ0˟ɐ҉Ԓ>˔ƦÐąоSũŶ7ѽЗԏƯ8ѽŋ˓',
                    'message': 'ǡāÿÍǇӌҁϏКҔzɽԚԝsӿ^ǣȬӦãɉȲԩԬ\xadúȚŢ¢',
                    'arguments': [
                            {
                                        'name': 'ʲѾԃʜóѰuӾΧwїǩŔӊГʌɤʹй{ĳÃȃL˃ƑϽÁ¶',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ðIƊǪLʸγˢԑͽʮŤԈŌƟњɭҸX',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            791668.5972234904,
                                                                            351891.80146965565,
                                                                            794507.4108649158,
                                                                            -26655.336986829556,
                                                                            219704.32618648728,
                                                                            935537.6110184685,
                                                                            103915.33649435086,
                                                                            688646.6560377924,
                                                                            863097.4126785926,
                                                                            872732.0458109106,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ZО˗˅ЊƅԁӐЅŵʳǒЙӇƛóȈѢƐѳӹĂҙ˳',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӪʒӦļҩҖņɝƇѩ҂\x9eÚζ˶ÅϰԄ\x84©ҽÐǂĿ\x91',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 952866.8243926046,
                                                    },
                                    },
                            {
                                        'name': 'ӣ,',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 16797.56891142769,
                                                    },
                                    },
                            {
                                        'name': 'ǥР\x8aɼǛГÚӣǠėtҋȘȫΞ\x9fΊΠэÅ~\x88ԋԎӓĪŎ»ӓe',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǿǃćsȆЍƫ˶',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7096359550277435357,
                                                                            5634387435986657579,
                                                                            -8916304069300130929,
                                                                            2971660550342367355,
                                                                            7330350641446880825,
                                                                            -4746742598556941564,
                                                                            -2521983250923319244,
                                                                            1776883695322300023,
                                                                            7288249464397017456,
                                                                            -8560700651614736583,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǏȲPαЭÔϤљǟtЂǹÄ_ӷӭĜԚͶɸʘСϼBыιқˀҐ\x92',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 941678.4315104643,
                                                    },
                                    },
                            {
                                        'name': 'ϐɇƪäςԭãÏǆҀѫԌʶѮӡ¸tȦɛʹΊʥʘ\x82˜ʊӄˤȉC',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5841344644343550130,
                                                                            3502609313364393854,
                                                                            -6200305523659362232,
                                                                            1819048174584520201,
                                                                            7089113981708909414,
                                                                            5896336683194541032,
                                                                            -2253552458325654778,
                                                                            5494477796554028062,
                                                                            -1842854665656839781,
                                                                            2859640701809414505,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǖk\x83ŎŵÖȲÞ˗ūk¶ͻюЅYøƆˠâŤŽŦžÇƞϡūǙp',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183118.200905:+0000',
                                                                            '20211104:183118.217742:+0000',
                                                                            '20211104:183118.234573:+0000',
                                                                            '20211104:183118.251421:+0000',
                                                                            '20211104:183118.270674:+0000',
                                                                            '20211104:183118.287896:+0000',
                                                                            '20211104:183118.304735:+0000',
                                                                            '20211104:183118.321829:+0000',
                                                                            '20211104:183118.338750:+0000',
                                                                            '20211104:183118.354713:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˂\x84Ÿпģ,ˣо˷ϟ6ҍCЀ!RϹ\x87(ԗЮԋҭȤʣŜ£´ΜЇ',
                    'message': 'ќӫɃзƥԌΠҁȧр¸ǏˈȚm>ƐϚĴӴȆӻυǜ˽ʺÿЬɜǟ',
                    'arguments': [
                            {
                                        'name': 'ŃҘɲԃдŹЂҮȃΆɜeϴɼɡӡãɇĦȺ¢ɛ)јΒѸÎɸxѡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Y?ʯư˕řƧΥҢĄɊ?ԆʴʊϊҬ¬\x96уȩ˭ŃȷēѩȵϦɏԄ',
                                                    },
                                    },
                            {
                                        'name': 'ĤƷƵΛϼ6ɟþư˨ȤΆǵȌĕÜ\x99ŎÅԩòʾԔ\x93σŸƏҰ®',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ԍҞΦяυłЕą\x80ϡϣϡˡŨʨԖϴɧѠòɂаé',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ӆΰ£ųb˜ϋˤԄġӑK¬'ԌЕўԝ\x9e\u038d\x8bMƾ.ϭиқɑ;˵",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǃϪ¶Ӟ\x92ϬǗҞήҐРΑɯƮю˄åɗѶ˹ѝȜǘɒҴӧʊňüЏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'еУǮЕƉнҼQɢĸѦҡźʚ҄ÏƪǂĵѬ\x85čʖÝʎɹԜҙˀ\x8f',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'МԔϹћ˝əɀưϖπǔήтƓȞЀǬГˠǦѳȿˊʈóΟҦҫȞÌ',
                                                    },
                                    },
                            {
                                        'name': '?ˎʑƙұ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'шŤŢԥӛȕΉιȉƿËķϥүѣåǿɈс\x9cźºĜJƑѷ\x8a҇ʶЧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5192485198351545864,
                                                    },
                                    },
                            {
                                        'name': 'ɷšˀȹŃϿǿӬԊǠӚѫÉғ\u03a2ʘ\x95ΝʭûʈĮ˄еΈCΠțIȫ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7997650890290166971,
                                                    },
                                    },
                            {
                                        'name': 'өƖѩô\x81ˬɩ\x83ƻ´Ȇ$ʎÎȃӔģřǕIƸɬаʑѾƤǿКǦҰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4547842257596043452,
                                                                            -3834430749345343430,
                                                                            3407235103797986788,
                                                                            6586580055877254334,
                                                                            -7920515871004196444,
                                                                            214043662626888442,
                                                                            7047528428853212819,
                                                                            -4410699828549445458,
                                                                            3688768094997079863,
                                                                            -3202897306170497048,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'sɲϮēӰΒϧ¾\x97ǾLνԅ\x9eŉѰʊŖƐґ!ԐǾɫ҅ɗˊK×Ƿ',
                    'message': 'Ğ1>o\x8cgӖлĊƆҫ\x8dҦğѝżϙϻҳҊ˳\x94L¬ЌLƇÝμҺ',
                    'arguments': [
                            {
                                        'name': 'ǶôӪİˁÉϱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183119.982712:+0000',
                                                                            '20211104:183119.999215:+0000',
                                                                            '20211104:183120.016958:+0000',
                                                                            '20211104:183120.033638:+0000',
                                                                            '20211104:183120.049741:+0000',
                                                                            '20211104:183120.066036:+0000',
                                                                            '20211104:183120.082406:+0000',
                                                                            '20211104:183120.099515:+0000',
                                                                            '20211104:183120.117383:+0000',
                                                                            '20211104:183120.133761:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɜƁˮЋǵίιϧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 365604.43811710353,
                                                    },
                                    },
                            {
                                        'name': '\x82˝ǯӈÃƝBЂІюŹҞ҅ȯԈɈӃ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѵѿҤϨϝҐϩǨ\x90ϽƦɈ«ªӬϓȸԚˁͽɢʔ@÷ƀŏȋҍɤщ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': '|X˛ΩњŻыȹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183120.629958:+0000',
                                                                            '20211104:183120.647435:+0000',
                                                                            '20211104:183120.664562:+0000',
                                                                            '20211104:183120.681712:+0000',
                                                                            '20211104:183120.699432:+0000',
                                                                            '20211104:183120.716757:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'θюϦȈͿԆŹϮͲj\x8dόéèģʷʼ¨ĹRƾƄí',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ћѻƧėƔ]ʸř˺ԙӜƴ\x82ʴκǉç¼˘ʳθӑÆйԨƵƎЖȖǤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 686175.0249764703,
                                                    },
                                    },
                            {
                                        'name': 'ȑÕ\x9băȿêÂŵ§\u03a2ε*ҴƣҠ˪ӖŲÂŠɋΧáȍʙʨ˭',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183120.952599:+0000',
                                                                            '20211104:183120.969384:+0000',
                                                                            '20211104:183120.985791:+0000',
                                                                            '20211104:183121.002480:+0000',
                                                                            '20211104:183121.020207:+0000',
                                                                            '20211104:183121.037631:+0000',
                                                                            '20211104:183121.054221:+0000',
                                                                            '20211104:183121.071034:+0000',
                                                                            '20211104:183121.087849:+0000',
                                                                            '20211104:183121.105865:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҃ͷvаžҒԫŰӲӽѺѴӸʷѼ\u03a2ϛ˥ɺǪѢȜȸЙØұƯӼęѱ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 364969.8690868761,
                                                    },
                                    },
                            {
                                        'name': 'γŀƹęҞί>ǂӱ ӸƳċʓµŰ˽Ăų˫ҌΗӒâɊ˱ґϳȓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183121.260398:+0000',
                                                                            '20211104:183121.276928:+0000',
                                                                            '20211104:183121.295121:+0000',
                                                                            '20211104:183121.312552:+0000',
                                                                            '20211104:183121.329553:+0000',
                                                                            '20211104:183121.346168:+0000',
                                                                            '20211104:183121.362514:+0000',
                                                                            '20211104:183121.379547:+0000',
                                                                            '20211104:183121.396552:+0000',
                                                                            '20211104:183121.414089:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˈҷӏɶǐƜ\x8cǈѷ˦ӹԞƉ˳ѸÂχÚɱGǽ\x84ѤǧÅOşhƾƬ',
                    'message': 'ǹǍʙæɿӆƹÿóƹļWŞҥƁШ,ǖ˞ȚʞҡȬ+;ȘɁſӇy',
                    'arguments': [
                            {
                                        'name': 'ģϑǴǺB',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ǹ7ΙѨ϶¿Ӊ,ƓǈÖyɚϿҚϧƔʻˉɄǦĄёʋȫˢ҈Ǔªɂ',
                                                                            "Ϭĉ7?'˃ōɳƩ˸ϟľřѷϾα϶ΙȾϋ.ģÒԬЙ\x86һͿǢŚ",
                                                                            'ŝԂ\u038bƤòШġҕk\x9fȚȵӁˠІ\x81ΖșÖʾ˸ČƐȥǦҞԇƟΚϷ',
                                                                            "Ƥϡԁϟ'˯фƤʶˢХϗˬ\u0378ϯͿȎȗȄȞɔПεӥȰѧƐ\xadκҾ",
                                                                            'Μǥʵ\x8fƤʬēЏԣ˛ťɘȍ˧ēƲˢȡ\x81ǧйɉ<ˈ®ӗú˟ӭѲ',
                                                                            'ҶɋʢͷůԒѤԄ˝Ўԕłԅǟ1ƶҎɖѭхAɑҦӹWȠůǤŗǅ',
                                                                            'зЋUϵҞřȧȮĥȟ˦ȾĸéƖœ£ȻŨсǡӗ7¾јГϯ\x90Ӌȉ',
                                                                            'ʇˮΊҫȽÎʃʩǝaΜÈŵѠpďӜϭѰѸ½ʰƦSńϯƚˡΈʣ',
                                                                            'YϊȦϚęŜ<ǫӨ\x87ˆӭΛΘɹԞǷʟBʯҤ\u038bӯǀԪβʪ\u0380ϛҖ',
                                                                            'ɍ4ǭҭɔ\x8dɞҰǘǩˋƢEűýĨϸȂʟÐɪƇбŵƒ\x7fԪдəț',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЮӜǌЧԨϫ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ωҵ˅ŔǺ>ӎлȯśϟőƕĂԂƅ˵ıːɅΠћhɩʦŒϟɕѭô',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 260873.44846377766,
                                                    },
                                    },
                            {
                                        'name': 'HD˫\x83ɚŨöûӉƧϑ:˚ɳĴʒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183122.142628:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Χ\x89',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183122.211736:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѝWǐѧŋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183122.284359:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ѹǎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 390617.4252708614,
                                                    },
                                    },
                            {
                                        'name': 'ȨϱǢԓЎԦǘ˜ȱσȀùϬǛҬÐåʪєª',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'ǸӹԋžʦĺˎĨӌϨϯɳȹӼȽÄΞȢƬʓԩԢδҘоѸơ\u0378нҹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            516304.6074466413,
                                                                            86783.40523534286,
                                                                            -23024.798020030838,
                                                                            978136.0532329616,
                                                                            -10788.180424189617,
                                                                            797052.0668623662,
                                                                            826406.4774642943,
                                                                            519270.68022324063,
                                                                            117838.07015123914,
                                                                            734053.5779204102,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '®Ē\u0380ɸÙӥ½ÛЦŉÈɫԨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6212245068416385838,
                                                                            -4850753063022701153,
                                                                            -4659255923227954195,
                                                                            -2607974343868983561,
                                                                            -5327435972463765474,
                                                                            5747987870171147951,
                                                                            7905709068853353738,
                                                                            -8529988143093408314,
                                                                            -7156452788100227709,
                                                                            7775224610822993811,
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

            'scope': 'verbose',

            'messages': [
                {
                    'catalog': 'Ȯʞ',
                    'message': 'ϟ',
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
            'identifier': 'ņϷˠǟђЦӌ˜ԍѱįȟƊĺȍPԆByãМŰ_лͷċŮJȒƮ',
            'categories': [
                'access-restriction',
                'access-restriction',
                'internal',
                'configuration',
                'configuration',
                'os',
                'invalid-user-action',
                'os',
                'internal',
                'os',
            ],
            'source': 'ӲìɾҧœƱжЈǳͶ',
            'messages': [
                {
                    'catalog': 'ԉԡĦӦЕʾ\x88҄þɏ\x9d\x85ÌѫġәѽͰǡЫKǼǣҡХѧǱċгś',
                    'message': 'ĢѕŰӡɣơǮϷԑΊʾϭŕЯɖΩѶȷǰқāƨ\x9dƩҴɉĨʭĶϴ',
                    'arguments': [
                            {
                                        'name': 'ĵġ˔s5yϓ;ҚʰԎ\x97ƤүFЧѻͻöȹŖюǱŋƗʏ\x85\x96\u0379˯',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'йԃЅӰĭˑëÔƉȤ\u03a2ŤȉɤԪ\xa0҄φҏˌÛʠæȚǡǀшҩÚƏ',
                                                    },
                                    },
                            {
                                        'name': 'μεĊ-ȒDöC˻ϳʈ҆ʯ¹ǩɋϊǱĹ\u03a2Ǩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 412015.8120124857,
                                                    },
                                    },
                            {
                                        'name': 'ΠȰҖɍȢhƦή\\ЄOŧǷŤ\x9aɔēƂĈɧƪŉҝį\x98ү£ʼԙʆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183134.951686:+0000',
                                                                            '20211104:183134.967686:+0000',
                                                                            '20211104:183134.985002:+0000',
                                                                            '20211104:183135.003828:+0000',
                                                                            '20211104:183135.022944:+0000',
                                                                            '20211104:183135.040217:+0000',
                                                                            '20211104:183135.056653:+0000',
                                                                            '20211104:183135.073183:+0000',
                                                                            '20211104:183135.089489:+0000',
                                                                            '20211104:183135.105752:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȶӰfʲUӭ˅ϿįλäͷԄҪӛѓčśɾ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˱ǑȮȽȩĠӒ҄\x99Ƿϱή͵˛',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            639238.0660659268,
                                                                            733278.150876407,
                                                                            841557.5855041199,
                                                                            105547.20619890236,
                                                                            842231.7100426157,
                                                                            277919.88272403757,
                                                                            962826.6762879346,
                                                                            -88883.31925638704,
                                                                            -43287.575573239075,
                                                                            489563.10832471575,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѩï¤һŲȮǁɯҿƬΟЏÕӶŮƷȱˇӈ\x81ˊľ\u03a2Ξ˟ŮԊЩНõ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӤƑӀʟƈͺŔƾѴЃԕΥ\x9cЃĄΘʌs;ˢұўҍĝĽˎԘϤάΘ',
                                                                            'ЂƲȘѺȺΐčƞƼΞæϞǪǚ_ĉɞȳȘʆɬǽ¢ҞċСϒϻºρ',
                                                                            'ǽφĸɁǾYѕťҊƇ\x9eÖʉȿЭѯɦÅȼ¹ΑԘɎиdдķΟ\x8fʪ',
                                                                            'éΟӅ˯KюԚlґȳ*єȋZ#ΣÐɄΡўϨϬöЦƩԋÆúǣϗ',
                                                                            'WóŅ˒ӮLȃѴ>ӽɇȍÐϣŪǾҔĐЁ\x96ԥƍƁʘĳ˘ёĻԤ\u0381',
                                                                            'ԦЯφɫήрԅҞ˨ȗЀȮӷĴ¬Ӎ\xadϛƋjҟ¢ƸҸа\x87Þњʪȡ',
                                                                            '˫ѩӐǍƞ\x82ʌǌѓОʲĴҏÍϛԘ˗\\ҵb4ŐѠбӖɗф%ß͵',
                                                                            'æҗҬϾƁωҨђЖĠɁĽMVɢąѦĦ°ƨ1ɗЁсCӴӟȄѶƟ',
                                                                            'Ϣ˷гƎ7ǨҴ2ǍŢɈξɖ¬ˉ\x9d3ǢѽÓəЁʧϨҳφʛλƮͳ',
                                                                            '˼убɯövЙİ1ɷ3¬ȤύԪʯˉɎŜ˘ƬϬԜƼˍÑƓΆǌҶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'йɧ_HϐƿƔũαҪǈҡӬʦɫŁƈ҈ǘłҀɽȝŔń˓ǑɵϴД',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3025704515997344817,
                                                                            -2192813533763338076,
                                                                            -5616466826646004107,
                                                                            2653006992639395537,
                                                                            4330463791737341532,
                                                                            -3622496823402014141,
                                                                            -8572592816748864683,
                                                                            6084504243306822912,
                                                                            1033313831209040337,
                                                                            -2596720355762120781,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¸ľџ-&Θ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': '˨ˎȽο1ȁǦ˲ӥĹΧŘȩζԛƝǙԩĩčŵҽјÝōƤӎ]Ƭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8438921471935644184,
                                                                            -1223667635034308848,
                                                                            -3136538561525449966,
                                                                            1084665311951777131,
                                                                            8730271514739804695,
                                                                            7935610181589670523,
                                                                            -5247209229415510946,
                                                                            -5811095758640517152,
                                                                            7943150234930151943,
                                                                            -6150663370804969533,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҫƺѿ±"Κü˒˧јĻĶȖ\'GːĂÇϰȮfΤӎϏЌYЩ%ΥŎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            99878.42360059262,
                                                                            200307.90799592197,
                                                                            907636.0198740812,
                                                                            943189.4476209322,
                                                                            270880.9476812844,
                                                                            494698.5161903009,
                                                                            -61272.793547188056,
                                                                            611342.5080959199,
                                                                            467267.4288418535,
                                                                            994026.3525311481,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЃȰμӻƗAĂ˩ȡċϷÖҀ\x9fƢɞΗĆŅ°ȴξӚ\u0381ǀ҃¥ĶĸƢ',
                    'message': 'aʛŹªԍ˪τЕЁɪʯŃƍǯ\x8bwΐoϵǙcс\xa0ƜӘśпѐΖğ',
                    'arguments': [
                            {
                                        'name': 'Пӑ˗ΑƺǞȦŦѥϻɡCάдуŎӕӺχ\u0378ũ˚ͺŅȱґ\x89ԍľɟ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÆΎѝˌƵɣÜɑҁ$ԋȌѽѧ¾ìѡĎ»ʩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǆͺӑŧȃȈ¤ғĽÚŨӪȰңŏɡȜī`\x99UȴӊđѝɔɄǚŭ;',
                                                    },
                                    },
                            {
                                        'name': 'ƵģЙҴѪѲȹ˦Ǚ˙˛ʏʹҒpԪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҜǒsÄ\x87ԇϲƗҀЋϺêƉҸʩӾͳȠúǍ˒ӺǃɛŅˀ¿҃ŕg',
                                                    },
                                    },
                            {
                                        'name': 'Ǔ\x9dю#MБď\x9fȾǋ˝ˊΆƧÓ\u0383ȢɁϺыͺĭØȏɜɸǘ\x85Ӥj',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183137.219514:+0000',
                                                                            '20211104:183137.236206:+0000',
                                                                            '20211104:183137.253908:+0000',
                                                                            '20211104:183137.270396:+0000',
                                                                            '20211104:183137.288059:+0000',
                                                                            '20211104:183137.305231:+0000',
                                                                            '20211104:183137.325911:+0000',
                                                                            '20211104:183137.346864:+0000',
                                                                            '20211104:183137.365364:+0000',
                                                                            '20211104:183137.385789:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'þʸǇҷԥɀƨΛƐϊЦÆʙÙŉ´9ȨѳʺͰ˰ҕ\x9cЙŀɾΉǴě',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            508208741226480167,
                                                                            8833094540721603876,
                                                                            6934547438966623408,
                                                                            4020423236933656918,
                                                                            5184500575862580402,
                                                                            3521980101406222405,
                                                                            -1722115084679544263,
                                                                            2648425724182775662,
                                                                            -7091764387010944999,
                                                                            8074392389608930442,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԏӰ\x9eіŰȍ\\ųƕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʄ˶ʶû\x97żĿĪȹǑɠõǤʙ˄ˤҲĕђñúӟ\\ԊĈΌӾeĎč',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7281665574183370336,
                                                    },
                                    },
                            {
                                        'name': '΄ӢʆɡëȔ.ξ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7435934020214577275,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƀ\x9c',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            51907.62609749596,
                                                                            343982.00726471836,
                                                                            796796.6974506628,
                                                                            839521.075034966,
                                                                            374475.0762993381,
                                                                            324639.0435686395,
                                                                            975495.1435203885,
                                                                            609086.0661796199,
                                                                            75168.1764615647,
                                                                            82973.84289196826,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '~үϧē˦ÝȤȔϥʤɡ§~юөƀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ԓь[ӫνӬʻŗɲǈΪФ˃JҎΪ\x84ԎΠ>˶ȿҡΛԗơ˞ų˷Ā',
                    'message': 'ӆǋȳϿƯҰ˘ϛ˕=ȑϫǛȆ\x8eʴˏ˸ƟНТӏʗÞɚɬ҇ßIˈ',
                    'arguments': [
                            {
                                        'name': 'ҕʐ_ˬί',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˚ŬӆˣƖԈВЊ˘ȄͷжӣȹȏӚƅƢŲǪƄɵƒ˥ѹˉ΄ϻɢ<',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7747653283098903303,
                                                                            8018110206518154776,
                                                                            -3711513216528280561,
                                                                            5428512022181505244,
                                                                            -6880789338820491581,
                                                                            846926848932492928,
                                                                            -5643812482569754582,
                                                                            6364553927605993570,
                                                                            6061349585617492593,
                                                                            -4694449445012846133,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȭБҲFŚʫƃȳȕΤϝ¿Ɓˋț\x8fφ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 828638.0069837525,
                                                    },
                                    },
                            {
                                        'name': 'ɊŽĕĶΔ˷˵\x7fӘɪÌɯʚƣӯĮψϾОӪΗԑįǫʈрʑĮх',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ăһˑφРҐ5\x9cʉұΤųΟǘʆıҐˇ{ΐԀΚʧϐѾҪƦȍȦЈ',
                    'message': '4ʂєǜ˗aһӢǠȤʭҀԜzĉтЖʪėЏԆșɱʉΐиԃЋȾv',
                    'arguments': [
                            {
                                        'name': '˖˺ϾƑɽĕʘɆĕȼľHSś҆ĺӠыͲ÷ȦΜϪŰɘҟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 788141.1438927494,
                                                    },
                                    },
                            {
                                        'name': 'ϺҋĊʫȀĆȱОyʅʪǉʤȓƹӲˍŌϳCÑ\x97Гǁʢ\u03a2ӹͳŁӾ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183138.917914:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʤӈ˘˥',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183138.995486:+0000',
                                                    },
                                    },
                            {
                                        'name': "ƊȺ'ȼȁÍůż?ЛƎЄ+ǌˌΚÀEώ˗\x94YğťŠйǟɤ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȐĈ˹ŗҢ˟ˠ\x87ĲΐїȨǱÁμҾӐè˄Ҝȉþ˽ԔϝԖВɺҘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            778356.3397102597,
                                                                            475893.7849941056,
                                                                            936345.817643543,
                                                                            174764.23660849093,
                                                                            704554.3630833413,
                                                                            478040.19567583746,
                                                                            134062.85072145742,
                                                                            463221.0629961357,
                                                                            964802.5739445109,
                                                                            890519.9102682589,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'UƃМȐʅîӧк΅Ļǀ]Ύ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 229898.24804399878,
                                                    },
                                    },
                            {
                                        'name': 'ŻĘˍʊǅӅԭǨ˖ćʂǄĊűĀŴ¶ıԦғ¯ģΰϑӷ¾ʩѐæѶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ӓ<ŖBԅǟĖўĥΩϗ\x95ȭɞʅʯ҉ŭ®Ť¹Ȝмӻʁȏͳӳĩɰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǅɤlԍĢӳΞJϩƔƷOĴȬҺǯơ˰Ήfȡɳɍ/˞ɱśζ\x86ß',
                                                    },
                                    },
                            {
                                        'name': 'ƓԒʓ˹ш!˽$źˬӫ\x8cɏʡͷКԫǡġғ˄ҹԐŃĝӘgΨѿơ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 158045.04604017248,
                                                    },
                                    },
                            {
                                        'name': 'Ϗ}ˤϕ˦ǠӒǱυ˒яĔПҽҸƢŲҦŦѸɩ:ʯαΰ2ӬҰϷ˭',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3661050222947984847,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʜʴĴԦφĜLǋēѪʅΕΏ6&Ż˵ɚ\x90ƀђҪǵǷ\u0380ȢFŹΥӦ',
                    'message': 'ѢĺѥϑŉԏүЃҲ҆˲ŷαϥҤĂÜeƶŌӖ˂\u038dǧȎȹęӎǅǾ',
                    'arguments': [
                            {
                                        'name': 'ϕ2άˣϝԦӍЙǧЇʊìë',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɍΪ\x89ǖŐ\x87ζϞʩ˾ȗň\x8fˆѶЋ$ɡ¨ϚӉō˨ÁųĻқӼŉϭ',
                                                                            'БǄϽ×ԤĴȚϖ˝ȫυÿɽX ŝčάӨϢǷ(ïҝҖȍȘЩŚѮ',
                                                                            'ϼħǚǮƛÕŦʁ\u038dƉʾЛƂ£\x81iƬϞȮwġɽ\x8f˫ɺ˥Cџλɛ',
                                                                            'ƞĩʑƧӯӇϧ°ŷ~ɣɣ1yȼħáĎϰǈǍԂƫҐҊǮ£E˦ɋ',
                                                                            '˸˲>χɹ˪ҝƭ˴M҃ˁӨɦ\x87ʒ\x94ћɷǈĈʨν˱OĿԈŏǃɠ',
                                                                            'oĲı\x8dőӌĻ4ӕĩɪʀΩɂϪýөǰǏӕґ9ϩ#ҎūǂƮÛк',
                                                                            'Ѡ˶ɖɣȔƚϵψԗԄ˱@ʡʻԏĊӉȊĺԫž˸ðӲȱ\x91ȴ˩g5',
                                                                            'ҒǴģȰʸʚˈûʈ3ɼ¿ɷhӰǕƢ˧³ѹζҪʻƖӣɵҰқѩ\x86',
                                                                            "ȃǜǎŚ˖'ҮҙƤκԊ0ɞӰǣƗÍџЂЃϔӌƇӼϽοπҍ\u038dΗ",
                                                                            'ЦoʹŞǀӈʖԘèҗȼƴÉ\x82ȻƲˡnӅơͰĩǊɟ˥jɏԊɐН',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ċθΖȨɮƙǖĉʑnuGӒˈNӕҞԇ˜',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1497124087470698984,
                                                                            -236018381920656466,
                                                                            449653490912998628,
                                                                            6255060798438961940,
                                                                            -1628963873536864055,
                                                                            2111276564154415563,
                                                                            -3976662528775006844,
                                                                            -7903546094773897260,
                                                                            -909774330391925326,
                                                                            7596306769411991611,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǉ\x84ʸԐҎϓǫ\x92ԐƢЂɣƋɒϝЏ¿гɿ˟ĕ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            129582.45296722659,
                                                                            957660.6781008525,
                                                                            737777.00223314,
                                                                            -71658.43092193932,
                                                                            51623.60640057767,
                                                                            449638.314944973,
                                                                            584947.4740738197,
                                                                            283229.26989419066,
                                                                            693355.6375417953,
                                                                            648478.1454149187,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӾӢҿӠåҦϬËń°ƭχƀӆҫӠɢťΏӎń',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183140.638469:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӁӖѮ΄ӔχΛķãɗюК',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 283138.35280114075,
                                                    },
                                    },
                            {
                                        'name': ']&ӚӋʿėɩʣΑϵϺѻǮȦóŭÛѸԭɝ&ώȐԩǸE˱ӽʶӹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183140.777017:+0000',
                                                    },
                                    },
                            {
                                        'name': '4ĎԟӨs',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 24368170112029411,
                                                    },
                                    },
                            {
                                        'name': 'ˤɉǟ\x8aƵBГΞɶϢσƾ¼е˴sǹɏĨfΦĄɳδƜӽŠзӡń',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƝǩǉŴ˜\u0380ԢƯůćσӭƚР1ƫʱŷǜлʿӆưȄсҘˉŇ˹ɜ',
                                                                            "ʝǫƬĕ×ѡӕΆʉόԠεɇҶӼĔɸξ'њŘοӣΪАȸĒIϳȗ",
                                                                            'θýѶҙтêʷˊ¨ǈ˺ǧкĀɃ(ǥ˜ԤˠǣҬ҆ĠκĭƃӤȐŮ',
                                                                            'źƧ±ЍзӢӛѭńѓ(ˁǢǥԊɨƒ(˳º3ϪņѥǪʔµϏˋ҅',
                                                                            'āɅͺ˞ӎʠɐɏҧŋȵ\x86±³ΆQŏǮǒŽѶЖЁʛΨ\x91ǥԬҽԉ',
                                                                            'ЌʛШʓȪҝѧȁфҢͷêςˉĵÃNͽ+ɱϮɨȝʤҦƥ¿ƴǗƎ',
                                                                            'ˑǈ˸ЏԛɨǬȷļ͵vɽˆ\x94ҰѶʰɔǏύ˟ԫӛͻ҃ӷΫCªз',
                                                                            'ǹͶƄ+ӂҾȹƠнγÁsʄ6Ʈ\x8d±уĨŇРϥɟˊΎUȎӼƏʄ',
                                                                            'əEğSȑϓÈŜǛΘϱŧU҇ĆŜоoƆƴǵį˅ЇˀƍԬğӧʩ',
                                                                            '\x9eΐ§ÀɱƺЧˣԗԤɩňƠcļ4ƞϲΥˀżҭӎÊήʞķԠҌʍ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѠӕbȭǱDӠγҰǨҲYΧ҈',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ш҇ȫŹˡʸϪˁӵвǨȳȳñ҃ʧϢΪϨУɸє˰ƿԦιǎ\x81ªă',
                                                    },
                                    },
                            {
                                        'name': 'ɌҸɃюӹMҲPё',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϸƶȋ\\^íôĔθ˗ÏɍȸΣŰưƁÉÄπЧqƤѾˋɝњÇɲȳ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ļɔ˕Ƕ˴ѢuӚʁƣО?ϹÂӅɮŚʖ/ǫԊѽɫšȔƠǧWǋ·',
                    'message': 'TʲȘơ?ÄϒúʎΟѸʊʾϓʍKЪďЃ¾ԏ҅śӀӛ|ǝʏз˶',
                    'arguments': [
                            {
                                        'name': 'ѱǼ\x90ѻĐӪĀˊ\x91',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183141.404962:+0000',
                                                                            '20211104:183141.421303:+0000',
                                                                            '20211104:183141.437334:+0000',
                                                                            '20211104:183141.454796:+0000',
                                                                            '20211104:183141.471185:+0000',
                                                                            '20211104:183141.487395:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ';Ʀ\x9aԘ˅Ѳ8ԏ˜ϬΔӖL˷ƞżп\xa0ǳӭѮļԑЎͼȜЖŃĝƱ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƭŢԝ˱ѕˍːӫѳЬКgǵщńŤ\x88!ўʛР',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8aӲҶҴƤ6Пʛțʮˎ£SΤԋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɩӠƣϗżīȧãԙϹǥȣšŨϓѬĖϬ҄ѵШԔα(Ϥяfѫ\u038dɊ',
                                                    },
                                    },
                            {
                                        'name': 'ԗĈǪȘƅ[ПπԜе˲ŲȏɊӡïы²ȋҖʋѾňȥǶZԮ¦Ǿɒ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3568622261115225786,
                                                                            3117207568913922320,
                                                                            3101246768283130958,
                                                                            6603356037333790031,
                                                                            -3912841427136202846,
                                                                            162216553403829516,
                                                                            -6471451843007542321,
                                                                            4548284127687225597,
                                                                            8071209526940310052,
                                                                            -4765966562886158469,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŔЪВԚҭѾǃίƚğό·ӆԄòĔþƋæ¬ȎɍÄɜЩСϰǢҫſ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            415337.9154430263,
                                                                            265063.71934507514,
                                                                            -27564.201370950395,
                                                                            960553.5488493307,
                                                                            -98291.03036579206,
                                                                            883269.0956918399,
                                                                            -29455.531433638622,
                                                                            320678.8997353546,
                                                                            960749.5179163618,
                                                                            319079.8043640735,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'DϢʹӛĭϯşg˵ƤȾɹǄƙӿ#^ΨӮѤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7590036855232985897,
                                                                            772144312593155452,
                                                                            3483216743292270698,
                                                                            -4451797821767128598,
                                                                            5221957507460738132,
                                                                            5631994393551220591,
                                                                            6249278880068825173,
                                                                            -6135001799581535968,
                                                                            8715129697067901255,
                                                                            -1390877917470019902,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "Φʛ\x8bұͲӸɀ'ɖ˅ʶТϨˁļŖԍԃOɐÆ¾ʘùϲɲƙ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʔҖǠʗ§ķȧӾʻˠǛΙГVϧ\x93ĝӈҽҟҡɫåȒзњ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:183142.554907:+0000',
                                                                            '20211104:183142.571235:+0000',
                                                                            '20211104:183142.588099:+0000',
                                                                            '20211104:183142.605434:+0000',
                                                                            '20211104:183142.622526:+0000',
                                                                            '20211104:183142.639052:+0000',
                                                                            '20211104:183142.655849:+0000',
                                                                            '20211104:183142.673532:+0000',
                                                                            '20211104:183142.690906:+0000',
                                                                            '20211104:183142.709445:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƯŝȽΊԛЅ˩ΠȏìӒź˧ȻŝʢŬ˭дϛѴϟź˨ϕ8ɜǩɪʹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'µĔԃ͵ʜȌ*Ɋ\x94ѥɮφЖŒǷΡ϶ϰѲ¦ƤÈÓ\x8cώ·җԒƄЃ',
                    'message': 'ɿƼҊόϳȖѲЇϠĢ°ΰDƹƗǫԝƎԤŁ˪ΥѻřŧŮÑҠTÂ',
                    'arguments': [
                            {
                                        'name': '-',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 48659.77612574736,
                                                    },
                                    },
                            {
                                        'name': 'ԃðŸΕ\x99ІŻơÄ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ϛҽś',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183143.071747:+0000',
                                                    },
                                    },
                            {
                                        'name': '°ηҭӚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            393596.9225274203,
                                                                            123468.18529166435,
                                                                            841793.368320802,
                                                                            906273.6643653571,
                                                                            -10981.8712537159,
                                                                            179342.39751534938,
                                                                            -43028.88325255413,
                                                                            989537.8911677445,
                                                                            269330.0199818802,
                                                                            203507.7545991168,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŒҘӦʻԡɾϻ\u0378żȋǄǮҕźĈɨʸЁɅȨɌѝʲɣԟΈɤѰγҋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183143.401453:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ђƸĺȋʹΔȂƫԛԟƩ˲τÝɓɽǺæʈѯȘ˥ƺƛĢxΏÜϡԎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            52016.4733470857,
                                                                            84639.25121176706,
                                                                            931654.644940845,
                                                                            141926.2031110871,
                                                                            403498.7896751333,
                                                                            743699.5257915609,
                                                                            668980.774036565,
                                                                            213094.51354544255,
                                                                            374830.4835414883,
                                                                            944566.6204116183,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƚ\x8dЇͽң%,ǚǶPϠӊΊ#ƠǜŞҌǄϞȑԍǀВϓǯЅӄʘϤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3607563766409138741,
                                                                            5071011375932289722,
                                                                            -7261296130554197306,
                                                                            6715640441905001893,
                                                                            4398668053381462082,
                                                                            -612619748545094264,
                                                                            4230430238785498348,
                                                                            -5715397530307721698,
                                                                            -38230522564491453,
                                                                            4196766716110274551,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǅӣǲį\u0383ɣɌŅϲ%ӤѢ΄ĿӍҖŧϋԫͳν\xadsȹӶ-¯ˢɤʷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÞǩǍнӸ\x83Ƹϯ¨ǦŮ\u038dʐϨ¿Ґо_áЭДƜϞԂęԧƢ7Ƕˈ',
                                                    },
                                    },
                            {
                                        'name': ')ɃϦĨҾƉΛǃŜ!ЛġԋӞџÌԚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҥɼ¡ȶțə˒Ê҈1ƽǪȌԊ\x92îÜŕǺˮǼǐǺäŶΝԜeąà',
                                                    },
                                    },
                            {
                                        'name': 'ʲғȩΔ?ӗӫƼН\x84ϮϒÅäӵƱϳѶй\x8c6Ӛ ɼɗʍĔ\u03a2ÐŰ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -82768.4342629225,
                                                                            770067.5878402569,
                                                                            533970.6778029354,
                                                                            -33111.53066104335,
                                                                            806047.3524654928,
                                                                            137997.31854044797,
                                                                            132663.52041763274,
                                                                            281486.43611476856,
                                                                            671772.2923037937,
                                                                            -15352.468807168203,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӫʑè\x7fŸδθĉóιeӼȥΈ\x8fΑғҟҐĠёʁǭƧƜԄɊȨ"7',
                    'message': 'ӮϵѼŇӏ\u0383«ӉŐǹƖΦȧƍǯТɢĝϴäzќ҅ӢɸƵѪӋ΅Ʀ',
                    'arguments': [
                            {
                                        'name': 'ϡÎз"ԑŀӹǒʑԣ΄Ǝň\u038dԑĮҪ\x85ͼÔȮť϶ӲϞŭǴĻԗ`',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183144.493678:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӿɖϱƹғԥӾƉ\xadτӌӆŊѼ¡Ĥ\x81ȳêmˆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183144.560955:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĹųåԕȬΊȌθʘɟТ˙ӡȓӏŖXƁĉÓҨŧ\x96ԟЄƠЫ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѱЛɱ\x97јÀǉԅʔρёԟӶҽ˴ӟűλβĂɎ0ˉɐҡϺϺȨʋЌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x96÷ҁӆǌƆϨΕøŖʺƍԃʮϚŨIȍƉƍȞʮʃ¤сƊǃʙǗǪ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Γ\x9fθˊɽѩ\x90ѢƕӎɎĬ;ŸɍӢѥâҶɧХДɳϖŻŰʷOØZ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8509569202434203828,
                                                    },
                                    },
                            {
                                        'name': 'ʆϖөiýʶϼЬпƜâƌēɎ˩ΈȇпSӁgȫξŢKӝvtƒТ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԄҊɲĐûӷĲδÞјԍ\x9fҚă˕Ӿȿη˙˺ѱ҈ӬȮϦЙȖ;ϣʡ',
                    'message': 'ɮñɻņˋΏƖτʠȅo˦ЖƑȝǤǫ^ʑàȐŸɶȝIҰӀɞҢʦ',
                    'arguments': [
                            {
                                        'name': 'ʿâΌϞњǔʵɍӢȝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 238977.50060291984,
                                                    },
                                    },
                            {
                                        'name': 'ҧӁǎϜzӁŶôӧњşǐφʢčơӦӄӝǔȹԓԍωӾӆѨʭʩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĨɩӃʹʲ˓DȜãԔʫƁºÒĞуѿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˀɂſǛōѵȺԉ¯Ԍ¹҃͵ѡʚщŢ}Ή÷Ϯǖȴʷ¥ӨӪÄӴϦ',
                                                                            'ԒŤ\u0378ѥą4Ȥ\x876ťGơȎԉȯ¾ԩā\u038dBƛΆяӎʹȈª҃ơǺ',
                                                                            'ϭǜU·Ɣјҫʁ˽Ǵωɼ\x9e\x9cĚˡҧɶćɇа\x84ѶʇҴʝӃɘ\u03a2\x8f',
                                                                            'ŝ\x80ʞўРŬ;PƟƾ\u0378ӜRӋÓɇ΅ӵʛʴ1ΚҟӪԜʠǓƧф)',
                                                                            'ƟˆMΘϋ·ŇÅѩʑˮЏhʬς˹˞ӥϊ˴ҲHϴȋѿϹъAɪ0',
                                                                            ')ϺƒΤ\x86гGʾıɎĄҨǒɯ¨\x9cęҖЫɩȺʀdɥĞ˄ʫŨƧy',
                                                                            'ÉʈԦсϸԥƏϚŽ^Пө¥ȱŷҢȗʭʓқЍàƔȑ˹{Śĝϳю',
                                                                            'ŝкӝԡɞįǄӿɷɭšʗӗˎКςлЍĎ˜ԆÈǼɹϪĞǷҼ҄Ƶ',
                                                                            'ƖȱˈĂÒ¼òʆ`\x9aяΘԨҘόƉЮяɧǓȊқõәťîƓɏϔǏ',
                                                                            'ˊĂÁǖƛģћ¼éØóŪĚˮСŻġpˢwɂФљˏńȾ7¯ȜĴ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x93ˍԞWӏδʿǓʻɮŮΑыoĲǿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            447556.27264121687,
                                                                            -92296.91049274047,
                                                                            363137.2511106624,
                                                                            365237.9145507334,
                                                                            76511.3913909407,
                                                                            194663.59135354025,
                                                                            459259.9510899454,
                                                                            -61670.92204521456,
                                                                            244039.93585655332,
                                                                            320621.79627644445,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱȸύӞªŖӽšбMԤбȾ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x81\x94ҝdͽ\x87ͼѴΪԄԠʑ\x9a ϵĈɹӑĄĊĤӯʘυȮΌĘͽʓɍ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЬL\x87ˉ\u0380ÚϖҹȂɬԋ\x81ΛΤіƘƿşѓԏîƥ͵ǏΫ˲˭ҽɆș',
                    'message': 'ӬɯsƇѧȇҒÄβÚƇѣƕηГ϶ћǩ\x9cΫΖДӣ´ǠİŻǈĞӰ',
                    'arguments': [
                            {
                                        'name': 'Æɸ҂é\x91ΒåьЂȀơӔ҄ĚԠǋӃó!Ȧŝ©îЌӁÈɇ\x97ªϾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3478629589614560570,
                                                                            -6516597639267685582,
                                                                            3233743483457563337,
                                                                            4853334864460198005,
                                                                            -1283304125275315816,
                                                                            7000151876491168592,
                                                                            -6174414051765003836,
                                                                            3870611409476419921,
                                                                            -3619377122915735892,
                                                                            -3573966664881629782,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɘҼƍξн',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            999204.3343063004,
                                                                            603412.6369047973,
                                                                            481321.30341914657,
                                                                            393702.4502724374,
                                                                            131967.93062104814,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'čÎɋλӋөʪɜБΫǯҸ!ЩŉįѼχǮϢѹƭđ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɞ˂ΝЈąΤŋnȉȜʍӔӮɐ|҅Ŋ\u038bӷʊԩ¼\u0382ѯĎgƲλǍą',
                                                    },
                                    },
                            {
                                        'name': '^όΚǟŗΒԒʱқϣĦψΙΟ^άбɲѾͶϽʺζӥȔi\x97ȴʐX',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183146.617412:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x9baМÎ\x81ϑƍĲȹόɹƖΡËůƛrʺ˥ӅӡӔȜ\x96ŐȩʔȘЬѲ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:183146.683034:+0000',
                                                    },
                                    },
                            {
                                        'name': '4\x92',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038bˡќ˄ïЋϼˀ҅QѽϱŶĂ˺Ȫć҉ŷʕÍѥƥΓMϦΌȥͽŐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 202967.56467560184,
                                                    },
                                    },
                            {
                                        'name': '\u0382˘МCɚҌƏŃѥďȨ˷.ďőɪq\u038dźÖνčνɵ\x7fЯԝ\x9a˴Ά',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 151132.08297787778,
                                                    },
                                    },
                            {
                                        'name': 'ÌÖъȡȉʤ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2372187330639388836,
                                                    },
                                    },
                            {
                                        'name': 'ѭŚҮѧЧ˸ǘ.íƉʗ҃ӽҒϸˣŧõӭжɘ\x7fɆɎ®ԧÞǥɛŇ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
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

            'identifier': 'ƃμʵƚҌ',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'Ȯĥ',
                    'message': 'Ϧ',
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
                'identifier': 'ҮǥɚѾӋŋξʊʁbřΌҖÎϟƏѬϗѹм\x89˵φǧ˫ϏԠя˦ɗ',
                'categories': [
                    'file',
                    'access-restriction',
                    'network',
                    'file',
                    'os',
                    'configuration',
                    'configuration',
                    'network',
                    'configuration',
                    'internal',
                ],
                'source': 'ϭìӵǦĆѱӿƑØ=ɉЙ˾ɄѴǶ˟ξΞʂƉňǍλ²ʅϯơʻы',
                'messages': [
                    {
                            'catalog': 'ҮîɇѦƷʏʛϑҭϨ!źɍҐê˟пŪєˋǀӀaѪрŏĚθ¶ŀ',
                            'message': 'ƔʨSОɼӸԦӿҡδ˦/ɠ¨Өʅ»âê˹˦ʁɲ˼d˳ԝŊÕ΅',
                            'arguments': [
                                        {
                                                        'name': 'ˀĒϤʕ}ȒϳǊˣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '<ѕ˯Я˽ԭʉʋўϧsԠӝLφȓƁʗǖƊӭџҼҲϨǷӉӤˏė',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'eȷ,ȀʊԨАÛӘĭǵúLăbǮ_Ύ˃k˨ƔɿĤіŉλʹƯı',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƥȝʼ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӛԑЌȭЭҭQӠʮɘl',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŀм.ǟÈɹǿ»Ҕž',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȩÍµȢʆƽɞ\x83ʗЊФʙԮҕҳɁ\x95ҋн˖ˍxЀůȓ\x96ΪщϦӷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮȘÙɹǣͲĀЫƭSҥǛŢ˦ȳ?ʓǧȺűșλÙʢ˶ĳ}ɟ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʧϪÌƀĸȰʀч\x8fĶЖę.ѥȩǄÇǨЙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 250142.93638259132,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'έq\x9cǵǀΜҾďΈBÉ΄I϶ĿӼƳŨåУΕÃђҫúмʚҐӟˏ',
                            'message': 'ǦѪΤÓҍǸԛԘÓɟYǧŢÞ\x97ҟұʎҌΦʺήÖF͵ĞҘԑ\x83Ϲ',
                            'arguments': [
                                        {
                                                        'name': 'ŞØӯǛ҂uˑơ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 621215.7294178252,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύҵčƉǕú1ǭӘű҂єȴӊĕĝǒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'өĀ£ψȽцϜұ×ҫŊХӭĻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8025506326909324621,
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ǅμʌʗ~ѳϜʃΞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ƝЎ\u0383ɻΡRťʩ˰ɇĺéμҌŎưδѥӨǃƋ'ʣӪӄѥ˂ʓ-}",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'jˀIԂͽţӶĒgʘҏƦɷ×IƭγzH',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183127.516363:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˖àƭʊĆЍѺшβƷΪmϝӉĚҨ«æҮŮɃƈȈʒǼȁϬѥϋѰ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2157944356442495044,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƹ¡ŝÚӡсGÖЁдŢı',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƒǟėæ:ϘƈƇĠǿҧԆÖˀEӟɚ"ͱыɼ°ϗќђѧɡґēӼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŗÚˈЪԮ4дʹыΗǗΞΤÊ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183127.787071:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'δ4¡Ϸз˛"ЌҕƴXÝҷӝǷҰѶƘȿДȠǈÞԕϾº',
                            'message': 'ЋѿΡ˸Ĕҟ\x8aɨ\x95ҩKT˔ķƜΩҡĊъâҮ҈ЕѯБ3ɨ\x8e҃Ч',
                            'arguments': [
                                        {
                                                        'name': 'ƺƐϙЄúԇŋĆĲL',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183127.935849:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍŒ\x92ÛГϙМȗϧÄԈ¼6ȹ2kɳŵΎxҁĠĽДӱфӎǅΔǍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9aĐҎȓNʃџ\x96ĽhƛɑĽ>ÖжķŜҫҭƽϳʠЌШЗɯΪ;Ќ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'еҺǌƬòҍŉÃŁ˒Ή҃ʹӔ\u038bɰ˒\x7fΥĉȿϊƋΚ˫NɾĚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 260685.1754020754,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Η\x92ʂǯҏͱүơŶa˩ʂӏђΝnңͼĮǻʯΨПʷΟƣƬɟȼǤ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'rбŊ\x98âӉюγѵӹѢҼѾˍӎэǁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЍơμɓŠ\x9dȄ\u0381Øο~ʼMĖ÷p7ºѳϡ˚ɏӋŠɆǝéґ˷ɠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЗЙĠʟҘůǅ ʉşҵлԑʽė\x90ǟе˃ҭ\x93ɴΏØǾȶµ^Рӊ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183128.352026:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐ#ʲbԕʠҀɟ\x8fфкƴƟДϒԆо\x81ӟȇʘѷ{ưȡήϚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dυΠý\x9eûřρȳʶ½Ԛâӣ˪\x90ȐӶзɟӚőӊyʳRFӜ½ȇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 650954.0928505927,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝΩ\x8eϦЕӺxʥ»ҩΑƀƆ=ӫ҆ɊƸƅѣ˼9ɓȣӼȊ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183128.567285:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĜĲҨ˃ƦЅϫҳʖʧǡŧˌǍ\x8b|ƴȖѹ˷ƒΰǡвΫǮĲ˯ӳ§',
                            'message': 'ήфҲtИл»ƻ҉πʏɶɪĥȶжɮǔҩéɧˈʽ\u03a2љϐſҞϧc',
                            'arguments': [
                                        {
                                                        'name': 'Ϊ]УҸϥ8wΖЄÒƉƪВʹλӱѡӁhѳ\x9bȾ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 78488.6698438923,
                                                                        },
                                                    },
                                        {
                                                        'name': 'НƖ¿ɣɽҩ^ВϪҊ\x84åҤfĿɰɊqԁ\x91ӷǥɯɡǯδ\x89ɌŤȒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183128.786465:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӣ¼ǃȶҲȷ\u038bůˆђѯ»Ĳǐ´ҚżҽƳ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183128.859927:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȟ˕+ψˇϤ6ǇȞí§ơȿƧŇѳϜĝǪӬȡĄµј¬Ҍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЫťӺх\u0378˱ҤҏԩźŶșưǗTͽҙˑѴɔĆʒГÑя1˴m0F',
                                                                        },
                                                    },
                                        {
                                                        'name': 'с¡˕rʑЏūΓҗFƒȌÆ҆ΎпɎϫˋӠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183128.995347:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӌϑ͵ԢĮȜŚɢ`χцԧÚǸ/àŌʕ²ȝ˗ҽƑʎǤĩʢ¼ԉĚ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5440779482705134845,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x85˓ƥΟŔȦʜѫ˧ҖλʓȗϒMĮиΝѓNmŋbƅԉϘÄyï²',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 108905.65879963845,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŗ˝?',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԠҬҡЀĨÆԤǾǴΨΊưϽ_',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '0˸Ÿǟʸɤ\x81\x9dǶɁƲˇɖ,Ú\x90дҹхӏͱʑ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183129.330382:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '+С¢ƫʱ˛PˮϤɁӪʿӶҕǊ˪ЍԋƸы˄ΌѺȤ\x86ɈҳӃʊƌ',
                            'message': 'qǆˬǨκȡĐƦҔғǍϔԖϱʬɰҕćƇёѹĵȚͱϳφʕòÿ)',
                            'arguments': [
                                        {
                                                        'name': 'ӊ±ϭćȜԔϒѭӸӨɛCǫĂΦWϖΤȯĊУľ˯ʞΡΠʑ˥Rӊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'юˇϏ¢ƘŒϿΎω϶àӸӌμҜάƈӅɣЅΕÊɆƟħƔǌԁŮh',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁǎÇɔпÂĦϷ˄ɿû˗ʬҬЍά',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 179297.97619777423,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЯӢsŗǒÇԒ³Ї\x95ƬɥӰѲӚɩ\x89ӸώólӲʕӁřǆɮϔƧ\x90',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђәǻĎς¼҃ϸɏӑ\x93¢ԡ˅DΧnÛЌѯ\xadƄ˻ѥăǹŲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86ɀÇȁΣӨϕǱTΕǡЯºӓ½ŔӒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183129.823046:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЉĢҌʟҞɭёσн϶ƨϭԋɚЉЩ?ӟєũɄӜӗЗѩԓƸˈ\x7fŖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӰʠԍҾȤʾʓȦĦ1«ƂΗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'kĶôψÔxӤ0´˳ΕƂϚǂÞρĲζӥҵʰƫЎθʭȎbɞ˼÷',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 882373.1219950606,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϸ\\ύʄŹȹ\x8cѨbǚƧӎ÷ʯŉƞþ8ιƯӁË\u03a2іԍíÜȧеȳ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '҇ŪӨҝʘ˛ȓL¹ˈɹŔЄȋʭķӼƈϯ˽ʞγҊѾɬҧˀǮσț',
                            'message': 'ӾϼЗ˶ĔÇ˩ЁÕЗėȊȱθhĪФôάƋʼ\x8aźčɳԭȳqҪɘ',
                            'arguments': [
                                        {
                                                        'name': 'sЁеϋȗɢǓ˫ĚΌҨ1ƤʿϟŝĽ×ĈġǾɯȧϢҹ©ň\u038bˑA',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1716252388356149792,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ªĝљ\xadƋǥǾφӦīųƁɁãϏӔ±˷ѧѧϧОƘX˳Ȭɩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʛsӽҨлΖǘŸΈɽρɻŒΠ˵ȪɣƁàŮЅȏз\x8eϤдɧ҅ғѿ',
                                                                        },
                                                    },
                                        {
                                                        'name': "&ʒǳѺȾŬƺУаɒ'ӚVǻΦ\x9dʊ ƪԞ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѸӶȳƳĚɅR\x8apӃ˕YϒɴАΙыˮȊ¤ˆϋ˯',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 27423.63844248718,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x91ēiδ\xadԧϙԩ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'τԜħ˝Đκӈ˟ƶÙҠ\x92ȫɼƿГȥǊνЫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183130.586537:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԈҽȼŊʰɌ϶өɫНƴϯňϾԩӀϔŸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183130.686970:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ХɷďĪ;ZтɤΙЖ˛Ǉȏvɴηзǥ͵'ԟ/ρӢŷȏȿɯˊϹ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʦŢĂǈȋqԝɫїҊƸΣǈ\x9b¤óѫȯ\x9eКǴƯǗϑԫҡ\x9c¢ȶӍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖ\x7fȒΤвØƷҗŅцÛǰĩ˚άΫBŏ\x9aΈХżӢĎßĜŪά',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҹѲʘǤƩO˨n\x8dƗɕĤȼƟèɲäТżΑȲ\u0382ŭȘ˫ΏÎΨэɷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʖωȥʘЛд\x99ѩň',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183130.899685:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u038bźĵУȶȸ\x7fʫӇҤʈĚӴǲǱϤμмҚƸÍͿçϡϰȽ\x87βΒҢ',
                            'message': '˖ÇğԠЫΉ#ǭȝΑľˋ˞ǨʨίƃƥΪѝǲӭȻʵґĨǯƢӶϓ',
                            'arguments': [
                                        {
                                                        'name': 'ʓhĬ˦ˀќʺĘɥʂҐ¿ӾɄɓ\u0383Ɓȷҡɞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯϒȷ҇ӈ\x96ӟ]ƐҿĨКƫƔÉƇѧͱƺæ¦Α˽ƘǵĸɑϔϬԈ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183131.108109:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӸƺōĸȹѽαrȤʧȪʤ6ʏŵ\x9bâȞȽďҎӻĘʚáӀɮÙΦӵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "ŵȘåþҘкӵ'ԅƆԂư\u0382Ãįǻ1ĵmϓуǻƧǯǅɑ|ɉˈͰ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183131.249246:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲɊȗ\u03a2ƇШԟcӝɽʒŵ\u0382Ϣɂȋ\xadđƵ;(ȾѦɦδ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5628470462006749678,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Όȏ_˵\u0380ŝaɎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x88ơɯèѩӄ˹ʙĊʌǬЎӇγѽíΞӈŃǩŻжѬέƹЌǝóΒ¬',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'YԄдʠԇЁÏśΎãoӞɨԞŮGҫ˸ɌZ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏļȕ/³ҩЏҟmƜεΰɗƆŪΞȄӥϺʵО¬IjϲӅ¶ҿØȑ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183131.591497:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'җаȻĎɭǝ҆А<',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183131.658864:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'MϘӤAԜү˒\x80ª_ҏŉ\x90ʤƵɒȻþ ơЃҜ]ΒŶɕ\x9cΚσˉ',
                            'message': 'Ҟ¸ӗˤʉћʂȉOɅģϖɡ=ʱȯ˚ʱϊđǢΏ˦ȵƧɤŦ҄ϤӬ',
                            'arguments': [
                                        {
                                                        'name': 'ȲϦʒĥďăЗƕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɗɩѠĢ\x96ÎFĴ)ŐԦƪʑԤξ\x9a.nϐƯӬŨ˛',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 298533.35633423,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ιӎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ěýИСĦҳ˲ȴѩʝJ`Ľ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʼȣwǱʻЦ˜ƣ˟ɌȑƯĘөѽҵҔҺϱ"ȧӸɍͻĂůѡɾԃE',
                                                                        },
                                                    },
                                        {
                                                        'name': 'gʚһϊӎԁҍҤɻʢδǼ;tǀӰЊ<Ť˶ĊΟԐҸǂΕƲЮҳO',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѵʻŚíM\u0379Œӱ\u038dɔʄԐˉȴșϦҎʁ÷',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǮǺÇΰлҳĤΏԞêѼʉˉσӌγǄɠzӪԘˈϥó',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȐΣÅŴƛϮȱʽǟȯΌņҷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0380ˡ#;ȵărʦşМȦ˝7˥˻фԅ?',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0380ǿ7uŵѡЖʇȹ!«\x97Ќ˜ůÇŁȸ˖şў)ǕÙ˒ӂƴԭтʫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7252458598091086038,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'уԎдDԅф,ѼʥʿцѩѩҶӛәθņƋ҇Ĕԙź;ɋӲДϒӴ\x84',
                            'message': 'ЮǦɞӞϦʖԇϺƤԖøõȫӀкӶȩĄ\x83Ҫ˻Ԛ\x98ьӉƠ£~Ӡȹ',
                            'arguments': [
                                        {
                                                        'name': ')ĭˇ˺ɸȃ[˼~˯ʳðƃ¢ͽǑ1Ûé',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'џӮʇΥξNϞѴЍʺвĝđ˞Ü\x97',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 762523.9998380066,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϦǾѳ°ӘÐǾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'єӁ\\ȼĎ;ΏƺԖԣѪ·ԦŃ¹ǙÑуɝӼřѩ]ś@ǳŉƃő\u038d',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁÐύϑȲǓ\x84\x80ȮҮůòбͿѽϻӮĀњ5ҙͱɥËêŠϜ+ɧд',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƐΛѮȚ¼.ĔθȘȱѩӇȌƚƙɏƻǻʡЀ˒ƛýɏƓǺ½ѧҳϷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˡеˆʇŹˮÌѵӔшϗЂӥɐǯɂʸŕΚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˥ʚοиʩÀíҨɬǝāӞǜ6¾σǃż͵ǈƊİ\x89җȪȧÅɑˈ\x86',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183132.942780:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӮԋΙÞσҳΆƭӅľϠÄƕßqȪщĐŒ˭ХƓƵγɖуӾΤTȂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÃƱUǧΦ\u038dІҁνψɯ\u038dŁ˨ӝВԅˤƅΆ;-\x96\x8bůNɾ%¡',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƪѾČƖɜ\x9dˆ½ԣľĹӯ_çԨЍѿжɀäʕȽ҆ҟʑͻӯ}ϗӜ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 403974.30843560584,
                                                                        },
                                                    },
                                        {
                                                        'name': '˙ѻ҆˩ʈ˝ɣӜԅӽȻЇ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ϼƐѦ\x8eЍөϭ˂˗˥ŘĮŇä'ЊͺƂξӭήˤФXЌÓϗ˄ʡÑ",
                            'message': 'ťʡZнŀnсԊȸχɥПɵʑˏȜϏzѻĸgèӬԎʤŵϚЍҷ҉',
                            'arguments': [
                                        {
                                                        'name': 'Ɵrə҂ƞ\x8dïӐԗϼȢѴȾјˮǌԠʛĥҩҩƪ\x8eǿĥίƠȖΩL',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6883134702828288970,
                                                                        },
                                                    },
                                        {
                                                        'name': '˰ҾДoөԐˠΈƖǪфмƢѵˢ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻӲϟƸԚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'φӚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЕǍȓҬȭ;ƥˀӰψƁɝѪŲӉ҉\x9eқ˼ȢьԄǛˡƾΛʓЗҌæ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦƦοěǇıѮ\u0378ψΊˈµɺĴѱ¦ɌƙӵҶʣЎԡν+ɗƏνͽȼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 838211.5385931134,
                                                                        },
                                                    },
                                        {
                                                        'name': 'þцǆĢʉόϘΑ˄ɉʉÒˉǭίҔӊԔˏȼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ψΉҙƕɗϭҼѱ\u0381ɟȹéǝԞDҜЦYѹȓAʯĆýӨДҐŋԙŌ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӺĬżƬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'љІ\x82ӏȋȉ˄ŋđˏҕȮɁ]ǡӈ£TįЛǵУ,àµç',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝȢѨīÜɶÅѶ˛Εφ˪ĬĪü²Ǭ˨˼ÝŁKaаɪрhϿÖϵ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183133.958502:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌʹȫĄӰ҃ԮԜЏĴԃϓӖӫçɼЂвsSӀţϻÁʫQ¸ӕǮƖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 352849.2591804928,
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
                'identifier': 'GβæĿΔ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': '˨ɞ',
                            'message': 'φ',
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
                'identifier': 'ɚΦĚĒτЦʟöԜӄƓŖϋŖɬЖˀƨЪұҧǥԘʂҊƳоȪŖё',
                'categories': [
                    'os',
                    'configuration',
                    'configuration',
                    'file',
                    'access-restriction',
                    'internal',
                    'os',
                    'invalid-user-action',
                    'file',
                    'access-restriction',
                ],
                'source': 'Ŏfɷɰ˳âѿąȧţԪтɤҝőӍοϽбȨ½В@mͺŔҏǢɡĎ',
                'messages': [
                    {
                            'catalog': 'ԟǅαǡ˚ȗώŋӫԪĳӃʱǞҗ˘ήʹƑćƯƘ\x9d\x8cн˧\x9fʒ˽ʋ',
                            'message': 'ԐԇΩǄЁ«ˣ҈¦ӿƬÆ·҅ÅϖƔȓĽǲuɝƠӉŨФɉҗĎd',
                            'arguments': [
                                        {
                                                        'name': 'Ѳ\x88ȐϺϓϗпȹϚʽǕŽʓéӡӝǶʘ҃˺ѣċsðїƟņӷť',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5369266903433784159,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЎθƙşöçϧӝӎӫѷȘŤjίрƄЙ ҉ӹԦȺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷ\x83\u03a2ԪƒԊŘϑͷЈ˕ĂъкʈʖɧɟԍТǈΓ2Dǒ¦',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 764381.7494028021,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǎʿʗ°!ěэʛkȚԈӃѩyɱҙȪ˥ίȪgʺʫ˷;ȉ2ʥ}Ȭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3610169894362062091,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͼ\x97ΞѰ\x9bΦӪGқρɤĄ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ń',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƷƾΓһțɧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΤKĕƟ˷ӬưĘŶƳ\u03a2\x9bʚ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5474059127896381200,
                                                                        },
                                                    },
                                        {
                                                        'name': '˗ѩ˵ɊʣȌӑŅƪM cƷʾȝР\x8cƒιͲȷȺЀfӊsƅǐŢƭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉϩ~,ȬƮңîˤԀÏǩȹˤƅӺˇȷѧǟɜǁöȢŏȟô',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŧǰǎѲʝɡƢ',
                            'message': 'ɵϵуS\x8fҌƟ˪ŕ҇ҡʑҢĊ˗ʜǑAêМϤ\x9fÿҢƭǉǸҟҩƂ',
                            'arguments': [
                                        {
                                                        'name': 'ƮҗЈŔr@ãұǙĠŸŋѯɈŷ²ӍѕƃǹύԡµƯŖ\x94ʉĽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȫӓΨǗVˤ¦Ρ\u0383',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'тўєԤɡʅĶÔɌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǉͻȓÆνӁʎǝжϯǫЃЕҖѼÑHӆȦϿ ќҤВ\x82Т˥',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9aκҴԋƍįͽРѰӶɚ˪Ǣ2ēИĊÎʡŔϑǈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂ"Ӆh',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӆǟłӂɵύԡǣό˙ǯǇďˈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 375967.70158041955,
                                                                        },
                                                    },
                                        {
                                                        'name': 'йԟ}ƸԝvаˠƹǄģȤɹԇЍӭΣҴԂ\x88İδɦˤϨ÷3йѥ%',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4590159775399253415,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÑʸȩôAȍƶĭӫҋǝҁ´ϿņĮʀӀӸԤǅïԔ\x99ϣźƮȶԍk',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'â*ӹ-¡ҧҁıӿѠŒ¶ϸѠɨ©ҏĒǒζǃґҡƁ\x87˦ǝÚъΈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԫŷӘˑ¥ǑѧҾͶpƤƣ÷ŇТԙòъĹϤʠ˟ŜңєƲ΄зЗͿ',
                            'message': 'ӋʳȃįáӾXȅͿ6GÃшʹĽŶɷ{\x91чºбҢîȐԝДĽ˧Ҟ',
                            'arguments': [
                                        {
                                                        'name': 'ǿͽӃĬɋŅ`ŴŚγXƄ\x8féĮɊћʏŭʺtԛЩÏƄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183149.342057:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɍ±˘ƶ¹˷ϧʧѼļ9PɪyӇąʄ\x9buŕĆ\x89ȋ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϏӢӓȫ.Ƒŵ3҇\x9dϻɇӊļº\u0381ѕφҹUԁҧыŕђɮ,ƙʒӻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƲѓɎįʣĥӲşѺmĪġӈˆҰǯίǯM\x8fѨӏʺʯnę\x84ȭҡѷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9f\x9eɡ)ԫС÷ɓ˔\x90ЦĆ˸\x85ϰЇŦ¤ӑą˨σͺϞyϴ)ȄƥQ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183149.625246:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'щÎɯό#˾ÙŘЭůΓͶȫ\x90ң',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˧ҫăɍʮЅĮ\x97ЃƷÊϠǧԮѷҕʤʉKɢğǥqȳѐįӶΕȬĢ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183149.755801:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȧѠÌΕρε',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 289752.0952157199,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȢĥɸǉȐОѦ:ĞýºгȫƔ]ʳҙǸĶ˙ӇҤ÷ԞsӜΝ˛ȼҏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183149.915327:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵіƜ¥˛ƃUɞˋҖʹĸʪť6',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˯ŢGʻvȧ6ˋĕʙĸȖǏϰΑΑҔBɫœȯˎʹϺȚβϒԙ¿ŉ',
                            'message': 'ǜӢԦщĚǋЦ\x8fӟŨÔ˼ɌԢЬʑƲ°ĥҒ·ά҉ϮΖ,ȵѝλƣ',
                            'arguments': [
                                        {
                                                        'name': 'ȭX\xad·ІФɄßӮҍʩ£\x9fǒÊǻɻìʼĨȞǑȚĜҜΖ҆ϼϿ˄',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'pʙʭϩҟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɩȬ˲BЃҕ÷ҘɲτŧӵҳáΚʅƈɑĆнęиŐԫȍˑͽ˶gÝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 59831.85761465074,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ė\x9cǦ~ǟϦƳǙeĲȀɥŮӸɝ¼\u0382ϼ¸ȩ϶ʿŸϙƏѫǔɗÐÐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˔ӴɉÛʓϼӲѤǝҘѤҫ¼ÝһǫҠԌ\x83ҿ·@φǓë\xadȈȮԮȩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183150.507824:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ζјşŇԖӳϘÞԆ˜ĘνǏʷȁζӰ»˨ɻ¼',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 480359.21669575805,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˑĺҙЬĚωǞʂ@ϓȔ˗Ӎͼǉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'юǄ˺҃ԤÈ˗ԋӷȯůŕēӽ¿ĪӼѶÂkƋǁΣЪβˈԣѪŕ\x95',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦõһïџИɇǖѬ°ӓĠҪΐӁÙɾӵ˥нӼҹʛς϶ύžȀȢ˘',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183150.712132:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӼƊÅ\u0378˾ѓȖŲ\x91šʖµµXΟ\x9bŴùҵűԁ£ĻϰʞƑΔ˥\x90Ŝ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƞŧǐģӾɷˆƃκYŻϝȔ˾şԗćԩƊΊϟӷԌɺϚyԕŉǥѯ',
                            'message': "řтkòΜ҅\x9bƖԈÍʊ˳ϴƞŐǡҫǫňˡѥɺ'ȩŐ?ɡӤĔҜ",
                            'arguments': [
                                        {
                                                        'name': '΄ˣ\u0378ɏþơӭͿ҇ʉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "҅ʎĠȵɲ˨bƜЂǼüΕΘˢңШϡџÆ¡ťҋƔZϙ'ś¤Ĉѻ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǽ;ҩʒ)śɐИ\x9aQpäΎ,η6ʃ@ãˌɜ҇ǁƻ\x9a#¶Àԍў',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6512267277631846551,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɈԆĤɤɭĨ²ͺĹѥǣǄǡǤƞ҄БҲũӵ?πΜӅɘӏѷ˓мԞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:183151.086626:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҕșƍѝ=ßȃȶǜ_',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ьԞ\x94ύ˲ϯźӒ£Ǹ˫ϥʔԍάљԥ˒ˊǎɷǘɼwÍŎϵбėʽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'lǗǮԝϖ*ӟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86ȵ˪iԬѐћƔǞ\u038bЪљȖӝԗȎжҴҹǞӾöԍťΠ',
                                                        'value': {
                                                                            '^': 'int_list',
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

            'user_error': {
                'identifier': 'ʜ\xadƨrӯ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'àś',
                            'message': 'Ƨ',
                        },
                ],
            },

        },
    ),
]
