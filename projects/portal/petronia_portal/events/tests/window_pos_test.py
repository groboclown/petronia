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
            'window_id': 'ҡǛԔɈϯԧƲƌϤҢț«ΕӏƽǦȿ˞ѐϠԆțŬϼʆТɤȫλҪ',
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
            'window_id': 'Ɩӷˁ~Śőj\x93ÂϭȿƴѲǿũԤΦ˓ÌДʆtθîϭ˙λĞ҉ј',
            'desktop_id': 'ïNʫїąѫƳƟӯȀ\x8dґҋȲьџЁϯφǌԈɦͲʌҠ¨ʨαӶԛ',
            'pos_x': 109367,
            'pos_y': 3995189,
            'width': 9370847,
            'height': -2639067,
            'chrome_west': 6556811,
            'chrome_east': -8239532,
            'chrome_north': 44106,
            'chrome_south': 9963505,
            'minimized': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ɡˣҍ\u0382\x8a',

            'desktop_id': 'ÕӛЗЖЅ',

            'pos_x': 9528405,

            'pos_y': -7682733,

            'width': -7714699,

            'height': -1970872,

            'chrome_west': 6632693,

            'chrome_east': -3078721,

            'chrome_north': -4204127,

            'chrome_south': 3153034,

            'minimized': False,

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
                    'window_id': 'ȾƵͰͷÌȩʕƓςҾıѢǋɢʽѭ˂Ν\x9d˫ȔѮǵΖȳԌȁϗǉ˅',
                    'desktop_id': 'ӫÇҏϛ\u0378ŗɧ\x89ŷǘӢÉæͻŸǜh˚ҰаǾƏŔΆѲӀƎʽҗĂ',
                    'pos_x': 8572462,
                    'pos_y': -4033711,
                    'width': -3651851,
                    'height': 334184,
                    'chrome_west': -7920323,
                    'chrome_east': -1164576,
                    'chrome_north': -1821989,
                    'chrome_south': 5832483,
                    'minimized': True,
                },
                {
                    'window_id': 'CζζИșŕыbǖοǵ~ǢѠӋҝƂȎѲFψΈK˷ѾȍÒ8SϷ',
                    'desktop_id': 'Ǚмsůźɮ-&ЋԗƆħÙ¦ϖ3ҽºҿ\x90ŊЦʹʿǼʎ\u0380ǣԞԊ',
                    'pos_x': 3093708,
                    'pos_y': -5426422,
                    'width': -8462192,
                    'height': 3993027,
                    'chrome_west': -1191244,
                    'chrome_east': -1002338,
                    'chrome_north': -6368020,
                    'chrome_south': 6193387,
                    'minimized': True,
                },
                {
                    'window_id': 'ѝТӕӃĠȹȞū°ƗȬ҃ҫǟң¢ˡȗϯԛŎŃҤӝӲʮHiƽˀ',
                    'desktop_id': 'ƒɰ\x85ҾǧȖ+ϽʃӏѠĕƍÑҲɃʮƚŶ¤ΙϏ\x81ɷǇˁӶάӿУ',
                    'pos_x': -496537,
                    'pos_y': -1580205,
                    'width': 7238804,
                    'height': 9136043,
                    'chrome_west': -513873,
                    'chrome_east': 7621173,
                    'chrome_north': 1892835,
                    'chrome_south': -2267931,
                    'minimized': False,
                },
                {
                    'window_id': 'ӝ΄§Ǧφo¨҄ȕ΄ƈʠȑŲƥƿŘˉӴӵёƛӅԉƙǆƛҠǢȎ',
                    'desktop_id': 'ϸѽƜұÎ˚ĥчτοqȰϭ³ҝŻǿ$ЪǦЬ\x96ӝå˨͵˳Η\x88ӻ',
                    'pos_x': 7887725,
                    'pos_y': -7654608,
                    'width': 3723556,
                    'height': -8045721,
                    'chrome_west': 6789858,
                    'chrome_east': -3600617,
                    'chrome_north': 9662832,
                    'chrome_south': -1245262,
                    'minimized': False,
                },
                {
                    'window_id': 'чʙ\u0379ʃ˴ϒϹԤǦǀΙӭlԎǝ˅ɆĐǨԭ˗Ӵű҈ųιШŴSƒ',
                    'desktop_id': 'ӾόԊɪɀðsԚÚĻӇÚ\x8a\x9aҭļӗBԟľɪŹЩҧUßӽƺɵ\x88',
                    'pos_x': -1974819,
                    'pos_y': -2487930,
                    'width': 2088510,
                    'height': 6768397,
                    'chrome_west': 3324612,
                    'chrome_east': -4236808,
                    'chrome_north': 8523223,
                    'chrome_south': -8817085,
                    'minimized': False,
                },
                {
                    'window_id': 'Ҡ®RȢŇΪϞϗȢ\x99ҲμѯȨÚШħŘ҆δγѶ\x8bm\u0382ӦИaȩɤ',
                    'desktop_id': 'ƚ·ƳӴˎςϤԞŝԨŢƌƧѦ¾ʝŬђʎѐǍįáп9ŸЂʹԢѲ',
                    'pos_x': -7702919,
                    'pos_y': 1239587,
                    'width': -2017976,
                    'height': -3697677,
                    'chrome_west': -2618849,
                    'chrome_east': -4005246,
                    'chrome_north': 7572347,
                    'chrome_south': 5542701,
                    'minimized': True,
                },
                {
                    'window_id': 'ȣІȤԢƭ,ƨƑ\\-ƦҦϦфЉѡӔ®ӣЫǍȆʡʦӉιɼЦиŎ',
                    'desktop_id': 'Mчς˧ʧóƹƻ!Ґɸ˥ЮͿïЮύ/ʸȚ\x89ӆɵӼ\x9eɑӽВĆɛ',
                    'pos_x': 4304598,
                    'pos_y': 6438293,
                    'width': 6694005,
                    'height': -8818646,
                    'chrome_west': 8861624,
                    'chrome_east': 3585629,
                    'chrome_north': 5741323,
                    'chrome_south': -7656161,
                    'minimized': False,
                },
                {
                    'window_id': 'ˢ\u0382ƭ҉ǃҬгϡӕƑAɁɥԛнǳȵƳºĖˢ;ǘɳƨ\x99;Άҽȶ',
                    'desktop_id': 'Ҡɋ(ʟƅќ˕Ѵ\x84ĭĬ;ȿʭӐ|˵ƦˢȻōʑʞȧñĘŜƌӗġ',
                    'pos_x': -3685048,
                    'pos_y': -8091088,
                    'width': 1638195,
                    'height': -5328734,
                    'chrome_west': 7189625,
                    'chrome_east': 7163728,
                    'chrome_north': 6437813,
                    'chrome_south': -5539176,
                    'minimized': False,
                },
                {
                    'window_id': 'ȐȲȤɚ\u038bӡɕӅƟˋȢȒǟv÷Җ%ГӂӚÈоTҮĎǰǐǽъd',
                    'desktop_id': 'ȑҦϝѵ˖\x80ͼԚķœʒ%ұӑϏɕǠɇ;шΐЋ϶ˈĊʹňʊ-ϒ',
                    'pos_x': -2425290,
                    'pos_y': -3639819,
                    'width': -4683027,
                    'height': -6812184,
                    'chrome_west': -88823,
                    'chrome_east': 5873993,
                    'chrome_north': -9675018,
                    'chrome_south': 904609,
                    'minimized': False,
                },
                {
                    'window_id': 'єԃӞϛ˷ƝȹѦѪųȆҙhщÙӊOǔ˄ΛҋӟЄ\x90ϘSɹɘKĹ',
                    'desktop_id': 'Έpƃԕяҁƌƾϑʱσȉ\u0382ćЃΝÆԀ\x97ǥҥ\u0381ˈÇĹщƖ\x88ȱȊ',
                    'pos_x': -4574943,
                    'pos_y': 8643919,
                    'width': 3962584,
                    'height': 7952658,
                    'chrome_west': -6961903,
                    'chrome_east': 1481071,
                    'chrome_north': -3920940,
                    'chrome_south': 2240563,
                    'minimized': False,
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
