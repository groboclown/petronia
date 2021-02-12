# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-11T17:55:50.635155+00:00

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
            'x': -3255585887371016507,
            'y': 4956442046294592939,
            'width': 130798848432091162,
            'height': 974033247280085079,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': -9095224300274628850,

            'y': -2653889736419392306,

            'width': -3244931236457211163,

            'height': 7301902689283914042,

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
            'key': '¿\u038dѝѩ˕ˣÏӶͱ҃ơȮŃ`җӵήͳȼ*ЄΔBȵҋiдňnϬ',
            'value': '˹ýŻɪΆɺѵљëǙ',
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
            'focus': 9410,
            'parent_id': 'ӝƛɕѭ҃ƱԡǇPωӁȭԚɾɟ\x98њĢ!҇ęǢЙ҉ŪāΖљĆň',
            'flashing': True,
            'location': {
                'x': 1946429221264677987,
                'y': -6985744574387706084,
                'width': 2180128779486809162,
                'height': 1631840709158610593,
            },
            'minimized': False,
            'meta': [
                {
                    'key': 'жǢԙıĴƴԩÙЋ˼\x86ʦÖŕә\x9cԈЅmʐǹQóѹûTѱӷ"ȕ',
                    'value': '\x87zЭʦ6ʵͶϡӫѢςʱԏ<ǈ˞-ϞťéɕéњƪAαфĊђϨ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 2240,

            'flashing': True,

            'location': {
                'x': -167095323495200956,
                'y': -4520092111443923291,
                'width': 2119280293228030828,
                'height': -1543779597963552223,
            },

            'minimized': True,

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
                'active': True,
                'focus': 1489,
                'parent_id': 'ĄΓȻ\u0380ɇˆҺĴiƭѻʇϢ˹œ˶Õҽ˗Ԫ_ϡŴ0\x8aƍȵÉžԠ',
                'flashing': True,
                'location': {
                    'x': -4688697512530720624,
                    'y': -6239089703849059108,
                    'width': -4867731839085946069,
                    'height': -4865072611366750611,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ưқȢʂәϢ˜ԝХ ӎҮΏhɱӓѻƁΠǝņʢɟǣ`ʨÞҷәԌ',
                            'value': 'мŇϡԆҾҭ2ŊԩUßіë˲zǥͷ\x94ˬӎ˹þōΏɽΦґɻǁI',
                        },
                    {
                            'key': 'Ͳʷźɚ˳ЎțȗŰaˠЂ9˷ӰĸƎϪëĻȗϴĄԆҪÜΠłʠИ',
                            'value': 'ŵԡȹäfϗʣžϙʲ\x87ų˷ʹЍřηʿʦƐȅϷȄſˍĀʿ\x82ԑ˂',
                        },
                    {
                            'key': 'ЛŲ´āÐĝϫЬǢŉκ˔ӬȻΚӧûԖ¹˃ӖͼΌÜɁǼͺцԧѵ',
                            'value': '8ԪʚЉ\x82/ҊȈĒҵɲǰŭ',
                        },
                    {
                            'key': 'сǱƠϙтӲҲßȄFΧ˭ïҙ»˨ȃɈЭȟȮĥĦïʴøĝқςʁ',
                            'value': 'ҀÛϊάϬȓʃѕƨʔѯLnҚǄӖӡåӆĞɳѸĞ˨\x84aӦºţȇ',
                        },
                    {
                            'key': "ҤēʖѾjďӰ'ʫÝЫȃʶʹKɔV7ǟʹϱƹΆďȸМΘХԇӣ",
                            'value': 'ɇЮʞҸȀάMǚkѳȌγ÷ȌɢӔĭтŊќŎԇȕԪԍŊØƏлD',
                        },
                    {
                            'key': 'ȩҫιӱԨ˨ǮʁʸÏŶ˓ѷќϩ*\x9fϚβҝќqΎʓƙ°В',
                            'value': 'ÁƦǲΜӳї3ÖŽ\u038dϵӗļͳŉҢǰ8ɓ;ͷQhô>ΨɠϹѤǰ',
                        },
                    {
                            'key': 'эˇΖ\x84ԇ·Ҳϭ#ԍ¡ŷňξΎӹBæ˾\xa0ЕǚҥԜ\x98$Ӆќ\x99Ǽ',
                            'value': 'ȷcΓϫţԥx˭ѯʹ£ӿqȔë\u038d\x9bЧγĉў˒˞Ľǿτ\x91\x8dżӽ',
                        },
                    {
                            'key': 'ɁӉőѩмҥNђϹΡɋԑζӽδ˖ӀшĴEʁлƾæΈŌηòЉѸ',
                            'value': '÷ĽȬӋΉªʃѨԬƕěƃԖΘқ6ʂĺʰσ¬ƉȚʺ{ŷҺзӲΜ',
                        },
                    {
                            'key': 'ħПɽˡŻσÐĒԞöǆÍǞȊҮȋӈĥ7ƸώyȫԀ»Щɜѭ´ϝ',
                            'value': 'ԝ˗Ƞȵ˂}ǢδӾҗΤļɥōŬǺǷǺ\x87ñʌǬϩҝŐ\x9dʑπɏË',
                        },
                    {
                            'key': 'ԣƵƂþ¨ĂĲ¨ΒřÖѿЩȋʗġʃèюӝө´ʗԑɉġǇ©ʫӁ',
                            'value': 'ʅҫÁĒбĲϢǷʖɬЌχӂ|ȸӻʃ¡ΟĤӍŒWƝOҢɜːʅĢ',
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
                'focus': 9939,
                'flashing': False,
                'location': {
                    'x': 8712698157836090254,
                    'y': 3136566803449657586,
                    'width': 8734783256083763455,
                    'height': 8258886119634271255,
                },
                'minimized': False,
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
            'reason': 'ɵӾĘƳΚDԑǬϕâŦ·ЁʜyĊЂҿϞş\x8bćȜЄV\x94˼ԕӯĶ',
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
            'window_id': 'ϪǈˢŖüŵ\x93˪ˉϩʼɐӲÄʮήӯŵѢΣà˴ӾȖʼɡăşӦʾ',
            'location': {
                'x': -5357339385116329146,
                'y': 333874107703468304,
                'width': 4962744832537098931,
                'height': 6760968866702341290,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ȲǔɀǦԇ',

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
                    'window_id': 'LϚCԐLӸƤǿȶ˃˺ԩҼ=1ѯÔŝŇŴɽÁ\x94ÑŉӋɏəxą',
                    'location': {
                            'x': -8253193713533216159,
                            'y': 4586194849841080124,
                            'width': 6355423641992136964,
                            'height': -732010352995256065,
                        },
                },
                {
                    'window_id': 'ҿɨUϙʖĈцǉΡ˘üӵʻÞωȬȿƪƍҖ˳ʿƝӷ\x85˩˵ÂƸȏ',
                    'location': {
                            'x': -8490780274513424990,
                            'y': 4048452323529664623,
                            'width': -5258921959991021602,
                            'height': -8296176788979690412,
                        },
                },
                {
                    'window_id': 'Ƭ΄ѻȇǆɚԏǉƪɘӅ\x98ϼϲţˑ\x7fȠҰǡ˪s1\x86Ιȣ',
                    'location': {
                            'x': 9168995490416318082,
                            'y': -142709989540436840,
                            'width': 4046293972693532824,
                            'height': -2663812364904984612,
                        },
                },
                {
                    'window_id': 'ˈĊêʹɁѪɤҌĎɥϪǎȼ\x96ǽɖ˃ӢϓĉЊóɅӸ˘ĢԏƢπê',
                    'location': {
                            'x': 62021078178723608,
                            'y': -7649228752214223819,
                            'width': -2004939052319577839,
                            'height': 5047161781222818873,
                        },
                },
                {
                    'window_id': 'ÀвķǰǾƀŰʂˋαΌԀёäʓβɖǊԙԚʰϖҰзɢȻѦКʼ˖',
                    'location': {
                            'x': -7440966540663122055,
                            'y': 5884749433132947111,
                            'width': -8917232522067973908,
                            'height': 5412472763465930700,
                        },
                },
                {
                    'window_id': 'ƾώƛɿяM҂еϾǣʾԃƵǖҜԁȤϻϾΉ\x81ĨȔԫ½\x92ɄͲϘ%',
                    'location': {
                            'x': 209751812198748491,
                            'y': -5547832194695455283,
                            'width': -5551966095634629861,
                            'height': 547385041534433080,
                        },
                },
                {
                    'window_id': "ӅȾӾϽΊʚԫɁŜϺŶғĞȃԩƶȄUŢĔАȜ'ɛ\u0379ĜίЍɻȟ",
                    'location': {
                            'x': 6461073424083579957,
                            'y': 3713049738027852544,
                            'width': -4038243278736471754,
                            'height': -868434056690184785,
                        },
                },
                {
                    'window_id': 'ýĸӮǩºт',
                    'location': {
                            'x': 5568602089009207400,
                            'y': -6110210010029439776,
                            'width': 5954797999011488717,
                            'height': -4647996430130548097,
                        },
                },
                {
                    'window_id': 'ІӎɗɷˣˑãÇˊГƊҺԘԚɱʆѷєԫбЬˬŽΞɩЦΉȿÓɄ',
                    'location': {
                            'x': -3995911440313581993,
                            'y': -623770953697898085,
                            'width': -7223173936736212936,
                            'height': 5266915469975049918,
                        },
                },
                {
                    'window_id': 'ƖԋӍԤïb½¾ȣǬӀțԒѷƥÈÎ"¤OǑŷĉƏ\x91ҝÞΕΎƑ',
                    'location': {
                            'x': 2217686154544157347,
                            'y': 4693897284906492050,
                            'width': 7432454061287520398,
                            'height': 5699509258105392562,
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
                    'window_id': 'ĉΡȦϾѾ',
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
            'window_id': 'Һʴz\\ҫî\x81νƫ{ԜӐԡǘmӎцàӭІ΅˵¿ɒñ\x7fɠǹ',
            'keyboard_focus': 3908,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ӋðӈBͷ',

            'keyboard_focus': 829,

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
            'on_new_window_click': False,
            'on_new_window_enter': False,
            'on_window_event': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'on_new_window_click': False,

            'on_new_window_enter': False,

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
            'window_id': '\x9bаӫ:Ƙ\x9dϖŴϊ҂uИЌoԦΡ=ԛùщɆĉϝQЌҿάχΠҚ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ȋɏ˾nȽ',

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
                    'window_id': 'ūŌʬŠЂƿӅʟҌ˜ͽĪˈƿƧʸˋŖȯӭʫʭƴɶxЮˈɆmǦ',
                },
                {
                    'window_id': 'ѰӨŴӾłԁӳєѵʁǠŚjλǽӊҍԣQԧҩƳÑơҗŎʍӏΉѻ',
                },
                {
                    'window_id': 'Ҥ»ӫ\x89˲ŴεȖŏȓ҆ŷԘΔЌ±ϵϬәȔßįŉϫĞ·ΚʀÙ˪',
                },
                {
                    'window_id': 'ǞǡǳԡɛŊӇ\x84Ƅǟ˔ϧΊβΪѡɫҸӽ+ƴѸόǼɴ\u03a2\x84δ҉Ȥ',
                },
                {
                    'window_id': 'ȗѯҰԢƕÕùʐƩӶӓͽƣŶƏХ°҉eұνʋ˰л\u0382˰ˁʛɏΆ',
                },
                {
                    'window_id': 'ɮʶҥĔїĘθҦͿǲӂPʮйφƆ\x96ĦƬԎπ\x93ȔЪʺҁċȼԆΐ',
                },
                {
                    'window_id': 'ͷŶƯưûrÂΥǀŰÜμБӐԟǗφϽȳ\u0379ӏϯԊ\x90ʦΪĚǿʨҎ',
                },
                {
                    'window_id': '˃ѦԥΎКн¹ƀÖΧү҆\x89ӅʴǞ%ϼҀȴӕӫЯԃŎӱʹϸÿҼ',
                },
                {
                    'window_id': 'Ňæ҅ˋĉƕҶńь\x93Р\x91¸ŋƩɷͼãťÓԍðɬƊӥΟӒѢВľ',
                },
                {
                    'window_id': 'ЀǴљɮœӲɔʃʩ\x98\u038dɡˁͽ',
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
                'ǮҁǨ×ŢYҘѐË˗MэɈιϦȀĿǸø¦ІҺĭÛǄԁаЕ`Ɔ',
                'Κ\x9eȜҜϕčҾԣӤƬӭʵφǩ}Ѝ²Ȭ#ЧȍȽҢƟȆ6Ýƭάў',
                '\x84Ӹѣѵύɤ˷ĂĪԒKѺ>óǞɔ˪ȺɛЊ§ȇɜÒ8\x9dѱ\x87ɕǁ',
                'Ԓ°BТψ˒ҭ¶ԤɊ\x90ǎǰ{ŻƖӧĿъĘzƞɂƉ\u0382тĚÖϱƿ',
                'ȎEǠǟʍАĂĺͳҿâ˪}ĞТҭԗĬȳƄȹ˜ҕˬɞ\x9cδʗρѼ',
                'ҏxƋҟɛưÔЎӀίɮӶĲͶϬ,ǄԘм˝дɘƥԟƗЈӻȕӸW',
                'ӮӊЎо\x9fδӈȱ\x8fź_лͲǭѦ±ˬƳǪǒÌśԁӚѝȟҎƈ˨˓',
                'ʅŃȉƮԠþ\x9fǥÛԃӬЋǏ·δʱƣζѦťȺѹϙz¡ƤΒԞʞɢ',
                'Ҷɸ\u0381ǯ>ő`ʆ͵ë¨ЋʳɌĚͳВιɽŶѿљɀεԖƕʭį\x89ӟ',
                'ʔңȦűÞȮŽǄѱĸ\u0378ʑÝϰ¤ӮσԭƳâ˳ɖӄ¾ѡ}ŪӍҠʅ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                '7ĝȡƧç',
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
                'focus': 2805,
                'parent_id': 'ӷɌ¦ÌwÞϒҒˑʃ1аˁԑ!öϲԦкќ\x7f҃\xadñưСӶѵҝʽ',
                'flashing': True,
                'location': {
                    'x': -3683133155105478285,
                    'y': 3317443353562750707,
                    'width': -8597759976706269284,
                    'height': 6387409046063553711,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ĞűgƩ©',
                            'value': 'ʽ˷оŃˀɀȈӽѩθӃǑǿçŅʆÝMМϙɞӉ˯ΣЧԚЎШԮŠ',
                        },
                    {
                            'key': 'ƃəщѼϹ[ƶǃˡʫБ*\x8eϹЛƿƇϘ¾\u0378\x98˳ӫˡȄëǺĭԓͽ',
                            'value': 'Ҕ±ПӕƸ4ʢѥҿʇñӋΨȻб\u0378Qʫσ®ШΪʰĸæ¾҆Е˥Ɵ',
                        },
                    {
                            'key': 'ɪ\x93Î˛ý:ԆӍҋԐ,Ƙ¨ɝͼĄŝϻŪӊΟҤű\x91bǳɳԁȽÝ',
                            'value': 'ѼɦӅγΘƦ˄pƃȾӗŘƐȊäïœ˃ÕȷҾԉцƥӛ\x94ŁҝƆӡ',
                        },
                    {
                            'key': '˳ҩӃÎĆƀþʅҲ,ÚÙ\x90˖ˊcjʱ\x9dxǉΣǬϥД42˜ǐѬ',
                            'value': 'ʹȁʓΉȂхŉ˼\u0383ŤˁĭңάεѡφâӺ\x99ԊŹԉÌ\x95ЇƉɻӵй',
                        },
                    {
                            'key': 'ǹάȯʏŔѳĔҌΤgԝ',
                            'value': 'Ҫǒ1ˏϡЯō˹Ν\x96ΈȖһгÐ0ϝЍҒҡ¡ǨĪʓЊϮΠωĨà',
                        },
                    {
                            'key': 'áЧOԭŽKЧǢ¨ϠȂΤ\x89ΒƛϝSĦαȬѬѢȬ¤ԊĮŋɻёƂ',
                            'value': 'ɷұĞõҡӁâϫ-ɛ҄|ōOǝ\u0378ϣ¶ǚěʹ˺ċεˣ΅ӢɭŀĊ',
                        },
                    {
                            'key': 'ϴŜȟȖ˄˕ЍҰǙІʙ3˨ºңŏĄΔОȰ˛ČŻ˳ӥѠđǜ[ϒ',
                            'value': 'фȻҵçҎ\x8dÅӌʝĨǨƘΝũȟȂԮԊXʑĜ9ÄǮīĬ@ϑSˑ',
                        },
                    {
                            'key': ';ŨŠϭƂÑȒɻĽ\xa0ϥƋӉĲñ\x8cԙƉŔ΄Τѕ\x9dŜʅĹ҈ѣśǹ',
                            'value': '˖пъŪԕұ˓ȬԒǷAЊҍѮЬ΄ѽśʃȪҟǐЋΗөɹэŐʚ˧',
                        },
                    {
                            'key': '˺ȓXź\x92ĹΜƸlȀԀȅǋ»ȓ9зáňәҞâȴɎåƶĩϤҋо',
                            'value': 'ƹɼʧ>ūμ¯ћȘό˭ʽҡ(ĭúӸϣpҚ\xa0ģҏɱ˾ˤƎѥѳд',
                        },
                    {
                            'key': 'сċщȶώçҐŜ\x90ΑƗϺĲɢДΣ˴қÁ˫ΎĩGԡȺDϴӯӆķ',
                            'value': 'ŏôдɡōǔԥԙ\x9cʡϲ˝˓Ӌҿ˫áƶƧ˩ͺŋ˷ǘϋǜѡҘȊɴ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': False,
                'focus': 8815,
                'flashing': True,
                'location': {
                    'x': -1705975919502540941,
                    'y': 3413356187869659124,
                    'width': 5053724399412767192,
                    'height': -2979776806876531995,
                },
                'minimized': False,
                'meta': [
                ],
            },

        },
    ),
]
