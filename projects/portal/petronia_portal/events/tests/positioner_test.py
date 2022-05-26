# GENERATED CODE - DO NOT MODIFY

"""
Tests for the positioner module.
Extension petronia.core.api.ui.positioner, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import positioner


class VirtualWindowTest(unittest.TestCase):
    """
    Tests for VirtualWindow
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in VIRTUAL_WINDOW_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.VirtualWindow.parse_data(test_data)
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
        for test_name, test_data in VIRTUAL_WINDOW_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.VirtualWindow.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


VIRTUAL_WINDOW_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='desktop_id', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='pos_x', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='pos_y', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='width', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='height', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_west', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_east', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_north', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_south', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='minimized', name='VirtualWindow'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='keyboard_focus', name='VirtualWindow'),
            ),

        ),
    ),

]


VIRTUAL_WINDOW_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': '1ӠȋяŢӈˤ\x8aĝƧīҒЬÎĪÔɽɱȃϦ¨˒ˏŕ\x83ǱӐӱȴʗ',
            'desktop_id': 'ҁѨJҳƌê¼ƆGʗãӷ}ǒï˵˄қńÂÂïħΨѩчӍӝʫǭ',
            'pos_x': 2029189,
            'pos_y': -5595690,
            'width': -4035763,
            'height': -3197596,
            'chrome_west': 6502796,
            'chrome_east': 4945832,
            'chrome_north': -1368403,
            'chrome_south': -3040188,
            'minimized': True,
            'keyboard_focus': 589,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '|ĢȒεƲ',

            'desktop_id': '~¢Έëҁ',

            'pos_x': -2641310,

            'pos_y': -4485930,

            'width': -3675644,

            'height': -3365018,

            'chrome_west': -5440359,

            'chrome_east': 9156322,

            'chrome_north': 6942976,

            'chrome_south': -1415012,

            'minimized': True,

            'keyboard_focus': 2412,

        },
    ),
]


class WindowUpdatedEventTest(unittest.TestCase):
    """
    Tests for WindowUpdatedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_UPDATED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.WindowUpdatedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_UPDATED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.WindowUpdatedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_UPDATED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='settings', name='WindowUpdatedEvent'),
            ),

        ),
    ),

]


WINDOW_UPDATED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'settings': [
                {
                    'window_id': 'ĴϻňӢҗΰŰH˱\x85ÙʄԆűΟθΐȸǹϿrǁ1ΐɏǻ˰ƛӍŵ',
                    'desktop_id': 'ōˆϓ\x93ĊÓԗƛʘлҔҷБŷµʭΖҹѹ«ŇҌőюʈƎƐΥȦȃ',
                    'pos_x': -4692320,
                    'pos_y': -543417,
                    'width': 9533565,
                    'height': 8293455,
                    'chrome_west': 1285947,
                    'chrome_east': -5876578,
                    'chrome_north': -1907861,
                    'chrome_south': 2780506,
                    'minimized': True,
                    'keyboard_focus': 6790,
                },
                {
                    'window_id': 'àǛǳÜ?οўÖöћƤҧοÀɓӔƇĈˁ÷ƴÇι˱\u038d¨˦ʵS"',
                    'desktop_id': 'ĕÜʓѰҁπҦкƱƿьɧZƊŬVȬ¢љǽɽǠLEЮлϵΤșŧ',
                    'pos_x': -2919874,
                    'pos_y': 8107019,
                    'width': -7901558,
                    'height': -8301406,
                    'chrome_west': -3303119,
                    'chrome_east': 9596268,
                    'chrome_north': 8419943,
                    'chrome_south': 2761709,
                    'minimized': False,
                    'keyboard_focus': 6177,
                },
                {
                    'window_id': 'ϼʞǔҧʲӌˌԓʐͷʙĘЃҳUˬEӊѹQǶÊҝ¼ƘɚΉǧńɧ',
                    'desktop_id': '&ȿȇ϶8ԏҳˍŢȲԭтŭħԖɫƪªʕåǼɎΚɝѸПɛϗ˂и',
                    'pos_x': -6257480,
                    'pos_y': -3398986,
                    'width': -3348148,
                    'height': 553399,
                    'chrome_west': -5085617,
                    'chrome_east': 9043966,
                    'chrome_north': -6331240,
                    'chrome_south': 4526265,
                    'minimized': False,
                    'keyboard_focus': 4454,
                },
                {
                    'window_id': 'ɥXЌџЌɛЄʆұŚϸʉΆІǝҁɭ\x80LŐɞFǌӼѿɱԎӋѴю',
                    'desktop_id': 'żʘĞԣΙɨӻ',
                    'pos_x': 5988838,
                    'pos_y': 7269434,
                    'width': 9268331,
                    'height': 1701905,
                    'chrome_west': -6981811,
                    'chrome_east': 3376791,
                    'chrome_north': 7650718,
                    'chrome_south': 8330534,
                    'minimized': True,
                    'keyboard_focus': 3749,
                },
                {
                    'window_id': 'fǎÖ5ԥІŦΪѧ.ǰ\x97ƂкӒı˗Җȋɠѥ¤δʆҬ±ϰƜθм',
                    'desktop_id': 'ϊêÐˌќɉ͵εќВӂҁȐmøʎѰEŚ\\ˉĆʞȄřеԟгƸѡ',
                    'pos_x': -2105232,
                    'pos_y': 5759812,
                    'width': -6988547,
                    'height': 4826125,
                    'chrome_west': 15673,
                    'chrome_east': 9770525,
                    'chrome_north': -7171785,
                    'chrome_south': -8408277,
                    'minimized': False,
                    'keyboard_focus': 2753,
                },
                {
                    'window_id': '΅ҞΫNʀӊҍ˭ŔίïΒ\x86ƿƬųςŻśŶѵʐ˧ġӭʣƝ3γɉ',
                    'desktop_id': '»HɂιԑʹˌŖʞëDȆáӢϧаӭʭƟŇșԪѫɎȸҧgӠ϶Ģ',
                    'pos_x': 7908235,
                    'pos_y': 972048,
                    'width': -1626100,
                    'height': 7194926,
                    'chrome_west': 7018538,
                    'chrome_east': -4356962,
                    'chrome_north': -5451539,
                    'chrome_south': -363243,
                    'minimized': True,
                    'keyboard_focus': 659,
                },
                {
                    'window_id': 'ϙƥÍȸѓÉІ\x9bðáΰȴ\u0380ďʊEԅˣfʶЏõˎǩʨΧѬȦУl',
                    'desktop_id': '\x93Ù\x8fѾŭͺǢ5ʉĀ\x87иʸ7ȁҰ˘ʻēyºӘ¦Ŗ΅ǆˀԜ\x90ų',
                    'pos_x': 9750312,
                    'pos_y': 1226349,
                    'width': 8176930,
                    'height': 1572347,
                    'chrome_west': 8615789,
                    'chrome_east': 4489498,
                    'chrome_north': 8695217,
                    'chrome_south': 5954705,
                    'minimized': False,
                    'keyboard_focus': 1696,
                },
                {
                    'window_id': 'ҵǤŬΧƶӀӯǠ×Ͷšƻɺ}ӭӧрԔϱӲ(ɉºũάԃɃ;Ӝţ',
                    'desktop_id': 'ɆƊӲôШђѺ\x80PϘБ!ĩȴщʐǥцϫʵċ\x94âÕχӤx҇íª',
                    'pos_x': 9828590,
                    'pos_y': -3760294,
                    'width': 5058395,
                    'height': 3253050,
                    'chrome_west': -2161033,
                    'chrome_east': -3238246,
                    'chrome_north': 3984074,
                    'chrome_south': -6479220,
                    'minimized': False,
                    'keyboard_focus': 2494,
                },
                {
                    'window_id': 'ˑnǩkòóɬʚ¿ÊȅƾԖãҕʣǢůŮҝĸʛΙϖͻќˢƓΑѭ',
                    'desktop_id': 'ɜģϝħҤ¬ļЛɿӧĚȫǺǪɉɣǆɤ,ʑїÝӒǅŞђǺ»ΜƤ',
                    'pos_x': 1958061,
                    'pos_y': -8236039,
                    'width': 5714443,
                    'height': 8622899,
                    'chrome_west': 257319,
                    'chrome_east': -8352185,
                    'chrome_north': 4433453,
                    'chrome_south': 4411427,
                    'minimized': False,
                    'keyboard_focus': 2167,
                },
                {
                    'window_id': 'ӕʃϰӣɲǝѱҟѯ¤ĶŚӱłƖȼόиҖӋŲϷéМ˽.ǸÃƸƿ',
                    'desktop_id': 'ӭhԐͷ\x85ΪʀԨěϡкz\u0382ɶʐ˺ѥϷȕƨȣYO³ơӺї\x8f\u0379Ȳ',
                    'pos_x': -4912000,
                    'pos_y': 6269754,
                    'width': 1297259,
                    'height': -7677052,
                    'chrome_west': -5491456,
                    'chrome_east': -2363623,
                    'chrome_north': 3762824,
                    'chrome_south': -3893762,
                    'minimized': False,
                    'keyboard_focus': 837,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'settings': [
                {
                    'window_id': 'ˎƻӄνҠ',
                    'desktop_id': 'ĥŕУ\x85ϋ',
                    'pos_x': 9492787,
                    'pos_y': 9533887,
                    'width': -3313699,
                    'height': 6323663,
                    'chrome_west': 7774811,
                    'chrome_east': 9472643,
                    'chrome_north': -6333249,
                    'chrome_south': -9759453,
                    'minimized': False,
                    'keyboard_focus': 7252,
                },
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
                res = positioner.WindowCreatedEvent.parse_data(test_data)
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
                res = positioner.WindowCreatedEvent.parse_data(test_data)
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
                dict(field_name='window', name='WindowCreatedEvent'),
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
            'window': {
                'window_id': 'ӞTԞéиNIЖʄi˪ʈļԒƝ˕ΆҘƳƻƑъǈ˻ƠԐ1ɼϣԅ',
                'desktop_id': 'Ѵϒҡȑ˧Ëԗɇ\u0383ϹĪҹʣȐԋtӌƗјϝѭgθ²ȆžЅd\x80Ӳ',
                'pos_x': 9592167,
                'pos_y': 7269090,
                'width': 1194772,
                'height': -6441992,
                'chrome_west': -1751027,
                'chrome_east': -6269010,
                'chrome_north': -5308507,
                'chrome_south': 1314881,
                'minimized': False,
                'keyboard_focus': 6876,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window': {
                'window_id': 'ӕζҚˊƇ',
                'desktop_id': 'Ƅȿ:ȭ¯',
                'pos_x': -2831889,
                'pos_y': 1742694,
                'width': 4622527,
                'height': -7685792,
                'chrome_west': -4697590,
                'chrome_east': 5330379,
                'chrome_north': -4467507,
                'chrome_south': -7544129,
                'minimized': False,
                'keyboard_focus': 4386,
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
                res = positioner.WindowDestroyedEvent.parse_data(test_data)
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
                res = positioner.WindowDestroyedEvent.parse_data(test_data)
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
                dict(field_name='window_id', name='WindowDestroyedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='desktop_id', name='WindowDestroyedEvent'),
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
            'window_id': 'ƈѝvԗ¡ǄҠӘˢɱTĽξ*ңɞZҍ¾ӣSα\x82ңǍƪƿ˫ԋQ',
            'desktop_id': 'ѵˣçķXˮ\x80ҺĻʣʙҢķNʯάèȕfƱгøʤϮоĨũǭГȂ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'Ѷр©ʇя',

            'desktop_id': 'Ā҅ԡЂӵ',

        },
    ),
]


class FocusWindowRequestEventTest(unittest.TestCase):
    """
    Tests for FocusWindowRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in FOCUS_WINDOW_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.FocusWindowRequestEvent.parse_data(test_data)
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
        for test_name, test_data in FOCUS_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.FocusWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


FOCUS_WINDOW_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='desktop_id', name='FocusWindowRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='keyboard_focus', name='FocusWindowRequestEvent'),
            ),

        ),
    ),

]


FOCUS_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'desktop_id': 'ԠϖӽÄгϾeьϞαМǋѕɱԓÒϙ\u0381èŒŦрʃӷƱӖŀƚȂƽ',
            'keyboard_focus': 2569,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'desktop_id': 'ΉƎŷ˹ƺ',

            'keyboard_focus': 6547,

        },
    ),
]


class MoveWindowRequestEventTest(unittest.TestCase):
    """
    Tests for MoveWindowRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MOVE_WINDOW_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.MoveWindowRequestEvent.parse_data(test_data)
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
        for test_name, test_data in MOVE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.MoveWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MOVE_WINDOW_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='desktop_id', name='MoveWindowRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='pos_x', name='MoveWindowRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='pos_y', name='MoveWindowRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='width', name='MoveWindowRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='height', name='MoveWindowRequestEvent'),
            ),

        ),
    ),

]


MOVE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'desktop_id': '\u0378ȊʄɎcˮЃȚӧҴƬ˜ʪÛƮćΗţԡ҉ĦΩäĆЪɝǥċ9˄',
            'pos_x': -1386760,
            'pos_y': 5919622,
            'width': -5909885,
            'height': -7856964,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'desktop_id': 'ƒɊ,ԁϊ',

            'pos_x': 9542800,

            'pos_y': -5810912,

            'width': 6549671,

            'height': -1576286,

        },
    ),
]


class CloseWindowRequestEventTest(unittest.TestCase):
    """
    Tests for CloseWindowRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in CLOSE_WINDOW_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.CloseWindowRequestEvent.parse_data(test_data)
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
        for test_name, test_data in CLOSE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.CloseWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


CLOSE_WINDOW_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='desktop_id', name='CloseWindowRequestEvent'),
            ),

        ),
    ),

]


CLOSE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'desktop_id': 'èžǡʖʟζ˛ȩϵҀ]ЦǗʥɡCGʑ6ԁÕɷȎЌӖӞɒӯԤ˽',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'desktop_id': 'ϘќӇϱȎ',

        },
    ),
]


class SetWindowChromeRequestEventTest(unittest.TestCase):
    """
    Tests for SetWindowChromeRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_WINDOW_CHROME_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.SetWindowChromeRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SET_WINDOW_CHROME_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.SetWindowChromeRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_WINDOW_CHROME_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='desktop_ids', name='SetWindowChromeRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_west', name='SetWindowChromeRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_east', name='SetWindowChromeRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_north', name='SetWindowChromeRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_south', name='SetWindowChromeRequestEvent'),
            ),

        ),
    ),

]


SET_WINDOW_CHROME_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'desktop_ids': [
                'Ӧüќj¼ыσƎШҫόċŬȊŧŮїĳѐмӤ\x93Љǘ\u0378ʪʵʛȽʐ',
                'ӻɂπʕʣƣ\x98СØΞɧΚĖˇӧҤòЩɄӛgΑ¨Ԑ\u0380ýΜĄѝɓ',
                'дƘƑŪȇӕЛ"К¡ƹǽӂźΪȓˆӅȈ\\Щ}ɠ\x8cΈ҄$uʞĂ',
                'цͺԛĕԤUȌԒғǁқѫԕǲѡńȀŤΕ-ǐЩΚƂ\x94ˌѰ]ιð',
                'ɐǶқĴ\x9a\u03a2Ű˘Ʉ;*nɸ}ԃ͵\x83\x8aMʆҺÝʉȠӎɲʯɊ°\x89',
                'ίʹϫƟӈϤϭԏӝȹȂĐʰƁɿǗ˹˾ʲϡȸͽ_ďԍšҺKӝɎ',
                '(ȿȃϿȂƜÿȸҚ¨÷ǟҧTɊ\x86ȮɶʴώӦȲӄіԍð˷ʪ\x9aσ',
                'ʢδκƉӽѣʨ\x84˕HCƎȒѧҽԭƞϩÁˠӎDƑΆʺȠϾόЗѺ',
                'ȎʦӞƁЄƩ±˛ʞɉԑǆ\x86ԁ<\x8dѤЬшʴʒŁђȈԛʠӎï\x96Ĝ',
                'ҖЂŀƷʠьӠɑӇѣѴԀěľѠɳΦǽω\x86ƉżĺˢИŨǻ)ċʿ',
            ],
            'chrome_west': 4390740,
            'chrome_east': -7159564,
            'chrome_north': -4976057,
            'chrome_south': 7012527,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'desktop_ids': [
                'Ώʦ˽ԇґ',
            ],

            'chrome_west': -5005574,

            'chrome_east': 2000112,

            'chrome_north': 8886138,

            'chrome_south': -9322707,

        },
    ),
]


class SetGlobalChromeRequestEventTest(unittest.TestCase):
    """
    Tests for SetGlobalChromeRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_GLOBAL_CHROME_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.SetGlobalChromeRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SET_GLOBAL_CHROME_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.SetGlobalChromeRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_GLOBAL_CHROME_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_west', name='SetGlobalChromeRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_east', name='SetGlobalChromeRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_north', name='SetGlobalChromeRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_south', name='SetGlobalChromeRequestEvent'),
            ),

        ),
    ),

]


SET_GLOBAL_CHROME_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'affect_all': False,
            'chrome_west': -7658749,
            'chrome_east': -4209701,
            'chrome_north': -9171517,
            'chrome_south': 1561472,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'chrome_west': 6005721,

            'chrome_east': -4656591,

            'chrome_north': -7559986,

            'chrome_south': 6066672,

        },
    ),
]


class SetWindowSizeStateRequestEventTest(unittest.TestCase):
    """
    Tests for SetWindowSizeStateRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_WINDOW_SIZE_STATE_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.SetWindowSizeStateRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SET_WINDOW_SIZE_STATE_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.SetWindowSizeStateRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_WINDOW_SIZE_STATE_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='desktop_ids', name='SetWindowSizeStateRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='relative_size', name='SetWindowSizeStateRequestEvent'),
            ),

        ),
    ),

]


SET_WINDOW_SIZE_STATE_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'desktop_ids': [
                'ǝj-ҔԛʲάϬ\x92ӕûʥĘʉԦʌѸˋӜӂфҫɋkԅøǓŏƆ',
                'ȠŹГɦÄðȃ«ĎӠЕüɘǔҨεϴΕιʣƿϫͶԀљγƙã÷Ǆ',
                '˦âωÂԤ×Ɵ.ɡǇɾïȇԞƝӼȜԁԚŕӇĴȢҳǰȉƤҿԝĵ',
                'ĝʈŘкÞɥҐƠǲʦǬwɁ˭Ƿ¢ʛҰЈρԉξ\x86ϔӏƽ\u0380ҝғC',
                '΄ҭųmÆʖʖҡɅЦǮȃƌεɰĤȕӺȒ0\x94ʆĸЬȽ¾®ƩȾК',
                'RӬƕҮ\x85Ǆǌ\u0378ǌ°ҋP˫ԁĲˈЕȘОƟ\u0383їϻeγyλºʏƊ',
                'Ԑ˅Ґ×ԢɥӸŤѧȺЫԕʷϟ$¤Wɔ¤\x85Ƕ˺Ѱ˝rϳʗǕêʐ',
                'ӛˊδƒЯȐȇ7ҹϹǣȮͺȅɍȯѢǶðSȞό;ƣƨȭԎԞ\\§',
                'ć˴µϝǝƂ[ékëӬԢŮĔËõơӗ%ˋѰό:ӫ(Ԡ¸Ñͽť',
                'ƻҒȞýīԓȈɱӅ:ƝĝѬʸӸѧiҭ\x8cșƗ˫ЦC˅ωϚ˪Ϟʓ',
            ],
            'relative_size': 'restore',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'desktop_ids': [
                'ŌĢмȈҼ',
            ],

            'relative_size': 'restore',

        },
    ),
]


class FocusStateTest(unittest.TestCase):
    """
    Tests for FocusState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in FOCUS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.FocusState.parse_data(test_data)
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
        for test_name, test_data in FOCUS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.FocusState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


FOCUS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


FOCUS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': '@_Ԝӏ$χʹӶˊŖśӐǊƊҸǌҝ#Ҡ6đŸŏҌ˸Ƚe˓ɭȉ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

        },
    ),
]


class DefaultChromeStateTest(unittest.TestCase):
    """
    Tests for DefaultChromeState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in DEFAULT_CHROME_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.DefaultChromeState.parse_data(test_data)
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
        for test_name, test_data in DEFAULT_CHROME_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.DefaultChromeState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DEFAULT_CHROME_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_west', name='DefaultChromeState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_east', name='DefaultChromeState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_north', name='DefaultChromeState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_south', name='DefaultChromeState'),
            ),

        ),
    ),

]


DEFAULT_CHROME_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'chrome_west': 4824402,
            'chrome_east': 7356763,
            'chrome_north': -5750519,
            'chrome_south': -6191246,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'chrome_west': 9855505,

            'chrome_east': 9443764,

            'chrome_north': 5516622,

            'chrome_south': -3231861,

        },
    ),
]


class WindowsTest(unittest.TestCase):
    """
    Tests for Windows
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOWS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.Windows.parse_data(test_data)
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
        for test_name, test_data in WINDOWS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.Windows.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOWS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='desktop_id', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='pos_x', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='pos_y', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='width', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='height', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_west', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_east', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_north', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='chrome_south', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='minimized', name='Windows'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='keyboard_focus', name='Windows'),
            ),

        ),
    ),

]


WINDOWS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': '±ɔ˰ʮ˟rҍƺʙn˹ϳƞĜΫÊСɇʷ\x96ͰΒȸҖƥÌȊɤқ\u0379',
            'desktop_id': 'ӞʴґΓĲӗŕæÈϐԬ˒\x81ԖӠ.ûƏӇƨЧ˚ķkȥŪԮьTǨ',
            'pos_x': 1221774,
            'pos_y': -330460,
            'width': -4386073,
            'height': 200802,
            'chrome_west': -8260644,
            'chrome_east': -6129122,
            'chrome_north': -956969,
            'chrome_south': 5944778,
            'minimized': True,
            'keyboard_focus': 4243,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'îöàȘ&',

            'desktop_id': '<ӅŐњЦ',

            'pos_x': -5979185,

            'pos_y': -5775365,

            'width': 4119624,

            'height': -5869069,

            'chrome_west': 2709439,

            'chrome_east': 8967560,

            'chrome_north': 8314681,

            'chrome_south': 6915685,

            'minimized': False,

            'keyboard_focus': 50,

        },
    ),
]


class VirtualDesktopWindowsStateTest(unittest.TestCase):
    """
    Tests for VirtualDesktopWindowsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in VIRTUAL_DESKTOP_WINDOWS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.VirtualDesktopWindowsState.parse_data(test_data)
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
        for test_name, test_data in VIRTUAL_DESKTOP_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = positioner.VirtualDesktopWindowsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


VIRTUAL_DESKTOP_WINDOWS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='windows', name='VirtualDesktopWindowsState'),
            ),

        ),
    ),

]


VIRTUAL_DESKTOP_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'windows': [
                {
                    'window_id': 'ыΞǽ\u0383řʚцˤŜɆƎϢͿƀśуБɶęʴ˷Ԥ\xa0¬ʈĄʩεҰȼ',
                    'desktop_id': 'ɼŨ\u0379Ĵ҄ˍƈ\x99þƵҺĶųеԜ˸ʮʰиťǛЫȔӞάǓůХʼϱ',
                    'pos_x': 2834978,
                    'pos_y': 7342241,
                    'width': -6872759,
                    'height': 7890772,
                    'chrome_west': -5082808,
                    'chrome_east': -6469894,
                    'chrome_north': 8179541,
                    'chrome_south': 4177005,
                    'minimized': False,
                    'keyboard_focus': 5330,
                },
                {
                    'window_id': 'ʳ´ÿWϐŪͻɜǂH҄F]ϤʑıǏ\x8aǰѥ2£ƘȸʛҝŷʂȔʘ',
                    'desktop_id': 'ǤƧҋϩƌЁĖӥƪϳt\x85΅ԞMϙǎңǅκ\x82ˍΠМĘň\x9cЊĽž',
                    'pos_x': 2230123,
                    'pos_y': -3148017,
                    'width': 9426151,
                    'height': 384557,
                    'chrome_west': -8097143,
                    'chrome_east': 3887470,
                    'chrome_north': -882410,
                    'chrome_south': -5184833,
                    'minimized': True,
                    'keyboard_focus': 863,
                },
                {
                    'window_id': 'įö¨\x81ʇ_uɇуʊ˗ҹĠʘéԆϖƚÈɎϺɔǍӷĊҥΨυ?҂',
                    'desktop_id': 'ĵΡȐӬѰψ˼ƔFŬ\x97ȠQ\x90\u0381ε\x86ӓȴΚӚ\x96<έԦĵȞȥǴϡ',
                    'pos_x': 3055012,
                    'pos_y': -2609768,
                    'width': -6876267,
                    'height': -5876632,
                    'chrome_west': 3068618,
                    'chrome_east': -5844034,
                    'chrome_north': 8798903,
                    'chrome_south': 8717539,
                    'minimized': False,
                    'keyboard_focus': 1059,
                },
                {
                    'window_id': 'ӝ\x9eőȇɿ\x9cɣϰӭʚƶň,ʀнƀтŬˣάмNèћʴýŞΌӬ/',
                    'desktop_id': 'ΣƘҒȍŧ˓Ѣɢŧ.ЛȡóԡŷʇŘÂ͵ԋ\xadԃԐԩӇɭŗШҘů',
                    'pos_x': -4600539,
                    'pos_y': 871109,
                    'width': -7242845,
                    'height': -9659379,
                    'chrome_west': -2403575,
                    'chrome_east': 811652,
                    'chrome_north': 3562698,
                    'chrome_south': 2961065,
                    'minimized': False,
                    'keyboard_focus': 2755,
                },
                {
                    'window_id': 'ŌűӠàӦ\x84ƽʧ6τˡ\x8fɒʒĻ\x91ʗɱŶӀȩɄρő˚aа<ԉϚ',
                    'desktop_id': 'μъăÊԌήƁʮӈˆĝюѲ÷N\x9fϭ˧ȜôȢӵȔ¿ˀ˘nƀǲϡ',
                    'pos_x': 5614164,
                    'pos_y': 8675106,
                    'width': 5230964,
                    'height': -7064615,
                    'chrome_west': 2227170,
                    'chrome_east': -3447534,
                    'chrome_north': -4680986,
                    'chrome_south': 748844,
                    'minimized': False,
                    'keyboard_focus': 4721,
                },
                {
                    'window_id': 'ȫÇ\x87ϟЁå+ѧӋť\x86ɨǱͲƭељɌìͷȢή\x87ӢƨƐƚŢмɟ',
                    'desktop_id': 'ӅԋČӕы´ˣȧ!¶ҚȋҺɅ\x99ÏU¯ÚĭώџʨʷѾǰĴҽСĭ',
                    'pos_x': -8169173,
                    'pos_y': 6008552,
                    'width': -2525308,
                    'height': -9822269,
                    'chrome_west': -5079388,
                    'chrome_east': -5287476,
                    'chrome_north': -7496401,
                    'chrome_south': 6990460,
                    'minimized': False,
                    'keyboard_focus': 1692,
                },
                {
                    'window_id': 'ˮЮЯƲӈЛӉЈ#e¢ˊȽďЄшȗο\u0383ʋ˹@΅҄ҙўQΛĳν',
                    'desktop_id': 'ˊÍԐnéʖ҂ԙвŬʙʱȜӕΉѷƽɆѤ\x9bεϓ.OΦĪˮ8Ƙʝ',
                    'pos_x': -7545070,
                    'pos_y': 8438065,
                    'width': -3776455,
                    'height': 9003546,
                    'chrome_west': 8989075,
                    'chrome_east': 5172503,
                    'chrome_north': 2714649,
                    'chrome_south': 6815532,
                    'minimized': False,
                    'keyboard_focus': 8845,
                },
                {
                    'window_id': 'ӝ\x9fȚ˥ѬнVÁʘɥЙ˷ы˾ͶΎĐӍŨMǲһӆΙkâƩʤуɳ',
                    'desktop_id': 'δ˺ȝóɾǙ˖˕Ϳ]\x85¦£ʕҺƢʠʠǮӲʿɘӆɱтѐүŸƭe',
                    'pos_x': -9337549,
                    'pos_y': -5708638,
                    'width': -6879511,
                    'height': 2013473,
                    'chrome_west': 4411545,
                    'chrome_east': -468729,
                    'chrome_north': 5255902,
                    'chrome_south': 5309407,
                    'minimized': False,
                    'keyboard_focus': 1,
                },
                {
                    'window_id': '\x98Ƕȿʻżғ҆ʂɽӏɻ9ö҆ƆϔĐΥϝʕƲšY\x84ǱȬɡͼ˰ѫ',
                    'desktop_id': 'ƴŷVДѣ÷ғХ\u0381ϴͲʦƞϟҲрԊűˊ3ΦӊҮырǁĞȤǽğ',
                    'pos_x': -6788355,
                    'pos_y': -9742891,
                    'width': 4935646,
                    'height': -3479350,
                    'chrome_west': -1961240,
                    'chrome_east': 7977844,
                    'chrome_north': 7385632,
                    'chrome_south': 1721397,
                    'minimized': True,
                    'keyboard_focus': 7650,
                },
                {
                    'window_id': 'ԒԀѴʘΜáʯ/ȠԨ±čΰƫʱϗΊУϭĉĀđ>ұ',
                    'desktop_id': '©θʮ҂SԬұǣɽǶâfԖɠĹΗΒģʯԕӪѠӈƾlɺĈƨΓǭ',
                    'pos_x': 2803190,
                    'pos_y': -3090520,
                    'width': -831659,
                    'height': -6199676,
                    'chrome_west': -610452,
                    'chrome_east': 6597504,
                    'chrome_north': 8563832,
                    'chrome_south': -7944418,
                    'minimized': False,
                    'keyboard_focus': 8047,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'windows': [
            ],

        },
    ),
]
