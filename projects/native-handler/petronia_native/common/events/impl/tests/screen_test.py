# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-01T15:28:50.572821+00:00

"""
Tests for the screen module.
Extension petronia.core.api.native.screen, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import screen

class SourceMonitorTest(unittest.TestCase):
    """
    Tests for SourceMonitor
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SOURCE_MONITOR_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.SourceMonitor.parse_data(test_data)
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
        for test_name, test_data in SOURCE_MONITOR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.SourceMonitor.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SOURCE_MONITOR_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='SourceMonitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='width', name='SourceMonitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='height', name='SourceMonitor'),
            ),

        ),
    ),

]


SOURCE_MONITOR_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 6979094,
            'width': -4524814063687493129,
            'height': 3454035578455864776,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 3794957,

            'width': -4318921526883136033,

            'height': -2914778808719963979,

        },
    ),
]

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
            'source_monitor': -568970,
            'source_nw_x_pixel': -3805497741881196153,
            'source_nw_y_pixel': -9175621529498797304,
            'source_pixel_width': -499287177574655537,
            'source_pixel_height': -7482919004894081785,
            'rotation': -1560953499972986033,
            'virtual_nw_x_pixel': 241672369,
            'virtual_nw_y_pixel': -1053073229,
            'virtual_width': 1106823942,
            'virtual_height': 950900149,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -7905875405219122375,

            'source_nw_y_pixel': -7315259071357998028,

            'source_pixel_width': -1816675918724152953,

            'source_pixel_height': -7076365448111649973,

            'rotation': -1643907170233497471,

            'virtual_nw_x_pixel': -1571666032,

            'virtual_nw_y_pixel': 662117043,

            'virtual_width': -1138497609,

            'virtual_height': 1598925107,

        },
    ),
]

class ScreenMonitorMappingConfigGroupTest(unittest.TestCase):
    """
    Tests for ScreenMonitorMappingConfigGroup
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SCREEN_MONITOR_MAPPING_CONFIG_GROUP_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.ScreenMonitorMappingConfigGroup.parse_data(test_data)
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
        for test_name, test_data in SCREEN_MONITOR_MAPPING_CONFIG_GROUP_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.ScreenMonitorMappingConfigGroup.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SCREEN_MONITOR_MAPPING_CONFIG_GROUP_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='monitors', name='ScreenMonitorMappingConfigGroup'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='screen', name='ScreenMonitorMappingConfigGroup'),
            ),

        ),
    ),

]


SCREEN_MONITOR_MAPPING_CONFIG_GROUP_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'description': '/ȩԣӜdӞԎȌǽØĂ˾Ϳәx˹YҠģҙʂĮťȌĶʭȿ\x9bԬö',
            'monitors': [
                {
                    'identifier': 2582304,
                    'width': 8866880247547196297,
                    'height': 8904478320419207125,
                },
                {
                    'identifier': 2508142,
                    'width': -3128331628750835695,
                    'height': -5933445564421750640,
                },
                {
                    'identifier': 999897,
                    'width': 8074526470486317625,
                    'height': 4162681909472711378,
                },
                {
                    'identifier': 751861,
                    'width': 2625535913559320583,
                    'height': -441214580129458431,
                },
                {
                    'identifier': 6419641,
                    'width': 4903944744825814626,
                    'height': -3469691574930824431,
                },
                {
                    'identifier': 5531882,
                    'width': 3476798882303484254,
                    'height': 1732866017462059874,
                },
                {
                    'identifier': 7419477,
                    'width': -5403522793102078662,
                    'height': 8091940640015966562,
                },
                {
                    'identifier': 6503330,
                    'width': -3840625113282761770,
                    'height': 4687364601316085584,
                },
                {
                    'identifier': 1113030,
                    'width': 1422713883612621685,
                    'height': -4169226361231992788,
                },
                {
                    'identifier': 4376765,
                    'width': -2822283138635845769,
                    'height': -7055309960049892283,
                },
            ],
            'screen': [
                {
                    'source_monitor': 4969190,
                    'source_nw_x_pixel': -4440938813295230942,
                    'source_nw_y_pixel': -1201697712739916963,
                    'source_pixel_width': -3384838365679650230,
                    'source_pixel_height': -3491241909061371310,
                    'rotation': -2771882035267700715,
                    'virtual_nw_x_pixel': -1391296491,
                    'virtual_nw_y_pixel': -1628600439,
                    'virtual_width': -14993345,
                    'virtual_height': -310146172,
                },
                {
                    'source_monitor': 9085815,
                    'source_nw_x_pixel': -5055536633105273197,
                    'source_nw_y_pixel': -4538713832067372254,
                    'source_pixel_width': -5946799727540525018,
                    'source_pixel_height': -3261590140336459505,
                    'rotation': -2027800587897379454,
                    'virtual_nw_x_pixel': -1005026436,
                    'virtual_nw_y_pixel': -1253455921,
                    'virtual_width': -843150083,
                    'virtual_height': 1881859335,
                },
                {
                    'source_monitor': 3606151,
                    'source_nw_x_pixel': -2224079159854275509,
                    'source_nw_y_pixel': -2943540733425931327,
                    'source_pixel_width': -977215313317049292,
                    'source_pixel_height': -7339430943321299936,
                    'rotation': -5378277849698070011,
                    'virtual_nw_x_pixel': -1473492075,
                    'virtual_nw_y_pixel': -1049487872,
                    'virtual_width': 498280714,
                    'virtual_height': 1781672268,
                },
                {
                    'source_monitor': 6752496,
                    'source_nw_x_pixel': -6393336554559218050,
                    'source_nw_y_pixel': -6519289677314732535,
                    'source_pixel_width': -5140741742048998989,
                    'source_pixel_height': -5703331093079772374,
                    'rotation': -5191513799669657557,
                    'virtual_nw_x_pixel': -1549595224,
                    'virtual_nw_y_pixel': 749538786,
                    'virtual_width': -255532461,
                    'virtual_height': 1793729020,
                },
                {
                    'source_monitor': 6525578,
                    'source_nw_x_pixel': -3648991795233326267,
                    'source_nw_y_pixel': -598319405831816764,
                    'source_pixel_width': -2257155599796524260,
                    'source_pixel_height': -6453546839469805545,
                    'rotation': -5182119179454295018,
                    'virtual_nw_x_pixel': 1967841950,
                    'virtual_nw_y_pixel': 1147845514,
                    'virtual_width': -657056457,
                    'virtual_height': -1351491868,
                },
                {
                    'source_monitor': -513969,
                    'source_nw_x_pixel': -3282045843604966288,
                    'source_nw_y_pixel': -8024703591744334975,
                    'source_pixel_width': -4160221816460360321,
                    'source_pixel_height': -501180331201068374,
                    'rotation': -5006046104321646254,
                    'virtual_nw_x_pixel': 679206007,
                    'virtual_nw_y_pixel': 1792641831,
                    'virtual_width': -1735357578,
                    'virtual_height': -301329763,
                },
                {
                    'source_monitor': 9749698,
                    'source_nw_x_pixel': -1485149479315399409,
                    'source_nw_y_pixel': -7211224512653642949,
                    'source_pixel_width': -796620798470692759,
                    'source_pixel_height': -5976538754873062729,
                    'rotation': -1373929541361807500,
                    'virtual_nw_x_pixel': 1600279083,
                    'virtual_nw_y_pixel': -206197058,
                    'virtual_width': 601256480,
                    'virtual_height': 65185664,
                },
                {
                    'source_monitor': 8790340,
                    'source_nw_x_pixel': -888698687072919501,
                    'source_nw_y_pixel': -7818573151720920820,
                    'source_pixel_width': -4367132400163218875,
                    'source_pixel_height': -2738895241350042178,
                    'rotation': -2824602117001232630,
                    'virtual_nw_x_pixel': 955340756,
                    'virtual_nw_y_pixel': 874108919,
                    'virtual_width': 1533406690,
                    'virtual_height': -213159306,
                },
                {
                    'source_monitor': 6537210,
                    'source_nw_x_pixel': -6105045236178656461,
                    'source_nw_y_pixel': -1186232746150804509,
                    'source_pixel_width': -2564599185691138142,
                    'source_pixel_height': -1689420831060735380,
                    'rotation': -934304681558795214,
                    'virtual_nw_x_pixel': -686151731,
                    'virtual_nw_y_pixel': 1227869703,
                    'virtual_width': -1862931229,
                    'virtual_height': 1356183458,
                },
                {
                    'source_monitor': 6534593,
                    'source_nw_x_pixel': -2275779752571243779,
                    'source_nw_y_pixel': -9221129464368321269,
                    'source_pixel_width': -6703552923888202946,
                    'source_pixel_height': -8097578807429397380,
                    'rotation': -854326053593363412,
                    'virtual_nw_x_pixel': -363442749,
                    'virtual_nw_y_pixel': -133246714,
                    'virtual_width': -71734,
                    'virtual_height': -539633695,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 5643583,
                    'width': -5960844618567172388,
                    'height': -5467103574513737067,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -8411206615562693420,
                    'source_nw_y_pixel': -4668412677019554840,
                    'source_pixel_width': -8777336380922940993,
                    'source_pixel_height': -2458603688527515099,
                    'rotation': -3285016787706147676,
                    'virtual_nw_x_pixel': 1180259356,
                    'virtual_nw_y_pixel': 1531937109,
                    'virtual_width': -1975640713,
                    'virtual_height': 1315215466,
                },
            ],

        },
    ),
]

class SetScreenConfigurationRequestEventTest(unittest.TestCase):
    """
    Tests for SetScreenConfigurationRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_SCREEN_CONFIGURATION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.SetScreenConfigurationRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SET_SCREEN_CONFIGURATION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.SetScreenConfigurationRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_SCREEN_CONFIGURATION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='request_id', name='SetScreenConfigurationRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='mapped_screens_by_monitors', name='SetScreenConfigurationRequestEvent'),
            ),

        ),
    ),

]


SET_SCREEN_CONFIGURATION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'request_id': -477714,
            'mapped_screens_by_monitors': [
                {
                    'description': 'Ŧ˧ҚԈҢ˜ҒΚĔпəķǿԟҸЗćĪźɗϡ҈2Ӊєȓʹ=ǔʢ',
                    'monitors': [
                            {
                                        'identifier': 2186059,
                                        'width': -6408256319594354627,
                                        'height': 1450709918550831671,
                                    },
                            {
                                        'identifier': 5965644,
                                        'width': -1991270358988538065,
                                        'height': 6125028056497835515,
                                    },
                            {
                                        'identifier': 9190656,
                                        'width': -8650707697292138282,
                                        'height': -4480262147737180940,
                                    },
                            {
                                        'identifier': 1339949,
                                        'width': 2050208775156461650,
                                        'height': -7929679324959231090,
                                    },
                            {
                                        'identifier': 2973691,
                                        'width': -5104875086788933319,
                                        'height': 6771417707484986197,
                                    },
                            {
                                        'identifier': 1118050,
                                        'width': 1723778292698937211,
                                        'height': 7406382049778157429,
                                    },
                            {
                                        'identifier': 6381102,
                                        'width': -4538752729109329598,
                                        'height': 3676220279798868808,
                                    },
                            {
                                        'identifier': 6549769,
                                        'width': 313621156734363729,
                                        'height': 4249406638514954955,
                                    },
                            {
                                        'identifier': 9450148,
                                        'width': 2365871129394663844,
                                        'height': 7083500990728006352,
                                    },
                            {
                                        'identifier': 5476905,
                                        'width': -7104773078084733763,
                                        'height': 3998192511518046819,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5436640,
                                        'source_nw_x_pixel': -4450678961833985597,
                                        'source_nw_y_pixel': -5005089971037234914,
                                        'source_pixel_width': -5796734291571117495,
                                        'source_pixel_height': -9184386501519732434,
                                        'rotation': -3071417563898008049,
                                        'virtual_nw_x_pixel': 213384523,
                                        'virtual_nw_y_pixel': -315231233,
                                        'virtual_width': 192571232,
                                        'virtual_height': -1604335244,
                                    },
                            {
                                        'source_monitor': 7509025,
                                        'source_nw_x_pixel': -6084166832621276806,
                                        'source_nw_y_pixel': -4379765599308056113,
                                        'source_pixel_width': -2844997632359236753,
                                        'source_pixel_height': -1669718578707814752,
                                        'rotation': -6628773725768306259,
                                        'virtual_nw_x_pixel': 1441854051,
                                        'virtual_nw_y_pixel': 656479911,
                                        'virtual_width': -1128509924,
                                        'virtual_height': 840037880,
                                    },
                            {
                                        'source_monitor': 1962187,
                                        'source_nw_x_pixel': -8443059202557226265,
                                        'source_nw_y_pixel': -7220131152429806675,
                                        'source_pixel_width': -4338139333328371422,
                                        'source_pixel_height': -4905504549983351008,
                                        'rotation': -3596842031369295177,
                                        'virtual_nw_x_pixel': 1286721955,
                                        'virtual_nw_y_pixel': -788017747,
                                        'virtual_width': -1722722957,
                                        'virtual_height': -1813790867,
                                    },
                            {
                                        'source_monitor': 8796308,
                                        'source_nw_x_pixel': -2501175844143990055,
                                        'source_nw_y_pixel': -7595370066549947545,
                                        'source_pixel_width': -8865830346742157066,
                                        'source_pixel_height': -1897403632498982164,
                                        'rotation': -4212611926923870129,
                                        'virtual_nw_x_pixel': -198788448,
                                        'virtual_nw_y_pixel': 1795438087,
                                        'virtual_width': 721160338,
                                        'virtual_height': -599657432,
                                    },
                            {
                                        'source_monitor': 8288790,
                                        'source_nw_x_pixel': -4027684472195565783,
                                        'source_nw_y_pixel': -4805075199644657428,
                                        'source_pixel_width': -4561467599706500868,
                                        'source_pixel_height': -667671625386482038,
                                        'rotation': -3224263818563882144,
                                        'virtual_nw_x_pixel': 1457751489,
                                        'virtual_nw_y_pixel': -748010452,
                                        'virtual_width': -1941388689,
                                        'virtual_height': -350570622,
                                    },
                            {
                                        'source_monitor': 3961892,
                                        'source_nw_x_pixel': -8199100458081084248,
                                        'source_nw_y_pixel': -7773723211147435303,
                                        'source_pixel_width': -7263946024401489068,
                                        'source_pixel_height': -8462441352329981899,
                                        'rotation': -1256559723681654217,
                                        'virtual_nw_x_pixel': -1360617050,
                                        'virtual_nw_y_pixel': 143713319,
                                        'virtual_width': -1412587624,
                                        'virtual_height': 1381955337,
                                    },
                            {
                                        'source_monitor': 706044,
                                        'source_nw_x_pixel': -782220505868114860,
                                        'source_nw_y_pixel': -790007286036476676,
                                        'source_pixel_width': -7648984270878184357,
                                        'source_pixel_height': -6142338813894943287,
                                        'rotation': -2509671860813981020,
                                        'virtual_nw_x_pixel': 516753508,
                                        'virtual_nw_y_pixel': -1784188408,
                                        'virtual_width': 746148810,
                                        'virtual_height': 207755413,
                                    },
                            {
                                        'source_monitor': 4262130,
                                        'source_nw_x_pixel': -5196065852321045282,
                                        'source_nw_y_pixel': -2227451566485492070,
                                        'source_pixel_width': -8790547803004202155,
                                        'source_pixel_height': -2995680674234924107,
                                        'rotation': -1576863681794225481,
                                        'virtual_nw_x_pixel': 498801,
                                        'virtual_nw_y_pixel': 1903871558,
                                        'virtual_width': 1078648248,
                                        'virtual_height': 390978097,
                                    },
                            {
                                        'source_monitor': 5516626,
                                        'source_nw_x_pixel': -6274145653944380064,
                                        'source_nw_y_pixel': -4329648362714648481,
                                        'source_pixel_width': -5319671057031727117,
                                        'source_pixel_height': -7326839014108141167,
                                        'rotation': -5176002092926115201,
                                        'virtual_nw_x_pixel': -829278808,
                                        'virtual_nw_y_pixel': 1437501162,
                                        'virtual_width': -246240925,
                                        'virtual_height': -1467873926,
                                    },
                            {
                                        'source_monitor': 4968329,
                                        'source_nw_x_pixel': -1644355581633637523,
                                        'source_nw_y_pixel': -8550635110864561637,
                                        'source_pixel_width': -6130589170748044007,
                                        'source_pixel_height': -4067095128618390062,
                                        'rotation': -7873384907432605542,
                                        'virtual_nw_x_pixel': 1881299639,
                                        'virtual_nw_y_pixel': -1478062961,
                                        'virtual_width': 815871322,
                                        'virtual_height': 1086875063,
                                    },
                        ],
                },
                {
                    'description': 'Šϭʄ˷¢ƤѶͲƩćԉ˾ǭԪѸǸÕƜÊÇч˰ľʢɲϮҗ\u0380қr',
                    'monitors': [
                            {
                                        'identifier': 3077674,
                                        'width': -7665493979882070906,
                                        'height': -2112211972173268587,
                                    },
                            {
                                        'identifier': -489521,
                                        'width': -8470999690821445404,
                                        'height': 1625614666197752879,
                                    },
                            {
                                        'identifier': 1591843,
                                        'width': 899991818764648683,
                                        'height': -4105229745325045294,
                                    },
                            {
                                        'identifier': 5797410,
                                        'width': 3763322437053998086,
                                        'height': 5974661206537662591,
                                    },
                            {
                                        'identifier': 8549293,
                                        'width': 7805767193134175071,
                                        'height': 1751366042251062680,
                                    },
                            {
                                        'identifier': 7510782,
                                        'width': 7214965734719614239,
                                        'height': -2237955333735218669,
                                    },
                            {
                                        'identifier': 7999027,
                                        'width': -1151314481757500677,
                                        'height': -7243998079716931019,
                                    },
                            {
                                        'identifier': 5363242,
                                        'width': 2547781240984514317,
                                        'height': -5242939836632862331,
                                    },
                            {
                                        'identifier': 5398580,
                                        'width': 8321277766437879777,
                                        'height': 1121401957161969754,
                                    },
                            {
                                        'identifier': -837082,
                                        'width': 6683582821062961206,
                                        'height': 4670059202740174475,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8370264,
                                        'source_nw_x_pixel': -6662597174368657009,
                                        'source_nw_y_pixel': -1392210027825775885,
                                        'source_pixel_width': -5022533201705370646,
                                        'source_pixel_height': -913777269574660484,
                                        'rotation': -4751888118571549034,
                                        'virtual_nw_x_pixel': 282946789,
                                        'virtual_nw_y_pixel': 1327056769,
                                        'virtual_width': 1785145249,
                                        'virtual_height': -317718502,
                                    },
                            {
                                        'source_monitor': 821464,
                                        'source_nw_x_pixel': -4202348427763436056,
                                        'source_nw_y_pixel': -481206162333230829,
                                        'source_pixel_width': -836942083032397444,
                                        'source_pixel_height': -3575952611184014292,
                                        'rotation': -4664742440990570151,
                                        'virtual_nw_x_pixel': 862473570,
                                        'virtual_nw_y_pixel': -1050032548,
                                        'virtual_width': 1475114154,
                                        'virtual_height': 365253315,
                                    },
                            {
                                        'source_monitor': 1369294,
                                        'source_nw_x_pixel': -2132321405125405980,
                                        'source_nw_y_pixel': -6275678192937728923,
                                        'source_pixel_width': -489082000894476368,
                                        'source_pixel_height': -4959090378000923508,
                                        'rotation': -1668688101451655221,
                                        'virtual_nw_x_pixel': -122609120,
                                        'virtual_nw_y_pixel': 125311141,
                                        'virtual_width': -1676242185,
                                        'virtual_height': 430939050,
                                    },
                            {
                                        'source_monitor': 347418,
                                        'source_nw_x_pixel': -818047158127788568,
                                        'source_nw_y_pixel': -6613640861785137293,
                                        'source_pixel_width': -3832954855211455770,
                                        'source_pixel_height': -5447451304912974218,
                                        'rotation': -884504644384002528,
                                        'virtual_nw_x_pixel': -1068423522,
                                        'virtual_nw_y_pixel': -77031144,
                                        'virtual_width': -1961685140,
                                        'virtual_height': -187250076,
                                    },
                            {
                                        'source_monitor': -770288,
                                        'source_nw_x_pixel': -4220427742413943780,
                                        'source_nw_y_pixel': -4172798754814589058,
                                        'source_pixel_width': -4782869538557844145,
                                        'source_pixel_height': -3519172973106395498,
                                        'rotation': -3971380174020020506,
                                        'virtual_nw_x_pixel': 169722685,
                                        'virtual_nw_y_pixel': 1399726844,
                                        'virtual_width': -1575266770,
                                        'virtual_height': 967002439,
                                    },
                            {
                                        'source_monitor': 1204405,
                                        'source_nw_x_pixel': -2951113387223606676,
                                        'source_nw_y_pixel': -6663834007410589994,
                                        'source_pixel_width': -614222555130205719,
                                        'source_pixel_height': -570016847553096337,
                                        'rotation': -5013638511724811442,
                                        'virtual_nw_x_pixel': -264879420,
                                        'virtual_nw_y_pixel': 716350029,
                                        'virtual_width': 1633273668,
                                        'virtual_height': -426084550,
                                    },
                            {
                                        'source_monitor': 5475831,
                                        'source_nw_x_pixel': -4469124269159396281,
                                        'source_nw_y_pixel': -5529748771481659048,
                                        'source_pixel_width': -7949462398437745591,
                                        'source_pixel_height': -1016988756809787790,
                                        'rotation': -1626428666352625474,
                                        'virtual_nw_x_pixel': 646955007,
                                        'virtual_nw_y_pixel': -1841468496,
                                        'virtual_width': -1865780786,
                                        'virtual_height': 91370204,
                                    },
                            {
                                        'source_monitor': 3096767,
                                        'source_nw_x_pixel': -4929238700221203838,
                                        'source_nw_y_pixel': -4619036064944633633,
                                        'source_pixel_width': -4744945074770549082,
                                        'source_pixel_height': -7183021536206073765,
                                        'rotation': -55602245627615943,
                                        'virtual_nw_x_pixel': -1450169684,
                                        'virtual_nw_y_pixel': 1156072943,
                                        'virtual_width': 445171055,
                                        'virtual_height': -1922403606,
                                    },
                            {
                                        'source_monitor': 4145658,
                                        'source_nw_x_pixel': -3195852840714749059,
                                        'source_nw_y_pixel': -7162713588764114981,
                                        'source_pixel_width': -4141656015024826356,
                                        'source_pixel_height': -4197517237482291687,
                                        'rotation': -1166445294409270882,
                                        'virtual_nw_x_pixel': 1541610194,
                                        'virtual_nw_y_pixel': -969114566,
                                        'virtual_width': -944514022,
                                        'virtual_height': -882138181,
                                    },
                            {
                                        'source_monitor': -642730,
                                        'source_nw_x_pixel': -2361546391679545648,
                                        'source_nw_y_pixel': -6417389093657920270,
                                        'source_pixel_width': -4343631247169988885,
                                        'source_pixel_height': -760395514823330907,
                                        'rotation': -6520273035103386013,
                                        'virtual_nw_x_pixel': -1618561780,
                                        'virtual_nw_y_pixel': 1147804937,
                                        'virtual_width': 1210416788,
                                        'virtual_height': -991087886,
                                    },
                        ],
                },
                {
                    'description': 'ãѮӿΩ\x87ŨΑšɄƌǲΔÕǅӍҗ&ƹˈƆυӨзЊĩʳƓфĘҮ',
                    'monitors': [
                            {
                                        'identifier': 2432371,
                                        'width': 2638350241048976532,
                                        'height': 7867431393076737401,
                                    },
                            {
                                        'identifier': 1694412,
                                        'width': 4922351920492920927,
                                        'height': -8885309312170531605,
                                    },
                            {
                                        'identifier': 6468621,
                                        'width': 7184102046393771371,
                                        'height': -1594009081757607747,
                                    },
                            {
                                        'identifier': 9840901,
                                        'width': -4554232314224968930,
                                        'height': 4993236162905783051,
                                    },
                            {
                                        'identifier': 8435659,
                                        'width': -6148845461645651855,
                                        'height': 6265484345296955877,
                                    },
                            {
                                        'identifier': 1127915,
                                        'width': 2763118046550577770,
                                        'height': -8108397644023937036,
                                    },
                            {
                                        'identifier': 9791536,
                                        'width': -7652383646705886109,
                                        'height': -6407985460878224940,
                                    },
                            {
                                        'identifier': 2990553,
                                        'width': -2062242811374018524,
                                        'height': -1494016896713649419,
                                    },
                            {
                                        'identifier': 8046948,
                                        'width': -5016930956438350126,
                                        'height': -1983663804984862359,
                                    },
                            {
                                        'identifier': 4585100,
                                        'width': -5783550548064395510,
                                        'height': 4210961847008116109,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9477259,
                                        'source_nw_x_pixel': -8835130054215826043,
                                        'source_nw_y_pixel': -692172287127784775,
                                        'source_pixel_width': -4154988744654760261,
                                        'source_pixel_height': -1958165131130467029,
                                        'rotation': -2514005665842030038,
                                        'virtual_nw_x_pixel': 1048802598,
                                        'virtual_nw_y_pixel': -1804331414,
                                        'virtual_width': -1381050152,
                                        'virtual_height': 1112185578,
                                    },
                            {
                                        'source_monitor': 8022072,
                                        'source_nw_x_pixel': -6218520594590891923,
                                        'source_nw_y_pixel': -8972940349962119053,
                                        'source_pixel_width': -6542173165543151415,
                                        'source_pixel_height': -3531717387082998412,
                                        'rotation': -7117325534247730575,
                                        'virtual_nw_x_pixel': -1310049742,
                                        'virtual_nw_y_pixel': 1926098001,
                                        'virtual_width': -1700517213,
                                        'virtual_height': 1261227812,
                                    },
                            {
                                        'source_monitor': 1845963,
                                        'source_nw_x_pixel': -9203660811167651498,
                                        'source_nw_y_pixel': -54163524583311563,
                                        'source_pixel_width': -7683581817847432009,
                                        'source_pixel_height': -5345250062630223689,
                                        'rotation': -1960705450908773522,
                                        'virtual_nw_x_pixel': 1231602657,
                                        'virtual_nw_y_pixel': 611186066,
                                        'virtual_width': -844430591,
                                        'virtual_height': 1452189334,
                                    },
                            {
                                        'source_monitor': 2633048,
                                        'source_nw_x_pixel': -4463442088570466165,
                                        'source_nw_y_pixel': -4979403735398640304,
                                        'source_pixel_width': -1342049188836183523,
                                        'source_pixel_height': -8307516750333029744,
                                        'rotation': -6335313034068690206,
                                        'virtual_nw_x_pixel': 309502461,
                                        'virtual_nw_y_pixel': 1927440828,
                                        'virtual_width': 69185844,
                                        'virtual_height': 357953372,
                                    },
                            {
                                        'source_monitor': 9621604,
                                        'source_nw_x_pixel': -3757277100716471786,
                                        'source_nw_y_pixel': -6972893104335401279,
                                        'source_pixel_width': -5567470554393406309,
                                        'source_pixel_height': -5613018832295469855,
                                        'rotation': -1992566154549140981,
                                        'virtual_nw_x_pixel': -1561851760,
                                        'virtual_nw_y_pixel': -987072701,
                                        'virtual_width': -1055076167,
                                        'virtual_height': 1962477602,
                                    },
                            {
                                        'source_monitor': 3903779,
                                        'source_nw_x_pixel': -3114710238347721085,
                                        'source_nw_y_pixel': -4933457331552543346,
                                        'source_pixel_width': -1250090418069483578,
                                        'source_pixel_height': -6014922579672710511,
                                        'rotation': -8463800016372369337,
                                        'virtual_nw_x_pixel': -392177376,
                                        'virtual_nw_y_pixel': -405334551,
                                        'virtual_width': -1169625665,
                                        'virtual_height': -916285194,
                                    },
                            {
                                        'source_monitor': 3485864,
                                        'source_nw_x_pixel': -2019968588632453063,
                                        'source_nw_y_pixel': -6129198094042959536,
                                        'source_pixel_width': -1159763148041664450,
                                        'source_pixel_height': -2250943812802586781,
                                        'rotation': -2242879972203056204,
                                        'virtual_nw_x_pixel': 1271618792,
                                        'virtual_nw_y_pixel': 1154557058,
                                        'virtual_width': -1942633616,
                                        'virtual_height': 1456306083,
                                    },
                            {
                                        'source_monitor': 6186910,
                                        'source_nw_x_pixel': -547423074688178303,
                                        'source_nw_y_pixel': -620426353977840931,
                                        'source_pixel_width': -5958673085172513378,
                                        'source_pixel_height': -51868690344925127,
                                        'rotation': -8401327745177455566,
                                        'virtual_nw_x_pixel': 1710005724,
                                        'virtual_nw_y_pixel': 1594847402,
                                        'virtual_width': -46139404,
                                        'virtual_height': 375066784,
                                    },
                            {
                                        'source_monitor': 5743299,
                                        'source_nw_x_pixel': -4201011138431719595,
                                        'source_nw_y_pixel': -6427617535190944269,
                                        'source_pixel_width': -7373471472861716881,
                                        'source_pixel_height': -2610135957426503239,
                                        'rotation': -7167324654753752340,
                                        'virtual_nw_x_pixel': -504373102,
                                        'virtual_nw_y_pixel': 330683237,
                                        'virtual_width': 292835762,
                                        'virtual_height': -1991412923,
                                    },
                            {
                                        'source_monitor': 422447,
                                        'source_nw_x_pixel': -816592711550495149,
                                        'source_nw_y_pixel': -3892951258141082093,
                                        'source_pixel_width': -7540347435506086746,
                                        'source_pixel_height': -5741130772356494600,
                                        'rotation': -6841871947160873561,
                                        'virtual_nw_x_pixel': -903723928,
                                        'virtual_nw_y_pixel': -571736284,
                                        'virtual_width': -665324863,
                                        'virtual_height': 596379618,
                                    },
                        ],
                },
                {
                    'description': '˷ǥʙˆăCσ¬\x9dҿːƴǙуѓΡĢI˼ɎԇœҀɰ˷~ŁȃԋЭ',
                    'monitors': [
                            {
                                        'identifier': 8383589,
                                        'width': -6091898438762520882,
                                        'height': -7398727734577264498,
                                    },
                            {
                                        'identifier': 9069810,
                                        'width': -6441853645590533701,
                                        'height': -9099494210984541198,
                                    },
                            {
                                        'identifier': 6047555,
                                        'width': 8825864381314878401,
                                        'height': 8013591015188971071,
                                    },
                            {
                                        'identifier': -24111,
                                        'width': 2158097530883488695,
                                        'height': -4604560443254948800,
                                    },
                            {
                                        'identifier': 458234,
                                        'width': -6714587441263946494,
                                        'height': 2473667745413123336,
                                    },
                            {
                                        'identifier': 9765291,
                                        'width': 834114670775306774,
                                        'height': -3728019252017461249,
                                    },
                            {
                                        'identifier': -851389,
                                        'width': 8695804144879318716,
                                        'height': -2286426622990802962,
                                    },
                            {
                                        'identifier': 9905251,
                                        'width': -1443632479861134346,
                                        'height': 789341303633120377,
                                    },
                            {
                                        'identifier': 2337616,
                                        'width': 6512271579944441658,
                                        'height': 7080633361484144673,
                                    },
                            {
                                        'identifier': 2988187,
                                        'width': 3437572995892358048,
                                        'height': 7142537802377579785,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6367228,
                                        'source_nw_x_pixel': -4226289150469461033,
                                        'source_nw_y_pixel': -9101912958508958920,
                                        'source_pixel_width': -3940346990766860710,
                                        'source_pixel_height': -1652135672682477758,
                                        'rotation': -8708118279384400251,
                                        'virtual_nw_x_pixel': -855248132,
                                        'virtual_nw_y_pixel': 1357355153,
                                        'virtual_width': 1441887392,
                                        'virtual_height': 922243525,
                                    },
                            {
                                        'source_monitor': 2298153,
                                        'source_nw_x_pixel': -8263320280354314486,
                                        'source_nw_y_pixel': -6786228510699115018,
                                        'source_pixel_width': -1435077750524879957,
                                        'source_pixel_height': -8309502125988560869,
                                        'rotation': -5948393729238226447,
                                        'virtual_nw_x_pixel': -37909039,
                                        'virtual_nw_y_pixel': 1645935844,
                                        'virtual_width': -766599327,
                                        'virtual_height': 865687588,
                                    },
                            {
                                        'source_monitor': 9274695,
                                        'source_nw_x_pixel': -3345444552476420103,
                                        'source_nw_y_pixel': -1552437010069070904,
                                        'source_pixel_width': -5545081442420933064,
                                        'source_pixel_height': -8871343867357753997,
                                        'rotation': -154374804208249777,
                                        'virtual_nw_x_pixel': -1723679127,
                                        'virtual_nw_y_pixel': -321943500,
                                        'virtual_width': 574888792,
                                        'virtual_height': 1329618635,
                                    },
                            {
                                        'source_monitor': -541070,
                                        'source_nw_x_pixel': -6774563759312574228,
                                        'source_nw_y_pixel': -2818575312476497891,
                                        'source_pixel_width': -4173223592303042990,
                                        'source_pixel_height': -5635479255552876023,
                                        'rotation': -6908306809823502168,
                                        'virtual_nw_x_pixel': 1577849266,
                                        'virtual_nw_y_pixel': -398710417,
                                        'virtual_width': 1778903795,
                                        'virtual_height': 146365190,
                                    },
                            {
                                        'source_monitor': 3010041,
                                        'source_nw_x_pixel': -314994831481303357,
                                        'source_nw_y_pixel': -8629252655619392274,
                                        'source_pixel_width': -6283713124641004973,
                                        'source_pixel_height': -5728096331183482459,
                                        'rotation': -2641520533440351087,
                                        'virtual_nw_x_pixel': 1855515592,
                                        'virtual_nw_y_pixel': 1670330679,
                                        'virtual_width': 168816728,
                                        'virtual_height': 620440170,
                                    },
                            {
                                        'source_monitor': 4531775,
                                        'source_nw_x_pixel': -4718850966603387604,
                                        'source_nw_y_pixel': -4828435300236487293,
                                        'source_pixel_width': -8365712868103489643,
                                        'source_pixel_height': -4933773729428688284,
                                        'rotation': -3721991085413981442,
                                        'virtual_nw_x_pixel': -663401269,
                                        'virtual_nw_y_pixel': -1121019091,
                                        'virtual_width': 1409624546,
                                        'virtual_height': 155506682,
                                    },
                            {
                                        'source_monitor': 7865020,
                                        'source_nw_x_pixel': -3756929942864869002,
                                        'source_nw_y_pixel': -6891573818530324143,
                                        'source_pixel_width': -5625902774241231308,
                                        'source_pixel_height': -1112702795230016597,
                                        'rotation': -2598274736398166593,
                                        'virtual_nw_x_pixel': -1023189662,
                                        'virtual_nw_y_pixel': 1095629751,
                                        'virtual_width': -212883029,
                                        'virtual_height': -1683396113,
                                    },
                            {
                                        'source_monitor': -648367,
                                        'source_nw_x_pixel': -5246910172099128267,
                                        'source_nw_y_pixel': -7300710836897913831,
                                        'source_pixel_width': -4327166958351434662,
                                        'source_pixel_height': -8138865306438932106,
                                        'rotation': -1690362996520228819,
                                        'virtual_nw_x_pixel': 779220497,
                                        'virtual_nw_y_pixel': 846819904,
                                        'virtual_width': 1210939871,
                                        'virtual_height': -1218038033,
                                    },
                            {
                                        'source_monitor': 3872567,
                                        'source_nw_x_pixel': -6541711202201344974,
                                        'source_nw_y_pixel': -1635887201097204485,
                                        'source_pixel_width': -2405263301816278117,
                                        'source_pixel_height': -1595345009155361613,
                                        'rotation': -7472031647734905148,
                                        'virtual_nw_x_pixel': 211471038,
                                        'virtual_nw_y_pixel': -1121253585,
                                        'virtual_width': -1387478797,
                                        'virtual_height': 964102104,
                                    },
                            {
                                        'source_monitor': 5748339,
                                        'source_nw_x_pixel': -2963327751866534464,
                                        'source_nw_y_pixel': -4467467111091293776,
                                        'source_pixel_width': -1306615371747715217,
                                        'source_pixel_height': -7120181245444081034,
                                        'rotation': -5610457191936690175,
                                        'virtual_nw_x_pixel': 841648855,
                                        'virtual_nw_y_pixel': -950912768,
                                        'virtual_width': 278248957,
                                        'virtual_height': 1162494931,
                                    },
                        ],
                },
                {
                    'description': 'ŦzÓŪȑԛҙ8ψəӪÂȊɜƅǆɤȳʦøÌƪñªԣ˘ѐʫӠԟ',
                    'monitors': [
                            {
                                        'identifier': 2873810,
                                        'width': 3412717396446012328,
                                        'height': -3248049150050035763,
                                    },
                            {
                                        'identifier': 2794243,
                                        'width': 4646193963421032654,
                                        'height': -3167821766717173500,
                                    },
                            {
                                        'identifier': 5161476,
                                        'width': -391307624396860827,
                                        'height': 1342587729552267332,
                                    },
                            {
                                        'identifier': 2362044,
                                        'width': -867657472084863355,
                                        'height': -5633955974828663298,
                                    },
                            {
                                        'identifier': -226598,
                                        'width': 7067902525695671259,
                                        'height': -3307161505980214907,
                                    },
                            {
                                        'identifier': 7998110,
                                        'width': -3647909109148650312,
                                        'height': -3152492565118180274,
                                    },
                            {
                                        'identifier': 2254102,
                                        'width': -6530443283596454538,
                                        'height': 2087817100485279169,
                                    },
                            {
                                        'identifier': 9685041,
                                        'width': -5891820575123660457,
                                        'height': 2092088426123778172,
                                    },
                            {
                                        'identifier': 103549,
                                        'width': 2540202466568012501,
                                        'height': -8121199756122177324,
                                    },
                            {
                                        'identifier': 3772092,
                                        'width': 7315299794859178786,
                                        'height': -8622404819231851649,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9079552,
                                        'source_nw_x_pixel': -667704644085053065,
                                        'source_nw_y_pixel': -841853552343077588,
                                        'source_pixel_width': -3857436022119057383,
                                        'source_pixel_height': -947896592930812948,
                                        'rotation': -6599373223257580280,
                                        'virtual_nw_x_pixel': -686294673,
                                        'virtual_nw_y_pixel': 1697804874,
                                        'virtual_width': -818977767,
                                        'virtual_height': 507001123,
                                    },
                            {
                                        'source_monitor': 4468482,
                                        'source_nw_x_pixel': -4180825993494978256,
                                        'source_nw_y_pixel': -7617567666739678601,
                                        'source_pixel_width': -5545501229798881653,
                                        'source_pixel_height': -8921176447224870236,
                                        'rotation': -253461977409265863,
                                        'virtual_nw_x_pixel': 987958739,
                                        'virtual_nw_y_pixel': 311179037,
                                        'virtual_width': -924200375,
                                        'virtual_height': 403487535,
                                    },
                            {
                                        'source_monitor': 5346049,
                                        'source_nw_x_pixel': -2346745273209127686,
                                        'source_nw_y_pixel': -152012464726200991,
                                        'source_pixel_width': -437280749519466839,
                                        'source_pixel_height': -1463986413619866057,
                                        'rotation': -5161857688830594439,
                                        'virtual_nw_x_pixel': -1629160851,
                                        'virtual_nw_y_pixel': 500783474,
                                        'virtual_width': -818948978,
                                        'virtual_height': 131737372,
                                    },
                            {
                                        'source_monitor': 600830,
                                        'source_nw_x_pixel': -8518478021601166909,
                                        'source_nw_y_pixel': -1341693170445922274,
                                        'source_pixel_width': -6355179490620173734,
                                        'source_pixel_height': -4184085008119991415,
                                        'rotation': -4436019203826330051,
                                        'virtual_nw_x_pixel': 87514021,
                                        'virtual_nw_y_pixel': -576056134,
                                        'virtual_width': 346646,
                                        'virtual_height': -1241457795,
                                    },
                            {
                                        'source_monitor': 2674172,
                                        'source_nw_x_pixel': -8885228878354214581,
                                        'source_nw_y_pixel': -133428828140276539,
                                        'source_pixel_width': -5972487878319762870,
                                        'source_pixel_height': -4752962191873957930,
                                        'rotation': -5549487885232155765,
                                        'virtual_nw_x_pixel': 490097951,
                                        'virtual_nw_y_pixel': 797898588,
                                        'virtual_width': -1097596845,
                                        'virtual_height': 1832763596,
                                    },
                            {
                                        'source_monitor': -25688,
                                        'source_nw_x_pixel': -6873779085924467383,
                                        'source_nw_y_pixel': -6096277972710902934,
                                        'source_pixel_width': -2002823657899471180,
                                        'source_pixel_height': -1847149966501594563,
                                        'rotation': -2271121423542625524,
                                        'virtual_nw_x_pixel': -1282023758,
                                        'virtual_nw_y_pixel': 1434235822,
                                        'virtual_width': 618801633,
                                        'virtual_height': 228732211,
                                    },
                            {
                                        'source_monitor': 9213755,
                                        'source_nw_x_pixel': -97570177350529096,
                                        'source_nw_y_pixel': -6622808420179258695,
                                        'source_pixel_width': -2018032999726365659,
                                        'source_pixel_height': -3445899826786849473,
                                        'rotation': -3163589217443162464,
                                        'virtual_nw_x_pixel': -1861134007,
                                        'virtual_nw_y_pixel': 1630615146,
                                        'virtual_width': -819484207,
                                        'virtual_height': -270308961,
                                    },
                            {
                                        'source_monitor': -898008,
                                        'source_nw_x_pixel': -3332226657452990316,
                                        'source_nw_y_pixel': -6978178613883192672,
                                        'source_pixel_width': -3848252695081501246,
                                        'source_pixel_height': -6871838730021123110,
                                        'rotation': -8947231224190986472,
                                        'virtual_nw_x_pixel': -535640296,
                                        'virtual_nw_y_pixel': -1183552570,
                                        'virtual_width': 1054692347,
                                        'virtual_height': 292669876,
                                    },
                            {
                                        'source_monitor': 3160779,
                                        'source_nw_x_pixel': -6253348187745056798,
                                        'source_nw_y_pixel': -9037387937630042892,
                                        'source_pixel_width': -4283552214158010511,
                                        'source_pixel_height': -1359292311859893988,
                                        'rotation': -4026873528859435627,
                                        'virtual_nw_x_pixel': 152691400,
                                        'virtual_nw_y_pixel': 1365511176,
                                        'virtual_width': -1732371487,
                                        'virtual_height': 1320996389,
                                    },
                            {
                                        'source_monitor': 4753533,
                                        'source_nw_x_pixel': -7592759230316973848,
                                        'source_nw_y_pixel': -5865481433059205623,
                                        'source_pixel_width': -8356374576127050784,
                                        'source_pixel_height': -892157287892742541,
                                        'rotation': -8272778799154998472,
                                        'virtual_nw_x_pixel': 924796701,
                                        'virtual_nw_y_pixel': 463910654,
                                        'virtual_width': 1736903268,
                                        'virtual_height': -992425274,
                                    },
                        ],
                },
                {
                    'description': 'ʻǶȐɥĂǕȑÎιʬҢϤȻǯҪԝDԀоųČūѧ˱/ĂǾΏƣΩ',
                    'monitors': [
                            {
                                        'identifier': -859058,
                                        'width': 2927467020736961953,
                                        'height': -7708838871101065491,
                                    },
                            {
                                        'identifier': 9803533,
                                        'width': -6696941133365629193,
                                        'height': 7420018210293483735,
                                    },
                            {
                                        'identifier': 7856965,
                                        'width': -2049520230094699692,
                                        'height': -2461507478542042478,
                                    },
                            {
                                        'identifier': 2359265,
                                        'width': 2631859706909113485,
                                        'height': -6397044242292625762,
                                    },
                            {
                                        'identifier': -91060,
                                        'width': -2663158263191117375,
                                        'height': 7714108760390777849,
                                    },
                            {
                                        'identifier': -245254,
                                        'width': 1763459020162638351,
                                        'height': -4855626915206136772,
                                    },
                            {
                                        'identifier': 9172526,
                                        'width': 2175267853260819471,
                                        'height': -1821793395252367404,
                                    },
                            {
                                        'identifier': 6655313,
                                        'width': 4441007477598156946,
                                        'height': 5548472659927137278,
                                    },
                            {
                                        'identifier': 3627783,
                                        'width': 3656976296873158305,
                                        'height': 3835564275051320768,
                                    },
                            {
                                        'identifier': 8971347,
                                        'width': 3801189335628969136,
                                        'height': 5911158565330710718,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 670892,
                                        'source_nw_x_pixel': -3091179778461338539,
                                        'source_nw_y_pixel': -3438749630946533643,
                                        'source_pixel_width': -4875751725839195323,
                                        'source_pixel_height': -6355923707581615116,
                                        'rotation': -4345893981105692850,
                                        'virtual_nw_x_pixel': 388297403,
                                        'virtual_nw_y_pixel': 690105428,
                                        'virtual_width': 556566907,
                                        'virtual_height': 307098287,
                                    },
                            {
                                        'source_monitor': 4836008,
                                        'source_nw_x_pixel': -6764030028260930608,
                                        'source_nw_y_pixel': -7256898355210698407,
                                        'source_pixel_width': -163927084631546496,
                                        'source_pixel_height': -6377944015990311605,
                                        'rotation': -5541050193499082732,
                                        'virtual_nw_x_pixel': 584170526,
                                        'virtual_nw_y_pixel': -1524037279,
                                        'virtual_width': -1511194612,
                                        'virtual_height': 967132817,
                                    },
                            {
                                        'source_monitor': 8782427,
                                        'source_nw_x_pixel': -2860311309387946873,
                                        'source_nw_y_pixel': -5580693582619505087,
                                        'source_pixel_width': -6466388456747416531,
                                        'source_pixel_height': -4146965048925021674,
                                        'rotation': -1290979363949474906,
                                        'virtual_nw_x_pixel': -1510650474,
                                        'virtual_nw_y_pixel': 755615879,
                                        'virtual_width': 996166072,
                                        'virtual_height': 1821042091,
                                    },
                            {
                                        'source_monitor': 9965500,
                                        'source_nw_x_pixel': -3382846333948403195,
                                        'source_nw_y_pixel': -6842757256500553857,
                                        'source_pixel_width': -5490564683870639801,
                                        'source_pixel_height': -3001176935990354618,
                                        'rotation': -6883427669988824160,
                                        'virtual_nw_x_pixel': 760186339,
                                        'virtual_nw_y_pixel': 482823620,
                                        'virtual_width': 605533,
                                        'virtual_height': 1532422414,
                                    },
                            {
                                        'source_monitor': 4816307,
                                        'source_nw_x_pixel': -4753593890488381757,
                                        'source_nw_y_pixel': -6967377572272869418,
                                        'source_pixel_width': -5565842434629402442,
                                        'source_pixel_height': -8570146007565819744,
                                        'rotation': -2695184080626888027,
                                        'virtual_nw_x_pixel': 39206443,
                                        'virtual_nw_y_pixel': 1533506829,
                                        'virtual_width': 5359817,
                                        'virtual_height': 625406333,
                                    },
                            {
                                        'source_monitor': 8600356,
                                        'source_nw_x_pixel': -889009012399087657,
                                        'source_nw_y_pixel': -7210837301539286724,
                                        'source_pixel_width': -1019554829575921772,
                                        'source_pixel_height': -3938073052333644765,
                                        'rotation': -2627141899124581933,
                                        'virtual_nw_x_pixel': -1908733719,
                                        'virtual_nw_y_pixel': 155006875,
                                        'virtual_width': -137623842,
                                        'virtual_height': 983761446,
                                    },
                            {
                                        'source_monitor': 2480141,
                                        'source_nw_x_pixel': -2055752012575722688,
                                        'source_nw_y_pixel': -9029915743084264486,
                                        'source_pixel_width': -291313050181907915,
                                        'source_pixel_height': -279441656161879019,
                                        'rotation': -7268656704155647663,
                                        'virtual_nw_x_pixel': 1098275750,
                                        'virtual_nw_y_pixel': -146347363,
                                        'virtual_width': 1103980198,
                                        'virtual_height': 599008370,
                                    },
                            {
                                        'source_monitor': -320838,
                                        'source_nw_x_pixel': -5383005232125378479,
                                        'source_nw_y_pixel': -1274970756537341215,
                                        'source_pixel_width': -6357776322451095067,
                                        'source_pixel_height': -5101684909897396429,
                                        'rotation': -114919093125269224,
                                        'virtual_nw_x_pixel': 26108750,
                                        'virtual_nw_y_pixel': 11189221,
                                        'virtual_width': 127260418,
                                        'virtual_height': 172198416,
                                    },
                            {
                                        'source_monitor': 2535812,
                                        'source_nw_x_pixel': -6706466751005747389,
                                        'source_nw_y_pixel': -4454729765948448334,
                                        'source_pixel_width': -6928337193385193107,
                                        'source_pixel_height': -784566715483956188,
                                        'rotation': -8493174300424076282,
                                        'virtual_nw_x_pixel': 177323751,
                                        'virtual_nw_y_pixel': 1174546373,
                                        'virtual_width': -209849302,
                                        'virtual_height': -1913221856,
                                    },
                            {
                                        'source_monitor': 3302078,
                                        'source_nw_x_pixel': -7719029449220398502,
                                        'source_nw_y_pixel': -9064779071136469886,
                                        'source_pixel_width': -8867765763966624420,
                                        'source_pixel_height': -2099896975459335712,
                                        'rotation': -7020767801532045037,
                                        'virtual_nw_x_pixel': -1181781601,
                                        'virtual_nw_y_pixel': 1545848573,
                                        'virtual_width': 391889589,
                                        'virtual_height': 1208484394,
                                    },
                        ],
                },
                {
                    'description': 'Ӥӟʴ~ԓΕˠ¬åšӴŒŗϺWÀŎϮјȮŻȼӧΎŊΈϼУ˪ĺ',
                    'monitors': [
                            {
                                        'identifier': 8628938,
                                        'width': 2473277331728511188,
                                        'height': -7404369290585669011,
                                    },
                            {
                                        'identifier': 8414295,
                                        'width': -8338608513814443530,
                                        'height': 3218571552233411558,
                                    },
                            {
                                        'identifier': 5999641,
                                        'width': -2943680075119588631,
                                        'height': 1301858359329773265,
                                    },
                            {
                                        'identifier': -235017,
                                        'width': 104285088123849088,
                                        'height': -7394751484047747138,
                                    },
                            {
                                        'identifier': 5098826,
                                        'width': 7282306596198891572,
                                        'height': 7246423198832410497,
                                    },
                            {
                                        'identifier': 8331528,
                                        'width': -3052797364970104427,
                                        'height': -6793732211952733858,
                                    },
                            {
                                        'identifier': 1664783,
                                        'width': 3513801670531399959,
                                        'height': -6943904903098573841,
                                    },
                            {
                                        'identifier': 6597175,
                                        'width': 7770648540506440199,
                                        'height': -7936543485201650842,
                                    },
                            {
                                        'identifier': 1771696,
                                        'width': 1236732805677277602,
                                        'height': -6953765625938163848,
                                    },
                            {
                                        'identifier': 4040086,
                                        'width': -3671680615115765304,
                                        'height': -7720882145412481898,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3257331,
                                        'source_nw_x_pixel': -2263763349646652713,
                                        'source_nw_y_pixel': -6630325517628975491,
                                        'source_pixel_width': -7435270023518253042,
                                        'source_pixel_height': -2771761796119646584,
                                        'rotation': -3604419631825700550,
                                        'virtual_nw_x_pixel': -147053946,
                                        'virtual_nw_y_pixel': -1059161146,
                                        'virtual_width': 1861189994,
                                        'virtual_height': 1059563927,
                                    },
                            {
                                        'source_monitor': 5218099,
                                        'source_nw_x_pixel': -2536220098118681369,
                                        'source_nw_y_pixel': -2122200078274949763,
                                        'source_pixel_width': -8767031604495051862,
                                        'source_pixel_height': -2133312249378180997,
                                        'rotation': -5113221554755444948,
                                        'virtual_nw_x_pixel': 75399915,
                                        'virtual_nw_y_pixel': -1309090965,
                                        'virtual_width': -764223779,
                                        'virtual_height': -810670967,
                                    },
                            {
                                        'source_monitor': 8315625,
                                        'source_nw_x_pixel': -3999850657588225261,
                                        'source_nw_y_pixel': -2482772241749819548,
                                        'source_pixel_width': -254507867761829255,
                                        'source_pixel_height': -5541204317978253563,
                                        'rotation': -7310709584555454496,
                                        'virtual_nw_x_pixel': 1848482287,
                                        'virtual_nw_y_pixel': -1481240362,
                                        'virtual_width': 345589647,
                                        'virtual_height': 382748056,
                                    },
                            {
                                        'source_monitor': 2018754,
                                        'source_nw_x_pixel': -3624971440935725378,
                                        'source_nw_y_pixel': -5365810698024816169,
                                        'source_pixel_width': -1487486514275785490,
                                        'source_pixel_height': -4499651752334469671,
                                        'rotation': -7022852167288788386,
                                        'virtual_nw_x_pixel': 1789475807,
                                        'virtual_nw_y_pixel': 1888888574,
                                        'virtual_width': 1701507921,
                                        'virtual_height': 691519427,
                                    },
                            {
                                        'source_monitor': 9973715,
                                        'source_nw_x_pixel': -5747832219221728489,
                                        'source_nw_y_pixel': -2751527963542462098,
                                        'source_pixel_width': -8015277516906903661,
                                        'source_pixel_height': -5527151448116549726,
                                        'rotation': -8865318402428161030,
                                        'virtual_nw_x_pixel': 1762975033,
                                        'virtual_nw_y_pixel': -796878837,
                                        'virtual_width': -1603135854,
                                        'virtual_height': -607533863,
                                    },
                            {
                                        'source_monitor': 4562522,
                                        'source_nw_x_pixel': -1531598722071885894,
                                        'source_nw_y_pixel': -7047535041567992153,
                                        'source_pixel_width': -4095273328638539448,
                                        'source_pixel_height': -4178573796216878567,
                                        'rotation': -7692293198407172181,
                                        'virtual_nw_x_pixel': 1351059072,
                                        'virtual_nw_y_pixel': 1769955094,
                                        'virtual_width': 379526704,
                                        'virtual_height': -1368607928,
                                    },
                            {
                                        'source_monitor': 6722871,
                                        'source_nw_x_pixel': -6614795390795323135,
                                        'source_nw_y_pixel': -4969898992613960532,
                                        'source_pixel_width': -8798450871975779920,
                                        'source_pixel_height': -3420460615312373514,
                                        'rotation': -2039771253448586475,
                                        'virtual_nw_x_pixel': 476540616,
                                        'virtual_nw_y_pixel': 820721901,
                                        'virtual_width': -1537235348,
                                        'virtual_height': -1657483724,
                                    },
                            {
                                        'source_monitor': 6042658,
                                        'source_nw_x_pixel': -7569392131845996675,
                                        'source_nw_y_pixel': -4207092450934259067,
                                        'source_pixel_width': -5544770844805343152,
                                        'source_pixel_height': -439030958024219647,
                                        'rotation': -2005768355277431018,
                                        'virtual_nw_x_pixel': -438124796,
                                        'virtual_nw_y_pixel': -840157014,
                                        'virtual_width': 1365911438,
                                        'virtual_height': 1410872532,
                                    },
                            {
                                        'source_monitor': -928537,
                                        'source_nw_x_pixel': -1505911617521420215,
                                        'source_nw_y_pixel': -4843052577662595938,
                                        'source_pixel_width': -6811433162976940886,
                                        'source_pixel_height': -7760677514924215764,
                                        'rotation': -4852016735754982780,
                                        'virtual_nw_x_pixel': -627561657,
                                        'virtual_nw_y_pixel': -1970838837,
                                        'virtual_width': -141447505,
                                        'virtual_height': 1384617204,
                                    },
                            {
                                        'source_monitor': 4853776,
                                        'source_nw_x_pixel': -6583912810988544980,
                                        'source_nw_y_pixel': -6724551902201083750,
                                        'source_pixel_width': -2800651010700623290,
                                        'source_pixel_height': -7263951540202576373,
                                        'rotation': -1107407396869808924,
                                        'virtual_nw_x_pixel': -1039911906,
                                        'virtual_nw_y_pixel': -1019525008,
                                        'virtual_width': 591928543,
                                        'virtual_height': 440675832,
                                    },
                        ],
                },
                {
                    'description': ')ԜÛʠΠʣӁȷAɺӏǧmҍϒƙΠϢʅҌʴɕˌ˅ҡìЌǩ˄ʼ',
                    'monitors': [
                            {
                                        'identifier': 4426508,
                                        'width': 7474673245624709633,
                                        'height': 3506200946880138103,
                                    },
                            {
                                        'identifier': 3353156,
                                        'width': 2123681693463759387,
                                        'height': 8936072719910460593,
                                    },
                            {
                                        'identifier': 2199816,
                                        'width': 773361744540208619,
                                        'height': 8403341899900539283,
                                    },
                            {
                                        'identifier': 3196837,
                                        'width': -2876748907696538573,
                                        'height': -7708677745419986861,
                                    },
                            {
                                        'identifier': 699107,
                                        'width': 7826458968573102269,
                                        'height': 6925016805522560508,
                                    },
                            {
                                        'identifier': 3729830,
                                        'width': 6716946508796341846,
                                        'height': -2863543525654084128,
                                    },
                            {
                                        'identifier': 9715491,
                                        'width': 9058554313159107517,
                                        'height': 5336851241904715566,
                                    },
                            {
                                        'identifier': 2548146,
                                        'width': 4917784954105018023,
                                        'height': -1174038919109579707,
                                    },
                            {
                                        'identifier': 1067310,
                                        'width': -8138253343514966773,
                                        'height': 2658659567294617451,
                                    },
                            {
                                        'identifier': 5828044,
                                        'width': 3646290784653869601,
                                        'height': 1650931378622815147,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 440091,
                                        'source_nw_x_pixel': -1957213816453006871,
                                        'source_nw_y_pixel': -6612318458283390377,
                                        'source_pixel_width': -4133540314472188309,
                                        'source_pixel_height': -2564950529472497062,
                                        'rotation': -715739219690696900,
                                        'virtual_nw_x_pixel': -340199377,
                                        'virtual_nw_y_pixel': 1996803161,
                                        'virtual_width': -408381255,
                                        'virtual_height': 1656327322,
                                    },
                            {
                                        'source_monitor': 499663,
                                        'source_nw_x_pixel': -3803649890605373518,
                                        'source_nw_y_pixel': -1606553461151094214,
                                        'source_pixel_width': -8729874890238378698,
                                        'source_pixel_height': -8079162113171746666,
                                        'rotation': -5439526507670662133,
                                        'virtual_nw_x_pixel': 1683067089,
                                        'virtual_nw_y_pixel': 982682853,
                                        'virtual_width': -1369563858,
                                        'virtual_height': -674109591,
                                    },
                            {
                                        'source_monitor': 3326315,
                                        'source_nw_x_pixel': -3368069753487343274,
                                        'source_nw_y_pixel': -3469912888126749789,
                                        'source_pixel_width': -3276398220423070303,
                                        'source_pixel_height': -859382188408610679,
                                        'rotation': -840321408041532009,
                                        'virtual_nw_x_pixel': 634778831,
                                        'virtual_nw_y_pixel': -554429908,
                                        'virtual_width': -781193405,
                                        'virtual_height': -1534468527,
                                    },
                            {
                                        'source_monitor': 6197907,
                                        'source_nw_x_pixel': -3317084632743149383,
                                        'source_nw_y_pixel': -8753949848575519928,
                                        'source_pixel_width': -4352070517417131284,
                                        'source_pixel_height': -3810604907227071346,
                                        'rotation': -3602292753610379479,
                                        'virtual_nw_x_pixel': 808351992,
                                        'virtual_nw_y_pixel': -309571215,
                                        'virtual_width': 539244060,
                                        'virtual_height': -701775453,
                                    },
                            {
                                        'source_monitor': 7383919,
                                        'source_nw_x_pixel': -708928703425414646,
                                        'source_nw_y_pixel': -5024431080211039278,
                                        'source_pixel_width': -4503476534759885258,
                                        'source_pixel_height': -394939240578168415,
                                        'rotation': -4751975603759920761,
                                        'virtual_nw_x_pixel': -1894456389,
                                        'virtual_nw_y_pixel': -1498490431,
                                        'virtual_width': -1302791113,
                                        'virtual_height': -110559659,
                                    },
                            {
                                        'source_monitor': 6595811,
                                        'source_nw_x_pixel': -50218318820820531,
                                        'source_nw_y_pixel': -6568387417644432714,
                                        'source_pixel_width': -5672427781683647940,
                                        'source_pixel_height': -4203514841771945680,
                                        'rotation': -3315061193848789221,
                                        'virtual_nw_x_pixel': -1836380463,
                                        'virtual_nw_y_pixel': -1495441723,
                                        'virtual_width': -1261222576,
                                        'virtual_height': -1788523672,
                                    },
                            {
                                        'source_monitor': 8897548,
                                        'source_nw_x_pixel': -1584850746801937190,
                                        'source_nw_y_pixel': -1420715121716730824,
                                        'source_pixel_width': -8563465789371382814,
                                        'source_pixel_height': -3673555204092249205,
                                        'rotation': -8491649772766081832,
                                        'virtual_nw_x_pixel': -632290652,
                                        'virtual_nw_y_pixel': 349537120,
                                        'virtual_width': 1355567559,
                                        'virtual_height': -40394834,
                                    },
                            {
                                        'source_monitor': 7824490,
                                        'source_nw_x_pixel': -2863446616611026074,
                                        'source_nw_y_pixel': -8840611918795615415,
                                        'source_pixel_width': -1802748180923395353,
                                        'source_pixel_height': -3429026648381064902,
                                        'rotation': -653312044925114544,
                                        'virtual_nw_x_pixel': -908925718,
                                        'virtual_nw_y_pixel': -1201163053,
                                        'virtual_width': 1008687868,
                                        'virtual_height': 423409761,
                                    },
                            {
                                        'source_monitor': 3847194,
                                        'source_nw_x_pixel': -6065371021607705726,
                                        'source_nw_y_pixel': -5220212086223148979,
                                        'source_pixel_width': -3685829973701218767,
                                        'source_pixel_height': -7914987597344036665,
                                        'rotation': -9138558593305952409,
                                        'virtual_nw_x_pixel': 143924126,
                                        'virtual_nw_y_pixel': 1477639502,
                                        'virtual_width': -229470210,
                                        'virtual_height': -679981922,
                                    },
                            {
                                        'source_monitor': 209232,
                                        'source_nw_x_pixel': -3980491011349389455,
                                        'source_nw_y_pixel': -3443073620554213763,
                                        'source_pixel_width': -2268099029060326301,
                                        'source_pixel_height': -7682596194530025890,
                                        'rotation': -5500266276039173983,
                                        'virtual_nw_x_pixel': 16897596,
                                        'virtual_nw_y_pixel': -549384171,
                                        'virtual_width': -781156951,
                                        'virtual_height': 1736299591,
                                    },
                        ],
                },
                {
                    'description': '\\ţҍJɅҫјӐʫ¡ƶѕƆ˯ҟHǋ5ǹЧϩVЍѴšĘȸȧӪЇ',
                    'monitors': [
                            {
                                        'identifier': 8762173,
                                        'width': -5387362748225912041,
                                        'height': 7366548269472484674,
                                    },
                            {
                                        'identifier': 4624872,
                                        'width': -7203052182821448105,
                                        'height': -2770436204908276952,
                                    },
                            {
                                        'identifier': 656368,
                                        'width': 2455891884827484761,
                                        'height': -2780683928965602696,
                                    },
                            {
                                        'identifier': -172981,
                                        'width': 4494669559525873105,
                                        'height': -1641268064358352890,
                                    },
                            {
                                        'identifier': 2010381,
                                        'width': 1499206085094246851,
                                        'height': -3904084608560576364,
                                    },
                            {
                                        'identifier': 6268076,
                                        'width': -4031861470967688943,
                                        'height': 6853069100384554874,
                                    },
                            {
                                        'identifier': 9612649,
                                        'width': -4510981083826830613,
                                        'height': -4309763688543240178,
                                    },
                            {
                                        'identifier': 7098275,
                                        'width': -4223937976097256498,
                                        'height': 4604632474038735124,
                                    },
                            {
                                        'identifier': 6855515,
                                        'width': 8137420039678801863,
                                        'height': -6344311382471820601,
                                    },
                            {
                                        'identifier': 4177647,
                                        'width': -2792693060684353204,
                                        'height': 6110204538519412534,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5510060,
                                        'source_nw_x_pixel': -8465831439720851767,
                                        'source_nw_y_pixel': -8697144050153417551,
                                        'source_pixel_width': -8774278912948019611,
                                        'source_pixel_height': -4884978027132498605,
                                        'rotation': -3716493139309766088,
                                        'virtual_nw_x_pixel': 529680029,
                                        'virtual_nw_y_pixel': -38249836,
                                        'virtual_width': 521368733,
                                        'virtual_height': 628271857,
                                    },
                            {
                                        'source_monitor': 2560496,
                                        'source_nw_x_pixel': -3583655365510016754,
                                        'source_nw_y_pixel': -3520424308884555122,
                                        'source_pixel_width': -5616280669519940819,
                                        'source_pixel_height': -3299781899764833498,
                                        'rotation': -3986072001726721761,
                                        'virtual_nw_x_pixel': 1853126344,
                                        'virtual_nw_y_pixel': -1808659376,
                                        'virtual_width': -689620373,
                                        'virtual_height': -885453921,
                                    },
                            {
                                        'source_monitor': 7279112,
                                        'source_nw_x_pixel': -5032242625521758486,
                                        'source_nw_y_pixel': -4344935006961611489,
                                        'source_pixel_width': -3612865969554642420,
                                        'source_pixel_height': -3731347399054393116,
                                        'rotation': -6318309102940889319,
                                        'virtual_nw_x_pixel': -1324951386,
                                        'virtual_nw_y_pixel': -502750948,
                                        'virtual_width': -1835139931,
                                        'virtual_height': -1379509656,
                                    },
                            {
                                        'source_monitor': 3404173,
                                        'source_nw_x_pixel': -2607107502466604945,
                                        'source_nw_y_pixel': -3223974186972281805,
                                        'source_pixel_width': -5442800062802956535,
                                        'source_pixel_height': -8420819976477206301,
                                        'rotation': -8784736507772759593,
                                        'virtual_nw_x_pixel': 800885534,
                                        'virtual_nw_y_pixel': -1668763322,
                                        'virtual_width': -1052759454,
                                        'virtual_height': -1424444848,
                                    },
                            {
                                        'source_monitor': 8202488,
                                        'source_nw_x_pixel': -1305611242559394257,
                                        'source_nw_y_pixel': -689424527298572930,
                                        'source_pixel_width': -2623439521731210300,
                                        'source_pixel_height': -6754898782199253637,
                                        'rotation': -1665096870826872997,
                                        'virtual_nw_x_pixel': -1192568693,
                                        'virtual_nw_y_pixel': -1425182018,
                                        'virtual_width': 40200828,
                                        'virtual_height': -417438537,
                                    },
                            {
                                        'source_monitor': 8368160,
                                        'source_nw_x_pixel': -9022426797026326466,
                                        'source_nw_y_pixel': -4227482901260290483,
                                        'source_pixel_width': -2702439979360558680,
                                        'source_pixel_height': -154152643650569398,
                                        'rotation': -8707801922836895479,
                                        'virtual_nw_x_pixel': -199612933,
                                        'virtual_nw_y_pixel': 1186256765,
                                        'virtual_width': 1040468416,
                                        'virtual_height': -376352288,
                                    },
                            {
                                        'source_monitor': -618975,
                                        'source_nw_x_pixel': -4663892976383118366,
                                        'source_nw_y_pixel': -8442780498332552324,
                                        'source_pixel_width': -203691205988133117,
                                        'source_pixel_height': -1054139313062619590,
                                        'rotation': -4600730357330665816,
                                        'virtual_nw_x_pixel': -688592798,
                                        'virtual_nw_y_pixel': 1026502992,
                                        'virtual_width': -1485272012,
                                        'virtual_height': 1847258045,
                                    },
                            {
                                        'source_monitor': 2810867,
                                        'source_nw_x_pixel': -8710394594737444993,
                                        'source_nw_y_pixel': -5688354186100781113,
                                        'source_pixel_width': -6638431231625178386,
                                        'source_pixel_height': -357176992397606216,
                                        'rotation': -6879058766464227390,
                                        'virtual_nw_x_pixel': -1073543679,
                                        'virtual_nw_y_pixel': 1044032612,
                                        'virtual_width': 843609958,
                                        'virtual_height': 446539037,
                                    },
                            {
                                        'source_monitor': 8083924,
                                        'source_nw_x_pixel': -3342988865808821526,
                                        'source_nw_y_pixel': -8560229081379556568,
                                        'source_pixel_width': -7387727116376565177,
                                        'source_pixel_height': -3793770992135243489,
                                        'rotation': -7635306191500812057,
                                        'virtual_nw_x_pixel': -94654357,
                                        'virtual_nw_y_pixel': -737762822,
                                        'virtual_width': -713456213,
                                        'virtual_height': -336096742,
                                    },
                            {
                                        'source_monitor': 5134906,
                                        'source_nw_x_pixel': -1330484906225126767,
                                        'source_nw_y_pixel': -5501935843267247138,
                                        'source_pixel_width': -4696101418699571444,
                                        'source_pixel_height': -6703586825975848037,
                                        'rotation': -5379458156464414437,
                                        'virtual_nw_x_pixel': 1654903591,
                                        'virtual_nw_y_pixel': -1659720208,
                                        'virtual_width': 973625169,
                                        'virtual_height': 1781212951,
                                    },
                        ],
                },
                {
                    'description': ' ÖϹÖÍŨɩӸJыæҊѣĭȍԣ;{ӎԥϣѺčRӔѾŞҨļɹ',
                    'monitors': [
                            {
                                        'identifier': 382269,
                                        'width': -4692837703705165090,
                                        'height': -238640327764891372,
                                    },
                            {
                                        'identifier': 8833411,
                                        'width': 4638570640440114584,
                                        'height': -8677078390841562373,
                                    },
                            {
                                        'identifier': -959687,
                                        'width': -2640787287365664835,
                                        'height': -6881820062924123385,
                                    },
                            {
                                        'identifier': 4810747,
                                        'width': 5122138582843702019,
                                        'height': -1603124466604937364,
                                    },
                            {
                                        'identifier': 5016550,
                                        'width': -5695425310865321051,
                                        'height': 599836948088157344,
                                    },
                            {
                                        'identifier': 4767073,
                                        'width': -2909639304660226520,
                                        'height': 7431786022349681580,
                                    },
                            {
                                        'identifier': 1310088,
                                        'width': -4597335881799491295,
                                        'height': -4514799499735797874,
                                    },
                            {
                                        'identifier': 9432007,
                                        'width': -4359743749978645547,
                                        'height': -784040988548208438,
                                    },
                            {
                                        'identifier': 4831229,
                                        'width': -542683706448773294,
                                        'height': 3839611607629088735,
                                    },
                            {
                                        'identifier': 9165037,
                                        'width': 1065639244067803882,
                                        'height': -3407197968571290778,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8543997,
                                        'source_nw_x_pixel': -8970722670077201586,
                                        'source_nw_y_pixel': -4661664100587136603,
                                        'source_pixel_width': -1302835738448425834,
                                        'source_pixel_height': -9210794280880838206,
                                        'rotation': -1754253009197362215,
                                        'virtual_nw_x_pixel': -753049398,
                                        'virtual_nw_y_pixel': 44891991,
                                        'virtual_width': -611522908,
                                        'virtual_height': -1977340601,
                                    },
                            {
                                        'source_monitor': 5126475,
                                        'source_nw_x_pixel': -2348338368621068609,
                                        'source_nw_y_pixel': -5214729247248728218,
                                        'source_pixel_width': -1126759150360049002,
                                        'source_pixel_height': -3642024079472229658,
                                        'rotation': -56815840646013307,
                                        'virtual_nw_x_pixel': 1296990960,
                                        'virtual_nw_y_pixel': -1213456914,
                                        'virtual_width': -1281294499,
                                        'virtual_height': -203368733,
                                    },
                            {
                                        'source_monitor': 4387187,
                                        'source_nw_x_pixel': -2315563303615872366,
                                        'source_nw_y_pixel': -66165917818014518,
                                        'source_pixel_width': -4184943551144235657,
                                        'source_pixel_height': -7733442959400619034,
                                        'rotation': -127332228302665286,
                                        'virtual_nw_x_pixel': 724963432,
                                        'virtual_nw_y_pixel': 27917121,
                                        'virtual_width': 155434729,
                                        'virtual_height': 1649450009,
                                    },
                            {
                                        'source_monitor': 9968224,
                                        'source_nw_x_pixel': -8424568423864377084,
                                        'source_nw_y_pixel': -1406002303612873174,
                                        'source_pixel_width': -6218143278061536667,
                                        'source_pixel_height': -5271639977867869459,
                                        'rotation': -2585676117219863248,
                                        'virtual_nw_x_pixel': -1844988435,
                                        'virtual_nw_y_pixel': 1054432087,
                                        'virtual_width': -361069790,
                                        'virtual_height': -1534105813,
                                    },
                            {
                                        'source_monitor': 449760,
                                        'source_nw_x_pixel': -8093111885198168788,
                                        'source_nw_y_pixel': -5692540987509890298,
                                        'source_pixel_width': -7934941168988200859,
                                        'source_pixel_height': -1516806617386443785,
                                        'rotation': -1766968028636686407,
                                        'virtual_nw_x_pixel': -173319556,
                                        'virtual_nw_y_pixel': 1758251371,
                                        'virtual_width': -1430327104,
                                        'virtual_height': 45385692,
                                    },
                            {
                                        'source_monitor': 1200791,
                                        'source_nw_x_pixel': -3200343029267232445,
                                        'source_nw_y_pixel': -174164719070530405,
                                        'source_pixel_width': -5055617613460543133,
                                        'source_pixel_height': -7538009445805371974,
                                        'rotation': -38748809950174174,
                                        'virtual_nw_x_pixel': 67650693,
                                        'virtual_nw_y_pixel': 823952501,
                                        'virtual_width': -861479816,
                                        'virtual_height': -1217611635,
                                    },
                            {
                                        'source_monitor': 9820323,
                                        'source_nw_x_pixel': -7140339636433572211,
                                        'source_nw_y_pixel': -9032151711511151537,
                                        'source_pixel_width': -8545932155998504500,
                                        'source_pixel_height': -6422334016382329200,
                                        'rotation': -2217904538642887915,
                                        'virtual_nw_x_pixel': 1718998620,
                                        'virtual_nw_y_pixel': -1466672727,
                                        'virtual_width': -1142397114,
                                        'virtual_height': -1638184623,
                                    },
                            {
                                        'source_monitor': 5624669,
                                        'source_nw_x_pixel': -7907425707538470832,
                                        'source_nw_y_pixel': -4013191800682555705,
                                        'source_pixel_width': -453179231139653694,
                                        'source_pixel_height': -8555328826292524236,
                                        'rotation': -8088626898024723308,
                                        'virtual_nw_x_pixel': -176932148,
                                        'virtual_nw_y_pixel': -1741556030,
                                        'virtual_width': -1408983902,
                                        'virtual_height': 1563492133,
                                    },
                            {
                                        'source_monitor': 3341640,
                                        'source_nw_x_pixel': -8154758887640833497,
                                        'source_nw_y_pixel': -2548963616098206021,
                                        'source_pixel_width': -1340613170568653441,
                                        'source_pixel_height': -6861259678976286849,
                                        'rotation': -8492776115265462052,
                                        'virtual_nw_x_pixel': 152780349,
                                        'virtual_nw_y_pixel': 561931561,
                                        'virtual_width': -131045142,
                                        'virtual_height': -157058922,
                                    },
                            {
                                        'source_monitor': 4646596,
                                        'source_nw_x_pixel': -3233832884266906085,
                                        'source_nw_y_pixel': -8289924285596532179,
                                        'source_pixel_width': -2978700780329578462,
                                        'source_pixel_height': -1907311780820357909,
                                        'rotation': -655937510758808982,
                                        'virtual_nw_x_pixel': -1009797528,
                                        'virtual_nw_y_pixel': 445874393,
                                        'virtual_width': 1897773887,
                                        'virtual_height': 1030309581,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 6164411,

            'mapped_screens_by_monitors': [
            ],

        },
    ),
]

class SetScreenConfigurationSuccessEventTest(unittest.TestCase):
    """
    Tests for SetScreenConfigurationSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_SCREEN_CONFIGURATION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.SetScreenConfigurationSuccessEvent.parse_data(test_data)
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
        for test_name, test_data in SET_SCREEN_CONFIGURATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.SetScreenConfigurationSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_SCREEN_CONFIGURATION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='request_id', name='SetScreenConfigurationSuccessEvent'),
            ),

        ),
    ),

]


SET_SCREEN_CONFIGURATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'request_id': 6934131,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 6800660,

        },
    ),
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
                res = screen.MessageArgumentValue.parse_data(test_data)
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
                res = screen.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ҭ×ƱˌAĉ¶ϦƝéƈʱKȥĸҳǚĿϮȅΒǜф\x86ΜϭӗòԖȚ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2905591173776149389,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -41880.79655238079,
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
            '$': '20210301:152850.454501:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ƈϫȵάΩ/ȎϟѬǎĮ¹ZьѣȚԇ\u0378κŕ¡Ѣ\x84\x9cƍƃ1ƶáϝ',
                'ώΕŷϟˣʫŒƈƥӊӖη\x8dļϚèȰfЏʢǗŨKьƱŊԈԚЙʍ',
                'ɉѻѳŦԡ˵Êʩ\u038bӃѓƽğ~ÀÃЌÇSŗԣЗϏƇɡЦВѶ˖ɚ',
                'ѧɗǈСЯϩОǗɷϰҝ˴Ǔ+ηȒϿƣɨǮύƚʯξҝĎìŎǞЇ',
                'ʰӸÀЁɺƄΐǈ¶ǵ¥ưύγ˙ŴÃȏԢˏɳԂϊĠƾÒɲNɫǻ',
                '¬dɎвѺϐǁ˄ĜҜС;ĘÅШȷŮϢ\x97ɬΙ£ЊˤўӒәˉƐ®',
                'Ν΅˖ʬҜȁΓЫƛ\x91ƕӣŴƂ҂˯ЖԐǨɂӱӤͼϚƓĵÀɡ˷Œ',
                'KƦϟŒªʤɾɌ3ҋ^ȍ˗ѲϥϝԂˠƝг_£ԎͺԐЉɴ¼Ύȓ',
                'ɡѢѸЎʏLŞƛϮӀДòŢ/ýƕĳԟыϔҘфѨҺ˜iʦŊϋÈ',
                "˄ȅԢĩõ˘ıȚʡ'Ўο\x91ԀΏс(\x91ΫǒМȔԙ˅УҘ\u0382\x94Эѭ",
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                8037299312009907535,
                -1095239681208474814,
                -3121401712322407448,
                5703090163440749384,
                9205038285606778154,
                -3820864284431357368,
                4226418688160140909,
                -7153527610566406469,
                223793640039648393,
                -3099469852068392513,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                381422.9042120276,
                64334.67848698559,
                899667.6536457574,
                -29938.713624200187,
                383722.5104167958,
                358784.2897122927,
                657199.6187899531,
                90194.48822053397,
                853142.0930483963,
                70311.84079304943,
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
                False,
                True,
                True,
                False,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210301:152850.455371:+0000',
                '20210301:152850.455385:+0000',
                '20210301:152850.455392:+0000',
                '20210301:152850.455399:+0000',
                '20210301:152850.455405:+0000',
                '20210301:152850.455412:+0000',
                '20210301:152850.455418:+0000',
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
                res = screen.MessageArgument.parse_data(test_data)
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
                res = screen.MessageArgument.parse_data(test_data)
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
            'name': 'ӿŴӻŋQіʰȊђΔ\x9aŇ¸)ДѱǬʹѓ҄ЊђФѳVˣВř',
            'value': {
                '^': 'float',
                '$': 266324.78310383717,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ˇ',

            'value': {
                '^': 'datetime_list',
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
                res = screen.LocalizableMessage.parse_data(test_data)
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
                res = screen.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ȶӉ¥Ͱӻ҉șѬл÷ķǒмųƭ\x9bŲƱ\x81}ϯӁźςĄĥΐʘdǂ',
            'message': 'ńʂͳǡŠЕѸėό˟ŴϷ\x8cґШѪƕˤǚ҈ʲΥƎhʥǣĒːфʑ',
            'arguments': [
                {
                    'name': 'ξξНеѥĪƄϋԬXė\x91zɃжôǨx˴Ķò',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -86803.28190926013,
                                        651356.7580642147,
                                        308398.09631625185,
                                        848693.4746419811,
                                        81242.64023611805,
                                        -24356.82761785017,
                                        301885.9222080491,
                                        53185.20624958663,
                                        237718.0503852482,
                                        -15532.293656374415,
                                    ],
                        },
                },
                {
                    'name': 'іĩŭ҃ʗеԕԣ\u0379ѼЫ˟Ȇ\x96ʮ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210301:152850.452119:+0000',
                        },
                },
                {
                    'name': 'ѦK|қҎѽҸҍ|¼ȊѦϏұǣ\x98Ҿǆʋӏ:ϰ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
                                        False,
                                        False,
                                        False,
                                        False,
                                        True,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ȴӶ4ʒȞϰ×ƅԡǕ ȇü˞˓ʒȖϮΨïΒ΅ŰǫƼȚ±ƒҧ·',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -8607101968219992893,
                                        -8192787820474288228,
                                        5333329934673100000,
                                        -2836497429160000883,
                                        3903921566174500895,
                                        -281355600405300078,
                                        1469571950364342002,
                                        2070436376004245469,
                                        3120424904096495979,
                                        -557941472008276543,
                                    ],
                        },
                },
                {
                    'name': "śřʔҩǐȍұҰaǤ»\u038bǘRůİΊc'əԑТɢЗӐ=ԅΞɜΦ",
                    'value': {
                            '^': 'datetime',
                            '$': '20210301:152850.452754:+0000',
                        },
                },
                {
                    'name': 'ɵȴҤőċįĔƚǑÜрȊђʍɒȹQʞɱɔЇ\x81ǦƀҚțͻÏЈȃ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210301:152850.452936:+0000',
                                        '20210301:152850.452952:+0000',
                                        '20210301:152850.452961:+0000',
                                        '20210301:152850.452969:+0000',
                                        '20210301:152850.452976:+0000',
                                        '20210301:152850.452983:+0000',
                                        '20210301:152850.452990:+0000',
                                        '20210301:152850.452997:+0000',
                                        '20210301:152850.453003:+0000',
                                        '20210301:152850.453010:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ſԝʿǞδґ^ê\u0381ӓȴʯǮ˅ҰůӣҬɓҗ\x95ҰςȨк\x80ʰ˂Ǩɘ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ЁϤТʑЅȷâķæΑȠХ˸ȔŹƱÅȿЁǿɖƟҖʄԟˋϼǽԊƇ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3551957262010226178,
                                        -2407034652257316448,
                                        2055903221216194538,
                                        2028661371938123285,
                                        -5223746039309737806,
                                        2713315997534227645,
                                        -4826562246550039703,
                                        -8816129009370912987,
                                        -344008566724212427,
                                        -715999202939096028,
                                    ],
                        },
                },
                {
                    'name': "'îԗ:ӎŒ\x89ÐƠŤÁŴ˷ƛŦçѕ\x94ȟȾŵɞ\x84ϻAǿʸɵbĴ",
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -23615.134884480314,
                                        257969.41095953673,
                                        113755.21940755422,
                                        245943.79955168744,
                                        849708.442363493,
                                        114822.24493789664,
                                        520135.7727556244,
                                        372483.5997836771,
                                        877377.5240100129,
                                        617646.1301548111,
                                    ],
                        },
                },
                {
                    'name': 'ҚҒѫϛʩ\u03a2ɘѩȝãȯ˽ԐØ¥ǀɼƶϗŻ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԇӭ',

            'message': 'Ӂ',

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
                res = screen.Error.parse_data(test_data)
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
                res = screen.Error.parse_data(test_data)
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
                dict(field_name='messages', name='Error'),
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
            'identifier': 'ŜҨԪΠûŷШƸɃŖǧʋˠêΆʾŊɌϚÞαуțʋϺѥʃӹЧЦ',
            'categories': [
                'configuration',
                'internal',
                'internal',
                'internal',
                'file',
                'configuration',
                'file',
                'configuration',
                'os',
                'os',
            ],
            'source': 'ĥҁÐɲɎŕƆĢƨ˲όŔ\x9eÔӪЋÒПʞϫȿĩϗȽʳǲȬɰƚӊ',
            'messages': [
                {
                    'catalog': 'ŹӏζĤγǩt\x91ΣƟOӛыӇàˎΒҲÒ.HȁІХǸªλƏ',
                    'message': 'ȜǥOѓӾɺͳФɽʓϽϔȔòȘǏҥ҃ƾȵʋʗβ҈cԗ,ƂҒ5',
                    'arguments': [
                            {
                                        'name': 'ǝόӄĦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˵ϼśйɸɀɦȗ˖GγZRРЯʢЃϯɹ;ԫӖ˦÷Ȋ·ԃѫ\x91¡',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3363042899636148673,
                                                    },
                                    },
                            {
                                        'name': 'кʽD\x93ЇìȊȜŶ϶ϐҼѐ»Ҵ§˱гɲѻɧ\x8cȃΞѕǁʲəɵ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2495557668320240078,
                                                                            -8029103825340318618,
                                                                            3681426776352082658,
                                                                            -657956918357288436,
                                                                            -3024995496354398614,
                                                                            5684739509220525369,
                                                                            -1450844517128389381,
                                                                            -7715112402016437868,
                                                                            -4254249237784131553,
                                                                            2251842200865960045,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʟщкηȏͶɇϷ8ήƂł«ĤǴǑ±\x88ͱŽ˫ŶȎȥҠ˄˴ςѓȼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '!Ѯњћϼ\x95Ȇ¦ǏӶǻӌΰ˜ϻӻѫ\x84Ӿɾ·ÌȃƊȝʢҍӴ\x9bċ',
                                                    },
                                    },
                            {
                                        'name': 'Ш¹ŋ¶@ΟÕЖ\x8eѣдȦǈјҔʆγʴҠϿȤѱÎƙŬȢƩʃͶŚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            498493.1404199776,
                                                                            505229.1003246058,
                                                                            301906.145269313,
                                                                            93077.04746549972,
                                                                            399001.9541441694,
                                                                            -69473.63995570001,
                                                                            998064.9192079913,
                                                                            730829.0429042596,
                                                                            544221.0411260073,
                                                                            588768.1673174785,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '>δȤĳɻĽ\x81Ɩάпǘǥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.421792:+0000',
                                                                            '20210301:152850.421807:+0000',
                                                                            '20210301:152850.421816:+0000',
                                                                            '20210301:152850.421824:+0000',
                                                                            '20210301:152850.421831:+0000',
                                                                            '20210301:152850.421838:+0000',
                                                                            '20210301:152850.421844:+0000',
                                                                            '20210301:152850.421851:+0000',
                                                                            '20210301:152850.421857:+0000',
                                                                            '20210301:152850.421864:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'mȫƐôΖѕ˺ƌє˃úϱÚԙĹԢңѠȰ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĭӿcνȳ!˙ɁǐċȂԖЍoǼƺĕ˘ŀʓΒӈßр',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϾýҾɷѦǼѯЊȚˊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӐϨ\u0380ćҽȳѱƔŉϭӑρѮΎԋҵǨź˓Ȟʔ¯ˆϑ5ΑɳΥ\u03a2ƪ',
                                                                            'Џ¬ǳφʦǷӏԉïѝԅȽ\x84ҏщȴȐɿпӶэˋҼːȦż˺θ϶£',
                                                                            'ºԚϙĤϗɷȃе҅£Đ¦˅ЅЧĳȹӮǘRӂɎĄѷgȂӎҧ˖ɂ',
                                                                            'ĩ·ҧԚԙҗєϘ\u0383ğĹάШɤĈԠГӾэĉѻƌӔɾԆʛĺÔРŁ',
                                                                            'ž\x8dşͿҵιǺˈҹйëóǰŅÀҺσԝӃ&ȀŵƤѱŋķєƦϧϖ',
                                                                            'Ԣ˄Å҂БsƝ˭ҝΌùɿ%Ůνť˺ЎÀʺȐаșÍùæӸĠ˜æ',
                                                                            'ѝϾŪȺƁʡɮЦљțɲŲǼ`ȞnŃ˦ӜӾƘ˫ƾĨƯĒϵĶǝŶ',
                                                                            'ҙΦȊ}ԜԉȇԥĉЮϞ˳ŚŨҺlϝʋН&ӦřΎЊσΊȜ\u03a2Íѣ',
                                                                            'ԩ\x8fé¿ϬҬ\x98ѠȰBƣʏюϨġ҄ʿԛԪ¿ɣƚŽǸԎ¸Ȕ˰Iӑ',
                                                                            '\x95ZˀԝԆ˼ӭƮĨ¬Үъ\x8b˵ΠӶҒϦƞѤϼʠˡĵ΅ԠɠҕɐӚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϒӭΣțÛ·ϱ\u0382BѨϫТԊ@τԫʕ˚ïĹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ςЊЌőƦуÇǯ*ΰğЖˉϰđʵȱԒЅПǿƷįεˊăˉȀѨõ',
                    'message': 'ˈ¼®нƺȄдϙȍĜ \u038dһʖѩпЯȸΌ˂Ndŝ"Ѕ˖_Ӧϸљ',
                    'arguments': [
                            {
                                        'name': '¶ăʦЮΣŌʙҫŃӲȬȜĩИģѨs_ԩӟǀ˸ɺĹǌŪǶǯǪƲ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3751887897011571040,
                                                    },
                                    },
                            {
                                        'name': 'äϽ˛ҷIҼmѧϪ˳϶ǊʍѰљѐѿͺȖȍҕӓυɅɋѠѝӆ<ǘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.424142:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƊӡԬƳӍǩ˦',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.424312:+0000',
                                                    },
                                    },
                            {
                                        'name': 'g΅ŤÖʥЫԟӮѨǆψȚͰҼʠËåȰʺͲXԑšȉµʑȐōʏǠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 868400.1919380793,
                                                    },
                                    },
                            {
                                        'name': 'ӑԫ˗ѤɈЁSҞɟԁҵӦΠ(!ƻʁQΜȹá÷ň\x90ҳǥЯɉүΙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8935766278982951508,
                                                    },
                                    },
                            {
                                        'name': 'ħѫ\x95ƔҲɓƙʨԭĞˋӔBʕ҇ё\x8c/ҭƠŸaа\u0381όўκɝϢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 413442.43432386976,
                                                    },
                                    },
                            {
                                        'name': 'НŶgơѐӍʑʪʕҡΝNį_ɱ˲ͶɋĄӬԕęɚʒίӹǝϾǊƈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5540186012107869865,
                                                                            -6952130224015097222,
                                                                            5644524530312190756,
                                                                            5251625148373982937,
                                                                            3712808479802457018,
                                                                            4482410402270479440,
                                                                            2896589649809997933,
                                                                            364267190086013193,
                                                                            -4016967140633435741,
                                                                            -3474278657874091114,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƊͲȜʜôŇãʦĵǚʞ\x9bЏĪґЄƁӮģ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӢUƯ4®υʒ¬IϏΕƆʤϼȬҙϷԛӓóцɝȷԓчԭȑʜNʐ',
                                                                            'ӫʩɗˮѪѪϵҽʴ-®ɑɬьś˲˩zҝďĂϽя΅χǂơLϺԡ',
                                                                            'ͳΝdуʺŖƫ΄Ԑϔ˞\x87qĮҨËŉȂзˏ2ЬԖҎѕ4ɰſåǠ',
                                                                            'uřȸ\x93ƃРѻζԌʨ~ɠ³vсӴЛɋ\u038dϷЖƄѶRīŰŔϯŸl',
                                                                            '$ˠϰГrɓƵаĝĲӴ\x9fԄϠlĪѬс\x9bóȅМëƺ˾ƅΊЉәŲ',
                                                                            'ϟҎҴ\x94ϕ×ƒů].ƚ±ĦʆūȀŵԠ\x84ȁȄſŋϤџǱʙVˣč',
                                                                            'ӡ³έѪШɫÇϵɽ\u038dˡƤÉǹȢ˺ӳвҨ^ќпϥєϵćҏѩюĐ',
                                                                            'ƯӲԠƤćҷCɒ˕ʹ\xadþ˂ғtrXCϖŬЇγeɓԢƸκɮˆǁ',
                                                                            '\x87˹щĴѶŪѼЬƎНԜе\x9dH҄ĘˑҩȌӕήɚŲԐĒ\x88aɰˊκ',
                                                                            '*ԉôҙ\x84ˊΟʼěҿĔİѧçͼҝ¤ϺѪ΄Ɵ˸"¶ӄʊЍŶΪВ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӼƊǵʋ˜͵ŋБÚѷΦԏɄȡΟɕђŜĴԕġşŽһǠȕƾĕͼӭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5546236588156616077,
                                                                            -5926724865359985437,
                                                                            -5908606813975093473,
                                                                            9174931663247784171,
                                                                            6926819362399719970,
                                                                            -3132488127293942356,
                                                                            -487162429929988332,
                                                                            -2144995928694937216,
                                                                            6296068679768313480,
                                                                            -2544847932544811151,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʇǳ×Ϝ\x8fԜʈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "Íҁӿ˓Ɏ҄іĴǣЏγϷ÷Γ˥ҲԛɯāȤŗҸͳɕÐΛġʆ'С",
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʇĺ]Θ\x9a\x81¦ҽ',
                    'message': 'ƭćζɚɧéˍBԣԌчӠϿĜϪ"Ȗ\x93ìʥӷɟƣʗȁφSҶ3Ȟ',
                    'arguments': [
                            {
                                        'name': 'όǠԩʃŲŽßǈϾϞsǹҲķ˘ȺŲņǅÅotd\x9a1BˍҐȇǉ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4734976208518992188,
                                                    },
                                    },
                            {
                                        'name': 'Qӹ˻ǏчŁҧˢě˽[аáAȷkÝғʺӜӁԀЍ\x8bӯgɇHҝβ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7863329874485782683,
                                                    },
                                    },
                            {
                                        'name': 'ѫӗεҧȖDɢ˒ȡã',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ηΛëъŌˌӖÉȘЦ;XĹʁŌԮŐˁέͺ\u0381ʙȭöɌҐƎȃ¶&',
                                                    },
                                    },
                            {
                                        'name': 'ҷKΕӋʳͱƧӏğϤȞˉ\u038bԆʠАɦʛЅǿŒҎӍɍʿГɚϾʮ[',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'яïҟĥ˶ԙáÆʹȩԊȟӞȞШѱӕˀΧ_ϏԛβΘϔ˱ǅƝîȣ',
                                                    },
                                    },
                            {
                                        'name': 'ӶƾҨˑðʖºŇ\u038bӲԋʍ\x95EҲŞѻ\u038b)дƘbӐϗƐ[лëºǅ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4386638032207413892,
                                                                            6528736932943916763,
                                                                            6790586416006374415,
                                                                            -565820553609032953,
                                                                            -9155397349603122818,
                                                                            -6335618052727687845,
                                                                            -3192495938970616629,
                                                                            5208869672543064522,
                                                                            -7747366617567758284,
                                                                            -5149403772023623568,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɩϜͳҽύёĒɳͷήȤғĦŰ˲',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7481139798253438274,
                                                    },
                                    },
                            {
                                        'name': 'ǡĬǆ˽ԐԦʘɔʈѣ7ϻѱɸцǺӦÛ%k˚é˫ĿÝEšɪ"G',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.427485:+0000',
                                                                            '20210301:152850.427513:+0000',
                                                                            '20210301:152850.427521:+0000',
                                                                            '20210301:152850.427528:+0000',
                                                                            '20210301:152850.427534:+0000',
                                                                            '20210301:152850.427540:+0000',
                                                                            '20210301:152850.427546:+0000',
                                                                            '20210301:152850.427552:+0000',
                                                                            '20210301:152850.427558:+0000',
                                                                            '20210301:152850.427564:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʵǴ\x9eʃâ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˟ĿũʁϘϦſÁȬ\x9eʟȕʼÛԬ˴ʡȬ¦ȎǃЛǌʑΆύŻѫʳΉ',
                                                    },
                                    },
                            {
                                        'name': 'Ğӟҵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 363351.8891408563,
                                                    },
                                    },
                            {
                                        'name': 'ψşϼ\u03a2źć',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 383876.14355307666,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'CȠӕİlɸёʰˊ>d~άӾҀѭƶϠҋзˈɆ±5\x8b~ҏÚǃɁ',
                    'message': 'ҴɶŋĞǏͰĈĤЫΰ\x9eЄzˈͱѼɠϰŕě4tŸʡКϜӝ҆ʝŷ',
                    'arguments': [
                            {
                                        'name': 'ȦӼĹѵ\x8dǮӭϐѫ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ИҍԞ"˰ǧʤǌТùƹƤƩϣрǖęáÔԚ˜]ԄʈάʁЅͺӷɻ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǫθіüωԍÞЙǒ)ϩ҉ԥԘѿѿvɁŎ˺˽Ѕ]ϕǧѿβǪүĥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            569123.5180562407,
                                                                            -4722.343610287731,
                                                                            775601.0785311055,
                                                                            753748.917199954,
                                                                            700953.3944821147,
                                                                            899307.1864239494,
                                                                            489037.32746400277,
                                                                            234695.89150271547,
                                                                            824579.9261873203,
                                                                            353009.7967944955,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʾВƑͷӕ˦\u0380ɜԬƻϞÄʘӪʱӵ\u0378æ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 550500.6722602921,
                                                    },
                                    },
                            {
                                        'name': 'ř\u03a2ѼļԪʯόŧЌȡȥλ\x93ΧϲïЎвƵÍ\u038b˅Ʌ\xa0ͻОƪíǟ˳',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            486854.0536040971,
                                                                            521165.4377627064,
                                                                            260893.51770546194,
                                                                            701494.7396409265,
                                                                            682890.4180357455,
                                                                            118720.38453010857,
                                                                            715070.6772200203,
                                                                            156858.74465476617,
                                                                            686404.0310527454,
                                                                            843464.213518697,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'љĨгǿŴʣȧʹͺ˛ȡωҰď˽кƎƯȝɏǭҹĻăұQƅ:ŐҎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʐMfϢҬȎ˃Ķ\x8aЂԡϴʿ˜ř"Ӈ\x84τʚå\x84һ·Ƃʥ\x8cӯέΚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            804014.4069926998,
                                                                            200346.991997541,
                                                                            147630.3635375902,
                                                                            44210.53814673837,
                                                                            765294.3435843119,
                                                                            119495.2368608405,
                                                                            24218.76083399837,
                                                                            99074.23523307106,
                                                                            -5086.770615849542,
                                                                            714539.6776349939,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ϿgÊˠÌ\u0380қɱЊʐ'ѰʰѼ˄ʗӋƢɏȬĚș\u0378ʹԛ˰ƉƟOΡ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.431411:+0000',
                                                    },
                                    },
                            {
                                        'name': 'λԥşɤȷÁԎͳȍϑľіĂ^RҊʂɘсςƅˉˬƀӥ1ïÕԛ]',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ũӷгӢcЦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '3ӥԎ˫ӗԘȿ¼Å˽ԅÐƚɛŐӥЊ;Ͳ˰ÔùӁƒIƳ˽΅¬Ā',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĐӑҁήƯѱřєЗřΫ¿ʩƸ]έůϛИѬѐǆԋҨͳҀԔɀǶ¡',
                    'message': 'ǉɓ÷Ħȭ˜ȍǌѐŇɨϱƉŗÇkLYӫώ¥ϣЀѐϚS,ÂҤʛ',
                    'arguments': [
                            {
                                        'name': 'ΓúΖɌҼͺџӡ-ŭ\u0381ϛÉɺʣѵ[ϞϸƂʹɏлɍԩψӜϤӞǢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӦnfԇИБ˕ɔˠρхԊǨAÐʯήζϵșЛ6ǂʪРąԝ\x94˾\xad',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЁŅҏєѳӌƦӨ\x85ŵ¬˶ȻήʌӥŶ\x80ľɸԨĤȊ9íŖƦ˻ȠϬ',
                                                                            'ѣP¹ȼĹτĪӦԗӖʤŽхƚɞĝɕĲһϟȾʱҭϠҫĮĥ͵ȵǵ',
                                                                            'ƭԗƼ\x9cʿPԓ\x88ŗĔԪ´ʋɶвԋkhҔȊιɘȷɹľӻȸʅŽ˳',
                                                                            '˱Ͻǘ˙Ķðɫζί҄ύɄΤǂϪ.ҡʘʖµ˘ËƴƗǐϳЕЍȖѷ',
                                                                            'ơφϪȕйȳƻ\x8cɗĶϴŦůǣ\u038dɍŋƉ\x9b˽ԭjƕǱƊȖƼӕ2œ',
                                                                            'ĭӳўǟ˙ʸʘϲģȳВӡĜÌǡм҃ϸǪǩǜŕҨƠ0ǩή҇kǫ',
                                                                            'ƙnŕ\x84ʪΣӁɸϘźɲ°ȷƢǆîԦļҎǪȆʬΠ\u0380ӇǦˉȣßξ',
                                                                            'ϋϮÆβ҅Ϫм¾˅\u0379ԩӞïđȹʗӢУȺ\u0381āŻćЃBʻǵġҜϋ',
                                                                            '˳ʐˎmŴɹҭ©JŠʗńԉ\\ƥǭź˃еӧғöƤɑг]ćǋΆǅ',
                                                                            'vԗ¨ʁƂ˒Ȝͼ#\x8aĳ˨Žr\x9eΊȘΔφºŌ¬ǖëӶƜʬыԉZ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǚǧ1R\x9eӠ6Ӽ}ӫèψӘɄӨςRǍřȓœ±ƠȇŸZѮŷȴί',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            728908.0217422659,
                                                                            790818.0681347251,
                                                                            947345.8062252171,
                                                                            243986.8852469012,
                                                                            923951.2558631407,
                                                                            912919.0440417171,
                                                                            105129.62793539939,
                                                                            456037.1937641434,
                                                                            781016.4830851224,
                                                                            -86410.85860653795,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĮʂsIǉƈ{ɹ\x85¤өӓȤўʆǚϵȪƗʯũȌ˄ԆԟW',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˂ƈ҉ǈСʨȵ»ӮTΣЂʅ9\u0382ФҁԪǇŮΆ\u03a2ΨɊΟκɩҞҬԙ',
                                                    },
                                    },
                            {
                                        'name': 'Ŝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'οнʓdˏ0ʾҒʡԌƪƣӺʟȕÂρƁƼπͻȈ˜ˊӄѸȆ*\x8eʲ',
                                                                            'ʸѣиɥŠ2Ԋ˲ӡHі΅ŗӼéāɔϻйŮUåώïϖǝІΨŦэ',
                                                                            'ϯÁ.ӋƘľɣ¢рʧƐԘ˛ҐԪĆԝĆӦǂȭĵÂӜЬNÎĺ4Ҙ',
                                                                            'ʣʷrtïǶ˽ƨтȺɳØͶIќ\x80\x90ȒҶ\u0381ĝȵΩԧǂğˊ´ϒȫ',
                                                                            'ÚϥҐϫԛtɸɜɵŹһȾ˥ˬϼ˥ԑȎRoó²ìПͱhǰŸLП',
                                                                            'ƻȎ0}ˣȩǔңԣ#˘ȗһÒȅһʑ˕ǥĽŽӦӟĶƮѓǾʌщѸ',
                                                                            'ǈʉyϥҾӬÎ҅ƯʇƶѮĠэʍ˧÷ʼɲLŧԊȷƄƔAѴνΒЦ',
                                                                            '\u0383ì÷ųϬĊʚ˾ӎƂFDԅħR=ϮľɇLѤ˗ϊ˄»ƼЖKȖȮ',
                                                                            'ƹ˶ƹѓ\u0380żǲɡԪоųƇҀə˰ƆԜˮέĶƭϽͲò˕ιľǩaЂ',
                                                                            '҈˫ȉ>ÍԉİɸђϋÊðӧоɻ˖ͱƃєΑӦҌΠěÒ҇ђʜķɩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˶ɨϱǩŌчĶԦʓĶӨά¼Ԑ˜ȪMˁʖˢħíp3ƣˊ\x8d>Ҁ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            278885.48769886163,
                                                                            453461.7938233138,
                                                                            724790.0522338802,
                                                                            311891.00413673103,
                                                                            192632.10005200893,
                                                                            631620.023172819,
                                                                            452167.4896867714,
                                                                            161260.54991301455,
                                                                            894380.4931796511,
                                                                            286496.4299304248,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ќǖşÉҴ˾˽ÏѦ\x7fұщӂǅҭƁȴGθЁ·Ǩӭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5592029407647089733,
                                                                            71186211469785152,
                                                                            -8049771917405533117,
                                                                            -5374662982445328375,
                                                                            761476068082004664,
                                                                            8421582963659176440,
                                                                            -2234197207346990727,
                                                                            -4326003618143021531,
                                                                            1498028728678332148,
                                                                            6798955235971301470,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ġԣҸơˢҒȳΗϘƘѮƖƟєʩ˵ʙЍЕǥҴǤ\x8cbϘͷԪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            448628.29557598906,
                                                                            173681.7945216869,
                                                                            846711.2377424332,
                                                                            101207.88207604954,
                                                                            551039.7953826858,
                                                                            404050.4834393714,
                                                                            678298.4636177538,
                                                                            345674.93344626075,
                                                                            653607.641724747,
                                                                            208803.61549382738,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ќӒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7070671006482988259,
                                                    },
                                    },
                            {
                                        'name': 'AǷϜˑӐΎϴǝ\xa0ɟŝ\x8eɘàѳƥѢ¦ѣɶҗμƿ\xa0ЗȗǠŠґȴ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            430056.2332392958,
                                                                            580463.3091562865,
                                                                            350620.89993530815,
                                                                            61383.40742036901,
                                                                            601613.292482538,
                                                                            421265.2546234123,
                                                                            483461.8667154709,
                                                                            743208.4393266446,
                                                                            460186.81619460473,
                                                                            90385.58480988664,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Vɍ΅%ǊѿċϰΩ#ɦ΄ŪѴȽEǊBƌ\x93ғҧÄϣҒμƏƎоȻ',
                    'message': '˘\x90ϱʄϏ@ċӄөÅȓʰ!ŊĵƏӦхʩkŃʛάʩã\x94ǌјУȧ',
                    'arguments': [
                            {
                                        'name': '˻ɑːѱøĆğȸ˕ɀϓλ\x89Ŏь6ʔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʃĆПӢĕ¡éȴѨ˽ЫΏʝЫµƘΓƷ\x97ϼʎͺԫ˰ȱ÷\u0378ŀ·ň',
                                                                            'ĘȣҲ§ȱǎvȟʫԔhзќèȢԑμ6ϩѧ-ÌԧńHŵń҇ѱў',
                                                                            'Ҳԕӗθ\x8e,яӦɩŐȟщ.Àɺϳ\x9dĀʰ˳ľ.ҲřҠƕëϢǤԣ',
                                                                            'ʲĔĘōǕăӮƇƃȐ΅ļƆǂӺɘ˷©ІВɳʣӄŤǏºkϚҍϯ',
                                                                            'ӓϤɈɩϯM:\x9fЎѳʉȬȾķðęʧ΄ŕʦӿοΦӴßώѡҮŽ҉',
                                                                            'Ƌ\u03a2ѽԜКԬˮʦ\x97ɨšŤҾǍж˦4Ћ\x9eƬνҬŭ҈ɜΑξԦЖы',
                                                                            'ҧmϫʳƒӮÍѰѫǘϋƄжϻΛƃ-ţ9˙ʋωǼǌ˫;dǬĜ˝',
                                                                            'ȫġëѺўMƂчуƧuԨɄќɲĽĠÂħѠɧˋú϶НƁÚϻ\x83в',
                                                                            'Øԏϝ˝ɼԦəˌŲʤѐӪҏʩϷƖňʏ\\һҷȥΪΔŉϛʽŢЄҀ',
                                                                            'ЏЬƜЁƫʵΐ\u0381ʞŋːǱ¬ɚϢȜ˷Ͼƣˌ:˲ȥʷ\x81ӱʊ{Ǜʬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЉԪӋȷ4ҏԠѡѳ¾Ζéί-ΌлӹǊ\u038bα{',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -67631.27216205793,
                                                    },
                                    },
                            {
                                        'name': 'ìԉаď',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.437944:+0000',
                                                                            '20210301:152850.437969:+0000',
                                                                            '20210301:152850.437978:+0000',
                                                                            '20210301:152850.437985:+0000',
                                                                            '20210301:152850.437991:+0000',
                                                                            '20210301:152850.437997:+0000',
                                                                            '20210301:152850.438002:+0000',
                                                                            '20210301:152850.438008:+0000',
                                                                            '20210301:152850.438014:+0000',
                                                                            '20210301:152850.438019:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0383ʃ§gʬɭҷ^',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.438230:+0000',
                                                                            '20210301:152850.438241:+0000',
                                                                            '20210301:152850.438248:+0000',
                                                                            '20210301:152850.438254:+0000',
                                                                            '20210301:152850.438260:+0000',
                                                                            '20210301:152850.438266:+0000',
                                                                            '20210301:152850.438272:+0000',
                                                                            '20210301:152850.438278:+0000',
                                                                            '20210301:152850.438283:+0000',
                                                                            '20210301:152850.438289:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȍѻʸȇì5ӊŎšľҪŝʁԦʋ¯ǨȃѢô',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˱ĥӦƯɭʷƽÉŝwǞҁӁҜŅҲRɇүñѡΈңΑǯüпϤΈҐ',
                                                                            'ӓÄÍzŭӭO´Ы,ԬľҦӷþϲ\x92ƾȩЍЕͺф˫яƺȲӊΌ˝',
                                                                            '"¥ңΞțҕŎɳˮǲƀĻԆϏϰʆПǈɻ²іҧ»ʕǕ#ĨҋƏϊ',
                                                                            'įбǼɛҳƨМªƀέήΌ`sЧĎ>ԭĿОғ]ӑìȾȦʋAwʓ',
                                                                            'ŤďҒ\x8bҠõΪɒʞɆŃƸӉҝˋљ϶ſѿǋɽϾjӕ÷ÎϼʌαÉ',
                                                                            'НϥμɲŪ˹Ӥ*łҔϚ½ԍʃôΣĴӰԥȓƸψѫӱвȾѭŗњӦ',
                                                                            'ʙĕ´ŵĝιMʦ·ϏUyĊŧƽ˨Μ=ҀԑźцŹϿѤƥҡȀɟҹ',
                                                                            'ƍѼЎџƖòϖˎμѵpӔÆʳʼїÌ\u0383ňѨˇӁһԇw˘Fčuǎ',
                                                                            'ǖǗŽ\x90Ѯ˪ԃìÍѭíȗӨѽFĉĭŤ\x7fʢȓΔϪʨԄȇϛдƳs',
                                                                            '\x7fcĻÜԮʠ*М˨ѽŽιԋɬҌӸŊʥˮ\x9bYӁȘę4ԏɤѿƈѪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȅŅķǰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1310424031778519947,
                                                                            -7594983420648136315,
                                                                            8031250287089507031,
                                                                            543787333163665959,
                                                                            5462145717278957242,
                                                                            4114832650119243431,
                                                                            4545140594343942704,
                                                                            -8546940740375547890,
                                                                            686932652679121687,
                                                                            8461723212619216154,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҡ˞Ϳ»ԈǨґνн;˰ͷUŤːÇpŴŖǍҏɈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǯð«ΊÕųԁ\x8aӃĦҲŹǌΰӉƲӚȔʖǛΐĖԗțQƐrșϣˏ',
                                                    },
                                    },
                            {
                                        'name': 'ҫ{øɖǴ<ϲӍΖΦƐMШäӁȣ*ϩҵÀɒϱҲτĕƶҬ4',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.439254:+0000',
                                                                            '20210301:152850.439267:+0000',
                                                                            '20210301:152850.439274:+0000',
                                                                            '20210301:152850.439280:+0000',
                                                                            '20210301:152850.439286:+0000',
                                                                            '20210301:152850.439292:+0000',
                                                                            '20210301:152850.439297:+0000',
                                                                            '20210301:152850.439303:+0000',
                                                                            '20210301:152850.439308:+0000',
                                                                            '20210301:152850.439314:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǕBȻǂǱŕƾȪ;Ȑ˅ǂǌƼЃóωɁŎʕƍůʽԞýǟоàĕέ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.440020:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԔπƩћӊAȋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.440183:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɾɄҚ˚ĊЂԤl˥˜¸-ˀãóǣѿǱʭԌͲʹhɑɦΈ¬Ҽȴɣ',
                    'message': 'ЍĉЫԉѰȔųƭΫŔѠńā{Ń!ф\x98É©:ğӘЯ3ʳƎёʮӈ',
                    'arguments': [
                            {
                                        'name': 'ӭϣǹӑƕҸӔƉǼԊҭĵhΚҍɕаΰìɒ˦[ńȦɰԧÌȆǉǪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.440642:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƟюҦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.440787:+0000',
                                                                            '20210301:152850.440799:+0000',
                                                                            '20210301:152850.440808:+0000',
                                                                            '20210301:152850.440814:+0000',
                                                                            '20210301:152850.440821:+0000',
                                                                            '20210301:152850.440827:+0000',
                                                                            '20210301:152850.440834:+0000',
                                                                            '20210301:152850.440840:+0000',
                                                                            '20210301:152850.440846:+0000',
                                                                            '20210301:152850.440852:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'vЍЭǈ&GԄǖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.441077:+0000',
                                                                            '20210301:152850.441088:+0000',
                                                                            '20210301:152850.441096:+0000',
                                                                            '20210301:152850.441102:+0000',
                                                                            '20210301:152850.441108:+0000',
                                                                            '20210301:152850.441114:+0000',
                                                                            '20210301:152850.441120:+0000',
                                                                            '20210301:152850.441126:+0000',
                                                                            '20210301:152850.441132:+0000',
                                                                            '20210301:152850.441138:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'еÒɟŬȝϪԌ2vE',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4574658286548892789,
                                                                            -6666559060942983634,
                                                                            3461252999056950064,
                                                                            2397152775713179614,
                                                                            8000173102555265311,
                                                                            -1363362463938982184,
                                                                            -5395276367376059066,
                                                                            -785182009847522294,
                                                                            -4324273833541311522,
                                                                            8060080465873862027,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȇә˃ʖŰœɒăʎɺ8ҤʳǤєǱӺɁϬ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˝åҖ\x89ЖЛеƙƖԒёºƲ´˝ϡАҏǻ˕ˤѨyʁƍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 526740.3438795934,
                                                    },
                                    },
                            {
                                        'name': 'ƎүˈƥԟӡΓǔˋʏӌȟѴʺҝѧӑҖΐτȱЍϭ¼ƨº˫ԃˡј',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'LѮƱċĵ\u03a2ʙϥϗзτќȑ¿ƵǒюҔįă\x82Ɏʾ¢ѧǚОʢöǱ',
                                                    },
                                    },
                            {
                                        'name': '\xa0ȢɬǪШƘъ\x8fHȺ˸įäϯţӏД˞Ķ\u0379Ħ¦Ɏoɧɘŭӂ˭ŉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6843481899980372353,
                                                                            8526804970325285235,
                                                                            -1713593672100029333,
                                                                            -2790146374098076511,
                                                                            -6819109114207515909,
                                                                            8964947643327928587,
                                                                            -2149916747339204319,
                                                                            -1690485314600154564,
                                                                            -9196402884388037831,
                                                                            3610792965267946708,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˎƴшɖǲҜRЎçȝ`w\u038dΆÿʅ¼ҢõҮuŉȳÎĩʤĈɸȘł',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'cιĘȒe\x8a\x82Ѯæƴɸ\x9c˳ǫ˭ɱʌϛc\x9c%ѣɵěЩűҾͽx΅',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ű©ŵϕbҘϣ\x7fɝŰðƛɔȊƗ¿\x87ͱԛJ\x89ҭϛ_ŤıԝɝӼƢ',
                    'message': 'ȹ\u03a2řҾˢȅԎɫϾҺҗ3<ƀϽ\x8eέ¤>űEҟ˓\xad\x8bҨšȖɬɍ',
                    'arguments': [
                            {
                                        'name': 'ӨʣϮфǴɆĽ4εě[É¥ɴd\x84ʱŵҲҀěƎƏȹγϜԩΒӽɛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϙǹƃ\x8dŒӈȱϪǸԃʞÚұιǶεȘĐbԒΙ\u0379ĉHҢъȑЫơʡ',
                                                                            'ϸЬί#\x87ƤȺԔęÚ¡°ȟŠŽȿ²ɎĎӶӖȲԗѨξ]ϹġϱɊ',
                                                                            'ʼФŊԑΗɅÏҔӵΈń÷ā}ӧɭԢҪр˃ɋ%ĔnҾ˘ԈŠòҩ',
                                                                            'ƾʙëɿ.ŋӟǝƬʥǱɔ(ȧŒ¢Ԥɷ\x82ʿʶoʢʞ˜Сӗ×Ŷ˰',
                                                                            'ҕaȠšͼԍҌѹԧǅŹӟӀɌũˎ΅ͳ\x80ԬҘêӶҋǌϏѶƓŎÓ',
                                                                            'Ǫ˳ԬȀbΔҔȁѤĳϳɰԆÜIʔxϳʫȦ=ÊÒϝѵөƊǑƩș',
                                                                            'Ϡъρ¡ŮʀȚÂ аԛџ5«/łŚМʢфǠ3ёÚЪΆơЕC҄',
                                                                            'WѾĠұΠΫăJ*Ҟŗ-đŧȐʉsȌćƇődƹěçЭϺԦͻɲ',
                                                                            'ͷАůʍŷ4ϖͻ$°ʫ¯\x8fŭҡβςʛĎɆņӊƙ˕ͼИrȧҡĘ',
                                                                            'ӭȿЌћǓʉΞwԁΙùȢ>ʖҊȃҸҎӎáԘƢĦ˥ǮΝîήŪĕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'í¤˱ѝϜпʇƗğɐæ<Ϯ{ʺɿʱԄfbʫɵξȃśn.\xa0ҽȀ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǻѱ²ҒqǸҴҝӛԧɘ~҅Ƙ\x87ϯҼǦɀęòÊӽūȘǅќАΓ¬',
                                                    },
                                    },
                            {
                                        'name': 'ǰʞҺɋçʪΏȲɓšIɥμĀȴӐĝћDҼΎϼʴˬΊàŁƹĢĶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8671236807317676605,
                                                    },
                                    },
                            {
                                        'name': 'ȇҀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƤЃģ^ϷԐε˝|ěȎӶλƂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɢѓʁƘɃЁɐӑ-ӡ ˟ϵĢ˔ĴΈÈ϶ĴςŶˁԧӛŮԟƐ˕ӹ',
                                                                            'ϊɱԉΗŐѣӒҺӮȓνȀҘɝЄмŻèʐιƜʍƞԚɺßɍѤƪӈ',
                                                                            'ӾǱƒɣɲΚӫѢϟ`ƚϧ\x95ƌȚ6;˒ӥұұȀ`yȇӧhΥŢɈ',
                                                                            'ɸȔƌҒvƚѳÐʀԘǙмʭӆŻŴӮ%а\x90ʯȯȾʼŲЛņĕίü',
                                                                            'ȚǂţƯΘЈŎӁœě˚ľʢӻԠЄ&Ѣǉʉ¹ɰ˻ȣļ»}ʙ˖Ͷ',
                                                                            'ѬōѾȟÙ\x8dĲϴΖũªԀȺАъѪʄª4ȶʡ˸ͽʹʳɑˊΌ΅W',
                                                                            'ɞǨŁľĐΝЩĮʚɄӅЃӼǺ˒ΞƁƟȑ\x84ѯϲʉȺȡǳԒNȉɈ',
                                                                            'С˗əбΟĲԉ;ɞ/)\x85οŭʉΘϐȘj˝ĲÀ҂ԋσɭ¥ˆƃҙ',
                                                                            'ŔŌīgӧxϮјȽɇĸƐҨΔ¯ΗāϤǓʍмͱíǉƶǪʧǚΧϫ',
                                                                            'џó|ԧɼѰԐұÚÌ\x83ǢʱСǡǁΓЀлDӰ\xa0ďŜģԑʽǺ)˞',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǆŃǣɑĹҼ)ȶУɒÙЋΕȶƽ5ЬƙΟҖϱӾțЀŌƪҁѧө!',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 787844.2160776559,
                                                    },
                                    },
                            {
                                        'name': 'qŞˣѽҍ˙ѽӽѡϐɰҩɹCάԐǉӻӍĵпѡËЪ˦ưbvʦӔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.444634:+0000',
                                                                            '20210301:152850.444653:+0000',
                                                                            '20210301:152850.444663:+0000',
                                                                            '20210301:152850.444671:+0000',
                                                                            '20210301:152850.444678:+0000',
                                                                            '20210301:152850.444685:+0000',
                                                                            '20210301:152850.444692:+0000',
                                                                            '20210301:152850.444698:+0000',
                                                                            '20210301:152850.444705:+0000',
                                                                            '20210301:152850.444711:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˰ЎŽ˓Ȥˊʇϑɏ3«љĤҡ˧ʰþ˺ǿžҙΞƕиV˫ϷǃȐԃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -679031513589292051,
                                                    },
                                    },
                            {
                                        'name': 'čˢѯ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            772046.4994817077,
                                                                            380585.532932049,
                                                                            973790.5935162276,
                                                                            65204.864669855044,
                                                                            979527.8561398208,
                                                                            -82666.7445980735,
                                                                            476906.65279079066,
                                                                            797900.1675175476,
                                                                            39282.296214667294,
                                                                            618196.5865993229,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŪϨĕĕϟȜεӫŴʆҢŏ˴ЏąӝύеƱȖΙлǑȻԬΥȺԧɮʐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 591645.263202238,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ęҪƺǶϱІ˄ÿÀӘԫƃ;\x9fĿWʑѝҕʘΜʀȕ˳āԜϭџϦҦ',
                    'message': 'dЊà\x98Щ\x9aĦǧyʇȓɴϺî˥тό\x92ĤсáƁӑǸʭӰϐȍҸź',
                    'arguments': [
                            {
                                        'name': 'ŔӄҀĩѰ\x96ǲ\x88˟é;ŷĻЗͳħƆʪЏÖ_Дǫ+ƭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ѣӥ\x94ѨщАҪʽɓŹǌŊkυ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȅЄœȔӅæͱ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѹЫŞƢҬҞŲɐÍΑќʂЬŤυǍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            643027.9763344324,
                                                                            -13822.020345098601,
                                                                            208142.3777456811,
                                                                            -24195.691263745583,
                                                                            290639.7067116486,
                                                                            -23429.646696607015,
                                                                            685938.3968846605,
                                                                            -70207.32774392192,
                                                                            824381.8121490314,
                                                                            227107.53546775325,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȼӈʟĞ˻ʥϓίӞBŎӍӢ˳ϛãC˃',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԮʙgʹԒř',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            305431.2603722022,
                                                                            101620.95547274468,
                                                                            262148.85784147034,
                                                                            9112.466586927403,
                                                                            260962.07410957944,
                                                                            189907.2065987693,
                                                                            961757.9392455241,
                                                                            468226.70547057886,
                                                                            553828.0003783172,
                                                                            181049.88527889212,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʣǅ@Ͽ8ɯӭΌȧ\x860ũԘϔȻϜSÃÖɳąǘˣ˧ΔәǟӒŞ]',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -96937.31920743993,
                                                    },
                                    },
                            {
                                        'name': 'ɒшÇͷυŦÖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\u038dнöğPĈЁˉҹȗӤѺÂğˬŦə˧ӎĠѼӅһӃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2076183778594958779,
                                                    },
                                    },
                            {
                                        'name': 'ΔȜƄƹ˶\u038b\u0383ŬҺɐɊǏŤ_ÉҽӮ҅ȇΕԄ3>ԦҌɛΛΔŏИ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7952285862639870032,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ͿɈţȈ\x8bɟĎ[ƭȌΪɅԉ_ˇыĞŰǀŇĢĔϵȔӢŜ,Юϯ˨',
                    'message': 'èѮєϝЖĠOԒɲƎŤԅŀǐЍ¦фϔsѲςэβїÖƙћҘąĶ',
                    'arguments': [
                            {
                                        'name': 'ł¿ɆŚɞɡ3ĩǗХÕˑʗʚϾŌʝ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҁ£йˣ˩ӉȟŉΡϢҫԛɋЉӪ=PΗʶ҆ɜӵƧӼԋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'юԋǑ5Ҋ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÅҫȐȂ=ʂżӝÍ\x90(ǌτ˟яѭΩɹĪΙґƺӅˣԘǺ\x90ǦƤѐ',
                                                                            'ɧˡɨˢɫT˃ļ\x8aĮœinŻŜӋԕʿʞƚ\x8aèǷÔηɘ?²ȁǰ',
                                                                            'ӮΈγҥĢeɤИ\x92ҽ΅ßǉҕ˽ɎǲɃ`3ǲ˛ŪэɌǱǥЄΔʔ',
                                                                            'ώǇЁǴҎŹԛ£ɷǈϫÚKJȳϋTͽFDvͺƷ\x90ÉưΕǅà£',
                                                                            'ŏψƤăeĂȏҿҰĠûϱɈʢŢ˹ʶ¼ϧωӧҧϻǉоʈIұϑí',
                                                                            'ƍ§ҞɳǻҒŤĚȦŁΗəˎ+ҌɑʗÉЧѵӹϊЁÿÏƽұρͿϏ',
                                                                            'ğȞļѻмéɋòǸЌLνƜϣϳк4ıѡǯːƻҮӏӋȍň\x97ǛϾ',
                                                                            '˴Ⱥ6ͷӤϋ1кяԂԧӔ\x91÷e±ͰӯĪːzе˫ĄʹĴȀ\u038bтВ',
                                                                            'ŻОΧʏƒЦǂ\x93©ΡʘˆȌγȥӅyƋȁŅҩӰƭHǘ˳ˣJξɖ',
                                                                            'дԊÄɰfǣϱʩ#7ˆʨϑɠΞİģLЮѧјЎȧ·ҍŬ\x9bѽȚϖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˧ÜТ˓ҶǁˇˀƿӮ\x8aɡOƋԠơ\x96ƙαˑāҚпĶӛ-ušŧλ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.448907:+0000',
                                                                            '20210301:152850.448923:+0000',
                                                                            '20210301:152850.448932:+0000',
                                                                            '20210301:152850.448940:+0000',
                                                                            '20210301:152850.448948:+0000',
                                                                            '20210301:152850.448955:+0000',
                                                                            '20210301:152850.448961:+0000',
                                                                            '20210301:152850.448968:+0000',
                                                                            '20210301:152850.448975:+0000',
                                                                            '20210301:152850.448981:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɩĹ΅ğ϶ИӞÿǠԉŤΰ7ͱҴԝ˰ĩ˼Ǵì{рңϸc¡Ԋ͵ˢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǷśįŶʋǭƹƐǓĎĿӝωԢӬƏӦЀͲҁ%ΚʐͶΧ!ʠĬ®ǅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǢϩɮʴџÑ˚Ƀ҆öǺɱҜƨɌͼҷY«dԜɝ\x83±ʉϑθҏƠʲ',
                                                    },
                                    },
                            {
                                        'name': 'ԃԆ\x9dïǕЁȌκзҳĜӮŌəΦǖͲŚųΟǘĸòpБȞΰӞϗҵ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĹŤƺ˜Ï`ϾžùË·ɖzҟ.ӁʈѬ˷ʅˢ®ɝӖϵΔɤƜөϗ',
                                                                            'u¹ÇǣaƓƝ˕ɥҞћūʘ˷ƅϬ˸ÌíĆϒӊnΝԀӾϒɺƵʳ',
                                                                            'ё»ӄ^ğĖȐ:ҪȝӛÃJXťδƛƦӆϢɉƨηЩϙ˼ΎθэÅ',
                                                                            'ņҕˁԔίҀ\x9cɿԏƅǨķʖņӵŀ:Jіȃҙβҙλ\x84ϑӧφѠ¡',
                                                                            'ʑƕҗȹͼҁǣ®Ŀ¡ȿNŹțДϸʦƟżȫɨʯ˯ĕɎȓԋɩӚΐ',
                                                                            'ōőħFșâӧyͶƔ°9¸ŉҖѨĺɞҲ7ɑϬώŚʻÉ˧ρŎР',
                                                                            'ĶʯɌҽɿǐɨ\x85Гϊưƿԝϑˮʝ\x8eʊϏǜИԏZũѼtРύœǌ',
                                                                            'ѻ÷ɴČҙюΑΧʘӎԤӁҌʘʦɑÊϿωp\x9eǿ·ȈԮé͵ЄΥ\u0379',
                                                                            'џã1ĘɉԂϣϠԄvŪ\u0383ԆѓǌРˮƪԖŶӤ}ʗ\x80ҌʴԧԀҝƣ',
                                                                            '¢Źɨýəǃ\u0379qƒȕdǰGʸ˽ҝýëГˢ`ҖӘ\x82ţˆΌº˅Ԁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԃ¬ƴ<àљђͻʋķôҍˋȢʴӥǺĄ˭ԡ˹ԍɗѼОЕǁԓˤ¿',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.450000:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ź\x98ȌñӮȘԂöÊ˱½ԈHάҋL×\x83Ɲ\x9fƲϧșҥЫЈĤŞ¯Щ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǳЎȁɻϒϻ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.450311:+0000',
                                                                            '20210301:152850.450330:+0000',
                                                                            '20210301:152850.450346:+0000',
                                                                            '20210301:152850.450360:+0000',
                                                                            '20210301:152850.450374:+0000',
                                                                            '20210301:152850.450389:+0000',
                                                                            '20210301:152850.450401:+0000',
                                                                            '20210301:152850.450408:+0000',
                                                                            '20210301:152850.450414:+0000',
                                                                            '20210301:152850.450420:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ԃŕȨ΄ҥ',

            'categories': [
                'os',
            ],

            'messages': [
                {
                    'catalog': 'ļǗ',
                    'message': 'д',
                },
            ],

        },
    ),
]

class SetScreenConfigurationFailureEventTest(unittest.TestCase):
    """
    Tests for SetScreenConfigurationFailureEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_SCREEN_CONFIGURATION_FAILURE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.SetScreenConfigurationFailureEvent.parse_data(test_data)
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
        for test_name, test_data in SET_SCREEN_CONFIGURATION_FAILURE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.SetScreenConfigurationFailureEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_SCREEN_CONFIGURATION_FAILURE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='request_id', name='SetScreenConfigurationFailureEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='SetScreenConfigurationFailureEvent'),
            ),

        ),
    ),

]


SET_SCREEN_CONFIGURATION_FAILURE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'request_id': 2410081,
            'error': {
                'identifier': 'êxΔԛϩӃԍș҆ʛȃŉČũɜЧԪӮӵЪΞӯʈœѣøТŐʻǴ',
                'categories': [
                    'invalid-user-action',
                    'configuration',
                    'file',
                    'internal',
                ],
                'source': 'ǛÑӟӒχ\u0382ǸĒÅ³ͶŚǩϬŮѓΊ˻;NҜƖЌӪʡʫµɭ\x95ͽ',
                'messages': [
                    {
                            'catalog': 'ңñқ>¤;ҵȈPƧȵ5ѡzĢļɟ2Ʈ\x87ϋвɃ˽ʌǍè\x86\x8dʏ',
                            'message': 'ҽȎϞǟȸԝϝ˷ųѠ²ѰĚƾ˘ҥκ˥Ƀ^˄ӑŢ\x95Ѫ\x99ϘԜɞӊ',
                            'arguments': [
                                        {
                                                        'name': 'КśƋõОђƪ¥ʥЂ·ΊҔȕƯz\x96ԑDÓÊ˳Έ»BǐԝYϨľ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 143905.90057491945,
                                                                        },
                                                    },
                                        {
                                                        'name': 'İӍҘćǌԙʆşȬψŽ_ąŏȒК',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɉ:ӽѭǄпRqͳʼßҐʑϾҤҙȶ˗[ёӝưž|ʹԐҁ˯Ҟӱ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 467021.22650045354,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϗ˷ͽϐBģʁy9ҢзҜӧʠʿƖƴƲʞͻԝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɃәĻƀΞ˝ʚӞiЋϑǜͶϡσӴъԪѡėЗǄѕȼʜӳȁϜӻ\x99',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2687324593914890060,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӚƂƭÞһŷťϴѨϕĂħԨҷȦƱ\x95ʊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8908829866494716495,
                                                                        },
                                                    },
                                        {
                                                        'name': 'CњňŻΌǩCҠΫԙXҤʹЫƿӊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϙ§ƌÑÀёļ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152850.403793:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '-ɂ"ȦĩԦƇÃAɒЖϪӣ_˸ΣʜkΙύϰ˛ǪѕɄ ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'çˈƮђϰ\x86ТӏӤ\x99ϨQˏѭЄɗʨģ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -842772778007561812,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ѐȯ-ԞǀˎшԏζǬ¿%ɮҩˣȪѤȜʌʌÑѾŰŧӭʧ˭Ͳΐԟ',
                            'message': 'ùƆˡМҿŚщΞӓ˙Ѵȩ4ɯēĹƿʯʘƲƬҚΪEɊĊɬƧǇŞ',
                            'arguments': [
                                        {
                                                        'name': 'ǸјӚƜū\x9c\u038d:ǈȕВğӜʥˆΩ>ĥ҃ºԎˍͽыēȸƭЋυѱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΆԣƞӜȇ´ĞɃb1Ӗǫƿзԫԓј9ΡăǤ1ĹґɢҲˑɅąȵ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϺʅӖӖʂϤˠǧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉĥŎħǴˀΗϯѕϝ˥˴φԄĦ7ƿ¦ǲΊˊǁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'İϼ\x7fĘ\x7fȬѸҚųǭ˄ΩƳӕɁʁӹγɇɐâӑžͱȅʕƳ˺ѐǏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈԟĤƝԘсĭ<Εүԛ˓ʗħăOʓϒͶ҈ėҰԅáɂĔȞ<ǏҲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԑΛdˈоӞʊçҬҤ˞еʧǂβԕɫνÇш^ěͶƱčʟǊͽҩχ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'PϟÍΧűŕėӌӌ6Ĵʾԗ\x89ʕǷ\x9dʑƠԈѢҹĹĕŴɘʚ҇ҕ<',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x7fǹƌʺҶȦѠϸ΄ѷ͵иѷεɞƬҔјɿĭЈ҈ɣ^ŚɇƷȡCȉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152850.406078:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҸбɲʔˣήӟөƍνˑђиҐҏӏƜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'JѓɩʧƊзьҤУźҁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6254710950892982536,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʽƟӟϗȏďѸƀȜѶԇӴƛ\u0378ԆȓɲӆԟʱӒÑЁêҍØδƌψȰ',
                            'message': 'ƞĲ\x8dȞɼƍǇƥЎǚʯĘԒͱҿɽŞˣȡЁȓ=0ҖϠƘ¢Ͱԥφ',
                            'arguments': [
                                        {
                                                        'name': 'ƅͰȐέ\x932ʤсќϳ\x97',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -1031.0467495638295,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏȬϳɒ©ġŞӷūÓƀϠӰ\x9a·ē\x99ɺг!ʚɣњʶΊȟѽнǨҵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'âѵáž\u038bǚɟ\x85Ĝ\u0380ΌӃϮNʎԍɡΫȘƗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԄÎʹVЅӆ˥ŲӠНԋ#ʓɷҟҤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3240005364170740459,
                                                                        },
                                                    },
                                        {
                                                        'name': 'řӣώ˟ħ˥ǹ\u0379nȊʱрʦyşͺ˙ӔȖҩūѝʳņơЪȻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 982828.4786319805,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺ˶ΡC\x82ɞÌłζȒ\u03a2ÀŮɰǄћӚ˞ԕǂŭǎȚjȈҜʰӉгʖ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԌɰǝϽ϶tͷљ˱ˁҔӦӏ\x98]ҐОЃȁ÷wҙ҉ʗάАǙҧҋ!',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒˠӓɹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ý',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭǵȂοϝ΄ØǄəРƹǛȜҟȈǊ4ğΎƔɓGћƐӿɣNʋӝ҄',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ğʬʨβ\x91ǥҩNŉÛˆɞƼыѼβ˕ɹӉԣĭŹÙΥ˟ҧԔɃɂϮ',
                            'message': 'Ǆ¦ɗ\\˅ЈͶ˺IǬͽʡŏӕәɄӞ\xa0ϔtϕ˭¶РϒǠӭσȬϣ',
                            'arguments': [
                                        {
                                                        'name': 'ɂΏϞë˨ЯӽȓŇ˜ɸ\u0382˛ψðЙэԃȂ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'гŠǖԨΡʪɶ˘ʏ\u0383\x91ɉ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 462469.35131047375,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʘżīȗƲϚҁƢ\u0383\x84ԛʹϐƮϙѱëđŵȟЇѢɀªзѬɈʜʡ9',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĕӛԀɕ\x85ʬӭȢÆȤАϬřѿέӵ˩ȼ\x8aҗʽϡΧɶhϐӓӜȘǌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύśƍȏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4082041689938402852,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʫӌǓшɆĄыˤϦŻӴЛЀƌ˻ʳìҡЈƩҾ$ЯЯƗНč¾\x83҉',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˦ǳѭТɝӃÔ`Ŷűɴʆǚ΄ǱÕñʃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152850.411335:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӍҠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʓʝőΠ\x94˄ťʩθǷǸÜǄόʍϱΠĜҴÁǎѮҝђʍфÃ:υҙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 5117.354143948614,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂԚСӔǭ˭ϻѮΤ¸τɄɸԐˁИȀҙ·ҫʕŗ\x87Ȯ{Ɇɞņį˺',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 34577.68956372095,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˁñťτЁΏ',
                            'message': 'ǭvЁìɍ¦ȁ\x88ɒ˼\u0380ͱѴԪƃæϿѴѯɵ¶ƜҫӻʄζʄȂ@˅',
                            'arguments': [
                                        {
                                                        'name': 'ɝ\x89ҡĕƫіǯԂӹѭϢ˜ɖȣ\x8eʛȬϢϪÎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȖǙҫÌʪȤʘҔŌĠȏƏřЗΆϰʛƅÜǄʼΫƗΖȸ˒ǠȲżҀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ş¯Ј҉ѱԮƑоӫ·ӉðȎтȼűбè',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĹɡԩʣϑÜǿəƥҖʝӂzӖĳ®',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '×ěў\x8eɳҔδ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ιɥѝ҄Nѐɕɟƣʋ¢ʺɇĉăϩ¢',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ИɈͿɌУƤêѹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƸФďϔdвϦӞüȡΓǠңßŊџÏŌļš˼vY#!ˍĎċÓˑ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȅφ&ʜĀαӋԚΦɿȪАÝƌʗϻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 393047.4798767214,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůš\x82ϕƬΧɅ·єɵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӯ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҹɿ\x98.ĮДԚҘ΄_',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΛQίԚңť\x9dΓλȽȐȾО˔ύɦԟřθʑɎǧÔŰ}ҵǝêV~',
                            'message': 'ԉҮЫ¼Š\x90ҩŮҡī\u0380«ȋL҃зÒҙǭЁn\x98ΣƐȡϰɖѽʉǜ',
                            'arguments': [
                                        {
                                                        'name': 'z˷§ƌƪƻͼΝϛȡЄмЋþġ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152850.414172:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʀ\x82ΰӗӊŵĀ҅Ͷȹ˅ҘԎϋĻ\x7fћuùĚʛԑºǧàӺʛ\x81ΥÄ',
                            'message': 'ƥÙʔħR\x9cǸвѨƁЀήӂǩέмcˇԈȪūԪ§ӏƞӄªƌӉÄ',
                            'arguments': [
                                        {
                                                        'name': 'ˊЮĂǦε\xadҢHӍĲƤŅδ˧wƩɘğтȍϋ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧѝĠǠҌϼǣϏΫŊKɥƋɸƼΡˉĎϮǤѕʭѸԩċɜ\u0380ҼìΛ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8370416235738300406,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ü\x9bϖҽǛŢÿӒĜz˼ǛǔȋǀѼñɕёƳǹґԈӦɷÔ҆Ѳȝʐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9eǗφӫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ř9íɮёȂɸϴʦǩĕæаӷͱɏȔ\x8cϥȿӥβ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻњŃĶӻэǝԢC϶ˢƋ©\x85ƈВЁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˼ͻČΰRʼDˍǇVϛµҧǏƽтŕȱÎԮ˽\x81\x9eıjȊǾҟoʒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4568016001784158269,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԛU\x8aƼӐфȞ˲ʬҹȖĖɊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 410563.5857164675,
                                                                        },
                                                    },
                                        {
                                                        'name': 'æč[ʾeƒԟ˔ӂŋĈÏɇΜϿҳl\x9dǮӕʎŻӧ\x9cƚ˟(˯ʴĲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3402697850820390494,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЕҕжĚ¡ĴϷλʀѝΦ|œ¹üȞǮ>ȎϏǛ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 160067.30007550077,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ВŴőʊѿɵ\u038bΏǉϫԚѫǤΆκ¥ɥźϢϴÍĸͻЙĒWʌˎĮ±',
                            'message': 'ϗŊɭӵɔȁǂˮO΄ìԦʟËҼšǒԘãkϋЈÉӬêǩźG;¡',
                            'arguments': [
                                        {
                                                        'name': 'ʑԪӮЯŰDǬǵ´ĩнƲĮʷÛ˾$\u0379Ȏ˖ɚ2ɪɻǺȉÒ˥¼ņ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5420257229825351693,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӅǒϹÐɎıǨƼόӲӂ«ɾɫġɦɧ\x89ßҝƙ˦Ӟ҇űâεúԬ˟',
                            'message': 'ÎĴɰМҤʱѱ˟ҋɻ˷eƏԉıġ\x84ɚëÖӐӻüϻźə҃ȌѤЉ',
                            'arguments': [
                                        {
                                                        'name': 'ӼăƼϦӴ\x8e˟ЫȞӄ\x95ëˍËˏƱϜ\x80\x91ѓ҄ʹƀi¿ҡ˧ӊԠ·',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 9525.38642354816,
                                                                        },
                                                    },
                                        {
                                                        'name': 'оʘƛǨЃ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 42257.91413854837,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ōӀ¹éӬ7ϱɒîƧѓɤє\x83ɀЮȢˁӕ|Ĵԑ\x89ŌҏǐɈǫ˘ɒ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺCͶϓ*ł~ʶr±ӻɢˍӈÙπҫɰāϖёКΠͽЦ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'кϦүʷÐҷԁƀ˫\x8bΟ¦ɿÀʺȨНЧßПĕƲƑԢ}è',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152850.416952:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '"ϭй\xadҤΝԃɀ;ķЌˎüәªԝΩэιţ\\',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152850.417083:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'üԛbň',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɪ\x96ƛȚѴΠĲІʰĵđ*ϸіОыԕ\x83ʮԊƤZǚɬьϊӽμң»',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '9',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1576285340087145846,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʾø҆ĢҖҕӑųпϯ\x90Lѻǘʼ3f¨řɨЉžŧϻIк',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӏѨÕȢȣѶǟƷӓĈˋɌΥŧ҄\\Ǣŷˋʗ˓ӮșǊǈυӝȜґԙ',
                            'message': 'Åѽяʙҟƿİԁàʖ\x8cǊѧʜÞCȪͳʣЕƿĬҺÉԈșØɷğͲ',
                            'arguments': [
                                        {
                                                        'name': 'ϕ\x90\x8bS÷ԡŗÝџσǲϣȠ˴ΚÆӄeÛϔƺĽνƢΈƀʣģͳɵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'җʾŶǫϗeTŊeÐƿȏҍΙʌɣϾ©Ȣԙϓϡ\x85ѦЦëӈýþȈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '#ԆΪ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҴӃwҫҺÞĽŇtϘҿè\x8fţő˖ԗƔӷ´p˒҆ʞˉˬѺÌμz',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņʡϷʾɕµȹʔιʎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'uɴЃϴμƢАϬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6905963211327715594,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟ\x81ϨЕ\u0380σǏѩѦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152850.418672:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸàåҁŋƈŢӣ\u038dȻ®ѳśȄѸϝEǝϩΘ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛÄ\x81ƣ˩ăŢMδѓҧ϶ҀфŪɨȶźЗÎϤĦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕҼăΫɾǏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȤӼǪХͷԝý˟ϙÔLbώƝāЕёċНΨøȺėɞƩ ſƝ\x80Ӭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 2360936,

            'error': {
                'identifier': 'ĽΩƘѤƷ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'čϏ',
                            'message': 'Ó',
                        },
                ],
            },

        },
    ),
]

class VirtualScreenBlockTest(unittest.TestCase):
    """
    Tests for VirtualScreenBlock
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in VIRTUAL_SCREEN_BLOCK_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.VirtualScreenBlock.parse_data(test_data)
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
        for test_name, test_data in VIRTUAL_SCREEN_BLOCK_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.VirtualScreenBlock.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


VIRTUAL_SCREEN_BLOCK_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='nw_x_pixel', name='VirtualScreenBlock'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='nw_y_pixel', name='VirtualScreenBlock'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='width', name='VirtualScreenBlock'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='height', name='VirtualScreenBlock'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='ratio_x', name='VirtualScreenBlock'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='ratio_y', name='VirtualScreenBlock'),
            ),

        ),
    ),

]


VIRTUAL_SCREEN_BLOCK_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'nw_x_pixel': 611187446,
            'nw_y_pixel': 1910136138,
            'width': -4817637115702655129,
            'height': -2961647276892692858,
            'ratio_x': 4562739602482306247,
            'ratio_y': 3175767588881150058,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 1552963296,

            'nw_y_pixel': 1154744975,

            'width': -4170735856011155750,

            'height': -3043292755128817958,

            'ratio_x': -5565383630159299862,

            'ratio_y': -5497834786343320799,

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
                    'nw_x_pixel': -178287956,
                    'nw_y_pixel': 638804204,
                    'width': -3865503593561310941,
                    'height': -5900804907628006612,
                    'ratio_x': -7359213772333259310,
                    'ratio_y': 2976392736852126220,
                },
                {
                    'nw_x_pixel': 687869135,
                    'nw_y_pixel': -1018748320,
                    'width': -3610581162704438661,
                    'height': -7096559164480827428,
                    'ratio_x': 2257711425861025091,
                    'ratio_y': -5107915602470939063,
                },
                {
                    'nw_x_pixel': 985345416,
                    'nw_y_pixel': -1662612044,
                    'width': -462014017083293349,
                    'height': -9048783584008275476,
                    'ratio_x': 473892211720673716,
                    'ratio_y': -7602708986826181531,
                },
                {
                    'nw_x_pixel': 19572773,
                    'nw_y_pixel': 886521407,
                    'width': -421237446144456831,
                    'height': -6118206868061210233,
                    'ratio_x': 8105855955594036480,
                    'ratio_y': 6971255858619368460,
                },
                {
                    'nw_x_pixel': 1443779345,
                    'nw_y_pixel': 280133957,
                    'width': -3956702962072022257,
                    'height': -5438668984746491143,
                    'ratio_x': 8606146129039379534,
                    'ratio_y': 3302306523205451153,
                },
                {
                    'nw_x_pixel': 664573317,
                    'nw_y_pixel': 1113313175,
                    'width': -2049403246972744310,
                    'height': -2206852275769456921,
                    'ratio_x': -5066267690573056766,
                    'ratio_y': 727171353442248016,
                },
                {
                    'nw_x_pixel': -1355546353,
                    'nw_y_pixel': 573779005,
                    'width': -6597886488617353278,
                    'height': -233089410353997930,
                    'ratio_x': -8823275381438280619,
                    'ratio_y': 3082621780120279111,
                },
                {
                    'nw_x_pixel': -837669019,
                    'nw_y_pixel': -398878522,
                    'width': -7335207966239544553,
                    'height': -2107175894225248362,
                    'ratio_x': -3269197473811872311,
                    'ratio_y': 7285136737785107334,
                },
                {
                    'nw_x_pixel': -111020467,
                    'nw_y_pixel': 547111769,
                    'width': -6307719803508191134,
                    'height': -4517665141651066501,
                    'ratio_x': 7407952681133102341,
                    'ratio_y': -1585386592487469346,
                },
                {
                    'nw_x_pixel': -1191792278,
                    'nw_y_pixel': -622608622,
                    'width': -5663931193756119348,
                    'height': -4050911171481526171,
                    'ratio_x': -598491351530486721,
                    'ratio_y': -6550945054253734325,
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

class ScreenSetupsStateTest(unittest.TestCase):
    """
    Tests for ScreenSetupsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SCREEN_SETUPS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.ScreenSetupsState.parse_data(test_data)
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
        for test_name, test_data in SCREEN_SETUPS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.ScreenSetupsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SCREEN_SETUPS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='mapped_screens_by_monitors', name='ScreenSetupsState'),
            ),

        ),
    ),

]


SCREEN_SETUPS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'mapped_screens_by_monitors': [
                {
                    'description': 'ʛʒϷőȢËɓċϔϬͺʊύʟгǚԥǱʫˇʪ҇ÔʩӈÕ\x8dĮԨʳ',
                    'monitors': [
                            {
                                        'identifier': 8888642,
                                        'width': -4853668314597830619,
                                        'height': -3387382918438457057,
                                    },
                            {
                                        'identifier': 4757258,
                                        'width': 5923552587554081647,
                                        'height': -5790309701609333805,
                                    },
                            {
                                        'identifier': 7493459,
                                        'width': 3792650867412975196,
                                        'height': 9044945545259269963,
                                    },
                            {
                                        'identifier': 6289965,
                                        'width': -4334875123805424566,
                                        'height': -1136360437136695874,
                                    },
                            {
                                        'identifier': 1068392,
                                        'width': -6188726774754366192,
                                        'height': 583536525581547939,
                                    },
                            {
                                        'identifier': 7384861,
                                        'width': -4453203744778926835,
                                        'height': -8163961144078679813,
                                    },
                            {
                                        'identifier': 17678,
                                        'width': -3622132019495469101,
                                        'height': 2966779408715906258,
                                    },
                            {
                                        'identifier': 6406345,
                                        'width': 9087574968783533165,
                                        'height': -3228933087043295421,
                                    },
                            {
                                        'identifier': 2050061,
                                        'width': 5139100424701606166,
                                        'height': 6922789302762140370,
                                    },
                            {
                                        'identifier': -215258,
                                        'width': 4422069013384243235,
                                        'height': -841564062264573407,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8601531,
                                        'source_nw_x_pixel': -8453930503619905340,
                                        'source_nw_y_pixel': -2605130242050035227,
                                        'source_pixel_width': -2147534667723767897,
                                        'source_pixel_height': -1208685102328884771,
                                        'rotation': -7933953583220716370,
                                        'virtual_nw_x_pixel': -1012671413,
                                        'virtual_nw_y_pixel': 1893848143,
                                        'virtual_width': 1622495550,
                                        'virtual_height': -1716606724,
                                    },
                            {
                                        'source_monitor': 5058749,
                                        'source_nw_x_pixel': -6285549384728896820,
                                        'source_nw_y_pixel': -1403889717605153000,
                                        'source_pixel_width': -8461249259131819783,
                                        'source_pixel_height': -6277632270421826273,
                                        'rotation': -8414575551614945013,
                                        'virtual_nw_x_pixel': 922192284,
                                        'virtual_nw_y_pixel': 813130603,
                                        'virtual_width': 940551423,
                                        'virtual_height': -1658064926,
                                    },
                            {
                                        'source_monitor': 2774881,
                                        'source_nw_x_pixel': -8536135694267773868,
                                        'source_nw_y_pixel': -8786245565137096173,
                                        'source_pixel_width': -8083742670968409510,
                                        'source_pixel_height': -271391402111507608,
                                        'rotation': -4648098783386534500,
                                        'virtual_nw_x_pixel': 1378936252,
                                        'virtual_nw_y_pixel': -165681528,
                                        'virtual_width': 616042026,
                                        'virtual_height': 348578955,
                                    },
                            {
                                        'source_monitor': 4899235,
                                        'source_nw_x_pixel': -6630450848969567074,
                                        'source_nw_y_pixel': -1052710380068223802,
                                        'source_pixel_width': -3193685893167450671,
                                        'source_pixel_height': -4607787423922993606,
                                        'rotation': -9100307850560790595,
                                        'virtual_nw_x_pixel': 470928653,
                                        'virtual_nw_y_pixel': -1060184819,
                                        'virtual_width': 619554789,
                                        'virtual_height': 116238598,
                                    },
                            {
                                        'source_monitor': 2029846,
                                        'source_nw_x_pixel': -7642860607069377211,
                                        'source_nw_y_pixel': -2260019842884620427,
                                        'source_pixel_width': -6634850870142160407,
                                        'source_pixel_height': -3451765482553312019,
                                        'rotation': -2309797268941690098,
                                        'virtual_nw_x_pixel': -1924915462,
                                        'virtual_nw_y_pixel': -277518598,
                                        'virtual_width': -190975633,
                                        'virtual_height': 42598114,
                                    },
                            {
                                        'source_monitor': 9889776,
                                        'source_nw_x_pixel': -6781824739026659091,
                                        'source_nw_y_pixel': -8539107215109874598,
                                        'source_pixel_width': -8551670017484694947,
                                        'source_pixel_height': -2645687807920678649,
                                        'rotation': -454949726969168843,
                                        'virtual_nw_x_pixel': 1659122020,
                                        'virtual_nw_y_pixel': -1898957035,
                                        'virtual_width': 1172415933,
                                        'virtual_height': 1336221687,
                                    },
                            {
                                        'source_monitor': 8720069,
                                        'source_nw_x_pixel': -7661044277873057692,
                                        'source_nw_y_pixel': -8218943537213864358,
                                        'source_pixel_width': -3133586182471157262,
                                        'source_pixel_height': -6200321091534052543,
                                        'rotation': -8253978085384351354,
                                        'virtual_nw_x_pixel': 548772516,
                                        'virtual_nw_y_pixel': -1223761394,
                                        'virtual_width': 16828250,
                                        'virtual_height': -1103989147,
                                    },
                            {
                                        'source_monitor': 7026105,
                                        'source_nw_x_pixel': -8984270456705720082,
                                        'source_nw_y_pixel': -3005907593318615155,
                                        'source_pixel_width': -4865208793456761132,
                                        'source_pixel_height': -6519623079482622529,
                                        'rotation': -8339981622063776778,
                                        'virtual_nw_x_pixel': 1200652928,
                                        'virtual_nw_y_pixel': 673766074,
                                        'virtual_width': 785401630,
                                        'virtual_height': -1899968115,
                                    },
                            {
                                        'source_monitor': 415989,
                                        'source_nw_x_pixel': -5304237336546765092,
                                        'source_nw_y_pixel': -5958700249458218629,
                                        'source_pixel_width': -8612502155584658931,
                                        'source_pixel_height': -7724914693277874074,
                                        'rotation': -1399503992348328434,
                                        'virtual_nw_x_pixel': 269693709,
                                        'virtual_nw_y_pixel': -260811648,
                                        'virtual_width': -850522273,
                                        'virtual_height': 141905487,
                                    },
                            {
                                        'source_monitor': 2290367,
                                        'source_nw_x_pixel': -830420849817038802,
                                        'source_nw_y_pixel': -6805971517437037975,
                                        'source_pixel_width': -4921752821121407690,
                                        'source_pixel_height': -109190283605443689,
                                        'rotation': -6165136404214827812,
                                        'virtual_nw_x_pixel': -795398337,
                                        'virtual_nw_y_pixel': -696239352,
                                        'virtual_width': -996763327,
                                        'virtual_height': -1706277933,
                                    },
                        ],
                },
                {
                    'description': 'ȦƥЉҌ˾¿û\x8bêӊʃіˑжЪǷɚЅЕϨԆτȦ\x80ʈʽħǿSv',
                    'monitors': [
                            {
                                        'identifier': 6101346,
                                        'width': -1674691305307970415,
                                        'height': 7683080541624766653,
                                    },
                            {
                                        'identifier': 9936827,
                                        'width': 2858814611293525398,
                                        'height': -5711455331013005766,
                                    },
                            {
                                        'identifier': 357011,
                                        'width': -1602767585673745733,
                                        'height': -4477714560399522568,
                                    },
                            {
                                        'identifier': 1876666,
                                        'width': -9134109821257296201,
                                        'height': -7584851346341091465,
                                    },
                            {
                                        'identifier': 4438696,
                                        'width': -5026545995693576823,
                                        'height': -3174857378103912925,
                                    },
                            {
                                        'identifier': 6239834,
                                        'width': -5201748192350324888,
                                        'height': -7260849875034124962,
                                    },
                            {
                                        'identifier': 5960728,
                                        'width': 3773827472987202144,
                                        'height': -8916698692985614306,
                                    },
                            {
                                        'identifier': 7272525,
                                        'width': -1877740699100203067,
                                        'height': -2580616718427777387,
                                    },
                            {
                                        'identifier': 1953749,
                                        'width': -1211677353977967405,
                                        'height': -4638138555569183873,
                                    },
                            {
                                        'identifier': 2143280,
                                        'width': 8697915893408054535,
                                        'height': 6557925192928509237,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4032375,
                                        'source_nw_x_pixel': -1931572986592068156,
                                        'source_nw_y_pixel': -1271169401835801476,
                                        'source_pixel_width': -9122853809663867361,
                                        'source_pixel_height': -8694735642702767119,
                                        'rotation': -3621390761587495415,
                                        'virtual_nw_x_pixel': -935722908,
                                        'virtual_nw_y_pixel': 34159235,
                                        'virtual_width': 1192537086,
                                        'virtual_height': 42458045,
                                    },
                            {
                                        'source_monitor': -216886,
                                        'source_nw_x_pixel': -6180314869124511769,
                                        'source_nw_y_pixel': -2713473200680673367,
                                        'source_pixel_width': -409238749085595555,
                                        'source_pixel_height': -3419965740125537900,
                                        'rotation': -3195971694635830253,
                                        'virtual_nw_x_pixel': 301831972,
                                        'virtual_nw_y_pixel': -661112949,
                                        'virtual_width': 1348639639,
                                        'virtual_height': 685332830,
                                    },
                            {
                                        'source_monitor': 9209697,
                                        'source_nw_x_pixel': -1567155844888307072,
                                        'source_nw_y_pixel': -8941658323048414526,
                                        'source_pixel_width': -6361887710485753815,
                                        'source_pixel_height': -7428850777994814449,
                                        'rotation': -6555209306293245821,
                                        'virtual_nw_x_pixel': 1052991504,
                                        'virtual_nw_y_pixel': -497443547,
                                        'virtual_width': 1896846387,
                                        'virtual_height': -1676818274,
                                    },
                            {
                                        'source_monitor': 917831,
                                        'source_nw_x_pixel': -4541424946543559280,
                                        'source_nw_y_pixel': -3153694493582033331,
                                        'source_pixel_width': -3173200287113000678,
                                        'source_pixel_height': -1427810326715163840,
                                        'rotation': -8028229600217531370,
                                        'virtual_nw_x_pixel': 1738817918,
                                        'virtual_nw_y_pixel': -872050242,
                                        'virtual_width': -1324950638,
                                        'virtual_height': 1296074121,
                                    },
                            {
                                        'source_monitor': 3470430,
                                        'source_nw_x_pixel': -5265106454803077665,
                                        'source_nw_y_pixel': -8718345847409112071,
                                        'source_pixel_width': -8622475110486878046,
                                        'source_pixel_height': -6831209339606932086,
                                        'rotation': -5442875003776717810,
                                        'virtual_nw_x_pixel': -710852203,
                                        'virtual_nw_y_pixel': 622615107,
                                        'virtual_width': 1905139920,
                                        'virtual_height': -1686825721,
                                    },
                            {
                                        'source_monitor': 7385830,
                                        'source_nw_x_pixel': -5742665301392372210,
                                        'source_nw_y_pixel': -3764944917346717391,
                                        'source_pixel_width': -8669040384750362754,
                                        'source_pixel_height': -8405308770188850982,
                                        'rotation': -2384720801845846337,
                                        'virtual_nw_x_pixel': 90256004,
                                        'virtual_nw_y_pixel': -366745431,
                                        'virtual_width': -1777516671,
                                        'virtual_height': -370514527,
                                    },
                            {
                                        'source_monitor': 7618078,
                                        'source_nw_x_pixel': -7211708536788367426,
                                        'source_nw_y_pixel': -4117136420987950654,
                                        'source_pixel_width': -9051179984573040409,
                                        'source_pixel_height': -1503706819288842895,
                                        'rotation': -648819349281572450,
                                        'virtual_nw_x_pixel': 601961430,
                                        'virtual_nw_y_pixel': -1455403861,
                                        'virtual_width': 688702463,
                                        'virtual_height': -591362219,
                                    },
                            {
                                        'source_monitor': 1423663,
                                        'source_nw_x_pixel': -2849833789516708928,
                                        'source_nw_y_pixel': -2110502511665970245,
                                        'source_pixel_width': -4042157365991421145,
                                        'source_pixel_height': -7704013730500444100,
                                        'rotation': -4580079275467831599,
                                        'virtual_nw_x_pixel': -1579266400,
                                        'virtual_nw_y_pixel': -966897897,
                                        'virtual_width': -1072200501,
                                        'virtual_height': -514925632,
                                    },
                            {
                                        'source_monitor': 2549212,
                                        'source_nw_x_pixel': -5129198902501813305,
                                        'source_nw_y_pixel': -2198273562887024205,
                                        'source_pixel_width': -4284983558395299663,
                                        'source_pixel_height': -3456495728471322040,
                                        'rotation': -5337147074078288318,
                                        'virtual_nw_x_pixel': 1727055879,
                                        'virtual_nw_y_pixel': 587977002,
                                        'virtual_width': -744880855,
                                        'virtual_height': -212027085,
                                    },
                            {
                                        'source_monitor': 1028743,
                                        'source_nw_x_pixel': -7617239962117275693,
                                        'source_nw_y_pixel': -4330535527936159023,
                                        'source_pixel_width': -6021282392988956655,
                                        'source_pixel_height': -5310909305278800568,
                                        'rotation': -2296077196878362262,
                                        'virtual_nw_x_pixel': 636362275,
                                        'virtual_nw_y_pixel': 788777961,
                                        'virtual_width': 89610955,
                                        'virtual_height': 262752222,
                                    },
                        ],
                },
                {
                    'description': 'ԑĦіĔЧүǮИɝϿЇњЦùƗИ˥ŬϞǵǏЊ\u0382ȋ¦җνҨ҄Ѿ',
                    'monitors': [
                            {
                                        'identifier': 240643,
                                        'width': -6562289035570648693,
                                        'height': -3263319583461651814,
                                    },
                            {
                                        'identifier': 2055348,
                                        'width': -7252345523457267197,
                                        'height': 1462604225666539143,
                                    },
                            {
                                        'identifier': -802573,
                                        'width': -4178574080353692661,
                                        'height': -7733833177510308661,
                                    },
                            {
                                        'identifier': -69904,
                                        'width': 3177124270321389784,
                                        'height': -4064097085441574940,
                                    },
                            {
                                        'identifier': 6024763,
                                        'width': 5598909576001020981,
                                        'height': -9168170464707374619,
                                    },
                            {
                                        'identifier': 9555146,
                                        'width': 1356229183921992291,
                                        'height': -9186030726741246776,
                                    },
                            {
                                        'identifier': 8765156,
                                        'width': -4539569124175473717,
                                        'height': -6720688630057311546,
                                    },
                            {
                                        'identifier': 6534764,
                                        'width': 4830257020896195427,
                                        'height': 5208715500868088416,
                                    },
                            {
                                        'identifier': 6075185,
                                        'width': 8333850612810820983,
                                        'height': 4780292020800138956,
                                    },
                            {
                                        'identifier': 743216,
                                        'width': -2618803338497796222,
                                        'height': 3949861204852815554,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1274850,
                                        'source_nw_x_pixel': -5834778675688350125,
                                        'source_nw_y_pixel': -2251404103671931554,
                                        'source_pixel_width': -2191512530144456610,
                                        'source_pixel_height': -2657885744464427579,
                                        'rotation': -7119513254050488450,
                                        'virtual_nw_x_pixel': -733089464,
                                        'virtual_nw_y_pixel': 1721088318,
                                        'virtual_width': 1648523869,
                                        'virtual_height': 488651180,
                                    },
                            {
                                        'source_monitor': 9682141,
                                        'source_nw_x_pixel': -637356732730785370,
                                        'source_nw_y_pixel': -4645130477582827947,
                                        'source_pixel_width': -7884096486048227,
                                        'source_pixel_height': -3271969933426073958,
                                        'rotation': -3484378934755252127,
                                        'virtual_nw_x_pixel': -361694551,
                                        'virtual_nw_y_pixel': 1870926080,
                                        'virtual_width': 101586245,
                                        'virtual_height': 1784505162,
                                    },
                            {
                                        'source_monitor': 240889,
                                        'source_nw_x_pixel': -2643630584110197853,
                                        'source_nw_y_pixel': -2254651746076066624,
                                        'source_pixel_width': -2311164993271811928,
                                        'source_pixel_height': -7419563629702937495,
                                        'rotation': -6400839222096716943,
                                        'virtual_nw_x_pixel': -514704867,
                                        'virtual_nw_y_pixel': 328317258,
                                        'virtual_width': 413620127,
                                        'virtual_height': -46651831,
                                    },
                            {
                                        'source_monitor': 2518374,
                                        'source_nw_x_pixel': -4294132215150768744,
                                        'source_nw_y_pixel': -5172261461555877011,
                                        'source_pixel_width': -8841600856279131699,
                                        'source_pixel_height': -257615507199905346,
                                        'rotation': -4998012186989222214,
                                        'virtual_nw_x_pixel': 252624471,
                                        'virtual_nw_y_pixel': 1014885015,
                                        'virtual_width': -558486902,
                                        'virtual_height': 1638756425,
                                    },
                            {
                                        'source_monitor': 6697252,
                                        'source_nw_x_pixel': -7465950236465731282,
                                        'source_nw_y_pixel': -1203356972525131825,
                                        'source_pixel_width': -7567380143307238676,
                                        'source_pixel_height': -829415397549903875,
                                        'rotation': -8775027221962319161,
                                        'virtual_nw_x_pixel': 869391563,
                                        'virtual_nw_y_pixel': 581644596,
                                        'virtual_width': -471997762,
                                        'virtual_height': 80004883,
                                    },
                            {
                                        'source_monitor': 2076628,
                                        'source_nw_x_pixel': -1365960184725207418,
                                        'source_nw_y_pixel': -4604306807164377661,
                                        'source_pixel_width': -6812521519882502196,
                                        'source_pixel_height': -5065790585997431875,
                                        'rotation': -218984526489889919,
                                        'virtual_nw_x_pixel': 620166269,
                                        'virtual_nw_y_pixel': -1484832297,
                                        'virtual_width': 105106729,
                                        'virtual_height': -411938216,
                                    },
                            {
                                        'source_monitor': 5199486,
                                        'source_nw_x_pixel': -7767965276814652137,
                                        'source_nw_y_pixel': -2198700932802835368,
                                        'source_pixel_width': -5927708398822421878,
                                        'source_pixel_height': -1591384998402285784,
                                        'rotation': -2551256392064151218,
                                        'virtual_nw_x_pixel': 655591900,
                                        'virtual_nw_y_pixel': -1024990959,
                                        'virtual_width': -1474515058,
                                        'virtual_height': -1020529430,
                                    },
                            {
                                        'source_monitor': 49321,
                                        'source_nw_x_pixel': -2546109130652239842,
                                        'source_nw_y_pixel': -2361909822733883481,
                                        'source_pixel_width': -259616867659195233,
                                        'source_pixel_height': -8039682626216909303,
                                        'rotation': -4510384207433116900,
                                        'virtual_nw_x_pixel': 1577541911,
                                        'virtual_nw_y_pixel': -1146153413,
                                        'virtual_width': 855782808,
                                        'virtual_height': -518908807,
                                    },
                            {
                                        'source_monitor': 9907888,
                                        'source_nw_x_pixel': -2593946533575709922,
                                        'source_nw_y_pixel': -5300639711179332630,
                                        'source_pixel_width': -2423338915016999166,
                                        'source_pixel_height': -7815730124671067370,
                                        'rotation': -6545192361614155488,
                                        'virtual_nw_x_pixel': -1935189558,
                                        'virtual_nw_y_pixel': -1913856019,
                                        'virtual_width': 432086393,
                                        'virtual_height': -1814118738,
                                    },
                            {
                                        'source_monitor': 8575284,
                                        'source_nw_x_pixel': -8715446881795422206,
                                        'source_nw_y_pixel': -8780349880109257474,
                                        'source_pixel_width': -6531247332864788993,
                                        'source_pixel_height': -5032399636482445447,
                                        'rotation': -5184376629918499726,
                                        'virtual_nw_x_pixel': 647102014,
                                        'virtual_nw_y_pixel': 485854473,
                                        'virtual_width': 649619698,
                                        'virtual_height': 578887190,
                                    },
                        ],
                },
                {
                    'description': '>ҵʙƤñɔƬġȿԕǢҙ˧5\x98ĤˡЪÀǺ6V+Π˰ΧԐ½ҫʡ',
                    'monitors': [
                            {
                                        'identifier': 9319138,
                                        'width': -5828616872857296067,
                                        'height': -6024931134895673647,
                                    },
                            {
                                        'identifier': 4058770,
                                        'width': -2254971026904702801,
                                        'height': 3281156200665438315,
                                    },
                            {
                                        'identifier': 5836036,
                                        'width': -6362062646534548185,
                                        'height': 8387387903788757139,
                                    },
                            {
                                        'identifier': 5895098,
                                        'width': 2909297576572212800,
                                        'height': 7621336592266880560,
                                    },
                            {
                                        'identifier': 1238133,
                                        'width': -7777214999764308829,
                                        'height': 4865869508114571093,
                                    },
                            {
                                        'identifier': -334394,
                                        'width': -1367992655714830315,
                                        'height': -7868514008976193300,
                                    },
                            {
                                        'identifier': 758250,
                                        'width': 5144780160135490053,
                                        'height': -9045261722011613647,
                                    },
                            {
                                        'identifier': 9358629,
                                        'width': 7319631549707038925,
                                        'height': 8094577828137998808,
                                    },
                            {
                                        'identifier': 3798610,
                                        'width': -2256637489642133717,
                                        'height': 1167531206631597944,
                                    },
                            {
                                        'identifier': 7303907,
                                        'width': 6798655224927250857,
                                        'height': -5841243586275310007,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9664710,
                                        'source_nw_x_pixel': -7692622914856439528,
                                        'source_nw_y_pixel': -5267592125555935046,
                                        'source_pixel_width': -7779009279286130098,
                                        'source_pixel_height': -7761769330010408986,
                                        'rotation': -8219438886739499671,
                                        'virtual_nw_x_pixel': -1650427900,
                                        'virtual_nw_y_pixel': 371216984,
                                        'virtual_width': -1588459637,
                                        'virtual_height': -794010848,
                                    },
                            {
                                        'source_monitor': 313011,
                                        'source_nw_x_pixel': -4264862590930155705,
                                        'source_nw_y_pixel': -5910586467306744648,
                                        'source_pixel_width': -8314446476757632904,
                                        'source_pixel_height': -1794198305021605032,
                                        'rotation': -6681892259614107586,
                                        'virtual_nw_x_pixel': -642805460,
                                        'virtual_nw_y_pixel': 1273393753,
                                        'virtual_width': 819054653,
                                        'virtual_height': 657307029,
                                    },
                            {
                                        'source_monitor': 7147125,
                                        'source_nw_x_pixel': -6076908547466417356,
                                        'source_nw_y_pixel': -5360476267898417077,
                                        'source_pixel_width': -261055173484953850,
                                        'source_pixel_height': -5759353976755004538,
                                        'rotation': -7743956956649038046,
                                        'virtual_nw_x_pixel': -1936712491,
                                        'virtual_nw_y_pixel': -1106154319,
                                        'virtual_width': 157067520,
                                        'virtual_height': -1329063973,
                                    },
                            {
                                        'source_monitor': 1751243,
                                        'source_nw_x_pixel': -3886105365067539586,
                                        'source_nw_y_pixel': -2430300915737707500,
                                        'source_pixel_width': -2039204718388685178,
                                        'source_pixel_height': -4119852551733598710,
                                        'rotation': -5310526890693792715,
                                        'virtual_nw_x_pixel': 1607957061,
                                        'virtual_nw_y_pixel': -1381981169,
                                        'virtual_width': 491603618,
                                        'virtual_height': -140389606,
                                    },
                            {
                                        'source_monitor': 927858,
                                        'source_nw_x_pixel': -2341004574244252388,
                                        'source_nw_y_pixel': -7797153336135734924,
                                        'source_pixel_width': -8607005872610156983,
                                        'source_pixel_height': -2547492517639338327,
                                        'rotation': -7548284667599618178,
                                        'virtual_nw_x_pixel': -655729875,
                                        'virtual_nw_y_pixel': -1735927622,
                                        'virtual_width': -1519558302,
                                        'virtual_height': -751057672,
                                    },
                            {
                                        'source_monitor': 1909516,
                                        'source_nw_x_pixel': -2101915107022005830,
                                        'source_nw_y_pixel': -4196781297550928172,
                                        'source_pixel_width': -8439871057738724369,
                                        'source_pixel_height': -3883712341717361974,
                                        'rotation': -4916898900232897026,
                                        'virtual_nw_x_pixel': -1440072919,
                                        'virtual_nw_y_pixel': -893676557,
                                        'virtual_width': -1637952531,
                                        'virtual_height': 755864618,
                                    },
                            {
                                        'source_monitor': 123032,
                                        'source_nw_x_pixel': -6970346836261879112,
                                        'source_nw_y_pixel': -7930415343204338782,
                                        'source_pixel_width': -1567876511971006378,
                                        'source_pixel_height': -3429780486392507345,
                                        'rotation': -4362318275389047522,
                                        'virtual_nw_x_pixel': -553071011,
                                        'virtual_nw_y_pixel': 511927851,
                                        'virtual_width': 1544806276,
                                        'virtual_height': 1469197390,
                                    },
                            {
                                        'source_monitor': 4352119,
                                        'source_nw_x_pixel': -8407676070424245688,
                                        'source_nw_y_pixel': -1588294255226009787,
                                        'source_pixel_width': -2084127029652111791,
                                        'source_pixel_height': -833717024037651381,
                                        'rotation': -7760047365917175361,
                                        'virtual_nw_x_pixel': -75969824,
                                        'virtual_nw_y_pixel': -787032208,
                                        'virtual_width': 1546771975,
                                        'virtual_height': -1165386377,
                                    },
                            {
                                        'source_monitor': 5825835,
                                        'source_nw_x_pixel': -9007236412237385511,
                                        'source_nw_y_pixel': -8896331742201309061,
                                        'source_pixel_width': -6561283498794877726,
                                        'source_pixel_height': -441688726752287678,
                                        'rotation': -6297377167424157021,
                                        'virtual_nw_x_pixel': -356726301,
                                        'virtual_nw_y_pixel': 1524682798,
                                        'virtual_width': -1849571435,
                                        'virtual_height': -1179758441,
                                    },
                            {
                                        'source_monitor': 7391896,
                                        'source_nw_x_pixel': -8560837179120670816,
                                        'source_nw_y_pixel': -6630386619325141744,
                                        'source_pixel_width': -1067959497093928712,
                                        'source_pixel_height': -2358046805558865922,
                                        'rotation': -6903788951329572985,
                                        'virtual_nw_x_pixel': 833342837,
                                        'virtual_nw_y_pixel': 999638985,
                                        'virtual_width': 1052933933,
                                        'virtual_height': 58746027,
                                    },
                        ],
                },
                {
                    'description': 'ʡɄ\x80ă\u0380þғǈһӬɷƠԩӞΏǎǾӇбϮЇɕѯуɴ¸ɊưǚƄ',
                    'monitors': [
                            {
                                        'identifier': 997492,
                                        'width': -3050962804735809693,
                                        'height': -4825101007480619719,
                                    },
                            {
                                        'identifier': 6642036,
                                        'width': -9072144626474501689,
                                        'height': -5574418747264042322,
                                    },
                            {
                                        'identifier': 8659860,
                                        'width': 3043080218847690656,
                                        'height': 216197847056653431,
                                    },
                            {
                                        'identifier': -323806,
                                        'width': -1113360626945555923,
                                        'height': -5335458513734465755,
                                    },
                            {
                                        'identifier': 5456546,
                                        'width': -982149423444492741,
                                        'height': 7103838602256535607,
                                    },
                            {
                                        'identifier': 2170377,
                                        'width': 350240363481488429,
                                        'height': -2748312818936468751,
                                    },
                            {
                                        'identifier': 8494375,
                                        'width': 7821801070735654916,
                                        'height': -9112528087056463765,
                                    },
                            {
                                        'identifier': -300902,
                                        'width': -5081852833338057218,
                                        'height': -7879652911806287774,
                                    },
                            {
                                        'identifier': 8158034,
                                        'width': -8293188233696964266,
                                        'height': 4845684088737647726,
                                    },
                            {
                                        'identifier': 4038602,
                                        'width': -3874436117835161128,
                                        'height': -5574396111011445589,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8240252,
                                        'source_nw_x_pixel': -1406039380436980308,
                                        'source_nw_y_pixel': -3907422402533828821,
                                        'source_pixel_width': -1216855911287768551,
                                        'source_pixel_height': -3364812977308302860,
                                        'rotation': -1452452404615834726,
                                        'virtual_nw_x_pixel': 217597242,
                                        'virtual_nw_y_pixel': -895827531,
                                        'virtual_width': 228717019,
                                        'virtual_height': -455213585,
                                    },
                            {
                                        'source_monitor': 5838885,
                                        'source_nw_x_pixel': -5558171403177660996,
                                        'source_nw_y_pixel': -8972610992853766008,
                                        'source_pixel_width': -5892474926632250127,
                                        'source_pixel_height': -2426389893559024083,
                                        'rotation': -2343216682983895910,
                                        'virtual_nw_x_pixel': -1199982622,
                                        'virtual_nw_y_pixel': -1211522572,
                                        'virtual_width': 1723561711,
                                        'virtual_height': 1002629788,
                                    },
                            {
                                        'source_monitor': 9233408,
                                        'source_nw_x_pixel': -6121112103434188799,
                                        'source_nw_y_pixel': -5747783584207150883,
                                        'source_pixel_width': -7979249428962780992,
                                        'source_pixel_height': -629762859729933396,
                                        'rotation': -5877452263782198186,
                                        'virtual_nw_x_pixel': 664498052,
                                        'virtual_nw_y_pixel': -1670490227,
                                        'virtual_width': -1266570926,
                                        'virtual_height': -1029756158,
                                    },
                            {
                                        'source_monitor': 5923562,
                                        'source_nw_x_pixel': -2857904447505059269,
                                        'source_nw_y_pixel': -1879458032817761882,
                                        'source_pixel_width': -3965707291218099581,
                                        'source_pixel_height': -6268908417204140933,
                                        'rotation': -3149876396597101992,
                                        'virtual_nw_x_pixel': 961998249,
                                        'virtual_nw_y_pixel': 327763535,
                                        'virtual_width': -40922062,
                                        'virtual_height': 1931388496,
                                    },
                            {
                                        'source_monitor': -487673,
                                        'source_nw_x_pixel': -7670398471318640442,
                                        'source_nw_y_pixel': -5019789693941758128,
                                        'source_pixel_width': -4340498948799557329,
                                        'source_pixel_height': -4726803245137794848,
                                        'rotation': -4860092712066816803,
                                        'virtual_nw_x_pixel': -326403965,
                                        'virtual_nw_y_pixel': -123539883,
                                        'virtual_width': -1906474345,
                                        'virtual_height': 415139628,
                                    },
                            {
                                        'source_monitor': 6728820,
                                        'source_nw_x_pixel': -2530573471512821057,
                                        'source_nw_y_pixel': -7734642705784933750,
                                        'source_pixel_width': -8573017069567749470,
                                        'source_pixel_height': -7057924337401268341,
                                        'rotation': -7038959091171014256,
                                        'virtual_nw_x_pixel': 1562805021,
                                        'virtual_nw_y_pixel': 1836570184,
                                        'virtual_width': -547529548,
                                        'virtual_height': -718471398,
                                    },
                            {
                                        'source_monitor': -975185,
                                        'source_nw_x_pixel': -6302407826170896339,
                                        'source_nw_y_pixel': -2891309092141508805,
                                        'source_pixel_width': -4818882497954010249,
                                        'source_pixel_height': -4047067514080711798,
                                        'rotation': -5586217113083987112,
                                        'virtual_nw_x_pixel': 468583588,
                                        'virtual_nw_y_pixel': -1815251548,
                                        'virtual_width': -799766060,
                                        'virtual_height': -1462611701,
                                    },
                            {
                                        'source_monitor': 5005281,
                                        'source_nw_x_pixel': -1122122283001928903,
                                        'source_nw_y_pixel': -5748223794553313406,
                                        'source_pixel_width': -3770006502895978568,
                                        'source_pixel_height': -2466196632986887795,
                                        'rotation': -7119507984896287432,
                                        'virtual_nw_x_pixel': -49925344,
                                        'virtual_nw_y_pixel': -1413249482,
                                        'virtual_width': -777307140,
                                        'virtual_height': 28188231,
                                    },
                            {
                                        'source_monitor': 5083761,
                                        'source_nw_x_pixel': -3691848610478785021,
                                        'source_nw_y_pixel': -6780083328122878112,
                                        'source_pixel_width': -6794678907354504833,
                                        'source_pixel_height': -7363613414146957023,
                                        'rotation': -747703064775501958,
                                        'virtual_nw_x_pixel': 1894102771,
                                        'virtual_nw_y_pixel': -1948848343,
                                        'virtual_width': -749757714,
                                        'virtual_height': 1637368924,
                                    },
                            {
                                        'source_monitor': 5378018,
                                        'source_nw_x_pixel': -2007642104956331434,
                                        'source_nw_y_pixel': -6364121729543195721,
                                        'source_pixel_width': -3829331642089519383,
                                        'source_pixel_height': -9107950133878080703,
                                        'rotation': -4193045741735435338,
                                        'virtual_nw_x_pixel': -1621646413,
                                        'virtual_nw_y_pixel': 1342386152,
                                        'virtual_width': 1182079496,
                                        'virtual_height': 304112244,
                                    },
                        ],
                },
                {
                    'description': 'ѹrˤɍɤˑѦʂàµːѷɃǸǇ5ʀƜțʔԇ%νҔοĈЊĲóǳ',
                    'monitors': [
                            {
                                        'identifier': 7598481,
                                        'width': 3539678199647847313,
                                        'height': -1335267982540186070,
                                    },
                            {
                                        'identifier': 7547750,
                                        'width': 8973284365291162217,
                                        'height': -9040693880674563092,
                                    },
                            {
                                        'identifier': -186173,
                                        'width': -4301915111420999562,
                                        'height': -6013821923026295660,
                                    },
                            {
                                        'identifier': 1079392,
                                        'width': 1757528774705774170,
                                        'height': 2416999966852418358,
                                    },
                            {
                                        'identifier': 3594078,
                                        'width': -1715314856037958037,
                                        'height': 1926521980703336648,
                                    },
                            {
                                        'identifier': 6290936,
                                        'width': -3495141091161348421,
                                        'height': 5138334615585183540,
                                    },
                            {
                                        'identifier': -713002,
                                        'width': -4770391998769067022,
                                        'height': 1213093677392850966,
                                    },
                            {
                                        'identifier': 8146984,
                                        'width': 7944285932797029855,
                                        'height': 698979011033268269,
                                    },
                            {
                                        'identifier': -106678,
                                        'width': 9010202317539161876,
                                        'height': -2520586065420391504,
                                    },
                            {
                                        'identifier': 9761900,
                                        'width': 5198868067773323616,
                                        'height': 4162546313313093870,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5172850,
                                        'source_nw_x_pixel': -4525566103369517403,
                                        'source_nw_y_pixel': -6221554733188399030,
                                        'source_pixel_width': -3847364107376723263,
                                        'source_pixel_height': -1444300936163153270,
                                        'rotation': -3292901771074116733,
                                        'virtual_nw_x_pixel': -509147630,
                                        'virtual_nw_y_pixel': 1366012147,
                                        'virtual_width': -1266076040,
                                        'virtual_height': 813643172,
                                    },
                            {
                                        'source_monitor': 9837957,
                                        'source_nw_x_pixel': -7326126604678272185,
                                        'source_nw_y_pixel': -2330129128201277783,
                                        'source_pixel_width': -9077316524806200797,
                                        'source_pixel_height': -1470723037799711786,
                                        'rotation': -3088360644172441671,
                                        'virtual_nw_x_pixel': 1129353366,
                                        'virtual_nw_y_pixel': -1014399042,
                                        'virtual_width': -1920131365,
                                        'virtual_height': 745333989,
                                    },
                            {
                                        'source_monitor': 5577001,
                                        'source_nw_x_pixel': -3360805111383173731,
                                        'source_nw_y_pixel': -7518228807363471779,
                                        'source_pixel_width': -4297351690286479606,
                                        'source_pixel_height': -8458123903925743313,
                                        'rotation': -5888148123892479093,
                                        'virtual_nw_x_pixel': -1345224937,
                                        'virtual_nw_y_pixel': -184269746,
                                        'virtual_width': 1894796454,
                                        'virtual_height': -589887526,
                                    },
                            {
                                        'source_monitor': 7067544,
                                        'source_nw_x_pixel': -3036690577661738093,
                                        'source_nw_y_pixel': -4286072661600778853,
                                        'source_pixel_width': -4187793648047670776,
                                        'source_pixel_height': -6081270187740144042,
                                        'rotation': -452909004966284536,
                                        'virtual_nw_x_pixel': 1998346884,
                                        'virtual_nw_y_pixel': -762786693,
                                        'virtual_width': -807298462,
                                        'virtual_height': 1447874627,
                                    },
                            {
                                        'source_monitor': 8853006,
                                        'source_nw_x_pixel': -8100689167894952693,
                                        'source_nw_y_pixel': -5892634288020585481,
                                        'source_pixel_width': -90881868825352562,
                                        'source_pixel_height': -6629718880620567129,
                                        'rotation': -3069843520300851335,
                                        'virtual_nw_x_pixel': 642385124,
                                        'virtual_nw_y_pixel': 480692930,
                                        'virtual_width': 1372322982,
                                        'virtual_height': -660185213,
                                    },
                            {
                                        'source_monitor': -922418,
                                        'source_nw_x_pixel': -895081384757640291,
                                        'source_nw_y_pixel': -8196241773023166882,
                                        'source_pixel_width': -7212500457331118139,
                                        'source_pixel_height': -1922290004626396930,
                                        'rotation': -700530179976928319,
                                        'virtual_nw_x_pixel': 343133525,
                                        'virtual_nw_y_pixel': 1173370383,
                                        'virtual_width': 1838562448,
                                        'virtual_height': -724399625,
                                    },
                            {
                                        'source_monitor': 6178374,
                                        'source_nw_x_pixel': -1763730515604408154,
                                        'source_nw_y_pixel': -5742593176729360781,
                                        'source_pixel_width': -7777932046134480589,
                                        'source_pixel_height': -1254998633810983198,
                                        'rotation': -9144428689294313945,
                                        'virtual_nw_x_pixel': -587615237,
                                        'virtual_nw_y_pixel': -584789311,
                                        'virtual_width': 367373843,
                                        'virtual_height': 123592145,
                                    },
                            {
                                        'source_monitor': 9364090,
                                        'source_nw_x_pixel': -4720399462915876650,
                                        'source_nw_y_pixel': -2015004464597233146,
                                        'source_pixel_width': -5422044982597189124,
                                        'source_pixel_height': -457205331288271488,
                                        'rotation': -3799281603634654969,
                                        'virtual_nw_x_pixel': 933138552,
                                        'virtual_nw_y_pixel': -1332753475,
                                        'virtual_width': 1436864251,
                                        'virtual_height': -818788615,
                                    },
                            {
                                        'source_monitor': 6143377,
                                        'source_nw_x_pixel': -5321892665122434970,
                                        'source_nw_y_pixel': -1622844213314957460,
                                        'source_pixel_width': -480472990938795997,
                                        'source_pixel_height': -1100753688308427038,
                                        'rotation': -3928331791217042204,
                                        'virtual_nw_x_pixel': -565793073,
                                        'virtual_nw_y_pixel': -1284301126,
                                        'virtual_width': 1395208309,
                                        'virtual_height': -1028430251,
                                    },
                            {
                                        'source_monitor': 7903663,
                                        'source_nw_x_pixel': -4107446610743848628,
                                        'source_nw_y_pixel': -9107168683500169054,
                                        'source_pixel_width': -2897629269349816915,
                                        'source_pixel_height': -6147965167936859410,
                                        'rotation': -2290457974663293680,
                                        'virtual_nw_x_pixel': 929297022,
                                        'virtual_nw_y_pixel': 1969894889,
                                        'virtual_width': -797801472,
                                        'virtual_height': -1475469852,
                                    },
                        ],
                },
                {
                    'description': 'WΩãO/\x8e\x89ęÂϡϑδƈӮʔǮϏзΖҏ´Юė҆ӏ;ǥӂԍǈ',
                    'monitors': [
                            {
                                        'identifier': 5865185,
                                        'width': 433451676599002894,
                                        'height': 7844059638091854229,
                                    },
                            {
                                        'identifier': 2295947,
                                        'width': -2604501135852035421,
                                        'height': -2399508229672247348,
                                    },
                            {
                                        'identifier': 1875263,
                                        'width': -4078959788019686481,
                                        'height': -6557453231075812069,
                                    },
                            {
                                        'identifier': 9607784,
                                        'width': 5432994337472888652,
                                        'height': -4256153811514261339,
                                    },
                            {
                                        'identifier': 5918896,
                                        'width': -3809224068155820504,
                                        'height': 6082465144377442077,
                                    },
                            {
                                        'identifier': -192328,
                                        'width': -8521224286754904144,
                                        'height': 8994671865851443741,
                                    },
                            {
                                        'identifier': 7489124,
                                        'width': 8624415213599113572,
                                        'height': -26576314832243858,
                                    },
                            {
                                        'identifier': 8046421,
                                        'width': 1210483141092410635,
                                        'height': 895751635243768543,
                                    },
                            {
                                        'identifier': 2564132,
                                        'width': -4155674590239799403,
                                        'height': -6484753838420246733,
                                    },
                            {
                                        'identifier': 8273851,
                                        'width': 2142142162530962978,
                                        'height': 9171710397395278644,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1669416,
                                        'source_nw_x_pixel': -181571374277225203,
                                        'source_nw_y_pixel': -7826301379549816209,
                                        'source_pixel_width': -3283866482791662262,
                                        'source_pixel_height': -4326697189734690165,
                                        'rotation': -180946026407283871,
                                        'virtual_nw_x_pixel': -1175758578,
                                        'virtual_nw_y_pixel': -1925624068,
                                        'virtual_width': -311810398,
                                        'virtual_height': 802548708,
                                    },
                            {
                                        'source_monitor': 5538456,
                                        'source_nw_x_pixel': -437134339381439685,
                                        'source_nw_y_pixel': -4095344792541805644,
                                        'source_pixel_width': -422699834797458719,
                                        'source_pixel_height': -6600516278083151523,
                                        'rotation': -4800183628699450731,
                                        'virtual_nw_x_pixel': 44199928,
                                        'virtual_nw_y_pixel': 766550685,
                                        'virtual_width': 40380617,
                                        'virtual_height': 1126166181,
                                    },
                            {
                                        'source_monitor': 8886826,
                                        'source_nw_x_pixel': -3623940292223500099,
                                        'source_nw_y_pixel': -7036948877017090857,
                                        'source_pixel_width': -2078235335961682017,
                                        'source_pixel_height': -7172697610938550125,
                                        'rotation': -4334265120919587264,
                                        'virtual_nw_x_pixel': -1664232261,
                                        'virtual_nw_y_pixel': -647625750,
                                        'virtual_width': -480293991,
                                        'virtual_height': 1809870291,
                                    },
                            {
                                        'source_monitor': 4924212,
                                        'source_nw_x_pixel': -279549668382513850,
                                        'source_nw_y_pixel': -7480927134644494595,
                                        'source_pixel_width': -3586676403030231835,
                                        'source_pixel_height': -2140179475391626362,
                                        'rotation': -1054802930420008507,
                                        'virtual_nw_x_pixel': 185409600,
                                        'virtual_nw_y_pixel': 879933548,
                                        'virtual_width': 1418884031,
                                        'virtual_height': -1644588981,
                                    },
                            {
                                        'source_monitor': 8373680,
                                        'source_nw_x_pixel': -5058451617955809069,
                                        'source_nw_y_pixel': -4375512945414709100,
                                        'source_pixel_width': -4962540987563720717,
                                        'source_pixel_height': -2865590183752447340,
                                        'rotation': -1243144042726565539,
                                        'virtual_nw_x_pixel': 1556966340,
                                        'virtual_nw_y_pixel': 851077456,
                                        'virtual_width': -227590008,
                                        'virtual_height': -1627999255,
                                    },
                            {
                                        'source_monitor': 5660909,
                                        'source_nw_x_pixel': -1759871361521781290,
                                        'source_nw_y_pixel': -4037577079099402791,
                                        'source_pixel_width': -2481084875746923988,
                                        'source_pixel_height': -4640952329273430992,
                                        'rotation': -5697716441150191244,
                                        'virtual_nw_x_pixel': -1413761474,
                                        'virtual_nw_y_pixel': 1617134373,
                                        'virtual_width': -1978551878,
                                        'virtual_height': 432045611,
                                    },
                            {
                                        'source_monitor': 2389271,
                                        'source_nw_x_pixel': -7386492613856052055,
                                        'source_nw_y_pixel': -2424907524814844204,
                                        'source_pixel_width': -5254583057315824442,
                                        'source_pixel_height': -838743002729206942,
                                        'rotation': -1537895304635828153,
                                        'virtual_nw_x_pixel': -30490430,
                                        'virtual_nw_y_pixel': 82208020,
                                        'virtual_width': -204416547,
                                        'virtual_height': 757437454,
                                    },
                            {
                                        'source_monitor': 7618854,
                                        'source_nw_x_pixel': -2560275662684390605,
                                        'source_nw_y_pixel': -6589451936933490895,
                                        'source_pixel_width': -4440595864932755576,
                                        'source_pixel_height': -7635777665712665955,
                                        'rotation': -7848392732668870997,
                                        'virtual_nw_x_pixel': -1824449027,
                                        'virtual_nw_y_pixel': -1169266255,
                                        'virtual_width': -702870596,
                                        'virtual_height': 1175363830,
                                    },
                            {
                                        'source_monitor': 8474265,
                                        'source_nw_x_pixel': -1695665425070104723,
                                        'source_nw_y_pixel': -6831607938035549174,
                                        'source_pixel_width': -7663521244441331499,
                                        'source_pixel_height': -5303498997450667396,
                                        'rotation': -1940183831735011173,
                                        'virtual_nw_x_pixel': 1294482930,
                                        'virtual_nw_y_pixel': 1783971414,
                                        'virtual_width': 11864995,
                                        'virtual_height': 1086144311,
                                    },
                            {
                                        'source_monitor': 1540256,
                                        'source_nw_x_pixel': -2603773858143685793,
                                        'source_nw_y_pixel': -7078939228629609023,
                                        'source_pixel_width': -244780853631810703,
                                        'source_pixel_height': -1155967631910388459,
                                        'rotation': -3625413535338403350,
                                        'virtual_nw_x_pixel': 1463504555,
                                        'virtual_nw_y_pixel': -868965291,
                                        'virtual_width': -842297088,
                                        'virtual_height': -1888216780,
                                    },
                        ],
                },
                {
                    'description': 'πÙѕŦЕŭџ¾ɧɕѦĭƒñý£ɁӜǜȋңKɻЛХЎAɤ\x9cЬ',
                    'monitors': [
                            {
                                        'identifier': 975462,
                                        'width': 5234966274421129739,
                                        'height': 4107631986309045464,
                                    },
                            {
                                        'identifier': 5499703,
                                        'width': -6287019429187306441,
                                        'height': -539980533137545185,
                                    },
                            {
                                        'identifier': 5416615,
                                        'width': -5024116786490796415,
                                        'height': 8882842181444945019,
                                    },
                            {
                                        'identifier': 3963367,
                                        'width': 6366290987042493488,
                                        'height': -1037744442026292995,
                                    },
                            {
                                        'identifier': 4934064,
                                        'width': 8948099462632537527,
                                        'height': -289816864925197684,
                                    },
                            {
                                        'identifier': 4161436,
                                        'width': 508666629385311197,
                                        'height': -4884190048424563753,
                                    },
                            {
                                        'identifier': 4990313,
                                        'width': 9077397493844637776,
                                        'height': -1864438921773455918,
                                    },
                            {
                                        'identifier': 9767894,
                                        'width': -8803141795410133591,
                                        'height': -7166944149361766619,
                                    },
                            {
                                        'identifier': 2922269,
                                        'width': -7584537573898867845,
                                        'height': 4100856201653007613,
                                    },
                            {
                                        'identifier': 5649412,
                                        'width': 7645172677635426659,
                                        'height': 7689649799706133415,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2476514,
                                        'source_nw_x_pixel': -2632424287728383862,
                                        'source_nw_y_pixel': -1716292677550437906,
                                        'source_pixel_width': -4508306924721497361,
                                        'source_pixel_height': -581426528892058748,
                                        'rotation': -4768809309976991454,
                                        'virtual_nw_x_pixel': -1131119675,
                                        'virtual_nw_y_pixel': -900645250,
                                        'virtual_width': 966331187,
                                        'virtual_height': -456464993,
                                    },
                            {
                                        'source_monitor': 8497508,
                                        'source_nw_x_pixel': -5683969231200256213,
                                        'source_nw_y_pixel': -2542878805390425524,
                                        'source_pixel_width': -9049899446746538521,
                                        'source_pixel_height': -2803136578564148251,
                                        'rotation': -1803043901807299181,
                                        'virtual_nw_x_pixel': -435015275,
                                        'virtual_nw_y_pixel': -134860231,
                                        'virtual_width': -1339371768,
                                        'virtual_height': 957041625,
                                    },
                            {
                                        'source_monitor': 1886003,
                                        'source_nw_x_pixel': -2661527200963485747,
                                        'source_nw_y_pixel': -5599937322612627290,
                                        'source_pixel_width': -3711827498281179814,
                                        'source_pixel_height': -1609334163327703650,
                                        'rotation': -5062709654124870254,
                                        'virtual_nw_x_pixel': -576031840,
                                        'virtual_nw_y_pixel': 30022226,
                                        'virtual_width': 774954471,
                                        'virtual_height': 949764345,
                                    },
                            {
                                        'source_monitor': 1941663,
                                        'source_nw_x_pixel': -995819526162197243,
                                        'source_nw_y_pixel': -2409978665311646815,
                                        'source_pixel_width': -4634596483209124192,
                                        'source_pixel_height': -5550641936788731255,
                                        'rotation': -6127782118347409413,
                                        'virtual_nw_x_pixel': 215846426,
                                        'virtual_nw_y_pixel': -1359519662,
                                        'virtual_width': -1622586819,
                                        'virtual_height': 62049235,
                                    },
                            {
                                        'source_monitor': 6062258,
                                        'source_nw_x_pixel': -8245584508990854833,
                                        'source_nw_y_pixel': -1014981153134263694,
                                        'source_pixel_width': -1953784826554643434,
                                        'source_pixel_height': -7598161274595221446,
                                        'rotation': -761290549234998834,
                                        'virtual_nw_x_pixel': -1846168215,
                                        'virtual_nw_y_pixel': 1012072971,
                                        'virtual_width': -501592324,
                                        'virtual_height': -1386648669,
                                    },
                            {
                                        'source_monitor': 932008,
                                        'source_nw_x_pixel': -2597730336761159671,
                                        'source_nw_y_pixel': -2901790164149850384,
                                        'source_pixel_width': -2902647156099130316,
                                        'source_pixel_height': -9096008058161714614,
                                        'rotation': -5304443552905768162,
                                        'virtual_nw_x_pixel': 689038957,
                                        'virtual_nw_y_pixel': 914756915,
                                        'virtual_width': -504657867,
                                        'virtual_height': 1978459472,
                                    },
                            {
                                        'source_monitor': 921303,
                                        'source_nw_x_pixel': -7568757996429009306,
                                        'source_nw_y_pixel': -3652406914024045758,
                                        'source_pixel_width': -2557046019581640088,
                                        'source_pixel_height': -6173150935155213618,
                                        'rotation': -4420479369461353620,
                                        'virtual_nw_x_pixel': 419255621,
                                        'virtual_nw_y_pixel': 1920873811,
                                        'virtual_width': 205004144,
                                        'virtual_height': 1820337834,
                                    },
                            {
                                        'source_monitor': 9044636,
                                        'source_nw_x_pixel': -4645965819118991179,
                                        'source_nw_y_pixel': -29277395445094437,
                                        'source_pixel_width': -3060870230573819197,
                                        'source_pixel_height': -8176421203451684885,
                                        'rotation': -8474260071584415485,
                                        'virtual_nw_x_pixel': 482614006,
                                        'virtual_nw_y_pixel': -1792946504,
                                        'virtual_width': -800093656,
                                        'virtual_height': -823980465,
                                    },
                            {
                                        'source_monitor': 2960812,
                                        'source_nw_x_pixel': -3497327258011130511,
                                        'source_nw_y_pixel': -6147529236177352419,
                                        'source_pixel_width': -3744435210316709760,
                                        'source_pixel_height': -2384111965692282635,
                                        'rotation': -8454267646934171697,
                                        'virtual_nw_x_pixel': 1083420066,
                                        'virtual_nw_y_pixel': 1284379655,
                                        'virtual_width': -1098869233,
                                        'virtual_height': -207608439,
                                    },
                            {
                                        'source_monitor': 4307199,
                                        'source_nw_x_pixel': -5199504296213012389,
                                        'source_nw_y_pixel': -9014646823567781603,
                                        'source_pixel_width': -6765108054743695192,
                                        'source_pixel_height': -8670433774086896713,
                                        'rotation': -4289847209538741919,
                                        'virtual_nw_x_pixel': 1295178961,
                                        'virtual_nw_y_pixel': -966043238,
                                        'virtual_width': 263628612,
                                        'virtual_height': -1685035859,
                                    },
                        ],
                },
                {
                    'description': 'ĖŁҙҲчϔ˱ʞϋɳŐŞ\x823Ț˥Ǧ\u0380ùǧʝ˅ȁԐЁ{ɥĿԞΘ',
                    'monitors': [
                            {
                                        'identifier': 2860728,
                                        'width': -6329451213942420034,
                                        'height': 5034610018110612645,
                                    },
                            {
                                        'identifier': 6347972,
                                        'width': -8268326269582535555,
                                        'height': 3837690061377880697,
                                    },
                            {
                                        'identifier': 689210,
                                        'width': -5948765139934002778,
                                        'height': -2830876216067154173,
                                    },
                            {
                                        'identifier': 9832901,
                                        'width': -3545006206261203241,
                                        'height': -1376008678672263382,
                                    },
                            {
                                        'identifier': 2977206,
                                        'width': 5435184634728126505,
                                        'height': -785013875741610992,
                                    },
                            {
                                        'identifier': -450299,
                                        'width': 4390408000695431243,
                                        'height': -2209355069781293194,
                                    },
                            {
                                        'identifier': 742187,
                                        'width': 214435466124198024,
                                        'height': -621920965832065690,
                                    },
                            {
                                        'identifier': 5760851,
                                        'width': -1170337589355459280,
                                        'height': 2979789405459066162,
                                    },
                            {
                                        'identifier': 3765250,
                                        'width': 7301846979978515010,
                                        'height': 666188411814460833,
                                    },
                            {
                                        'identifier': 8731263,
                                        'width': -3252913803422294205,
                                        'height': -7712755454473307502,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2397983,
                                        'source_nw_x_pixel': -7950697288133055475,
                                        'source_nw_y_pixel': -2965503114129373150,
                                        'source_pixel_width': -4738113457942196604,
                                        'source_pixel_height': -805124869944457614,
                                        'rotation': -4747507311138757294,
                                        'virtual_nw_x_pixel': -1917056688,
                                        'virtual_nw_y_pixel': 49562575,
                                        'virtual_width': 1839454250,
                                        'virtual_height': -859683181,
                                    },
                            {
                                        'source_monitor': 1289427,
                                        'source_nw_x_pixel': -4732241241520808065,
                                        'source_nw_y_pixel': -6335406868951971124,
                                        'source_pixel_width': -4798401513222858400,
                                        'source_pixel_height': -1374743009774378880,
                                        'rotation': -5074984094863041235,
                                        'virtual_nw_x_pixel': -1238181405,
                                        'virtual_nw_y_pixel': -1397687538,
                                        'virtual_width': 1296023382,
                                        'virtual_height': 1250107113,
                                    },
                            {
                                        'source_monitor': 8605700,
                                        'source_nw_x_pixel': -5783347255818670819,
                                        'source_nw_y_pixel': -8511459902381817798,
                                        'source_pixel_width': -135043129446197754,
                                        'source_pixel_height': -6303694883912610431,
                                        'rotation': -5214984887450434705,
                                        'virtual_nw_x_pixel': -1140752035,
                                        'virtual_nw_y_pixel': 1715106818,
                                        'virtual_width': 754503935,
                                        'virtual_height': -1494174051,
                                    },
                            {
                                        'source_monitor': 1095417,
                                        'source_nw_x_pixel': -1154614179895554667,
                                        'source_nw_y_pixel': -7417573559213308337,
                                        'source_pixel_width': -4696557461008574895,
                                        'source_pixel_height': -7966790980834532437,
                                        'rotation': -4806850379352265165,
                                        'virtual_nw_x_pixel': -1732916972,
                                        'virtual_nw_y_pixel': -1459656913,
                                        'virtual_width': 1304032307,
                                        'virtual_height': 339296752,
                                    },
                            {
                                        'source_monitor': 6457033,
                                        'source_nw_x_pixel': -208135076397307454,
                                        'source_nw_y_pixel': -1354779401030263810,
                                        'source_pixel_width': -1334270104881256154,
                                        'source_pixel_height': -7074770587275875054,
                                        'rotation': -3644236091103121565,
                                        'virtual_nw_x_pixel': -896670420,
                                        'virtual_nw_y_pixel': -1465140120,
                                        'virtual_width': -1184219663,
                                        'virtual_height': 888524354,
                                    },
                            {
                                        'source_monitor': 1615045,
                                        'source_nw_x_pixel': -6644315293391574657,
                                        'source_nw_y_pixel': -2777094948287948004,
                                        'source_pixel_width': -1387658049378695883,
                                        'source_pixel_height': -516001277724468164,
                                        'rotation': -5882589434393313258,
                                        'virtual_nw_x_pixel': 414590492,
                                        'virtual_nw_y_pixel': 224465851,
                                        'virtual_width': -484709740,
                                        'virtual_height': 1017095565,
                                    },
                            {
                                        'source_monitor': 9949896,
                                        'source_nw_x_pixel': -60058031025062229,
                                        'source_nw_y_pixel': -7260053678988755823,
                                        'source_pixel_width': -7578979827647297144,
                                        'source_pixel_height': -1275595396744225657,
                                        'rotation': -6184981667995789641,
                                        'virtual_nw_x_pixel': -1587521732,
                                        'virtual_nw_y_pixel': -1771479226,
                                        'virtual_width': 97490676,
                                        'virtual_height': 1651615399,
                                    },
                            {
                                        'source_monitor': -232406,
                                        'source_nw_x_pixel': -8320460582784981216,
                                        'source_nw_y_pixel': -4071668046297713234,
                                        'source_pixel_width': -3920586277549394690,
                                        'source_pixel_height': -1882563774382684646,
                                        'rotation': -7296553548147299698,
                                        'virtual_nw_x_pixel': 1738658731,
                                        'virtual_nw_y_pixel': -826643414,
                                        'virtual_width': 1281420957,
                                        'virtual_height': 298564061,
                                    },
                            {
                                        'source_monitor': 5272343,
                                        'source_nw_x_pixel': -5633155540097907290,
                                        'source_nw_y_pixel': -6853767339735340586,
                                        'source_pixel_width': -7218113844933227811,
                                        'source_pixel_height': -1578196612733657531,
                                        'rotation': -5254784887089658337,
                                        'virtual_nw_x_pixel': 404540114,
                                        'virtual_nw_y_pixel': -816232443,
                                        'virtual_width': 97545174,
                                        'virtual_height': -1181312819,
                                    },
                            {
                                        'source_monitor': 4871533,
                                        'source_nw_x_pixel': -7057912751982223664,
                                        'source_nw_y_pixel': -2959706439920305934,
                                        'source_pixel_width': -7891281988549011134,
                                        'source_pixel_height': -4207403887229743949,
                                        'rotation': -6571510303005574830,
                                        'virtual_nw_x_pixel': -1999671056,
                                        'virtual_nw_y_pixel': 679356449,
                                        'virtual_width': -1908420611,
                                        'virtual_height': 1450074006,
                                    },
                        ],
                },
                {
                    'description': 'µҭҹϬέӈ\x83ȘҡĴӡǥď\x8dɰӦðʵʑɻǶ҈ƯɯȊ6\x81ӤԔʑ',
                    'monitors': [
                            {
                                        'identifier': 8931804,
                                        'width': -5405066791379652028,
                                        'height': 4675502436245245720,
                                    },
                            {
                                        'identifier': 8770671,
                                        'width': 8559970711106805643,
                                        'height': -470943433516105911,
                                    },
                            {
                                        'identifier': 2592238,
                                        'width': -7447640444350335785,
                                        'height': 6868731426352251353,
                                    },
                            {
                                        'identifier': -394082,
                                        'width': 1256464834979866661,
                                        'height': 9047520960479475009,
                                    },
                            {
                                        'identifier': 4801787,
                                        'width': 4673350094862753534,
                                        'height': -720790704715872826,
                                    },
                            {
                                        'identifier': 4542538,
                                        'width': 4484076022802971055,
                                        'height': 1060003269641838923,
                                    },
                            {
                                        'identifier': 6691595,
                                        'width': 8864667657222577546,
                                        'height': 4077547172872133227,
                                    },
                            {
                                        'identifier': 6471306,
                                        'width': -3579431882227369371,
                                        'height': 2304814361167471880,
                                    },
                            {
                                        'identifier': 6192519,
                                        'width': -2491352000063667013,
                                        'height': -2944793404954025497,
                                    },
                            {
                                        'identifier': 1692197,
                                        'width': -2579630926117619310,
                                        'height': 6357883601440819681,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1156258,
                                        'source_nw_x_pixel': -9169765463716175820,
                                        'source_nw_y_pixel': -6830855649385444151,
                                        'source_pixel_width': -8740120652321504659,
                                        'source_pixel_height': -9137319236779235041,
                                        'rotation': -6327228998797018222,
                                        'virtual_nw_x_pixel': 212996041,
                                        'virtual_nw_y_pixel': 813317189,
                                        'virtual_width': -1601153260,
                                        'virtual_height': 1360415953,
                                    },
                            {
                                        'source_monitor': -180371,
                                        'source_nw_x_pixel': -7582228906825942452,
                                        'source_nw_y_pixel': -434185603220976395,
                                        'source_pixel_width': -1785144125637626237,
                                        'source_pixel_height': -8217973500154502570,
                                        'rotation': -8148926321399081208,
                                        'virtual_nw_x_pixel': -1894902516,
                                        'virtual_nw_y_pixel': -69812945,
                                        'virtual_width': -1298582744,
                                        'virtual_height': -1880486883,
                                    },
                            {
                                        'source_monitor': 6629382,
                                        'source_nw_x_pixel': -6522646381898235693,
                                        'source_nw_y_pixel': -3241777827057049686,
                                        'source_pixel_width': -36947390318279444,
                                        'source_pixel_height': -6223475940702445785,
                                        'rotation': -2228179161981851271,
                                        'virtual_nw_x_pixel': -245652322,
                                        'virtual_nw_y_pixel': -1535049848,
                                        'virtual_width': -98695759,
                                        'virtual_height': -1243537176,
                                    },
                            {
                                        'source_monitor': 5891918,
                                        'source_nw_x_pixel': -7761078556124214378,
                                        'source_nw_y_pixel': -7414346373305375798,
                                        'source_pixel_width': -512537590814639320,
                                        'source_pixel_height': -4121778650742112539,
                                        'rotation': -2420033162463855948,
                                        'virtual_nw_x_pixel': -123001482,
                                        'virtual_nw_y_pixel': -300464776,
                                        'virtual_width': 1517870878,
                                        'virtual_height': -216377383,
                                    },
                            {
                                        'source_monitor': 1262748,
                                        'source_nw_x_pixel': -6864095509071503589,
                                        'source_nw_y_pixel': -1742267648291231810,
                                        'source_pixel_width': -3906398100771333514,
                                        'source_pixel_height': -6015578707356747406,
                                        'rotation': -696338649317339710,
                                        'virtual_nw_x_pixel': 1733627871,
                                        'virtual_nw_y_pixel': -19838309,
                                        'virtual_width': 1422401332,
                                        'virtual_height': -1193297995,
                                    },
                            {
                                        'source_monitor': 6567217,
                                        'source_nw_x_pixel': -8014861082484415562,
                                        'source_nw_y_pixel': -3204470297653456821,
                                        'source_pixel_width': -665062230944786393,
                                        'source_pixel_height': -911220831422736490,
                                        'rotation': -2182019410054393500,
                                        'virtual_nw_x_pixel': 32039905,
                                        'virtual_nw_y_pixel': 994758783,
                                        'virtual_width': 1930186296,
                                        'virtual_height': 1510431413,
                                    },
                            {
                                        'source_monitor': 5620948,
                                        'source_nw_x_pixel': -8808002604178445358,
                                        'source_nw_y_pixel': -7754650051093411627,
                                        'source_pixel_width': -6270647976472301367,
                                        'source_pixel_height': -1933691880812882057,
                                        'rotation': -1233709698577031995,
                                        'virtual_nw_x_pixel': 1168030957,
                                        'virtual_nw_y_pixel': -826440166,
                                        'virtual_width': -1988090094,
                                        'virtual_height': 882262697,
                                    },
                            {
                                        'source_monitor': 7342645,
                                        'source_nw_x_pixel': -1862420336749420358,
                                        'source_nw_y_pixel': -3413341489711429184,
                                        'source_pixel_width': -3581749243231876234,
                                        'source_pixel_height': -7389268864476411873,
                                        'rotation': -2582271979811317404,
                                        'virtual_nw_x_pixel': -1154314438,
                                        'virtual_nw_y_pixel': -1797887665,
                                        'virtual_width': 1382328543,
                                        'virtual_height': -728925877,
                                    },
                            {
                                        'source_monitor': -244235,
                                        'source_nw_x_pixel': -2121652896890495197,
                                        'source_nw_y_pixel': -5859534592426126950,
                                        'source_pixel_width': -7377350295026736879,
                                        'source_pixel_height': -1955607172121893461,
                                        'rotation': -5309936243126177324,
                                        'virtual_nw_x_pixel': 1038465833,
                                        'virtual_nw_y_pixel': -1954608443,
                                        'virtual_width': -370133739,
                                        'virtual_height': -872785186,
                                    },
                            {
                                        'source_monitor': 3126304,
                                        'source_nw_x_pixel': -6177927063664763259,
                                        'source_nw_y_pixel': -7554460257212529903,
                                        'source_pixel_width': -2968702863147102551,
                                        'source_pixel_height': -7033180034487290906,
                                        'rotation': -7917092111200489662,
                                        'virtual_nw_x_pixel': 1976885150,
                                        'virtual_nw_y_pixel': -990403071,
                                        'virtual_width': 193650202,
                                        'virtual_height': 1803046176,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'mapped_screens_by_monitors': [
                {
                    'monitors': [
                            {
                                        'identifier': 5105635,
                                        'width': -2789831124954505736,
                                        'height': -7086876390507613329,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -3980872264859717090,
                                        'source_nw_y_pixel': -4028011030813208329,
                                        'source_pixel_width': -3797376972071390121,
                                        'source_pixel_height': -6311961828614448411,
                                        'rotation': -553336287344020722,
                                        'virtual_nw_x_pixel': -819620539,
                                        'virtual_nw_y_pixel': -1357149595,
                                        'virtual_width': -1217884903,
                                        'virtual_height': -1900132943,
                                    },
                        ],
                },
            ],

        },
    ),
]
