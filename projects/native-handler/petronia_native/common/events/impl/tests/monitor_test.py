# GENERATED CODE - DO NOT MODIFY

"""
Tests for the monitor module.
Extension petronia.core.api.native.monitor, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import monitor


class MonitorTest(unittest.TestCase):
    """
    Tests for Monitor
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MONITOR_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.Monitor.parse_data(test_data)
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
        for test_name, test_data in MONITOR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.Monitor.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MONITOR_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='real_pixel_width', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='real_pixel_height', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='dpi_x', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='dpi_y', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='supports_rotation', name='Monitor'),
            ),

        ),
    ),

]


MONITOR_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 3042082,
            'description': 'ζÓºʝͱĲԚƔȀʡзȽNƝȒŝӪʓŸƹʶåǐơoӵȡϦҒǹ',
            'real_pixel_width': -4694527455511530163,
            'real_pixel_height': -2755724426038218534,
            'dpi_x': 706815151523162195,
            'dpi_y': 3339043773774042343,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': -963867,

            'description': '',

            'real_pixel_width': -1281142948304263173,

            'real_pixel_height': -7150137259998476067,

            'dpi_x': 8279269488498872428,

            'dpi_y': 8212167530360013717,

            'supports_rotation': False,

        },
    ),
]


class ActiveMonitorsStateTest(unittest.TestCase):
    """
    Tests for ActiveMonitorsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_MONITORS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.ActiveMonitorsState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_MONITORS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.ActiveMonitorsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_MONITORS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='monitors', name='ActiveMonitorsState'),
            ),

        ),
    ),

]


ACTIVE_MONITORS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'monitors': [
                {
                    'identifier': 233487,
                    'description': 'α\x82ԉұ1ʶςʞƱϟЬн\x90˕Ѭψ5ԞɄĦͰҖħǐҤφѦϧΡ˹',
                    'real_pixel_width': -7751800430410351489,
                    'real_pixel_height': -6285889088507921338,
                    'dpi_x': 4331070706239276006,
                    'dpi_y': 898972581827694884,
                    'supports_rotation': True,
                },
                {
                    'identifier': 5241700,
                    'description': 'ҋМ¤ˊäҶƘɣȠȤFΉOӯȑ\x9bΉȮTɓЯǞΛǛ÷}ƋӘΠ÷',
                    'real_pixel_width': -5839616269506068501,
                    'real_pixel_height': -2789781118453372615,
                    'dpi_x': 3295368189355205358,
                    'dpi_y': 6025536436532371210,
                    'supports_rotation': False,
                },
                {
                    'identifier': 244683,
                    'description': 'ӺѵèҤχȟȳ÷҄ýҵĳûǊɤԑгˡÂҢΔϖϲӊwѭÄȏÜһ',
                    'real_pixel_width': -69770255786611896,
                    'real_pixel_height': -7985625998745009948,
                    'dpi_x': 1478467195358435735,
                    'dpi_y': 596267840694713017,
                    'supports_rotation': True,
                },
                {
                    'identifier': 7972983,
                    'description': 'ʆTǜ˵фɄΆЫӃšΑǡĞŐƙΓʎôƛ?ԚѼxȋȌɃϓ˗ǅԑ',
                    'real_pixel_width': -4813210158210642135,
                    'real_pixel_height': -7681912161617567035,
                    'dpi_x': 9191536149546423611,
                    'dpi_y': 8365848616421473959,
                    'supports_rotation': False,
                },
                {
                    'identifier': 5370990,
                    'description': "Ʒʯ+Đƺϛ˦ѬјǁƖœϢҰυȪ'ɷӒҺ҈ʽ\u0381jҼÓǮ\x99ƪƒ",
                    'real_pixel_width': -5792857524013622701,
                    'real_pixel_height': -1000200927586250716,
                    'dpi_x': 6174387862610127673,
                    'dpi_y': 8791722901558213711,
                    'supports_rotation': True,
                },
                {
                    'identifier': 8385714,
                    'description': 'ɕ\x96ӄȇϳŢԙ\x8aѫѬơ~Ԋԙˉɼʬĉşʝ:˹ͷíѠº«\x9eɃҙ',
                    'real_pixel_width': -2409788651242515049,
                    'real_pixel_height': -3784305406761375178,
                    'dpi_x': 2673952304294967068,
                    'dpi_y': 565631738492334543,
                    'supports_rotation': True,
                },
                {
                    'identifier': 4485190,
                    'description': 'ϦРӊҶϝʼɟƃƷĕƧѳӬȥĆԛȹɅƯRЭƹџÀŗҒȂԥжӔ',
                    'real_pixel_width': -3040850545942912516,
                    'real_pixel_height': -6440811567135417475,
                    'dpi_x': 8513379623891346019,
                    'dpi_y': 7702170530434289882,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3070037,
                    'description': 'Ӯ<ϡӵƯϟĈ\x8eŶȜƶщϺѲĢʦ˻чѝԡȋѨŭƠ˂ԖͷΕΞǣ',
                    'real_pixel_width': -7514278044653509388,
                    'real_pixel_height': -6990364356942842820,
                    'dpi_x': 3361122897798344892,
                    'dpi_y': 5290287897094840614,
                    'supports_rotation': False,
                },
                {
                    'identifier': -872538,
                    'description': 'ӛ½ѻbŐ#ԡ.т˼ÛʋϔӕҀCӋҒԜͷɂå\x89ʃѷŒѽŨӁʞ',
                    'real_pixel_width': -8376923612578483856,
                    'real_pixel_height': -5466473779668858636,
                    'dpi_x': 4181097555072720520,
                    'dpi_y': 2200195766645104100,
                    'supports_rotation': False,
                },
                {
                    'identifier': 7333469,
                    'description': ']ƥρɸƑǆІǕj=ʵ\u0383Қѥ˄ÜӀҶÓȗϭ>ӻˮȹưʐЉѨι',
                    'real_pixel_width': -8811587249201295419,
                    'real_pixel_height': -8878900031299908916,
                    'dpi_x': 7532516121040419520,
                    'dpi_y': 1656641790666115498,
                    'supports_rotation': True,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
            ],

        },
    ),
]
