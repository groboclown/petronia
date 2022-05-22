# GENERATED CODE - DO NOT MODIFY

"""
Tests for the window_pos module.
Extension petronia.core.api.window_pos, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import window_pos


class FocusStateTest(unittest.TestCase):
    """
    Tests for FocusState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in FOCUS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window_pos.FocusState.parse_data(test_data)
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
                res = window_pos.FocusState.parse_data(test_data)
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
            'window_id': 'ͿЏҶƕѹϭÜ"зŠ\u0382ұӭ˅ΑҶĝɷͳԠηЌĴɬ6ΙC\x88Ԑÿ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

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
                res = window_pos.Windows.parse_data(test_data)
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
                res = window_pos.Windows.parse_data(test_data)
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

        ),
    ),

]


WINDOWS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': 'ƍ\x9dƵiЭ˳ʑȭԘ\x9cƬт"$ћәЀӮʩσÃӂʱӀґǀѹϹů¬',
            'desktop_id': '\x92ӽӌҚѼŒŮɞĤSГʡЖũɌƅσ˽иʯ˼ŊǒƑ©ʮҹÜҵˌ',
            'pos_x': 71948,
            'pos_y': 9351442,
            'width': -3966021,
            'height': -7267791,
            'chrome_west': 947887,
            'chrome_east': -3339228,
            'chrome_north': -2922172,
            'chrome_south': 4956113,
            'minimized': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'øĄΰЙǋ',

            'desktop_id': 'ЋñΩúϼ',

            'pos_x': -4548100,

            'pos_y': 3228716,

            'width': 6872171,

            'height': -4304965,

            'chrome_west': -2396002,

            'chrome_east': -3399328,

            'chrome_north': -1178618,

            'chrome_south': 3069078,

            'minimized': True,

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
                res = window_pos.VirtualDesktopWindowsState.parse_data(test_data)
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
                res = window_pos.VirtualDesktopWindowsState.parse_data(test_data)
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
                    'window_id': 'ԙŐůʪʪѲDʐҭćé˛+˯¤ХцÖʩƱŨȿƌÄsϧņΞёϽ',
                    'desktop_id': 'Ԛ˧ÛАƜľ˾YԬ\xa0ŭΐɽθɃˍȾҘѥɏĮгɮӡĬΑϰɊѬʠ',
                    'pos_x': 7227555,
                    'pos_y': -5597619,
                    'width': 3841305,
                    'height': 5647652,
                    'chrome_west': -2041503,
                    'chrome_east': -5535167,
                    'chrome_north': 546027,
                    'chrome_south': -3625439,
                    'minimized': True,
                },
                {
                    'window_id': '_ǮɼƟԭXƳдԜǸɤ˳ύtūɀҬѦ3¬Ӥʣ˳њѠ˹ĄɆǶȨ',
                    'desktop_id': '\u0379˥φʱɒÌ҃õѷƟҘʻǧƍaŸАʭ\x98Ͱ@Ɉéæ6ѹúŖƶҵ',
                    'pos_x': 6556433,
                    'pos_y': 2962975,
                    'width': -694898,
                    'height': -8704934,
                    'chrome_west': 7607160,
                    'chrome_east': 9189951,
                    'chrome_north': 616487,
                    'chrome_south': -1689378,
                    'minimized': True,
                },
                {
                    'window_id': 'ƙΟóěΡȶtƓÄŖƢŽʝŷŠĽЧőӎǩCόПiϡˑŨ˂џǫ',
                    'desktop_id': 'ƂɸΘǨпËā҇ʣʚƩϾȋȓ»һʓÑĬѡɹſǖԏȆԭ˸ˌπ\x9b',
                    'pos_x': 1415622,
                    'pos_y': 5449210,
                    'width': 8552488,
                    'height': 3429260,
                    'chrome_west': 2246914,
                    'chrome_east': 6646577,
                    'chrome_north': -4173876,
                    'chrome_south': -8470632,
                    'minimized': True,
                },
                {
                    'window_id': 'ŝi˳rɚ»ρĭŲҙ\x8c^ϝȿ˺ʇıɗȁҽýĻɜõīžΌʁиĀ',
                    'desktop_id': '˄yίř\u0383ñӠƵϢUƐТNюЯǶϟäëʬӆ\x80҆ŸƯ\x9d*ŶYȟ',
                    'pos_x': 7495186,
                    'pos_y': -9146426,
                    'width': -4632165,
                    'height': 1144535,
                    'chrome_west': 1961943,
                    'chrome_east': -191806,
                    'chrome_north': 5853185,
                    'chrome_south': -7114597,
                    'minimized': True,
                },
                {
                    'window_id': 'ҍЧʷ×ȎÕmÄŃ«ðԉєǥľɍίȥ˄ǉвƵƘɘѭĖËX\x9dŸ',
                    'desktop_id': 'ҟäΨԤɧԔɔҿǏǪRҳЃʁƄϔҜŃεɐŎ\x96PȄҲâ҂ĔĐѬ',
                    'pos_x': -5299462,
                    'pos_y': 7456251,
                    'width': 1895366,
                    'height': 7258079,
                    'chrome_west': 6780796,
                    'chrome_east': -1093785,
                    'chrome_north': -6974901,
                    'chrome_south': -1079730,
                    'minimized': True,
                },
                {
                    'window_id': 'ʭũэӮӠԤÚԛʘ҆Ғ/ԟÌĕȥʨĠγýõːǜçØο҂ļʞÚ',
                    'desktop_id': 'ĬϡȘɲȥǰėȏӘɂιǫÃ!уˣԟɑžв©ӫȓ;ǗìЋÈÖӰ',
                    'pos_x': 9478316,
                    'pos_y': 4017963,
                    'width': -8793334,
                    'height': -987639,
                    'chrome_west': 6306111,
                    'chrome_east': -7880626,
                    'chrome_north': 1854443,
                    'chrome_south': -5033620,
                    'minimized': True,
                },
                {
                    'window_id': 'ҒΘgŤЇʓКԠēôԅΝͷπǬʅϯɷäԕŃğҲě¹ʚȼÙŲʜ',
                    'desktop_id': 'ϰŴӠǏљƇɆѿ\x90ĠŘÚǭͶvkȜț҂ҵŚIĽЯ_Đ\x9bȒ˪Ѵ',
                    'pos_x': 58182,
                    'pos_y': 9212120,
                    'width': 6076401,
                    'height': 4290758,
                    'chrome_west': 649353,
                    'chrome_east': 3405162,
                    'chrome_north': -6129665,
                    'chrome_south': 2294090,
                    'minimized': False,
                },
                {
                    'window_id': 'iŔʋ&ĄśƑΧƁͼĽЭȴԁѥɲϥǃҳɰ=ʿӐűɗ˯ϋ\x98ҿƝ',
                    'desktop_id': 'œʋȋϾ>Ʌ\u0382ÌɎ\x93Ľ˛˼ʍϭӟƎǅΕϓÐ)ƱЃĩԍ˨˻ќʟ',
                    'pos_x': -7037766,
                    'pos_y': -8903075,
                    'width': 697516,
                    'height': 8314742,
                    'chrome_west': 6364226,
                    'chrome_east': 2296096,
                    'chrome_north': 4946175,
                    'chrome_south': 5571619,
                    'minimized': True,
                },
                {
                    'window_id': 'ˇӯgǼЮɍȔеҰƁŪňƾαĒųԒԍǗŪͺ˨ŝлҪăʗòӴӒ',
                    'desktop_id': 'ɫжy˃öó/ʜҟɸΗ\x9dʬǦő?Ӎιɱ¤ȅZɤǀŷϽϸɀżΗ',
                    'pos_x': -7742406,
                    'pos_y': 1690341,
                    'width': -2166490,
                    'height': -4990793,
                    'chrome_west': -6674100,
                    'chrome_east': -6984291,
                    'chrome_north': 7148442,
                    'chrome_south': -7426472,
                    'minimized': False,
                },
                {
                    'window_id': 'ɟÐßɢȧɸ«\xadЉʇӄȂíºҪaÉǂǣɲĠ˔ѕэ˷ѧӅӒ˦Ķ',
                    'desktop_id': ',ͷëʼʆÀːǺéΨAЕǝɜ\x9dpɞƽ˸ʏʗļÏҦͼÚ\u0380X¡Ǉ',
                    'pos_x': 818489,
                    'pos_y': -5096462,
                    'width': 2207339,
                    'height': 8966145,
                    'chrome_west': 7945010,
                    'chrome_east': 2737401,
                    'chrome_north': -6705740,
                    'chrome_south': 3052063,
                    'minimized': True,
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
