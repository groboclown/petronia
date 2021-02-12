# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-11T17:55:50.555415+00:00

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
            'source_monitor': 156322,
            'source_nw_x_pixel': -6830045021299662245,
            'source_nw_y_pixel': -4868532666660181873,
            'source_pixel_width': -2558455770536894341,
            'source_pixel_height': -4960523469505484030,
            'rotation': -7939712999688461035,
            'virtual_nw_x_pixel': 1629708678,
            'virtual_nw_y_pixel': -855327352,
            'virtual_width': 638504841,
            'virtual_height': -148518969,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -1270464112966961762,

            'source_nw_y_pixel': -3257487755560066442,

            'source_pixel_width': -711384542354698426,

            'source_pixel_height': -5874751380785761515,

            'rotation': -7636330326515767848,

            'virtual_nw_x_pixel': 1205988402,

            'virtual_nw_y_pixel': 1161367895,

            'virtual_width': -1452507292,

            'virtual_height': 599832596,

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
                    'source_monitor': 7420876,
                    'source_nw_x_pixel': -8431575125021507430,
                    'source_nw_y_pixel': -8442427448364988600,
                    'source_pixel_width': -10635028882071148,
                    'source_pixel_height': -9065414000709315672,
                    'rotation': -668495447204844568,
                    'virtual_nw_x_pixel': -931967567,
                    'virtual_nw_y_pixel': 306072932,
                    'virtual_width': 1822403159,
                    'virtual_height': -1833885230,
                },
                {
                    'source_monitor': 9828332,
                    'source_nw_x_pixel': -759676969675440352,
                    'source_nw_y_pixel': -4143049725153723966,
                    'source_pixel_width': -183848695053921674,
                    'source_pixel_height': -3280417550133030572,
                    'rotation': -7999646320363438098,
                    'virtual_nw_x_pixel': 386714867,
                    'virtual_nw_y_pixel': -784481470,
                    'virtual_width': 1021907039,
                    'virtual_height': 1140451426,
                },
                {
                    'source_monitor': 992303,
                    'source_nw_x_pixel': -1339191390899000748,
                    'source_nw_y_pixel': -5186176611540797966,
                    'source_pixel_width': -7003956965627603230,
                    'source_pixel_height': -2909456755569416979,
                    'rotation': -6274700370179978198,
                    'virtual_nw_x_pixel': 1416922726,
                    'virtual_nw_y_pixel': 510135361,
                    'virtual_width': -491110372,
                    'virtual_height': 1066929656,
                },
                {
                    'source_monitor': -234561,
                    'source_nw_x_pixel': -6533254874462832820,
                    'source_nw_y_pixel': -2557764037174078223,
                    'source_pixel_width': -5893012981103230458,
                    'source_pixel_height': -4661797812483282140,
                    'rotation': -4177663284838297065,
                    'virtual_nw_x_pixel': -1321817463,
                    'virtual_nw_y_pixel': -1898875905,
                    'virtual_width': -973779322,
                    'virtual_height': -1099308211,
                },
                {
                    'source_monitor': 5420472,
                    'source_nw_x_pixel': -6970543679911983695,
                    'source_nw_y_pixel': -4885553984527591885,
                    'source_pixel_width': -2120681481336806289,
                    'source_pixel_height': -473269932314620045,
                    'rotation': -6304105970975967403,
                    'virtual_nw_x_pixel': 1274355770,
                    'virtual_nw_y_pixel': -1486877111,
                    'virtual_width': 156694817,
                    'virtual_height': 704633553,
                },
                {
                    'source_monitor': 5141634,
                    'source_nw_x_pixel': -7208893025938867399,
                    'source_nw_y_pixel': -4845696658901227672,
                    'source_pixel_width': -6971674485416614950,
                    'source_pixel_height': -1754224242680005050,
                    'rotation': -208099365484363827,
                    'virtual_nw_x_pixel': -1612409199,
                    'virtual_nw_y_pixel': 1530527101,
                    'virtual_width': -65765764,
                    'virtual_height': -1194563263,
                },
                {
                    'source_monitor': 1462985,
                    'source_nw_x_pixel': -4716433572916569143,
                    'source_nw_y_pixel': -3127076787827920067,
                    'source_pixel_width': -973274922995733035,
                    'source_pixel_height': -7504173293746130323,
                    'rotation': -2053145069681393353,
                    'virtual_nw_x_pixel': 23434400,
                    'virtual_nw_y_pixel': -1831325772,
                    'virtual_width': -1614535092,
                    'virtual_height': 135024044,
                },
                {
                    'source_monitor': 3638369,
                    'source_nw_x_pixel': -8611421814146496344,
                    'source_nw_y_pixel': -8021980696376556122,
                    'source_pixel_width': -5566425471382312560,
                    'source_pixel_height': -31883970644787265,
                    'rotation': -4071502297897945219,
                    'virtual_nw_x_pixel': 933080888,
                    'virtual_nw_y_pixel': -1117611206,
                    'virtual_width': -331737411,
                    'virtual_height': -1670273629,
                },
                {
                    'source_monitor': 2539305,
                    'source_nw_x_pixel': -4733836134536012610,
                    'source_nw_y_pixel': -5878648833913388933,
                    'source_pixel_width': -4526210025871980702,
                    'source_pixel_height': -6691462474298038416,
                    'rotation': -247308215094489610,
                    'virtual_nw_x_pixel': -1194604593,
                    'virtual_nw_y_pixel': -22181910,
                    'virtual_width': -546516875,
                    'virtual_height': 771557490,
                },
                {
                    'source_monitor': 5053833,
                    'source_nw_x_pixel': -6395581843934945654,
                    'source_nw_y_pixel': -5157043700985128077,
                    'source_pixel_width': -1485167447809430469,
                    'source_pixel_height': -1788921143944718028,
                    'rotation': -3988864763494992698,
                    'virtual_nw_x_pixel': 491511375,
                    'virtual_nw_y_pixel': 1439350829,
                    'virtual_width': 349771356,
                    'virtual_height': -449322405,
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
            'nw_x_pixel': -1100919798,
            'nw_y_pixel': -427499009,
            'width': -6179825121135503044,
            'height': -3832443129088221408,
            'ratio_x': 3989212291511592560,
            'ratio_y': 7293146069063480837,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -956211379,

            'nw_y_pixel': 1605080502,

            'width': -3695640747742506831,

            'height': -7077539249436391111,

            'ratio_x': 239040142564034627,

            'ratio_y': 8355140004742973458,

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
                    'nw_x_pixel': -285671632,
                    'nw_y_pixel': 704846467,
                    'width': -7877869590570508419,
                    'height': -2233552706158140362,
                    'ratio_x': 889933504704190853,
                    'ratio_y': -7020492964934040710,
                },
                {
                    'nw_x_pixel': -1762669069,
                    'nw_y_pixel': 679915270,
                    'width': -6877678872268083726,
                    'height': -8667691851062465678,
                    'ratio_x': -462101701675768829,
                    'ratio_y': -1194125475434254164,
                },
                {
                    'nw_x_pixel': -713776250,
                    'nw_y_pixel': 1126195268,
                    'width': -5781247734418237769,
                    'height': -606301438520421742,
                    'ratio_x': -3807236861016035148,
                    'ratio_y': -310275802947160377,
                },
                {
                    'nw_x_pixel': -866752637,
                    'nw_y_pixel': -261445918,
                    'width': -2770583201138938258,
                    'height': -1888743414956754390,
                    'ratio_x': -6442046229254538282,
                    'ratio_y': -6112210647108621133,
                },
                {
                    'nw_x_pixel': 839908025,
                    'nw_y_pixel': -1595814988,
                    'width': -3601510759303654428,
                    'height': -1501336535189418869,
                    'ratio_x': -4744148189068994754,
                    'ratio_y': 8270981357510411860,
                },
                {
                    'nw_x_pixel': -521580800,
                    'nw_y_pixel': 1114073640,
                    'width': -5807345524571361040,
                    'height': -1639539814013415758,
                    'ratio_x': -855415601635471868,
                    'ratio_y': -1932743929382964151,
                },
                {
                    'nw_x_pixel': -735100946,
                    'nw_y_pixel': -1451268323,
                    'width': -182132193596568596,
                    'height': -3241439592505351503,
                    'ratio_x': 5267616047282049273,
                    'ratio_y': 4764388655140319245,
                },
                {
                    'nw_x_pixel': -366434275,
                    'nw_y_pixel': 517230777,
                    'width': -6748443260441340368,
                    'height': -8162651222257204691,
                    'ratio_x': 4779975448543243753,
                    'ratio_y': 3357504881745265033,
                },
                {
                    'nw_x_pixel': 1605834466,
                    'nw_y_pixel': 700315680,
                    'width': -6477711689470853393,
                    'height': -7277394248772849875,
                    'ratio_x': 8828231212727984623,
                    'ratio_y': -695791921657256609,
                },
                {
                    'nw_x_pixel': 1146624180,
                    'nw_y_pixel': -559905529,
                    'width': -865522337852354971,
                    'height': -3672966461875334995,
                    'ratio_x': 9066414165082814696,
                    'ratio_y': 8446998380185302864,
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
