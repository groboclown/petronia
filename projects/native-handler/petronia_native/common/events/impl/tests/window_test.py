# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-12T16:50:56.970535+00:00

"""
Tests for the window module.
Extension petronia.core.api.native.window, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import window

class ScreenDimensionTest(unittest.TestCase):
    """
    Tests for ScreenDimension
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SCREEN_DIMENSION_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ScreenDimension.parse_data(test_data)
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
        for test_name, test_data in SCREEN_DIMENSION_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ScreenDimension.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SCREEN_DIMENSION_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='x', name='ScreenDimension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='y', name='ScreenDimension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='width', name='ScreenDimension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='height', name='ScreenDimension'),
            ),

        ),
    ),

]


SCREEN_DIMENSION_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'x': -4419283558594305860,
            'y': 5336830132737931694,
            'width': 5265243736270122871,
            'height': 4580184549132637025,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': -2059505037226732224,

            'y': -4623814361386582646,

            'width': -8141551923602722598,

            'height': -6451840982256416175,

        },
    ),
]

class MetaTest(unittest.TestCase):
    """
    Tests for Meta
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in META_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.Meta.parse_data(test_data)
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
        for test_name, test_data in META_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.Meta.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


META_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='Meta'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='Meta'),
            ),

        ),
    ),

]


META_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': '!іҿѦ˫\x88Ϟͽǐȣ_ĒσҵҴȦŴýѓǓ\x7f`Ԍ-ǱƃƂȴ9ö',
            'value': '¸˘ЄӦS@¨ɹʹҧʑѩÔӸɝŪõ~ΘˁʀʃԔȆȕԐԋΰЛƘ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': '',

            'value': '',

        },
    ),
]

class WindowStateTest(unittest.TestCase):
    """
    Tests for WindowState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowState.parse_data(test_data)
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
        for test_name, test_data in WINDOW_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='active', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='focus', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='flashing', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='minimized', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='meta', name='WindowState'),
            ),

        ),
    ),

]


WINDOW_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'active': False,
            'focus': 4590,
            'parent_id': 'Õ˛ȁȓéʹȫΪԐѕϓȂΩѠǚ˓ԐŜҀÃџ˝ͼũͻӐӜɇȔͲ',
            'flashing': True,
            'location': {
                'x': -630333197042246772,
                'y': 5287266871795959769,
                'width': 8237064020221800087,
                'height': 535970567665830613,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ÀÐǁΎӈɿҭ˴ʚѿЬή˴ˢ˖ƠƫґőƊ1ϱʣӹºӳ(ǒɩÛ',
                    'value': 'ĳӫͶѾцŃκȐӿøӘђļŴӥΦќ´Ъ©ұzūʢŘÑ˴ɗԝӹ',
                },
                {
                    'key': '˄ҝϚʰҖҺѝ˲ǺȰΧǙEŹҋˋрҵʞɤƄѾÅǟч¾҅ǔώÞ',
                    'value': 'ðŁ×Кԡ\x80гPbȈ&эϒʾ',
                },
                {
                    'key': 'ΩīϰƯԒȂ˂ƀȺŻûďīnҹĂĴɀãƐʛƛƝЈѦĎςћFԚ',
                    'value': 'ˁͰˊԡaĉ¡ώΏ˧ʮ@IэǙΖɩåΎ',
                },
                {
                    'key': 'ӫĿɇǫαƮƨȭ˥#ҺűɮSPВžʄ[ɔәǅ\x9bϱʖ2ǑёƠğ',
                    'value': '+ӔāӸҼ\x8eӱÃ˓ΖžʆѿɳҋɅɃĹё°ϸƢҌέɗҺʧͼїų',
                },
                {
                    'key': 'ˇÏɓԗǢԍǵɨӞÓɚЏƞːҿͷɦƌíâёӒȔǂšGЭѴF\x93',
                    'value': '˽ĄҰ÷ƫҰɃҟ˝÷Ȩ<țϹӲǹZtİʸi¥Ǐ\x9cӘÏʓɡӢϙ',
                },
                {
                    'key': 'Tǧ\u0382ǄΰӏÖɁļǒUԊΞπɎLʃ˝Ԟү_Īţ^ԝЛvř¨а',
                    'value': 'ΊɦɬΑԌ˱Yɫɋθ¾ƢԐοƋ_ЇҨÁѷƟϞƎƭсϦƯӽѩ',
                },
                {
                    'key': 'ďϾŪ˓ǡƓнøȍnˍɡɲҭҡϭǐʹˠȿʯƘːιʉΊЪīĈ=',
                    'value': "\x91\x9aɥ\x95ͱɹҢƧ'ÖƘ¸Ϋ˹ŔҔϰǛĩāť˷uͺΤҢöʂ҃ƫ",
                },
                {
                    'key': 'зʧʬȂ»\x83АшöǠӀƝyǟϋɔѤΪсϢTƪȧһȩ˝WÚȣG',
                    'value': 'ͰέxţѤЕɞԢ˔ӽɜӧҘζʐиtӨǟÃɪCű=ƙû˜ƿЈӃ',
                },
                {
                    'key': 'ȽӝːˮȊ\x9b¬ɶϾΔӔҠρҵüǠ˾gǖģěnіEɡAɭԅrǇ',
                    'value': '\x8b^Ϊ¹ǕʋКԑͺǠӹĭǽϙɞԧ®',
                },
                {
                    'key': 'ƦџӨŎҰԒΔŲȧʘӽӝЮőƱԜΓҶ¦ëϭʅƳҏʑ˺ˑ¬Ȳd',
                    'value': 'кƘǙԉʄĎҒџхŚ˹!ȂʏʾÞʔʆčңԆƩ²tȑɗĦDȍɥ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 3467,

            'flashing': True,

            'location': {
                'x': -552405449048534887,
                'y': -2530054469622519915,
                'width': -6593270913857765798,
                'height': -5388030672058803598,
            },

            'minimized': False,

            'meta': [
            ],

        },
    ),
]

class WindowCreatedEventTest(unittest.TestCase):
    """
    Tests for WindowCreatedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_CREATED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowCreatedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_CREATED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowCreatedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_CREATED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='state', name='WindowCreatedEvent'),
            ),

        ),
    ),

]


WINDOW_CREATED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'state': {
                'active': False,
                'focus': 8272,
                'parent_id': 'ȷáíП˺gǗԡɆͳ˹ƳxİԧƩ.ĳýԭWʚȆϽ1ō\x93υ\x86ȋ',
                'flashing': False,
                'location': {
                    'x': -7905458922069561610,
                    'y': 1303780142690009763,
                    'width': 816021223187183564,
                    'height': -8837557488029119985,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ȒʙžʹųͿŵƓΜéВ \x7fÉŗԎɕǁӤśκͱTʭӴ˹ѿҷăσ',
                            'value': 'ψЃȈˬŒ\x8dϗƴҤυϏ˭îŶӌȢǖǧOμËϯԧԃ¬ɖȟ"ԕԩ',
                        },
                    {
                            'key': '\x86ÖťҌƥӉɟгȣϋǒџӧԡ;џɗʆπϕɬƜЕЙƊҸɅӤʪҽ',
                            'value': 'ӵ\x81еɔPƯ¼\u0380Ŝɡʳ\x9dԂȗȦǷтƻɥёɏƅϳ҉ʂƍЪʱōȂ',
                        },
                    {
                            'key': '\x8bPϴͳϼƛϮӽōŃоJ¡ϲąÌϵɀŨѮX±ɸɓОƸƅİĮŕ',
                            'value': 'ηƊxʥѩƅνæή´˟p˰ιīϻ\x81ΔƁсæÎѡъӌфΎΪ',
                        },
                    {
                            'key': 'ɅкѱÁјЯұхΗΆҐͼйÝĊЏ˝ĪӟǇғ²ƀò˓εŧїRϕ',
                            'value': 'ŏФӥѺɜʯԞlҴ\u038bŶаm¿ĉÈƅˏϔˎϞԋÖŬ\u038dɰχӛϭn',
                        },
                    {
                            'key': 'ȌЯэ!ɹѢȹƻŰƃʢƉӏǹäūѝƗɀҿӞDÌāǏǳʯʩ˂ԛ',
                            'value': 'ĸÕӕçώҚЬ"ʛԚɊɴԗȫʾ»ȶϖБԂÓuƚŞӃҼԗ ɫ\x87',
                        },
                    {
                            'key': "Ļ˲ƫӍʺ'ʮʉĈήcŹϋvЀȤҬΔϝѲɠҋԂ\x7f\x98ѢɖðƲʓ",
                            'value': 'ȏɞȟӪҸϓQɶҖǔјϮҜpҍ϶ǈ˷Ň\x80Ԏ¥HʆƂŧ#Ҩȭˤ',
                        },
                    {
                            'key': 'ƿѲӇʌΤбѡøξϚ҉ƍ˭ŃųÜɗOǾɀȐԚ˖ǡêԞ¨ϛϑĨ',
                            'value': 'W\x87mσҵǤǠͽ˔å΄ΒǉāåȡщήɢęǼԨÜЎԙϙƽυƚȔ',
                        },
                    {
                            'key': 'ȃѷeŻѤėǒŖ˰ԜǊҳӭͺǸѽˊϲӜ\x87йԔҝ\xa0уԢ\u0380Ȅӊʗ',
                            'value': 'ԢЕ±ĢĀ\x81ҥŭώʲƯʠέ˗ӾȫvŜȁ\x88ΆǤ˳˨ϮӧʖɪϮѷ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': True,
                'focus': 3948,
                'flashing': True,
                'location': {
                    'x': -2390560073407644671,
                    'y': 4463576875867560239,
                    'width': 3053214887672731119,
                    'height': -2491111575784489414,
                },
                'minimized': True,
                'meta': [
                ],
            },

        },
    ),
]

class WindowDestroyedEventTest(unittest.TestCase):
    """
    Tests for WindowDestroyedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_DESTROYED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDestroyedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_DESTROYED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDestroyedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_DESTROYED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='reason', name='WindowDestroyedEvent'),
            ),

        ),
    ),

]


WINDOW_DESTROYED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'reason': 'ÀĔλɚʹϥҘO}ȬҜȗОƘԩĸрͶӎĝÙȵʐɏӹϋѐѿʴΕ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'reason': '',

        },
    ),
]

class WindowIdPositionsTest(unittest.TestCase):
    """
    Tests for WindowIdPositions
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_ID_POSITIONS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowIdPositions.parse_data(test_data)
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
        for test_name, test_data in WINDOW_ID_POSITIONS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowIdPositions.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_ID_POSITIONS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id', name='WindowIdPositions'),
            ),

        ),
    ),

]


WINDOW_ID_POSITIONS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': 'ĭ\x9fӴɲʬÎŢœƾȝӖɱӂɿ\x9dǾѭԘˈʖŁԩӍǌèĕŘуϓǏ',
            'location': {
                'x': 1537351892468563729,
                'y': -769803705797089400,
                'width': -966402847157265231,
                'height': 6966464297209904355,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '\x86ҿѷºȐ',

        },
    ),
]

class SetWindowPositionsEventTest(unittest.TestCase):
    """
    Tests for SetWindowPositionsEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_WINDOW_POSITIONS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowPositionsEvent.parse_data(test_data)
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
        for test_name, test_data in SET_WINDOW_POSITIONS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowPositionsEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_WINDOW_POSITIONS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id_positions', name='SetWindowPositionsEvent'),
            ),

        ),
    ),

]


SET_WINDOW_POSITIONS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id_positions': [
                {
                    'window_id': '5ɅņĚȋɞ\u0383\u0379ѱ΄ƥIõŮӷǅFéѰȷ±ɾЂϻΦɋ\x87Ŷ\x7fӲ',
                    'location': {
                            'x': -7438947280333345968,
                            'y': 1973115347698102905,
                            'width': -9080482034393049450,
                            'height': -3906237215961612876,
                        },
                },
                {
                    'window_id': '˭Θ7Τу[Ёʮ©ʶҚʶėÇȿӯwƽЎėūǸǤԡӊǦӭʵԨ\x82',
                    'location': {
                            'x': 2832315872053897045,
                            'y': -8472217013479972097,
                            'width': -360644188242081098,
                            'height': -5797987391760078969,
                        },
                },
                {
                    'window_id': '\x84ƂĀЎ\u0382α.҄\x97ԛǺӌ\x8fĨҰǗҼ˻ЖŏʦśΒ\xadʫƼ]ҾȺǁ',
                    'location': {
                            'x': 4777239671902331145,
                            'y': 3532072579370562744,
                            'width': -3257034764362466881,
                            'height': 6718193443876002658,
                        },
                },
                {
                    'window_id': 'σѤӺΚŗɋιźęǅRΝŜͽеÛŏрԡ\x83ђêÑϩȂҟȩeŃэ',
                    'location': {
                            'x': -8450283354043915446,
                            'y': 2926649250009381565,
                            'width': -8947452466887627029,
                            'height': -2495482165492771974,
                        },
                },
                {
                    'window_id': 'řȠɜuƃ±Ӆyҙ҅\x9aЧϵͶԜԚђâϖґçŚǄǴ˱΅Ǝúӳґ',
                    'location': {
                            'x': 4975915600570641660,
                            'y': 3998204004139151196,
                            'width': -4254107524452593345,
                            'height': 469516814388460616,
                        },
                },
                {
                    'window_id': 'ǂͺȵϬƍԨ»ЊŃƪΒłżìȹ΅oѧѳűӊʥɀԧǈĚ{\\Үƹ',
                    'location': {
                            'x': 7507681289269611628,
                            'y': 1802197571115013189,
                            'width': 5839404299913341487,
                            'height': -5937186960911771482,
                        },
                },
                {
                    'window_id': 'ŠȂÁ˖ӈиǢě-ɞ˵ǀ7ŋʹƅÎˉˌьРƷ·ΠȂŗИҥʫΙ',
                    'location': {
                            'x': -3051424764290748494,
                            'y': 6249623324219277666,
                            'width': 6487940190392546488,
                            'height': 5621069338317163428,
                        },
                },
                {
                    'window_id': 'я¾ԨӦĀƁIАЇfƮΎ\x93γAĚ·ϽɆƍϏŢхϏ\xadÔΣϏҙ˦',
                    'location': {
                            'x': -4617705264862546987,
                            'y': -8546889315375253987,
                            'width': -5544520162902973099,
                            'height': -2292306121335094034,
                        },
                },
                {
                    'window_id': "WΓʺ£^ɗʖļҕȐ¿Ļ'¼ȓȔš˩˝ʄωӚǛӅʥѦȬȾƠϕ",
                    'location': {
                            'x': 5837784688146969078,
                            'y': -6262003312704891521,
                            'width': -7669197414402142447,
                            'height': -5550095183429585808,
                        },
                },
                {
                    'window_id': "čврєůщĨӴϬ\x95ƩÀѪӚǁĂīӁҬĚɢ.˅¾їǧǸ''ю",
                    'location': {
                            'x': 6506525873966710052,
                            'y': 6064926320607571601,
                            'width': -7984460398071302230,
                            'height': 9183058970168891330,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id_positions': [
                {
                    'window_id': 'ǤɄǴʽǽ',
                },
            ],

        },
    ),
]

class WindowFocusedEventTest(unittest.TestCase):
    """
    Tests for WindowFocusedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_FOCUSED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowFocusedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_FOCUSED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowFocusedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_FOCUSED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id', name='WindowFocusedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='keyboard_focus', name='WindowFocusedEvent'),
            ),

        ),
    ),

]


WINDOW_FOCUSED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': '[ïқӆџº3ɕȿăћԆƊПӵмΗļˡOґҒ1Мȷ˖h˩ůЗ',
            'keyboard_focus': 8155,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ȠȑВ˙Ʋ',

            'keyboard_focus': 2699,

        },
    ),
]

class FocusSettingsStateTest(unittest.TestCase):
    """
    Tests for FocusSettingsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in FOCUS_SETTINGS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusSettingsState.parse_data(test_data)
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
        for test_name, test_data in FOCUS_SETTINGS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusSettingsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


FOCUS_SETTINGS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='on_new_window_click', name='FocusSettingsState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='on_new_window_enter', name='FocusSettingsState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='on_window_event', name='FocusSettingsState'),
            ),

        ),
    ),

]


FOCUS_SETTINGS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'on_new_window_click': True,
            'on_new_window_enter': True,
            'on_window_event': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'on_new_window_click': True,

            'on_new_window_enter': True,

            'on_window_event': True,

        },
    ),
]

class ActiveIdsTest(unittest.TestCase):
    """
    Tests for ActiveIds
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_IDS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveIds.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_IDS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveIds.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_IDS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id', name='ActiveIds'),
            ),

        ),
    ),

]


ACTIVE_IDS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': 'ßȈͺӛϐʳƐʵѨɞßȝϫ\x86ËЧǴɰʹԏΩɭźӍ\x85ŦȲяϞЅ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ԈÌԈɢϓ',

        },
    ),
]

class ActiveWindowsStateTest(unittest.TestCase):
    """
    Tests for ActiveWindowsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_WINDOWS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveWindowsState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveWindowsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_WINDOWS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='active_ids', name='ActiveWindowsState'),
            ),

        ),
    ),

]


ACTIVE_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'active_ids': [
                {
                    'window_id': 'ʈɽɐĵȳǝғɑσǚɞђɝǰƿϨÐgƯςƮҩʌþ˞\u0379˰#ˣӂ',
                },
                {
                    'window_id': 'ʙơÄκɡ^ҞЦʄŖϓ˗џŉϋ҃ɘ˒гѲČɭųżŻÊÊ\x8bɑӔ',
                },
                {
                    'window_id': 'ҐΗύԗƁŻĬԎŖ+ǋɔİʪʡ˴þˮ+\x84Ԧ˗˓˒vŁ!ʋ΅q',
                },
                {
                    'window_id': 'ӝňRӉңɎĩΤæ˾μ\x8aǈȓдʁҷΗǟѭԋĄҞԘΛΑʸɖ˖ы',
                },
                {
                    'window_id': 'í×ӽї\x8fǃϏņϩҢηĭÛήѐ)Ř3ϴ®ɊǞčŋǱǚǸɃȸ\x83',
                },
                {
                    'window_id': 'íњƏƈԪeΜȪőGФɘǫȏ\u03a2Ӽɩɒ\x8a7ɅЄ¸ƩЉO;tų\\',
                },
                {
                    'window_id': '˙Ѵ΄ҙ˒ͳѲ¹ЗҍϕӽčzȍɀĠ³ɫǼȭϻƊĪэǃǯWèљ',
                },
                {
                    'window_id': "Ϝ\u0382·ˎò\u0382\x8cρɘÛǊÓӼ¢Ӱɕ˟PʳǄ\x96ӑη'ńњƠʘýҙ",
                },
                {
                    'window_id': 'ŘҼȾˉѡ\x8aŉ(6ŧȻѲĹͰs˝&˄ŲϢқΚPţ\u0378ÃĜȥʄǹ',
                },
                {
                    'window_id': 'ɮʶԎԫçɕƂӛЯнŤʉɻԎĠ\x80ͽ\x9eɠȄδʮǏКʈ~ȧʄǩЇ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active_ids': [
            ],

        },
    ),
]

class FocusedWindowsStateTest(unittest.TestCase):
    """
    Tests for FocusedWindowsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in FOCUSED_WINDOWS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusedWindowsState.parse_data(test_data)
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
        for test_name, test_data in FOCUSED_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusedWindowsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


FOCUSED_WINDOWS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='focused', name='FocusedWindowsState'),
            ),

        ),
    ),

]


FOCUSED_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'focused': [
                '˶ŒďŁhʲơˀIΠϡиЄǘϊ\x96õ8ѷŕȁž˩Ϯ\x8cǣǉĲӥ.',
                'ҤǣҺЩ±ÌаȦȚøéưπƚ҃РԠÏҁŴ˯˴ԃÍ҉ϰЍаѺԪ',
                'ƷēɦαӉёжȻϡ҅į˘ЗӥȰкБѺéЅ·řĶʄÕɈǯҧЊӺ',
                'ʭ˟÷ȈĮÛŤƬʒǴтʤѽӣӦ;ņAĆτԙϷЛɻӣӼζĝϬĠ',
                'ЭȇԆͻΔ˗',
                'ɖεоĺäҤƚɆӦ7Ǎ|ǦˏɮƠƟхƆǼƘӴʐȅϦ˄ƺαĈҽ',
                'ĜΌЭϣäӬϮƚҳϡӷúĮ\x82Z³ҭ¤ΚkяǅǔƧÀԜӭjĝɺ',
                'ʸ˵Ʊ\xadfǤéɻȹ\x8fӷgӪΉ˔ɀǻǶϧˇ¯ʍζЕ\x95Ϗ\x9cŽмζ',
                'óȟҩ¦ȆĽˋУҭìȲӁĭƐɩУˏӭȥœɼ\x98ӜãƦƭɫȪɨʘ',
                'ӢǧʣΗȨCӕɬϰĸ"ӯʤӫȕQƚΔ˦Ƶ˯ʌÁшʤȦԭŠÓӜ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'έЪţ˻ȕ',
            ],

        },
    ),
]

class WindowDetailsStateTest(unittest.TestCase):
    """
    Tests for WindowDetailsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_DETAILS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDetailsState.parse_data(test_data)
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
        for test_name, test_data in WINDOW_DETAILS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDetailsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_DETAILS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='state', name='WindowDetailsState'),
            ),

        ),
    ),

]


WINDOW_DETAILS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'state': {
                'active': True,
                'focus': 3591,
                'parent_id': 'Ȭ×҅ќǌ͵вԠȤӅͱsʛȊΐz˩έӪƲŵǯɤLӮØΗâl˓',
                'flashing': True,
                'location': {
                    'x': 5590377175766399875,
                    'y': 3809338338969369991,
                    'width': -3482628242001871851,
                    'height': 6164142574383368191,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'ȇЦǜάhˠ͵zѧȵþʊǜąνƆ˪®ҖʁкʨʳѶ9\x87ЉӘӨԙ',
                            'value': 'QԄΞʊĪϒӈǓĵ˄ɽͼЌȵѵĭŹƸ:ʊӔљ´ˠƿƶȩʭ˽Ç',
                        },
                    {
                            'key': '˞Ѵ,$ѡɟĕ#ĶƽСȾŶӲ˓y^іʹĄ΅ǋgÁĎҝ˪ę%ť',
                            'value': 'ƂʿªÑēǳăı˦ӦˁϐНΆǉȒſӳҚѦԉѪȈÅĜƷЁ˾Ԇϲ',
                        },
                    {
                            'key': 'әƅӵŐϲȩЎđÎҺĵѥΦԎ\x9eɔˬsȸҞҗѩśǷëȟɨūϴƚ',
                            'value': 'пһϐ\x9fˆɭȫϚƭɮȫĺбîȏȡά`Иґĩ\x98sѓўƻʙàΤ»',
                        },
                    {
                            'key': '˃ãȱӋӞѠѿΧӦ\x89ΎɲЭԝĀЇ',
                            'value': 'ʑԄϤӳˍŹʉόίϕӲԗΎĜҙƽʰкԮŠүŋúҫȲ¹ӟÔʺȶ',
                        },
                    {
                            'key': 'Íɥ\x95{҉ԘĔӝxůyӼɨϊ?ǩЛʏƨϽǑ}ěșĶϣΎǣϧȜ',
                            'value': 'ǄӦǚɌӴӘ\x89Џȴ\u038bщǭӚʔ·ǡɃƶΐĲĳјɗ¤˓RƦұÛĚ',
                        },
                    {
                            'key': 'ѵȜÒíʪɊ',
                            'value': 'ZũɄɲΤřÍЧĬʆџɛƞҦľęѯЪH\x98Ɨƻ\x92Ġͱҁ Ͷɼы',
                        },
                    {
                            'key': 'ͳǙұ&їϛɢ!yҰ·ӤӀȨĲǆÔȊůƓ,.ĘˠЕФģˏӹ8',
                            'value': 'ǈǁƵǏқ\x9bɳƽВľʃЏЯҡˬ˳ŅȍȁϒиОǗ҄ŗӕ˷ԇʿɾ',
                        },
                    {
                            'key': '˱Ђϛʤȳԓ˙ˏʷаҍӇϘϠʃ2҂QϳÜѠÃѕä˜ȅ+І}І',
                            'value': 'ï',
                        },
                    {
                            'key': 'ɜӟӝƵ!¼ũʳ˃ʞӜǸʈ5ƀђŏԄƤϟӎß',
                            'value': '~şҢΤ\x96ϳκȾǣûШ©ɻȮϲеѢʴӼҢƦɸȿƧƳʶƕʘ˜Ҽ',
                        },
                    {
                            'key': 'łǔΏȼªʒ΄£ӌЌҳı·ύӑԐȠłɘǣΡСбνʢԖƢzè\x87',
                            'value': 'Ɏĉʌѻ˥|омɀњéɲ˗цˌø˕ȔĢƽɅƤԟйһӕʽʂԏ͵',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': True,
                'focus': 708,
                'flashing': False,
                'location': {
                    'x': 7533619059537806151,
                    'y': 8553338790027779015,
                    'width': 4561026808083013805,
                    'height': -8243257501822154950,
                },
                'minimized': True,
                'meta': [
                ],
            },

        },
    ),
]
