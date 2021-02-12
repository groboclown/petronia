# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-12T16:50:56.893915+00:00

"""
Tests for the screen module.
Extension petronia.core.api.native.screen, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import screen

class ScreenMonitorMappingTest(unittest.TestCase):
    """
    Tests for ScreenMonitorMapping
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SCREEN_MONITOR_MAPPING_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.ScreenMonitorMapping.parse_data(test_data)
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
        for test_name, test_data in SCREEN_MONITOR_MAPPING_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.ScreenMonitorMapping.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SCREEN_MONITOR_MAPPING_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='source_nw_x_pixel', name='ScreenMonitorMapping'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='source_nw_y_pixel', name='ScreenMonitorMapping'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='source_pixel_width', name='ScreenMonitorMapping'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='source_pixel_height', name='ScreenMonitorMapping'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='rotation', name='ScreenMonitorMapping'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='virtual_nw_x_pixel', name='ScreenMonitorMapping'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='virtual_nw_y_pixel', name='ScreenMonitorMapping'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='virtual_width', name='ScreenMonitorMapping'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='virtual_height', name='ScreenMonitorMapping'),
            ),

        ),
    ),

]


SCREEN_MONITOR_MAPPING_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'source_monitor': 9203252,
            'source_nw_x_pixel': -1436268560149034249,
            'source_nw_y_pixel': -996014203559673763,
            'source_pixel_width': -2776362738967584046,
            'source_pixel_height': -247736188704981886,
            'rotation': -1576481996163615985,
            'virtual_nw_x_pixel': -1869242535,
            'virtual_nw_y_pixel': 1126101732,
            'virtual_width': 275046288,
            'virtual_height': -906801463,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -6920427623790378254,

            'source_nw_y_pixel': -4179791019080375293,

            'source_pixel_width': -5344925311098653656,

            'source_pixel_height': -5760174622766956048,

            'rotation': -1873175287057737861,

            'virtual_nw_x_pixel': 1523750275,

            'virtual_nw_y_pixel': -543445880,

            'virtual_width': -1999878475,

            'virtual_height': 795445324,

        },
    ),
]

class MapMonitorsRequestEventTest(unittest.TestCase):
    """
    Tests for MapMonitorsRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MAP_MONITORS_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.MapMonitorsRequestEvent.parse_data(test_data)
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
        for test_name, test_data in MAP_MONITORS_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.MapMonitorsRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MAP_MONITORS_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sceens', name='MapMonitorsRequestEvent'),
            ),

        ),
    ),

]


MAP_MONITORS_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sceens': [
                {
                    'source_monitor': 6053920,
                    'source_nw_x_pixel': -7724882110061634622,
                    'source_nw_y_pixel': -8897930842006750589,
                    'source_pixel_width': -4850778188245238873,
                    'source_pixel_height': -3940832729969622658,
                    'rotation': -1928004521659582425,
                    'virtual_nw_x_pixel': -646049757,
                    'virtual_nw_y_pixel': 1301321992,
                    'virtual_width': 1323838136,
                    'virtual_height': 271235736,
                },
                {
                    'source_monitor': 6608767,
                    'source_nw_x_pixel': -9195177563939253572,
                    'source_nw_y_pixel': -5174708862359419725,
                    'source_pixel_width': -3128301080116680011,
                    'source_pixel_height': -2318062952007097383,
                    'rotation': -6558905009666330358,
                    'virtual_nw_x_pixel': -906502505,
                    'virtual_nw_y_pixel': -1719573128,
                    'virtual_width': 154127371,
                    'virtual_height': -1896214983,
                },
                {
                    'source_monitor': 5400359,
                    'source_nw_x_pixel': -6449077656047828014,
                    'source_nw_y_pixel': -2442613912291891909,
                    'source_pixel_width': -3963907997520499806,
                    'source_pixel_height': -7251417549848331362,
                    'rotation': -2068292815401346264,
                    'virtual_nw_x_pixel': -1227394285,
                    'virtual_nw_y_pixel': 390763440,
                    'virtual_width': -196350129,
                    'virtual_height': -316469322,
                },
                {
                    'source_monitor': 2104565,
                    'source_nw_x_pixel': -7482454912780812029,
                    'source_nw_y_pixel': -2252694275092976582,
                    'source_pixel_width': -8093142176436884452,
                    'source_pixel_height': -5905556473578744047,
                    'rotation': -632422951817593738,
                    'virtual_nw_x_pixel': -840376017,
                    'virtual_nw_y_pixel': 887289498,
                    'virtual_width': 11769333,
                    'virtual_height': -189276516,
                },
                {
                    'source_monitor': 1159189,
                    'source_nw_x_pixel': -8720697853785344814,
                    'source_nw_y_pixel': -1514436158643269289,
                    'source_pixel_width': -7822448694334833391,
                    'source_pixel_height': -5957226144726115647,
                    'rotation': -3815745858811296468,
                    'virtual_nw_x_pixel': 901935912,
                    'virtual_nw_y_pixel': 1296346282,
                    'virtual_width': -1502868420,
                    'virtual_height': -630136754,
                },
                {
                    'source_monitor': 3997328,
                    'source_nw_x_pixel': -1376327708064519337,
                    'source_nw_y_pixel': -7415737282518078051,
                    'source_pixel_width': -8973894361301715258,
                    'source_pixel_height': -5789116938235734295,
                    'rotation': -2187333534989547347,
                    'virtual_nw_x_pixel': -733738965,
                    'virtual_nw_y_pixel': -722007315,
                    'virtual_width': -515256221,
                    'virtual_height': -73667841,
                },
                {
                    'source_monitor': 482759,
                    'source_nw_x_pixel': -3957903724365075000,
                    'source_nw_y_pixel': -2192374988418177345,
                    'source_pixel_width': -7055594077152217207,
                    'source_pixel_height': -8696542899359584519,
                    'rotation': -8941200632406619327,
                    'virtual_nw_x_pixel': -1736888480,
                    'virtual_nw_y_pixel': -891261242,
                    'virtual_width': 1070307372,
                    'virtual_height': -155779914,
                },
                {
                    'source_monitor': 6701198,
                    'source_nw_x_pixel': -891538043603286983,
                    'source_nw_y_pixel': -7633926969652884335,
                    'source_pixel_width': -2244906221966909161,
                    'source_pixel_height': -6969654434848333643,
                    'rotation': -1349115279628318132,
                    'virtual_nw_x_pixel': -1737752578,
                    'virtual_nw_y_pixel': -1737443167,
                    'virtual_width': 809985915,
                    'virtual_height': 190666766,
                },
                {
                    'source_monitor': 9925440,
                    'source_nw_x_pixel': -1667600692611597780,
                    'source_nw_y_pixel': -2528485431405333676,
                    'source_pixel_width': -7375656665173896137,
                    'source_pixel_height': -4722605223045776778,
                    'rotation': -8470713712660143784,
                    'virtual_nw_x_pixel': -1014544035,
                    'virtual_nw_y_pixel': -1521120806,
                    'virtual_width': 897119300,
                    'virtual_height': -444962741,
                },
                {
                    'source_monitor': 3772031,
                    'source_nw_x_pixel': -1669588114613594289,
                    'source_nw_y_pixel': -6467456763409305415,
                    'source_pixel_width': -105331170599410532,
                    'source_pixel_height': -5198946873634468532,
                    'rotation': -4458741004405008944,
                    'virtual_nw_x_pixel': 589404180,
                    'virtual_nw_y_pixel': -1035159160,
                    'virtual_width': -885422565,
                    'virtual_height': 1964796045,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sceens': [
            ],

        },
    ),
]

class AreaTest(unittest.TestCase):
    """
    Tests for Area
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in AREA_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.Area.parse_data(test_data)
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
        for test_name, test_data in AREA_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.Area.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


AREA_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='nw_x_pixel', name='Area'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='nw_y_pixel', name='Area'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='width', name='Area'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='height', name='Area'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='ratio_x', name='Area'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='ratio_y', name='Area'),
            ),

        ),
    ),

]


AREA_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'nw_x_pixel': 88441092,
            'nw_y_pixel': 645703867,
            'width': -4771680070365419002,
            'height': -1730652948635273812,
            'ratio_x': -8279477086403149346,
            'ratio_y': 2165764930522568053,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -1892530595,

            'nw_y_pixel': -1592608354,

            'width': -1320911051924432336,

            'height': -5114090800894707333,

            'ratio_x': -2060351238856527840,

            'ratio_y': -4015314885463600587,

        },
    ),
]

class VirtualScreenStateTest(unittest.TestCase):
    """
    Tests for VirtualScreenState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in VIRTUAL_SCREEN_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.VirtualScreenState.parse_data(test_data)
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
        for test_name, test_data in VIRTUAL_SCREEN_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.VirtualScreenState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


VIRTUAL_SCREEN_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='area', name='VirtualScreenState'),
            ),

        ),
    ),

]


VIRTUAL_SCREEN_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'area': [
                {
                    'nw_x_pixel': 977591452,
                    'nw_y_pixel': -141697495,
                    'width': -3171805147319800154,
                    'height': -6567559753425905382,
                    'ratio_x': -3519239115072347460,
                    'ratio_y': 7955313283086393210,
                },
                {
                    'nw_x_pixel': -938607246,
                    'nw_y_pixel': -1573081073,
                    'width': -4328557646267662126,
                    'height': -4920546478243734214,
                    'ratio_x': 3759597110573840825,
                    'ratio_y': 7321426325601253716,
                },
                {
                    'nw_x_pixel': 394558473,
                    'nw_y_pixel': 1977323804,
                    'width': -3600149530560998663,
                    'height': -7434261112820153215,
                    'ratio_x': 287160913198573585,
                    'ratio_y': -8904489870071026413,
                },
                {
                    'nw_x_pixel': -1279610645,
                    'nw_y_pixel': -1924553688,
                    'width': -3256511078584766549,
                    'height': -774218822171475775,
                    'ratio_x': 7084061576463820799,
                    'ratio_y': -1045899797928869753,
                },
                {
                    'nw_x_pixel': 105294786,
                    'nw_y_pixel': -881874035,
                    'width': -8987750740633698249,
                    'height': -9021130046460678636,
                    'ratio_x': -3610933378556515576,
                    'ratio_y': -5499850878976636970,
                },
                {
                    'nw_x_pixel': 1436113204,
                    'nw_y_pixel': 1710881517,
                    'width': -6211521773002807935,
                    'height': -4564308455988084449,
                    'ratio_x': 2114285739663478989,
                    'ratio_y': -8229325893053940994,
                },
                {
                    'nw_x_pixel': 1171095435,
                    'nw_y_pixel': -1516745041,
                    'width': -5343437963192804715,
                    'height': -782443255598662999,
                    'ratio_x': -3315617306451515522,
                    'ratio_y': -9174155290098523254,
                },
                {
                    'nw_x_pixel': 1722693750,
                    'nw_y_pixel': -1159197338,
                    'width': -6410952419117110374,
                    'height': -2262649675529860160,
                    'ratio_x': -8909106032404055797,
                    'ratio_y': 5815666188259159681,
                },
                {
                    'nw_x_pixel': -797963803,
                    'nw_y_pixel': 661449594,
                    'width': -1208593570436023076,
                    'height': -1127775380182373933,
                    'ratio_x': -4937647172084822806,
                    'ratio_y': 1064141576132683455,
                },
                {
                    'nw_x_pixel': -1846661276,
                    'nw_y_pixel': 1307187743,
                    'width': -7052305303262694798,
                    'height': -3315156689804271211,
                    'ratio_x': 3975509914438000213,
                    'ratio_y': 4841650587204950781,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'area': [
            ],

        },
    ),
]
