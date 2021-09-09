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
            '$': 'ĞͲщЏhȲR\x88ͺ¸ЯɤѫħΈ˃ȭĦ˟0ȂψĤÂɓӏԜ¨М\x86',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 4256027438390958898,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 70876.32697164366,
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
            '$': '20210909:201553.972160:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǟBëJȊÑϲyԟѤɹõ˃ҝҶĬɒҁ\x87¹dģҎ˻γϿЛӜǌd',
                'ǲΛŝŪɃΥгσΫӔƙЮЩΧϋȫǡʶƐƼ˦ȵ¨ӵӪiťϛκҽ',
                '˺ӛǭ˰ɼʪǦԁēőƀȳǌƇØ¡ӹ\u0382ШøǺҠʳѝҞРιŰӱÑ',
                'ł,ɑ˂ʓ2ϯ\x84Ǉђ΅ϝҝϥƟѩμɌŲˀѸōÅƲϴȖγɑˇĖ',
                'Ѿ(ΤǶΛVȿǩϛͽɵ²ðƞ˩Ǒ¢ƭ\x8eÖιқɌσѲѽğǜëІ',
                'ĕɥ@Ҵ#ĬҦЪȱ\x93ÕӱӣѰ\x8bȩҹƅҷ:ӛ\x90ѣǀ\x85ш£ƝĆƪ',
                'тђɰʉʱƜªԣҀƖҵŐ¡Πƚɱɨ˪ƹϞɰŋȁΝċxQ˅ԧɑ',
                'ӿƨҌʈƔæȍϠòВŁғêʧЉѰ˰wƻѧƓĨĊæy\x83"\u038dǏğ',
                'ơӿÓ75ҺĜɽȎҚƼѴȎfЂӦӮЮˌäjҀԬū˧ӐπЕӪΰ',
                'Aȕ¶ÇħçҴ\x84ȼ÷ǒ΅ɽɐåïɥ˰=βœѕü9ƴɒʕʡPʼ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                5366631866112059219,
                -2863244689275383498,
                4015736139815218171,
                -7898917891102076424,
                7602492864437540558,
                -650004604871282429,
                -4424318385931096910,
                8269686458497705316,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                706850.5677274243,
                638224.9930832775,
                -11672.687475271217,
                10776.811771061242,
                639105.7507333623,
                490408.530023384,
                -8572.956801900596,
                921736.3604159271,
                46184.65694783858,
                -94424.49067108642,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                False,
                True,
                True,
                False,
                True,
                True,
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
                '20210909:201554.870239:+0000',
                '20210909:201554.887142:+0000',
                '20210909:201554.903893:+0000',
                '20210909:201554.920560:+0000',
                '20210909:201554.936282:+0000',
                '20210909:201554.951975:+0000',
                '20210909:201554.970250:+0000',
                '20210909:201554.988358:+0000',
                '20210909:201555.003951:+0000',
                '20210909:201555.029384:+0000',
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
            'name': 'ǻ·βγǙǃ\x95ҳ°ÏțσВ=ȠǐqČŖaɕѲǚХŐрÿȎǡΧ',
            'value': {
                '^': 'string',
                '$': 'ɌͶΓÜӵЉǃȰѤɻϽ\x9e¬лӘ¶ÄƌȈȄÇÙʐ΅Ώѩκʦǻ˝',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'J',

            'value': {
                '^': 'bool_list',
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
            'catalog': 'ԁ#ľĆˀұѸʉˮ\x91҂ʪ°Î\x95çϻˢǍÞͶԪ˳ѽźͽɣ\x8eʻҘ',
            'message': 'ɷҠÉÇу\u0378>\x9dԮԘɡΆиDΫǛɩĂ|ʨхʱĥűʟԌù·ĳĳ',
            'arguments': [
                {
                    'name': 'Sӳɚ\x81ɦěΓѺƖƸa°»YÍҧͼˀүȞԛŸʃӥԐ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:201552.407875:+0000',
                        },
                },
                {
                    'name': 'ўưӮ\xad',
                    'value': {
                            '^': 'string',
                            '$': 'ӍʴĭʽаxωԨ!?ʪɳϢǽʖϛʹЗП\x9eВėĐDҼ˜Ńɓ˪a',
                        },
                },
                {
                    'name': 'ÖëӰǿȄјf·ȪˏъӡРǖϫʗǩƴȯǩˎʥӣ\x84þïȃ\x91κ˫',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ΉĀΖʻʠʖҎѶ',
                    'value': {
                            '^': 'float',
                            '$': 131379.69097442942,
                        },
                },
                {
                    'name': '-Ƅñ϶ԝͷßЕʴӏ\x9fīƣѝϷʽȯȖȯ;ɒȵԭɏŗƍƂĹ˵Љ',
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
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ѿͲҀƽćĵϓӏƇ0ͷA\x99ӬʯƺǀȤËʹ˘ʥЕʓԂѫƦ\x88',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:201552.911178:+0000',
                        },
                },
                {
                    'name': 'ĤˤҸÔē\x9aӎɜμD\x97ӹ¹ǉѰɩϊϒʯ˶ƫƣƦåŗϽ}Ώчѕ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210909:201552.987147:+0000',
                                        '20210909:201553.005645:+0000',
                                        '20210909:201553.023041:+0000',
                                        '20210909:201553.040703:+0000',
                                        '20210909:201553.058050:+0000',
                                        '20210909:201553.074725:+0000',
                                        '20210909:201553.092789:+0000',
                                        '20210909:201553.109840:+0000',
                                        '20210909:201553.135514:+0000',
                                        '20210909:201553.155441:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ƮɳùʁǣǺ\x81ĨɕҮƬӄӰӉϠÐ:җ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        8044887173624652073,
                                        3866867768658963780,
                                        -7147775996040471097,
                                        -4561764838418926078,
                                        -7750068314430676034,
                                        -6825541052682796001,
                                        -7267267321094138553,
                                        633444451852249844,
                                        7942995336838346841,
                                        -4141689888112881923,
                                    ],
                        },
                },
                {
                    'name': 'ťɯ»ƀѣ\x98Ϻ˯ӛǁиaˉʷӻÏĖɣƑŻǉĲәðӥïǸ\x86˃ц',
                    'value': {
                            '^': 'int',
                            '$': -1974646537962303971,
                        },
                },
                {
                    'name': 'ϲö',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ĠΊ',

            'message': 'ԟ',

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
                    'catalog': 'Ѥ\x98мŰϣưƆόЕє\u0381˄ѭ~ΤҢȀɡγҤɯьĆʇČÆËʴҮϭ',
                    'message': 'γͲ˚˼ˁ%ȨкŹʽ¹˾ǎҋх:ǒ`Јȅλ ҙɲӾΞʘ҄ȷӋ',
                    'arguments': [
                            {
                                        'name': 'ώrȑћűŶҹѠ»ƞԞΛѾΞрϡŷéeǙӾ\x888',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 903764.1561793607,
                                                    },
                                    },
                            {
                                        'name': 'у%űļļģȕͱ˃',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɍϐ˜Ƥ˻ǖ¥ŨǴҊŀñеςɜσ˦ŴΏѲϰxӀяǨĺ1ќХң',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 872506.6229790903,
                                                    },
                                    },
                            {
                                        'name': 'ǍÐĽΗΝ@ɋŜƳɋϲѠCǕʙȉуӨFŁȑЅѣԀώ\x7fƒ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȍ÷ѝǋùΈътΠӌîʈѻӍʓǫïƨ\u038dȮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ĩж¤˷БМɡϟŘĒǫɋğQƵјdγĩƸеǥ.ӘҢNÖɺЖƦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201537.598475:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ą',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            238557.8700079717,
                                                                            406957.0085090013,
                                                                            27731.353598279835,
                                                                            645839.9580533445,
                                                                            403219.8512546262,
                                                                            133220.57809295075,
                                                                            41137.07502348049,
                                                                            274947.2368581254,
                                                                            436391.47111856844,
                                                                            832208.3959015587,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԒǾɁıʬΧѭѦȂ@ȴɠ¿ӄ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʮȿĭʘϥѬŶ˛ҢѳӮԂ9',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201538.156437:+0000',
                                                                            '20210909:201538.175222:+0000',
                                                                            '20210909:201538.191825:+0000',
                                                                            '20210909:201538.208807:+0000',
                                                                            '20210909:201538.225431:+0000',
                                                                            '20210909:201538.243411:+0000',
                                                                            '20210909:201538.260055:+0000',
                                                                            '20210909:201538.277749:+0000',
                                                                            '20210909:201538.295532:+0000',
                                                                            '20210909:201538.312265:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĥ҅ĔӋo\x84Хƽt\u03a2ųȎɗ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            79175.8403855967,
                                                                            9556.359276571326,
                                                                            717177.4793336606,
                                                                            98989.07319251716,
                                                                            832370.7582358968,
                                                                            368604.3111770825,
                                                                            439432.8834750169,
                                                                            722759.4204235729,
                                                                            531605.4155363214,
                                                                            185284.3532078318,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ý;Ŗ\u0383éĚĢ}ȄҔĝѮͳ"ʛŐvʵŸѝ˔śŖǒòɟŝãϼC',
                    'message': 'ҖʛʎѨĝʗʶӠӋĸɆҫǸΞтɪɎˉʟǆƆ͵и˽ԘǹÂ\x97˯Ω',
                    'arguments': [
                            {
                                        'name': 'ϫз˂ùΔaҥϹɀįԭĽЕѤЍή²ɮgƱЊϟ¶ԑѬɁɶӝ{˻',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201538.756730:+0000',
                                                                            '20210909:201538.773856:+0000',
                                                                            '20210909:201538.790578:+0000',
                                                                            '20210909:201538.806304:+0000',
                                                                            '20210909:201538.822474:+0000',
                                                                            '20210909:201538.837912:+0000',
                                                                            '20210909:201538.854358:+0000',
                                                                            '20210909:201538.870976:+0000',
                                                                            '20210909:201538.887737:+0000',
                                                                            '20210909:201538.904785:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǫ\x88¸ͲͿșƀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201538.993412:+0000',
                                                                            '20210909:201539.009099:+0000',
                                                                            '20210909:201539.025808:+0000',
                                                                            '20210909:201539.042464:+0000',
                                                                            '20210909:201539.061522:+0000',
                                                                            '20210909:201539.078330:+0000',
                                                                            '20210909:201539.095282:+0000',
                                                                            '20210909:201539.110992:+0000',
                                                                            '20210909:201539.126539:+0000',
                                                                            '20210909:201539.142027:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¨ȾŲŸgɖˠԐȕ˲aʙǰѵӱŭς˝ȼϻҔҺӛƪӱԁʫąҒ˚',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201539.227373:+0000',
                                                                            '20210909:201539.243392:+0000',
                                                                            '20210909:201539.259518:+0000',
                                                                            '20210909:201539.276959:+0000',
                                                                            '20210909:201539.294325:+0000',
                                                                            '20210909:201539.311936:+0000',
                                                                            '20210909:201539.329475:+0000',
                                                                            '20210909:201539.345726:+0000',
                                                                            '20210909:201539.362060:+0000',
                                                                            '20210909:201539.379989:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ưжġɽʋʗСLŢA?ϿǠėÊŤƮIιŸÐԙ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7987948672413024937,
                                                                            6416715883652126901,
                                                                            -6922810260004571233,
                                                                            2457374818278676954,
                                                                            -3541413281240807570,
                                                                            4467498566949272069,
                                                                            2790873937894504712,
                                                                            -7905334567467445001,
                                                                            5412419935512224171,
                                                                            3051300014299630740,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȱ\u0382Ɋϧ?ԕмõԔĿΑɇŇΖųӱϺoˈҜĚ4ήÚ¿¡ʒӦǵ0',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3322542236273078327,
                                                                            -2106218049000231573,
                                                                            -8051552042724052203,
                                                                            -5041833512199947458,
                                                                            856499421628041097,
                                                                            -6574260610645964085,
                                                                            1533120687673165801,
                                                                            5205406381631500868,
                                                                            -8282030638518338804,
                                                                            8884906231556864569,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЍѕłǪΌȘē\u0379ïũƢϗſͱӿĖԂѶӔȥԡЍΔϹ\u0383',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'řЏ¶Ɛŭ\x8bПԥԄΐԭΜέeμ8ʝρìĆЗҰüdΑΟŔAȤƱ',
                                                    },
                                    },
                            {
                                        'name': 'Ҭ4ɞʭĜԄɏƐ\x9aü\x81ƑȌѠɦÃǤǬâ&ƱɤĹˬźЂqĄ£Ɉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӈϙΣϕ\xa0ZԂp˙Nǆ\x9dǸԣÂʨғН˃ҾСʣѿɅԩɏ\x88[Ǽʅ',
                                                    },
                                    },
                            {
                                        'name': 'ЏѦǢrɖχ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ě\x95ӫβΧB˕σԇɰȺˍżЂΏʛĳҨӮϷʺī\\Ǫ²ԛԀȷӽȦ',
                                                                            'ӷƐÛȧ?ŗеˑĈӧȝËɔȸԭϷƱ\u0380ԘϥѽҠќĪҘӀӧΎʘ3',
                                                                            'ÏӐġӹҠ«ώźɊҩĒǏҝȟ\x92҉ͱѮɈԚʥӋČòѶŏέɿjʔ',
                                                                            'cǷŒ9ȴ½ӴӸcÕȊҔӰȘϛԂ\u0381"Ðϙʢţ\u0380ɑ\u0378ĊʈϿѝó',
                                                                            'Оӻƨ˻ͼʁНϙȞMӍ1мŦþªʔԤη˾WʓĚȋ\x7f\x95ʰǑȵџ',
                                                                            'Âʘ˰āĠɋƾȔŃVϺԕИ¡ʮЗПԁϫԩ\u0380˦Η˘ЈǟМ,Ǳư',
                                                                            'ɓЄԧРϽχ\x8a:0ьтΉŻfЋȜ\x81ǒŸʧɐJɨ¾иƯîKщĴ',
                                                                            'ǔEΥԆͶзǴҎ˽ʖƄǛȾʹп˱ΦЅԄЁƅԊĺƒӿÌȥфєˋ',
                                                                            'ȅˢͺҚѠʁɶvȏәNƟǍēҾƊʧ\x80ġ?ˏŨÿʉίǒŤʁǆϼ',
                                                                            'EʴǡƆTʑÉҤˢ ǵ.ʹиоҫʧ˰ȱʱȹЊİϪ˄âѥěёМ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8dғũԌš',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            343384.2525843557,
                                                                            837187.6849830252,
                                                                            873712.8211098277,
                                                                            684262.6524993902,
                                                                            507464.45614989416,
                                                                            389473.6315716363,
                                                                            829934.5758836905,
                                                                            901195.5075991537,
                                                                            644530.7059730316,
                                                                            392655.41840501426,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ə˗˴Ũ˴ČȤʉĚŗĒέ?ϟơЊō<źûʍƣΦŇҢм',
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
                    'catalog': 'шŸԞǛѦʑƥ[҅ǡ͵Čʒɖɘӊʠʄļíʇˊѷ®ó˜ˌˁĕζ',
                    'message': 'жʕƮɞђ˺ƳμȦҩɆӪϸҨҮƐыȤӞ\x9bҰΒɧд\x9bŐʕķņğ',
                    'arguments': [
                            {
                                        'name': 'ѭϔș2ǅDɋ҄ӞȹӪǸà',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201540.927923:+0000',
                                                    },
                                    },
                            {
                                        'name': '˦ĢԬ\u0383ƚҌÕԭˁʐÿҴǢ¿°Ù®ŉόˁƯұćӵçɶҭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϡԁȣęȝʥʱАѵĻ*Κƭ6ОӀƫ\x95ÆǧҐм\x88ċԥPɋʝƤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6628396074714563842,
                                                                            2194583188996434412,
                                                                            -4980881155804688638,
                                                                            2744036013513477649,
                                                                            -8905109188609007112,
                                                                            -5094773003127357987,
                                                                            -1775077695420055745,
                                                                            3241352721920294783,
                                                                            8381682113791688985,
                                                                            -1277528244389221882,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҐЊѧʸ\x92ԂĻȓȿĦ˃Өʝ˕жϏƟɍ\x93˱ď°ԒˈҘʮƈȌˎΛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2280191900738342982,
                                                                            -1073759036026597986,
                                                                            8012112552625009905,
                                                                            -4414590626646843856,
                                                                            5331250957602558677,
                                                                            5172992570346493726,
                                                                            -9082674576660581840,
                                                                            6235423969145093561,
                                                                            -3555790717116548697,
                                                                            2026556572284389707,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӾЖӡǊ\x90ΑƩΪȕɃ]ЬȽˋŧԕșç˹γʨǟøŇϽ˨\x8f˴и',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'çϣ`ѹµÃҊѤ˨ҊɟȁЌöԬȑϋǮǃɣưȶüǱʠ\x953Ʈɫ˂',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɗǤȆу³ðǰƜʜïўtВžД\x9eӍԬȭӛϢԢ7þˏəƞ\u0380Ľ҄',
                    'message': 'ҎҘĈĀҤҩǯӺÜȡюƦ4ƥӛĐӺ˴vҼхлѭЮ\x8cϋvʧGƲ',
                    'arguments': [
                            {
                                        'name': 'ǤʏüӷСЩŤǸȨÀʵƪƴ\x89ѹΫ-3ǡǘ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '_έҶϤ@ơ¡nHʓɜËͷѽŦǙÞĭѳҾȹűȐʦĶĆʽƀѳƙ',
                                                                            'ưʠҝȢÐ\u0378ЍcúѦϫʑϵƛϒЙ҅ʐ-ǢζΈӨϺg˺ǫȉͲʊ',
                                                                            'Ӥȹýɴ΄©œэɛȰљϊƫ˩ŹΕӂÅӵ´ϜѣϸљʞCʗʊѭϑ',
                                                                            'ƫʓ¿ŰŢȘɘǩcэņΐƤɄëșҭͼќËʺ%Ӻs8ˬƚëˑǾ',
                                                                            'ӶéˠқҔ˃ßœŰüȿѷȐɁ\x91ԇʷƹžǹͺȹǊʍЬΉӬɭʻȍ',
                                                                            'p\u038bǮ˰žŁήѐʒ\x8aãɒӣ>Ԙņ\x97ħӥϢ\x94ɾԗɪΜƚˠɍҍģ',
                                                                            '@°ԜĩїԎѴŮϲǂȈϚˋÞ\xad˳cų/тȚLüί\u0380\x8fǿΣіӑ',
                                                                            'ψīɨyӀѐπÇʩтʵóǤɀȷɟŒѐύɐ\x91ϘҀǣԜͳ˓Ȫêũ',
                                                                            'ГŶƦɮDǘͺŅҜáƤþȋκɠӕʱαδяÌƾÝèЄßιСϫɏ',
                                                                            '?ϡÓ8LѠүʕƿ˃˲ǚӏЀ\x90÷В8\x84ĩɥA.9ɼơΡӃғÖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӀѪĬɃπҜŹԚëˠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'pȪ£ӄίӷІЀȼɍ-\u0383ϋΊɠļҺǏƬҦ×ˏɟϫʡԫˆѳƫэ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'ηŭѳƽǈȞ"ɗ˭ϛкŮӪҩчӧüϏ\x80',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1906495248500584201,
                                                                            -6534639810413611743,
                                                                            7382589280010416458,
                                                                            -142003853692360344,
                                                                            5399290517612252584,
                                                                            -7327124309946408449,
                                                                            -2047781112457766255,
                                                                            4167274373311505716,
                                                                            2698420081564846147,
                                                                            -190593704093017014,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҿ\x89¨¾yҰÔ˳',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϚэǻːЎͳaоť˲åӔˤǚƂȝЋѻȋФӂ϶ΰķ;ͺСˠǩР',
                                                                            'ğԊ3Ɨ[ĠѥΈѭƚšɴϝԚШʾғŕҹҢ¤ǣȘѭӨӞʾȢ˸ţ',
                                                                            'хɟӚҋƇѬǈБ\xadʔW˱ȼӒɌŉμďђѤ·ȈʦЪɱʾ:ÙɃ°',
                                                                            'ͲƓʋѡӔåĢѪҰϘјҜĦҢȢȵʤ˩ϙαќȳˋɉ˰0Ҭϥʉх',
                                                                            'ЭɢϩэӨºϦŶАϥģԝƜ£ÊƆɽǑɇɒġǃ\x8bҋ!˓ˇʽɯϧ',
                                                                            'ԇΐǪɢБťƀƒκκϦ®3OҒԒ҅\u0378ɣ\x8f˅ûɗ\xadÑʅˈ½ǒə',
                                                                            'ʨ(úŚƓУÐӍʪѰČżǆʹħ"ф\x93иíˁ÷ϼȆӛӽ9˛ȓ\x83',
                                                                            'ϹĽ[ĕжʛɓõʷĵЄҜʉӭƞӝϦ,ԫʕʟɓͷĤǡйiԦǒђ',
                                                                            'ŲӐ˚ѳƗыӕœҨˉóǚʘΟϚĵˇ˙ίk*ѐ˧ƸĬEęѓүÀ',
                                                                            'ƈȕˊɚҊǛǋȪʋԘȺ#\u03a2ѻԮǢɶԇЊ[ʹĉǇϘņĒŘӿӉӥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҢʻǂтïγΛ:\u0383ôӚȝĻȕå\u0380Ǜʊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201542.760650:+0000',
                                                                            '20210909:201542.783175:+0000',
                                                                            '20210909:201542.804125:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȉ\x8eSӂϙƹΛӡɢэКӨÑŞϿB&ÚoѣȚÒİ\x82˚ʝАˑ˜ɬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201542.888219:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɣмɏɱß6уҨ\x9cӁȢӾΊǎŮ#Ҁ÷¬Н˃ùš',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201542.955445:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ZΚӫѳξțēˑƀЃ·KǉԘĕӭлȫ\xa0ωɀ\x827',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1104679894571527030,
                                                    },
                                    },
                            {
                                        'name': "ǽ\u03a2ǭĦźĉϠҔǢŘϗħȩйƭπ'Ŝøĝŉ˼Ǒсӓ{њФѻё",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201543.094297:+0000',
                                                                            '20210909:201543.109755:+0000',
                                                                            '20210909:201543.125839:+0000',
                                                                            '20210909:201543.141937:+0000',
                                                                            '20210909:201543.157894:+0000',
                                                                            '20210909:201543.173670:+0000',
                                                                            '20210909:201543.190578:+0000',
                                                                            '20210909:201543.206217:+0000',
                                                                            '20210909:201543.221569:+0000',
                                                                            '20210909:201543.238100:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԎʣԐ·ôƹōƊ·ɚϡƹњϓÿÇ¡åӹa˟íϺѺӪӧƬʦˍʫ',
                    'message': 'ͶɩéҞɅɬж˽eιƴ˷ʇ\x89µύҞM˰ʌʂѡ\x90ĤʗѕʱЙā˯',
                    'arguments': [
                            {
                                        'name': 'ԅ2MԪҩɖlдƫӠȖMȺμːÒүɸɒɵɿÕʔʲǌ\u0378ӖbΫΒ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1423842816632534301,
                                                                            1297556604172521370,
                                                                            -3898803705035530976,
                                                                            784645167665861851,
                                                                            -1974175819586249717,
                                                                            -3569492286748513864,
                                                                            696514263535113473,
                                                                            -7701112837250522650,
                                                                            -4360286794305674019,
                                                                            -1343979372223062213,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'лѸтéÅжǊnʳ©ǽ\u0379˰ϳ˓HϑÕDΜɓǰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201543.637929:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ù,ҶˎҿѤUÄԊEԋĐʁίţűЊлѴǡȆԊӎ³Ҏϙ¨ӭĝ(',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201543.704530:+0000',
                                                                            '20210909:201543.720901:+0000',
                                                                            '20210909:201543.738486:+0000',
                                                                            '20210909:201543.755899:+0000',
                                                                            '20210909:201543.773257:+0000',
                                                                            '20210909:201543.789867:+0000',
                                                                            '20210909:201543.806065:+0000',
                                                                            '20210909:201543.822556:+0000',
                                                                            '20210909:201543.838730:+0000',
                                                                            '20210909:201543.855599:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˺ѥʢɫӃϧϚĪ;Ʀӭʼ˓ŽĠʄΤѽʲaϮɇɎ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201543.945274:+0000',
                                                                            '20210909:201543.962117:+0000',
                                                                            '20210909:201543.979419:+0000',
                                                                            '20210909:201543.996242:+0000',
                                                                            '20210909:201544.011409:+0000',
                                                                            '20210909:201544.027098:+0000',
                                                                            '20210909:201544.043367:+0000',
                                                                            '20210909:201544.059311:+0000',
                                                                            '20210909:201544.075985:+0000',
                                                                            '20210909:201544.092903:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɫҌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'МԂŭѳБķќGˁTĽ\x90ÚљÆϡԞцʁҽɛР\x82ΟαāЂMŸϖ',
                                                                            'Ď˅ņŔεiγĸŻ˅ˏ#ʄԚĄȊʅá{ǒԩӫˡӘS·ôǝԁю',
                                                                            '%щ\x92ƑˡȃçúϕԑҖϵ]ҴЙԩʛκϋǙΤϪЪ0Ҽʹ\u03a2ΖȨҺ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'τԗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1073927478149090463,
                                                                            2083686281115564912,
                                                                            -2074630503172205842,
                                                                            -4208186107594099447,
                                                                            1630058776410450678,
                                                                            9143882004674759575,
                                                                            -6333041866344871796,
                                                                            8708709858493414353,
                                                                            8316918378057315925,
                                                                            884289303024909077,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϯĉáЈTԮӒԥȟǱқҿHάҽ\x87ȁԮˀj˚ɭȹǷѫʨԥηÃȱ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            821121.3034554388,
                                                                            231354.6266899209,
                                                                            154182.79218691651,
                                                                            -47894.14314446011,
                                                                            400663.1812142777,
                                                                            387853.1939087149,
                                                                            138737.68224613494,
                                                                            934901.2234967406,
                                                                            332172.202977039,
                                                                            780892.0392499464,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϛѳ˓ȰЀģȣЛʬóӋˌČpEƂ°ƁΖϲЅƞҸȊ¥ЊʃЀʦˬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201544.778862:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʤǢUĀŭĹGŒ|êŜŃńӞĔʈЕŖѵxļҿț9˦ŀDуϳЕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201544.843919:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʓƘЇЫmɏvΛҀͼʣ\xadőσЪ²ҍʐƁƓȕɸƛДɛШ˓ŒԦѲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9204470757638854283,
                                                                            8899117112391227150,
                                                                            -1764268807233201138,
                                                                            2853690576874901196,
                                                                            -1279392521822885769,
                                                                            3294867908978604221,
                                                                            2497342220659635096,
                                                                            1120213593509358883,
                                                                            8408913074116484509,
                                                                            1393667532753553425,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʂʗB˯Ѥȑέȕàu1ǸƖNNǃ9vАAǹ/´Ԡŗͺ\u0380ӈҁҏ',
                    'message': 'Ӆ˃©˥ͳѦǷǁrŞϟʚɬӔȯƒłБˇΝɢʶ΅äIҁϯ2÷ɋ',
                    'arguments': [
                            {
                                        'name': 'ǊЩ©˞ķŽЂŜȢӲΨʠâLĖȎʷƏɱԒǬυѰ\x80ʎЮг',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȣȞƦɨƨʐ²ћȍжɽΩΗӑƜȏ?ˎʉ˸bтÓԖ҇ǲćēǍʬ',
                                                                            '˛ȧɐŗĞ˂Ē˅ŇĺԏЙˣ¸ӉёēɅӑ˩Ż҂ȚѐҶɴˊɱΑǫ',
                                                                            'GŦҕƱɳԑҰȆǉǟϿHÒƐӍ˳ɾ£ȆѺώӃżʫǏԭȲʻƈɨ',
                                                                            'Ģ\x8b¿ēǫ˯źǊ˱ҨōÆçϒęȊǍͽӲыOȉϕĿɿψķŋЏԙ',
                                                                            'ϿѧԧŔѰȣčƎ!ƐŐ\x93Mβť\xa0ˌtƸʄ˩ɂʺ"҂Uӊȹ˧ʁ',
                                                                            'ŃO˱˯[ԩӉǺSӕԀѐČԖŴΗïάф³ԆӒaɸ˪ұríӿ҈',
                                                                            'ÙɍƢԨǻǙ4΅ʚӡɕˡlκɔҤŚŸΈѫű¦ѱʃϻʹTӖʥϽ',
                                                                            'ҵȶÑɖСѡεѳĄĪПàЕөƷȵ˹ʆâŵУΗʄļoƻȾґҴʸ',
                                                                            '<ĮϼɵŗфюǍǭʉ&ƩѓΑжɐӭŀϞԣʔˑӦșѧɈǅˠџʍ',
                                                                            '˥˂ȪӑˮɰԆȤŅǟǒưΊ¹͵ơĐɠÑ]иѪ˩ʾδԟğҙĪԞ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǃBǯɟϖôɕŦʞǡǅ¯ϒѼƍý҆С\u0378ęѹѰŦ*ϳsƈȞөґ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'iє¡ŊȜėɄÅ˕Εɱȕ\x8aŬǲɺuDӈþҙēɗǅŵǆǒϩѼ²',
                                                    },
                                    },
                            {
                                        'name': 'É%ъǰϸȅˣĀҤɇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 856567.9569629497,
                                                    },
                                    },
                            {
                                        'name': 'ʨ\x81ƻɐƯ\x96ʷǭ\x94ϯɟȝʆѿҩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            297453.1147698168,
                                                                            25379.589088712368,
                                                                            290749.25725848944,
                                                                            908155.0608488113,
                                                                            975838.5727331338,
                                                                            951315.7223067516,
                                                                            240630.95470103808,
                                                                            228185.12660741265,
                                                                            391340.3978300555,
                                                                            733616.9557452863,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŉIѴ˄ˊ\x87ƈđϏӫɺĲϼɫғ˜ѓǦ!Ŗ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˱ʙӎȶҰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201546.033001:+0000',
                                                    },
                                    },
                            {
                                        'name': '˟Ҹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201546.106498:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÆʈɏZCжƾǭÌϝȉ\u0380ӤȯơÇ\x91ѵјʄЧǧѼɹɸϬ҉ŀČh',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӅŻì',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201546.252529:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϡvŊÁ˓Ơү\x84\u038b˒qĂҐȔҟʓƥöƄȜvή®˲ʪϗŨԚąɴ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'ęƬԥ˨ʬйÜpΈӞԊGЉύϑНϨˆ=ǚӸѷdŖ³ʽΩ҇Гů',
                    'message': 'ˉаԔҳԂŋǁƧϯřZǴҾϙаĈžϛιî\x8fWǽPĂȒůʢҹʞ',
                    'arguments': [
                            {
                                        'name': 'ϖâӫǞҗàФƴ;ϥ®+ʧȑÍӅŽϿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201546.648245:+0000',
                                                                            '20210909:201546.665801:+0000',
                                                                            '20210909:201546.683148:+0000',
                                                                            '20210909:201546.700495:+0000',
                                                                            '20210909:201546.717088:+0000',
                                                                            '20210909:201546.735492:+0000',
                                                                            '20210909:201546.756577:+0000',
                                                                            '20210909:201546.776251:+0000',
                                                                            '20210909:201546.798577:+0000',
                                                                            '20210909:201546.814810:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȟœɣːΟҧΆϘӲǍӳȘ˾ҩʦƘ˘ȒΫȞ[|ΊҖӻǱϟɜɕԇ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3379814170461036640,
                                                                            2902936108083275075,
                                                                            3470537327281146301,
                                                                            2650247859359830656,
                                                                            -4696150864993593426,
                                                                            -4212588192712219295,
                                                                            -5278423076927228241,
                                                                            -5275879088829123033,
                                                                            5256857007426452555,
                                                                            3899216831445035156,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ґͱ\x9aλ˧ʿϯԡĚ^Ɗĥҕʄ҉ŃԠˉӇԐǹƂ¦ªϽžɸēě˟',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            927356.9974408684,
                                                                            157461.05986846334,
                                                                            52649.45379533328,
                                                                            272079.6516211786,
                                                                            900217.9695794578,
                                                                            870650.3367096552,
                                                                            252123.47420598072,
                                                                            807240.5720801178,
                                                                            491921.5305638483,
                                                                            953994.8876022089,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'НԚ±ѲɤĎǼɡ\x8bĥԍƛϏȖ÷й',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201547.385180:+0000',
                                                                            '20210909:201547.407986:+0000',
                                                                            '20210909:201547.425146:+0000',
                                                                            '20210909:201547.443437:+0000',
                                                                            '20210909:201547.459695:+0000',
                                                                            '20210909:201547.476798:+0000',
                                                                            '20210909:201547.495525:+0000',
                                                                            '20210909:201547.512354:+0000',
                                                                            '20210909:201547.529031:+0000',
                                                                            '20210909:201547.545892:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x87ҁӨλŬźҹҏʰȡπȫѤϲϖĺΡźԝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'χѻϿ˯ř\x8bҐ¾˞ĺԦqǒƨ\x8dӁƊʅйъŘгͼ¿Ǿ(Г³ЎŖ',
                                                                            'ʯπˮˊӯǪĘ>ˇʦԢђӔԛɟӉͳ5Ԯʺϗč˞ŽúĶƯȶƺʥ',
                                                                            '˲ҁВȸǯΫŠ\u038dˬк1ŶʅɃдɞƁǂͺʽԠĉϦùĈŉѡ·ʂυ',
                                                                            'ɦηʺШɺ(АúӨҙӞ\x95%ĊƋ˸Рԃϧ\x83ǹǄť˨ëǕя¶ˀ˽',
                                                                            'ɳʀĬ˭ƖĮëθÞԚƍ˹ˢűŊϚŽȨȦѨUÍҗ3ɭƲ2Ίȋˢ',
                                                                            '@ӐС҃}ƣΣŋǩʉȷɻƿĜӨФe˗"ŶɄЯѓԉмŉЊɀџƥ',
                                                                            'ʥÙϼЌυѡłΑYɾӧĺСʰķǸԛҶǺvjҭӝäԖʌŤƍԒΣ',
                                                                            'Ɠċ˵ɶʁɜӒƓ˽%˒Йлɥ÷ŨȐМΨ2ˑǦо˖ˍ˫ЖɪԅҢ',
                                                                            'Pѷßԝӥ҃ɶĄȔĴϖŻť\x93ɫȒʄȬǙҨ½фŐӹĤѽǾǑh«',
                                                                            '\x8dƫ˭˓ȸ\x9aˑѓҥΧϟϹϣҀѢȦ˴ӢҢЩİǬƞƼҺÞÏē#˓',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɒťѿȩŅÒԟĖ˒',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԑʮʎ˶ʬǟЪǼŅ*ʘϱ\x9a˔¤ŤΣȧǓʜϷӫJģŅʪǡƎƟȕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5887985990726870895,
                                                                            -1460014781896675807,
                                                                            5113891070382005111,
                                                                            -8096860249365517159,
                                                                            8171834383178125501,
                                                                            1213295339030165820,
                                                                            2955160234126224817,
                                                                            4252066362819625535,
                                                                            -4261166619580216266,
                                                                            1348180257071016874,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȉùºϑԍЙŮƏɿѥƩZ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ĲšΪŅǣȿҺ΅зΗʯĩàĘԊȕǊ_ʸԆĀҮÚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 611707087718187849,
                                                    },
                                    },
                            {
                                        'name': '˘Ʊ҃ǨbɮƮƩʄĨȽˤȤζŷʻťќ\x9fоħȓΉUЋ\x95ҺʘR˱',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȁыšȳΉενӣǌ˻ϊΉ\x91ǊѥŌԬԌɐ\u0379\x82ϰ[ΕГřґѮНǻ',
                    'message': 'ελʴǑѷƦŝȤŸ\x9cІƶѢVͽ˛ΫҨϭɏЇūÏΪŷυzϵȊÒ',
                    'arguments': [
                            {
                                        'name': '¤ʡфʶɻȑВȳЄԄΈЫƆҺà.ƾȃΌҿΟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 233721.25076615543,
                                                    },
                                    },
                            {
                                        'name': 'ɵѭÓͿɍȵΘԫùƏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201549.083002:+0000',
                                                                            '20210909:201549.099410:+0000',
                                                                            '20210909:201549.115723:+0000',
                                                                            '20210909:201549.131949:+0000',
                                                                            '20210909:201549.149506:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǵȝ2ΔːϨãӢɝ΅ȝϣҋІâñőʉЃsӋ\x8cÂȁ/ȶΠƄҤȣ',
                    'message': 'ЪίϠŰʉ˽Ǡʂw˨HӞøɶɴȴ˝ʦ\x9aȰNĎʇЮӋǆǠӄиԁ',
                    'arguments': [
                            {
                                        'name': 'ХśƕҐ\x9fȂƟЋȮŘѪ˙ΔĦˇĨԒѵȷӣІǗҞ\x9aщӚЊ\x9bҜο',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 589418.4217451933,
                                                    },
                                    },
                            {
                                        'name': 'ιȾѡƺёӀȚĤВΪΓȺ=ʚªϯƎɺҊĔϱ8ѽýΧĉвʵɴϪ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԩҩĢŚƠтɶϡѪŢʮˇ\x96ӶǎӑɘŅϘǀƜѳĲɩȖZƋϒʜċ',
                                                                            'ѷϢʝć°eұуċȻĸϖ$ԨʞǹӞũ%ҬĎΕS\x9a`Ҍî˹=ϋ',
                                                                            'ưӵoҷɹŁŕFǿœbŝǑʐĐͿtɄ@ɥ˖ԉӻɒжȠάƔ\x98ˈ',
                                                                            'ϡșµºǮÞƽȍõțɐƟϺєʾξÇŒ˅ȼ\x9aǮŞ»ȵԁӲ£Ο0',
                                                                            'ʖʘѧԘҤKѮǑǜɅҐHͻpнÃɽҵ\x9dЫӯɰ}ˌ$Wғϔβɽ',
                                                                            'ԣӞĚÈÞœ˪ϞӰͿƯþьΗίӞǒɚԔǩΊӽýʒəƼ½ˀϾǔ',
                                                                            'ԣ¢\x80ԬǂŤĀϊ˨\x92ǘ6мˌǼҰѽȸйùͼϡҘϳ·ӠɁϬϭҒ',
                                                                            'ƩǥyƤȺĐæiѹˆҔ\x99ȌȓÝкЁǠȄǎȎŸӄϷгſӉ΄äɽ',
                                                                            'kϔǽ΄ͳЏȕƇˆŢЦɔ˙˻į\x9aчӪҺҁȄώǣҼ˶ŞԝϺѳƣ',
                                                                            '+ΣƖɄµΗƨ˘Îƨ©Ѓŗ˪ŵȃƘԚԇK)ňȐǯһΆȱ˕ѓŖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¹>уÆãǭԜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201549.613941:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǽ˹ÂЎ»ĲąƎ=',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201549.681659:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƊŞ£\x7fĎnȄɷηǞƗҲ˗ϖ\xadTíί\u038dǨ҈ʪĉȑĆʒӟǏɅ˼',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -37284.72188413715,
                                                                            888546.4457290561,
                                                                            676756.6697723356,
                                                                            339632.2390827946,
                                                                            555302.3989503192,
                                                                            748272.8923727736,
                                                                            171243.35384465888,
                                                                            808517.801649961,
                                                                            146417.60982412985,
                                                                            840664.0889951019,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѩVŎήǉΙəѭӯП½ʮǈ˓Ȗ˦Ɓ҅ǻ)',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϻԔƥўʲƊϛǟƹЬʦĄƦ/ƅǴҒʷǬɺƹѐʌѴЅVnO˂ϰ',
                                                                            'Оу»ӲŻaӎʺƵɎЇЅŴЛǊЇФ˗ǃѻҵğАIĶёɅԦ\x9fĠ',
                                                                            'МǑȓȊѭƋкɑɔԠ\x97҅чoЋϬԉǀ\x94ʬʬͶ˧Ϸ\xa0Ѩζϭзa',
                                                                            'ϋώƎ¸ϝĚũůϙɌʿƚРӬ\x9cȵT·ѶUзψƣŀMԚҜ\x8dƊk',
                                                                            'ZŸԨѧÜÈӱΞŉҒEшŪȜȑͲĆˆЁʐğΞƲƂҔԊӲԆҒԣ',
                                                                            'ǒȨмΟѼБŁσɧŕɘ\u0382ι§ƶӇ\x98Ā˹ɟ"ŬǫǢŅùΞϏɟO',
                                                                            'ÎҎрЏ\x99ÜɌҡǍCԗ˼ȁ\x95łŴŞʌдɁΥgȣώ\u0378\x80żԨƌō',
                                                                            'ҙƉ²ЃËҸɹХͲѿӻұ©Ȅƿ\x98ɋȄ˟ɿ¨ǡȖèҽȕɷɬҳʏ',
                                                                            'ʞzŋǈʘ¸ϦϹϞŵˌοѠǌѰΖźɜǔϠӵʕκȮƵßQnŽ\x84',
                                                                            '˯ϞǄȇҒɌάņƤЊːȾʢΪԨÜЖǃϜʸ4ӌȬɶЖчȦ\x8eÁâ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǾǮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': '\x84ζŲģӘŤˊԣ\x9bįӈ϶Жϯӛ<ӏř˗\\ŕÂɯɇƃȿ_ϲЦů',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȺuĦѾĢɤŒϚӲːϪ˴Ȋ\x86ƩȍʸԥѫҏЀӃµ\x96ƞʞʔŁӛӭ',
                                                    },
                                    },
                            {
                                        'name': 'ˮӲŋИuϊŦАƯ¯ΫɎʋҫȋǔÈԑőǒҴH˾˯Ϛ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ËΊнɒјħϴћũƀϠѣɯʵʱϏ¬ÂɞѮǼĝ˴ÝűӳǆŚƠĠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5508243449942926455,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҰѝѲĎ˂ξŏфðȉĻȹΑНľôԏ¦˴UΧφɊƤöєź¦Ҷ˨',
                    'message': 'Ѓѡ!ǐˢ΅ΉʴģЪϼλŐˑĤˀҪӖѕ¸РµЫԍǴљҪ˨ǆą',
                    'arguments': [
                            {
                                        'name': 'Ϛԋϊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'щȹӐ˧¶ѽ©Ԛśӻџ\x80ƱЍţҽΤȎΨԧԨѢİĪĐʷȴϼϽΫ',
                                                                            'εʦûɷΠ˃ʝƕԆ&ƇŭМϊÇǨ¦ӠŶǂцē·Ĵ±\x93Έ¬Ȩȱ',
                                                                            'ӧɦ҄ʵЅ˾У$ӵҰɋĜͱɤӛ˦ӎÊƒĘÒǭԑ\\ŔԂƛӅɲʕ',
                                                                            'ȬüɫӠԆӲѳɅĻŜ\u0379˵ǑӮǐάɴԫÐӍƏ\u0378Ɨūņ:«χг˭',
                                                                            '˻ˍȹѵ˅ЖѤǄʫǒ\x87sԫĂƺа҃Ȭ²ͺ[ɬ΅лĸxņɆÆԖ',
                                                                            'ʚҞӗɯǬħҾдԘêƫӺ\u038bӈăÄΌʛƐγͻȅ@ʼшǼoȔȾ·',
                                                                            'ӊʅǝ\x81эҸǂȎҷԀʈʡÑĘљгƙƎĘʆ¨ω\x87aÝŌƊ˥,Ӡ',
                                                                            'ɮғQŖԉɿҲΐȌȭǮĿԙђώҕϕҶҷģÖπ].жьņnА˪',
                                                                            'ϷΥˋø˘ǉ?B§ʨȆεӌѹáĐƚɛÒɪĶ\x94оbάιpKΦŁ',
                                                                            '\u0382ҰӃʴΟğʃÊѬǾоȚɅʸǪϊɂÍԚĦȨ\u0382\u0378ÙƑЮÙϡсϿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ъ°eĎιԣж',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 227402.2231395737,
                                                    },
                                    },
                            {
                                        'name': 'âΈȦѱҩǊŵßӌӾˉɅŚ˃ƽuΊ˯ÒȠҀϟτ˞ϋΡНƊωМ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201551.080119:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȋȞȋԀ¼ԌÏǠԬрРŰ3"Ѕ\x9aЎΐғĶǸˡǬćǛǗƭʿѫŖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 13283.939713916203,
                                                    },
                                    },
                            {
                                        'name': 'ԍӆӎãĳ\u038dǋ3¤ÃɨԦӁƀϾһχÜǄ(ϱɎТȂ˓цͺťЈY',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '"Ϟ%¯ɡȏϻίƓkѠПÓǢϝɞƮBϢЉŚԇſÚӌĸӇŅâȶ',
                                                                            'ƚɕɅӖόɥƭ˛ĥԈʙʉ~ʸЏҡǾ\u0380¦ƆʙǱҶĔǌŉКîѮΞ',
                                                                            'ђwɷЧUԇùєИӮϚҲʌùʅӎâфҘϭ˙ǧɂƻΓӬ{ȘƂ.',
                                                                            'ԡӉԍ}ɢ\x7fӐŲŶŭϻňĒ!ÃћâǳɯйǚΒˊǍļ#¯˸Ώˑ',
                                                                            'ÚĄԄîʆϦѰ˃ʠʇ˟ɁΠˑǀцēεʬƚɩЉȺǟƸќËѧӃЦ',
                                                                            '҂ЪЍ˂YſɝȃƑѕˁѽɕƴŽ˔ӤĮҸǉӴԉ˓ԑ\x88(Łӏhƌ',
                                                                            "Ə\u0383\u0383ϧɨNǡʰ˴ӗ÷Ͱğώß¡ÉƜÎɁдΨ'Ľõʘþˡɂµ",
                                                                            'ϬӮĸЫwӠӲuưț¨Г˱ɋӐêԓԬúѮɊӹϾɁαѫӽɅҎǅ',
                                                                            'ҿ|ì]ĂϴщφԕƣñәeюȚɞ\x88ƮèGșԒпɊàƿҭԌʽ&',
                                                                            'ϖD¹ͰԘűӅ˙ӒËĚӱа¹ɶÖ˱ҎƎīɐʨðƊ:\x8c\x7fĮЁń',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͼˏГψϝ˻$\x94ϙыТˀξťөϷɨӻҊȊǨӐȋɨʊӿț¹ɜ%',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǏοӜҠƈTȠ%ԒǦϨƽLѶɚСΉƣЩǖɽԧԗɖυȘOԟŉū',
                                                                            'ӔѼ˳ʻýɶиûИғś|ΩɡϿî4ÒӟÞǒҊΜʞĉƎ҇ƏǠ\x98',
                                                                            'ƽǫÈȡŁôӑ˕¤Ŕρòӂś˩иңԙŧ3ƭǼ{ϞſЬĮtˈƟ',
                                                                            "<ʓ\x87¹i+jǖͽåǨʞӡ'я˞ѻҗ·ʪƶԫĆϖԋӑːˮӡʴ",
                                                                            'ȆѮ³ÓϛҮƑ5ÒȄӳƤƙǙ\u0379çÒʬɎ6ˢȃԫıɇԉҘҥёȗ',
                                                                            'ЪtqʎĺԆ˩яzŐ¾ȸѸŮЭӘԭƳǚӶ\u038d°ӺĥΌЊƪʆǝʽ',
                                                                            'Ɗ´\x88ǏǤцƴš\x8fɇÖѡҖŚfŋҪ»ѩĈÔӿíȣϝкΥӂЀ˛',
                                                                            '6Ĉʺ\x95Ҧ_ЩvҙЗνʿҹȊ\x9cǃϞcκ\x8bʴɤʚϏŌǥÆ˨\x9eÇ',
                                                                            "ТЬҊʩ\x8fȹԂǩȷɽ҅ĎȌ!ÛƺĔ#àϚΈvҫƫð'Ѓс˷ʧ",
                                                                            '\x94ĉʧ˻ɀƭβӬиʾÖБâŦуҌ´ʟͼԔȓɼϣŦyȣӮҾʰҹ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˺ĖνƈˁѯҘьҐɌŦŰТѱѺ\x9c',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 610342.4008174371,
                                                    },
                                    },
                            {
                                        'name': 'ϡ\x9eéģѵёşԀĽɑȿϜϬҠưԚƓʇɁϨɖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȳѴшʅ\u0383ƾҫŮɦϡŚүχĈϛ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 636866.7469536959,
                                                    },
                                    },
                            {
                                        'name': 'ӵˬíÂҩ҄EǤǒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'W1˹ĢʋԌӿфО)ΡԃǄ҄ɏÝŻ΄ҷԎеӭʫѯӂӡɒ˫ИÛ',
                                                                            'ę=ԩ¹ǂ®ӦċɲśǁΒӌȑ˥Ɂԫɚƶԃ¤ƣ˾ϸɖԚѾ*їϞ',
                                                                            '\x8a˗ԨȚгųƕŎaƖLƋŒˤ˅ŪƜΔʘƜƔ˯¹ʩϴӇ˲ʤǒǔ',
                                                                            'ɡΦэ_ǉоɒɘKӟȣӢҢϓήϊŋ\x9aϚԥ;j%υɣҍĳ¥\x85ǿ',
                                                                            '7ǅűˏĩ˷\x86ҸѪʻƠʛцХţԃм҃ѥ\x98ɦȴǝ\x9eǆ˲ƌѨϓɩ',
                                                                            'ȞœÝɰ\x9eɊΏyȯѠúͷǆȘ5Ӟέ\x98ѱҲIűӬϿсȬŖДӛɖ',
                                                                            "ƅ'Ԛϓʴ·˭Ә¾H¯˳ƫµČēӼсXőŧļǐŲƙáлɪӍϓ",
                                                                            'ĥP,;ΦȖҡRӼ\x94αŷЮŊʠţѠˇҤ҅ɲȚg?ßҚŮϬ¹ʜ',
                                                                            'Ǫ˔ßСƟʼǡӥɗ\x80ƳȺĆȍ˲Юļɰ\x8bɐȣˍ/4˒JʍǹϠѠ',
                                                                            'ŸԣѕӆҸǐ˘ѸξӺƱ²εɅĩҦƍңâéӚȃÍwĥҐ˓ϛǒƕ',
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
                    'catalog': 'ȉϳ',
                    'message': 'ȳ',
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
            'identifier': 'ӂҪήπˋɔϮѢˋ¶ʐćϤ\x9cγЖѥæǏƬёˀäΟЦÍ]϶˧Ζ',
            'categories': [
                'network',
                'internal',
                'network',
                'access-restriction',
                'configuration',
                'access-restriction',
                'network',
                'internal',
                'os',
                'access-restriction',
            ],
            'source': 'ØѪ"5Ё˒ʁčѯʈǦȑħGhҟӊ¶Ӈ˦ɔÔј%Ѿ¦Ȯ˕ԗĉ',
            'messages': [
                {
                    'catalog': 'ÕɐҬѸŸӾνύѯAҁÕFİ3ȃ˂ҟЃʴɋёƗѯΝéċЃǗʪ',
                    'message': 'Ū£ӏҼјҮƥŪεΨѕĴɯũ\x89(ɞmеĺϙǗʈ0Ä˻ѬÅ/Ģ',
                    'arguments': [
                            {
                                        'name': 'ҭѢϟӋ\u0383&ԫǒʶАϙϨʎŀσӨƶɁʸǽXıPćyűĵĮǹƃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8228696332356893331,
                                                                            5512790868150905215,
                                                                            3032128141845311114,
                                                                            -1520826397423739463,
                                                                            -7408059221744868425,
                                                                            -2799098992823019487,
                                                                            6708130786600878309,
                                                                            -1127425869735795094,
                                                                            694307202055785781,
                                                                            8581628094516939853,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÅĞuј\u0378UҠ¼ʩ˛ŶǸ9҅ΠϾΛ&ʒΒϕűԖˤѿПΒӬŪΧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȫȓŔӮɻɟœ\x81ɝˋˑžӈдϫϥѓѪԮϮąфӲQȿŽǌXҮ2',
                                                    },
                                    },
                            {
                                        'name': 'ŮȢOǙЇɡӖźϋλʜƼȇӡηɺġǮʕͷ)ǠѲ˖˒ɓȓSʚ!',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ɏΡ\x88Ѳ#ȢĘою=ɥĈΛľɯȿpɅ¬ˆ*ԑȒǒʒϪÓɓQπ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            431655.1244133393,
                                                                            387729.9355476445,
                                                                            529546.1315368736,
                                                                            -9424.885462397244,
                                                                            259414.9973333364,
                                                                            181980.8797084018,
                                                                            -26136.390666761217,
                                                                            192864.8988412014,
                                                                            114623.40719120207,
                                                                            547918.8760317954,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӱʟƋӷ[σŪҜ˟ƣ½Ӟǒӳ\x92ɲԧϦƢСĂѐϤԂ˭Ƒĳǆ0Ì',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': 'ůѰѯӅԛ˘\xadѦшбдјą',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 459851.9866548608,
                                                    },
                                    },
                            {
                                        'name': 'ˣɂȆ\x92/ͻԢɗʥαßñ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 726851.4423506267,
                                                    },
                                    },
                            {
                                        'name': 'ϯɴϑԗ·+nΞҫѧɤŴЊġƑȽƧȐԙԍҒȍǙЊÐ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            826405.7565029359,
                                                                            850145.4716910176,
                                                                            636196.3153430988,
                                                                            472768.8874125463,
                                                                            681046.934572546,
                                                                            -42280.10840590566,
                                                                            486803.6812435399,
                                                                            980678.9418274562,
                                                                            381764.75841957296,
                                                                            625631.5970488838,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͼΐēΥєĎЋєсѪ˪Ȓ {ƻӟƪͼͷӆ{',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '¤ŧԜМÏԥӂP~\x8dǳӻG\x9a#ӄ½ʙȜѥΙǲ*¤ļƒЉȖιƞ',
                                                                            'Ůǔ¶ıįǌΟmĴ|wωVɌ˚Õņȫȴԝʎƭ\xadÁρȧƐ$Ŭʤ',
                                                                            'ӕʗԅϮҐ\x94ɻɏΎĴǑϾĆʟȹҶҩӚĎʏț¨ǼʋчVKϜњ9',
                                                                            'ƝԁŹПԕ5Ћɮʟ˹ԞˑűͻͳůϖȚƐEOΛӬʕƮ®Ţȸyé',
                                                                            'ǒėԌ¶ƏʅħÛ˫ʅνНӀͲϊƃ˺ǷкɐęǃǤΩǀˬӎԘɻɩ',
                                                                            'Ŀřɠİ\x81¡ļʞʅÈϿϊˑїǚ·хӺΣ*üʕ˕ʾ϶˯ģǳˬŢ',
                                                                            '\u0382șɽПÚǏɴșýńȐÃҁѨ@ԀԨԩʮΆҵcǾ\x82Ý˴ϋĤʠ˾',
                                                                            'ʑͲ ұԭҭȋӚԨğ\x9aӏΑӰǮЙͺĝʕ\x8fǇōѐǲԕ»ƑӗKƭ',
                                                                            'ŸĄҷΞԗȚSDɃƍҿЩŨtɓɅǠҿɐԏǚǠŗ\x83ǜӞ×ȍþŜ',
                                                                            'ɤғöƠȂҶàșђϐǯԎӶˣ˖ȚϾÄͰ@ƲčҏˑmъƃĈʀĠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'φ˽<ΈµеКTƋ¡%˧Ϻγ˫ģѨƋ\x89҃ŴӶлƿ\x93ϲȻѣѝď',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǡɝǿќ¡JʏǨƩ˻ɷƚȔʾ\x91Ήʯ¯ʑ%Ҍѭęәѳ\x80°ұүJ',
                    'message': 'Ǡξ϶Џ¾ԭЈЇΏēɳЂΡЊа҆ѴħǠѾŒǆÛƵȍɼŋ2ϧϑ',
                    'arguments': [
                            {
                                        'name': 'ˤˏνŴɃȋЀ˅ͳƅËӂӗŵςŪƊΣʑқ¿Δ6Ù~ЉΫÛΝą',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƏэǁǅȹFɭÍ>ӎęɕйуɯ҃ÜȀүɫǭϔԪ·ː¥ΘΤɽ~',
                                                    },
                                    },
                            {
                                        'name': 'ӝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 971941.9736382647,
                                                    },
                                    },
                            {
                                        'name': 'ʽ˧Ŏ˗ˊǝåŃЫÄŶɪЍ?ҦŚȴҸč',
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
                                        'name': 'ƥɱȍȗïѓԨѓȬɋԍIШʹG¾ԤԕуɊ\x8f»ʋ҂ӂɷЫͽĪƇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3693142993630954788,
                                                    },
                                    },
                            {
                                        'name': 'νҴԦłÉϏԃɛǇЩѨѷȁŇʻѧʚ`ʝОѴȗҺ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˣƤԅÖáʺώšŗÆҵŁŎQԄRЍд',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201604.159146:+0000',
                                                                            '20210909:201604.175043:+0000',
                                                                            '20210909:201604.191861:+0000',
                                                                            '20210909:201604.208212:+0000',
                                                                            '20210909:201604.224643:+0000',
                                                                            '20210909:201604.248289:+0000',
                                                                            '20210909:201604.267710:+0000',
                                                                            '20210909:201604.283801:+0000',
                                                                            '20210909:201604.300530:+0000',
                                                                            '20210909:201604.318220:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҇ǦŹοǹĕǱɿΕѝɱѮsΑʋɊƖѕЏƼϨȹĕԎǷǿц˙уK',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            736962.8263472453,
                                                                            83238.07318809407,
                                                                            744732.4506802897,
                                                                            149826.39039738395,
                                                                            380314.9918237293,
                                                                            851771.6993753442,
                                                                            682614.3025251987,
                                                                            947229.961782736,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϠƮҸҘȓƋɞûΒŜǻѯƲϭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʢǻȳã',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -12002.124076336113,
                                                                            344066.9744795033,
                                                                            362078.70299406064,
                                                                            311803.3688089423,
                                                                            246124.78803145984,
                                                                            911010.8549547953,
                                                                            560290.6007168633,
                                                                            530858.8818822902,
                                                                            175591.55930674146,
                                                                            -29983.634179791974,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˬĩЉҷʟŵɲƞ/ǃ¶Р ь\x9bǂ\x9fʣƠɱˢʻ<ȦϔΆĲ»Гʩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǀʤΜӚèŒӣ¸Ò˩ѯȱϻö˜\u0380ʟԪЊ\x88Ѭη£ΎѣЋӘӐʂп',
                                                                            'ŽφƬƒĵѾʚφ\x9c\x81Ɏέϩ\x88»ŦͻʗˬdϞԩzӽªŷCβРǙ',
                                                                            'jέlѪӱϱґÝθA\x8c¼ŵȸa\x84ĩɹӤύ\x90ġωҀμюôϨĺӛ',
                                                                            '³ԈЪ҃ŞͺϦɾıʆȽŒEʉҠјĴˮКƬŕǭчҲBā\u038dϛΝň',
                                                                            's҃ĵåČˍɬ´ýΖΩǩӛƋJāԐzǴ4Х^=ӂūνǁЊЩ˻',
                                                                            'ĲԐζzʄKģˏϨǆӘͳŀЊϪĥЧ\x8dҩ\x8fȝƎʹ˖Ɛ˃ɍd°Ȉ',
                                                                            'ӆŖӿèÔȲʧǪ&¶ˣˬƹӍǓN϶Ƭ8Ǔ¿чόȼȃԑȷĖєû',
                                                                            'Ҽ{·aɏΞΊďńΙȃǃѫҡάіԚЖÉFÖʝϫɶýɴИ#ј\x86',
                                                                            'ХmȌԓƧȰȣШͼԂȱ˄ҥ7ĕƐɋȰÚʗӒǮБĜ\\\x86Ķтøӥ',
                                                                            'ϛϭԉhϬːĀӺɬƎǹ\x83ЌƔȮƮƾŰǈɥǤŻ\u0381өͻʲгμʴΥ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x8cѻ˓Yѯǿ\x9bʵԀȃƚӭɏǐʪŴɱËíԪ&Ȋɪ\u038d}МÇûuɄ',
                    'message': 'ǃʏӹыĵӍԟIмӓqŎǼWїʌԄʋˠ6˗ƁБʪϾ?ԮӉ(Ʃ',
                    'arguments': [
                            {
                                        'name': 'ϐNїͿöÀԊѸɍҘĠӿő˅ı©ɟɝʢŊǄԫЁŦȇ\x89ψŷȞÅ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3507190305991942724,
                                                                            8431919349372686977,
                                                                            -1094673400219885898,
                                                                            -318801815322799411,
                                                                            1555679482988491115,
                                                                            4594117960119260892,
                                                                            -4470396725397059822,
                                                                            3273526262005814775,
                                                                            -408099697088103630,
                                                                            8194534531022608757,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¿ƟCӠĂɧҽЩҰҦǲџ˘ƁΩɻËЈǅê˪^ɭϩŤ˩ΉŀɽÞ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 727547.1782217531,
                                                    },
                                    },
                            {
                                        'name': 'ʻӼ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            166372.14028860343,
                                                                            918637.3490312882,
                                                                            289606.62870031636,
                                                                            359982.89405291696,
                                                                            101005.69097331827,
                                                                            836113.4551574559,
                                                                            318981.83130124566,
                                                                            98200.31120455044,
                                                                            577923.233660047,
                                                                            719091.8588121191,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ßę8ϓ϶ȬñØ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            777054.7399985463,
                                                                            545599.5578574139,
                                                                            270185.83624995954,
                                                                            687767.4941876106,
                                                                            -99952.23423302517,
                                                                            282242.3368327646,
                                                                            503489.02094441664,
                                                                            698014.7885006992,
                                                                            768662.3284459575,
                                                                            408093.07142044266,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЭϚцɨŚˑϲԔҨˢӛȗϒӑƸԧ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ДµPĖŮΌʯƐΘ\x8dѝϢõĄΰԍ±сτӸ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 458974.471451142,
                                                    },
                                    },
                            {
                                        'name': 'σΝľc',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201606.355780:+0000',
                                                    },
                                    },
                            {
                                        'name': 'τУτʞӰɽΤʆƵӾυĳƦȊěƙ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӥ4Ӟ˅ҎȢ˹ɗԑɷǩͱɨη˄%˸ѤŦˑðƽŋ¦ƙřЊƁƁH',
                                                    },
                                    },
                            {
                                        'name': 'ϻɱƟӧў',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            483738.3465244429,
                                                                            588109.7526145412,
                                                                            615468.7362096488,
                                                                            478168.24371801724,
                                                                            700835.4373586933,
                                                                            180682.15129563364,
                                                                            514638.1366751696,
                                                                            909664.908464095,
                                                                            219861.32258912362,
                                                                            -98383.77067484782,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϭ`˶ѧ-ˉyϒД˭ɦˬɈǋғΜѥν®~ӎҳəγŎА9β/ԭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201606.733588:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ПЬƽʶǭӥ҃ǿϗϥÌѦАÉ-ƼƝǅčҦҿœA\x93ʖȘŜǓРɕ',
                    'message': 'ӲРyňѱϰĮі˜ʉԊǠÝӎϭԜɹ8ƅʲcüƕӭϯμȑÔīǅ',
                    'arguments': [
                            {
                                        'name': 'Ơĺǜ}ĞԬƉɶѯзŗčɬʶӻȹƭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201606.869919:+0000',
                                                                            '20210909:201606.887483:+0000',
                                                                            '20210909:201606.904558:+0000',
                                                                            '20210909:201606.921049:+0000',
                                                                            '20210909:201606.937544:+0000',
                                                                            '20210909:201606.956424:+0000',
                                                                            '20210909:201606.980521:+0000',
                                                                            '20210909:201607.002311:+0000',
                                                                            '20210909:201607.019825:+0000',
                                                                            '20210909:201607.036901:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʪâɀξ\xa0ľǉѬŏɽЗϕʐѠĊлÈӾӟˑѓīǏȫŚԋʡӈɇɦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӗʣƝĜЦϨʨӲżΏƿԏͺϳÊτ˖ɸɁOъΛѾȪϛӗ!ϣƥԗ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3167411436778409547,
                                                    },
                                    },
                            {
                                        'name': 'ɀͲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4256736632222939819,
                                                                            9064480960890870338,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʌӥȮŃҿ˞£˕Γěј˗ʗ8ΗϭƢðȦɈρдďɑĽɮåςǨҨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'XӷԝǕ˃ƹɘʌ˸ӾȤɮфǊŇζ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '9ӅˑΗŀ\x82WäȿϞ˯ɭЅӺǷʞźɀӗбԥӍĆȨ´ӰΣҰ΄ǁ',
                                                    },
                                    },
                            {
                                        'name': '΄ӎҳŃȧĺćѲʯЩӃ˷ɬǡǃ˝ω҈ԡв\x8cϼԜ˥Ɠ˰ȽԔþԦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            704860.6858726961,
                                                                            841616.172898906,
                                                                            166989.81526886259,
                                                                            311490.83516373765,
                                                                            768677.7882483256,
                                                                            234048.49621429143,
                                                                            768235.1258818519,
                                                                            823197.059639672,
                                                                            390288.82152737613,
                                                                            967820.9510311142,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɖȞѕ\\ԛԎÚΥǔȊс(',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɏʖʺҔWǛzԪģǱʇʎГ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201607.843132:+0000',
                                                                            '20210909:201607.860796:+0000',
                                                                            '20210909:201607.878008:+0000',
                                                                            '20210909:201607.896244:+0000',
                                                                            '20210909:201607.913852:+0000',
                                                                            '20210909:201607.930558:+0000',
                                                                            '20210909:201607.947939:+0000',
                                                                            '20210909:201607.972065:+0000',
                                                                            '20210909:201607.994912:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Kįʪ\u038dάдԚӣЊϐƝЭ˃}ҥӐΚWӅӖЬĲ\u0381ԐʱǊѺ{ȡʧ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201608.099470:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ȥˀ¤ϾѢʙҩǈ͵ŭѱɳǏƀϷǃǻý4ŴΨ&ΪˑϐαɚīČͳ',
                    'message': 'ǪŁԣǭάĽʴJ҆ѽΊԜ\u0378қϱԭЋ;ϷɛӰΟң҈\\ʴĮ˝Ÿȣ',
                    'arguments': [
                            {
                                        'name': 'ƢжȰʍƁÏǕɨŞ\x84зP˵¯%ҧҜͱɊŖ:|´bԄη',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            577506.228698065,
                                                                            332632.73028175754,
                                                                            560486.120699559,
                                                                            270756.5595878087,
                                                                            536028.1407799793,
                                                                            476153.62751718203,
                                                                            203036.31896325917,
                                                                            30455.648998727862,
                                                                            651780.050636746,
                                                                            419153.99188362394,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӄƀ˴òϛТϣʴ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '³˻ԓÔʺøɭŇȽ˳ĤƧ¾¤ʃFҁƔъРө¯ɯ\x7fˡəдϓūӈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -14167.249412949313,
                                                    },
                                    },
                            {
                                        'name': 'ŧˬΨ}΅ǹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΟЃ\x87ϺŨŐɜЦȂҔĉȡƚϖюĚ\x8bz˵ĢԋΚЀpЄάɬǾʭю',
                                                                            ')ǹǃ҃ɎǙ\x85ТьϬЅϹԊ¦ǪȰҹɬԏ?ȢԂԝÊ΅±Ԍˑņà',
                                                                            'tԚðɛҘϜӿҞκ\x8bƬȴɜŦӉȌͿʚЅ˴oȬ$ǾϹʕγ\x9fάӥ',
                                                                            'ȁ)ǡӖ˴ǖ\x82ĤХѩҐҍʡѺɝ:ͻΗŕʝԝÅȠ6Ȕ\x98Ř¡ɐ$',
                                                                            'üӒˁưΕҏԫʴ˰ӚφНǒˎѸȒȉʾėʹĶ˄{Ѳ\x8fȄ˓űƅȼ',
                                                                            'rͻ¯ƨϺʔρƳƌëʃзÆӲ˪шųÆˢƃÓʄǲ>·єҦ;˙p',
                                                                            'ό˙ʽҫϰz˧āӌÂˊӚƽǟāУÍц˾ɜӮȦ?ϚӴԎ|\x8cμͿ',
                                                                            'őɪӿĆè\x87ːɃЧȥƮȒɊįӂŘĸÑʇȗʥ¹ԥàoќʤɖц2',
                                                                            'kɴ=йѫ]F,îәwρ#hŊƕѤŭɸҗȇíć-ҖʣҗʘҌʜ',
                                                                            '΄˜эѭȈ\x89f¯ũԣϒµӬMÉțҗ˟\x7fςͲбƤɆцJÁʐяϵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '!ҊΐцЮƺƉЁԗυŏ\x9aņʛѕҢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            616076.3847511096,
                                                                            50665.40508256847,
                                                                            553986.1214375877,
                                                                            55678.970225005,
                                                                            664224.1189872905,
                                                                            463789.03272193146,
                                                                            276573.09842007427,
                                                                            305748.2541543944,
                                                                            379252.1466779586,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԝʺɦґ\x82ǷÆȓǴτһҢɅ®ӎľšŦƇǌ҃ɚĪёʽч',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 92245.71621370487,
                                                    },
                                    },
                            {
                                        'name': 'ѝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 748253.7890974393,
                                                    },
                                    },
                            {
                                        'name': 'XЋșɳН;ԉĒƯʟȵüӳѐˬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'eԏԭĂєωȇ\x8cИŃЏųˆʲҰÃĜ˜(ˤz\u0383˪¹˱ʦѻ\x8d΅ͼ',
                                                    },
                                    },
                            {
                                        'name': '҅ěҫȻʻ˨\u0383ƹ7ӊſԊЧѬċŤ\x96ȇсԅĀïČ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201609.483652:+0000',
                                                                            '20210909:201609.500951:+0000',
                                                                            '20210909:201609.518335:+0000',
                                                                            '20210909:201609.534876:+0000',
                                                                            '20210909:201609.550556:+0000',
                                                                            '20210909:201609.567137:+0000',
                                                                            '20210909:201609.584947:+0000',
                                                                            '20210909:201609.606047:+0000',
                                                                            '20210909:201609.628455:+0000',
                                                                            '20210909:201609.650047:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѭАęľJɦþӚϩΉѺĢ˯ƥÇƣ˂ѠtɓɉǒИвғҀjӋȳԦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201609.739250:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϺŵÜǝԓˋЄӂӁɮIӽӇʗ˖ΤħԬƯŃƞ˩щʳѻӅα϶XԤ',
                    'message': 'ȯƞĆФġϫР\x83ȓŉɇǤEʲʶϝҼϱïɱҜƈʔăǎѤӶɹ²Ŗ',
                    'arguments': [
                            {
                                        'name': 'ΩɃвƦҋӈѱƑǿϘАƛʲȬӬх\x8býϷȀӣWЦʐǱ\x8cʚȨɷƣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            749777.8635439425,
                                                                            441891.91789716936,
                                                                            362906.97053721425,
                                                                            233135.5269001255,
                                                                            683591.8550380988,
                                                                            -9827.3581884257,
                                                                            690595.2764120849,
                                                                            -12932.96650850284,
                                                                            940493.1501256982,
                                                                            679433.551502741,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΟŝǰʌҥмӴϒϳ´ԉÍԉäΊ¥ſɒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '^ˀʬʲǛҠԈͰԉŨÞµʺȵχőśó҅ϐ,ʢǯȔɽ1ǃғ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˨Ż\x9bĜӞʛʊSτʱȑԗˏӧȯȺ?',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5753370331639058771,
                                                    },
                                    },
                            {
                                        'name': '®vјͿќτДȑŊАϔdĮσǔтƧіŞĨŶŤЗßгƉΊɈϏɑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˜ɷòыǖɸ§űԇћȃåˇǽˉӪĲҒ˫йĊɗɖǅî˙«\x91ЍǕ',
                                                                            '3bÛĭȳ˱ŠƐԏʴуǑЉĹÓЉόεΧùͽǨ҈ЦΒéPéɼ¨',
                                                                            'ϏʶԠ\x97ԣn\x95ɇϊӝԑщœҀǂѤŘąɋԨҭϘŮƤǆɤФƆHȧ',
                                                                            'ˌπƀįȩɽÖɹǉ˴ŀŃϲč\x88˾ӷǚȈɺˁ˸βƌĪ\x94Җʿ"О',
                                                                            'οʌɭǭɏҔPҡӳх,ȜӥǄҍѝΉήŽ˽ʣŚʟяϻƭŚϥҹҫ',
                                                                            '˴Ìǫм҄ͰY4ͳ\x9eψóʞӪҝƟȐҠ\x88ͺǥР҃ľӁŐȁÑǯԍ',
                                                                            'ҎͺӤôĊКϽȦǚβȎН\x92ǈțĴҡϾ-\x88ћă!ɓъЉиĈÄЍ',
                                                                            'ӧϢ½īĒ\x8bŊв˼ɭ¿ȢƜЂǾ_§K$ģòɭòąʝΦη\u0378Ď˘',
                                                                            'ňĤʺĶ#®VѪćӪȦƏϊԭʒǯ8ɘԚΒzψЂŒȂ˶ʈÕ҆Ү',
                                                                            'CѰІkʧӈóŽ˰÷ȇƆ˂ļȐ\x89ƥ2ÀҭбΧǀy\x87tѓώ;ɸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Łº®Θą_śѭ\x83ǆ˔Ō*ӻҹϗҜПɾʸƗάɌԈЛɏѯǚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ȐЍÂԭѮϋlê˶Ɋ˳',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201610.940800:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԟ˦ΚЏŹϘΫǇ\x80Šëλɒòʞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2734034335261673343,
                                                                            8515883572051016951,
                                                                            7522100831945814881,
                                                                            8347095605495742111,
                                                                            -6304941134093862462,
                                                                            -2785233963242074034,
                                                                            4088717009715696397,
                                                                            2457880192544975048,
                                                                            1544575814499631038,
                                                                            7738672825579936366,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÀӵŜʺɻǑķɁͲϰО',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˲Θ;ҏěǔ͵ïσѪUcξìԜƈǴӈ˩ŭJϺЍüŮň\x8aĵҖƘ',
                                                                            '\x8cɥěżѰΖ\u0381]ȫ\x88āÍН[fϟ¨šàɸÇД?ɥĔʏԃϸƵԉ',
                                                                            'ҦͽԮǦ!˜ƚѝ\x9fƚЏȮyŕωĐѣΑȁMҌĊƷÝŃԪʮ˟Ӏ\u03a2',
                                                                            'Ұǈǚ҅ςɍЦÔǃŃӌˤŢγ\x7f¸Ѯƾ\xadSВ§ȸ&Ǭΐźʏį!',
                                                                            'ŹҾǁԣɚƕ˼ʊЈĻˠſѦɂνІǥϠҢƒϯèфˡÎǳÚƌїɜ',
                                                                            'ĲγʮZŽ˶χԉЎӐѶ"ϰ\x84ɸʠϕȇΎл˦ҖψэŽɟʄΛz\u03a2',
                                                                            '×Йȫ·ƴÀāа\x88ԑϷ§ҊȲuƦαŘˠԝȒ?yСξǽΐΐ˽т',
                                                                            'ƵϵȂȨiҵ\x9b˨sиŉҺΐϡΕˮɸǣϟˎðѭ϶ӑȮκĎëĆǽ',
                                                                            'éīфцäLƛӏė˦ԃŔǇԙ¦ԦƴÙӰʟӕ+ȂΗ΅ˣӘ\x82ɱѩ',
                                                                            '\x91Ԉƙʢ˗əηǲ˚ȃİǤέΗƒӘuÿҪǗʃÑп҄sè>үȩZ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŨЊ\x98чРϨɨư±ſΒʿŸŮΘщŃҟøӵϞцɪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӗͱ\x98Ѫ{ͺiʹ˼ĸκʾǥɁοѨϑKѽŔӿңԥśǒūŒξMќ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ґɸЧԎ\x9dκʾљǯǾtĔӧƲǉϻǆʬǶϯ·˲ǋƝΘѓ°ѣ˵Ž',
                    'message': 'ʦȔƣÆƄżĽрӳƌӕͽǬʡǥȗʂȂǕǥЇȼυŴɹƎķΉȓë',
                    'arguments': [
                            {
                                        'name': 'ÞŅˤˣ˨цйɅӗϹĻåʉǅȹȂΞǯsŌʲԉƙŵ"δΧʎ\x99Ī',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʔҌόҀҒеғ\x9aÿѮ²ǩ\x80-\x9e±ͺŹҘ΄vӬ˶Ĵ¯Ϊ˘ԄtԖ',
                                                    },
                                    },
                            {
                                        'name': 'ЪзɧȡѳÖWrǥϻǾӧϡϐųɁ´ƬФϝӽҍȹʆŘԚ¨Ͳőƹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201611.685101:+0000',
                                                                            '20210909:201611.706237:+0000',
                                                                            '20210909:201611.724378:+0000',
                                                                            '20210909:201611.741306:+0000',
                                                                            '20210909:201611.756751:+0000',
                                                                            '20210909:201611.772811:+0000',
                                                                            '20210909:201611.789140:+0000',
                                                                            '20210909:201611.809769:+0000',
                                                                            '20210909:201611.827681:+0000',
                                                                            '20210909:201611.843153:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƝˢěɫŔƂ΅ҞèйǖӷĞǏþЎѩѾҍƿ˷ҴƧĐȶ\x8dѢũèƣ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201611.926806:+0000',
                                                                            '20210909:201611.943782:+0000',
                                                                            '20210909:201611.960306:+0000',
                                                                            '20210909:201611.977123:+0000',
                                                                            '20210909:201611.992600:+0000',
                                                                            '20210909:201612.011422:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'N҇ɓȽÌɺϨÒɧþˉű϶ɱϼǴΜӽ^ϓĮҤҩȫяư\x9dӲa',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6826338769826519345,
                                                                            -4906163401591723137,
                                                                            581619403238898706,
                                                                            -5405842906520519565,
                                                                            -6258722383548574200,
                                                                            8589096054575355101,
                                                                            -4886413313551549581,
                                                                            -1203892246699802408,
                                                                            -357749913049146605,
                                                                            -7188596349885068304,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˼чęоȿӌƄȉӷȬР\x9bΦҝđ\u0379ΏщѨиϘʧϡ΄ʽ·ӅǚӞǩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            42512.4163037111,
                                                                            898604.1807989656,
                                                                            448954.3381620303,
                                                                            655471.0827267561,
                                                                            161587.90105203423,
                                                                            527759.7432815295,
                                                                            755352.6770295291,
                                                                            278354.8407414672,
                                                                            119285.91326227243,
                                                                            77776.63607964304,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'оΪʤИƎϖ\x9eӊÒΕā',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƭ҃ѦXѰõźÑңȁh\x9b',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҐӈԤĘ/ӣʧ˒Ș\x93ż£ĲъƑȯʐƬŠåάҠȍŉĥɭjЉΏĀ',
                                                                            'ˁʤɵҲˬʺќȴϐɘś\x8f±ċ˔şΠěѰ˓ŬҰσĦȎГУȅϐќ',
                                                                            "Д'ХˇÞΕȫ\u0381ԓӗԥɻ¬ϕÒłηļοĠɶŊҳ?±ԉƕ\x99Οµ",
                                                                            'ɵŧε|ІӨǘϸнӮӒĐӳϺӲ˽ҿ¥ɚΜŖ˭ʘΌȨɖǴͺЉѽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'bǠż',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ͽ\x96ҏЬԌɬøą',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ћŜ˔ƞӧH˒ű\u038btТԗΧѺŘ9Ʊȅ˔ţԂɕŎӐҖ\x9bȴ¥ѭʚ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 26298.016404676295,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'μʢ?\x99ӘĞȯǍ>ҾΓΎŚĈÅе҈ͷʙŐЋĘ˕ɖʏҴ%ΑƦ',
                    'message': 'ɹȱʙѐï\u038d˳Ћԕѳ\x81ХAsқőԖʞ\x9cɘį˒ЅԠĝǽɮɜӠΉ',
                    'arguments': [
                            {
                                        'name': 'Ԕûʀԗì',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҹ˙ĹƖƉЌĥϹˀӌˠȠďϣһ\x93ĜâѤ@ӓɩΆÒӷҥҳӾõ\x95',
                                                                            'ŝΝÖ,пʴȪŸєƠȷѕǇ_˖ŇȩǤӏѳШȯŋơϓǃʆъԗ\u0380',
                                                                            "ǖЈоķ'ͽ΅ϤʺҜИαλƓȽеĀÍϼґϢŵӽĐʱŉѯɭ³ʎ",
                                                                            'ˏˀǳ˲ԓҬwҽͻϑʒǫǾЁʣȹχͻӱðϴԧƓҕîԀɨËÏÀ',
                                                                            'ԫвʑɄȯɉĤȯŹ5ӘǣƉ~ӳƩζѼȵї6Ѷ²~ɴ^Ҟѳc½',
                                                                            'жЖÐĨѫZ·ʕ˕҂ӞԍĉӋVɗǷͷź΅ˍÇʩϋŶǝ˨¨Γ˼',
                                                                            'έ0˳ȅɘбʝŨʨƋѭϏЏӍϟƚņΌʏӅϥāƿǿˡҟCԥåɏ',
                                                                            'ű\u038dÃĹӄѓů\x82Ѡ4ҾӾӬŻȞƟγӭ\x95\x82ˏ!ӸĎԕҒËɴ\x8cӳ',
                                                                            '˷ˮê_ӮѾ£ѐ¼ËϊéɎ˝8ǓɎηǶӘʾͷÖțϞҙɣÃБә',
                                                                            'Ɂ#ƷãnԮ\xad\x85ƻҌӳȶЩ˥Џʻ҅ʔԐŦ˒\x80ʌȴƦƱ˹МҗԜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'сaή]łǺĨЃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1365310146461836707,
                                                                            7396733385134135210,
                                                                            -7524190699494407215,
                                                                            -5987114019614351672,
                                                                            -1761602575672301614,
                                                                            -4425170009161769673,
                                                                            -749080568070365233,
                                                                            8950179312618919210,
                                                                            8164333691114441235,
                                                                            4702157915476574977,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӯ®ѧӦɤÃ\x82ҁǱԎ\x91ӸĳΫ¬ԆʜǮэ͵ĆƭȹƁƈ¤ɮͲˏ˯',
                    'message': "ȐʢǃȐɚГ˫ΙªʏěҶŤ˫\x80åǦœѦg¤ԣǌҕ'˪ўƓ´ɞ",
                    'arguments': [
                            {
                                        'name': 'ǃĦϋŤЪçΈʞҳɿԃӈУ\x8dʘΓ˥ȝʡʹ˷ǜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ќԓɺƛ·ҧƙſ¼ζχʲԥʥg҅ªėэυħ\x86ǤҢҋҪƾϳĚǄ',
                                                    },
                                    },
                            {
                                        'name': 'ӂѥЍòԩɓϐҙƹǹ\u038b7³σʩǎɆːŔɁʾԂԆƓҬюĕǝʹ˃',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201613.859774:+0000',
                                                                            '20210909:201613.878742:+0000',
                                                                            '20210909:201613.896227:+0000',
                                                                            '20210909:201613.913518:+0000',
                                                                            '20210909:201613.930224:+0000',
                                                                            '20210909:201613.946882:+0000',
                                                                            '20210909:201613.963352:+0000',
                                                                            '20210909:201613.985025:+0000',
                                                                            '20210909:201614.004825:+0000',
                                                                            '20210909:201614.023175:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x91\x90ĲůӢƖ°Û¯9βȌĩåƃÕӥɱȁ˲ŨëƉȖǣӇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201614.104349:+0000',
                                                                            '20210909:201614.119775:+0000',
                                                                            '20210909:201614.136012:+0000',
                                                                            '20210909:201614.152260:+0000',
                                                                            '20210909:201614.168118:+0000',
                                                                            '20210909:201614.184005:+0000',
                                                                            '20210909:201614.199657:+0000',
                                                                            '20210909:201614.215999:+0000',
                                                                            '20210909:201614.232215:+0000',
                                                                            '20210909:201614.253038:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѯˏѳ²ϚҕϓɳӞʬɉȵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201614.334584:+0000',
                                                                            '20210909:201614.350290:+0000',
                                                                            '20210909:201614.367284:+0000',
                                                                            '20210909:201614.383181:+0000',
                                                                            '20210909:201614.398786:+0000',
                                                                            '20210909:201614.414645:+0000',
                                                                            '20210909:201614.431090:+0000',
                                                                            '20210909:201614.447601:+0000',
                                                                            '20210909:201614.463769:+0000',
                                                                            '20210909:201614.480952:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȧԒϮăӰϊчɄŚ+Ҵɼ§',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7124336073700848477,
                                                                            2924675694995473607,
                                                                            2511113664653420339,
                                                                            4675548583639467147,
                                                                            6542898794649123025,
                                                                            1053235352314761518,
                                                                            -9106699451399044982,
                                                                            2233630966936948229,
                                                                            4033435347391472118,
                                                                            -6116634305378243138,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ʗ'σqΈÀƊƐĝʣĆ}ώɷϓCɱĠ¥ԥȿǝŀԪɼӾ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201614.815409:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˤ/ǞЮёpǥͻкŞȵΊXӈјӦĈ\x94ƎѮƃҮʔЯЈïòΠРİ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2056297699714429982,
                                                                            -6730915735597633089,
                                                                            -8546358686161693609,
                                                                            -3804746092667794576,
                                                                            1380753649148814463,
                                                                            -1186420250208070516,
                                                                            8431946178822897332,
                                                                            -5586867606879517598,
                                                                            -7841598354426314486,
                                                                            8778868649056416323,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɥʫńʞűԪԧЉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -83656.79671293056,
                                                                            368188.43933962914,
                                                                            709306.5284295816,
                                                                            625147.4675680316,
                                                                            317719.8932340159,
                                                                            368710.9137646888,
                                                                            422110.73032440443,
                                                                            808697.332961597,
                                                                            -36500.36306798903,
                                                                            159757.79569380466,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɺЪϥѓjȄ\u0383ŽƽʖƞϱȮƼĶĈśƪǆİϥЫҽǕÞƐѽɷˆŔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϐѕдϬӱӪɓεķϷңȆjΜϿΩ\x90ʴ(»±ΔĎhрȺvҮшѳ',
                                                                            'ӬÙōЯʚą˙ţ\x88мΝʞǱeԦЋʁıƮιȘ½§Ȅ!ϸşşӎѻ',
                                                                            'ԜōȄѪӆҠȟЅΐҨhҖĢΥԅ˂бϪǞҺeХƒφǌəϙϝƆԨ',
                                                                            'ǒ±bћΉ϶Ǌ\u038dћɃȁ;WŵψƳy˓ɝƝHϹȽȢŶͶŖ҉ŉџ',
                                                                            'ԝƱ˜ƦϐǤӮĞА¼¼ɳǣΟ˂IţȬɯȍӡQĝxɍӬã˻ͱʖ',
                                                                            'ŤʰЎ\x84˂ԏɽɽƘ\u038bԣɓŤҡϚī\x8cΟǘҳ˃϶ǴəΩɼҟƜ\x86˜',
                                                                            'ɑΐŉsʷ˟˴ӴǊƌƤŰȅΡȜАӝͳȩ˗ɃʧϜҽЛnӥȋ˖\u038b',
                                                                            '«òǡ;яοÅϭϝΥȅǢĥÏ¹ƜўѕˑƵʰ9ΚØӃȻǏѵˀл',
                                                                            '\x86˙ÆӕĿÚƵ˰HЏĢњΤѻѴќɵ/ɀʕƾ\x98ˋ|σƓԗǂǙĨ',
                                                                            'ϏǏ˦έȂ\x9bНÄѪѓԭчŝ˻ƅôƏö҂Ӄԝʹѐϡңʷʰыʸˋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѢlҖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201615.579635:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȣəчЈͱ˂WχҳƼvϴȀɨӻԒǀĦҎͲXŶ-Č»ȸМҏ҅Ў',
                    'message': 'ϭβÞƝǹȵɟΧɽēӤиßǽӝȕϺͱ¹ŹϋƞҊϷđȨ®ϔЩ˵',
                    'arguments': [
                            {
                                        'name': "\x97į´Ĳȏ/ǋЌʢƒʺ®ʫʉ\x83ȆěƂ<'ΡҨǻōõɅƼɨī",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 728549.5564835628,
                                                    },
                                    },
                            {
                                        'name': 'ȚǂѬĠЫȿɱҗȭƕˊҽІǁхүCӋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201615.789303:+0000',
                                                                            '20210909:201615.804928:+0000',
                                                                            '20210909:201615.821374:+0000',
                                                                            '20210909:201615.840423:+0000',
                                                                            '20210909:201615.860371:+0000',
                                                                            '20210909:201615.881694:+0000',
                                                                            '20210909:201615.903297:+0000',
                                                                            '20210909:201615.918780:+0000',
                                                                            '20210909:201615.934531:+0000',
                                                                            '20210909:201615.950590:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȖѽĀϒmĴ˄ǨНΛΘџʴȽ˒Äщѹ°ǷʃΛӵřЂπɫHЌ˪',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4782339129129517491,
                                                                            -1096335473910316244,
                                                                            8984683279668744785,
                                                                            -1987189297605345269,
                                                                            191092778873940922,
                                                                            -210088781805053235,
                                                                            -5832621442900413595,
                                                                            -2482548500696738164,
                                                                            -6638924439947062395,
                                                                            -294826504615231227,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɪ\x9aӧ\x87ӣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'рƣɛÚɠмԅϒéŝϺӠмҸɡόɤПî\x9aԥҦĄƷžȨσŋʈΉ',
                                                    },
                                    },
                            {
                                        'name': '\x8eɤ˨\x9fɕ\x9cȎŶȌƌѹ,ÂƴÈʀϜϩƏ˵ÌŉùʎoԆɪ9Ǝt',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϒЉΌӖуĎҹҘ\u038dƹЇ˹ηѩΞԞʈӏǕȍʐϊÑſťӥ˦[Ʀɓ',
                                                    },
                                    },
                            {
                                        'name': '˝ɚHЧǝγ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 143120.40380227176,
                                                    },
                                    },
                            {
                                        'name': 'ԭŞAkV\x8bȤ\x90ŦӈɂпȳŁμȪԠǹҰДǀΎҒӸ!ζҀΗӬϠ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': '\x9e3˸ǎҒƒοɤǥƟƓɀȶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 490718.3209957633,
                                                    },
                                    },
                            {
                                        'name': 'ûӗʫѩĿѲȱїҐЏÎ$ŊУɩĒƷŕzÙϑǒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǡéĺ³ƺϤǪŔɨΔԜƗҧ҃ԝʼőŬҽкŅϤӘćɔЙӍʤɚƶ',
                                                    },
                                    },
                            {
                                        'name': 'ћȯǡѤ$ыċτƞčӒǩĎ˥ĥҞˈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 707375.400927518,
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

            'identifier': 'ФԅӣƵЂ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ȼҢ',
                    'message': 'ž',
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
                'identifier': 'ԨƋģĂкÉƗőƼΗҌǺӆĬϷɇÜłʠ\x87þʱ˗ƦŘ`ǖǰŶw',
                'categories': [
                    'file',
                    'access-restriction',
                    'network',
                    'file',
                    'file',
                    'internal',
                    'os',
                    'access-restriction',
                    'os',
                    'access-restriction',
                ],
                'source': 'gǉϥϬɔÁďơĚΔԖ0ρƒʑŎʏĬ\x92˫νƞZʡƲǰ~Ȉ?\x9b',
                'messages': [
                    {
                            'catalog': 'ϯɭԜәǔƅ;ǊåɮӢˢӚɳΤʞнʈҠԩˬҦê\x80˒Ȕʈ\x86Үʢ',
                            'message': 'ԦŤȧƧΔłϫǭҌδ\x7fԅʶӝАȡьаȦԮʙʼȬŐɪьѨƩæЩ',
                            'arguments': [
                                        {
                                                        'name': 'ҁGлȡӡĀ˗ǚŉɄɋȔĸʥҪ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201555.559899:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҩӃϞíÛĚÏŎԎЦΆΙ\u038bɊDľ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɹԖxcůĶϡŷєΩЯɀūȝŝϠ±Γ҂ҝȂFƬǘ=ŻɟēϠҍ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƱǐʟæԋʖȗѾÕ΅Ҥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƑˆЀTǍΦ\u03a2ǬçKЊԑҢҼˠēÎѠ·ōɡɏыǠîȿӦÃӖѲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȻʗИ½ƚӼʛŸʃҞѐŖȂƄЯҸӳ҇ϷģƦӋѓҿѧƝ˫ǣǮȡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӪʰɉŞsƊȺ΅áɔɐЩ±hɖБрԤǎЯѤÆρȵÅЇÌΗϪѡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'įǼǩǂΆĲ\x84ǳˡтʇԄīɅÞȌѕʉʋĶǵҙÏŢҨȭěʵѿ\u0383',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĠȸƅД|ÑȾĿƤѮƭϭĝȌқҞѿОϕѻǃɫοұƉͱӱȌӒӦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΘӒ˺ԘμьԎ\u0379ɡɱȱԪԃ˕\x8fҽŸʓȽģ.˚ƖЪçƒљØ¸\x9b',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˩уɕìˢԏƯиӳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǎȺʸΫѪф\x81ЊқʓҁǤ΅<Ӳӂľ˖\x96ӃƧĸѲȻӒȤ\x94ѴǬʖ',
                            'message': 'ǝРŶŘϪĲǁθŀĺӂ\u038bǂӝ˰¦ЊĮ¥ɮ\x98ȷЋɮʝ5ĳ\x8fϬˀ',
                            'arguments': [
                                        {
                                                        'name': 'ãŵÆҔŤėʹϷө¬єȺԈӵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'cҼÿȉzǒ\u0383ϑѸƘƸơƒ\x8bƩȬ҉jǓ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηЍ^рg&{Ƶ{ФʼȽͱɹԜϙ˫ӑí(ɁiǰΐԤѥʒҟɑƚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʀέ\u0379£¢ƗƂʕτ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƐəÊԗʒщ϶ȫδ\u0381ǿɎϗ`ʑɬǛ\u0382\x86ǄŚí҄ņǣυƫ˄ԒӉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȄƧëʋǅӽЮԤɃÚӽ¶мϷϋkϷðµӁѲÏ˾ɘДɆюΜɊˢ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'οΏӁǜɓԖÀіŽˤɂϟҹ\x88ѴϺɢіàԗǝʒƻͽϡѹҧ©ɚţ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4457236741056992223,
                                                                        },
                                                    },
                                        {
                                                        'name': 'āǲɡùҥf˳цЭӉˊǍӟ\x8aǋʯ˖ЋÛ½Å˼',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЙʨĆĞûá\x85ɴ˱ɅӝċźэѯʦҵҠϜěɻɊȤɿɍǻƛäҧŷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӨĠΚʠ҄ҙͲT³РȻąƵ҉ΨæΰưȡƚΓȕΜѡ÷\x95Ӳĳҽҵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1426624859606113504,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ě£Ͱʦ$ƜǍΠĎ҈ŽқΡӧўͿ\x91ɡԑűŷʹőʃǢ¥˷ȽŷӍ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'æǃøҏΧϡŞiʳ\x99ƜÏѴӡɰԮx¨ƫ\x8bĤμŞ΄ɕŅŖǈßω',
                            'message': 'їņһϞɼƚӍҿɃƿͿ˸ Ġŏ\x80=ɪѲʇYʢѽӛЦ\xa0ɯ΅˙ɛ',
                            'arguments': [
                                        {
                                                        'name': 'Ȧřĥɯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6748508414683219715,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύЩÕЇѝπ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖƸǙˠϯȵŒΚзЕӋůȍӱVƗ˧ș\u0383˦ҊьµĜ²Кüɨȭ?',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǼǊɂųЃЧηyӥGϷ{êӘɳýƓӢ\x8bҒ\x85ҶÆơԏȽћԭo˸',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '4Ҝωǯʎ\x9eü7Ʒ˼ȳѸúzШ\\ќЦǨĨˏˆ˺ƕб\u038d˵˝ď',
                            'message': 'ź§nƐ˵йʲ΄ðѱ¡ѤˤӞӇІͷćʚǓʕǞɳӺӘ;ïʡƄɿ',
                            'arguments': [
                                        {
                                                        'name': 'ɗˣԁҿˊВĚƥɲʟДӹҟʚˀыҾʃά¨ÃȞŊáɈӷ\x9b',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '³ˑȕŏʜƠӮԊΕųǒϳæԀǎЊˉǉσσлԓŨҹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'IӃʌL˛ŬʦϏ˹µƓ\u0378˹ǰƂíåϟєԪǯ_ȠZʞªԒҧЌԠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԨǩȂȍǾ҉οЙƤ\x90ϏѲʛǢЖǬ´Z+ЪđʲŚƒĀљīǈ˯ҿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ё\u0383ѐʼ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƔˈўҵɶиɹʭϵҟΏС"î',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƪČЀąǥӅʥԎєΟԉSΕȌGé˚҈҄ɄϥƪЛʯ>6ʴƻțҨ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſǣĭ˯',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 63163.08362733357,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖӶ\x86ʮНӤԁɗΪ³ƚ;Ф©ӽLǶƄǲƐφùŊ˘ƷԀӁʍΕï',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' ІԄˑǕƍɮъ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǞƫʐēqɎэɈƓτèȘȐĵaʠȚӼµǎҗԬϓπɎȸʶҩƱƮ',
                            'message': "ǅ\x8cя\x92ϜÛǪȪ9\x9d˓ĿÌ'ʌѹēџҹÍnɛǃԊџ0ТƎ0λ",
                            'arguments': [
                                        {
                                                        'name': 'Ҁҋ˽ҊӱıºҔƿǮ6@ΩˎԌtԑȰθűƵʯßʑНҒʲςшΙ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˯Ӊ¥ÚИψѭzԘɇΚɗӅ\u0378xNЉːΔ\x7fʀɍƉ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 128128.99298167415,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͺΖƊŚźǔj',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¦ѺŢƈϡ˸ɟϏŚ²°ΧʭГ³87ȳѶʟƠѳЀΘμ\x8aʵ҉ĀЏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 552314.3699698236,
                                                                        },
                                                    },
                                        {
                                                        'name': 'чӳҦǬͽԫÁϑι˵ӸΊƟθʼV˪Ι¹үӗ˴ΐʳǮ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'mѣãǞʱҙǳoȶɡΰʨƪȌƷ\x96',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Кӎ˰ñɄˉϱԋêɛԇҨ\x98ƎȓɑƊԕï+ɻŇÐņҦĐǉE}e',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1361280569694893421,
                                                                        },
                                                    },
                                        {
                                                        'name': '¾+¬ѻӭĢ*ɢȴ¶ŻƌȰĄмΛͿΒӻƵɏɢυƀȮƥƢ˰Œ¸',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÍĿ˝ʢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЛϫˎҦÔԩԡ˖˕',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ȃκф6ԇŭʑңӐ˝ůœūЃ\u0378ϭƁΌʩϽǷǌӶή˼ɘɭƷų\x93',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˘ə8͵ͶĨҹŞҮҘѻТ˓˾Ūƈɘå~ҴÍЅƩ˙ѲƓĦɉϝ\x7f',
                            'message': 'ˇөŵԄƚΈʫǭƚƼѠ¯\x7fСǟ\x8aǔ\x8aʒɬѪО¾ӥĚþҟėЏw',
                            'arguments': [
                                        {
                                                        'name': "WɳɍԗгˡĬnĄĶ˩˯ѧҹ'ŻϨӝͱʓѓЀ^҇Ĉη",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5167486888235573616,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɓaӨҮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3016059926584244835,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԕǐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1981258054906578486,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǈuúǿǿ]ͶŕŞʙ\x90',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '«ƇʬŘÜҋʭϾȀÕ͵ЪϪѭʋϖ7ǧĵņʷˋģЪи»\x9cǽКԁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÑʟiÇƴʈΑăԙЧkʐȠòВ˕JɂΙɣώȌQԎѣшȱєǰť',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'íɥ\x8bʺӑż',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'АÏɖ+ӜɅ\x82ЯѪʾѱΡīҲсʨӤϖģŰάѭɧӽ©ĶƐʜŴĪ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201559.424530:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЊэƑĥȶƆԓȡŲΠАıϢǥ©ȍĎӭϼϣ?˴ĲǢďκ\x84ҚϦƠ',
                            'message': 'Ϭў\x93pĐhʻҜԟ½\xa0Àү˷ǐƱʛŻʇ\x9cύƐԁǶȷԊɴеѷȟ',
                            'arguments': [
                                        {
                                                        'name': '¨Ѫ:ľːŅȇӾæ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˕ΎԂĘғΟ҅\x98aϔɹ^ќuϤϮя˦\x98αк¶ЎҠ³5Қķǯϐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҐʂнƪͷiȻȱҌƙȮ΅ĿϡǪÎȻɤʤ\x97û',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'їѵ©\x82ИƉǯŔÜѫȦħŨȆ\u0379ѵ¹Əҟкů їƻǗŠϻŶӸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8eϖӨЪǾӆжҕθƒġ"\x8dƵϕҀʅ\\ǙӋ\x92ĨˇµԙοǗŏwͽ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7391061912804896861,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǤéҜϨț@ӎŀрԨī6ТʴǇǃŻʳ[ɺкŀʎǤϾǇϓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɩőZĩþɑӆǲk¾ͳȀȎҞȘƛϬɾǏʡºТрӇ\x8cȾ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƈѾБʝʆǛgœѢĶʾˍӖҖ#ԨĜӈĦȵˎīХ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201600.058536:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǑΞƑҏÝɥϖΑΧSˋɪͱӃʐԈǷžΉЍŞǵ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 716930.7153096461,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȧθʬ}ȠҞʮŗ\x83ùĂΧ˒ͲňF?˜Ҧƛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЩæČʛӥΫ҂ȉÇʽΤðчÜQ\u0380ǦΩϦȸʬĪʆаӀͻєȽǼ҄',
                            'message': 'ӎʃȶ\x84űƣԊBâҘʼȓĿƊƏʭѐϘӔřĐİȼаTɥҊȬωѬ',
                            'arguments': [
                                        {
                                                        'name': ';ÏϰȉѹŰҗԨĦǸȑ#ŧ˗ŴӁʨȟóӪɕ¥öO˘ăӷФʕÈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӫ҈ƦĄɸ,ƤũОϿНѵөÆƭ¿ɇЁȩȢЮ˩Ħǩɑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1448127323803598356,
                                                                        },
                                                    },
                                        {
                                                        'name': '°ƉȂģϠb',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӌϤҮ˖ћӽʹŗ\xa0˷ĵķǌ_ũҽԋӴԇԁ\x95өчæϿζŽˡƾ˸',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'їԃМRɭҟșHƽӲԪƿȾҒʴԞɵΗԄ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 725216.4975977954,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Â·Ɨ\x93)Ď2ğӲ\u0378ƏķŔͼȀӗК˰',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϡqѵƣ`ô%ºÀĂ;ǿЉƟ?ØƧҀūȰКқϡɚіԧАɘҨδ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ď˩ÎҩψΌѻk˜Ťˤ(µ.¤ê~ǔԞÃÌƅϧЩЈŏr',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7538007838236136386,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҙ˖ʑœʈѾҨ\u0378vʛҵɗ\x7f',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƣúb˒˂Ȍķʶԥ\x90ƇÊЉӢ;ηϮԁ҂ƫ\x89ҍӡȉûωԁναĿ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɀѽ҄ʐΑЏϳÐĈǟ˘ӓōζęίȜêƫɫԦɋ%74ԟˀȌč',
                                                        'value': {
                                                                            '^': 'float_list',
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
                'identifier': 'λЎ\x8fðΎ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ӓʫ',
                            'message': 'Ѷ',
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
                'identifier': 'ϥ҆˃ˮψҿЇʝи#ȮǏþǂΖͽϝģˇǫʸƆÀ+ʁ˜ӞƏ÷\x95',
                'categories': [
                    'internal',
                    'access-restriction',
                    'os',
                    'os',
                    'network',
                    'access-restriction',
                    'internal',
                    'os',
                    'configuration',
                    'file',
                ],
                'source': 'ѢʹʾöӄɲɧϡԏеӈоzxԘ]ŗƤϫҁԕǆȫӭɣԪӔɭʜŝ',
                'messages': [
                    {
                            'catalog': 'ȠѶӾȊ˺ƜШˠ\x9fӬ§κԬöˈҐң_şѦ˓ΔɉȪqЊ·ļµǂ',
                            'message': 'ÝǻӺŏʳǀčʁҟ΄\x8fΥˍѴЙұϘϐϜϻТҝϊŷεшŌѵЍ\x85',
                            'arguments': [
                                        {
                                                        'name': ';ǿΦȝÅǤĘǤӍBʫԄԓήҁ.\x8e҄й\x80ċ\x84ӅȒЬƞΰʟʇʩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӟѕншӵМǁρʧǺʉʗď\u0379ҭƥəȭʌӧφſȫʶДʗӉ˪ҋʆ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ċЋ\x86ӂǐÏjʕ\x88Ұ\x9eƫѹөƓʱʝÑкӜ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯƹùƸ҃ʑö\x8fɌЛѹξŒçИá',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѶąΤЅѽˍдЅѕϣʈŤѝȟϿʙÈΠ\x95(ʟҜÑÎǓˋҖˑŗʠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŰřϋȽăЀo\x91ӡ˩ʀĖƇɉɶԘҴĈˀČŝȺϑʄŮʯʺϒȍȷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦhń˰ȶ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5188280349930053859,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѧ\x83ėϗ"ΌưԖ{Ѯ¯Ɉ\x9cǝ`ƶĚhʫǹΎEŬŦΆȉǌŅ˙Ĥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɄGϜx˲˽ԏΡ˜ö¦ʉËƪɆǆЗɈʃңΟɐ°ѱюӞϼήe\x81',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 30265.434479281277,
                                                                        },
                                                    },
                                        {
                                                        'name': 'шͺѰ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201617.856248:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѪӡԃŝϏŇьҲſɏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '{ΖцϵԋͶ;ύłǢҖȧΩѵ˨ӧѳɳҦŚEʖЉрĹǒӿǲʈԣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'пҷ˓žűԆϗʘχЄȧˍάʨԛĎő\x85Ϟђӥώɜħ\u03a2ξȥʈƠJ',
                            'message': 'Ίϩˈʐє8óåŇŲϘѾŞɚ\x83ȕӜґɪĥǱАό˸űϣԌĉʩЯ',
                            'arguments': [
                                        {
                                                        'name': 'Ϥ˘ĠʘұμɠΌσȋǡӓ\x97ʷǼ\x82˒ёɑǵ\x98ƖӦԭҵsòͺŧØ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÌƗұϚωǇКēÿѺƣӖ˘ȚğɛǪҳʉôг(oȩɮѯɁӗʔə',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 912279.6835611927,
                                                                        },
                                                    },
                                        {
                                                        'name': 'хδPͶƙɎЈ\xa0Ҫȡɲɿҭэ@ӶЫҩƄȘϔ?ϡ7«ȊËƗήĄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӷōäİˬԍŐɻώÓĤ҃ҶŗϤňӁϢμǠȺԀÆ%ȭӓǘӜ\u0383Ԙ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯŴҫљƯӉʣŰҭȅ˘ТӁҩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'żưӣȇɿ?',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀЩƆԅƉʇҜ˧äm\x97čϼʙƜǠ2"ƹѣĢɁ˲ʘƌϢɤҫԤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳӒϷĴʑ|ӤϏʥé±ρˊӾˮǱƙ˗Ԇ°λ¨ЇêΕ\u0378ɸŵԦæ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201618.559399:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲӯΉʠЕǀćиӶӘȳɝĈ\x85ϞҼ\x86ɞįŔƇҏЖԩŸƸӆ¤ϪŠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'л\u0381TђŨ˒Äҽ÷3ȫǟЊȸ\u0378ƾȟӦϼϠү',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽÆ»E\x80Ś;ΧŸҭǾ\x97ȝŢǽӺΥǯóϮџ!ψ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'æӾөĘξǶʓɣº',
                            'message': 'ƔùbʉЪŢͿƮƜҸҜ˟ÒȔ£Ѡ]Ƃȩԩ|ŵáķɧΐϲĜΤĽ',
                            'arguments': [
                                        {
                                                        'name': 'ёӂ[ȐѣӾѦҸƟƒfů\x94ʣµΨŷԮÏ\x85ԑ˛Πȶ{ɫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6481006386335509843,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȰӱɟϞŪÂȌIȂɶzƂƍϳjƶђˀŔǳŇɌÂФÃƜÃ½Њ\x8d',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧϛѳĝV(_Úǩˢԝ϶ƈjƪǴе҇ӽǨ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201619.052311:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȌҶѣǗҺǔϬʱD˙њ˙πïŖϙ҂öŊҺԉԤҭΗӀ\x80ԑƩʄŋ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎҦΊӄЙ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӵҊɞÆOжYʞЈЃѰ0\x89ӜƸȾDϞzћů"ԨʳƕƌȕȸɲΦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201619.273456:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'πěҦǎ\x9aϳЇĔʲƮÃ˘ӇŨќȿ>Ԙ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϮʨВϰ\x82ɥҴ4ԜńѪĔȹЦǏĦԦǔS\x8eÞÏѸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201619.415990:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӳƝ½ǫϔ\x87ː\u0381ɗƝԭˀŭіwӾȏԜӻ°ȦҶӶ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЕȼϖřӷɣǤŜηϴӐǿʆϤþˀϹʃ˳һˀċđҴΔ˪é˩ǽұ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˕ʿϗźԕҎʣNȣэ˷\x85ҀњʉƮªʁиԝђʟƙȰʌ%ȉΗ˴т',
                            'message': 'ҋǃɡǜƧƳɀ*\u038b˔ıͼ˓ӗƙҊҊƣҵŘȨu\x88ґԛҹƹɅ\u0380Ϣ',
                            'arguments': [
                                        {
                                                        'name': 'Ęșþǝþ˲дїʋ\u038bĕԨˠûľɂǛƸȎǈ˞Ĕ`ʹÜjǥ×Î,',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġдǪçũͿñǙԕʔϗć\x87ѽӓȻЏWĺ·Ә˾Ҡυ҃',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6130520425764483593,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϽȽԃΡɒԓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'uНÌĊǌśˣgªå\x94Ţ9ŤŌè\x9eҮɊ/˃éʙɒϦŰǩǑʌ˔',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'bȤÃίͰѥȴɅ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԓѵԞΘΠӿǵǖʼӌЎYǬǳӥ*ĺȴuӼСӰ»Ŗ¡ƽεԘǅȽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'цҌʒЙςΎѴʒҙГ5Ǯ\x87ÏáʻǪ˽ƥ˃2ӥϏūĘˢƗАōƦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'eʜˬÏȞǊ\xa0ϟũ¨ҙͱɽǛũɁҢȴѳʸʥ\x87ӼȤͲƈ˻ʬãǬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'рæ¤ǪΊ\x9fęÑӉÙȃʏɟ£ȵ\u0382ҮИӒZПѼѦʫӢΆӑͺҥG',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˳ŜªǍ%ȷÌԛǧǈźГ˼őӨǎƄҐĤӾ;<¬ѝϣʤNҩҬ\u0381',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '͵ҊӛŨəŹџΖƋλӟ¿ƵΣФdƸ\x9f÷ƣȹȒёҦӶļԘȼņʖ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʸɰЄ\x93ɛ˨ñΞВƫÌҙ\u0378ҎԪćоϱǦ˯њ+Ľ©ɞǆԨсťț',
                            'message': '͵ńԄʹǦƊͰԮÇȑ\x96ɬϖπіˡƛϖќ\x85Ѷϐ@Ĉͻτ˳ϫ3ϼ',
                            'arguments': [
                                        {
                                                        'name': 'ǧѺǵͲϩνѺƜԮıL¡Ǖϧʧҭǉ¢',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Öɹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŗ\x8f\x92Ɍ˥¯κɬùƂ¸ɂϼȖƕ˼ƗȬӚɗѺɋ\xadȈž˔ž\x9fЧѾ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 161310.1893099589,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϘѕŃҷ˟ȶθˀϮÊǾҌYƒЯĽԦҭˣŰ\x92҄цӇ\x8eˊĴԇƊɗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˀїΑʝƯϜѥ©ʺȼ˙ˎǿɤĊώȭιŃ˰Ų%ÝŷñƜ˖ɖµů',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4701404621874552006,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΣɝʼɬqŻ©ɼ(ɞǭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹ˕˝ɣɄ϶ҟǔĲǀŖӊɂѽҒƷɮʲЫΉŴȢĞөˏ3ӜoƆщ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '#ŷɆɈԟ1ĄɰԔҎЏԁɢ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'IđľzϒϏʆ˦ԉҿԖƮԘ´ͽůϸȂɲʋΒѐӱĄКҎȿҘɎԟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3032571646141472403,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɠͱãҹ\x8fҜɔ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ζўϊԍéЯćҳӲўӕ҉Ϧʍщ˒ƻȠΌφŘɂÇԧɟĖÅɴŏ˟',
                            'message': "¨нVŒƝēϯŋ˅:ɔã¦ɡӁ.Ǒӡ\x86ӟ'·ùĮƚүԊ:ť˻",
                            'arguments': [
                                        {
                                                        'name': 'HһɶəПˉˬϥǶŉòЦǃ˫aɜԇñ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ûȐ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 331756.4533936859,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ōҪϜ%ѳЀƱɅϸБѱѐÕĉИqʙƩ0ЮsϬċϛ\x8aȿµǢ¿ĭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͻɶʫ¸н\x90ӆǃҋĸB˥*фөǥӍȞ¡ҡƀ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'вȿѷ˖КѽƊЂ˄Ĭɥё҇ʱʦ˂Iɉ6ưť±ϜüɆȶȓ·vǄ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹäĠƈ ԛФǰӈ˲λȞѾɒȐԖ˖uğӠ¡љƾǙŦ(ȵӊŠҷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɉ\x9eďɰѿҊȹӖοǴȴûӲȤŚʒӞɪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԦNÇǌШȼɸq\x96ȸӋƐ\x84ǫͶϒмԧǷřzʌфΟͶ˺\x9fδёʹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѱåü\\ȫȳǐҰ˷ĠΡӱQOGɛÃoǪůʱҐӔҖѾÕŨȂΚĲ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x85\x94ȯɷҼ˽ǤχEǖɁǧτҜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȫЬº}ѿXϭфñ9ΰǠƀѷȋҜȈӺ^ͻӆШЧ. ĖUχͿ~',
                            'message': "ʨӶI˂'ΧũʬȈƠԢǗˣңĚ;ԁ÷ǉ˱+юϤÅѳƱ;šɐƙ",
                            'arguments': [
                                        {
                                                        'name': 'ғȱǣɽ˱һÉȯӧ҂Å©ѶίΊӇϣǱԎԙ¢ѕʥȝǽɨʭľҪý',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 515611.2387902456,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ěʓ\xadʴxϋƯɾҿˆǞΚKc9gȴҖȠӫӎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦМҩνǉъϤÚ\xa0ЦōǯŞ΅ŲѲКǱȞԜуȕуүGѻƝĠûϥ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 120230.85562883425,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƘԅưÊǫ)ŌĪǮƜʭԮɸԚǺ×ŉȅϖ3NƏĘǆȷ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6922154445738665066,
                                                                        },
                                                    },
                                        {
                                                        'name': '˛ϣǸƍχēЁ]ԡ»ӥҫ·ŨġԖˤǅȼǋϮˀŕшѬǝҸҍʋ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˛ʩǪƆəÕϝLԄSȐǩѮɕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 230242.764998188,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʗӚʿɯҦϭΩȤӀŎÙȊϏČ˅ŁIҎǎĘǯŋGmȮXÃӝģ%',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 563252.5365176488,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɢӄĀȒҾǺu˙Ԩn',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 185155.56574777182,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x97',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201622.513031:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿʢ˦šɝѠǂ*Ʈ\x7fˉɣxĦһԊÓʉѷ+ѫÇȫŊԟϸͷϩҋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 352762.576706947,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɶп\u0382äŞѢȨǰɦÁҿâΩԒƙԖ҇ѭůԀ˒\x87ǃԓʻƉʴƢϷˢ',
                            'message': 'Őθ[ĪŋGˣɻӴԛȹțǂһԫ˷ʟ³ύˏƓԡϴӻªɂ˪ӭȈȺ',
                            'arguments': [
                                        {
                                                        'name': 'žЂīKc',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈԁƲLӞЛɞjʹӠϕҩϏćɧҐɗΞŮːŲѴϣĭӮӻЫ9JЛ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˶˰ɵԊƬņǄŨʜ±ЛɈɑĜȅǭAŌѼ§Ǐ½ΔΖ7Āʷюʅa',
                                                                        },
                                                    },
                                        {
                                                        'name': "şíіɄňϴ'õȴӀʋШʽ\u03a2žƜfVǓ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4011740736055351098,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȏ˕Ȗ˯',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3031205128175361561,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Š˯˼ʼ4ʄљфËԣɢôɩαҩ˒ǖȱ҉ξǸɧѦƈԅex§á',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʪҍŕЛҁŷҕˡǆΤє/ċ\x81ȞπˠђɈԑʈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x87IǋˬйѼʑˏɬƛĂ\x84˞ɀӋҁĶӦљХǈƵԧȖ|ϮϘџƮԌ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǢŚw1ƔɲϲŬǻɴ˔ƃξĽϰɀӜů;ĕҪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˢ˳ǪҭˣӅˤȴƓЫ»\x99§ĺǇϪӥљȁàѢÅ϶>ɨԃΉӞŴѱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'øÏΚϠѤơ¥\u0380˦',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӳҥ˛Өϻ3ĚʶʨѣʕʧǿȡԨίϐΈҬĀ˝ñ·ȃ\x8dԚӳЭԈģ',
                            'message': 'ȴĜ\x8dΉ\x9eɒԞ±ãɩӫѕԏɼДȭſĀ˶ўΕ΅ƞЧʧÇЏ˴џӽ',
                            'arguments': [
                                        {
                                                        'name': 'ϦӰĖLöʔğØƕʑ@ӂԭǺĲɻ(ЊǛȭƠˠ\x93ҺЂĤǛŜ˫ͷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 44208.388793407736,
                                                                        },
                                                    },
                                        {
                                                        'name': 'е˥Τǂ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'õǠҡĕÊӀ˫ЮʨӇǱӾӈʐұԣʃЄ҈˪ˆ]а˖ȝӏ\x98ʺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201623.604274:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͻѣ$ȞӁ΄ԛƥԮϱʉұɛ\x8fӅēǵ1ЮɹȌʛӰˮŜ\x83ǃȐцħ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ζХɗѶɼǺéѴwϴΥǨ͵$Ӫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĸӍǝњɼ^|ĪÍ˅҄SАĝ\u0380ЂˇƈʷΛқЦXqǛ#ÄĉėУ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӵϠÖύү\u0378ԦèȎŨɲəȧ¤2ƺŊĿʗŖ˱ЦлB',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6503811330220823610,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƦǅϏҝˉӚЪƬŢѥҖØƶɐũ³ƒƠђөʎ\x8dӬ\x82',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӪϰЌmŎʑ)ÉʬƄƃɘɥö˕ǾѯԄŴΜǾóȅԙέ÷RǏŝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ųӯ-ɮǆЫÚюүSʜśДĜϚԚǡȵƧʎ˯ȦşmĂӴ\x7f?ȅ.',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÆǊӘĲŴʷǆÔLіEūѷӨ˨VрėњŭĂ˔бϮˎЄŲǯ®ɲ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ñm®уƩőơ¡ӭϺĒˬЉИȍԆƯҽϸӑĖ˛œϏҲ҄ĲӬʴζ',
                            'message': 'ĴǕʞҎΙϡҷѮȒµ˪q¦ӗΧΘĥ`Ԗ˅ϼǞKǼӿ\x9aȥÎ`І',
                            'arguments': [
                                        {
                                                        'name': 'ęΕϻTŰΚćңѿƍêξű˱śàeԇǁ˩ԁʕ³.ġϢćŕӑѴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ôįƇəл*ιҚϢϜ\u038bŁȡĜōʌęШĭԫȼŦҀƍɶòȿԆNΊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'хɦͰлaʩΌß˾',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˀʛ\x7f',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɲϬȻ±ʽlˀƗƕΨĄʩĺтһȵ»\x91ҺǓϟǌ˗Ūʷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŅҒ&ļěĐǝϿ˓ʛϑɚҙлμ˫ȖͺɚáɸǽǺ?´',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 185040.35427853465,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĜăнǴP\u0380ӂюˬԦɓÙƴ`ͰрȌƲшƵѹȤįÎɠáȏԫǫЧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201624.544610:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'îɦӵΑ˘ˑ\x9bƓӑ|ɀǻҖÔϩрǭ ĭԋɖιНǩůѣȰʜ3ȵ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201624.611513:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9bҜǪʝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˌʬăаȌ´ϰʃűǳ¬@&ЇӨʃ΄ӟϡϦ6ҷŻДĴϿŶ\x8dÀơ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ö<ïҬӕΤαġĪƻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201624.745124:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĥԬϫťԞѤĹԨϦÈ\x8dmϸ˱Ʋě˳ɶăʃǸӃǺӼȄԉүƞу',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1724606727476122990,
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
                'identifier': '҃ΊŇ"i',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'Эʣ',
                            'message': 'ϟ',
                        },
                ],
            },

        },
    ),
]
