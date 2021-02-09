# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-09T15:28:54.344915+00:00

"""
Tests for the logging module.
Extension petronia.core.api.logging, Version 1.0.0
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
            '$': 'oϒǙʽτΌϠ˴мЇƂΦӋҳ͵Ԅ\u0382ǔӫo˘ӾмVԋͽхљơԄ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -6418036650990296010,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 692657.7922697616,
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
            '$': '20210209:152853.900171:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ͿӇǝĔїκҩș˒ĄԌѭƝΫϸҠşȉ%ģwα\x99Ɓϳͱ\u038bǄ˝Ԟ',
                'ʆýƾԀєАҦŞˌӲĘ\u0379ĺáċʆƥĺüëHāΓҺa΄ķϵԦͶ',
                'ʊ{ɸƿʹȽćAε҂ʴËθďʒĐƴŞʂC˖EµːѝɄư˰ɧк',
                'ƪʟńĪĐŭΕуĒўѐÒųƳϝѯɧӺ¦ѷʰ9ŐҶǇ\x8cʬѕʦƧ',
                'ʰ҄˛ĖǦ^¦Ć\x92ʨϨѿҕÏ/ȷʦӪ˶JǰJʯЏƅŇǹϳ_ȇ',
                'ϰǫȎС!ːϢ¹ѧ\xa0ɿň×ИмǷģÀԋǚʫȁǵыˉԧԩѾȊӧ',
                'гҠ\x88ɬЪɑǉӨ\x92ԤΗ\x97ϿӏĚʤ <Ӆȱ\x96έπžфҥŞ±İʆ',
                '˧ĂΟɋӻIɥϽɬԖ\u0382jȍŚĥƁҸųӱ¤Ɂυ\x9e õϰĕάԭϭ',
                'ԚЙŒ\x94lʙĘġEΛǽŔʬy\x82Ζӳ-ʅ҇΄ҷΌăӚаԉ˂Ɇ˪',
                'Ѿƒĕ\x82ƚ7ġʓHÂTœҷʛǑѓԐȳɥϕĶµďþέȗɛѭҪˏ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8805022363265859889,
                5991996715276547809,
                -4928591499593192722,
                -8877661037660401308,
                7549612548841822957,
                1320111512715472500,
                -8437426156165035904,
                6955081249340379968,
                3487078446423784904,
                8157929765083593451,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                417625.89010913373,
                904084.7396015334,
                92181.17046985854,
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
                True,
                True,
                True,
                False,
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
                '20210209:152853.901096:+0000',
                '20210209:152853.901111:+0000',
                '20210209:152853.901120:+0000',
                '20210209:152853.901128:+0000',
                '20210209:152853.901135:+0000',
                '20210209:152853.901141:+0000',
                '20210209:152853.901148:+0000',
                '20210209:152853.901155:+0000',
                '20210209:152853.901162:+0000',
                '20210209:152853.901168:+0000',
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
            'name': 'ȚĨԙÚє¢ʐ΄ʇʳП҄HӲЌûӡсʚĚѷʝԥ*ϡʦςȑŉˋ',
            'value': {
                '^': 'bool',
                '$': True,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ĕ',

            'value': {
                '^': 'float_list',
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
            'catalog': 'ԭŉōЇЈ·ɋƛκƦѿƎӥ\x9dԢP\u0378ˢùΪɀζĜúѡԘɜŽЇȿ',
            'message': 'γɦǶϻǅƂƳϭļҠǅ͵ρĿ\u0380ĪĿθǏÊƲˤĄǻûġаʒªх',
            'arguments': [
                {
                    'name': 'ˏҖõȤбҁԡУţʾҨˆǘ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210209:152853.893227:+0000',
                        },
                },
                {
                    'name': 'ԡӲĔā¼ԇīӿǝ҄ŲʎҨӌÔӛĠŏЎфŚƧ˃ˀoǪǓΑ;ʠ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ǋɈЃƋ\x87ļˆȔǪ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        916185.6924379709,
                                        571412.8812933719,
                                        619000.3709527951,
                                        863906.554079587,
                                        3406.8569544720813,
                                        123442.80892122228,
                                        435027.95689751813,
                                        -45244.38881721449,
                                        631169.8538935557,
                                        966842.2445626843,
                                    ],
                        },
                },
                {
                    'name': 'ȝȕПĞ\x85Dļȹ1ƻɜȺ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -9164201964771503931,
                                        659995038010016961,
                                        5734647845400097225,
                                        6299341625430513528,
                                        25829573306292345,
                                        7356131811627267356,
                                        7598563617334984451,
                                        418529833020466619,
                                        -1457765249425946638,
                                        -6996153362319682274,
                                    ],
                        },
                },
                {
                    'name': 'ϻJƺԕŀʬԕȏιӶ˅ІͲɅʅЁǧĥȹХʊßŉв½ө³ҧʝJ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210209:152853.895276:+0000',
                                        '20210209:152853.895314:+0000',
                                        '20210209:152853.895330:+0000',
                                        '20210209:152853.895345:+0000',
                                        '20210209:152853.895358:+0000',
                                        '20210209:152853.895371:+0000',
                                        '20210209:152853.895384:+0000',
                                        '20210209:152853.895397:+0000',
                                        '20210209:152853.895411:+0000',
                                        '20210209:152853.895424:+0000',
                                    ],
                        },
                },
                {
                    'name': '\x91Ȭɻџǯҿǡ-Q˹ъ˟Њӝ˫ēЯϘŸ˰ǓԟѬìɴǣЅаХĘ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210209:152853.896217:+0000',
                        },
                },
                {
                    'name': 'ЪRYȯĖ˜D×ƴѽρˣӣͶʾԮǚͰ˩Ȭɲʛϸ:ӷҼϮƉ]ò',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        530201.537142037,
                                        -71863.07052898982,
                                        -54296.451026963376,
                                        683692.6461620321,
                                        535036.0216832953,
                                        638049.0304049767,
                                        328990.6106384669,
                                        359715.32089543017,
                                        132959.9993324679,
                                        538986.4712450324,
                                    ],
                        },
                },
                {
                    'name': 'ήèĴӲĿҞϥҵČŒʠЮǓƽ¯ŮΪԀơEȨƛҋ',
                    'value': {
                            '^': 'float',
                            '$': 455644.8772753036,
                        },
                },
                {
                    'name': 'Ņ\x9cɚbʔҀ˃[Ǩѱ/\x88UҕÙ҆Ğ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210209:152853.897558:+0000',
                                        '20210209:152853.897587:+0000',
                                        '20210209:152853.897605:+0000',
                                        '20210209:152853.897622:+0000',
                                        '20210209:152853.897639:+0000',
                                        '20210209:152853.897656:+0000',
                                        '20210209:152853.897673:+0000',
                                        '20210209:152853.897690:+0000',
                                        '20210209:152853.897706:+0000',
                                        '20210209:152853.897723:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ͼģФ\x8cѣĜʈǳ¶ԣÁΡѡχϫʔǶҡȳƪȫϮ\u0379¦ˀαԔƐ Î',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ǜ˸ǥΰÜρǣˬσѯ/ÙŅƷͷưîҷρҮ҆НӶűɍҜ\x85ɗŃǱ',
                                        'ЩӚȑŎӖԊΙÐӢɕTÓͱӋƇʤːԠлɒԂ˖Şίˇ˪ȈЃǲ¢',
                                        'º\x9fԅīŋƶɢϴ\x82ŴӑUϔŝ+ҫԑƫEçÂ¸|S{ɻ\x80ė,ʓ',
                                        'ѳ´ǀ¿ŲáϬϖȍѫ˾ѫŰƄöƠī˙ґЙҚ¸ɯBʳ;ȗȨā\x92',
                                        'ˡσԛȎȭӜüԌҒűƩʫԎɎпǖҬđԮȏӓɓơāƽҹϓǺuԗ',
                                        'ҴʊŒ\u0378ÙɖԜ˩TɓӇȗ,ʜìѲӱǿǔƾԨ¨iфϡ¼ƳɹЇϓ',
                                        'ȆҭȘƌɺԔōʨ¥ĵ҆УɽǛåȧƲΤϳПɲǫЖϝĂʆ°ΐ˪Ұ',
                                        'ʦђҥ²˝ƨѽӕѤöѹбʃȃǥ.}ŒϏӍБθʹЭ\u038bͱƪжɒХ',
                                        'ˈХõɍŅѕć©έƽĘкìѪϿmgʎԒŝҨћҎǐɬöзϥӬԐ',
                                        'RԠ8ɋåǐ]×ɋ%Śшϊǫ\x89ҳΛȉɜ\x98ïјϗ\x9fþѭчǩʝο',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ʋʂ',

            'message': 'Í',

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
            'scope': 'warning',
            'messages': [
                {
                    'catalog': 'ʪ˷ȡԨǗтȞˌ\x83´éɞѳҙԄĿʪPԮƚë\u0382ԃǸŨɵɱǑʅĿ',
                    'message': 'ÞЂʁàάΕêɠțſ͵\x87ԎΕɉȑŐϪȮӫŘĀѲОԈĴ/ҴФʓ',
                    'arguments': [
                            {
                                        'name': '\x95ř҇ВYӫҖɺŗ¾ЖȓҖҋ˴\u03a2ΘƻҢͼ˕ƯǷƚԩǙƇԠԒľ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8853550365811908895,
                                                    },
                                    },
                            {
                                        'name': '}ȿ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'θӖӇā˲ǐʜ˰ƆΪǃʟµϢьǼǼŸҚфǱ¨ԩфͲҪȶГƼɊ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȃԉ҃Ĝǲӹϵż˻BҘʕЖǉĠ©ԪI˧ӱΊȷɥ\x95ǍΣ˞ʍ¼Ǳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6347261840486112715,
                                                    },
                                    },
                            {
                                        'name': '56ʕШą`%ȠԑǛянōʌЁș\x9dγŘ˧ǀʕψϿǧҫǆrЙ¥',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.857069:+0000',
                                                                            '20210209:152853.857115:+0000',
                                                                            '20210209:152853.857124:+0000',
                                                                            '20210209:152853.857131:+0000',
                                                                            '20210209:152853.857137:+0000',
                                                                            '20210209:152853.857143:+0000',
                                                                            '20210209:152853.857149:+0000',
                                                                            '20210209:152853.857154:+0000',
                                                                            '20210209:152853.857160:+0000',
                                                                            '20210209:152853.857166:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ϡԄʡŖ'«ñ˓їԪϢӱƌσ˛˾ö˂ѓЍΰŹƝʈ7ɼЎƝԙπ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.857418:+0000',
                                                                            '20210209:152853.857431:+0000',
                                                                            '20210209:152853.857438:+0000',
                                                                            '20210209:152853.857444:+0000',
                                                                            '20210209:152853.857450:+0000',
                                                                            '20210209:152853.857456:+0000',
                                                                            '20210209:152853.857462:+0000',
                                                                            '20210209:152853.857468:+0000',
                                                                            '20210209:152853.857474:+0000',
                                                                            '20210209:152853.857480:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ό|7iԌøҽ<ѝ[ǵʤ˄ԋԆ¤Ԁ˕=ԖNöȂѪϖȜɄ\x80Ņʙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ьƱʠŌ8Ī\x88ϘCĎʞҮПˮԡ°ҢɊ\x89ŢʡĚ˲Ų\x8cc',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.857924:+0000',
                                                                            '20210209:152853.857948:+0000',
                                                                            '20210209:152853.857956:+0000',
                                                                            '20210209:152853.857963:+0000',
                                                                            '20210209:152853.857969:+0000',
                                                                            '20210209:152853.857975:+0000',
                                                                            '20210209:152853.857981:+0000',
                                                                            '20210209:152853.857987:+0000',
                                                                            '20210209:152853.857993:+0000',
                                                                            '20210209:152853.857999:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "É'\x8fԓӂ+ȉƗƬЕőZȦÚň҉ǮϼƶϗTԊ˲",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϒ¼ѽ©çc|ǖѫŧDϤĿԐүȝѝˡІЭӰ˫Ԅ¥ѧ£ǲƻ¬¡',
                                                    },
                                    },
                            {
                                        'name': 'ϟҎƫǓíзƠΊϬʀKϿ\u0383ԬľшrĽАʗuɕҟǉγΩѫȈϚӸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            34053.07026489638,
                                                                            903636.2507697142,
                                                                            798536.7450762035,
                                                                            231464.58427672443,
                                                                            -32892.41266189827,
                                                                            699857.0330632743,
                                                                            893178.85340781,
                                                                            746313.0782257529,
                                                                            427765.38928486314,
                                                                            802531.8528111879,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ç)ʸċȟѫòȧΕϲԬŲʟɛęƖŝ÷ƴ˳ʛνďƲf˽ȒǸБГ',
                    'message': 'ԙ\u0380Ȇ_¶Ԛ˞ɶӗƻϜ+дEµӝӄѐӇπЁǷÞбϞҺw˂ɌŁ',
                    'arguments': [
                            {
                                        'name': "5ɇČȣŊϛȔϝɝ˒ǙËĺȳζǿAɂ\x8cќ'",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɏͱ˝Gs\u0382ĞūΨˍɜԊȦǂȡʌ&ˠŶƈџ\x8aĢoŤǥƇӢǺí',
                                                    },
                                    },
                            {
                                        'name': 'ǟƮӋǨԬϬȅΑɑDŌxΌҏӞ,ǵхƺӀ6ȥҐʡāƲќ©Ȇӷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˞ɩEùąçĜƩ˃ņ±ɕɟÍƏäΎҹюĈѫlǰҪ&ψĨMΈǑ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            688757.0611523071,
                                                                            309943.13310657657,
                                                                            360564.270922602,
                                                                            604111.6002849237,
                                                                            -48124.65758997339,
                                                                            -392.8423065977986,
                                                                            860825.2228579829,
                                                                            785859.7596524527,
                                                                            428538.17403044703,
                                                                            474665.5785876146,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԛČӾƓ˰ǻĕƱŖɸTŻƒώŴҸӞȚΆәʡƈ\u0383ʻӢŭäƎȌӠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1764329360771850855,
                                                    },
                                    },
                            {
                                        'name': 'ȏӭCdơǲK˕ѳ\x800ʝѠwīúʻʵБϘҌϝ˫ӀϧѓϩåϪΎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 374775.9397418187,
                                                    },
                                    },
                            {
                                        'name': 'Ⱥ\u03a2πԕʛ˾ƿϥӞыǷǵѸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            202348.50086579926,
                                                                            744217.5498008003,
                                                                            162915.67632362928,
                                                                            949950.7681479123,
                                                                            377820.0692331644,
                                                                            651910.5916925815,
                                                                            791683.8027327397,
                                                                            583241.4160330932,
                                                                            210033.8364720883,
                                                                            415524.49125934375,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ēόɑГċŤҹʗӫŉāԩϥѪʀÃĽԞΜ͵ȩЄ¼ѰǢ˴Ęԉȧȕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǯѱƑѬʜĔԎƠʱĨ\x8eș«͵ȃpǣuøΡΆƵ^ИӻқҋōŘɺ',
                                                    },
                                    },
                            {
                                        'name': 'ҪѢе±Ⱥæ[ѓƸ˾ҡ¶ɐŲӈřűâŝϖȗӠÐ%ʱξĆԁԊŚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϧѝςӔхɊɚ˄ʉӵΙȪιѿŶ[ӐҸɝЁщʚŦXѰЖӪʴϿɯ',
                                                    },
                                    },
                            {
                                        'name': 'ƈʁѕӥӤ£ǐӣƏϕ΅\x84ǜǏƉǙ:ɴѳǇЦĉȘƨƿӾÒƨ˚ŋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6573509969793948047,
                                                                            -1104523294197281541,
                                                                            2056459215369202543,
                                                                            -46181180407920071,
                                                                            9160269133949945729,
                                                                            1716711874039132800,
                                                                            7115627503213874885,
                                                                            2764202445980596664,
                                                                            1394976830744468499,
                                                                            -3275479849394978356,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӰӐìɗɩuФ˨fЋƚÿ˶',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            300747.1997506613,
                                                                            161495.2272738384,
                                                                            122985.49766631555,
                                                                            158405.3442627296,
                                                                            254784.1247695018,
                                                                            110833.20580512867,
                                                                            877680.7252283131,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˇɀͻϪ\x9cɵԙԨe×˵ĈČĳĻӃzԫʈƘr҅ҜŁӻ5˞Ԇ\x8dϨ',
                    'message': 'ʚ¾\xad˾рÿξƵЯʂ΄ΰҘτķЧӼȰʭƵńԗɬɉǆԋȬИˡȚ',
                    'arguments': [
                            {
                                        'name': 'ʙȘˁÔǰIÂģǑԩȥ×˪ƌɪAˎκ˕ơҖ,ӚœЎβ˟oϵˋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.861696:+0000',
                                                    },
                                    },
                            {
                                        'name': 'sоʌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϬGĳʗwȏPӋŲ8ƦƀØ\x88ҺϹOБƨɺЗʎɟєД\x9dǾЬԥǊ',
                                                                            '÷ЏҀȟμɻӧ$ӑͱѕпҦ+Ȕӑѱ\x9aԢÒƨ!¡ҵ,Ψó-ʁԧ',
                                                                            'ʒŜԎˌ{ÍȰϳªpӗāŔѽȝТǋbƤʱҾґ[ɛŧӣǥȊЇƗ',
                                                                            '҉ǑſғśǢηϰêΔƈɕԟԫʄƎϞ\x80yѩӌЁƣ˶ѤʤȳɴvԄ',
                                                                            '5ӐˀǔƔМRˆɜʍɂҐͲιʉƐŎKέ˴Ƴώ҇ǌѕҏÝч˪Ϻ',
                                                                            'ɦϙĂʬϡŭ\x877ȠÎPʑшΥˊrЛĊѨӰʘ˨y\x88өȧ Ɓɫǰ',
                                                                            'pν{',
                                                                            'ЄÏǻѦÖυ˕ԩԅĩʑ˒ԭԎɴȼϙīřʞϫХ˲9ɳÛƸĊ]\x90',
                                                                            'Өżčˣ˩Ƅͽ\x8aм\x9eЁʙӵŲjƅǟԝˇӻĔŐƶņˉ\u0378\x92ԃсˢ',
                                                                            'ʏӲȹʻϦώC£ǲǺϗаȠҌŸ#ːҭˌҁϽåʇɶԄȳÜĊÅǹ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԕRǒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.862340:+0000',
                                                    },
                                    },
                            {
                                        'name': 'η˦Áѕƾd÷ɓӑҖϣҳϚżɢѮұȑϔԊɰҪɝдΥѶģʺ˷#',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.862509:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.862656:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȃȒĢЛԍЭүģǖYԢԕϪφʻщӉ÷ĽӫxœӘ΄ѯ^έȗӗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 202631.16120163468,
                                                    },
                                    },
                            {
                                        'name': 'вźȴ¢¨ʓи@ƨ8ɍţ6ūԥǩʐè\x9eѩɅ?ǙѱŨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5209983530962184232,
                                                                            -8659183643646825121,
                                                                            -5382307376076676074,
                                                                            7555422892203069751,
                                                                            1086760029941773516,
                                                                            25172950157143377,
                                                                            -2341519825778461301,
                                                                            -7159978471992731932,
                                                                            -8545481261100483004,
                                                                            6532779638840521982,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȳǻʠ˵҆ʇɆUɛŊßɼIЅ˄ƺȺ»έλԏÞwӮŭȩѝМєʼ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'pї\x80ʬΣӰӐɁɞϲˬPťѹłѓƶҀʙΜύʪӎƎīθÖ˘ȤȈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 514662.8890093904,
                                                    },
                                    },
                            {
                                        'name': '¤ЁʧҊΗŔ¨Ӌԕǭ\x88ƚʐԩňψΕўƶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǩвҐŻϴɝïȝʔŁ˞ſÐȊŚҤ',
                    'message': 'ѿӗ϶ϟͽϑϧ¡ȱԃ¼Ĭ½ǢǨƅϳʏ`ǳ\x90ɏӠԄ\x97ȈȊ&źǞ',
                    'arguments': [
                            {
                                        'name': 'ʿŉъɼÎƫĤԃÇ~',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            529179.240657576,
                                                                            320861.302700653,
                                                                            200814.75719704654,
                                                                            980184.1069860354,
                                                                            827507.8884787648,
                                                                            176552.58620960877,
                                                                            987096.8699138202,
                                                                            483130.7280163325,
                                                                            295931.44876559323,
                                                                            511647.64533929934,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѽ˪',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǎ˪ĺΘώǇԜ˛Ƞâ=/Ǉȱʰ\x84ϵɛɳ%ƈǸσèҌʝȧ\x7fʱ˅',
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
                                        'name': 'GŰőÈɝӞ³ŠĊѵǗХҗŠӌ\u0382˸\x8fҍњ҅ď',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӊ\x96чѳƄˎѰŷʀҳƫьĨ2Ɲς?ļCɇ\x83ÞƛÃƒўĝȭÂΚ',
                                                    },
                                    },
                            {
                                        'name': 'ɫɐδʢҼɟȑˀЎԆԬЈʱŠĂБ¦ɹϛΨȹ¯ƲнѤƉͰȻʓģ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӲʶΨȘˈˈÿӥǷҽŎӰŁ҂œӠėǐҀϤΈɑɬǮѷʎ˗p~Ӂ',
                                                    },
                                    },
                            {
                                        'name': 'εƉʛӫ\x8eѐĸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2091607018083484561,
                                                    },
                                    },
                            {
                                        'name': 'үόĬɟΟŋ˘ӨǋƁˤȃ˥˶Ԭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6817288415214710202,
                                                    },
                                    },
                            {
                                        'name': 'ӲќǵќҵŭЉ˻фˉӱƀǚѕʰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.866690:+0000',
                                                    },
                                    },
                            {
                                        'name': 'щ˷ȻŤÑõΎӁԪöʈßȿӵҬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2962089437446373500,
                                                                            8061316989500935960,
                                                                            -5913043805865783710,
                                                                            4536476813797449447,
                                                                            4546676214288218778,
                                                                            -136043966675422261,
                                                                            -6483626495136882317,
                                                                            7942921882490334868,
                                                                            -6325790461791853530,
                                                                            -674519751593760360,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹκ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ũ\x9f`ʻóʡн{вԪíԚŨxϟɮ҉ņԩȵԎǕîŏù|wĽƠf',
                                                                            '҅ƲҎªŜʕƂσ\\ә%ýҒĶSӝŌɕ¡ûʟЁŜĿʋǮǔȬrȿ',
                                                                            '¦ąūҫşąŮѯÁʂÇϷҷǖҋƑɿьǞЊͳΊ\u0383ƻǓđҎƞǨѽ',
                                                                            'ȴƎɍ¨ĂˊΊϟҖÊИѶŦWχÈ½ǅӤɰżÎԈʬ҅UˍǠ+Ƥ',
                                                                            'чˈӿȤɨˊϠţǭˬ͵\xa0ŋҢϺӥxłòĢʏӀǄ\u0378ŹҿķĬŀɭ',
                                                                            'νϭWаɺő˔ӧɝƪĚ\u0381¹ÆƲɞƁкэϏҥȽȬǐˤƥ»Þʹğ',
                                                                            'ɎАȤіȶЍȍș\x8eϡÖΎүãǲ˶˷ËɄčѹҡλTÙ˷Ȃ˱н϶',
                                                                            "ǻÎ'¢ŶɔǸŋҭҒǒǓʭӋϟϪӌ\x8fЈǽ\x9eЉЅҚʩˢɔġxŌ",
                                                                            'ɜĖчë¼˪ǌЪ(ŕǙʤИҎǮԚȬɮƃĦňтɜͿӚƅѭщҸ˱',
                                                                            'ɒãҩьӏãǹËɠȃӚÅūé"MϞʈţ϶Ůŀϴń#ԕâΟӣ3',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҙ´ƘӔȭĨƯ(\u0382òҵ˕\x90ҁ\x9aϜҩÙѣҸπҲԮoʻQϡǥӻɠ',
                    'message': 'ƠӑёѽӸϕξЮãˀʳÕȗɒŽͼШ½ʐӈϦɃӜ²ƩȜԉѷƻɈ',
                    'arguments': [
                            {
                                        'name': 'ZԮ˭ԩɿφȓЇζʴŊňûĤЍɾ˹ĿȚİ˴ˊĸΪ6ԄȿƵϫԘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ċϐ˶ϑӾŗʰψͶӸȞҤΞԫ§\u038b;ϸσÖϘφΨdȌѭķ÷Ѣ#',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7928137223501211238,
                                                    },
                                    },
                            {
                                        'name': 'ÆĈċɃˡɫãԞйƚ¤¼õ¡ԨźӉmÇͽǉӯҋŗάӡξѩÌm',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            531683.5999422392,
                                                                            147574.22448675917,
                                                                            342699.86445122474,
                                                                            511090.1349036691,
                                                                            -93393.64261731037,
                                                                            -1473.3242072773282,
                                                                            305580.94657885813,
                                                                            494717.1266081829,
                                                                            179502.80309462437,
                                                                            573178.5888932786,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʱȇ\x94˒ӫԥľϕ¨ǟҭ\x8bйЦϺʭńǁʰȸӶ¯Ȧ\x8bÇʙωʋˡɼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǽԄоϧӷɳӼȾαԒĥɌ¡зɑLĿӾ˽ңǞΛɮȅϿхΕӬˮń',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԨнϒĩɝƔ[ˢĮĞѵϟ;ɝƵŪўÙǩЋюˑКөɀȈįЯä\u0380',
                                                    },
                                    },
                            {
                                        'name': 'ȯSȋZȝяƛҞӨņѧ°ѰǧɊ6ƼǗǷĬųVѼɵɓŹé˧]ˈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            283999.65660688124,
                                                                            843794.7450154609,
                                                                            12955.97278760394,
                                                                            467777.563534357,
                                                                            406082.93213638803,
                                                                            -78877.5094257847,
                                                                            -19735.092698239838,
                                                                            426964.58349210676,
                                                                            270419.9641362504,
                                                                            264575.09494491015,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9dϐϳΨǎ\x87˳ȕ҅ŎŁmň˓ОоƲˤуȼØ¿\x8dwҝȶʓϤʲϩ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϵƱԁίєw',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӖҴ\x91ԂʟӅÇϙǌ\u038bҭѴѠϢР\x9bǊ&őҚʜJƓʈɾȼöƘӿӹ',
                                                    },
                                    },
                            {
                                        'name': 'ψǲξ¤yԅÌӝēЅΊԈɓʷÛĐӕԛҨПϡ{ԊǑҊǖЭȒӾƂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӫ)ɞҵ\u0380{ȂԃĩȯΝѨȽȷΡǙĎҳювʬɇēΊĂўϟԗі˩',
                                                                            'Ԧ˟ƊƪƈªǊ˙ҁԅӹЛëġƌԤĠǋʾԧҶä\x82ҌҀȕӪǍҵƟ',
                                                                            'ԃɰɎҚƉȨҘăԧ,Θ˘ԥšĴӎʧΡ7\u0378ԕ\x89ˑҤǔʟȊѤБɕ',
                                                                            'ˑɊHϩÃ+EƲ¯ÀӝƐѧɽН\x9dɷ˸ƽɽȏ\u0380ȣԩ˅фĪÕʢǪ',
                                                                            'nИϒЍŻšјƑê˚hˍ˻ρɯνŠˣԉȉ˷ΕʒΌʄӰѥŋƝǙ',
                                                                            'ʦɚΓƳ˴ĥʧ˦όƤœȈĖ˟ԞZʡƉӠӑyҹфȗ\x8cӠƒEӬȐ',
                                                                            'CĲʜʄҕӐ˾ѷƟƐ˸ɓ\u0378ͺӯȁŌúȳȡ\x99ǽ9ҏƴʲЋΈƾÑ',
                                                                            ']lҶ«ȖеƱҁŭǧћԣяǷÝzúɴӦѱżˍĺКήÅˀӓēξ',
                                                                            'ʙšѸѲHҗŸå\x99ɴ.д»ȶәůȗ˅ǂĈ1ȏѪȧβÀ¼и˰ǔ',
                                                                            'īǙӿβ˜ѐȟ©дǩƨÝ?íϹҕȺӅнÂΒfΐцɝȟˣКӱɂ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҹɒNŀʑęĿӆԂ\x89',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3995509872889780262,
                                                                            33288735929141954,
                                                                            55071268894628729,
                                                                            -1315702396541233358,
                                                                            -8029036782611357248,
                                                                            8441491781206392599,
                                                                            -8889693019945542227,
                                                                            -7270289037335720082,
                                                                            -4322321958002972256,
                                                                            8194152321174532049,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\u0378őАͻ\x94ðφǤҰŴƎӘȚшɡέӗЮѿưЪ*ʬɬƴяǵԛ\u0379;',
                    'message': 'ʆȫ+ɇъӀԗνʙőΘƽŪě˰˩ąɬ\u0378Ř\x97ҞŖǁΓ1ĎЂϮӉ',
                    'arguments': [
                            {
                                        'name': 'ʔѢҬјƛøЯʊЀȿθȻӅđԗİĜļŕȦĺΆӤÂʯлīЭ˸Ԍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5587542965297804503,
                                                                            -1467345531413550320,
                                                                            5812291485312752733,
                                                                            615454447438348277,
                                                                            -7191363856502838820,
                                                                            -3690221201616489146,
                                                                            -518250856971843247,
                                                                            6877067904897283187,
                                                                            4136761968536622086,
                                                                            1008151584673932127,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɡ3ɜɲŵΘϼīȺȇϞįʝɥ½ΰÿҰʰвĸʖ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'χùϠɈÓѽǄUőҒϒȰЌźǿӳԜ\x92$ĽƽьȞ¨ΠǶͲĔĝɲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĔҏŜɁDʵʵΥŁϞ<Ȱ«ӤȰ΄ҲŉƘĔƍӟѬɣ˂Őè$\x98Ӱ',
                                                                            'XĲҜƹѸdҏʦԨѴѿΥɡσӨͿÇǰˑȉϤɴƤιҔЄ2˲ĄЃ',
                                                                            '˻˓\\ƧӥƤӅɑ\u0381҃ΎҦ\x80Ωϻʷҽ(ĸēЀ˅ˋň%ϡ\\ȨUО',
                                                                            'ǢʾĺʪԃOҤȌͳԃ>ǉ˘\x98ѾШLԮӝŁîƓЀφ¡\x93ƒӓŹЩ',
                                                                            "ǰ9ύΌΠƤɶӴ'уґѝȟɥǿÈ±ƤҮҥ\u0380lĶɧNSӛОŹe",
                                                                            'үɼƮǀɸҐ\x9fċɇϭˮȒďӦЙыάţʟ°ċǣÅǸ¬ęɯǿКŜ',
                                                                            'DҒˌŕӾ\x80¸ПiȬȓҳięϏ×˜ѴɴɌ˕ӀĔҽǎҦϺœŇɮ',
                                                                            'ѣӆȨ˛ɜӭċˎЂʛˑéϡóпʂưíԨɉҍѿ¿δѱƗ+ƫďХ',
                                                                            'ѿϮҿ[Ǘˋԋ#>ʄԑȧƏˇϠĦĻӝϱåƿ«ʡҟɛ8\u0380Τ~҄',
                                                                            'ˎǳѴıΩǪΡKÌʭ¶њжӏŐʓӨƵoԣ8ɦҨɚηҰ˵ʧ0Ş',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȢÚĀгoɐԝʢҴȬϱԤRԇςƸвȭʦʛϢњǭxɀ\x83Έτȉã',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'k ϼǑӻǾφϹāԄˆǘϚÕ¤ɡǈʯȆȠ˓ɵʞїèϼҧ\u0379ϼM',
                                                    },
                                    },
                            {
                                        'name': 'ϫ×ǵйľ҈Ȓϼʿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ºƆ҂ЅΨˁüʬĮϏȡҧ;ɬ8řсŪąȧвӽ×ȦʺЕϏ\u0379\x94Ŭ',
                                                                            'Єə\x90ҡӄ:Ӫ·ʀǲ\u0378\x82ÏȇJ\x9dοſĶğп\x8fϾ˙ҖҬж˥Ğϻ',
                                                                            'ʂɎˏԐʔWʫȕʪӐҙўϤɸKŧΰКҬľ˖ǞÝŌ=Ҷ«ȕһǽ',
                                                                            'żȼϮɆȇw¿ЊǸȹҡɶɠΟ\u0381˶ѺǍĚͷɷΉЂŨƎʳ҆ǸӃό',
                                                                            'ŤĆΠŹǷ˨ќхʕń˫ȅҹ\u0380¨ȣǶԑϏƦȿUɶTrĤϛԪ\x83Ƃ',
                                                                            'ϙ³ƁəŸ¥U´ɿȁѓÅ\u0378UЦɱѶɧǱɟ\x96Ćʣa¾άŎƧɄŰ',
                                                                            'ɭӭʥлѦƋʻȽʥsȍôїĊӂϒγ,U\x95ͰŘҩВːȱ˩иԂ˂',
                                                                            'ћˌƶɵĵÒϺqҠƐ˅\\ӭʺËэåӼ͵ρӞӟӽȚЦѠӢƍÏʤ',
                                                                            'ҸʳΉǈťφюĴˮɥ΅˾Ǥ\x8eɏãn\x87ʹƎČГψҨĨrҖ\x9aөϸ',
                                                                            "ОЌɲҽЕǅԀʈєƙͻʆJԠ\x92ʪӜ˾тƠÞɾö˔Š'ŸƢζȿ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŵЩшgǆ˸ɳϬϥʙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038b°ΔϦˇąʼԮÝҐҕµÊѬͶǓ˨вϨǽѧƪζ\x9eƻɱеԏζа',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŎƘǏĸ\x9eǂȂә˂ϩʨ˙Ì½łəğЈҦ5ʅѿԫEѿӌɻśɆɳ',
                                                    },
                                    },
                            {
                                        'name': 'ϪӰ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ū\x9cŇ˴',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1225034941392513293,
                                                    },
                                    },
                            {
                                        'name': 'ӌĉΒć\u038bˌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϒvȐ\x9fȸҒĩʞƮыҢǴƋƸǌFƁӍԚȓ·ʸƯ\x9bñίԒʵӄǴ',
                                                                            'ƹȍɦҒѨξϬĻώ˥ԅąȥТԆһІťƝzӴҶѱɾƱԙɔkŃԋ',
                                                                            'ƖРʏȮҭʌşȌЏҀ˦ѪΣQǢ;ϚɶȦ϶ǃф˗ǜ҄ГŃӐíĔ',
                                                                            '\x96ǷΟĀǣҘoЄJӦцƫƂĝǦ˕фҰȃΗ\x91Ԩжͺ˳ũ·ЊҊѤ',
                                                                            'ӆԣƸÌţЌ\x84ҡʜ҅ӿӱƔτÖϲлʱӘòëйˢҩêӱˮ΅\u0382k',
                                                                            'Ӱȴω҈ƣBɞÕ˪÷ƲҥҦϖƏʸ˃ĒϳԁĉɱŌѫqɼ˵ҀΣ˗',
                                                                            'ңĐȬˍǋʣ\u038dȲğòǰŅʱk\x97҈ˍѪʲ҃ӲғҔêØґϲԨΊΝ',
                                                                            'èӴΩĶ˸\x85Ʃȓ.ćˈ˥ƠϬƒɽåǶĝ\u038d\x97ψϢʦȃʅЪҍҧ;',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƓͳȜűƆŉϟΠҗ\x9cO˲`ёǼʂŢȏ5Τ^ѹŉȞΫҨX˚ҖǢ',
                    'message': 'ǢӔʖʏЛȍΊĸǯÐыҝӧÎħŘ\\ǅЩКŢ˚ǎɫԫŰӚњŭĊ',
                    'arguments': [
                            {
                                        'name': 'Œ¡Ω\x9f\x9cɧʝ҆˯ЏѰ`;ϸĲѝІ˟ˠйҙ ͷ\u038bȲȦƯÒ˺ˌ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĉʗѨ¥ɤιƚƅĖŚ\x87ŰsíӣRȗқTɏџ҈ҽĜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4002679266735756696,
                                                    },
                                    },
                            {
                                        'name': '˶БӊӄÌ¼Mǟӈå˕єΥƒҤǳђȩԟ˽ˉŉȻƿ¶˻҆ςˣԔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.875501:+0000',
                                                    },
                                    },
                            {
                                        'name': 'шų˅RѪÑǑɹǬҳƺ҈.aњɳҚÒɯűӃʫʦɁɘŭЋΐʿʳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѹ\u0381Ǆҕb*ˌφúѮf1ѽтјԝшʹХι¶Ƭ˦Ā~ëÎȅżӐ',
                                                    },
                                    },
                            {
                                        'name': 'zĬʡʐүԡȄΒ(ƻ˳ιʓє҅ҫăЪҍаȶğ@ǟƹʚĴˋԧΓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.875826:+0000',
                                                                            '20210209:152853.875840:+0000',
                                                                            '20210209:152853.875848:+0000',
                                                                            '20210209:152853.875855:+0000',
                                                                            '20210209:152853.875861:+0000',
                                                                            '20210209:152853.875867:+0000',
                                                                            '20210209:152853.875894:+0000',
                                                                            '20210209:152853.875909:+0000',
                                                                            '20210209:152853.875917:+0000',
                                                                            '20210209:152853.875924:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǧ¦ԒƷ*ĬčωƌëȼЋƄǪ±ЯĀεƮԊǸũεĶЬˈȴ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɿЖé\x95οβϥʙ΅Л˞ЮςКҼ*бв¼ϱͼœŎǋͿǫ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԑ˗ȅ҃κϮΤýҲӚȦȾ˂ŠιѽƬѨʡ˅όǫεÒ¹ӕueʈ˴',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƢҎӯǲOҕнÕɹǾӆϠɤtҤҧ\x9eɏӥлǋ·ǙŮΝûӮ\x89Ҳƛ',
                                                                            'ƹθƟŪŦԏΰϠͽĨΜĝϙϷȤћ¸ɢΘƅѐɢтϳƎ\x8dȇӹʮΚ',
                                                                            'ǮԢɖԡƍíȠѫiӉҵʱҼόǱĬʠŘњҜɵˋı˰ȪӡѲͿǲԅ',
                                                                            'kȱř(ϺƅΠӎɓǔĂĕМ˲ɘȷ҃ҚУЃʵq˧ʣŖɓͿ·μ\x85',
                                                                            'ϼÓcǋLҜк˄іʷѹƕԎȰ]ЖԤΗҙ\x83Ũƾ"ϩ¼ϑÔ˅ôϟ',
                                                                            'ːŞНԙϯʼѝǅύĞ˷ρ\x92ϯҜΰĵХʊ\x93Қzʚ˸ɢȌrƢѤѧ',
                                                                            'ɨЛϬѵʡÑȥǇʯİΓėˡƎӟξǉɰÐɑ¯ʆѪŋƟƍşЌƨƷ',
                                                                            '²Ȼʅ³ÃΞԦɷґzϣƥƙƵ˹οǹʔȵʻǔʐϢϥҷΏϒ˵ǁȁ',
                                                                            'ǱUŪ˷ʑϹΠŜηˁθнϓȐlĿÄϙŰčǌɤȻɇƸMǄʸϭЃ',
                                                                            'ēԞƮёоЅÌʉҋЕЯĮĠѥҩŃÊHƽśǫНơϟʄ΅ӣɃɰU',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'śˀΠ˂ɤӚOʳŶҏêǔȅɢȊШԆΠԎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8927976524875331164,
                                                    },
                                    },
                            {
                                        'name': 'Ƞ£ԅԈȄǂ˵ԒαıӦӣΨ\x91ŨԇӹǽƐҡμŻӆаϒƌʿѥͰM',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '΄ɭӃƁӘ͵ņƽPȝ²âЎŐґÐЄʎįįȢӧӒƆɨ˪ǸǐӉԑ',
                    'message': 'ӵ\u03a2\x8dĻǛĂ˒WΛκräǁԃˌȏŬșŁҦŎ-BыMǮʮ\x97μȢ',
                    'arguments': [
                            {
                                        'name': 'ƥÛӋ8\x8aYÛʹ¿ɽҎƩïʾUʂɥɒƛ˳ªˣˉΥɠĝƆ¡ƖΆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            701470.5985916037,
                                                                            346696.59797899396,
                                                                            875816.1635866675,
                                                                            -85661.59021737342,
                                                                            222496.57868165168,
                                                                            376197.1950481477,
                                                                            -63000.54149453289,
                                                                            -28412.820796962536,
                                                                            980911.038572266,
                                                                            218073.02653364395,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ıҭȜΜϫρѐԂвҹƾйέŏзÞÍʮĘΡ¾BŮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϼæӻǝn\x98ӂĀ҈ӳ[ͺҢӥŊƉn˘ΩΦѠ8Ò¢ŅƓnXǋĒ',
                                                    },
                                    },
                            {
                                        'name': 'ƏԨςʊОčχƾǭҤ˰ҷ@˗ҧ\u0383ǫƖʄЎѤіӃƕĊƵʽ˧δ\x90',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ðĂƏēΪ˝ԀʾӯԢȌҬ\x83ιĕèɨǍʱŭԣ\u038būƸÃƶǵÈ˫Ą',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.878711:+0000',
                                                                            '20210209:152853.878757:+0000',
                                                                            '20210209:152853.878782:+0000',
                                                                            '20210209:152853.878789:+0000',
                                                                            '20210209:152853.878795:+0000',
                                                                            '20210209:152853.878806:+0000',
                                                                            '20210209:152853.878814:+0000',
                                                                            '20210209:152853.878821:+0000',
                                                                            '20210209:152853.878827:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '9Άƹˬ;>ĎϮȱʆ,ő',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.879110:+0000',
                                                                            '20210209:152853.879126:+0000',
                                                                            '20210209:152853.879135:+0000',
                                                                            '20210209:152853.879143:+0000',
                                                                            '20210209:152853.879150:+0000',
                                                                            '20210209:152853.879157:+0000',
                                                                            '20210209:152853.879164:+0000',
                                                                            '20210209:152853.879171:+0000',
                                                                            '20210209:152853.879177:+0000',
                                                                            '20210209:152853.879184:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȘӜԔѨҺƓȇϩʷΥ+φ˴ͱԋ,Á',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԁçŕʉŵǌǈƊǗɨʱҏʘ\x98ŸeʦɠɦсӚҏԋ£˻ӜƼԆԮ˽',
                                                    },
                                    },
                            {
                                        'name': 'ϪΈԎ·όѦɮŧHϛɍϼŤň(ЅΒҳˁȥʺǕ҉˷ǂŮΦġïФ',
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
                                        'name': '˧µȱǭϹˬáŝƧƝЊaʌĜy˄ŵґǛɪвɹҧŕϸΦŦҷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'žñ\x8aЗʺ§\x86ʉϺЯʐηɶɾ˨ŚɶԎǞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4645093572026407640,
                                                    },
                                    },
                            {
                                        'name': 'ƞҌӓȠǛ\x98ωμҒȦ˫\u0382řŠǋλӱ\x9d˹ɓšɖ\x9a`ȸ&QǚζҬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6935484950237039424,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӵģЪ\x89Ѻɑ΄ѣɶ+јƾCҷџʏϮΔѾʠͶҵǓѶÄqMąȁ҅',
                    'message': 'Ǝ҆èϵʹȮԏʕU\\рŇǱԃԈ=үʫ¦ϞοΥƞҽăΒ|ȧǒӳ',
                    'arguments': [
                            {
                                        'name': 'ǞůЍҹýƬГóΜԩú˫',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĽҙăϋӷÛ&ǾǞцԘɍŁȔωō˙îχͷҶ˅Ȗ˄ϸïҸʰʁɐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 613093.3096176073,
                                                    },
                                    },
                            {
                                        'name': 's4ǋĆøӄё',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԝЂ\u038bİϖƭPҀӥѵӓʫʱðj´~ȨɇĈԅӅщ¶ҁҴԆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4221697395126700269,
                                                                            -5371740106790241567,
                                                                            4126153876583004243,
                                                                            -1323317488402280299,
                                                                            3168370103632368124,
                                                                            -7094974355011076745,
                                                                            9221273340173058171,
                                                                            -1666182915339082448,
                                                                            -4741470509608415466,
                                                                            -681314091086532800,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ғ˗Ф˵җŘ\x8e`ԭʸϑŻЈЪԠΫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            51766.7320750744,
                                                                            674130.2957462452,
                                                                            349053.96261659707,
                                                                            160085.4939630961,
                                                                            50288.18913517296,
                                                                            532022.0626101365,
                                                                            -49178.59248613916,
                                                                            435945.30951108783,
                                                                            -93642.63384024963,
                                                                            796159.875861478,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѰĐƽËͿó϶ǉ®ǪŦɡǛ\x8cpĚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ƬӱĂĀßȽń¡ǐǥ'ƦŮйЗƸԍƈƇԉЗœúƜ\x81˨ēҼUω",
                                                    },
                                    },
                            {
                                        'name': 'Ӆƈѕ"ӑ=ҼʟƒÜƦ£ҿƣĻʒϱҞӒҟҹZǜ~ƹǩ˓<_ѣ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.881819:+0000',
                                                                            '20210209:152853.881840:+0000',
                                                                            '20210209:152853.881848:+0000',
                                                                            '20210209:152853.881855:+0000',
                                                                            '20210209:152853.881861:+0000',
                                                                            '20210209:152853.881867:+0000',
                                                                            '20210209:152853.881895:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȆʅΟ˂',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 597428.2375101382,
                                                    },
                                    },
                            {
                                        'name': 'ɹѶɮÌŧǶƴпϕʖ\u0378ϡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ěáǋԙ;ЗЛԕΥºƑʻĖʌĵš҉˝п˓ǿζŇѡӾȰНǪŰȱ',
                                                                            'ΫǽʱˊǆҋȫʅƑԐRɗÌϕXΖԅѓǠ˅˹u˞ңͰϝӂĆàȸ',
                                                                            'ѝ˼цк\x82#ʹf²ȵS˓÷ƛЗKǌʲϸҼϿҺΛΥˇ\u0380ӳȖƏϯ',
                                                                            'ԞöлӄБҥԁԇG˾ιµӠƦɷŲjĝĄsÔϪȵ˾жȓǭьň˖',
                                                                            'ϳƃǪɗǫȾǔùuҪΗƈĂϗ˚Mȣ\x99īÇ\x8dBȧЁǻęƯ{ʆĐ',
                                                                            'јъŠҥ\x99ǭιÒLͷЧƫԍɖҿºÏOȞҢƿĠԉd\x8aCӰͲҨ¥',
                                                                            'ƂɳҦü˥ԕčҳСšǱDſǵԨɼѪдЇɣ϶ϽɜϊӨͿǡ%Ƃͳ',
                                                                            'ɯ˱Ǣ\u038bЂʆ.ŘǸ҃У˖ǲǆƣəŎ\u0379Ƽȼķn˳ӛƍύԙЄƥˋ',
                                                                            'ϲ`ÈЭơәˍɌѬǄȼϞƗ<ǧϿϠҝƃӡ\xa0ҢƝӴblԟɱĂ˕',
                                                                            'ѠхҁƳӡ˽ԝπȦɟɺ˚γÔԑ\x93ɷmӂπГӚϩʬ҉ӫąíиԫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˉJ¸ѯѮϹϞƪѣ-¹ԒҰ˹ϩƙțZΘ˧ÑԏoϹȀOěĪ$Љ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8868006815567370965,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʀɟ',
                    'message': 'ȚΰɥЯɬDĽϨéҊҎǆ˕,ȌǄєöȊȂ˞ǊÍЦǫ*Ӏ¢Ϝʠ',
                    'arguments': [
                            {
                                        'name': 'ŅŰł\u0378mǜχ˜ƝūÇĘaɫȟԑʧ΅ȇȹ\x9aȭΑɥӧɶ˝ŮÓБ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3024810108566044775,
                                                    },
                                    },
                            {
                                        'name': 'Ԙͺ,Ӱ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǪԜŹšЯѷЦǹ©ɏ{ĊϙцɵϞǴяƃƦɡȸӪȑɏѹ\x96Ȯџǻ',
                                                    },
                                    },
                            {
                                        'name': 'Ȅ҄ӢʀԮө{\x91ӥϗǝ\x92Ԋύϣ\x84Hȅӵ%˸ԢѫπˉƑьѠϻʆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.886936:+0000',
                                                    },
                                    },
                            {
                                        'name': '` œű\x8aɂҟȣМưǴƦƉҞæӠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            818596.3466615906,
                                                                            220742.08026221744,
                                                                            196437.2894022955,
                                                                            -76062.09074195751,
                                                                            138078.15941941124,
                                                                            56063.16455247003,
                                                                            91034.85412675497,
                                                                            909075.2198062597,
                                                                            388943.7454957569,
                                                                            21122.601303800926,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҰѓżbɍҴӸW˶ȏηѸ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.887854:+0000',
                                                                            '20210209:152853.887883:+0000',
                                                                            '20210209:152853.887903:+0000',
                                                                            '20210209:152853.887922:+0000',
                                                                            '20210209:152853.887940:+0000',
                                                                            '20210209:152853.887961:+0000',
                                                                            '20210209:152853.887978:+0000',
                                                                            '20210209:152853.887985:+0000',
                                                                            '20210209:152853.887992:+0000',
                                                                            '20210209:152853.888012:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʜ3ɻǎΣ\xad-яʿμђЩęχRȎʖнɗɕǝ˜KӫΊ]āµǪί',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ѕ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            803963.7696149834,
                                                                            -32864.795730147904,
                                                                            622046.2856171477,
                                                                            583556.6993670202,
                                                                            809484.3358741716,
                                                                            681313.4945598397,
                                                                            25670.658757201047,
                                                                            321706.9017497911,
                                                                            924375.8404391542,
                                                                            286738.78061333287,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˍӓψӆ\\ĉӞҷϞҊ·ȂƂӚȤįWǺϪ˔ȮƶȶӶøѺƩΛе±',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'µˇрɞ3ԗAǡδǕ¯ҲҾɜȃιƭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.889799:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЩèĻΖӐ#\x92ϮɮšїŽ\x81ҶÎ',
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

            'scope': 'verbose',

            'messages': [
                {
                    'catalog': 'Ƽή',
                    'message': 'ĩ',
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
            'identifier': 'ȨŞ1ȳ¥ˊӡӗÒϼӃыĦҊӖЏυʃɲɷ§',
            'categories': [
                'invalid-user-action',
                'configuration',
                'configuration',
                'os',
                'network',
                'invalid-user-action',
                'file',
                'internal',
                'configuration',
                'access-restriction',
            ],
            'source': '\x96Ƶxӎ\x8aаɩƂƛ\x9fǒɤÑş\x7fͰǄƓҲȋãҴҀɁҒԗҠð\u03a2Ɯ',
            'messages': [
                {
                    'catalog': 'ԘȫǔГÒƕȻʼɉĞНΚɘƲ{Ȫʅǆī\x94ÄþĚ3ȷχ\x88ΛŤΉ',
                    'message': '±ɭƑ}0ǤϹœʞϙõ˵1ĄϠɼŚϿĚҨłǸēǤĨΖǧɓƇƖ',
                    'arguments': [
                            {
                                        'name': 'ԋ˩ÉßȼώΔǽЕŦ\x8bΆԂːƆŘǤʜВȀ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7765472012296156300,
                                                    },
                                    },
                            {
                                        'name': 'Ń~ӰŐșӹь\xadǭȺϪӃƼǑΣȆѢҦҒčΝƯ˒ЭƄˣǀǣĝΡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.921666:+0000',
                                                                            '20210209:152853.921720:+0000',
                                                                            '20210209:152853.921736:+0000',
                                                                            '20210209:152853.921743:+0000',
                                                                            '20210209:152853.921750:+0000',
                                                                            '20210209:152853.921755:+0000',
                                                                            '20210209:152853.921761:+0000',
                                                                            '20210209:152853.921767:+0000',
                                                                            '20210209:152853.921773:+0000',
                                                                            '20210209:152853.921778:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ķңϯӤô\x814ӁϯϞˬҮǼƮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ÏΛŵ˚Ê\x86ӬϚȉŶˀ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĐĿҳɛȈñѸҦǥƩӿʣ\x80ϫnƪĀјҷˎϢ,ж˙W\x99ġĴЎʮ',
                                                                            'ÈªҔêҫvÃЍӠ˖ȂѕӌǁɻͼƃҴΪϨ\x84ĢӯғϥŹȣГЃô',
                                                                            'ѩʍũ\\дdňɝōӴƑ˻˕ʹηÆǪȻơ˦мÐҶ:ґ҃Ǐ˺ьĊ',
                                                                            'šƪ҄ĆţHńђƿżƈƲȲΓϗŊÏԁҰĂƚ%Ԇ-μʘΫфʐH',
                                                                            'Ѳǽͷwĕ҇ЮɑĊ\u0382ΞΞӁÒ˛ͶԍȍɆԟ±Ͱ˸υЇ\u038bçϮӃǻ',
                                                                            'ͰӣԂȿłБŽǺ˳тɠ$ɦ\u03a2;őɂĤӜΗͲ\x95ъϥ˔ӂϘɎΔʖ',
                                                                            'ѭ϶İзƂҝīҽɃǑıКфмUӼӊ˜ΐҙ8ȸ@ȼЇӘ˫sҿԉ',
                                                                            '¢ü\x98˂ķŌ¥҅˔\x80Ȳʇ϶҄δӪʍΝǙӱŵʖVĝΡıŔӱҗǦ',
                                                                            'ΓҀʚȥԊτԂϪɚȔԧéΤϳҤ҅пήШyơñƺE\x85à3ɋ¦Ы',
                                                                            'ýȠѴȬȽǽΩǏ¨ȀλγQρпbώėҨӸɣǈ\u0379ѴŦҡŷȺα%',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɣєʟҐӱƁҳʁ\x80Ҙҟ\x8agШϖơԪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƺЎɰҲ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǧϸǓ¤ј˶ǜʕŵĬ\x89˽ȏ¸Ţ±ţǁϢШ;ԈƕЅƵāŠƮŜ\x90',
                                                    },
                                    },
                            {
                                        'name': 'ήɬĭʋʛѝϳƉвǶɹƓΌeЗå¹ѣ҇ŚЎïɗ½.ɱʞʭԩȮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.923088:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ëʘ?Ȳ&ǫȤϤѦÿ҂Ľ\x80ŶʄƝ҅ϝȂҴtÿȰɋǖζʙȦčș',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            693309.7827128493,
                                                                            365159.2412048075,
                                                                            584303.8976713757,
                                                                            353826.20343678986,
                                                                            948297.955466886,
                                                                            515196.58591081365,
                                                                            254399.10322255432,
                                                                            75486.72526894239,
                                                                            252198.04717807443,
                                                                            177163.24921034387,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ёη',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Óŧ\u03a2ϧζϡЁġ˰Ƽпɭ˱ȑʪuϘЅˉӤƋɋɕΉΊǺԏƕʟd',
                                                                            'ъŠØʾɝ(œβʡŎӲ\x83ԓΡ\\ˋɽ4ǮЅԇҽS҃ȪɖɑƮΟѬ',
                                                                            'ԠъԑͳĖˏϴɬC˙ƪɞąǁʅłU/ɹʜȀǏɏԪŅѦƊǌŃɄ',
                                                                            'ϦMÚʼԡɡgҺюƝŦϚϓдʉϪ҇ҀЄƽø\x94ѫ/Ȃм˨ğʿs',
                                                                            'įĴȉЀˏƩǣéөǞĄҕsϗѪтQϠŔǙF҇ÿѴŶԣ˹Ͼʙӽ',
                                                                            '*щԩѼƐΖԪ©˱щÃëҘŵƓԙςɀԠбϚӉҙƻİμњѨŭn',
                                                                            'iŃ\x95ƤɎúÿőC\x99Κɺɩą\u0379ϐƇΖˊöŞѹϧƇ˰ɳÀŏ\x81д',
                                                                            'λŬņɡ±Ĺ×dƗĜф¾Ӗʠ\x8cЪȰЏԟʧɐʖĺˆŲӑˎϭßύ',
                                                                            '#ƃӸͽ¶ƳЭ²\x8aЍʮӍ\x9eň®ϬЏ\x84įȫɝҠͺÌzөɒƭ˚ē',
                                                                            'ůÙӲӗ\x9aҟʼ˾ҕʱɤƳŨŠáԞƻʓηОӳӸēϰѫçЙʩԊ˫',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȷȿϞîǳŏɴӱÓǞƐˁȵȭxЏʷήЫӼчŎҚŽРð',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҳʓŷԔԁƺSˌӡҶЫÓĤʃ\x95ИӘĺƇʨѬҬĦǤͶѺNʂͿϢ',
                    'message': 'ϼʵǹ"Ρɣ:ԊПlˋζȽθԢţπʇĦŤӗӁÍΉŀͲÝіСǗ',
                    'arguments': [
                            {
                                        'name': 'čũқāĢД˙ɦʠȌɷǅȑӴʝҪˮġýЬʼѻɗӻʾ҅έ\x9fƣӤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϕŲVåЏϗ{\xa0ҀӔgˈ҇ɤİ҉ƝağŢȕʲġВʲĆˑѧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            666258.1382887033,
                                                                            807421.2030235823,
                                                                            306528.41296018823,
                                                                            735736.7728431779,
                                                                            111266.14027299875,
                                                                            241286.28034061246,
                                                                            437220.70321314456,
                                                                            -48812.92397019095,
                                                                            22344.927850697306,
                                                                            423280.8607026798,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ф-ӸȝǃƃΊжӔΊǂӧŒŪĥNԖԭΙҊĒ˟¼д\x9b',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6590302708149522773,
                                                                            7116305572321548817,
                                                                            -201349410280877542,
                                                                            -3964407287662254342,
                                                                            2458760731324526426,
                                                                            3461629280021214058,
                                                                            5938905280008772446,
                                                                            4356153058626611273,
                                                                            -778536708628606968,
                                                                            -8813477724027698620,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϫǸȔԇΙƞƍˏεºɛҨƵКåхΎԖΪʬĕȋҮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.925019:+0000',
                                                                            '20210209:152853.925038:+0000',
                                                                            '20210209:152853.925046:+0000',
                                                                            '20210209:152853.925052:+0000',
                                                                            '20210209:152853.925058:+0000',
                                                                            '20210209:152853.925064:+0000',
                                                                            '20210209:152853.925070:+0000',
                                                                            '20210209:152853.925076:+0000',
                                                                            '20210209:152853.925081:+0000',
                                                                            '20210209:152853.925087:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǔν',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.925341:+0000',
                                                                            '20210209:152853.925353:+0000',
                                                                            '20210209:152853.925361:+0000',
                                                                            '20210209:152853.925367:+0000',
                                                                            '20210209:152853.925372:+0000',
                                                                            '20210209:152853.925378:+0000',
                                                                            '20210209:152853.925384:+0000',
                                                                            '20210209:152853.925389:+0000',
                                                                            '20210209:152853.925395:+0000',
                                                                            '20210209:152853.925401:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ώӟǭʓҒ6',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Čňә9ХҾΝŅȰΚγŋˁʺфÛȠAůˈΏÿģɮɬϛŁѻӥǽ',
                                                    },
                                    },
                            {
                                        'name': 'ЏǡήϝƝ÷8ͼǸə˜',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӡζ҆ԖɌ\x9bʇ\x9aʉӷϧƹӰ½Ɂ\x95ÆŢϺÙxŗ˼ÈƊѿēƑϩŠ',
                                                                            'ΦΓȋÆҚ[фƝƏȚʙюӗʁǹ\xadӸ±ʹӲuΪ˨ėȟǫňÔ\x8eΗ',
                                                                            'ƵʖΆȼȜӐǙƿ³ФѮĉğχȌƝ¨ǭ\u0380лЎǃϖҵПŹȟһҲǔ',
                                                                            'ǰįàʇʱϼ³ӬXƒˎѵ˟ȬΨ$ňϛÝϐǕë˾\x94\x90Ő©¢ή{',
                                                                            'ȅǧâӕȆғϗʚ\u038dʱƐzǧǴϻΦ˂Əηӈ\x95ƻ˂\u0379ϤÒ9ЛĨҞ',
                                                                            'ΠҢ¦ҒωøƬНЏȃ˲Ƭ-ø\x9fώˎϕÌőԭДЭшͺΐʋҗϘϣ',
                                                                            'ƃŹԟǱмӳУʯɄyҹҭʉưɍыéđäЃϛΚɐҚҊϽêªŘf',
                                                                            'ҾʮʋҁțĩΔĠΣ˩4t˨ƐÞ˽ǯ҅ҩϲůϊ˛ʁŇ¦QǅȮi',
                                                                            '˥ѽʻǖγǍ\x9e>.ǚȀȌʓĐОƳϑzʑşƟԐʪɞēдǄԪȔ8',
                                                                            'ˍýԪĞċ¤ũ"¯ʝƓė҂´\x7fȃƵҠɋƗ˰Ӄӎӓ*ɇĥSɆC',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͿāЍÕŖоӲΟǖȟȽʚǂÕ\x93ûǔˎʺԗѕˌɈʮqİVȍˑȏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -18988.207732553026,
                                                                            530018.3426956047,
                                                                            682482.9188295731,
                                                                            -78753.3571648982,
                                                                            120523.20533122844,
                                                                            267705.4427602429,
                                                                            670090.0024205259,
                                                                            -99562.15300707846,
                                                                            990574.0080716105,
                                                                            599420.5877456666,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӠǵˑΧүoưϽĽЀǳӎƼǿʇ˨ÿҋŶǍΨӋˀȄͻɫψ-ϛŹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '©ŵĖɵӦқƇѐ\x83аџʔłԍϕįҊǢԀħǗΓѦǷӏƤƪǄϷƄ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6467185816659593670,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'čïǮӁӪю˳Ԟϛҁ\x80ďϟӕīўҹӯǤkҤЧˈ\x99Ȣȿ¦y;ƥ',
                    'message': 'ˀ7ÍƉʬ>ɠӑѻʳÙÚɳŐԖȑɌ]ŇƁƬ¯ʜ¦ʣ\u0383;ÚǄȎ',
                    'arguments': [
                            {
                                        'name': 'ѶUԭѧǠĒѡɾƩǨѷǞĂљХʎӳɏǝ"ƅȸ\x92ιјǦÍЮӖԐ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÛҮӒҿǊ˽Ҡ˲Ҋɤ˩ʝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 304755.2244765945,
                                                    },
                                    },
                            {
                                        'name': 'ĬϢΪҕΔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ә;',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɌЕѹʲFǭώϑȺˊ·к',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȫƖǀŵңɫçȵԗќȅӍÁ҆ԑǾʂŶȋ\u038bԔĹȁ\x97BÀGξȼy',
                                                                            'ʼřŐЊӻЧвѹΈ˺҆ҮˉňLҬƅȠʽǊмʃʇƑȝьҷƈ·ǋ',
                                                                            "ҁĬѪȱўȀ`ǙźɏǪϫԤЬ¨ƼôљӋΙĘ'Ԗэʰ°жaxҗ",
                                                                            'ʖПɷΏѽԌpώ˶Ԍ˩Ǵѷ·ƢŰİµԬћГΠɁӐЍѧŻ`ϰƲ',
                                                                            'ɇĥǡ΅ŷǮԭħĜΪ7įӖӻҺǋӝ1ȿǬăˀɵ$ǡŶŻɑҶӦ',
                                                                            'ѹĹZ\u03a2ȵĺ]Š˘ΎM9ʵʬʩɲҗϸȢɴҰǪҸȲϑĿȞǫϺȅ',
                                                                            'ǽ0ϖϿ\x9e҆ѯԍƂŇ\x87ϟÝʫ҈ǁȎöмƂшё\\ɉԓˢ5ӑҝɭ',
                                                                            '\u0380\x83ҾɐǙZņǑʯǌʯɜўҦŦБРËΪƶԬСőӀǎɾԀ˙ӷѡ',
                                                                            'ˍ®`ԪŖP\x95pƤ%ҹƾʏƍʖǻͲɸ\xadćoҏϻƁͽԗιӷãϺ',
                                                                            '\u0381×ũωѰíΎȞDƸіĸɷȾʓ\x9aǣ\u0381ӥǻ˕6Ƌ\x86ȱĄҖΒϰʩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɂɥƉΥ˶įѵĒ\xa0ϴ³ĮʍǥԒƐǰʑɍɀU]ωʅȣŁП@Ȕί',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 232625.21406513813,
                                                    },
                                    },
                            {
                                        'name': 'ρˈĵĊғÕΌJ˃ƐӤƌŐ¡ʿΚʈĤȏȘҖOΩүνʽˇĕȔˇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.928663:+0000',
                                                    },
                                    },
                            {
                                        'name': 'cŝΡàɎ¯ƊmҍơɞϢōЃŘǮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЏҲ˞ԢčΧǅ<ɧѱС±ΊԏӨġ˂ː',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ºʛǄƚӿǕϐкŁΡƙǙ§ŽРѪΐÖҝŗĪ¦',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŗӍԤ҇ϮӐ\\нɿΣȬԧӇ®ӂӊ˖ѿζÊћ',
                    'message': 'ӜЪȐЧř\x93àȎǲͰʟͽњ¢Ȯϊɑɠҽˊϡʈˢðƫ\x98\x88ƁʎШ',
                    'arguments': [
                            {
                                        'name': 'ʪɀÈ϶Қsӆˉ˙жҟʢˬŨ^Ę/ӃɒüѽрϏ҅Ϥäɠ¾¥ȉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΡρʟϵηĪъϟκȸҬ҄ʲаӃӡɔӃOБЯKc¸ʧΏʅǴϣп',
                                                                            'ǑÞΒҵVԩФӄ˾ɸρԡӦŁǃʩ\x8eˍɻӢ˱ʟMЛѐXĩȦӠŋ',
                                                                            'ΐ˒ФčӬіїȯ*сΉѡĬÈгӯ¦ЍˊȀ\x91НʠȈǉɂѩӱČM',
                                                                            'Ԉѽж҄ėĖ{ЁʕĊ^нԜΙҦ:ҴϷĜ\x9aʃѰ\x88ɗɝÒāϹξЉ',
                                                                            'лȪƢŠ\x97ˠƗѴǜΝ\x86\x8cȒѩƫɆoˎȯʗϏʣҏøéơϤû·˱',
                                                                            'ғϷ˪ŢΎ˴ɭ2ʓcΛѱĔϮӰѯɤȝ˙ęӖɳ\xadРYƩʍΌӽҜ',
                                                                            "ęӃРз˝TMҕºĐ˙ˑſҝ'RǂűӕέÔδ\x9fˑĹɟƁƢĢѠ",
                                                                            'үӍѤͳͷͷҩ´ʽ˭ɣӐϲҤѽ½ƹþӓBɖ¶Κ˱ЌЏæǜƶȸ',
                                                                            'ѤŪӢɵ˴ӎԛіаƹԜ҇ɊоʳϨΖЊҰơΒƫӱѿϗӼԏ+\x9f^',
                                                                            'ɹϱλǝ¸iӰӢΖÛƛǉɀӄ˥ʸТľǶʢϦ·ϖҗδΕȄǊԚή',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '!ûǅǡʾ%ζˑz=ԝηAȔȼư\xadԂN',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 505255.0994381871,
                                                    },
                                    },
                            {
                                        'name': '·\x88ʠ§ʘҫƨϹӥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2310399794635822555,
                                                    },
                                    },
                            {
                                        'name': '˕ƯȚɠƕɁªѴòĈɂưđ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΔԦλΤѓΚÿЩԋԠǔ\x9aώ˔ƉԞΨɖμ¤ĮƳǰϥɣ\x8aϘ"ıļ',
                                                    },
                                    },
                            {
                                        'name': 'ԤҚ˞ϣϺоÌĔѤ҇ҟǒĦĩ˼ÂƪȩŗʪƫϞưňŨϗ×ΐЃ΄',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2376475625587705004,
                                                                            -6186397480240644769,
                                                                            -8332303268126014034,
                                                                            3577915852620376740,
                                                                            8187158868352053153,
                                                                            5288481901744838081,
                                                                            -1632166136387913396,
                                                                            8378487840020369773,
                                                                            -6540436296405917591,
                                                                            -4258313052300886719,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȩôӏϷЩп҅ÍʪƉѝщͷӟ\x96ɻaȘʎʬū7ƒҬϺȎɠѳҌï',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'șӴљÇƑӂɰɋʊʾʕȝ·ƏԋÊӤcϞΖοԕșǜűǜȹăʤÊ',
                                                                            'ÝŴƭϋňКĔзȹү¯ÑʟċѪҙǓԃɰ"MВŭęщĈҞˉŝ¶',
                                                                            'ʰŽǃȀҫӞԍŻǒȁψǘ²ԤēPɝʄϬґҀ˫ƯήėͿʛŦԝʲ',
                                                                            'ώӷ\x9fμȡɏņŋKӥĶȉWԍҾ˴ƿлñnʯ˄QÎц\x8fÐӈ¬Ӹ',
                                                                            'ʄʒċϢƬЫìѪ$ɗʭԇǁӣȅÃԩмҫβјҜİõq±АӷĲ£',
                                                                            'ĵʌŮ÷ОƐѩЖõŎ%uĴʄνŶƁԇÛг3ÈÞĉȁȅ˔XƤñ',
                                                                            'ǆŘιϖƻӔˡ2ѯŀɟ(ӛҙȞê×ơ;\x96ĳ4GϤ\x96ЖȦӁԋĮ',
                                                                            'Â%˛ƯҮɅ\x8eԭЦЗʐϷƒ\u0381h\x88ԪӚӔġľѯӃƯ\x80ǔˀƱ!ɫ',
                                                                            'm_ρɆĊхјӡí_ҕцʮάϵŪʔƐŘęфʆλҌȶύʏѲуü',
                                                                            'Ǳ\x9b]ȩìγƐіӍμԀɜӉ˞ƝЌʇǪŒ˓ŊϚŢϵɞͼËĨΑ˸',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˲ұƇŞϕõсƅˑ΅Шň\x98ȉ\x90БaȱȢ2ɯƢԍȈʒӤďØ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 996914.6556928926,
                                                    },
                                    },
                            {
                                        'name': 'ӱʺ˅ҜȤĚƘфәѡ\u0378ӰǊԓ;ǷďƜŕπΎľɗ¶ɿ;ȂΞqў',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'Э\u0379ӔѲԟЙ\x847żҾîʿȄȴ˃Ɯ=',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɁwƟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÉŚÓʼɑȒӹϸӑΚOȬvǳÆϕκД?ǕɀҝԉLǥӥ¼Фȍ7',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ìʨ\x97ǥˠ˛Ѹ%Β҈ѨћύӃԭłĥɑŇȒӨӃɓʜoâľѵԈà',
                    'message': 'ΟǖƳ\u0383ˌ҆3ҳøɦӜ¼΅ϲ˵ҒĹѳИōΓ˕ŞγʨԙzǼĀf',
                    'arguments': [
                            {
                                        'name': '˂рџѣΤ\x91σ{ǵ@ʆȕ¥ǀчŏұǈĄ\x90š',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 18168.443196127817,
                                                    },
                                    },
                            {
                                        'name': 'Ӭʔλ+Ԡ\x92ôϱԋЅɆΌЂȂƛԪΟϦʚ=˚ŠºΜϕψԑΒΩĺ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 820155.1779842952,
                                                    },
                                    },
                            {
                                        'name': 'Eŉ,Ѳđ"ʝȟ\x8bɭԔ˚ϭúòȔԊ8yǇɉĬVӺӒę˗ʼĚ\x99',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5405812626163734643,
                                                                            -5969873770312221550,
                                                                            9058312724851756237,
                                                                            6431008597489957416,
                                                                            6781125264640064572,
                                                                            2152720963891113102,
                                                                            -7016447702939989047,
                                                                            -391862304920632147,
                                                                            1754567985727499487,
                                                                            -5586241894287697166,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʟȡΛy?˴өĨǒŴҳǂэϨƳϻҖѐԗ˒ǮœƑʨŶ˃ʨϹąÏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.937339:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ăĔҀǱćǎϳ\u038dŲұ9ɫԉҦ϶ˀǹėОBΰlȻŁ=',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.937718:+0000',
                                                                            '20210209:152853.937754:+0000',
                                                                            '20210209:152853.937776:+0000',
                                                                            '20210209:152853.937792:+0000',
                                                                            '20210209:152853.937808:+0000',
                                                                            '20210209:152853.937825:+0000',
                                                                            '20210209:152853.937841:+0000',
                                                                            '20210209:152853.937858:+0000',
                                                                            '20210209:152853.937874:+0000',
                                                                            '20210209:152853.937891:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Т˷˚˛(ΣIϫԌʮѻ˸\x83\x9dˉʦҲˬҜĒϷӂȋŖΏ Рé',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȵé',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            352522.38308565546,
                                                                            255780.40820983582,
                                                                            248599.56755326898,
                                                                            742922.5486101343,
                                                                            80991.40403319104,
                                                                            19842.25973579324,
                                                                            962183.8267409962,
                                                                            655033.4034483217,
                                                                            271693.20569860213,
                                                                            776508.0889047027,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'HȲĘĉ>ΉРьʬΗͺȧ÷җĹɁˆɄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.939672:+0000',
                                                                            '20210209:152853.949272:+0000',
                                                                            '20210209:152853.949297:+0000',
                                                                            '20210209:152853.949314:+0000',
                                                                            '20210209:152853.949327:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŅђĨǲ¡ɮŸϝɄҜêʜѺɲȬ7öɎ½ȣþкк',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȹњ҈ά˦ŌĲ¼ˈԒ\x92ԦҥǲɑљúÿUŝ;\x95ұкԚ?ɢ˴Σǿ',
                                                                            'ʬм\u0378҂DȷӦΪ˾\x9dͿȊнǏϼÕ´ɤΈβĎȷȀƧɰƊ,ÙɃɰ',
                                                                            '×ӓ˳ҭΦnɱǕϷͶĖàÈtсѕ˨ʥʹϐ;ǣɧʼҊǉŁʎ=6',
                                                                            'ŶƻӞˎƤƮҏ\u038dԍ˧ɍ<Úӷ\u038dŧкqѷ®ǖҥ\x97ɆѮкÀHΤӈ',
                                                                            'ĀπԕþĩĘҽųΟŲʛÇˑӅвԍˋˆ|ȜʁʰơӘƈˠкԞƗ¿',
                                                                            '\x87ͷ\u03a2ӧΗӧŻŷРҖӡŉȳĢʚİ18ϪғȒ\x81ȜūŊЩʵDɴɥ',
                                                                            'ƻ҈ѴΑя҇ƕɎĆ\x83ǩԪ;˴ȹĕʁѭ\x86ɵŭӥ˚σ!X\x93\x84ҞŅ',
                                                                            'LҿДmrȱƠpđĆȢɝźșȁʟ˝¨őÅĽĐŗ¸ŮИȼΩПϊ',
                                                                            'ѻØѵ¬àҍΜʽϺŘѤɐѩª·ϾοDВȀҕ|ǠϏʒщǶˋǑǶ',
                                                                            'ʼχȤtΉƁХʀǐȨŲ-ɶώԙΒúJĎΓƊɋϣ˾яӽƒ˴Ɵ\x8c',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͽȁͲëŤºҦxâ˰5ŋӛĭţ҈ǆϛԬɞǎɯР+Ô!ҁ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ôγϨ˞ǎͼȠЀȦтӉɣǜЃ}ƲWȸōJĐȁʟԠЎɅԎʀЋ\x94',
                    'message': 'ьӫɳѰҭόΈɟӵǮģϮ˯Ďʎóȡ˚ʖСÇǬʶũ¤ӁӏXȞƪ',
                    'arguments': [
                            {
                                        'name': 'Ċ=@ƅǃϑʋԈӱ,˒ŴԦȞ˫ȥ¤Ĵ´ӐƕўƌːȯÐƪϧsʻ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӑÅ\x82',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ТԌ\x97ԖǠ˸ĠҀ\x90(ȫ3ȍɪʷ\x86ĤVʞĕ˭ϣїǖȇɆȃ˲Fū',
                                                                            'ΑҢԌìҶθƌ\x89Ԡӕð¾ԡǧɹѦϮʩȃȃìKƌϻȋȟҪFó˲',
                                                                            "ԃǿαάǉCԂǫϨ'Ěѣäʫwƫ´юˉέҮ»ԭ˺ЎfϷ҄ɣ5",
                                                                            '\x86Є7ÈѹÒ±ѐ\x89ЭҁЉыτ*ǜgґ«ƫΚӲӋÍȅőRϡ·љ',
                                                                            'ҘŴЂļƁȀȋȻÃÏʝƫɼÚȆ˃ɔȸӪ\x8eқɺŠÛЂΈϾʧýT',
                                                                            'ÎΜԎiǓΥʎɦǈōԥʩȸČ)ƍӧ˾¼ӳΘ¼ͲǤªΫơĉƇǻ',
                                                                            '˓Ж·ΫӮȹ˧ĸȁѪǟ5Ҧɿćý#ϖVԮΑ˨Ǡǣɀ˄ϓƷвă',
                                                                            'DΎȓԀǛѤѳ\u038dŰΉͷϑəˎєǒǄƻȂĤԈƐʡϏżʍӢɍϖƫ',
                                                                            'ͼƦȑŤСȜɾӬŭϋʮĸҀӡʤɦãěŮͿΥҡУϠ\u0381ϓϚ§ζΏ',
                                                                            'ʩХЃԝѐǞшȅвԔǗμκŴ;ɬʜԨş?ˢĢĥȷϔɜѮŮѾӁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'QϼϿǏiӠԥʾńԧҞĽį0ұҭŖӖԁѺԍϮϜ˾ĊƇɸӣʇǗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'İƭôĠĢǌPɐјǫȋΚιȎқԓ»ÞɊϳšфıӰҟɯюEǈө',
                                                                            'ϲл\x81ѥˤйǼҬӐԛaʮÎ¡¡ȨџŷȫȞíӺŹƳˣÍǧʍҏȼ',
                                                                            'óԐ&ͺǥȭ-˅ˮэ±ЭűΓ˺\x86˪ԮÎʮǸγҤĻϢ¢ƒӠɸ΄',
                                                                            'ľͿњȏƑŦϻˁÎЬǠЛԞ˾ҨѴɍˈʈӋ˂¢ÒĀ2ӫþǐʒԮ',
                                                                            'ˡǧYŏýȕ)ӺHȻͰȞӟ˽ˀƴƟұїЂÔхͳɺƒȭάɔŢƵ',
                                                                            'ύϼȉЦ\x91ЭҾ5҃ȰɓԅНњŘȶȆɗнѽơƃɰӶŗƫ®ËǣŎ',
                                                                            'ʗǕâƫБќ8WӢˁӧȢѝÚ\u0383ŮԍӮìӿ\x8eŅ˔ʤÌӨԆτλÓ',
                                                                            '˾čə\x90ɎʾґΧҢŭОΕϴ!Ζόɐ˹ԈәӔĶr\x92/ȹΝɺԩï',
                                                                            '2ȄȱˆǦέѪƉʐьǗɋű4˂bюơɯΤϨΑΆӜIΡ\x8cƆɇĕ',
                                                                            '<ǌҭȟЯƑòǩͼЎѓчʚҩѴÌĆŖҸҗ^ķ˝˭ŜϏÉĳ˰ż',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ź5ʏ%\x88ɏȶѫƬřʈ6ͺ˺ĤʎϭĞř°ǓŧŇҸ\x87ӫр#җϋ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɪĢżɶΈӲϐś[4Π˳ΈƆşͼıȀ/ÆĨdӶʨ*˹ʹӬCŞ',
                                                                            'ѥƹƾϾʐ˞[ѱģ|ҷȷƌÔƇɶю˨ʡЏϤǎҢĠɍʞɐŉ]ˇ',
                                                                            'ħӞƓТ×ćƽ|ī\u0380ӵīɢǥľ¹хëTó_ƣʳWǍŭ҇əàʻ',
                                                                            'мНɏцŕûӎԐĄϽV\u03a2+ǧ&ĝʛƕńЖȾԪüɾêȐѫÁŧA',
                                                                            'ƫǔңʇɭШiÎ\x84+҈ЕĊɰѵҚнӆόēɀӓʳtӭϬǬøȜø',
                                                                            'ǽĦȺ\x98Ċɋ˄½ƟKҾ@ÌˊµǠǍʼǶɉ\x8fɈʆĪĩδïЪŞØ',
                                                                            'ǖϲͳΫ˵ƸҏmƞÂǡɎăȯǙΣΡˉĕѳҎɾÌķÉËǔЪϟŅ',
                                                                            'ƨ˳˽ѯʌƆąŤҞɟưԁ1 ˘ːOºlěŷŊωǞıΩ\x8fӒw*',
                                                                            'ȌΦӴŤˋΙƐǯʽϗԕϡ\u0379ʿәɕ¼gӛȁϡĜãϊӓƥ˲ǕЌӿ',
                                                                            'ӹǫʙʥԔȯòǧԩ;ı.үīǹҽ§őͱƐήвƺВæŎώ×ȥƬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӌ˻Ѓї4јӭɍһRϢҾƆƳ˥ʝѤˮтĐ˅ѰԤƦŞGѳxģǳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'PıͽеЪƗʄЍĬ@ɞ[˾Ή˽ȇ҆FŰɘȘѲ\x8aԂӨ\x9cěǳΘґ',
                                                    },
                                    },
                            {
                                        'name': 'оćǤƂȅ+½лħƣωX8ԃ\x84ɚЫŹѳľĜțϔϻŞƵʷӓ͵ù',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            357408.4597303601,
                                                                            519536.55646758503,
                                                                            281912.07370532735,
                                                                            515254.38727571187,
                                                                            647755.5341016129,
                                                                            810377.9046330302,
                                                                            113393.22951599714,
                                                                            814426.5018406819,
                                                                            681648.2240315751,
                                                                            740211.2736384048,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x8cӜчŸɒˋʃϚԛӃĚ˩ġÄȝґϧҢԉǲöʐδыʝŁGǤκϞ',
                    'message': 'ĬyƉϧѦǗ҂һɰѥʿĶŦЙԃ%ěӋ\x87(ʹ҉ëўϡѤСȕCȒ',
                    'arguments': [
                            {
                                        'name': 'ѕˀЄʆѾęȳ4ɵƘWѝ\x83ΥӕυÔʜŎӫψɛЬΈȍơĿѳʩđ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ƈōԝ3ëǰZɢʭȊ͵ƉҶӐѸȾƩÌςφ±Ʋ\x83ЀÛʭ\u0381ɗŪ˹',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 330551.5814958795,
                                                    },
                                    },
                            {
                                        'name': 'sCɏΈ҈ɛЧĮŷȴwσȂѡ΄¸ŻȵŏϛљD\x9d\u038b',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.968543:+0000',
                                                                            '20210209:152853.968586:+0000',
                                                                            '20210209:152853.968602:+0000',
                                                                            '20210209:152853.968615:+0000',
                                                                            '20210209:152853.968627:+0000',
                                                                            '20210209:152853.968639:+0000',
                                                                            '20210209:152853.968651:+0000',
                                                                            '20210209:152853.968663:+0000',
                                                                            '20210209:152853.968674:+0000',
                                                                            '20210209:152853.968687:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'À\x8cϿ˙жӹΊǗĔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӷуМǾϭƄóÖΕ\x99ȮΥΘ\x98ϺƛŗÝϚ,ŬĢµ.ԞΏŇ.łʃ',
                                                                            'ѯʗδ˹ȨďƯ¡ȑüЅзԌ˯\x7fŇΤơŋЖϼȾşѫͽěԪ\x80Ȋ<',
                                                                            'ЇÑǁŧӬßȑԒÍωͿΌʋƀ¬Ј϶ԥƙȅƚЂ¸˖Ͻ\u03a2ƃӖzҹ',
                                                                            'ˌΊª±҃ĀǠūňŌ˅ΈΐɀϠĹþѪǮʑ˴ύ¤üɾāɽмŮϒ',
                                                                            'M1μŝԡΕєňȳӃŇ¢ĢιшԧөȯǒƿŔʅұԩĢɵŗ}ɸα',
                                                                            'ÊΑѦʥ\x8cōѕƐɽȀϥʨțeŪ˖ɁĒņ\x9aġɳԉϖͿҗūʵ;˛',
                                                                            'ȦɒїӉ¶Җ¬ʴ®υхѩāÿǪ(ʍӀȖӝ~žӼ\x9bÊʚȯӬіԓ',
                                                                            'Ԫ\xad9\x95р\x90ŉѴӖѶ҈íЄʙԗɖɶ˄Ω˥ŊāțÞƒԍй1ǲ˺',
                                                                            'Ҟa{ЌЄˊYƪϚԫӞщ˕PЌϴӪЄӯ$ŤȰ˷˓½ƟφɮʊҰ',
                                                                            '˚ϋę|üóчљƆȓbʈLϷΈƽɘĲϡЩˉğ±ǧдμã(ɩȠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˬƺГƮЧӯ˼æĿ\x8eГ\x96ʸȜдрϠɗ"ϘϊЧŇɪ\x8bӫЅԠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '?ǆѫȜƼɡцϑǫ!ʪԟͰФkÚįǕȇξʫӾƺʦсƓԜ.ζȝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ůȗ˺`ŠЎȑĄϺԌМý\u038dϯӋh\x7fвšѥ҇ЄӴ˴˞ϱӣˮ(P',
                                                                            'ȈȧȟԕƳgӣɽϥҼȦŴҜõӝƟȕƧЦŬwѼɨѣğɳǃǦϩʚ',
                                                                            'ǎžßҟМ®ńǘӃ:ɕƥѯȡˊĨΟԩʠ`ΤļΌžӹԜŒлġǵ',
                                                                            'œǨåßĻ/ʬƽwːԘþрªϤˣňǬѐЅǤΫϮЦˤԕгʞȽӈ',
                                                                            'ģЗ\\Сǋ-˕ɇҦšǩϹǢгßϑʭˬҊŀЊήƱɕѤo\x83ҖƦθ',
                                                                            'òӁɪ˪Ǚ\x89Ƈ͵¬ӄѦƗ˩ҁͼw\x87ǽІȹщњ˞ηʍѮœѬƔž',
                                                                            'ϷЈŪƓ˜Ѥ˼ʨЦŮĩɍе[>ƎÙǯö:ƟǴ³Йİƛ\x88ƝԕΎ',
                                                                            'ҾɌĦȜȞŶʱßĀĎʣąҩ\u0380϶ƕҢѵĿЭ%ţŉѾлƀυřǅ˫',
                                                                            'Љўgç˵ЋúΠɢˌΛʙƠ;ÍĻɧБHДŗéǷӡ˂ɲѮƾʜѽ',
                                                                            'ƻÒLбĦǽÀøʺҨˈ+ıďУ˪ρβǚƞĺɞĠτØ˝jкĵƠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9eȕʘƢʃɲҿçϼǘĉƍu\x89\x83њώĕ\u0380ʻґӹ\u03819ˎ+ǽʝӄÎ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1872039760984615837,
                                                                            7699495997725145350,
                                                                            7566986852344867012,
                                                                            -6935270412942166428,
                                                                            -6990216729720796610,
                                                                            -9151058127876356451,
                                                                            -4604623175798291581,
                                                                            -2186373953358929895,
                                                                            -377961198951805538,
                                                                            -5701111385287439681,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x94ɤԝʌėǊʂӺˇ˸ЂǬũŅÞϷЂԠ"\x84Ǿԅ\'ψő',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.982371:+0000',
                                                                            '20210209:152853.982414:+0000',
                                                                            '20210209:152853.982433:+0000',
                                                                            '20210209:152853.982449:+0000',
                                                                            '20210209:152853.982465:+0000',
                                                                            '20210209:152853.982482:+0000',
                                                                            '20210209:152853.982498:+0000',
                                                                            '20210209:152853.982515:+0000',
                                                                            '20210209:152853.982531:+0000',
                                                                            '20210209:152853.982548:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԈŧɒĢĻѓŰ͵ɪŞϳǱǛαƯʀбĈƩґɎҹǶ(¸ňϔw˔',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.983136:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȿ˙\\ŏӾƽȾɅԀÖαʽƈƅ΅ÁɠЦˑɼЇńѸɄԊ«ˑԑϡѶ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152853.983531:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'фͼïюёӥ˕ԌѣψџмɘΡϘҗǚж҉Ԣ®ƪtRӗˇºϥd˻',
                    'message': 'ĤŻ\x81ŁԌӾΔ˷ʜæņȥʯǥƣԄΉå΄шӓˌȘӇɚëǡ¹ӧģ',
                    'arguments': [
                            {
                                        'name': 'ľŕʼάůƵΤďњрáɒϘ\u03a2ϳЍ˂ŠđӝƝ\x99ƅˠωŖĉєӉ¶',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5419705728963382829,
                                                                            5371826780370011103,
                                                                            7140596212084596016,
                                                                            8416132384742413306,
                                                                            3269510968502497751,
                                                                            -2139464952327856373,
                                                                            1209941718371229403,
                                                                            -1305953776013993013,
                                                                            -7324136899024041607,
                                                                            2257067562020555916,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÊӮÃͽʅt˙*KĥɺǤԋΨH¾¥÷ѝԊШƷҌ]±/ĞŲξӈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ïǃǲƼòƞšΝŖʷЈgҢϋɘӡȁҴ7ЇѼȓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.985589:+0000',
                                                                            '20210209:152853.985628:+0000',
                                                                            '20210209:152853.985646:+0000',
                                                                            '20210209:152853.985662:+0000',
                                                                            '20210209:152853.985678:+0000',
                                                                            '20210209:152853.985695:+0000',
                                                                            '20210209:152853.985711:+0000',
                                                                            '20210209:152853.985727:+0000',
                                                                            '20210209:152853.985743:+0000',
                                                                            '20210209:152853.985760:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѷǿɤ.}ƛɅʻ\x8aοѻΨǫǪċϼүÝʅ¸ҟȻӆԆƺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6760666421179244589,
                                                                            8299140223771661151,
                                                                            -269560037554045196,
                                                                            1655407926103077245,
                                                                            -3638710778084335051,
                                                                            -8789810334042527584,
                                                                            1488607137315224139,
                                                                            6936725519206468911,
                                                                            -9044968598864395047,
                                                                            5880469867983971763,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'пȆŮѝȘԃȿӯʗƂŨҏϓǆϤӏĶưӱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152853.997964:+0000',
                                                                            '20210209:152853.998012:+0000',
                                                                            '20210209:152853.998034:+0000',
                                                                            '20210209:152853.998054:+0000',
                                                                            '20210209:152853.998073:+0000',
                                                                            '20210209:152853.998090:+0000',
                                                                            '20210209:152853.998105:+0000',
                                                                            '20210209:152853.998118:+0000',
                                                                            '20210209:152853.998131:+0000',
                                                                            '20210209:152853.998144:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱ\x88ˣǢì΄Ęԡ˕ˇ϶Ӝ\x9cӄΫǿΞǻЖƏЪӰѪҼԉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            740421.4917209818,
                                                                            925009.980218849,
                                                                            235220.6115338857,
                                                                            558277.7063198962,
                                                                            508244.06095012324,
                                                                            -47224.475474039515,
                                                                            355715.616721719,
                                                                            706003.2913834031,
                                                                            645365.8462272095,
                                                                            503298.71715818276,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʡʍȼԖҒBҧ¯ǴԋćϠǒҽĪοґЁ҇ȃ0ʊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2090065081598378520,
                                                                            3400455796144505290,
                                                                            -2535041775937991686,
                                                                            -900509941453620255,
                                                                            -7699760087483791805,
                                                                            1710436261771533541,
                                                                            2708750346214597363,
                                                                            4459195998357108476,
                                                                            1422161908568686934,
                                                                            -6352928870577975004,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҘŁ6ðӯɃ\x7fȘЫЏ\x87тԇҗ҅ĀǊӸ+˒ʀWķßΕуАȒԜ˄',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '[\x9eɓQФԅΒθ˃ЉэΞѹ·ƪ1ɯʯɨ2Ǔư>ȣѿdӉÅȢө',
                                                    },
                                    },
                            {
                                        'name': '˚Ӕ^©Ѫfí\x8eβɯπЮŀɢӵǾłä\u0381˟ϊƢÿˊҷ˝ăɿʜx',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152854.000075:+0000',
                                                    },
                                    },
                            {
                                        'name': 'áUIϺϮϝ\x84ƥʿϷƂԝӘμȈ˵ӬЌƟʳƹƄ±\x8fҖļӽϬƂҦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'áȸͻš5ƸąÌŠЉ˅ςÕÚ0уńəώӆǼѼ$ȴJġŠʜρл',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '1ĒϚ_ǹȉїſ˛ŧмΐ',
                    'message': 'ȑŲƶȖΦnƿǵ(ҖÛО ԅŮåƙԑҪũƌɏǡ²ȭ˚Ηǌȶ˸',
                    'arguments': [
                            {
                                        'name': 'µӆŔҚ˧ĘʣΫҙ˔wΌԧɣҺϖÇӱѝ`ѿÄ·²!ɐɧδȪȋ',
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
                                        'name': 'Ƅ\x88ϥǙȲé\u0381ǽŭϮāρřƿǩЗȭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 't˭ѦҲ-sį»ʣ9ŚʁɌξS\x8cυ\x96Ȅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152854.002507:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ѝ ğ҂ƛǞѕĻǩΐ\x9aфʰɈьƆӺӈŜά&ҵІ˖ÌȺϼИ%Ǝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 934307.7303332998,
                                                    },
                                    },
                            {
                                        'name': 'шĵȈʴéҭŢ¿eɓӰ*·-ıȲěŢɍѬĲǏԥɕ§ϛĀ˶Ìύ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4954959363457531585,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƾϛВм\x9cϤ\xadĳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152854.013768:+0000',
                                                                            '20210209:152854.013809:+0000',
                                                                            '20210209:152854.013824:+0000',
                                                                            '20210209:152854.013837:+0000',
                                                                            '20210209:152854.013850:+0000',
                                                                            '20210209:152854.013863:+0000',
                                                                            '20210209:152854.013876:+0000',
                                                                            '20210209:152854.013889:+0000',
                                                                            '20210209:152854.013902:+0000',
                                                                            '20210209:152854.013915:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͷʄ\xa0ǓѪ\u0382ȳ\x8cТǹ˝ϗϊ£æ˭ũɑŤUӛ҄Јź˫ƴ\u038dДäȣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 931420.3589206272,
                                                    },
                                    },
                            {
                                        'name': 'ȄГêĮåν',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʮģЧë³ˏǲЊΡɌ˚îѴFĵƱџΕ˖ʔçҳD\x81\u038dĜΟÐԥˮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 533887.5131741853,
                                                    },
                                    },
                            {
                                        'name': '¦ʧɓWї#ψԛςĄƛɭƃαǣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -363054244733636996,
                                                                            -2646210467829548938,
                                                                            4068442984568307851,
                                                                            2432065504529566212,
                                                                            -5045687809873227741,
                                                                            -6220565020771268736,
                                                                            5098955456767407394,
                                                                            4093321336536838666,
                                                                            -580090768541538390,
                                                                            -5256065508737590646,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѣbӳÙʸΒ*|Ì¬\x97ҁɨǊ\u0383ҝÁԪƛʘǹѳǒФŔґ¾Ƞơȳ',
                    'message': 'ʫˇϗáĉһĕ҄\x97Ҙ¢˦ϻӑӹ˃ԚɧʝŲɩėǥǣŶӠѝӤˀǹ',
                    'arguments': [
                            {
                                        'name': 'ƢԬΩԧŽŇǂŤǽŗώĨŹЉҜѓȊњђʲí҃śӷ˝ԨҨıȷŷ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152854.016848:+0000',
                                                                            '20210209:152854.016890:+0000',
                                                                            '20210209:152854.016907:+0000',
                                                                            '20210209:152854.016922:+0000',
                                                                            '20210209:152854.016936:+0000',
                                                                            '20210209:152854.016949:+0000',
                                                                            '20210209:152854.016963:+0000',
                                                                            '20210209:152854.016977:+0000',
                                                                            '20210209:152854.016991:+0000',
                                                                            '20210209:152854.017004:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'wǊңƽLƹȩɝ˴αϥӋʊǲЛӜҴяœ˓ʐԔɃƃЩɖǁ˘ġʊ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ȼӻΣơȧҝӱч',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѶβǕĈUȹĮЗ»^΄ŖȎ\x9cȤұиǿ%ìɵѴΣǵӻˎŉԝĬŭ',
                                                    },
                                    },
                            {
                                        'name': 'ʞƿǉ˓Ѫ,ӊԥ\x9f`˸Цҹ"˚Ͻāį>ʘϤ\xadзθǽǲԑiΜҴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:152854.018382:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ļ[Ĵԩѳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            344581.3846778097,
                                                                            23036.52109815413,
                                                                            944054.885014691,
                                                                            859456.050754121,
                                                                            716187.2953974581,
                                                                            274280.48278055846,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x92ȉËƁQǅξ˻ҥӁʃѤѸ\x7fē\x8fɭωĘϝƢҤоРqўšϠŻϟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʘơǆŖа\x8fčԧʂøiˋҕҶѹԝĦōҹћ\x80¯ƧƮ˥ФѸäŽŁ',
                                                    },
                                    },
                            {
                                        'name': 'ԬЅ҂ӡɇʝϨҶΊʪcǮҰȡϟʊͽėϢҮԄЋôǱyʵ×ˍ\x89ѡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '§;ˎªˉȍǿϕ˳ȯ˸¤Ѳļʬ¯҃ńñҜөʎ?ĞЉƉ˻ȦĖ˞',
                                                    },
                                    },
                            {
                                        'name': 'ǂҶϤɭ\x92ө҆ӦÀ˸ǴӇʈûʶ1łóΑ\u0381ɺʬӣ?ŉӿ\x8dЉˣÿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:152854.030468:+0000',
                                                                            '20210209:152854.030510:+0000',
                                                                            '20210209:152854.030527:+0000',
                                                                            '20210209:152854.030541:+0000',
                                                                            '20210209:152854.030556:+0000',
                                                                            '20210209:152854.030569:+0000',
                                                                            '20210209:152854.030582:+0000',
                                                                            '20210209:152854.030595:+0000',
                                                                            '20210209:152854.030608:+0000',
                                                                            '20210209:152854.030627:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǹ³ĥӬÆáȆ\xa0$ԟΗϘȯƷԧѷˮ>Χѩ҈ȭɈВĨ%\x935ЧǓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ČҖҷõĎțԈȐǫѬɊȶόϤέˑ˕ˡ΄ǟÁĺÿũéӐɒƤĩ˝',
                                                                            'И%ĦΌäɂҥΪşҵǦĢƅƽçжьȂ;ϔʻȟAȹnȗѷĐ|ʤ',
                                                                            'ȏv³ԛȤѦǹȺҜƠѲˡΠǇɞŹшɑ˰ ɑɁȌ\u0381íìȧȻԑϰ',
                                                                            'ɲʈ4ʣ«ӱǵҨϕɢқɑŦ¾ЈҋdφԅУϋԏӋСɑƵƜɝƚҷ',
                                                                            'ÓĪуŴȉɗǅȜĚšý\u03a2хЍҜąΈȣγӲύΓ÷ΥǮÊoĪ[ƴ',
                                                                            'ԤŷǡÄÓÝϺњҾϾ˚ģʝȔŞǯɜϿџȾӞѾϺɄжԠʸξЊö',
                                                                            'Ɖ£Ӿ͵ͲåÃԤкŮŏ¯ŸϘήӏґʹόɚďßĔďżĝěʒɏқ',
                                                                            "ѯǌ'Є/.ʥΧаȮȑ[ʵ˅ƼԖҧȟѶʧǒϫУ°ӡʾԆ;ѴК",
                                                                            'ƤņΒĠэϒéѥҒҨȑʀϞѲЂĢƝФŃŴ\xa0˄æɳŸ¶çǪ\u0379ʭ',
                                                                            'ΜϸʲȼЕºƀȺðăΑƚҫď\x92ŮЛí˫ћQšƬԆ\x85ϴδяʷĨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĒzCƈžԕǚŪǚӹ\x9fӴƳ˴ǘłΊϳз˟ІθΤɊψѱԝÇǈї',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9163319964823019321,
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

            'identifier': 'тЁIƌǗ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'Ԓ˭',
                    'message': 'ȑ',
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
                'identifier': 'ǅˏŵʌѧŽHŰ\x83҈)}Њϼû\x95×о˳ҹԒԮê½ąϠп\x8eЗЀ',
                'categories': [
                    'invalid-user-action',
                    'configuration',
                    'file',
                    'invalid-user-action',
                    'invalid-user-action',
                    'os',
                    'invalid-user-action',
                    'internal',
                    'internal',
                    'internal',
                ],
                'source': 'ȷԡlȐʵǲłčʳѠϛäϴӀӌԀБЛǥǧθɮǈ7ÿǿÔOӪʤ',
                'messages': [
                    {
                            'catalog': 'ʟɇϋѓ˔ψÌɂžȉØȑŖƛ¯δӪÝƘQӉȶӧΓĭҒǸ²ҹԉ',
                            'message': 'ѵӮ˸ŝČkȧʋ©ȇ˒ΦγӗåΟɬӃԃÖȱѤύŰϗСԞͽ˥˩',
                            'arguments': [
                                        {
                                                        'name': 'ĤљΓĉŁіƽϒϱˋσp҉ÉϾȩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'м\x84ЉLìԊΰĤń\x95ϤΚ»Ͻћ·ƴϝ2UҀ.ʯͺΟǣʻ˂Ўԃ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˀ1ÿŹҺ\x7fқ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152853.901833:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƪ˛ō͵ыǌƾԧɽǡYʌȟX7č϶áǶüԪӎӐԓ¶оϵП÷Ĥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '~ӷǑͺӫӚ˶8ёӒŻĲŚϢˋԣ\x8a˲ӆǛRТù',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԘΑ˙ğŊҳɾ˫W\u03a2ΑPɦˣ;ǴˁОØ^æÉ¦ƕΏȟѥϸǂʆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʼϫȄį\x9dɵӦӦѝýЬʝӸʦ/ċƿŉ9ŁæʼȓѦЪԧә¯ʉɤ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎǣD\u038bȘýРьɾʐϳȥыÞҙҙӉ˻ЀГ_ӸVƜv˼ȢCӾƧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8fʝВ²ΝҍΊĀԮ"ˎ\x80ȌˍЅɧΊϘϔƀ\x9eΓыѝЌȀηӞΔ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8bӂϦҗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152853.902891:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɪϛйϵȖ˪ǹƴ҈҅êƫŹÑSԏҞϸԍЧƇѪŲɟƨ\u0380ùДҫǚ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔъŵ\x84',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5541759280325058024,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'pƏ˒ħǯκZċ¢ɹˍұʹΆҤ҂ЋΑÍƱΛтʵǃːϟİʇ9ѻ',
                            'message': '4ęǷȶƠƬӶ+ҕũїКƏ¶ŵƏΨӎҋǁΘǣѱӀ¼ʊșԆѶǹ',
                            'arguments': [
                                        {
                                                        'name': 'ʋӳǵ*ƥҧ˻ǖƢиƤɟӲ<Ǒɥεѳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -592966443675820599,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǞƼ½ӢӆʼÐ\x80ʼǇʃŗƤʘǏśȗʼНѣφѣԥ¥ԙөҩÍʊ˕',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '·\x8aˀεèǑЮˑ²£ʌԈɩЬȴҽǛҢлɏl˟Ϊɪ\x8fÀҒķǢ\xad',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80њǧTʅ˄ΰӏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 240304.19312868686,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x87n\x88Ґ;ѱǎÌƄ\x94ҹϨƨːӏЦͺȿȖĚƓȥ\x8dƜ§ŚȉʆƉʉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀъųɊċҾÒͳԀ=ƎΡȘӀŧģNɈǇƹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȃό',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҒċƯÿһÈħ/Њȗ˲ŕЖɪȐWƷâ˜Kмȃ\x9fTӿЧɖèЊ*',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ċћνɾȓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 203229.32292527432,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅŁчԢӯɝЏŠǺȃʥҮƏȶɔŽΟʬʴƒӡʭɀʢΪ,ԅНӌҵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɢʦͶȹϢ.ɻơҽ\x96\x93˫ɄʗԫˣЗʃ\x8f÷Ą¼Œ«ȿʦˆɊÏғ',
                            'message': ')Ñхӧѷ\x85лȑ\u0383ҸѱηԕźϊΨɻWĒ\x82ŠҡηȝƕΒЛƠӇɉ',
                            'arguments': [
                                        {
                                                        'name': 'Ҏ¸ʈâ\\ÅϚӺͻԉ=Ɛ¥ʗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9a\x85ӝΚˠέάϽɼLƜÿҳ҉ѧ˟ґȵԆтҵЈǩȍǸƭӌǸѧ;',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 275321.8889273806,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷƇΠȳͰOǕεMͼȍĐɜҽѕԩâəˡŞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'EʟψҬȯÌÐ2ДȁŰÕűǎԉāǱͻӥ\u0382γЭϛєӔϹʲȯQҕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7503010757270377542,
                                                                        },
                                                    },
                                        {
                                                        'name': "l'ҳғÄƉʔ¿ÆĮȧ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x80ĐǺʉǧģɸ¦˞Ѭʯ~ԅÆϋƂșӾ&ҨЪύУλ²ϻȈьȰȴ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊƤɰУǡ˾ҨȊǵĭď',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻΏӘŨͻŔԏȩ˗ԝҏҢǎ˘ǏkȣωӱӼҎƮѰˮXŢüѻЄ҃',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152853.906242:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣρŮÀǪÊӱǘϤцβҁ҈Ͼңϟуʞʐɒªǣî\x95ȚƥӽġKǝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÏJӺ\x92ǠҀ\x94ѬԑІ˧ȯ7ʄСЎǚѹž\x80ɜΗǻ˼ȯęәǸ6р',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҧ҂ѐȗԝϞƿʂɾȣѠѾЀӎǫ°\x86OѳĹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϏԭȀϣ\x92\x8bʜƤƘRӧɦǎԈӳƓ˱íҐƐͲÄɗȁŐɖǾƕĞИ',
                            'message': '¾ˢҕϢǾ\x80ӖγϯǄέŲўϲƒʓǰԍԊȉΊҹԉԥ°¬ŀƮÉȁ',
                            'arguments': [
                                        {
                                                        'name': 'Μ0śǫȩИτѐ˶îώԉΜĥϵΑѩɞӋtνÛγҹʋї˾õʕů',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 954163.5742788773,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıӂȁʊV҉҈ΣНϺ҂ԉӐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϙ2<ƿsԖǷ¨Ê¶ΫůĜˈНÖѵԒеήԫƙıdÙ×ҡēĒц',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӠʡЛîρƲǪĂ˫±ʗӗѸ\x96шǓɄЎɾϽӲ\u03a2ǼʒŵǚƧöqӬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϒϺĥҾǛª\x96ȫʊ^ɽ˻ӻǡӓʓǋʐ\x97ýȊǊѣѴԦʥβƦʖc',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8692490084613719377,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÍϮӾ[ĥǯҿA',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3629943126078696491,
                                                                        },
                                                    },
                                        {
                                                        'name': 'дƻүț˓ҎԖ\x9fΊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӛ҃|ԣ¶˦ɈϴҪѺƮ¿<ʨȞƆǽτê˅ϮʀϚʑÿƵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǞƒțԇҤФŨҊϏȀɆÕĒưЯʈƼɤԀӰɅʆφЬǈʺХɧһĜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˱ŴӶ˖ƣ\u038bШͺѦʹЯǧҜ˵',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΣBɟ]í·RԧуѭӚԛЅƣ`Лӿĺ ȗʱWʏҮĿ\x8f˥Ӡ˯ә',
                            'message': 'ŗʇӣǭˬʶηϢ˰ɀȸԇ¹Ӌк¿ҝƫЂǘѯϜɦʔȹ¶Ϫ\x82ȦЅ',
                            'arguments': [
                                        {
                                                        'name': 'ԡɆŷ"űŽԡˉ¦Μʠ}ɪє˧ӗζ\'ҠбĪʜș¬ԌԢӺϙǻɑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋʟˊѬϷԛˈ/ĂǖOƮҤʈX>ʒȡƤѽǣɫżÔ\x9fΡҲʜӣӐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӡʾίǍӖҚơʢқġ+·ß\u0383ϊ}đā¸Ӌӱǡɰ҉˹ȹȿԉЌÂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 882615.8154353877,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋ˨ΎǣƳ;ǸˤĤ\x9aσȞΈδόǍǾʗQəҝtҴήˢƦŪ¥gȷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҴҒФʆāȲĆѣ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152853.909757:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'љɟʞ˵ΡΝӕďćˑНȧ΅ȰӮń˷æźƃѼřƢҴύХɅˏŻҡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'lȗɬ£ʺшʝЮϖӀŗyѿŰͿΉǡɰԋҳʆιθЇʟΪ\x85ƳѢȗ',
                            'message': 'ɤįҝưŕÎΠưƞЬ˪sњϛɸөе÷ ɘˉňʹԢVʹϭɺȤс',
                            'arguments': [
                                        {
                                                        'name': 'ǋСҰYһȒŔũɤΌ/ʾӴɿŗMзѺɷĆ(ћʨНԎđάȽѲГ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȝ\x97цƖїǅϫҁƼΕĴȏȨŲ˙aӕĪΫϤѰʦĠΫхǰΜĀМ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 597704.4749581872,
                                                                        },
                                                    },
                                        {
                                                        'name': "ʯj©яĥƥ˓ƅ\x80ʡ_'вӬˀ҃ŵΗˍ\x97ʩȯ˨ѪœI\xa0҂ћи",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'įŹ\x82ĵǘÊѫfϼʾƚ,Ɓàüƅʹ˔ѥąö˝ĽСzʼ҄',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʃҨϋuĹѷɮĨǚȝǪκʫϹţЌȧŇˀфʣÔȠϣӪϓИЕιɖ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ":şķӫȬТʞßӌŤ˗Ÿҗµғö³δƒɵϕϓщɛ'Ѥ\x84ýǶĳ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152853.911113:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʯƮŷЩðӏϕʣғaǕƖAȠôưĠʔ[ğTȧŊ@ҋPʮĦȵӭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӭɀKѨĻξȈӖЊË˚ŌÑ(ϖύħńϧʵ˪ϲˬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔƇƋĿԇӍƁžŬ^ǲ˯ЏȯŵѵяǠԦŖԘŶɧ˺Σҁųkǧˠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÚǒžԨȩƶ\x93šˣń`·ЍĨțÒ˜ǉӀƴ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 310558.8661510641,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ˍʎοҗŗA'ώώƩęȬfҼűɯ˒ϐ˘Шͻ˨Ѣͱ¶ǈŴPȷ\xad",
                            'message': 'ӷƮôʣюǻĝȑϟcʤ;ԝƵʭ²ζʈ˨\xadλњωƇȢӚԐǒϝм',
                            'arguments': [
                                        {
                                                        'name': 'ԪoZûν˾ŠřĕΓÂĤШѦЭ϶ŭƌіКΒCƑʊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѨÛϻϻɏʕ\u0380ЍȏǏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǏԞѹ\x99aԥƑɄɤ¯zƶǢΐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŴҕЙ§ƺԧúřϪVƝϒŦ²ǅӱ\u038bñ˄ɩ\x99ȫȶθ^рϔʒҷӓ',
                                                                        },
                                                    },
                                        {
                                                        'name': '±',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '%ǉѫ\x98"ԪǅӜ˻ЏȾ˵ο˹ӹǣɧӉϹ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Øȼԏ tɠȜlԗҨГ\u0382ȩĪȞ\x93ϥԑˇĘƋԧĸ͵ԞəͻӦAJ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŹʰSƧлʠȏӣ˛ǐǈчĘƞѦΓóӝvϩȒщӇĴķĄӠǜϝγ',
                                                                        },
                                                    },
                                        {
                                                        'name': '҆ȓбщκɔҦ½ǼƖ=ӌÝN.Æ°P^юεԩҵŝѪӥЃʯɼ\x7f',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -402553988750469228,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝˎǏĪϗʯĝʟˠϻǢѫʝԥϮɀɋ϶\u038dԨŻιąȈɯ˴ʵŢȣЅ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǣŊƪƧȡвԎ˗\u038bϑӣƲΆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍѓſ{ǎѼ҅ҎχȮÉѾўƻ3ʇФЗҾƟćчЅЪүӥʃŞūĸ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϏԨƖǢƇχRúȞʯš',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ќϚς6ԀVѮȠͺTԤʬʢԀnȍƪƉăќŘέǦɦЇʢǽӆҀη',
                            'message': 'ůМʦŢӈűɊκƧʏ˚ΠЅʈºпǋķʇҎ˂¬Ɍîə\x9eɓĽΆ\x9d',
                            'arguments': [
                                        {
                                                        'name': 'Ұr:\\ɃҌń¹ƆҐǛ7ӀˀΟȮǓԦӒʼƉ˅рк&\x84îӘюσ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 574527.2700568486,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȱ´ȽϒґҟɐԒƂĽŹм`ȣӾӚȱĻȆӸ>5ύɹÖӔǑǫĥǑ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӣʌ\x89ɄѰѐ\x8eȺȩғɢԠɰĆŞĭʭѓƂ˼ɴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '2șüϩơķŰŬʱ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØŵŶ˅гΖƿȑĕ;ȿțŢȘÂΉӧӪє',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152853.914773:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0378ԢŚ,ý\x9bѩŗ\x83ɯҔɨʪˠӥɑϼß:ύˀˠϞǗʤmӆϽȶ\x8b',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'öӈȶΗиԎʛϊҧǚʐȄӳǲԔϿUВ\x91лӉӈ˥7ɰʠźӕόӠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0380³ү£WȹȖϘεКԐYȭӋΏʻͽì',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҭèШɟñȟǨʐǌįƒԉǜǆ$гƎԛˎθљĎΠԪ\x8aǈĉϗˤɮ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152853.916465:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȧԒϹÓ\x9fńäǐԉћÖћŃóIҪ^¶åŻÎШҒǶŹώѺϝ˹Ӕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 279679.1974092282,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΕϦȮ˼ĊƹΉŇЯзɱ˾ʭȰýǳāĞ\x84ƞũƲƑɐʪɻȷƯʜî',
                            'message': '¦ѠѸ&ƟǧӘŷãɻԄӊɲƨē\x9cÊOӵƓȓĈ©ѝ»\x90ƳÀ5Ͽ',
                            'arguments': [
                                        {
                                                        'name': 'ćёѰĜWƼʣϝ\x93єӼôƅӤϛϮБϘ\u0383ɽʈŞԅӡƞϠəʈʰø',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӆȣ.Ϡóǉӗɐȋ\x86ŝ\x88ˆĐȊ˻ʸ,Ҋɭԍź\x8fӋǇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȢéԁЏҒвѽɇɰϬј҂ԧ҆ƴ¹үϱΝƚ{ϜњЧĶƶ°Ӯԉȓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'õҤҊɧ×ȕƝ:˻%έɱ`Ȯ]ЀȉǠȵоàĵӜӽĵʂ˧ȿƙƘ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u03a2ӏɨ˳ȽԂċԠηȘһӦ%ңǿҷёņźԥӪƜ>Гҙßԅ]ӈд',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¹Ɗ˵ÿҧˬȼӲɻ´ÈӵӎԒʉÝΨˠɔŹƱЕƽЇ˫ɆgŴΣы',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˯Ӎ\x82¥ёLˉȥWӍȕʺX҆ϟψӮǙǥ)ʱЪˌńŷʦѶҷÁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃҼzƪǐſƹʭǃʧ˩ϔӮƓҡƪѻ¡ʴžÓĶҙñʉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦҢǓӊÆƀ˵\x87Ȩԝӡ%Ѩ҉ƮӅбϽǚeϟƢɈËȴΈӼɆҶџ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 215818.97497104557,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͲȵɓɛΈρ_ƻʠ×Ĵу҂ŎӰщҺɜθτϸïʈȞʮϕѫ?Ī',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '^ɲӖОŒǯǆȹНҽȚέÏÎϮŒЧѮÛһȺӧƑŒƒП',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŶʺӳŋɁѸѨɎίƉŶĦϱӨͲΰcń˱ʡѲ=¹ȓL ˂dyh',
                            'message': 'ƏǕŖФƻǜÜƆϗԍƬ˃ķΠ:jϊ˔ˌ³ƑǊͱӐҷԞԀʂƥ`',
                            'arguments': [
                                        {
                                                        'name': "ʴ\x81ѭÍƲԗǎБҥƏ'\x7fŞĥɂҜyʺ҃ѦфӳҰ˅ȻѦΡӆҿϡ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЗԫǿƔĻʮʞǫǕԩLčҗ\x8bʞѣǡ©ˀϓОŤѭɼɰԔ>Bԡь',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԟȸӺŢȦʃ˝ӬȌi×ɬˊԙԑѱƨŵ\x80ÄϬͼφ¨ӞДό×3ˊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
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
                'identifier': 'əĪůĘϛ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'Üž',
                            'message': 'Ф',
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
                'identifier': 'ĻϒӤϫ)ѤҞʾƳàμѧÇŅԂʿϯЋ<оDҭ¥ɮыˊʼÀҨȮ',
                'categories': [
                    'configuration',
                    'access-restriction',
                ],
                'source': '˾LϋƤʥkНȕϊ7ʊɯҎʤӺɣδŝҕԬĨșǏüOęƤІɕӥ',
                'messages': [
                    {
                            'catalog': 'хӤԬӕɧԀ',
                            'message': 'ϱĝ*ѲҢŊԪǏņê3ǴĥƼ¾ʸ˽j\x9eŶīѨӍԖǡӧԄIԉƽ',
                            'arguments': [
                                        {
                                                        'name': 'ԉϛɳϲǉɝ»ǁǐ˗σΆьʑχ:˹ǘɍΞɘȨˤӾͱП\u03a2ƝҝӬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'U×ҼҫφɖĄǮǄ>=2ƐȤµʺ˅шęҳωҠêòŗѐӳҙΓћ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'õɛҾ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÆѼңɁOĪʮǥƊʙуѪƧϑΎҪҥЂԉǞˣӅǂŧзЬӕл˶',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.047069:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '?ɢϬѮ˱ŎǛҤȣðϐǟÙfϬŏģҥϒǽѶϧƐīɳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˙рνѣԣӣΕқϬ˃\u0379Èѧ\x7f¥уȺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋǋб˼ʾ˙Ҭ¸ɥӦ¸Ҕӊ/Ӿa¦ƬǒԃГWɿϿŇɠŎǂҫʤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˤҦȩѯӘԮǧɈ¡ǨҝӴɯɇȾѷśԂʥѳȂÂґ\x80Ʊ®ʣȯԔϔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'к҃ĊǶ\u0380˹',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԛ˘Å˅Ιˇҥ˖ĂÝȇŗɾŒǴaɼ\x96ѵ¦;ƔрӸƥ\x93Љœјɓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'őɓƃ«w¢Ĳ\\\x90ˈŧ³ŗюқı·ϾʜǉäЗȨԪϒþйӜϯŝ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÕԭŗȫÝэʉĝƷҢmʓɋϪԊʥēӼ͵ʄź©ϢшʒʂԄϥ˛ǋ',
                            'message': 'ԍ5ɤͼćRҰ΅˴ƚ\x9aȮУ ɀ϶Ĩ¶ѣǁǔŻҼπǧҳƧ\xa0϶!',
                            'arguments': [
                                        {
                                                        'name': 'ˋċȨНđŞÈÿҶˡΒԮр$ɏӀĿòЀĆЌY[Ϸ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΡԪƀĔ˜ӌʜІҾŲȘÜҷĵǕЙŨƄʞGý˫βӱȷȧҚŝÿƤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 265380.01619330875,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȁ\x86ғǂƖӒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 525907.5373358115,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҕόřĺÎ&İ\x8eҙ˭Ԥ\x9dĘԦԤǝã',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ºʤˋɸɳĔλʔúαϐƕɔäΛǎkƈ˕\x7fƨɜůŋĭˆóӪѢэ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘƭ÷ʓΜҰΊϊŸԛƖҋ˞ŜǋǗЬӃɉǱ\u0378',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 418995.0888451444,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9a\x99ͷɘϷŤЎºγѫʕЌȒNӂøб²Ƹԉ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 547593.2531879314,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĘʫǀN:,яƋІҥɎӾƦ\x96ЦůԎ¿˹҉ʎĵ\x98ʯϕ\x99҃Ƥϋі',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϛȊʇ×ѓȭƕşԫ\x88@Бʸȕԃ"҉ǺµӹƢԏ¨ϡ\x93ɏłʉńѾ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭпҫɸƈ§ҘɹȟԀȡT',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382ufǄ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'đƩȹvҔͺȔʑКŗēĳłʫԅǻüƴӂǐƶќǨ˴ƏοΤԓҏБ',
                            'message': 'ˋψʰԖ3ƀҚҊѶˁȊӎƍѢnɣMѫɓƲȐFɘŝԢƬŞƷѺҘ',
                            'arguments': [
                                        {
                                                        'name': ',ĔɕȃҴѬơɝѹԩӐǣʺlФѴ˄φԡϯҬǈuʟĥ\x89ѕɼͱʕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћ˓ʲ^ÇY҄*ɃǢɤԞɯԫΐƔѐ\u0379ǚRмȡșӉÅȤņƓŔH',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.065595:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˲å\x9aϱÒҔÁùǟҬ!Ԫ°ѿɲϒ¨\x9aîĘËϸПÁҽǳϣүſˇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӏłʁưĳԁǋʅȂɉӋҿˡïȳRϚñǈ\x83ҖɳȣŌнƙѽ3ҡͽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԗɌԤӶɽŲ҈',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸÏΧǴѰӢΆГɵ÷ƖʵѰҮ\u03a2κġ\x92ʹył\x88Бѥԥ˧ЫԝŌʹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˟ˇϒԔɁȆґɌԦÄͶĴÌϤˠǁ°ȽiӦOǼЛӡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɕï˖ԮƴǸ^ϡɝϺΦŤ˰ʄԛүӤÚрԧ\x9acǹ˙ʈӍώˉ\x8d¼',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃWνÃϢŐγ҈ņԛѰˇΓ\x84Έԭǌȃþн\x93ѡjӒΡe˃\x9dԌӈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'āʹѻҒϝŜʆ§řʚӗӣŌϝрϠ$Б\u0381ÙȗΛōӐưw˳ȨіΣ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.078827:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҘԕȣʡЛĔůÞɒˡҧǟґűĹѾΖɛҐɄЖťɀͼҳɴӢ\u0383ωť',
                            'message': 'ƈŲХŊȭȡæВȑɜԀƬʁͶҥԏF\x8fŀӁÃɫЯӽNȕώѤĠȓ',
                            'arguments': [
                                        {
                                                        'name': ',ǌϏTЬ˧бĕӷѨБϔǾʼǎǷΝƯˌaɣѭÈɚĵŽ8Ι\x99ˤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'фmʓƧ4ˆɟĲԏS҇ǇɺγшԨҬǩӹ9ɂͻó7ԁ|ʹϾŭx',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¼ӿɳ\x8fҵ¨6ќɨѦˣΝ¢ŐΊӌʚȊӂ\x9fԀώƥҎΜҡӨ6',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'łӭɉ\u0381чЍÚЮ\x80˺$˲лƿj҆˖×¹ɧԚîǳnъҥхÐĺʜ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŝϠ˔ęŌɋпɌѸʽŊčԮÊ¾˭òŗ˝µĦʡԡɴЮΠЌˌÓʩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ͽӢæҶƚÊȪέҾρRΒͶĨʕˣ°Ҭʶï'Ã¤ƐƢ¬ʅʠӏѤ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԫÃђųȁSīʁĤҦŞǦɡ˚҇ϸӧҘѥpɵӪԧřEПÚ\x8fȠΝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2611585568401729262,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍԒƓǭɑӟЩɻѽʺ˓',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƟʮʧјԤɷϒƚЮȘʳӨŵjƿə˱;˘Ҿœ.ЫɕʿԢЀȄͽҬ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀùʿŪ÷ʧԜƵɈźȶԛŝǠ\x89ӬȡĽ˙ҟͿ1ĺĿЮȤϮÿӥΎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.082750:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˹ŒĉϜҥ˟ЃǻǇĸ\x8bϴμòȹƘ:ɃхͻǠԥϨ¿μʝ|ѥƌϳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '&êtƞÜj\x9dûѡҹҊΆ~¨ȑҥ϶ɽ`Γ\x9cžϣQa\x8fȬżƙϾ',
                            'message': 'Ԉσľ4Ԫ˪\x91üԁȓĴ«ƻ\x90ҩƗϣǭ)ΥћǿΙÓ˱ϞӾđϮΡ',
                            'arguments': [
                                        {
                                                        'name': 'Ґ˯Ɯǈ˫ƕӞɰҼлə',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -74707.8427738391,
                                                                        },
                                                    },
                                        {
                                                        'name': '·ƻϝÖ4ȂɹˡϬњ$¯ʠӱ\x80ĭϰÚΘӫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'dξɶĳϭņʆõψƣ4ŻΗд\x85ҖɁѭǽΙѓЭɪb3\x89',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÑъҡϙҦ˕҃Ɗ`őZ~ԍ¨ӳΐŶhˋʝϨŕǋЯɥȄȵɎɂÈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -28994.794096217098,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůėƄԠLϴҩԁȜпҞ©ŀӞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԃ:3ф˅łŪҮҤ¡ӝˑφЙУTɀVΘԕӞN˟ʺʸ˳ϪʃԓҖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђʪ˜c',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 's{ӇҗàǝѤӴǲŝŪƔƔ\x9fџʢіΜЈҩͷʾѸϝϵљŷˇԖӛ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʌīʴɟ˅Ԑѓӏӿǔđǧ7ʐԅKˣƱѿѭƹċҘò¤˭ЅäǮǢ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.096701:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŝɫ\u0383Ԋŋʐрʅ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 362258.1208096171,
                                                                        },
                                                    },
                                        {
                                                        'name': 'œЀ¬ĳЉђҋʿƘΊɶǺtў&ҫĜkĉˠӳǑhʣğ»҆Ğψ¯',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1010948356056687254,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÖоŶœӸɥӷŐèóȇƼӳϨųēӫʐѳľƽğѶԨțԗFрǲ"',
                            'message': 'Ԍ҆ʉӽˊǧϯȧÂőϙΏԞԀȻǰČ\u038dȅȂƈˤśůƆ҄ҚѨ΄ŋ',
                            'arguments': [
                                        {
                                                        'name': 'ϖ0ϲƀUĊʙ)ɒçǥƨk˖ȯԋ˾Ϫ¿ǙʥРʼӜȶ¼ԇXѦϫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ɜЊȡŌȕҳԬҸȞ˸ӢȢÈɆȵõбЧƩ'ĔČСɩƸ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Îѥƶ\u0382ȮРƦɅȵȽΝɵÁ\x9bǮ\x89ϓʩ˗Үȭɠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÝТȞʇӨĥ҆ϝЭĬÜƎҰӊǵѓ´ӻжűʫZƮğʈʔϘàˏ\x98',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԍ#ΫˢөиŬĄŖƱƔLϜҸĿҰΪľņǰΊʉҩԐЙͻðʪĹƁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЎŃʎƣƀћјdѫŗɓɍÀkԈxfҸӈ͵ŵǯ¶иż4ʱàŪЫ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'WȴϛˤǄ²˧ЃŔӼĖԛжȤºǍʇ\x99eʖƟ˅С\\φҲ˫ԫ\u0382Ӈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʌϏƵʔӯqԌΠÒĄùê˙7ѴĪ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѲўʇʝʕɿK҂ϑďʋ\x9c',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.110817:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '&ҟń¹҅<ѿ1ǠʸЉȦ\x8dˍ³Ӥ×ɉŘȂҼƨƦºΪɡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀȤ\x95Ȱ˫9ǖ×ԈƒϖʰσWӹǧ×һ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'įǕѲoеυϥǀ',
                            'message': 'ΣăĈ¿ȦċԣȫŲ\xa0őʴԞʳңԅĀ˜\x93ίӌй`˞ӖʧÆɑͶĕ',
                            'arguments': [
                                        {
                                                        'name': 'é¥°ԓɨ҉ҲɀĺΞДЏśºƮĠĬ6%ƈѮ˭K˳ĬήĝǑʔç',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 69351.56219588692,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ρ=ʞ\x87ӯjǉɈћhɁ˩ƕǕɥѫř¤ȑzǥȵƪ\x9cϽѤƜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'OЪƶʀϐИäӴɁѠĔ˺ǫ(¤Ņ%ʩơԙ2ϮȲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ц\x90%_ŀ\x84ʜ5\x85ЎРǉҷ·уȠɸϬЧ˘кЁƍ°ìԙ\u038bӤǹʕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϭȧċƬƚҤʄӼͲЈƶʌ\x85Δž˾˳',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.113421:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʉSƛńќ\x96ЄДҠɣԆȮ˾ϥˬ6\x9fɄаȡӄCǔϖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛŶНԬєƕλɍȭΪÇʇҸҨҜ\x88іśɔЃDнЕЦūʉ·ҏѭˍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.114134:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͼпϦѬɲғòʙYxτȚRѣ\x81\x962҈8¯ЅŨϋžΎΓɛ;ӈė',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 827644.3290652052,
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ˤěωʌŠǁɋ˃ЁƩҊѱϛҷƿТӲɌÞ˽ɵƫÚˠѲөЀÓǘ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ͽżõȷɂ϶оΊŧʺĐŰʚʏѦΑŹƌʬңԒө˯XѣË҇ӠѸ£',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĒЀԦ˹ΝԊ,ίȄѨûЁƀϮżљɱҼʣлšϛŭΗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.125969:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˢŲȬӦíȣˎɹħ˞ӓеǂЈ҇КЀǡʅӭЫбʟΞѠƕӟ@Ѳy',
                            'message': 'ԂϒȠѾôҭƾßӿe˞\x84´ӀБÚ:ʢĳċÃāЪǎʹ˭˔ҹeΪ',
                            'arguments': [
                                        {
                                                        'name': 'ºêƘ˓ԈǙ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀɭȒҿɂĤԀҊ\x8aäȃPÄŹϚјȕōȒȗʋ*ɕɥ˱ķÌϚԪӈ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.127283:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '¢ҾЗʄӿ˻ԩơԁƨ·ĝӛǃѦ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӤЌѰ¸ƞӬɝCӨňĔʳɞѡҬǅƘŒˤζ\x9cϞҁʦŏɍ ϩǊѧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¬ɗҊÂ=яÅ\x93ʖˮʀͽҪԟÕ˹ϏþKЯҎʽēԈŶΑƆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɓ҆ͷѝӁ\x97\x9fҬĝåǁɫǳҘ¨д\u03a2Өźs',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƙ\x87ҤϩΧӾϚãџ˾\x85ϮϠӝU˵ƠÄϘɬΒԗ=ȭǄ҃ҲѶʄĤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "ǯƕɬW\x83˶СũȶīʮƠʹǧӰѥ͵)ϗ'˶ɼӊĬӯîϬҌϭɺ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1522138598919897869,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӈf',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7776463584427412625,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƉƊĬ\x81ΩͺϴȅǙ,\\ьÅЛŀЭ˷ώï~Ǡƙγ¤ѳӋΟЭ\u0381ʭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\xa0ҡсĐυӊͷŞ×\u0383шҳĉɱσѨī*ύϕМӳЫđ˅Ѻ¦ȊɞӺ',
                            'message': 'ëЦʕ¯\x9b\x8bџƚќϴͿÄāϐΝԆ4\x98ϗÑЬΙίƽӹдʢɀĀņ',
                            'arguments': [
                                        {
                                                        'name': '˚qɌԌԏŤӵiTȜҮπӡæÝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĤȏЄѹţЫeӷΞԮʎϩìǖːţҝ\u0379',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:152854.131108:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ДêӄǔŊǹɹЛŵΒЇө·ƳȼҶ§1ɂ˸Έšӏ\u0378ʠ¯ʪˉƯГ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҸǝӅĻЏҠ˝ѽʍЂŉèΟŭԞЕɘƿĝҎǞΣƕԣӌ\u0382ǹɥıж',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ōϸ;Ɏɽ\u0382ϩҀŝԙˈȍ¡ìȃ\x93уƻºOӵԔûƇǣΕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'įȒη¢жѨƿV˾ϥҽˍƒԪʆҋxŖ\x9eҸ8Ŀžҵŕȫ¾ʐЭӪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʫτӆ\x80y˼ΑёgɋΖǫėʘƖȷE´þźƄŠĪ5ƙϒζƍʝƢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ьΎϖӞϵʅ˜Ӎŏʹǫ8˰Ά\x8eǅǣþʀϬԜɕѼƓԗú\x8cӤϦȜ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѓØMӜ˃ʐɦʊλƸυ°ҔϰѐΗΑĭԤQуšɊԬϱаєщ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǓϾν˄νӋÎӐƂÎǙӝĞʖȠÅϢɠOћч¢\u0378ЦѲҤсАSɡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'α´ϙŔ\x85ǧͼҫΜQɰϋ϶·фĽ2ɱɈkЦѴƭʻĀÇȗĠèԫ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǌ!ȦǿӦѿӆȊǥ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6857420364673177223,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖԛˋÂΣ{ӶʲĖ{Ϳ¾ɂämώǞ\x93ҁȣϴȭŮ\x88ӱģɩ\x86ɒº',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -53570.776511177675,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u038dćɘ(ı˷ƘɉӓCѩY\x98ς\x8bˣɪŃDŸ\u0381Ⱦҩөԏˌнąӑċ',
                            'message': 'Ȫӑ{\x91Р+ΠŠ}ͷӸһJԌȓӍȀɝһΩ\u0378ӚɿþʃΑӉçüG',
                            'arguments': [
                                        {
                                                        'name': 'ĀĴԣΠ˶ȁK@Нı˰˗§ɤÅѩϰ{ɋФǬê˔ďƑ˯ǰźҖƪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴ˛ҞКȚԜµҖιӿЁЦϿŮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˖ԌӠЖӉH˓Ûʵ>ɤҗ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'шԋŢĪϜ˨Ҝ˸ÁƠ#ԫϭƣ)ʬӯG',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 558474.4307162173,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǤAɃĲξÚǘаԐRƏϳȊЩͽͲȍ\u0383',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˕ʂǢԝŤӚǫҁэΩԣȢмΎӿϡŽāҋ\u0381¢ʒȨϑѽƪƃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӚɢŰлǡŏ͵ĮƹԔ˯ŸҁǹϻЅҽÖӌƭ\x91ɱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'қԜńũʲѪҗ`ɱыϽǖЃCƣĮҴ\x85ҐǠȽщ΄˴\x94ӨǣţɘƝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': ";Ǣ'хÀӾĢŋȘғѝǶɥ˅ĺϑĠƋҮ¨ʉʮˌȠƙϧēĕҸϣ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǲϩɌҠш_ѡǶțŽĎ˧ɵɖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "ӴȠЗԚʵ'ȄǰȡŹǶӛ¡ňǳ?ʐϚɛӢ\x8dyΥŽҜɤƳʵ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 529759.3045511745,
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
                'identifier': 'ǔџΐƺр',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ȪΎ',
                            'message': 'ź',
                        },
                ],
            },

        },
    ),
]
