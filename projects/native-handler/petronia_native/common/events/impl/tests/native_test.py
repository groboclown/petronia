# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-06T22:09:28.487439

"""
Tests for the native module.
Extension petronia.core.api.native, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import native


class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='RegisterTranslationEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog_name', name='RegisterTranslationEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message_file', name='RegisterTranslationEvent'),
            ),

        ),
    ),

]


REGISTER_TRANSLATION_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'ʶŞ¯ɚ',
            'catalog_name': '\x9bƬ\x9aʶюӬΎзѾтƍȑԍзχ\x98λļơΞƲһɄ$ƘҌ˄Å¦Ǐ',
            'message_file': 'ɃҊӍҲ\x9e£ңƯžϟһbԗЧȉћȄʑę\x98Ɠ6΅ѕΐѨӒȿʀ6',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ȼ',

            'catalog_name': 'цǲ\x98',

            'message_file': 'ĢŐ',

        },
    ),
]


class RegisterTranslationSuccessEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationSuccessEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in REGISTER_TRANSLATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
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
                res = native.MessageArgumentValue.parse_data(test_data)
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
                res = native.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ϱΏҦÒ˸ɸȆƛΝΑŢ\x91ҀϿǑīѤêĵӋӓΠ҉öɰ\u038bÿюӣЈ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5662861290760003055,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -59711.65775855775,
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
            '$': '20210206:220928.408903:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ú˝ŭȴ˜Ψ˙ŌƮȲoĔŦ\x91$ɳѸǿ2u]ТϠ˂ҡԕáŦĀ;',
                'ɕȟϘʹþĸ\x8aζϖӄơ\x7fɏӘǸ˚ĂŕɞҪƖèΆϣЫòǲԪȀ|',
                'ɶΞǍӸ˱ě»Øίˌ˃ћ϶ԏҟˌ¡ƁϵČŜǠˢԒӭ7ƪvλǱ',
                '.ȝȦ˯ĩƫʆҖ˓ώѮЬƞƂΣҼʈҸԠǓȬɳԁƤνƄΨȸǜǁ',
                'ƋĻΎ˰\u0383ҙӔɖˉΑ\x97ɭɡѩƪ<ҼҨƞwϪɏìǡȤɘQμЈʞ',
                'Ωkʈӥ^ēƔԤˁďψԗϽ\x89ǊãӨĘƽҾȯĘʍʖӗTȧǼɿо',
                'ǻʶ%ϢɣčŜȤǦЮȝ\x85ԜŉѸQŏӾϿɹ˴ҋвӁ/ʪ҆ɕOџ',
                'ԐБϞыΨͺɗʧ¹Ѫ΅ԫ\x8fÈʌΰҥӂǵъ¯БżƘǦѽ?ӡu˭',
                'ǙŦԄƋĜͶћӠ^ӃƸ˹ЋӭQѲ\x81ȼϺȾ2ь,Ҍ҂\u03a2ѠǞġť',
                '1ͶǆϚ˼ђΒƇ˅ɵ˴қʧ˝Ӏǝ˱ːƅ\u0381ƹƨҧʍҟȵΛɈȢȮ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                7003832674381825846,
                3675687457826365864,
                -1663770760914023215,
                5754758675910338269,
                6000101487730754021,
                3375973466679861326,
                -4816945476464207237,
                3809509427573860986,
                -4050094388203316882,
                2994492461655174606,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -44645.23466244351,
                814404.9336773508,
                474053.45083349315,
                579258.2609501289,
                799417.5654451362,
                595511.9415623703,
                961163.6360276046,
                669139.9073387559,
                415500.4982205341,
                343430.2803615141,
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
                False,
                False,
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
                '20210206:220928.409795:+0000',
                '20210206:220928.409805:+0000',
                '20210206:220928.409812:+0000',
                '20210206:220928.409818:+0000',
                '20210206:220928.409823:+0000',
                '20210206:220928.409828:+0000',
                '20210206:220928.409833:+0000',
                '20210206:220928.409838:+0000',
                '20210206:220928.409843:+0000',
                '20210206:220928.409848:+0000',
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
                res = native.MessageArgument.parse_data(test_data)
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
                res = native.MessageArgument.parse_data(test_data)
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
            'name': '˗ƪлZöͲӸϗΤʤȼˢǕѴʏêɰҠaɃˈǋͿđǛΘӞʮ',
            'value': {
                '^': 'int_list',
                '$': [
                    6533596040978625077,
                    -1373046145241042807,
                    -929342483531415103,
                    -1384801548189628681,
                    -8994043435191083787,
                    -6531054631947437733,
                    6610625962645626627,
                    3092194386071229325,
                    -6700317886515337373,
                    -6054351413216430816,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ď',

            'value': {
                '^': 'bool',
                '$': True,
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
                res = native.LocalizableMessage.parse_data(test_data)
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
                res = native.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ɨԌùʸ¯ɍ\x83ԫÔӧ®ƐʰēӾ˒πҸ*ѵɜʬʎʻҨǓ\x8fИȜә',
            'message': '=Ȳәĉ«ӜϸϐŋѬɅàЕЧԫĢȃ˯ˈцCmӇʒ\x9eѩ˦вЫ"',
            'arguments': [
                {
                    'name': 'ĒПҐƞЊɮʚɞ\x90áϟȗ(\x93\u0381кīŢȇŦƏňúЁÀßҢJ ά',
                    'value': {
                            '^': 'datetime',
                            '$': '20210206:220928.406871:+0000',
                        },
                },
                {
                    'name': 'ѰүѬāĎӻҿ\x93ʲƛt£ѧќ҉\u038bэȢɏUӑӀΡȐӽϔЯӴƝϽ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3487691380765268984,
                                        1936986936379995334,
                                        -8669140811495004702,
                                        -4728325920817517947,
                                        6278122459934922523,
                                        -1956184356221507707,
                                        -2898987674106276512,
                                        8762979308441268526,
                                        -5658514873399837142,
                                        2075322782641992805,
                                    ],
                        },
                },
                {
                    'name': '\x8dЋ¶Ȓ/ŁɳϬϲŎɄԠó',
                    'value': {
                            '^': 'float',
                            '$': 674118.1237477941,
                        },
                },
                {
                    'name': 'į³ѷȓȣξHԁ',
                    'value': {
                            '^': 'float',
                            '$': 478512.994731231,
                        },
                },
                {
                    'name': 'ƄʟңƱîӀ˦Ǹɂɛɇȱǘ˾äĚÛϪ0ˣ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210206:220928.407471:+0000',
                        },
                },
                {
                    'name': 'зɇǱΛηӴÇƚƃϔоӪ;d¬ѩʏԍʼɘ0ɩҐǀ\u038bδȧŁ÷Ŵ',
                    'value': {
                            '^': 'int',
                            '$': 6330933130265942283,
                        },
                },
                {
                    'name': '˫ōǞȂǉ.ǟҕɑǧʫ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210206:220928.407712:+0000',
                        },
                },
                {
                    'name': 'ƠσЋáɳšŠΟϥȝͶѓȖѿДőҋφήΒыӍ\x89ó',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
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
                    'name': 'ӗЁњµәԁӠπαáΨΙŢ¬%ȏǅЗßҋɿ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        60010.99773862772,
                                        932454.2995463642,
                                        871471.6331817807,
                                        156461.97070206646,
                                        297272.1021098856,
                                        106222.2882559101,
                                        140617.3434737594,
                                        106187.57374484697,
                                        778090.942750244,
                                        137501.5535356204,
                                    ],
                        },
                },
                {
                    'name': 'ŕĒö',
                    'value': {
                            '^': 'int',
                            '$': -5373474011385120626,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ɣǯ',

            'message': 'Ρ',

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
                res = native.Error.parse_data(test_data)
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
                res = native.Error.parse_data(test_data)
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
            'identifier': 'ʥͱŐ\u0383ŨfǚҮΉɗԂĭŘ҇ą@dɗ-ɌɈӂύƯ˪ÊЃȵī˰',
            'categories': [
                'internal',
                'internal',
                'network',
                'os',
                'os',
                'access-restriction',
                'network',
                'os',
                'file',
                'access-restriction',
            ],
            'source': 'F ӹңчВȓÅ\x8dð϶΅pʹ\x9cҬҼĸʮûϝƠңύŘƞԘÝĴԛ',
            'corrective_action': {
                'catalog': 'ƞμΙǫÔŖ\x89Ӱſͱɻǐǲ/ƅ˓ʎҨǒЖϗѺɖǧԉϡѣǖˇИ',
                'message': 'ӁѧxNŌЋȆЍÄƟ¥CƏǤϦRр%ǵˤĴȝƂǍѳ˴Ǣǚ×ˎ',
                'arguments': [
                    {
                            'name': 'ɕҲЍвʬͿīʮ\x8dòȶɆ˽Ʃ˕ҩɫČҪӘʨҮ˙˧¹',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210206:220928.404744:+0000',
                                    },
                        },
                    {
                            'name': 'Ʌ\x8cƿñ˷ӂŻʭԦȪʅҷʈʑƦËîw*˦ȥҦɆҵîu\x87\x84ǜӇ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220928.404899:+0000',
                                                        '20210206:220928.404908:+0000',
                                                        '20210206:220928.404914:+0000',
                                                        '20210206:220928.404918:+0000',
                                                        '20210206:220928.404923:+0000',
                                                        '20210206:220928.404928:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҥԮƻRғ',
                            'value': {
                                        '^': 'int',
                                        '$': -4620405746738618222,
                                    },
                        },
                    {
                            'name': '\x8bʞȴĖÄɑϗʐƔӮŸиʗЁĉӛŨȔԍǐˮѡǇѦÿˍђƾf\xa0',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210206:220928.405338:+0000',
                                    },
                        },
                    {
                            'name': 'Ȩ҃λάɵҦʊýŏBɔ¬;ΛĔЋmþ\x8cŪʏѹϦϠϽʽ˵ĄƋП',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ο½ʇʉǫ˷âKgѝǜαǚϑσɜɰЗyēЌѾĸцTɸuѱԎɜ',
                                                        'Ͷ˰ñȵΟхǲϱŴĬĕѪ?ˏȮΟɵұ²Ѡˤҧɔ!\x99Άʕǎɾӆ',
                                                        'ͻʔ%ɀÂ\x9bƿ϶KԈŧƲĞǏͽгˏđǳ˭ʟͳ\x97ǀɟƍőɪȽ×',
                                                        '{ʉcÃӹʑŭ8ԢĚρԝʜУƝ³ȢƿdӗÀӳǂǰΪϒèßƑğ',
                                                        'җЃΨķΕ²ȧʛϕȧĵϰÔʱɨϤϝɤǒĎȜρʎʉвŕГȊʦǄ',
                                                        'Ǩɭ\x80iǥŨΫ~Ϟûʂ\x8bαԨƣƭҎǈƕ\x93ǗĻȉϥȠďɽÈîƑ',
                                                        'ʉӏŻˁ èѢҋɂZӶ΄ΪЈRОāҧӮήržʞƛźȯјĂ¸\x9f',
                                                        '\x92ƆЅ\x9c\u038dТɁРЁѣԭ˺дĘʀǓƱqȋɀŐЎʨ\x9d˰JɡԂǹĶ',
                                                        'ҢДżѰʆӱɠÙЯȣɌȅ\u0379œȹĊ\x85гťҜť-ĨЖĞĿęȟ˛ҫ',
                                                        'ʻХ\u0379ҷ΄ιĳD4èßԅƪёXLҞЁү\x81Ӹżҹԋ7\xadӀҳyϵ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƽöǊƭҏ=ǘɝ҆ĜęǞԣƾʜ\x95ħϹʂ\x99',
                            'value': {
                                        '^': 'float',
                                        '$': 937753.4154726256,
                                    },
                        },
                    {
                            'name': 'ʢƏŴɬʆќƗǗɘſ˅АȽ',
                            'value': {
                                        '^': 'int',
                                        '$': 8824088147741081157,
                                    },
                        },
                    {
                            'name': "˧ѰЩԘԬӞ'ӐѴЍȎ˃ћјɨ҅Ȓ΄Ȣı҉ÚѩįƕйͷÅ(ы",
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210206:220928.406152:+0000',
                                    },
                        },
                    {
                            'name': 'Ťʛņ˰',
                            'value': {
                                        '^': 'int',
                                        '$': 7950526953520551837,
                                    },
                        },
                    {
                            'name': 'uԕİĖƈδȮóìƊjҡҾƻȘlҗȃ˷ŒŴϡԬȫǅ҉ʾvð',
                            'value': {
                                        '^': 'float',
                                        '$': 604612.5269304527,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ȰȽϿƣüӝķˮŻȗҁҀAҲњ\xa0έуʦ˗˕ӑʼӑλʡˬӵǛĎ',
                'message': 'ԏ\u0378ǃζѡӀĞƭΰӰ\x8bĦԥ¶øӤɔǰǯɡѴ\x9dҦϟˍϲӨƒүϊ',
                'arguments': [
                    {
                            'name': 'œĀ˃ǀƢdƄӼˆûÂӛÕ^ɩ´ԩǏ¢ԧʮ˖\x96Ʊʭқ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ə҃Ҷ¦ӆǄʮϪĖ¬ñҩ',
                            'value': {
                                        '^': 'string',
                                        '$': '˧ɣ^}ɭĊʷҁЙ˝Ч˫\x87М\x90\x8bҔΙ¿ʽёƻˢƬԔҧϛÐҶѿ',
                                    },
                        },
                    {
                            'name': 'ʽzͼ\x9eͲωȰ\xadƜЃˋР˦ÁǃˠțèƒͰ5ǐʮҎӴ˖ԁΚŇɎ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'Ţɱ',
                            'value': {
                                        '^': 'float',
                                        '$': -45888.88406386885,
                                    },
                        },
                    {
                            'name': 'ϯӕ5Ξ΄ʫÓʒWʼͻҠԤ҂УåϗΕˑůɛVö1ɋ`ҙӂǁ\x84',
                            'value': {
                                        '^': 'int',
                                        '$': -4462075772891674655,
                                    },
                        },
                    {
                            'name': 'ÃӖś˹\x81ѱϧӿǍкӒ¬Ǿ˨ǕѫǦɇҗɿŃдȓщś΅σȖɖǛ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ǙƑ҃zɤϲϏҤ<ɮ{ƨƷμДĂǑǠΕԏǛϤƻeуǰʟȡԝ҂',
                            'value': {
                                        '^': 'int',
                                        '$': 7156247404611083861,
                                    },
                        },
                    {
                            'name': 'ȇçŋ<Ų\x86ӪԊʲχΧ^ËĦƾ҆μΨƩɅұʝ˳ө',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        492410839222095593,
                                                        -7901132844136187621,
                                                        7785972951340758490,
                                                        4985598774321794588,
                                                        -2392602344661997542,
                                                        1974299138278030053,
                                                        -2355238064964881163,
                                                        2335193979730659626,
                                                        -1298200858345909048,
                                                        270916895344206044,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɣëʢɥƱʹź}Ä¿ȈʬßɉЩΟĶ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        -47182.49083777114,
                                                        486743.4379176528,
                                                        85403.08116714243,
                                                        174131.18637822027,
                                                        960924.9168264968,
                                                        350043.39699901827,
                                                        588412.5057327644,
                                                        620774.7409771428,
                                                        164647.84012683976,
                                                        818029.9094216898,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ѯRųӠҺʶǽ҉ˬƂÎ҅1єȧˀҁ\x8bſö',
                            'value': {
                                        '^': 'string',
                                        '$': 'Ɣʨ\u0381εЧǎȧǷϚǃӊЩӎʹϛУѫǬЏЬȫ˦Ů˵Ϗõҏȕ¦ɸ',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ȧ\u03a2ԓͰϲ',

            'categories': [
                'invalid-user-action',
            ],

            'error_message': {
                'catalog': 'ӎʛ',
                'message': 'q',
            },

        },
    ),
]


class RegisterTranslationFailedEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationFailedEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='RegisterTranslationFailedEvent'),
            ),

        ),
    ),

]


REGISTER_TRANSLATION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'error': {
                'identifier': 'Ҳ}ӝǿǪɽӥˡĒΝʃȏԪѢͺĿΙ˵ãͱӃŉOɗĒ˥ƲčͽГ',
                'categories': [
                    'file',
                    'invalid-user-action',
                    'file',
                    'invalid-user-action',
                    'file',
                    'os',
                    'file',
                    'access-restriction',
                    'invalid-user-action',
                    'invalid-user-action',
                ],
                'source': 'αӉlȑʣҦΌϯʙҹ#ǡʈɫԊˈҴ¤ʂԚǤ˟ѪǬȃРȭèĕľ',
                'corrective_action': {
                    'catalog': 'ø˩ʂɌ\x8aȥόˈʛǥƤòƺXË˟¹ČǦρˈϾÆϴΰȟʖхŢȥ',
                    'message': 'іƦƴfѹ\x9eҴˬƇšƐũƖϖԅ¼\x9cſΎĦǫχ\x9dЍǀϑÍ\x84Ԫ¼',
                    'arguments': [
                            {
                                        'name': 'ǆҧӧƱȰȈ¥ƖȝȒѭӢҜҢΤč°ěгȾģ\x8aыƫȰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1038813495333379492,
                                                                            -1691506343550568174,
                                                                            8265539572373828648,
                                                                            1754720254412786850,
                                                                            3948806916229041944,
                                                                            -2803241748953997667,
                                                                            3083401051751005585,
                                                                            -355587691757970410,
                                                                            3201525663454404245,
                                                                            -1742884392819161306,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˤ1',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҩcӀǷȤˉŬΤѽӄ\x98ґʖˇΌũԞɆєΧΧɗć˧/Γ¬%ɾϝ',
                                                    },
                                    },
                            {
                                        'name': 'ȂɶНāȨ\x86ŒʘŞӌԓòąΉ¶΅ƱbϴýċȬɦԈʁɄzʝŘԇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7495182224599208148,
                                                    },
                                    },
                            {
                                        'name': '˧\x85pŧĸɦӑйЭҲĀȴĒ¶ӖϏǘȠщ1ƍƭˣѠҧÌǴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9138172848229922397,
                                                    },
                                    },
                            {
                                        'name': 'ɋĤȎȸφѡӀȟǳ¬\u0379',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɌͺǨ\x84ǫѮ@0ŵԑĝžˬĝɿǗɪɩĵsɂLɰƿŭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ń\u0383 ʈŒƉƱюȁʘɨĈΧǛɡͰΌkԢƜŨÇћľԏҧΊ\x91ҲС',
                                                                            '͵Ơϒ˵ȴɫȜġˇ¹\x89ԫŷŞ2ȢΰѺϼӜɑ˫ҲԤ\x86ʌűŀȐP',
                                                                            'ƿԁЦɥRƑҌɊԐÓ\x8bδκǇƇʃŐ¼ЪѻȝмɃƉͷ\x90ЩԮŲԛ',
                                                                            'εơоĪźļϨӿҧϟƢzÏˆƵJ5әDzЊԌƟˬԥЇӤѹρØ',
                                                                            'ҴƘǦśЗʣȾӠҊԦ҂Ρԛўӭł΄ȑÏ×\x95 Ŷɜʙ)GѺИΌ',
                                                                            'ɌʆāȰӌLɓǮӱѩ.ԙʆkɠɋҧҾɿΫɜɿǮįʱȾ´ӮѲѳ',
                                                                            'äơůʧљҙˬſѫԅńюŁƠʔԑˉƮӕŻԃȼÁΚϬţӁƉʡe',
                                                                            'ǽ·-ňϺƈǑǠȳЕɓXԡԁs,ǉȅ^4ϋɪǉF?nԎĶʱͺ',
                                                                            '˹ѰѰϚǈΠŻԋǁ=мҐͿԍɣ\x8cÄǅΈǓȾϲŦʒʈʇɲȶҩƨ',
                                                                            'ЇЕħʞǆǗǤɞϰĕǠμ˰ʻŬԖқŤέγξϥϬĭӞϽЄXş˖',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ёɢ҈Ӎŧςǧɘʕ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': 'ҿҮсћƳ\x8eˡĿӋʢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ЙìΪȃǪҲвĶƘĠƗʍӺ¢ɭ\x98U',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 477586.8642415175,
                                                    },
                                    },
                            {
                                        'name': 'ŪԁðĩФȬϾɆĕΝǄнŘԀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': ';ҏ\u0382ξªʹ\x89ԞЅÒĸґˬщŉ(χҀʉñϜѤ\xadʉԞɕĩѠŦŉ',
                    'message': 'ʸďфдϻҳ,ǩțŭӽǘҥƲ˺ŅûЪNŶτƔìȼЈԆǥƕƤǻ',
                    'arguments': [
                            {
                                        'name': 'cԍӜϺ҂ˍĆЦɛȥӴӧ҅ÎѳɬԆǏвЭϣҺΗȈˮϮпˮԦA',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220928.401130:+0000',
                                                                            '20210206:220928.401163:+0000',
                                                                            '20210206:220928.401170:+0000',
                                                                            '20210206:220928.401175:+0000',
                                                                            '20210206:220928.401180:+0000',
                                                                            '20210206:220928.401185:+0000',
                                                                            '20210206:220928.401189:+0000',
                                                                            '20210206:220928.401194:+0000',
                                                                            '20210206:220928.401199:+0000',
                                                                            '20210206:220928.401204:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˰ΙĈϓèƪÒєƚɆȣȣÒԗˎ¥xŢȈȨȬӢϺĹ˪ӏɞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӧ²ǲҌVƴȲbˊІĻҔͽƉǊƗ«¿О\u0379ѦʳÆԊƴ)Ľ˾Ӂţ',
                                                    },
                                    },
                            {
                                        'name': 'Ζ3ҁoŠòÕ˳јBΛńҬƻԊŪȾ\x8eлӥGϳŕĚȑȤǸӍӮY',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x9fĩϱчĶғųҥ3ƸȄǥ7ʠӞԏɽƉżɚčΟˁğ1ʝΛæӺť',
                                                    },
                                    },
                            {
                                        'name': 'ÓΎΩȤ҈ŗEщɏŀϪŅκ!iǞuζ˺ӘԌJϴӧȮйǺïľȕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1802858461972327661,
                                                                            -8715988754130004408,
                                                                            8861230772302144800,
                                                                            8652754740890647249,
                                                                            -8995930669871105142,
                                                                            -6781307546874306234,
                                                                            8830908412429277969,
                                                                            -5028516677260181355,
                                                                            -7866281321630647527,
                                                                            8827745451103453380,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƮǞűτĪвĬѺϚчίӾͷÈ\x9aĒзιǺϚƋƥſǗWԛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'µɎ»ƊɦɸμƁϹ\\ʭýӉıͿĿʾŜ\x89áїӘӋȤϥСĺɁBµ',
                                                                            'ΠɔɌ\u038dɁȕǱԍѻѐɃĤːԡєҟҹĲȥŪƨ˚JΘҼԓƅВȟԫ',
                                                                            'ŤŒVϑӒίʿѰ¹ńɖϮѰMлiΉƄҢѐɡɰЮǜ¯ʍʃӂȭϵ',
                                                                            'ƣ˵ҌҕͻŻжҝäӿѤĔīǪ;ĝăԀјԮЋ·ѴĠʋ~ЏӚ˸ќ',
                                                                            'ƂΜɓΔԥ\\пʄƣΗeӘ¶ѻ\xadԣSʕѽŢ˵΄Ώϧ\x80*ϢǂΧŴ',
                                                                            'ĒŬÌ,ƎȞ\x93Ȧȉҡ˧Ӆԃыѩκ˥Ϥƿǵ˼ʹÂәЉѮԂÇ\\Ė',
                                                                            'ЌнΕzǠ%ά5ČҌӕѶžЯαƙ˝Ɗõhǃ=іҫƹÀůİƠЙ',
                                                                            'зǫRѯҖӦԥɠϱэŁĒvхƵĹʸċώƇõŰ ͳɢЉвŌ\x8dĔ',
                                                                            ':ȍѲ°νǚūƀ\x9eķǾņßʉθćˑȽ¢э˥4ӬсηÍͶѽӿJ',
                                                                            'Жɕɒ˰ѺįˣԃўϿĥч°¬ҮΪɍ˒ƻʻϕōԛ\x8cɁźǥϤΚЙ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӀĔŃқșμёƁäΥ҄Ǡ˙ȐЉЯÅxŅѩːӵ\u038d',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Б˺˒ɖýɠ¯ʉȿԝӦʊӈʬ˃Ѡǀλ\x9dð\x80ƱԝӗˠΌӺӸȸ(',
                                                    },
                                    },
                            {
                                        'name': 'уĸΔ×Ɓ˃ҩȋ_ҕǸӋғƌÔϰʈŁˮо',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4425623861056877198,
                                                                            3774948637296046413,
                                                                            8196052272619750598,
                                                                            -7457534075917991599,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˧ɽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͱǇĭҫƋ˵\xa0ȧÐƎѻĕ½gɸŀҥ\x97іŪȩŜˊʊ¥ɕ.\x84ҽƭ',
                                                                            'БEԖŨӣυɝΞұƻ/ʠŷVϼåɫϭDʨ?Ò·ȼΛѕʈĲpӁ',
                                                                            'ʈԁԑ·!!\x88҃Ȫōʒ\x87ʷǈ\x82ªԅҦԦĭʪǸƴûѬѵˈ÷Ư˘',
                                                                            'õОҕɌƞˏӁ5N¸ŶӌУβϷʦѓØǻҋїҰΈˈϯř¬Ƕľì',
                                                                            'ДŌԩȂУҁ˃ґɉϳ¬ÿȾ˧ƲΉĢĜĽƲΔɇ|ǽ¸§ɡο\x89Ӹ',
                                                                            'ǹ˹ЬƴǙʢ͵ȎѲƘ3ƠαÏżӚǜªіĖɍĎΣƈ\xadŅCpȨb',
                                                                            'ңѼϯT˸ӢЉǢŝËΛʰ\x88ΪҡfĚĥЭɿԏʌɖ1Ϣëɂԋ@5',
                                                                            'ԘҲɁëȥ»<ωʓ[ЄňŲȃѻȆ\x82ђ˱ʦͳԠȄŚʵҩѴ\x87˳Ц',
                                                                            'νĞ˽ЩɟÏ§ԥČXԩƌ½āĶcғƶƞɠ҃ϖɝžΉ\x8eȡƀɮ¹',
                                                                            'ʶΫэÿȿѤ·ǿЛѯϫɕˬТŒYɯȰɌоҞÛáǤНȄҏŲӶĶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'űʑƐŞҩƸ¨śΐɪôԒъʞŖƫǶɦҖȢXҔ0EÙÒԄрæҹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 215444.8384929885,
                                                    },
                                    },
                            {
                                        'name': 'ҼҶɑɟġlэмʼ˲DǞӅЧҞǹ˻Ɛя˺ȘπЕɘӵԏȷсɾε',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6495789428333463294,
                                                                            -2376113295744387946,
                                                                            -5500074801249094649,
                                                                            -7095978275483925019,
                                                                            7977057150965440812,
                                                                            -965678054971839125,
                                                                            3002662044662642510,
                                                                            3903163764466385854,
                                                                            1320984022992213848,
                                                                            8206876361523036595,
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

            'error': {
                'identifier': 'Ϝ,ǰΊҕ',
                'categories': [
                    'configuration',
                ],
                'error_message': {
                    'catalog': 'AͶ',
                    'message': 'ң',
                },
            },

        },
    ),
]


class RegisterTranslationMessagesEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationMessagesEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_MESSAGES_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationMessagesEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_MESSAGES_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = native.RegisterTranslationMessagesEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_MESSAGES_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


REGISTER_TRANSLATION_MESSAGES_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
        },
    ),
    (
        'bare-minimum-fields-present',
        {

        },
    ),
]
