# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-24T16:41:11.882261+00:00

"""
Tests for the i10n module.
Extension petronia.core.api.native.i10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import i10n

class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
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
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
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
            'locale_code': '»ѝѶϷČ',
            'catalog_name': '0ŹɘԜЇǠΩǘɮцА·\u0380ЗБěɰſ(έȅѕԦˌųηԚòǐɼ',
            'message_file': 'ςLˀԍȇǖ;ώДήуΤȄːΦǁӡzʬЗƽɏâЪʫŚǥӜιǊ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ǫ',

            'catalog_name': 'ňǁ\x98',

            'message_file': 'ұѨ',

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
                res = i10n.RegisterTranslationSuccessEvent.parse_data(test_data)
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
                res = i10n.MessageArgumentValue.parse_data(test_data)
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
                res = i10n.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ǞяŎ˔ӤȄ~ΜϖĉǪѴЏĺʦİxǭĘώđϷȊԊ҅ɹқάÑĽ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3486894220056658884,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 741296.826142675,
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
            '$': '20210224:164111.786453:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '¨ƌƦӃХтΆӮĀșƉӳȻƳÉϔËQӔȉӵTʯÌǹНͳIˑƪ',
                'ķĒĎɈɎɧʱǗӘ\x92m_ÖȿΦuӇΪԣѩԭГaːΗǦϱӍĴÒ',
                'ˀʙԭâˍƆάҌ\x96ԣǲČҢПѡΦҹҵʵûμīѯɇ\u038bӝȨƊҍν',
                'Ʀʎőƭ\x824Ӽ$Ųƹˡ;2ήlАȓ҄ШˠΡʠȣȄȽŖӆʎɻϾ',
                'ɸӭ(гΒĬSȘÝɿ\u0379ѭҞ\x99ӟш\x7fίԕҜĀʹѭҖ\x95МďӃFм',
                'ђɺëӗԖȝϘſʔΩҳ\u0381βrūϬƵźe~ƢжʝňɦȗҔ҄ӖҀ',
                '\x9bӹŐ.âπȱԧǍɍ˙\x83ОĪǯȿƜѲΌͶƸκĖǔÆ\\;˅ÿЗ',
                'ęΨӭͼǏ˺\x80ʇЕʨħδ\x98ɽʴßӲΝΒ«Ü&ЕǰїӌΞӱƳŊ',
                '҂ʃʇҕԆɱɉŉķƤĖȇȘǡkƯ®ү¹ūóȗӊͽêɝЩʻЬԇ',
                'јŹŴ(ƪҗϘԈѧǒӥȗǍɦϛӦԬӅPȉҘ\x87ė|1ѫĤД',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                3623679906554969187,
                -6735814325170202346,
                572763898786250333,
                7331790819813818657,
                1196887685661723850,
                -6326964033377559297,
                2786419559344128517,
                7676296358488967570,
                -4204394627969492216,
                -6142517378744135292,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                726818.0582027055,
                91407.81984295422,
                338089.3807451217,
                963727.2588692235,
                140889.4346192615,
                516346.44665843435,
                972252.5948325419,
                229866.91227329965,
                404403.2026664933,
                811193.2046966074,
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
                False,
                False,
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
                '20210224:164111.787588:+0000',
                '20210224:164111.787605:+0000',
                '20210224:164111.787613:+0000',
                '20210224:164111.787619:+0000',
                '20210224:164111.787625:+0000',
                '20210224:164111.787631:+0000',
                '20210224:164111.787637:+0000',
                '20210224:164111.787643:+0000',
                '20210224:164111.787662:+0000',
                '20210224:164111.787668:+0000',
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
                res = i10n.MessageArgument.parse_data(test_data)
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
                res = i10n.MessageArgument.parse_data(test_data)
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
            'name': 'ϔ\x9fѣε˂ҔԙǃѸͰĹȡɓŹœğω×ʺŲҢƨӕ+ʍϚԒͿȅ\x9f',
            'value': {
                '^': 'int',
                '$': 2792198912513847643,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʰ',

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
                res = i10n.LocalizableMessage.parse_data(test_data)
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
                res = i10n.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'Ίһҍ.єƐԠɂϖxɖΚBȣȗϢ9ÑѱɏЌJzŝџg˽пϊŌ',
            'message': 'ƉǴЗԨԄÖєǦњÌϒ˦ΫǲưÂзʠͰƶÐƺһѨƤɀěɎϞɓ',
            'arguments': [
                {
                    'name': 'żҟëȲώδƥ˨',
                    'value': {
                            '^': 'int',
                            '$': 298570232204978126,
                        },
                },
                {
                    'name': 'ŘǏƫŃʚӪʵ¦ÙE',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ăŷҡιоǜԝǇʙΎӎΒéщˠ\u038dԌŒˤ:ҶӨøǸɲǳǬé·Ν',
                                        'Ёhұиýɠȳϓΰ{ğϔʗБʴȑ҆ȃ<ԞѴ;ÅǍɡưʏϖѭù',
                                        'ʽŻЉƃɷԣKr×ƗgȽɃƦjʀӹїƱѧǞſɋĽÀǰØv(d',
                                        'ҰÎОɆ΄ƿǯűĶ1Ǆқ1ơрÑзϨҙҾҌǐϩΞőԬđʮʐŪ',
                                        'äӛƄЗ~ЕəԀΧӪɂǟѢũεòƜŽŦϿİЕĘʧԞCˡϸ˖ɪ',
                                        'ɝ҉Ο>Ù\x99ʈbšрɋ˰ǹ\u03a2ѓ7ʑԏұычԮȷѡ҄ŪЂϝԥĀ',
                                        '˝ϼӳȻƸȳ¥ƳѭǖķҢƷEѱз\x7fέѨǑҒĉĳϬÈļұàŇЫ',
                                        'Ƶ˝˪¢\x7f|ӔЊӅкηӵӪԤӎĉ=ќŭɠǾƚĖĩȨǙÕԈõӎ',
                                        '˸\x99ȼӀBШһ͵ҌƱĝ҈мŪАͶâưӵ»Пà@ǞіɕΚɼ\x8bӐ',
                                        '\x8dǃʯôϒ½ȡǽҦµͳˏ˭ÍʼyɋΦÂʝˊӌ3ȲʅѠМɔu˕',
                                    ],
                        },
                },
                {
                    'name': 'әƝԚҐжȐȎ˨´Бҝʃ',
                    'value': {
                            '^': 'int',
                            '$': 6301628150447203644,
                        },
                },
                {
                    'name': 'ҳԨеӡ\x84ʥƔϒԧČԘƥΔ˲',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'vʄɶԩűtŎϚɁ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
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
                    'name': 'ʾϜфʆǒ1Ѱ˪Ӡ\\θÓĿӨϜ¹ʟѴʮƆӼͳɁȩPҋ\x9dϡг',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ʪʟ\xad',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'Όґ¾ϬјɳȬϻōuƹԦǯӌ\x94ú>hӃ',
                    'value': {
                            '^': 'string',
                            '$': 'όȪȺ϶ɜʍ«ƹΪŎǪɳǇγҘ˯ƈͺҀƾƍ%˲Ѧκ\x88ŲɗӐҩ',
                        },
                },
                {
                    'name': 'ѕҪɻƎ˄\\˘џΑѺԭ\x83ҟTȏI®ɝƱ¡·Ʈˬ˶ɘФ˓ˢϣÿ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        845633.1632667172,
                                        -62134.85982935609,
                                        150711.79870270038,
                                        40720.94390548408,
                                        1812.8483782809926,
                                        591071.4400708544,
                                        462793.74790046655,
                                        497080.17917768797,
                                        533541.7774931701,
                                        495411.7369725988,
                                    ],
                        },
                },
                {
                    'name': 'ўҡǿǥ+΅ÙÄ҇ǿФò҉óҘӺ\x97˗҉ƹ\x80¥ɽΐʙҊź',
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
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '\x90˴',

            'message': '0',

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
                res = i10n.Error.parse_data(test_data)
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
                res = i10n.Error.parse_data(test_data)
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
            'identifier': 'ǙóɐǫΉҕʛ4PӈɛŃϑʢКʯ˩ǎǦҰc©ӊŢƻĘAĵÜB',
            'categories': [
                'configuration',
                'os',
                'access-restriction',
                'configuration',
                'configuration',
                'network',
                'network',
                'access-restriction',
                'internal',
                'access-restriction',
            ],
            'source': 'ɇƝʍϨɺŘԋ§χӴ҇ƗӲϜθƾŝӵӹĦӪΰ\x7f)Ɩ˭ȗϵԅϡ',
            'corrective_action': {
                'catalog': 'ǜӣԐʻҾӫCĖҴԫʳ\x93ԩөʤҼЌʽČIˆJŴÆ˴δϐʯ\x84ö',
                'message': 'śΦ»˺оȏƾѫÍȫˌˢ¿ҲËӮАҌţɠǷdʇþ΄ʬœƢšƿ',
                'arguments': [
                    {
                            'name': 'Ɲό˞˪Д\x80ҔƟΐӣżҞӲӴŒФ_ɿϠųЭǉӢĩǟ϶њĠůʾ',
                            'value': {
                                        '^': 'int',
                                        '$': -4738805876430792215,
                                    },
                        },
                    {
                            'name': 'ȵͷĬεȆԁƼБÙΕ±ǅƂρçȠųƁĞʶƺȷêÏиɫģľӺҐ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        918196.5189314751,
                                                        5203.608785367891,
                                                        95783.64360206033,
                                                        603570.5940963868,
                                                        291727.36061463313,
                                                        403600.28648476815,
                                                        -47800.15493967863,
                                                        542237.418904857,
                                                        756195.7455981941,
                                                        539304.5463290723,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʡŞ^ƱͳƾȦȺҘɌʁӧ_\x96ԍ\xa0ƺǥţќǮѻқŁȬГȞÛνđ',
                            'value': {
                                        '^': 'float',
                                        '$': 970169.0384167184,
                                    },
                        },
                    {
                            'name': "'ʯĶĊȌǷҹђ;Ǘήǣ\u0381_˵ɲLәžÿȊÐғIԍù",
                            'value': {
                                        '^': 'float',
                                        '$': 291304.12994048925,
                                    },
                        },
                    {
                            'name': 'Áѡî҂fɊϗÞĪӖƚЂϐ\u0381˸шҞ˒Ξ˱Зӳҁǅϯ3ЧŒӸ˻',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ƬÛϷӛˉҏҎŌϹRɯŧϖÑ«ϰћɱˊȢkѫҾНʍß',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ʥυȶűŗőŬƪǎʕİȴƥʌчŷӚμyĕ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210224:164111.780671:+0000',
                                                        '20210224:164111.780686:+0000',
                                                        '20210224:164111.780693:+0000',
                                                        '20210224:164111.780699:+0000',
                                                        '20210224:164111.780704:+0000',
                                                        '20210224:164111.780710:+0000',
                                                        '20210224:164111.780715:+0000',
                                                        '20210224:164111.780720:+0000',
                                                        '20210224:164111.780725:+0000',
                                                        '20210224:164111.780731:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'њŃǥ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210224:164111.780929:+0000',
                                    },
                        },
                    {
                            'name': 'зɠԠſҕFĲͳ\x89ӱ',
                            'value': {
                                        '^': 'float',
                                        '$': 868636.3241444018,
                                    },
                        },
                    {
                            'name': 'ƐöѳĮɍӜ6ѲžԐё¸ɱëǮ@ȑЗǨ¾ϠοψҰˡ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210224:164111.781175:+0000',
                                                        '20210224:164111.781186:+0000',
                                                        '20210224:164111.781193:+0000',
                                                        '20210224:164111.781198:+0000',
                                                        '20210224:164111.781204:+0000',
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ċϻí˭ĐΏάӇq²Ã.çĮȭӆξˮĖǴġп\u038dťϾȿßęͺ_',
                'message': '\xa0ľȢhâī¢рЀɒȺ˵eˮʱ˫ȁȊҿ\x90ōсҞϨĿԁεͱȐΣ',
                'arguments': [
                    {
                            'name': 'ҙЅҽӼɾǷͽȘҟŁҮЅôvχЮҠ£ěĕǒ¢',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210224:164111.787996:+0000',
                                    },
                        },
                    {
                            'name': 'tƙǟ҇ɭťǑӊϪɦÓÜFɜɘԥÆǑƜӇϛǬΊò˘ǎΐ÷Áӟ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210224:164111.788180:+0000',
                                    },
                        },
                    {
                            'name': 'ΘYɶҹ¬Шјbԇ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        342235.1929015094,
                                                        521383.3018058562,
                                                        425686.7920571307,
                                                        349163.94759577815,
                                                        260230.32984491804,
                                                        689762.9886879674,
                                                        521281.9407048748,
                                                        362229.970343716,
                                                        444151.6347128599,
                                                        500393.64378429344,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ʒ˥Ҩѣ©ȵ\u0383RδϨġÓѾ@ƖуҧɚĪϖϱš˧ǓҿDӱόΥъ',
                            'value': {
                                        '^': 'float',
                                        '$': 345266.85665092285,
                                    },
                        },
                    {
                            'name': 'Т˶ʤi˶µĤʽάċȘΟҞїǦŧғԨˌĉѷƽűĔ)ȬƩĄŕƈ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        126156.16189855887,
                                                        547712.2369320791,
                                                        -29185.374003877194,
                                                        947397.2271700092,
                                                        461519.95413603575,
                                                        875394.3918396081,
                                                        514448.49755705614,
                                                        61161.57453501559,
                                                        346327.8462901697,
                                                        559127.5910258195,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ќsʩ\\ˤϷπӫy)˱ƃʍӥ6ͻγԥԢ®ѡŦÉ8аɳǻ˄ӫɷ',
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
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ϓвϵɦɌDŸɺƙłʥƕӸ˫şūʍĎ˖ƪ˓гuƪȾјɟʙȩƘ',
                            'value': {
                                        '^': 'int',
                                        '$': 9186748036922213122,
                                    },
                        },
                    {
                            'name': "¡ѡяāκ'ȾɛϜ*ʞϘЅɨǝȚʬӈԝ˕ÁѻɷԤȱŻ\x8dӆƂǄ",
                            'value': {
                                        '^': 'string',
                                        '$': '¬Ҡœԣ\x9eЃԅԛƂϪϵǨϧ\x8dΒȜɊʆʀѠӴѝǊ´χЂǻÒȹƃ',
                                    },
                        },
                    {
                            'name': 'ԊϫҶ>ӗ\x85ПҬӢˡУɐΚ',
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
                                                        False,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǲԛûѩƯԑ\\ėrȆĤΊΞЬˋɩһĿ\x9eԅˍůĸƗȦѥϮώԌȾ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ɉġɺ\x83ʢӰҬĂŔĭҹпǖɁȇǂӽ+ѕgØΓϋ½ȝBǏɌ҃ƈ',
                                                        'ɮӛɠÌ҃Ţ˂ɢưӍɥĂҋʀÐʃnŮ\x88άǠЂӞѦӄО¼OƆa',
                                                        'ԧ˛ԧԥĒňΖІΌMӰґԭзȼȖ)ăȄ҉ēψЬϹǫŁУҩǍѪ',
                                                        'ÝŞ\x96ϝĜˁӑǳɏ¦ÕǺΛƹÈЙƧĎЉƐ¯ěʲϵѠʙȬɞʴʃ',
                                                        'ɒȎнҋĶЯɅ$ԛˠӾŁŴȒʹӠɌљ@м\x98ʡͱҽǘѱϑɧҋέ',
                                                        'ҧζƃÞԞМǈĬЏ˯Ӛ\x82Ƕ\x9aʦеұǯɩ\\ӶЦҴѠϩӤǹ?˳ǫ',
                                                        'ŝ«´°ҝ3ӡɾqƍʷ\u0379gñσѦʝeӾɚĤԤɱɩΔ6ˬÞόѢ',
                                                        'ЕӜƀОʣΜǌȝϳĴƠӮȕƸ˪ҜÍɴ\x8c3ZЖϥoǘʋȓǹΠ˨',
                                                        'ӹɳԆΖˇʴęǏƄÓЧџƬĹȅŘ¡ϟɃȨԁΚҜǒԊēƳљÈʋ',
                                                        'ҕ˻þʎˠĝŻǍͼѾϠԨƄϒ\u038bѸŖçFoȞ\x87ʪɞϝӶĮź˕ą',
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

            'identifier': 'ì§ӚωΗ',

            'categories': [
                'file',
            ],

            'error_message': {
                'catalog': 'ҷƙ',
                'message': 'Ґ',
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
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                'identifier': 'ˡɷ\u0380-XҙͰӋ¯ŃʥȃώъӡФïRĢƌöƾŢȊϑѫÕȽș˖',
                'categories': [
                    'access-restriction',
                    'file',
                    'access-restriction',
                    'file',
                    'file',
                    'internal',
                    'access-restriction',
                    'invalid-user-action',
                    'access-restriction',
                    'os',
                ],
                'source': 'ȇȾŵn\x9c\x94ίƅX\x84ʣʣʶʐĀuĊıǏBЉJԈӮғĦЎѶԜƉ',
                'corrective_action': {
                    'catalog': 'ϛѪң´ΈӃƝÇƬÁŧӔæʁƬɜїüђ˪ӼʬĻǈ϶īӛɴϙÜ',
                    'message': 'ÄmĄμʤϖѴ˫ɤпèԞ҇ɄÅ°Χˮ)ЖɳĺŒĉСʤɕ˳Υ\x9e',
                    'arguments': [
                            {
                                        'name': '˝ϛǿłǆΈɭŰҦΜѲǐƼȚǥӷǽɹΥтċƗjƪјèEΒǱ˅',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164111.772980:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȃʬ¼њғľԈƏɍɔ˄ɄχɽΕȧŔǳӄɛ˂ϓѵ¾ђѨ&Ӎ϶ʵ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'íǜϴȦΡɢѼȂ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Фƛ6НÉǇyԒƓѮЕŔĊƆΫҡƼŌΈuʁʆ\x97˻ϚϘтԛȎƖ',
                                                    },
                                    },
                            {
                                        'name': 'ŵċƛLǺϪЏɱť͵Ȋ˟σǿɤНʫбƬ·мÀɊ;ЭÙĚǦ\x9fԍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3101605898466129270,
                                                                            -1136083463178264045,
                                                                            -214703388218378628,
                                                                            3774968685519038334,
                                                                            5434916685245308549,
                                                                            7290713946195073835,
                                                                            -1150095298044273650,
                                                                            -429038554470414996,
                                                                            3511656018013207105,
                                                                            3676400593642400049,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'oςͲ΅Uɕ϶ƨҨ÷ʋêȹĵŗƄt˂Ϯϸ\u03a2Ȩ¤ƅъΚ˵ĉϴ6',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˅Ÿ\x90Ӏų{ӡˍӯԤǂɢƀǪůӠԏѭSɞӞ²гԁ\x87ˮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164111.775231:+0000',
                                                                            '20210224:164111.775252:+0000',
                                                                            '20210224:164111.775260:+0000',
                                                                            '20210224:164111.775266:+0000',
                                                                            '20210224:164111.775271:+0000',
                                                                            '20210224:164111.775277:+0000',
                                                                            '20210224:164111.775282:+0000',
                                                                            '20210224:164111.775288:+0000',
                                                                            '20210224:164111.775294:+0000',
                                                                            '20210224:164111.775299:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѝ˦ԞǠϮÇӋβʧιǷβēίǕƺV',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164111.775519:+0000',
                                                                            '20210224:164111.775531:+0000',
                                                                            '20210224:164111.775538:+0000',
                                                                            '20210224:164111.775543:+0000',
                                                                            '20210224:164111.775549:+0000',
                                                                            '20210224:164111.775555:+0000',
                                                                            '20210224:164111.775560:+0000',
                                                                            '20210224:164111.775565:+0000',
                                                                            '20210224:164111.775571:+0000',
                                                                            '20210224:164111.775576:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'hѯёÃь˒ХϥȒ˩',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164111.775789:+0000',
                                                                            '20210224:164111.775800:+0000',
                                                                            '20210224:164111.775807:+0000',
                                                                            '20210224:164111.775813:+0000',
                                                                            '20210224:164111.775818:+0000',
                                                                            '20210224:164111.775824:+0000',
                                                                            '20210224:164111.775829:+0000',
                                                                            '20210224:164111.775835:+0000',
                                                                            '20210224:164111.775840:+0000',
                                                                            '20210224:164111.775846:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϪĿԥѥĢӌhЋц·ȚʌЭħľ˭ѱӟĥoɕМ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʴŔï',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'К{ԆļȹѰЂƶĐiϭσеʯʤȎʥІЌӁɁЭɚΈЎŰťB˰\u038b',
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ȖĄƩϰΚ\x83ƀʵʉ}ǪͿØǊ$(ɶμ.˸Ѧʳˑ\u0381ˆ\x9aƛĮɷʧ',
                    'message': 'ƣκΣYΟǉԪő\x8bʽáѕɽʟԣӷƍ²Ə.ÂӦȒ³ҤŜȲτɫϾ',
                    'arguments': [
                            {
                                        'name': 'ΖŊт{ѳҘ\u03a2П®ȇ˖ωœǸΥЬβǍ˔ŒΨ\x97ϋӨɛ˛ǲ\x9fӹʎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164111.776595:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ҭѽƶϐ·ǊҺϗȼȩiώǰʬπ˲ΎӺђƐĲҹ8іЉͱ˪Ƚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': '·ρıʗóɬ\u0380ŜϼȽ£ƮéÆӛʿζìԟ˂ϘЁԖʵͷ͵ϘđĈϿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8208730596535769767,
                                                                            -189777962762650366,
                                                                            -92297775326433699,
                                                                            -892828479624433016,
                                                                            7776907395019487189,
                                                                            8740474596301348905,
                                                                            7691418550987931617,
                                                                            5253141824411839217,
                                                                            -4480124263736418232,
                                                                            -2848316646039827389,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˺Ѡxĸ-ɿϞ\x90˰ѷɥǗԤ\u0381ЩѡгΚ$ÓɟƫжӨɗ˽',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϘÂ˗ǖĭΪԗɴЊȨÙӧӦɕӌϙƔÔǼҷԥϋѡýԧǐȩĪώͲ',
                                                    },
                                    },
                            {
                                        'name': 'ɁlһŬ˧Ǥ˓ϛҮǟƺѓјɞʚҏ˯ԉǩ˛aѲǷʫҎMѷǫΔҡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ɗҀ\x83ƶôĳŃȓ҈з\x9dЂȩӭӸΔI'ґŹї8ΥŖͱԄɑMƑӄ",
                                                                            'ҀG<ԉε}γƮɟŨȫǍʇςÁн²϶҉ӬьŜɗƙҔϤĽˤѱГ',
                                                                            'ρȼʔúӷтЉ²ǿ/!Ӑ,зǥъөŲÕƃӍҤҺæΨϽĨľŦ϶',
                                                                            'ǮʟϕʙӻMÎŃȯˎƛnřɅˈй\x86řʂʩÔǀ;Ů3ɷɊeàˮ',
                                                                            'ʕʓtÆȘȧ2ЌɋŭΈԓίɗůĞӠͺ\x80ʆȡѧȆӖʡ÷ѩŅɁɼ',
                                                                            'ԖЮӓϟԓN\x8eǚύЙƶȍȵö\x80YĖ˃Ζ¸˹ʸČΕĵ$Ȫō\x9bш',
                                                                            ';ȸϟӍ˞@ņԅμȽȲρζΉƒĿӹάԍԍªϨ°ΈҒ(ʿĄW\u0378',
                                                                            'ǜӅ҃ΊȮǰŴ\x8bц\x94˕ƸƼƪùɕЛ£ϾЯƜȃƸ%ʈòͺ\x8eô˚',
                                                                            'ǗæȦƼҿϼǻͿ"ˎɵ\x99ӥМ\u038dҦԔΠʚĥ.ŅқyˊЀǟǜƕѣ',
                                                                            '·ŕŵʕǾˎƏþ¼ұĪͿΎơɚʫĴɘИөÿԎϷΊ\x99ңӲɒС\x9a',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ВěqвО',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            9624.30609710708,
                                                                            667286.4152676507,
                                                                            792134.8575501511,
                                                                            996443.2451910218,
                                                                            808934.7780570716,
                                                                            318264.7459603847,
                                                                            684836.125292528,
                                                                            837358.2000996072,
                                                                            622790.3899357669,
                                                                            -21905.695623502863,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸæӣŮčĈìƈʿ;ԕŢë\x94ɨӿӃɦьǢϣч˜HŘƂϵ-ѧҷ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 177626.6113455639,
                                                    },
                                    },
                            {
                                        'name': 'ĵȩʛΚȺЙӔoΪҎĝʗǍÀΐѳˠ\x9dΣɽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2518590050421272899,
                                                                            -6358962105791293600,
                                                                            2712551724085032289,
                                                                            1358665956311877546,
                                                                            5127905136909063556,
                                                                            5552399027707780712,
                                                                            -5306290383898278639,
                                                                            -4914708581385202361,
                                                                            -4771280763125601252,
                                                                            -5732274813393397733,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ċǷЕƲѪ'Ⱥ\x81ʪ°҂Ъɾ\x8fЦȐ?˅CͰɳÍÕ҃Ŕ+іԦθ҆",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164111.778321:+0000',
                                                                            '20210224:164111.778334:+0000',
                                                                            '20210224:164111.778342:+0000',
                                                                            '20210224:164111.778348:+0000',
                                                                            '20210224:164111.778353:+0000',
                                                                            '20210224:164111.778359:+0000',
                                                                            '20210224:164111.778364:+0000',
                                                                            '20210224:164111.778370:+0000',
                                                                            '20210224:164111.778375:+0000',
                                                                            '20210224:164111.778380:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ГǝΝ\x83ό˔Ѭơͼϋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164111.778585:+0000',
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
                'identifier': 'σþƴˆӓ',
                'categories': [
                    'configuration',
                ],
                'error_message': {
                    'catalog': '\x96ϙ',
                    'message': 'ˑ',
                },
            },

        },
    ),
]


class SetLocaleEventTest(unittest.TestCase):
    """
    Tests for SetLocaleEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_LOCALE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.SetLocaleEvent.parse_data(test_data)
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
        for test_name, test_data in SET_LOCALE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.SetLocaleEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_LOCALE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='SetLocaleEvent'),
            ),

        ),
    ),

]


SET_LOCALE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'ŖкΨӱÀȏǜ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'š',

        },
    ),
]

class RegisteredTranslationCatalogTest(unittest.TestCase):
    """
    Tests for RegisteredTranslationCatalog
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTERED_TRANSLATION_CATALOG_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
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
        for test_name, test_data in REGISTERED_TRANSLATION_CATALOG_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTERED_TRANSLATION_CATALOG_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog_name', name='RegisteredTranslationCatalog'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_codes', name='RegisteredTranslationCatalog'),
            ),

        ),
    ),

]


REGISTERED_TRANSLATION_CATALOG_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalog_name': 'Ê8ԐёɉήˮƕǇűϲʛγǆʭқԧǽƃѼÝ˳\x9c\x8bLʼ0ϐŖ˹',
            'locale_codes': [
                '÷',
                'ѵ',
                'ԡоīɼ',
                'ˣͶłĿҕˋ',
                'ďʰƏſŽˁ_',
                'ŻΩ˛',
                'ÃËʠoҪҘƈŁϓ',
                'ȁ;ßӭА=Ԙìɘ4',
                'ӂ/ħǌ˾Ŗőν',
                'ԩϚȗȜѠоĹϩϠ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ʲƔŚ',

            'locale_codes': [
            ],

        },
    ),
]

class TranslationsStateTest(unittest.TestCase):
    """
    Tests for TranslationsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in TRANSLATIONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.TranslationsState.parse_data(test_data)
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
        for test_name, test_data in TRANSLATIONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.TranslationsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


TRANSLATIONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalogs', name='TranslationsState'),
            ),

        ),
    ),

]


TRANSLATIONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalogs': [
                {
                    'catalog_name': "ЭϞë'\x8aџ˨Әϻ\x9aʼɐƉΞӈǙŰ\x97ȨïĻГwѱϕкϝϜ˕Ÿ",
                    'locale_codes': [
                            '\x9eΎƗɅwɽɶ',
                            'ʔ\x83ʕ˾ӼЏø',
                            'ƴ_ȃ',
                            'ǲЅÕϭêɷѳ',
                            'ʊÞӞѻɔĸҬ\x9f½',
                            'А',
                            'Ŝ',
                            'ɆЂ˯',
                            'ҪĲҮЫǵý',
                            'ι',
                        ],
                },
                {
                    'catalog_name': 'Ӥ*μ[ćѻΈФфǰ˭ɺʌУȖ˅ːÆʔԉϺґɎψϷѮóƙϲŲ',
                    'locale_codes': [
                            'ƛ\x94Ïіʓõ',
                            'ӯ\x82ϟȁϱ>ZÊ',
                            'ŅʢӨйƎćǤʬƢ',
                            'ϚŔȅ',
                            'ϦĒЄƽӐӱ',
                            '\x82˰Ѭç',
                            'ŀԞȔ\x86ͶƇϹȁҒԘ',
                            'Čŗ*ҧñѢź',
                            "ӿͳƉǄЖХƎ'",
                            'ӫůȆз҅`Ԩ',
                        ],
                },
                {
                    'catalog_name': 'ǭЪӀΕAʪëјɻȦЈɹќȂǌʲɽΐǀƀɊϼā!\x99ƹѱнŰэ',
                    'locale_codes': [
                            'ũʈ',
                            'Ҋҹ\u0379ŞŁφ˗',
                            'СȨ¼ȃКǋ',
                            'ɬ½пӶ',
                            'ϐȏ²^ȭiw',
                            'ԉВǙÂƁ˘Иǚ',
                            'Žψ',
                            '˷´ȠˍʩϜ',
                            'BɒЅʉ',
                            'á\x98·ʝ',
                        ],
                },
                {
                    'catalog_name': 'ӺʐҕÐĤƿʅɯƸSӟ¤ʆɆҹ˄ʙʣңʇқζŸǀXϺЍʲɎé',
                    'locale_codes': [
                            'Μ',
                            'џџâςʸқҕ',
                            'ĭҢŠЁ',
                            'ԣ',
                            'ƍ"Ӽ',
                            'ԮǷĳëʕƚȧ',
                            'ҢŷԖ',
                            'Ɋˎ',
                            'c',
                            'ҐxɊˤԓ҄',
                        ],
                },
                {
                    'catalog_name': 'ŜԈšʗƄ©ʭȿ1ȻǃϢǞѺȱ÷вͲȑԄǴǕϯҴÍ˞Íǘʾԑ',
                    'locale_codes': [
                            '\u0381æuoǎϻ\x8c',
                            '˞ǖԦ˃ʼɯ',
                            'īʫΞϻą¤Ɗ',
                            'ÖÃϣԛȯ\x8dӋũӬѧ',
                            'ѫʬӴ˧ͲΔɼî',
                            'ØбаЂӦɹš',
                            'ɓƹʽ',
                            'ԍ¡ˍȨ',
                            '6 0Ƀɒ\x7fǑƗɕ',
                            'ο¿ǸśŮ҉РŒ',
                        ],
                },
                {
                    'catalog_name': 'Я϶ƝЮˑҫʛƊǺ˪īӸYӺѯʽ\x92ʕ¥˗ļîГҕϯΨƴÈ#Ӓ',
                    'locale_codes': [
                            'ȃɩҫ˕ƖѨ',
                            'Ċ',
                            'Ę҃]ψΦʸҩƴǘȢ',
                            'ɇȾΨɀĕҽԕjј',
                            'ΪПʀѕǦɗêǼЮ',
                            'ʟ\x91ƴіʎάƱӜЎ',
                            'ȅɬӭϚĠ',
                            'wɒӞԋѸΘOȍҠ¹',
                            '*ӏψЄ{ɡԝԜě',
                            'ǟʧŅ˕ǁ\x80ήӱδż',
                        ],
                },
                {
                    'catalog_name': 'İùЭϷ˩ˑäƂΫϙӌЂſψLϸţШÄӣЂͼΆĻʡϹɤʬŸԏ',
                    'locale_codes': [
                            'Ɂ5ʞ˵',
                            'ҦŭѠƊρпű',
                            'ơolɜθˀѲȅ',
                            'ºѪˏɰЄň7ӣ|Z',
                            'ʹʏИїѼ˛Ԃ',
                            'Ѯ˾¨ŽЁȼ',
                            "ǹʽɰGωÉҝ'˖Ϩ",
                            'ǍŬθɎʜǆӕ²',
                            'Ƨ˯π"еƢʃѲʐ',
                            'ӹБЊ˚Ǖèȯ',
                        ],
                },
                {
                    'catalog_name': '@GεȂԟƜsğuɌņϻ2˗϶ϑӋѫɛϘɂ\x8fǚȺÛѿӠгюĺ',
                    'locale_codes': [
                            'Í',
                            'Ώƹ',
                            'ɯҩӣ˛˱ɁͶʻРą',
                            'ÈĚǒɣӯçӵѼ',
                            'ͻʸԤŏı',
                            'ҷэ',
                            'ğџóН',
                            'Ąǧ',
                            'ЙʊπЅ\x9eÅǲ',
                            'ǫęʙ',
                        ],
                },
                {
                    'catalog_name': 'ВXŎ\x9fŚĺšҗӸ¼ʷԏ\x9dэɐЛ˹ϒȢӥЋȝǪԡџʎЦԭ-ѷ',
                    'locale_codes': [
                            '¬žˆ҇ˣ',
                            'ƫ˧ʹƔˮ',
                            'rĘ',
                            'N΅˧ҽɽȚ',
                            'ѥэҚŰ*\x8bƆ',
                            'Υźɮ˭',
                            'ԉ˝ˮҋŵϤǧȾɧ',
                            'МƷ',
                            '+џљ',
                            '϶',
                        ],
                },
                {
                    'catalog_name': 'ˠЅȀЋϐϫƁǲʟȝˌĢрVƪʸčŌĉνȮѡHϱȎƵɅφҶĶ',
                    'locale_codes': [
                            'Ǚ˲ȡјťƀ¬˂˲ˮ',
                            'Hï',
                            'ыҳλ\x89˞ƥ',
                            '˹˚A9ƳǛt\x86ӿʸ',
                            'ûŐνϦʱԐˡĮ',
                            'ìķ\x97üŋTӽ',
                            'ϧǛˏЂǇəIʓ˅',
                            'Ǡ˞ϩɛ',
                            'ŨȩϋΆіɡȬєǌƕ',
                            ';ϹˑˣԚɯА',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalogs': [
            ],

        },
    ),
]

class LocalesTest(unittest.TestCase):
    """
    Tests for Locales
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALES_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Locales.parse_data(test_data)
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
        for test_name, test_data in LOCALES_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Locales.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALES_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='Locales'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='code', name='Locales'),
            ),

        ),
    ),

]


LOCALES_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ǷūҚɇ×Ōљ҂˛ӖҰ#ƫƋ6йĳȎ˦ĒДȱòԐϚˮDяˆư',
            'code': 'ѭʌӑçhӲҼ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʃ',

            'code': 'd',

        },
    ),
]

class LocalesStateTest(unittest.TestCase):
    """
    Tests for LocalesState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALES_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalesState.parse_data(test_data)
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
        for test_name, test_data in LOCALES_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalesState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALES_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locales', name='LocalesState'),
            ),

        ),
    ),

]


LOCALES_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locales': [
                {
                    'name': 'ʬÔΓӧѴЗΧӏқǑʟɐkϷģ',
                    'code': 'Ɠ\x95ȥУҸϫұ=ƌ÷',
                },
                {
                    'name': 'ƦǛƅѥǬĲƤ˴ǟWҬȀeķƊӴȧʓd ϔʲѣ˸\u038bςҥќǭÜ',
                    'code': '«',
                },
                {
                    'name': 'gþБЮьA϶Ѫ\u038dè˦ȭ\u0380ӳǋƣɸћûUɝ\x84δϨ΅ŸЏυȈʘ',
                    'code': 'ÂȌǗÖѤӁћ',
                },
                {
                    'name': 'ӝçƇҠԚ\x96Ѯ¢Ѩ\u0383҈ӪΙǪˉΎѢ÷ɜüǅ\x86ÔιԈɦӪΞƤЧ',
                    'code': 'Ӑ˹]Őӌɗ',
                },
                {
                    'name': 'ͽ\u0380˻˩ӍaʬɛƩɶϞſцәŝӲԌAƁφǊ˷˧ƚƸԁʬȦʞq',
                    'code': 'ȜӥȏǄɧʟόӭ',
                },
                {
                    'name': 'ĶрǹvqΜӿ]ŹГȄķϕςΡщ˹ɸɀқӊ½ƀɵȥ˷ʍŮʏь',
                    'code': 'ʮ',
                },
                {
                    'name': 'ˑȦě\u0381ԣӿȰƂ1ĆзǂԍaƯȷӤҖɍӯѬɗ\x91ʎԡ6͵ƃőщ',
                    'code': 'ȄҔʕ',
                },
                {
                    'name': 'ΒӰĆӗїûͷҏþʽѱϷ\x83РÎȩ\x9fŕΠӑѝҨÚȮѷŔιȕӦγ',
                    'code': '҉҇ѡĖ«Ƅǹ',
                },
                {
                    'name': 'ȴɻχԕýϥĥȸҙƿûȰ(Ƹȓ˔ˋǵEɣþiǜ\x99ΨʺȭҀ˵ʇ',
                    'code': 'ʨϵǪѳɻ-ƟşȠG',
                },
                {
                    'name': 'ǴʘFҬYТ\x92ȋfɇΒ\x96φ>Ԓ\x99˱ƣѢЦϐԦIʭӊΘìɼƹʪ',
                    'code': 'ōα',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locales': [
            ],

        },
    ),
]

class ActiveLocaleStateTest(unittest.TestCase):
    """
    Tests for ActiveLocaleState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_LOCALE_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.ActiveLocaleState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_LOCALE_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.ActiveLocaleState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_LOCALE_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='ActiveLocaleState'),
            ),

        ),
    ),

]


ACTIVE_LOCALE_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': '͵Ґѩ*',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Й',

        },
    ),
]
