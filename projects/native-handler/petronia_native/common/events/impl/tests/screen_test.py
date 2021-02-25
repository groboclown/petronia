# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-24T16:41:12.170426+00:00

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
            'identifier': 4372245,
            'width': 529655668515168647,
            'height': 8692506381601464514,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 8298070,

            'width': 7842029532726206669,

            'height': -5872151189209123267,

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
            'source_monitor': 3803040,
            'source_nw_x_pixel': -5491969325298705103,
            'source_nw_y_pixel': -2217228535611332399,
            'source_pixel_width': -1959532161835825205,
            'source_pixel_height': -671253375352720186,
            'rotation': -9062007626510490920,
            'virtual_nw_x_pixel': -274071915,
            'virtual_nw_y_pixel': -1451910177,
            'virtual_width': -1261620193,
            'virtual_height': 1930490262,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -9111607381392054766,

            'source_nw_y_pixel': -8260903818174492501,

            'source_pixel_width': -4556395341015016857,

            'source_pixel_height': -7328032968304241633,

            'rotation': -8758983496349785394,

            'virtual_nw_x_pixel': 1609848297,

            'virtual_nw_y_pixel': 616058910,

            'virtual_width': -216505505,

            'virtual_height': -1069692099,

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
            'description': 'ÐҺʏѼƄҒԥ§ҍƻϩ҃ĞϭŖ\x84\x82ӏɊ˙ĤԏEĈǹ¦ƌͿʫÜ',
            'monitors': [
                {
                    'identifier': 754494,
                    'width': 497330149802751899,
                    'height': 5611019678561494217,
                },
                {
                    'identifier': -64873,
                    'width': 7686601546007527652,
                    'height': 1313169705134664507,
                },
                {
                    'identifier': 381445,
                    'width': 1907475698653466808,
                    'height': -2827440153411867656,
                },
                {
                    'identifier': 8269756,
                    'width': -6494121183789315146,
                    'height': 4633621778824367492,
                },
                {
                    'identifier': 5863686,
                    'width': -6693208026025638082,
                    'height': 199900772686292585,
                },
                {
                    'identifier': 5246683,
                    'width': -3009680456064732763,
                    'height': 2497501379262491561,
                },
                {
                    'identifier': 5062096,
                    'width': 4687868953567385791,
                    'height': 5390413075102940838,
                },
                {
                    'identifier': 65043,
                    'width': 4786614916921166276,
                    'height': 5563749833390669630,
                },
                {
                    'identifier': 282850,
                    'width': -7777877063368019523,
                    'height': 4421701767627341409,
                },
                {
                    'identifier': 9423815,
                    'width': -8577953606971461228,
                    'height': 6560102955801789805,
                },
            ],
            'screen': [
                {
                    'source_monitor': 2893283,
                    'source_nw_x_pixel': -2025767312672462752,
                    'source_nw_y_pixel': -2541440378313504113,
                    'source_pixel_width': -1538480944684553065,
                    'source_pixel_height': -3725237124598433904,
                    'rotation': -316728143049870528,
                    'virtual_nw_x_pixel': -91325755,
                    'virtual_nw_y_pixel': 1402236705,
                    'virtual_width': 966983064,
                    'virtual_height': -1646622784,
                },
                {
                    'source_monitor': 3961443,
                    'source_nw_x_pixel': -329094807236501645,
                    'source_nw_y_pixel': -8715979673567200788,
                    'source_pixel_width': -6424703298608907750,
                    'source_pixel_height': -7511678600040019179,
                    'rotation': -2711954410035633732,
                    'virtual_nw_x_pixel': -1579750989,
                    'virtual_nw_y_pixel': -1465906343,
                    'virtual_width': -19402479,
                    'virtual_height': 1219939152,
                },
                {
                    'source_monitor': 6966530,
                    'source_nw_x_pixel': -5982895803729990459,
                    'source_nw_y_pixel': -305206385368634193,
                    'source_pixel_width': -3318714930391164018,
                    'source_pixel_height': -5865683143479354582,
                    'rotation': -5618399879713169446,
                    'virtual_nw_x_pixel': 1807835342,
                    'virtual_nw_y_pixel': 51892940,
                    'virtual_width': 1050792112,
                    'virtual_height': -1398056013,
                },
                {
                    'source_monitor': 1462858,
                    'source_nw_x_pixel': -3166791806194130627,
                    'source_nw_y_pixel': -6509856032420675968,
                    'source_pixel_width': -7256976067892903341,
                    'source_pixel_height': -6345733658967760763,
                    'rotation': -5516154895637307629,
                    'virtual_nw_x_pixel': -1444168117,
                    'virtual_nw_y_pixel': 1915563991,
                    'virtual_width': 536297481,
                    'virtual_height': -94155888,
                },
                {
                    'source_monitor': -310247,
                    'source_nw_x_pixel': -314227994816619617,
                    'source_nw_y_pixel': -4386410752003187346,
                    'source_pixel_width': -3706523380831255702,
                    'source_pixel_height': -1459539004499742754,
                    'rotation': -5564450006285027046,
                    'virtual_nw_x_pixel': -974538605,
                    'virtual_nw_y_pixel': -799872324,
                    'virtual_width': -1722769126,
                    'virtual_height': 109409130,
                },
                {
                    'source_monitor': 9105252,
                    'source_nw_x_pixel': -8936166937622253815,
                    'source_nw_y_pixel': -5130964567368600673,
                    'source_pixel_width': -7393982993875575183,
                    'source_pixel_height': -1763192259355565707,
                    'rotation': -9022390939990514591,
                    'virtual_nw_x_pixel': 906046995,
                    'virtual_nw_y_pixel': -1543403818,
                    'virtual_width': -1680024014,
                    'virtual_height': -1841515179,
                },
                {
                    'source_monitor': 609392,
                    'source_nw_x_pixel': -684626487675700144,
                    'source_nw_y_pixel': -4765377265579798634,
                    'source_pixel_width': -6192912088719425855,
                    'source_pixel_height': -2417490457884876116,
                    'rotation': -6823346540982956178,
                    'virtual_nw_x_pixel': 1044988121,
                    'virtual_nw_y_pixel': 97190867,
                    'virtual_width': 1341896704,
                    'virtual_height': 922163085,
                },
                {
                    'source_monitor': 1253444,
                    'source_nw_x_pixel': -2555039922170489458,
                    'source_nw_y_pixel': -955097108794891606,
                    'source_pixel_width': -8798187653979398542,
                    'source_pixel_height': -3152065395887887965,
                    'rotation': -6149357720388826129,
                    'virtual_nw_x_pixel': 1806684842,
                    'virtual_nw_y_pixel': -1377227234,
                    'virtual_width': -1919010628,
                    'virtual_height': -1703616352,
                },
                {
                    'source_monitor': 4216093,
                    'source_nw_x_pixel': -8820671565538228121,
                    'source_nw_y_pixel': -7413833919224785853,
                    'source_pixel_width': -8227929671450611713,
                    'source_pixel_height': -5845140549939231730,
                    'rotation': -5230614322231136383,
                    'virtual_nw_x_pixel': 896547748,
                    'virtual_nw_y_pixel': 1775167585,
                    'virtual_width': -1905537744,
                    'virtual_height': 1690737268,
                },
                {
                    'source_monitor': 1910267,
                    'source_nw_x_pixel': -7915129912671473909,
                    'source_nw_y_pixel': -3269272434329499032,
                    'source_pixel_width': -3680274246731796839,
                    'source_pixel_height': -1719083231584530911,
                    'rotation': -5714867037945847817,
                    'virtual_nw_x_pixel': -1433767057,
                    'virtual_nw_y_pixel': -797574262,
                    'virtual_width': 1170275924,
                    'virtual_height': 349704474,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 9212028,
                    'width': 5438670990178316681,
                    'height': -367196335567556561,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -8700079204460966343,
                    'source_nw_y_pixel': -4218403016936654274,
                    'source_pixel_width': -7444100827657586336,
                    'source_pixel_height': -4838526164375630090,
                    'rotation': -4929861285776470510,
                    'virtual_nw_x_pixel': -1587291660,
                    'virtual_nw_y_pixel': 950925627,
                    'virtual_width': 359740559,
                    'virtual_height': -783994556,
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
            'request_id': 7838461,
            'mapped_screens_by_monitors': [
                {
                    'description': 'Ģǁ]ȽӏұӇΈnюĖύx¹ήӖÜ\x8beҟʚȒѲǬʄŃŔеҢÏ',
                    'monitors': [
                            {
                                        'identifier': 6170256,
                                        'width': -4269048400244189440,
                                        'height': -5673254254365815900,
                                    },
                            {
                                        'identifier': 8684530,
                                        'width': -2639831221980048218,
                                        'height': -8992313194914275984,
                                    },
                            {
                                        'identifier': 6846918,
                                        'width': -4715003108625138497,
                                        'height': 8195280573100499879,
                                    },
                            {
                                        'identifier': 6539819,
                                        'width': -6947023066228415019,
                                        'height': 7851951086088089263,
                                    },
                            {
                                        'identifier': 6709316,
                                        'width': -1398308518076591708,
                                        'height': 3865483733608335029,
                                    },
                            {
                                        'identifier': 4441014,
                                        'width': 5945860414297421585,
                                        'height': -2994015478213837944,
                                    },
                            {
                                        'identifier': 63977,
                                        'width': 5958473253596792866,
                                        'height': -7574912719306418836,
                                    },
                            {
                                        'identifier': -131338,
                                        'width': 5483311745801786112,
                                        'height': 6136726218527745228,
                                    },
                            {
                                        'identifier': 4482699,
                                        'width': 6461357737505700306,
                                        'height': 7792852377631585890,
                                    },
                            {
                                        'identifier': 1439569,
                                        'width': 2670822631470870709,
                                        'height': -942965834028698497,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3304411,
                                        'source_nw_x_pixel': -426613450431383766,
                                        'source_nw_y_pixel': -6314423009423362615,
                                        'source_pixel_width': -5437789038185509657,
                                        'source_pixel_height': -5087030712248197820,
                                        'rotation': -2596465218649665238,
                                        'virtual_nw_x_pixel': -1086854077,
                                        'virtual_nw_y_pixel': 1809241430,
                                        'virtual_width': 1445499974,
                                        'virtual_height': 353923544,
                                    },
                            {
                                        'source_monitor': 8570044,
                                        'source_nw_x_pixel': -999406984507007161,
                                        'source_nw_y_pixel': -8675109852342222422,
                                        'source_pixel_width': -4737323425605234965,
                                        'source_pixel_height': -2401061573054781133,
                                        'rotation': -5915775292460298695,
                                        'virtual_nw_x_pixel': -1558543250,
                                        'virtual_nw_y_pixel': 949505395,
                                        'virtual_width': 704365914,
                                        'virtual_height': 1600827719,
                                    },
                            {
                                        'source_monitor': 5598036,
                                        'source_nw_x_pixel': -4071102477434174913,
                                        'source_nw_y_pixel': -580383970691124741,
                                        'source_pixel_width': -7703306998841316164,
                                        'source_pixel_height': -9202716262287288169,
                                        'rotation': -9071265399633953964,
                                        'virtual_nw_x_pixel': -1785463957,
                                        'virtual_nw_y_pixel': -501984770,
                                        'virtual_width': 1750376798,
                                        'virtual_height': 203753317,
                                    },
                            {
                                        'source_monitor': 3309656,
                                        'source_nw_x_pixel': -2857407164664442638,
                                        'source_nw_y_pixel': -1557080004472456826,
                                        'source_pixel_width': -4716008215383896144,
                                        'source_pixel_height': -2027506688927963015,
                                        'rotation': -2746608954288679581,
                                        'virtual_nw_x_pixel': -853546169,
                                        'virtual_nw_y_pixel': 609261020,
                                        'virtual_width': -794839676,
                                        'virtual_height': 1009864173,
                                    },
                            {
                                        'source_monitor': 5057802,
                                        'source_nw_x_pixel': -1687320277975722786,
                                        'source_nw_y_pixel': -7141767505856894855,
                                        'source_pixel_width': -5603573957298211705,
                                        'source_pixel_height': -1735960759262917781,
                                        'rotation': -7062212497256338756,
                                        'virtual_nw_x_pixel': 482459692,
                                        'virtual_nw_y_pixel': 298393932,
                                        'virtual_width': 1941877003,
                                        'virtual_height': -1490789736,
                                    },
                            {
                                        'source_monitor': 1793828,
                                        'source_nw_x_pixel': -4499549717945206075,
                                        'source_nw_y_pixel': -3404647651115890208,
                                        'source_pixel_width': -5501132951996675814,
                                        'source_pixel_height': -113854370935457582,
                                        'rotation': -2659280921540751221,
                                        'virtual_nw_x_pixel': 881946630,
                                        'virtual_nw_y_pixel': -853201328,
                                        'virtual_width': 1429834218,
                                        'virtual_height': 1292279853,
                                    },
                            {
                                        'source_monitor': -803446,
                                        'source_nw_x_pixel': -4867327666869657101,
                                        'source_nw_y_pixel': -92033051014197440,
                                        'source_pixel_width': -796856169067136942,
                                        'source_pixel_height': -3484266452462021440,
                                        'rotation': -804979937615785028,
                                        'virtual_nw_x_pixel': 760676599,
                                        'virtual_nw_y_pixel': -1320973819,
                                        'virtual_width': -444404590,
                                        'virtual_height': -1963390198,
                                    },
                            {
                                        'source_monitor': 8912110,
                                        'source_nw_x_pixel': -6398390781305271475,
                                        'source_nw_y_pixel': -7802299634888057014,
                                        'source_pixel_width': -4580476820411426072,
                                        'source_pixel_height': -6952250502460249921,
                                        'rotation': -1975087516358049307,
                                        'virtual_nw_x_pixel': 984005149,
                                        'virtual_nw_y_pixel': 1064823132,
                                        'virtual_width': -177678793,
                                        'virtual_height': -29802856,
                                    },
                            {
                                        'source_monitor': 7125654,
                                        'source_nw_x_pixel': -8199779842766636684,
                                        'source_nw_y_pixel': -7355235978304240493,
                                        'source_pixel_width': -1014120654569756716,
                                        'source_pixel_height': -4993865461700167484,
                                        'rotation': -1077290272562005131,
                                        'virtual_nw_x_pixel': -331769305,
                                        'virtual_nw_y_pixel': 1803776206,
                                        'virtual_width': -1363603135,
                                        'virtual_height': 981798642,
                                    },
                            {
                                        'source_monitor': 6198526,
                                        'source_nw_x_pixel': -6864132634123978701,
                                        'source_nw_y_pixel': -8218110997161680908,
                                        'source_pixel_width': -1658877132289967093,
                                        'source_pixel_height': -6353007084189859806,
                                        'rotation': -7039769667173848720,
                                        'virtual_nw_x_pixel': 355159418,
                                        'virtual_nw_y_pixel': 1347001121,
                                        'virtual_width': -964835879,
                                        'virtual_height': -888798413,
                                    },
                        ],
                },
                {
                    'description': 'ðĖԦƛ҈ԎȗÄҁŀӴȆӏuƆДʺöŹʪŌɫғŎʕԠƼИƽX',
                    'monitors': [
                            {
                                        'identifier': 6655316,
                                        'width': -7090721971502525262,
                                        'height': -521517944822088822,
                                    },
                            {
                                        'identifier': 2063002,
                                        'width': 6574971930119661410,
                                        'height': 6681839875320920934,
                                    },
                            {
                                        'identifier': 6452705,
                                        'width': 3235246440930689513,
                                        'height': -5507240903405887842,
                                    },
                            {
                                        'identifier': 6929020,
                                        'width': -7293232576820729127,
                                        'height': 5620627581250503571,
                                    },
                            {
                                        'identifier': 481455,
                                        'width': 2778521716452746977,
                                        'height': 6152061721163320610,
                                    },
                            {
                                        'identifier': 6173141,
                                        'width': 8715682132636983523,
                                        'height': -6799818328818745466,
                                    },
                            {
                                        'identifier': 5087614,
                                        'width': -5695823649069167931,
                                        'height': -7858009889353961820,
                                    },
                            {
                                        'identifier': 1252362,
                                        'width': -407630714912899029,
                                        'height': -698618835476391316,
                                    },
                            {
                                        'identifier': 5398232,
                                        'width': -1737841372499672561,
                                        'height': -5561295162974993825,
                                    },
                            {
                                        'identifier': 3608029,
                                        'width': 4809246689907336327,
                                        'height': 3525873462706013686,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7845959,
                                        'source_nw_x_pixel': -277896119947859987,
                                        'source_nw_y_pixel': -5636986172916780630,
                                        'source_pixel_width': -2306650184391142248,
                                        'source_pixel_height': -83345045182071979,
                                        'rotation': -5532613730080951813,
                                        'virtual_nw_x_pixel': 1650864254,
                                        'virtual_nw_y_pixel': -1574451978,
                                        'virtual_width': -1370740692,
                                        'virtual_height': 1392013389,
                                    },
                            {
                                        'source_monitor': 3491457,
                                        'source_nw_x_pixel': -8832820460205632043,
                                        'source_nw_y_pixel': -2261817644044669299,
                                        'source_pixel_width': -2018349353750518100,
                                        'source_pixel_height': -5426518649680979181,
                                        'rotation': -5352475149500370152,
                                        'virtual_nw_x_pixel': 105489839,
                                        'virtual_nw_y_pixel': -1109812385,
                                        'virtual_width': -1694590254,
                                        'virtual_height': 1164180340,
                                    },
                            {
                                        'source_monitor': -415125,
                                        'source_nw_x_pixel': -1879825463061726823,
                                        'source_nw_y_pixel': -5302299775390237484,
                                        'source_pixel_width': -3779904559043907621,
                                        'source_pixel_height': -3399109456966287522,
                                        'rotation': -374790589269859672,
                                        'virtual_nw_x_pixel': 439613993,
                                        'virtual_nw_y_pixel': 1471748390,
                                        'virtual_width': -1424479250,
                                        'virtual_height': -1226695336,
                                    },
                            {
                                        'source_monitor': 2417722,
                                        'source_nw_x_pixel': -2453036306381122786,
                                        'source_nw_y_pixel': -1193821904240243675,
                                        'source_pixel_width': -6127212688961988917,
                                        'source_pixel_height': -5268976711060366459,
                                        'rotation': -8415251208528918437,
                                        'virtual_nw_x_pixel': -1486325690,
                                        'virtual_nw_y_pixel': -1697061075,
                                        'virtual_width': 1428257182,
                                        'virtual_height': 592754130,
                                    },
                            {
                                        'source_monitor': 852416,
                                        'source_nw_x_pixel': -4656591137144677786,
                                        'source_nw_y_pixel': -3367010705008659962,
                                        'source_pixel_width': -3752046830986289713,
                                        'source_pixel_height': -2767192787900547405,
                                        'rotation': -3594662496437332666,
                                        'virtual_nw_x_pixel': -1568768140,
                                        'virtual_nw_y_pixel': -1094074009,
                                        'virtual_width': -1729887579,
                                        'virtual_height': 867205811,
                                    },
                            {
                                        'source_monitor': 8837549,
                                        'source_nw_x_pixel': -8264475903939462470,
                                        'source_nw_y_pixel': -7739918344325772975,
                                        'source_pixel_width': -1627764212689116067,
                                        'source_pixel_height': -4283371514759711320,
                                        'rotation': -8489234511902741704,
                                        'virtual_nw_x_pixel': -1733162610,
                                        'virtual_nw_y_pixel': 951389997,
                                        'virtual_width': -1559130895,
                                        'virtual_height': 1266579204,
                                    },
                            {
                                        'source_monitor': 4145098,
                                        'source_nw_x_pixel': -4785012385665195317,
                                        'source_nw_y_pixel': -505153191591563224,
                                        'source_pixel_width': -131524178810238042,
                                        'source_pixel_height': -6406337195548231551,
                                        'rotation': -6395301386301916791,
                                        'virtual_nw_x_pixel': -1362048759,
                                        'virtual_nw_y_pixel': 909020793,
                                        'virtual_width': 638523182,
                                        'virtual_height': -1030491065,
                                    },
                            {
                                        'source_monitor': 1651881,
                                        'source_nw_x_pixel': -3554063987527628978,
                                        'source_nw_y_pixel': -9189837786747617092,
                                        'source_pixel_width': -3009899600172835077,
                                        'source_pixel_height': -3506809983180479384,
                                        'rotation': -3990914263981306556,
                                        'virtual_nw_x_pixel': -670078793,
                                        'virtual_nw_y_pixel': -482436781,
                                        'virtual_width': -1516196981,
                                        'virtual_height': 1470798735,
                                    },
                            {
                                        'source_monitor': 1537835,
                                        'source_nw_x_pixel': -3398425076241707134,
                                        'source_nw_y_pixel': -5092015064799637705,
                                        'source_pixel_width': -3030963457097106938,
                                        'source_pixel_height': -4398127550527821726,
                                        'rotation': -3315082761680475105,
                                        'virtual_nw_x_pixel': 1716801396,
                                        'virtual_nw_y_pixel': -1043988976,
                                        'virtual_width': 1448843860,
                                        'virtual_height': -941181974,
                                    },
                            {
                                        'source_monitor': 1224640,
                                        'source_nw_x_pixel': -2657928218914607137,
                                        'source_nw_y_pixel': -7066875304262933372,
                                        'source_pixel_width': -6391771133479441440,
                                        'source_pixel_height': -6946779764560350143,
                                        'rotation': -833979372341240885,
                                        'virtual_nw_x_pixel': -1217254744,
                                        'virtual_nw_y_pixel': 1882547719,
                                        'virtual_width': -1932806969,
                                        'virtual_height': -1581775982,
                                    },
                        ],
                },
                {
                    'description': 'ǱęЙƉЗ;ȃfO²ДŧһɽμƪӴѫԛԓqƝәŭϊϩӖĴȽÍ',
                    'monitors': [
                            {
                                        'identifier': 2181294,
                                        'width': 250211114462469904,
                                        'height': -434419114407478718,
                                    },
                            {
                                        'identifier': 1696305,
                                        'width': -5553748451681510328,
                                        'height': 4776594594695632887,
                                    },
                            {
                                        'identifier': 6018788,
                                        'width': 5488634792142703894,
                                        'height': 5095236769085315540,
                                    },
                            {
                                        'identifier': 1656409,
                                        'width': -5550670391463433615,
                                        'height': 5634922038097281912,
                                    },
                            {
                                        'identifier': 8847216,
                                        'width': 7672797108811681370,
                                        'height': 6146314144186945416,
                                    },
                            {
                                        'identifier': 1544460,
                                        'width': 5532238446058942679,
                                        'height': -2079603759072332110,
                                    },
                            {
                                        'identifier': 4174859,
                                        'width': 2963177203395341750,
                                        'height': 2999747686198171744,
                                    },
                            {
                                        'identifier': 6658501,
                                        'width': 1195332545518139756,
                                        'height': 3842746952503803423,
                                    },
                            {
                                        'identifier': 7600005,
                                        'width': 4312630814503864401,
                                        'height': 7972292242532673528,
                                    },
                            {
                                        'identifier': 5891093,
                                        'width': 7767009537660958773,
                                        'height': -7207191471341914126,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3429629,
                                        'source_nw_x_pixel': -942050008025446653,
                                        'source_nw_y_pixel': -1853904857585831149,
                                        'source_pixel_width': -4916060302438491829,
                                        'source_pixel_height': -376168012509869485,
                                        'rotation': -7514622662204491629,
                                        'virtual_nw_x_pixel': 1079491000,
                                        'virtual_nw_y_pixel': -601451528,
                                        'virtual_width': 1650915717,
                                        'virtual_height': -1322745714,
                                    },
                            {
                                        'source_monitor': -555256,
                                        'source_nw_x_pixel': -6303225877878550412,
                                        'source_nw_y_pixel': -6963998029090679018,
                                        'source_pixel_width': -4744690463382046388,
                                        'source_pixel_height': -3775434625984398567,
                                        'rotation': -3168787456253803531,
                                        'virtual_nw_x_pixel': 724986403,
                                        'virtual_nw_y_pixel': -104879936,
                                        'virtual_width': 926014145,
                                        'virtual_height': 1474816472,
                                    },
                            {
                                        'source_monitor': 757076,
                                        'source_nw_x_pixel': -8808552014731672174,
                                        'source_nw_y_pixel': -4060413116807738284,
                                        'source_pixel_width': -212459554791895891,
                                        'source_pixel_height': -4518855521223714115,
                                        'rotation': -4039627724501106907,
                                        'virtual_nw_x_pixel': 329605464,
                                        'virtual_nw_y_pixel': -956655832,
                                        'virtual_width': -671389919,
                                        'virtual_height': -1655552327,
                                    },
                            {
                                        'source_monitor': 7721671,
                                        'source_nw_x_pixel': -1906920303030133822,
                                        'source_nw_y_pixel': -1609620238628468271,
                                        'source_pixel_width': -7645279932850911286,
                                        'source_pixel_height': -1000629695813663807,
                                        'rotation': -7101087318440851539,
                                        'virtual_nw_x_pixel': 680698191,
                                        'virtual_nw_y_pixel': -152337164,
                                        'virtual_width': 1971154791,
                                        'virtual_height': 1419894657,
                                    },
                            {
                                        'source_monitor': 5598198,
                                        'source_nw_x_pixel': -3323057984801389430,
                                        'source_nw_y_pixel': -2676895462132705047,
                                        'source_pixel_width': -4005006898709824790,
                                        'source_pixel_height': -8142172120735430856,
                                        'rotation': -6373896737130770526,
                                        'virtual_nw_x_pixel': -730933717,
                                        'virtual_nw_y_pixel': 1742277056,
                                        'virtual_width': 1485019767,
                                        'virtual_height': -300786128,
                                    },
                            {
                                        'source_monitor': 7961772,
                                        'source_nw_x_pixel': -2161937314558096308,
                                        'source_nw_y_pixel': -5103664229969277825,
                                        'source_pixel_width': -849812220964062345,
                                        'source_pixel_height': -6170469311193142895,
                                        'rotation': -1261996016254818708,
                                        'virtual_nw_x_pixel': 63511838,
                                        'virtual_nw_y_pixel': -1434450003,
                                        'virtual_width': -1054454507,
                                        'virtual_height': 740617016,
                                    },
                            {
                                        'source_monitor': 1184463,
                                        'source_nw_x_pixel': -3881600815761327670,
                                        'source_nw_y_pixel': -4890728433042171211,
                                        'source_pixel_width': -1594450764902034079,
                                        'source_pixel_height': -7355141598824326941,
                                        'rotation': -8091933894827574757,
                                        'virtual_nw_x_pixel': -360301171,
                                        'virtual_nw_y_pixel': 1691666104,
                                        'virtual_width': -1385340606,
                                        'virtual_height': 1301994800,
                                    },
                            {
                                        'source_monitor': 122389,
                                        'source_nw_x_pixel': -2145520563755093570,
                                        'source_nw_y_pixel': -2994710406260772159,
                                        'source_pixel_width': -4405425235652969603,
                                        'source_pixel_height': -7806066768853299359,
                                        'rotation': -4526682706877606662,
                                        'virtual_nw_x_pixel': 590343002,
                                        'virtual_nw_y_pixel': 1810661868,
                                        'virtual_width': -656732545,
                                        'virtual_height': -1192286613,
                                    },
                            {
                                        'source_monitor': 9122307,
                                        'source_nw_x_pixel': -5115902389060473460,
                                        'source_nw_y_pixel': -5764161598832852263,
                                        'source_pixel_width': -1180607983642677540,
                                        'source_pixel_height': -3568529552512742439,
                                        'rotation': -7160699544514197531,
                                        'virtual_nw_x_pixel': 1920672365,
                                        'virtual_nw_y_pixel': 267214261,
                                        'virtual_width': 254487285,
                                        'virtual_height': 1300742843,
                                    },
                            {
                                        'source_monitor': 617976,
                                        'source_nw_x_pixel': -4036595001310524664,
                                        'source_nw_y_pixel': -7737648798081747178,
                                        'source_pixel_width': -4721881305887048059,
                                        'source_pixel_height': -6172847630415305924,
                                        'rotation': -6568967874720313579,
                                        'virtual_nw_x_pixel': 1717609517,
                                        'virtual_nw_y_pixel': 1942653333,
                                        'virtual_width': 837519334,
                                        'virtual_height': -431055114,
                                    },
                        ],
                },
                {
                    'description': 'ÊУVÄӴ%ʺʏ*ˇϝʏɕЩЄҒ\x85ũƄǬ\x96ŲȑĪџѹҔGǔ˲',
                    'monitors': [
                            {
                                        'identifier': 8023852,
                                        'width': 4968193104108948153,
                                        'height': 2055185616568779210,
                                    },
                            {
                                        'identifier': 2299747,
                                        'width': -1061861881922374007,
                                        'height': 3190573799077722827,
                                    },
                            {
                                        'identifier': 9395480,
                                        'width': -6579014913837914164,
                                        'height': -1212042500725048042,
                                    },
                            {
                                        'identifier': 3311832,
                                        'width': 7135785266638927945,
                                        'height': 7922291851170227283,
                                    },
                            {
                                        'identifier': 6622922,
                                        'width': 8562444713924961779,
                                        'height': 7146918778949828371,
                                    },
                            {
                                        'identifier': 4308840,
                                        'width': -2974002582823319242,
                                        'height': 2737836816643977567,
                                    },
                            {
                                        'identifier': 7787718,
                                        'width': -8492564197139496111,
                                        'height': 8584478869532470851,
                                    },
                            {
                                        'identifier': 1697647,
                                        'width': 2358303919591560938,
                                        'height': -3675121165929558929,
                                    },
                            {
                                        'identifier': 567530,
                                        'width': -5565360552911357358,
                                        'height': -379920865210834673,
                                    },
                            {
                                        'identifier': 7753060,
                                        'width': -4250811609761131005,
                                        'height': -8699874720050228935,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8530270,
                                        'source_nw_x_pixel': -3253732745557211538,
                                        'source_nw_y_pixel': -8817673891669917796,
                                        'source_pixel_width': -1548143358247698559,
                                        'source_pixel_height': -5403718100707225164,
                                        'rotation': -5824077792181057659,
                                        'virtual_nw_x_pixel': 1861300974,
                                        'virtual_nw_y_pixel': 895303195,
                                        'virtual_width': 356001602,
                                        'virtual_height': -751642005,
                                    },
                            {
                                        'source_monitor': 2857951,
                                        'source_nw_x_pixel': -3259889349039813865,
                                        'source_nw_y_pixel': -6432768579122992843,
                                        'source_pixel_width': -4555654755314691895,
                                        'source_pixel_height': -268933553525933954,
                                        'rotation': -8713839860387246741,
                                        'virtual_nw_x_pixel': -883690191,
                                        'virtual_nw_y_pixel': -343391981,
                                        'virtual_width': -1425494579,
                                        'virtual_height': -1852703626,
                                    },
                            {
                                        'source_monitor': 4871513,
                                        'source_nw_x_pixel': -7214970565959468182,
                                        'source_nw_y_pixel': -4549382209392008762,
                                        'source_pixel_width': -557601266749170239,
                                        'source_pixel_height': -3411045890574384711,
                                        'rotation': -4948851309158319098,
                                        'virtual_nw_x_pixel': 1387748058,
                                        'virtual_nw_y_pixel': -1164526980,
                                        'virtual_width': 651965453,
                                        'virtual_height': -1691033867,
                                    },
                            {
                                        'source_monitor': 2232240,
                                        'source_nw_x_pixel': -8962698238847719771,
                                        'source_nw_y_pixel': -8283516937881916690,
                                        'source_pixel_width': -176249509824517630,
                                        'source_pixel_height': -7749058837364256732,
                                        'rotation': -669152361614251891,
                                        'virtual_nw_x_pixel': -752479931,
                                        'virtual_nw_y_pixel': -1429225418,
                                        'virtual_width': -1169980702,
                                        'virtual_height': -583133886,
                                    },
                            {
                                        'source_monitor': 2744436,
                                        'source_nw_x_pixel': -3046458057568981451,
                                        'source_nw_y_pixel': -4633365093107862867,
                                        'source_pixel_width': -2345295422497570505,
                                        'source_pixel_height': -4061363844076526631,
                                        'rotation': -3060645482522293563,
                                        'virtual_nw_x_pixel': -700199869,
                                        'virtual_nw_y_pixel': 1792487115,
                                        'virtual_width': 73960141,
                                        'virtual_height': -944205210,
                                    },
                            {
                                        'source_monitor': 2105219,
                                        'source_nw_x_pixel': -2367613071108651133,
                                        'source_nw_y_pixel': -1871049484754555167,
                                        'source_pixel_width': -7158467232961913353,
                                        'source_pixel_height': -2864621714906107943,
                                        'rotation': -6815660943717841109,
                                        'virtual_nw_x_pixel': 1283586248,
                                        'virtual_nw_y_pixel': -1955515570,
                                        'virtual_width': 207283772,
                                        'virtual_height': -146215031,
                                    },
                            {
                                        'source_monitor': 3497672,
                                        'source_nw_x_pixel': -6549968300199977731,
                                        'source_nw_y_pixel': -3198527244050345914,
                                        'source_pixel_width': -161090232835870463,
                                        'source_pixel_height': -5003290293722864862,
                                        'rotation': -8200845648470475154,
                                        'virtual_nw_x_pixel': 1222623572,
                                        'virtual_nw_y_pixel': 170991786,
                                        'virtual_width': -1948435723,
                                        'virtual_height': 928092921,
                                    },
                            {
                                        'source_monitor': 2811900,
                                        'source_nw_x_pixel': -8675229948816994632,
                                        'source_nw_y_pixel': -2214994778265024122,
                                        'source_pixel_width': -47877625653305117,
                                        'source_pixel_height': -7638932396707067764,
                                        'rotation': -3646741780770095767,
                                        'virtual_nw_x_pixel': -1422806565,
                                        'virtual_nw_y_pixel': 664078315,
                                        'virtual_width': -1093559260,
                                        'virtual_height': 1535992966,
                                    },
                            {
                                        'source_monitor': 3372335,
                                        'source_nw_x_pixel': -2996158727054963031,
                                        'source_nw_y_pixel': -3274009644404777049,
                                        'source_pixel_width': -3891852811469518291,
                                        'source_pixel_height': -6928578982611111248,
                                        'rotation': -4164104892096332256,
                                        'virtual_nw_x_pixel': -1406059740,
                                        'virtual_nw_y_pixel': -410944933,
                                        'virtual_width': 1592711201,
                                        'virtual_height': -115576290,
                                    },
                            {
                                        'source_monitor': 8366844,
                                        'source_nw_x_pixel': -758243598321995913,
                                        'source_nw_y_pixel': -4584955548847487580,
                                        'source_pixel_width': -7531426837024950921,
                                        'source_pixel_height': -772079936202403978,
                                        'rotation': -7532324344157777821,
                                        'virtual_nw_x_pixel': -946048550,
                                        'virtual_nw_y_pixel': 1518009380,
                                        'virtual_width': -1960418698,
                                        'virtual_height': 469091100,
                                    },
                        ],
                },
                {
                    'description': 'ǔüʳŉ˱Dļ˚ѲƎϬÅӮHɀʙʢɯÔϺͱ˹үһɞĵƭ\x9cЦŸ',
                    'monitors': [
                            {
                                        'identifier': 2615894,
                                        'width': -6617832151397205693,
                                        'height': -2383669652129622614,
                                    },
                            {
                                        'identifier': 2221116,
                                        'width': 5576990637918354382,
                                        'height': 4048067564930624191,
                                    },
                            {
                                        'identifier': 7733862,
                                        'width': -2215841409903671196,
                                        'height': 8896056580702132401,
                                    },
                            {
                                        'identifier': -442235,
                                        'width': 8013693638463577700,
                                        'height': 438161310124272285,
                                    },
                            {
                                        'identifier': 3115483,
                                        'width': 2742918102783805339,
                                        'height': -2505521137041587857,
                                    },
                            {
                                        'identifier': 5623397,
                                        'width': 7531060042954965102,
                                        'height': 7221407561168748066,
                                    },
                            {
                                        'identifier': 3049052,
                                        'width': -8353338326680765404,
                                        'height': -8014848238723356416,
                                    },
                            {
                                        'identifier': 3573229,
                                        'width': 7159172257846415418,
                                        'height': -1283584089568066875,
                                    },
                            {
                                        'identifier': 4275022,
                                        'width': 6430488451842972684,
                                        'height': 5590705069756015220,
                                    },
                            {
                                        'identifier': 897958,
                                        'width': 1423512509986607614,
                                        'height': 2170473004114461853,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7595847,
                                        'source_nw_x_pixel': -8235113966193451163,
                                        'source_nw_y_pixel': -8088713191989262514,
                                        'source_pixel_width': -5766180229003645822,
                                        'source_pixel_height': -6867651496661597956,
                                        'rotation': -4647678852523702920,
                                        'virtual_nw_x_pixel': 802227284,
                                        'virtual_nw_y_pixel': 1929569919,
                                        'virtual_width': 4689575,
                                        'virtual_height': 629766458,
                                    },
                            {
                                        'source_monitor': 7458444,
                                        'source_nw_x_pixel': -4078274435265108799,
                                        'source_nw_y_pixel': -7525880819069770017,
                                        'source_pixel_width': -1248611769381945080,
                                        'source_pixel_height': -8296291676333737059,
                                        'rotation': -1413814135466648897,
                                        'virtual_nw_x_pixel': 931447183,
                                        'virtual_nw_y_pixel': -1485876506,
                                        'virtual_width': 1843575137,
                                        'virtual_height': -109134637,
                                    },
                            {
                                        'source_monitor': 2107974,
                                        'source_nw_x_pixel': -6317184274500436277,
                                        'source_nw_y_pixel': -2994360892828858095,
                                        'source_pixel_width': -1381945218508836405,
                                        'source_pixel_height': -5706414695780128155,
                                        'rotation': -1566376007312975095,
                                        'virtual_nw_x_pixel': -962661005,
                                        'virtual_nw_y_pixel': 1626044794,
                                        'virtual_width': -322387140,
                                        'virtual_height': -371292173,
                                    },
                            {
                                        'source_monitor': 8903705,
                                        'source_nw_x_pixel': -8227121605027571861,
                                        'source_nw_y_pixel': -7556569893748604080,
                                        'source_pixel_width': -838381621807602550,
                                        'source_pixel_height': -3917051758418290721,
                                        'rotation': -6929434259839941235,
                                        'virtual_nw_x_pixel': 929046433,
                                        'virtual_nw_y_pixel': 130721249,
                                        'virtual_width': 449016642,
                                        'virtual_height': -507099747,
                                    },
                            {
                                        'source_monitor': 4938862,
                                        'source_nw_x_pixel': -2376425669507596195,
                                        'source_nw_y_pixel': -6566698008464563363,
                                        'source_pixel_width': -4313861110025842574,
                                        'source_pixel_height': -4415459843540714467,
                                        'rotation': -7841670476107789938,
                                        'virtual_nw_x_pixel': -1757818222,
                                        'virtual_nw_y_pixel': -556919891,
                                        'virtual_width': 1052739015,
                                        'virtual_height': 426744906,
                                    },
                            {
                                        'source_monitor': 2927747,
                                        'source_nw_x_pixel': -1107860592421306240,
                                        'source_nw_y_pixel': -7131667951320062238,
                                        'source_pixel_width': -8188034327631851660,
                                        'source_pixel_height': -6785903380080241939,
                                        'rotation': -520122596404190539,
                                        'virtual_nw_x_pixel': -862629991,
                                        'virtual_nw_y_pixel': -1777058607,
                                        'virtual_width': 1248205087,
                                        'virtual_height': 693241296,
                                    },
                            {
                                        'source_monitor': 4659203,
                                        'source_nw_x_pixel': -3143206884715045576,
                                        'source_nw_y_pixel': -5412828042202201852,
                                        'source_pixel_width': -2096245934927345221,
                                        'source_pixel_height': -8134442147121849830,
                                        'rotation': -956860356417472704,
                                        'virtual_nw_x_pixel': -1649195661,
                                        'virtual_nw_y_pixel': 612901123,
                                        'virtual_width': -637918608,
                                        'virtual_height': -663572168,
                                    },
                            {
                                        'source_monitor': 2297136,
                                        'source_nw_x_pixel': -6748724542315983701,
                                        'source_nw_y_pixel': -7169831864961868069,
                                        'source_pixel_width': -299336475073155881,
                                        'source_pixel_height': -6609752852832748265,
                                        'rotation': -1960755295126237926,
                                        'virtual_nw_x_pixel': -1135145647,
                                        'virtual_nw_y_pixel': -807318996,
                                        'virtual_width': 346955481,
                                        'virtual_height': -123722432,
                                    },
                            {
                                        'source_monitor': -424162,
                                        'source_nw_x_pixel': -1929225113775581324,
                                        'source_nw_y_pixel': -6127064459850859341,
                                        'source_pixel_width': -4481218911053218505,
                                        'source_pixel_height': -8338792670820025889,
                                        'rotation': -6710609253079919338,
                                        'virtual_nw_x_pixel': 224360207,
                                        'virtual_nw_y_pixel': 1252603783,
                                        'virtual_width': 438786229,
                                        'virtual_height': -54695461,
                                    },
                            {
                                        'source_monitor': 6348343,
                                        'source_nw_x_pixel': -7863439497951210462,
                                        'source_nw_y_pixel': -8061618670121175568,
                                        'source_pixel_width': -6487997861379675070,
                                        'source_pixel_height': -6519637094920420760,
                                        'rotation': -8827532858945445219,
                                        'virtual_nw_x_pixel': -437001288,
                                        'virtual_nw_y_pixel': -1668007933,
                                        'virtual_width': -755063780,
                                        'virtual_height': -1413250571,
                                    },
                        ],
                },
                {
                    'description': 'ӸȄӺǰˀǶҲϜþʭǎȟǝşԄ=ǍàÏɂrG¤гL\u0383ӭˎͺũ',
                    'monitors': [
                            {
                                        'identifier': 7924612,
                                        'width': 5687795539873184943,
                                        'height': 3528248735756302391,
                                    },
                            {
                                        'identifier': -732642,
                                        'width': -5170685510395137859,
                                        'height': 2239071504485608633,
                                    },
                            {
                                        'identifier': 8823982,
                                        'width': 4710598864889494270,
                                        'height': 6426559383473922808,
                                    },
                            {
                                        'identifier': 3932777,
                                        'width': 2924929784461461965,
                                        'height': -8026768346823374074,
                                    },
                            {
                                        'identifier': 1734253,
                                        'width': -286261758599088228,
                                        'height': -6148752844516566484,
                                    },
                            {
                                        'identifier': 6061544,
                                        'width': 5348807254875422392,
                                        'height': 9044131280558318180,
                                    },
                            {
                                        'identifier': 3169297,
                                        'width': -5454076286401185040,
                                        'height': 4960619813245634773,
                                    },
                            {
                                        'identifier': 3691616,
                                        'width': 4182276949093391791,
                                        'height': -3671308974181872272,
                                    },
                            {
                                        'identifier': 9461505,
                                        'width': 5738578498210673077,
                                        'height': 5923472412983531154,
                                    },
                            {
                                        'identifier': 2206191,
                                        'width': 7402178771032774933,
                                        'height': -4540268071791293325,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2196451,
                                        'source_nw_x_pixel': -5398891031328776371,
                                        'source_nw_y_pixel': -46149957618256399,
                                        'source_pixel_width': -1499163214986766759,
                                        'source_pixel_height': -398970208302963495,
                                        'rotation': -4560523541801240716,
                                        'virtual_nw_x_pixel': -1174602582,
                                        'virtual_nw_y_pixel': 1631095540,
                                        'virtual_width': 1876322766,
                                        'virtual_height': 1255045130,
                                    },
                            {
                                        'source_monitor': 8806573,
                                        'source_nw_x_pixel': -4878554366706972759,
                                        'source_nw_y_pixel': -6430688299542978040,
                                        'source_pixel_width': -5555721793030440233,
                                        'source_pixel_height': -533776731905616126,
                                        'rotation': -3759600315080452820,
                                        'virtual_nw_x_pixel': -725756575,
                                        'virtual_nw_y_pixel': -470498893,
                                        'virtual_width': 603027140,
                                        'virtual_height': -221583963,
                                    },
                            {
                                        'source_monitor': 5882816,
                                        'source_nw_x_pixel': -4312733414299190538,
                                        'source_nw_y_pixel': -1702847360459152576,
                                        'source_pixel_width': -2312596073287724219,
                                        'source_pixel_height': -993494263574635781,
                                        'rotation': -2335882663267122016,
                                        'virtual_nw_x_pixel': 851267302,
                                        'virtual_nw_y_pixel': -455023017,
                                        'virtual_width': 1881164204,
                                        'virtual_height': -1940386848,
                                    },
                            {
                                        'source_monitor': 8080507,
                                        'source_nw_x_pixel': -7183271774357841013,
                                        'source_nw_y_pixel': -8981470153276758016,
                                        'source_pixel_width': -6799949799511121325,
                                        'source_pixel_height': -2237741803279597374,
                                        'rotation': -7076556399713585013,
                                        'virtual_nw_x_pixel': -344593248,
                                        'virtual_nw_y_pixel': 957748369,
                                        'virtual_width': 1238378958,
                                        'virtual_height': 1070806285,
                                    },
                            {
                                        'source_monitor': 1728253,
                                        'source_nw_x_pixel': -5513661562858136177,
                                        'source_nw_y_pixel': -356424631660056113,
                                        'source_pixel_width': -7464376870574480589,
                                        'source_pixel_height': -3237928678600715150,
                                        'rotation': -329820863575806500,
                                        'virtual_nw_x_pixel': 666423165,
                                        'virtual_nw_y_pixel': 1408227418,
                                        'virtual_width': -393018792,
                                        'virtual_height': -1499187987,
                                    },
                            {
                                        'source_monitor': 7723667,
                                        'source_nw_x_pixel': -8465171418835563105,
                                        'source_nw_y_pixel': -5795847892053696849,
                                        'source_pixel_width': -2358466757066517167,
                                        'source_pixel_height': -2414116394468630314,
                                        'rotation': -4322936304322623662,
                                        'virtual_nw_x_pixel': -1770083772,
                                        'virtual_nw_y_pixel': 688938531,
                                        'virtual_width': -1172188640,
                                        'virtual_height': 425694526,
                                    },
                            {
                                        'source_monitor': 673967,
                                        'source_nw_x_pixel': -4186940759067121046,
                                        'source_nw_y_pixel': -6393285371203907798,
                                        'source_pixel_width': -6116835386123403290,
                                        'source_pixel_height': -640219369495024696,
                                        'rotation': -4064009002504876675,
                                        'virtual_nw_x_pixel': 1203189957,
                                        'virtual_nw_y_pixel': 1079663904,
                                        'virtual_width': -1347251507,
                                        'virtual_height': 1919117214,
                                    },
                            {
                                        'source_monitor': 7770050,
                                        'source_nw_x_pixel': -4322250966451677386,
                                        'source_nw_y_pixel': -1865458832849492868,
                                        'source_pixel_width': -4199706975110656932,
                                        'source_pixel_height': -6151718937193757263,
                                        'rotation': -5324364323816950376,
                                        'virtual_nw_x_pixel': 1432112899,
                                        'virtual_nw_y_pixel': 1024564394,
                                        'virtual_width': 1895193193,
                                        'virtual_height': -1665253524,
                                    },
                            {
                                        'source_monitor': 4905042,
                                        'source_nw_x_pixel': -4404956720222622551,
                                        'source_nw_y_pixel': -3382785868400250373,
                                        'source_pixel_width': -4568732508267374464,
                                        'source_pixel_height': -5680326651788346246,
                                        'rotation': -6665134408968302300,
                                        'virtual_nw_x_pixel': -672567986,
                                        'virtual_nw_y_pixel': -971758007,
                                        'virtual_width': 831408870,
                                        'virtual_height': -854541576,
                                    },
                            {
                                        'source_monitor': 7725085,
                                        'source_nw_x_pixel': -5067289969971645275,
                                        'source_nw_y_pixel': -4197413259709913583,
                                        'source_pixel_width': -5202461276808722877,
                                        'source_pixel_height': -9159827658398035488,
                                        'rotation': -3897056371642131579,
                                        'virtual_nw_x_pixel': 1378676833,
                                        'virtual_nw_y_pixel': -1969600982,
                                        'virtual_width': 1658939338,
                                        'virtual_height': -928898218,
                                    },
                        ],
                },
                {
                    'description': 'ɩŜ\x81ˌѭ\x9dƴ\x9bͼʖɪąˁ˜\x80ǬÕϯŔf"ɁǞѱҚƓ\x9eɺЁӫ',
                    'monitors': [
                            {
                                        'identifier': 4622996,
                                        'width': 1568919546302983237,
                                        'height': 3084370135311793164,
                                    },
                            {
                                        'identifier': -891970,
                                        'width': -638898493058669370,
                                        'height': 5656781063717441371,
                                    },
                            {
                                        'identifier': 8187703,
                                        'width': 1413606404339678591,
                                        'height': -306152150380172029,
                                    },
                            {
                                        'identifier': 9751077,
                                        'width': -6035530237115614488,
                                        'height': -24209511153395870,
                                    },
                            {
                                        'identifier': 6859878,
                                        'width': 3515482081316605876,
                                        'height': 6359379176551334775,
                                    },
                            {
                                        'identifier': 1278360,
                                        'width': 7261909438236621255,
                                        'height': 8314631418750833906,
                                    },
                            {
                                        'identifier': 5103187,
                                        'width': 7113104450957412901,
                                        'height': -2304926702458684573,
                                    },
                            {
                                        'identifier': -469830,
                                        'width': 7324262961479811825,
                                        'height': -4942375635477465842,
                                    },
                            {
                                        'identifier': 1625850,
                                        'width': 4413469411917951728,
                                        'height': 9102345206869804257,
                                    },
                            {
                                        'identifier': 9567988,
                                        'width': 8656904341752173379,
                                        'height': 4840069431283165351,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1760369,
                                        'source_nw_x_pixel': -3169479923519030117,
                                        'source_nw_y_pixel': -1654705941358366454,
                                        'source_pixel_width': -7056916181726499667,
                                        'source_pixel_height': -6022242736684205539,
                                        'rotation': -3860922346462255697,
                                        'virtual_nw_x_pixel': 238621686,
                                        'virtual_nw_y_pixel': 491000462,
                                        'virtual_width': 1273468549,
                                        'virtual_height': 534925747,
                                    },
                            {
                                        'source_monitor': 7640164,
                                        'source_nw_x_pixel': -3057659644771461714,
                                        'source_nw_y_pixel': -564361734043822333,
                                        'source_pixel_width': -7817739096393877727,
                                        'source_pixel_height': -5977997545692977078,
                                        'rotation': -3406628137140774327,
                                        'virtual_nw_x_pixel': 1187489172,
                                        'virtual_nw_y_pixel': -579327501,
                                        'virtual_width': -277278735,
                                        'virtual_height': 1903782937,
                                    },
                            {
                                        'source_monitor': 5586455,
                                        'source_nw_x_pixel': -8615581881707151728,
                                        'source_nw_y_pixel': -4763164136435044209,
                                        'source_pixel_width': -6779018257757762995,
                                        'source_pixel_height': -3848714531173842007,
                                        'rotation': -5456174912516486550,
                                        'virtual_nw_x_pixel': 466237007,
                                        'virtual_nw_y_pixel': -1513325376,
                                        'virtual_width': -29901855,
                                        'virtual_height': 676169884,
                                    },
                            {
                                        'source_monitor': 8394570,
                                        'source_nw_x_pixel': -3280510927835710556,
                                        'source_nw_y_pixel': -6384327146547998146,
                                        'source_pixel_width': -4424032554191012197,
                                        'source_pixel_height': -5979182584860617289,
                                        'rotation': -5726070746118065372,
                                        'virtual_nw_x_pixel': -486025693,
                                        'virtual_nw_y_pixel': 1042752529,
                                        'virtual_width': 908231144,
                                        'virtual_height': 1375562363,
                                    },
                            {
                                        'source_monitor': 8710704,
                                        'source_nw_x_pixel': -4363071976829159253,
                                        'source_nw_y_pixel': -3312395716455192923,
                                        'source_pixel_width': -729205108152878984,
                                        'source_pixel_height': -1636162104780558926,
                                        'rotation': -7305650417414523591,
                                        'virtual_nw_x_pixel': -495730001,
                                        'virtual_nw_y_pixel': -1605977900,
                                        'virtual_width': 1952500480,
                                        'virtual_height': 1195498187,
                                    },
                            {
                                        'source_monitor': 3593681,
                                        'source_nw_x_pixel': -4043665516225997642,
                                        'source_nw_y_pixel': -5065509588344771624,
                                        'source_pixel_width': -7867477885691958925,
                                        'source_pixel_height': -8302398203740722889,
                                        'rotation': -8451890911663464135,
                                        'virtual_nw_x_pixel': -1476532673,
                                        'virtual_nw_y_pixel': -13455245,
                                        'virtual_width': -199630836,
                                        'virtual_height': -1393296942,
                                    },
                            {
                                        'source_monitor': 2949533,
                                        'source_nw_x_pixel': -5950705489568467715,
                                        'source_nw_y_pixel': -9093574647736866173,
                                        'source_pixel_width': -774173714706253331,
                                        'source_pixel_height': -8571630838334033129,
                                        'rotation': -8435816118732004801,
                                        'virtual_nw_x_pixel': -1697634389,
                                        'virtual_nw_y_pixel': -1516127406,
                                        'virtual_width': 620926538,
                                        'virtual_height': 1606780575,
                                    },
                            {
                                        'source_monitor': 7731871,
                                        'source_nw_x_pixel': -1042358270008592083,
                                        'source_nw_y_pixel': -3131937069620685244,
                                        'source_pixel_width': -5634407430720703840,
                                        'source_pixel_height': -6630794689789764638,
                                        'rotation': -708614305706692361,
                                        'virtual_nw_x_pixel': -200553277,
                                        'virtual_nw_y_pixel': -1620474606,
                                        'virtual_width': 1085260524,
                                        'virtual_height': 256559335,
                                    },
                            {
                                        'source_monitor': 8587908,
                                        'source_nw_x_pixel': -6126927453068487384,
                                        'source_nw_y_pixel': -417319486931210936,
                                        'source_pixel_width': -8036510135493084732,
                                        'source_pixel_height': -7774785144697046343,
                                        'rotation': -463275779810549079,
                                        'virtual_nw_x_pixel': -93994495,
                                        'virtual_nw_y_pixel': 716629892,
                                        'virtual_width': -84578858,
                                        'virtual_height': -1018247618,
                                    },
                            {
                                        'source_monitor': 5253884,
                                        'source_nw_x_pixel': -3546667190516367956,
                                        'source_nw_y_pixel': -5002400401949307997,
                                        'source_pixel_width': -8005903704039779946,
                                        'source_pixel_height': -6723880019031450109,
                                        'rotation': -6588745986152066523,
                                        'virtual_nw_x_pixel': 799991353,
                                        'virtual_nw_y_pixel': 841005814,
                                        'virtual_width': 436208659,
                                        'virtual_height': -908582403,
                                    },
                        ],
                },
                {
                    'description': 'ˋǭtƁ˳Θˁ§ÎӋЅΊқŵÏȩǬŚåĆӵ¡ҧьȘӺ¼ҿαһ',
                    'monitors': [
                            {
                                        'identifier': 303194,
                                        'width': -6890684160767317447,
                                        'height': -9165845973387947954,
                                    },
                            {
                                        'identifier': 4025452,
                                        'width': 3089792269106729044,
                                        'height': 8705838857234853282,
                                    },
                            {
                                        'identifier': 9008284,
                                        'width': 8354267790456648652,
                                        'height': -948794573268822232,
                                    },
                            {
                                        'identifier': 2729030,
                                        'width': -5701001455719435063,
                                        'height': 5945639356752717659,
                                    },
                            {
                                        'identifier': 4216636,
                                        'width': 8050582993900047621,
                                        'height': -5526205059209822604,
                                    },
                            {
                                        'identifier': 6317056,
                                        'width': -8784337598668590066,
                                        'height': -2428614544200628616,
                                    },
                            {
                                        'identifier': 63691,
                                        'width': 916653729426971798,
                                        'height': 2879111348991292860,
                                    },
                            {
                                        'identifier': 797717,
                                        'width': -2266820226217142936,
                                        'height': 3500148323313021332,
                                    },
                            {
                                        'identifier': 1092540,
                                        'width': -7848985450523958226,
                                        'height': -316450012473893061,
                                    },
                            {
                                        'identifier': 1852896,
                                        'width': 3628303160687853059,
                                        'height': 3973629561467340448,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3139537,
                                        'source_nw_x_pixel': -4030872442967795397,
                                        'source_nw_y_pixel': -4633592157001272791,
                                        'source_pixel_width': -1074747990943691059,
                                        'source_pixel_height': -5874773691542551001,
                                        'rotation': -340971126185156037,
                                        'virtual_nw_x_pixel': 521247242,
                                        'virtual_nw_y_pixel': 1558842237,
                                        'virtual_width': -1253954196,
                                        'virtual_height': -1510408251,
                                    },
                            {
                                        'source_monitor': 2408328,
                                        'source_nw_x_pixel': -1171411684293934759,
                                        'source_nw_y_pixel': -202571562833563955,
                                        'source_pixel_width': -352563123867158615,
                                        'source_pixel_height': -4443031013249668804,
                                        'rotation': -8962686932201770411,
                                        'virtual_nw_x_pixel': 868229100,
                                        'virtual_nw_y_pixel': -1450528555,
                                        'virtual_width': 885652843,
                                        'virtual_height': 842224810,
                                    },
                            {
                                        'source_monitor': 4672769,
                                        'source_nw_x_pixel': -7622388033256557287,
                                        'source_nw_y_pixel': -4372037912905083269,
                                        'source_pixel_width': -7627310377257502184,
                                        'source_pixel_height': -121360196498111923,
                                        'rotation': -7257841506129838006,
                                        'virtual_nw_x_pixel': -419302918,
                                        'virtual_nw_y_pixel': -1310555015,
                                        'virtual_width': 456730454,
                                        'virtual_height': 1140174636,
                                    },
                            {
                                        'source_monitor': 1370346,
                                        'source_nw_x_pixel': -4369139649302294102,
                                        'source_nw_y_pixel': -8198634429965635943,
                                        'source_pixel_width': -714643066458764437,
                                        'source_pixel_height': -7307489603129651593,
                                        'rotation': -82549400998729438,
                                        'virtual_nw_x_pixel': 846776271,
                                        'virtual_nw_y_pixel': 1566065928,
                                        'virtual_width': -1376197012,
                                        'virtual_height': 920826579,
                                    },
                            {
                                        'source_monitor': -2294,
                                        'source_nw_x_pixel': -7964384808587952960,
                                        'source_nw_y_pixel': -5275855156748562994,
                                        'source_pixel_width': -3294517612417191912,
                                        'source_pixel_height': -73527867434741270,
                                        'rotation': -3850637984374179457,
                                        'virtual_nw_x_pixel': -1544640363,
                                        'virtual_nw_y_pixel': -77945639,
                                        'virtual_width': -1325945732,
                                        'virtual_height': -284170353,
                                    },
                            {
                                        'source_monitor': 8781911,
                                        'source_nw_x_pixel': -8665172223409750952,
                                        'source_nw_y_pixel': -2255991928714179934,
                                        'source_pixel_width': -6329096410810375449,
                                        'source_pixel_height': -9066641373728262646,
                                        'rotation': -5996922395001768811,
                                        'virtual_nw_x_pixel': -1892459497,
                                        'virtual_nw_y_pixel': -176660897,
                                        'virtual_width': 492365276,
                                        'virtual_height': 136634077,
                                    },
                            {
                                        'source_monitor': 5685963,
                                        'source_nw_x_pixel': -60404644623090978,
                                        'source_nw_y_pixel': -1905318764801426010,
                                        'source_pixel_width': -6970303245201701076,
                                        'source_pixel_height': -2527754551155380311,
                                        'rotation': -8914945391915966821,
                                        'virtual_nw_x_pixel': 252510853,
                                        'virtual_nw_y_pixel': 1829940746,
                                        'virtual_width': 1672682661,
                                        'virtual_height': 622395529,
                                    },
                            {
                                        'source_monitor': 6111376,
                                        'source_nw_x_pixel': -5688423361544741556,
                                        'source_nw_y_pixel': -4782260465129649108,
                                        'source_pixel_width': -1185223411071329971,
                                        'source_pixel_height': -5110252304586536053,
                                        'rotation': -6984748217967668292,
                                        'virtual_nw_x_pixel': 1135419517,
                                        'virtual_nw_y_pixel': 1521833237,
                                        'virtual_width': -1475952172,
                                        'virtual_height': -1853540222,
                                    },
                            {
                                        'source_monitor': 224037,
                                        'source_nw_x_pixel': -6762702130731378,
                                        'source_nw_y_pixel': -3731645616827731905,
                                        'source_pixel_width': -7928413306242990878,
                                        'source_pixel_height': -708677683509241800,
                                        'rotation': -5883255137889096815,
                                        'virtual_nw_x_pixel': 1763473094,
                                        'virtual_nw_y_pixel': -398986093,
                                        'virtual_width': -121665421,
                                        'virtual_height': -1181906045,
                                    },
                            {
                                        'source_monitor': -795552,
                                        'source_nw_x_pixel': -3239993507714543661,
                                        'source_nw_y_pixel': -7050685092382745536,
                                        'source_pixel_width': -976748544034467426,
                                        'source_pixel_height': -8689420594655634183,
                                        'rotation': -8936857653041532616,
                                        'virtual_nw_x_pixel': 24305534,
                                        'virtual_nw_y_pixel': 1777196265,
                                        'virtual_width': -744212514,
                                        'virtual_height': 1306776655,
                                    },
                        ],
                },
                {
                    'description': '\x96¢ɠцȘΑ ;ӼŭҞʯ7ťÁӰҺɘАɢĔäȒţĩ\u0380ǏԌλы',
                    'monitors': [
                            {
                                        'identifier': 4911497,
                                        'width': -6491180455951323952,
                                        'height': -9089773314994043231,
                                    },
                            {
                                        'identifier': 507541,
                                        'width': -2727743650801676008,
                                        'height': 1933416955638260988,
                                    },
                            {
                                        'identifier': 5733816,
                                        'width': -2023601928749256584,
                                        'height': 7734254366622757975,
                                    },
                            {
                                        'identifier': 5572348,
                                        'width': -46157622759041160,
                                        'height': 688483990770748137,
                                    },
                            {
                                        'identifier': 5873654,
                                        'width': -1770349348169107006,
                                        'height': 2480755652159561080,
                                    },
                            {
                                        'identifier': 2754935,
                                        'width': 5261244009788468997,
                                        'height': -1991634511917326279,
                                    },
                            {
                                        'identifier': -783187,
                                        'width': 7462264300019605247,
                                        'height': -4402313592542616262,
                                    },
                            {
                                        'identifier': 5000858,
                                        'width': -6648931303247091973,
                                        'height': 6457379235876442989,
                                    },
                            {
                                        'identifier': 682540,
                                        'width': 3304150547204736905,
                                        'height': 2706221571111437078,
                                    },
                            {
                                        'identifier': 4008913,
                                        'width': 2538859621788907891,
                                        'height': 7208300257992351854,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5520053,
                                        'source_nw_x_pixel': -1207262853265374090,
                                        'source_nw_y_pixel': -6634971425648319274,
                                        'source_pixel_width': -1066916477362542911,
                                        'source_pixel_height': -7861101714924128277,
                                        'rotation': -6427998855476772542,
                                        'virtual_nw_x_pixel': 759593964,
                                        'virtual_nw_y_pixel': -911851929,
                                        'virtual_width': 1392640414,
                                        'virtual_height': 1411920467,
                                    },
                            {
                                        'source_monitor': 3298822,
                                        'source_nw_x_pixel': -8086888721800570776,
                                        'source_nw_y_pixel': -4469649562706755312,
                                        'source_pixel_width': -7479962415211172518,
                                        'source_pixel_height': -6965432808996659421,
                                        'rotation': -4244959423608784984,
                                        'virtual_nw_x_pixel': -131315540,
                                        'virtual_nw_y_pixel': -776678581,
                                        'virtual_width': -137876145,
                                        'virtual_height': 1959881379,
                                    },
                            {
                                        'source_monitor': 7598509,
                                        'source_nw_x_pixel': -2357961121340542271,
                                        'source_nw_y_pixel': -4414794927904810273,
                                        'source_pixel_width': -4834926577237548188,
                                        'source_pixel_height': -5568986583667240762,
                                        'rotation': -1215794216044385964,
                                        'virtual_nw_x_pixel': -1212575714,
                                        'virtual_nw_y_pixel': -256480026,
                                        'virtual_width': -1709802594,
                                        'virtual_height': -264461024,
                                    },
                            {
                                        'source_monitor': 5000674,
                                        'source_nw_x_pixel': -9127994675659947858,
                                        'source_nw_y_pixel': -3344192189326316582,
                                        'source_pixel_width': -493660232794742286,
                                        'source_pixel_height': -2879314897969075844,
                                        'rotation': -897780394402498255,
                                        'virtual_nw_x_pixel': -695355553,
                                        'virtual_nw_y_pixel': -31309570,
                                        'virtual_width': 1835243055,
                                        'virtual_height': 708416444,
                                    },
                            {
                                        'source_monitor': 2565428,
                                        'source_nw_x_pixel': -6064307819860505967,
                                        'source_nw_y_pixel': -6316738132097227393,
                                        'source_pixel_width': -2208097089236717252,
                                        'source_pixel_height': -8337605445603194417,
                                        'rotation': -6641556320214680537,
                                        'virtual_nw_x_pixel': -284725010,
                                        'virtual_nw_y_pixel': 357817541,
                                        'virtual_width': -899196381,
                                        'virtual_height': -1432175287,
                                    },
                            {
                                        'source_monitor': 5783500,
                                        'source_nw_x_pixel': -1131348840225119972,
                                        'source_nw_y_pixel': -4716268129824470282,
                                        'source_pixel_width': -876989679397937286,
                                        'source_pixel_height': -2222406616209752855,
                                        'rotation': -4880179705577100523,
                                        'virtual_nw_x_pixel': -1896530576,
                                        'virtual_nw_y_pixel': -1625093592,
                                        'virtual_width': 1072845925,
                                        'virtual_height': -231484197,
                                    },
                            {
                                        'source_monitor': 1959824,
                                        'source_nw_x_pixel': -7051199831153909101,
                                        'source_nw_y_pixel': -3388974597349187938,
                                        'source_pixel_width': -6210920517425332853,
                                        'source_pixel_height': -4380692974837688054,
                                        'rotation': -322928784803909293,
                                        'virtual_nw_x_pixel': 63781933,
                                        'virtual_nw_y_pixel': -422567430,
                                        'virtual_width': -561717278,
                                        'virtual_height': 1036629484,
                                    },
                            {
                                        'source_monitor': -231119,
                                        'source_nw_x_pixel': -7225742954216624701,
                                        'source_nw_y_pixel': -1163469506401737510,
                                        'source_pixel_width': -5474126024582124778,
                                        'source_pixel_height': -3427225969394205039,
                                        'rotation': -3657047722208932462,
                                        'virtual_nw_x_pixel': -1946767615,
                                        'virtual_nw_y_pixel': 1078071000,
                                        'virtual_width': -1705797807,
                                        'virtual_height': -1404199955,
                                    },
                            {
                                        'source_monitor': 961801,
                                        'source_nw_x_pixel': -8379970244480313258,
                                        'source_nw_y_pixel': -3292599285014017431,
                                        'source_pixel_width': -4407249130833813606,
                                        'source_pixel_height': -5103958818066033277,
                                        'rotation': -1357511960853907942,
                                        'virtual_nw_x_pixel': -223288488,
                                        'virtual_nw_y_pixel': 1238027208,
                                        'virtual_width': 1280568878,
                                        'virtual_height': 1524321587,
                                    },
                            {
                                        'source_monitor': 7404930,
                                        'source_nw_x_pixel': -2037190654499225667,
                                        'source_nw_y_pixel': -237834967955421061,
                                        'source_pixel_width': -2654253163620727169,
                                        'source_pixel_height': -8187834983231727794,
                                        'rotation': -2448164733720411060,
                                        'virtual_nw_x_pixel': 410891130,
                                        'virtual_nw_y_pixel': 1917735411,
                                        'virtual_width': 1067379321,
                                        'virtual_height': 413370546,
                                    },
                        ],
                },
                {
                    'description': 'PĊə¸Ƣ7ѡÆΑsȒԆĆɹϐƧ*Åċӑκɗ<ƘÍǤˮЇɮЎ',
                    'monitors': [
                            {
                                        'identifier': -986451,
                                        'width': 353153938682601704,
                                        'height': -842947601682036321,
                                    },
                            {
                                        'identifier': -611120,
                                        'width': 5569694400417583683,
                                        'height': 3435625705484943969,
                                    },
                            {
                                        'identifier': -948337,
                                        'width': 3899359319613413719,
                                        'height': -2575968171092680886,
                                    },
                            {
                                        'identifier': 2440697,
                                        'width': -6473474475975069676,
                                        'height': 2461658609170387641,
                                    },
                            {
                                        'identifier': 368098,
                                        'width': 1572118497475988555,
                                        'height': 2155384456989167517,
                                    },
                            {
                                        'identifier': 9938983,
                                        'width': -4717035567451782978,
                                        'height': 5569047089996183352,
                                    },
                            {
                                        'identifier': 103300,
                                        'width': 6833826023932549314,
                                        'height': 1554602075203829276,
                                    },
                            {
                                        'identifier': 4109305,
                                        'width': 4341423657384388654,
                                        'height': 7079341092936819342,
                                    },
                            {
                                        'identifier': -994740,
                                        'width': 7070993843263086608,
                                        'height': -666804909597082450,
                                    },
                            {
                                        'identifier': 3564623,
                                        'width': 3910271376688109724,
                                        'height': -1255099286455106129,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9024899,
                                        'source_nw_x_pixel': -7217076924076060901,
                                        'source_nw_y_pixel': -9097396231463011621,
                                        'source_pixel_width': -8133235109740332168,
                                        'source_pixel_height': -8865273926161224875,
                                        'rotation': -8875907667509010355,
                                        'virtual_nw_x_pixel': 955406891,
                                        'virtual_nw_y_pixel': 418323946,
                                        'virtual_width': -500156454,
                                        'virtual_height': -146726403,
                                    },
                            {
                                        'source_monitor': 4362592,
                                        'source_nw_x_pixel': -151279578122080209,
                                        'source_nw_y_pixel': -400346214925219575,
                                        'source_pixel_width': -2387119014160622938,
                                        'source_pixel_height': -1631997807362255829,
                                        'rotation': -4448114564266855598,
                                        'virtual_nw_x_pixel': -1247398592,
                                        'virtual_nw_y_pixel': 1741027747,
                                        'virtual_width': 3675794,
                                        'virtual_height': -611959302,
                                    },
                            {
                                        'source_monitor': 3587125,
                                        'source_nw_x_pixel': -7476992106541794074,
                                        'source_nw_y_pixel': -2068217385626037353,
                                        'source_pixel_width': -6782504232855623285,
                                        'source_pixel_height': -8315929226041331728,
                                        'rotation': -3288374776934149074,
                                        'virtual_nw_x_pixel': 1706248315,
                                        'virtual_nw_y_pixel': 1764853907,
                                        'virtual_width': 1396995289,
                                        'virtual_height': -133464662,
                                    },
                            {
                                        'source_monitor': 6906692,
                                        'source_nw_x_pixel': -5628190378029225336,
                                        'source_nw_y_pixel': -2932491976937233451,
                                        'source_pixel_width': -3854537214554830673,
                                        'source_pixel_height': -8150538335803793420,
                                        'rotation': -3584422327826592773,
                                        'virtual_nw_x_pixel': -1077513682,
                                        'virtual_nw_y_pixel': 1962722109,
                                        'virtual_width': 658687823,
                                        'virtual_height': 1470647186,
                                    },
                            {
                                        'source_monitor': 813996,
                                        'source_nw_x_pixel': -2616568542189023213,
                                        'source_nw_y_pixel': -6475284126665404074,
                                        'source_pixel_width': -5804902622861367881,
                                        'source_pixel_height': -1671098193645224508,
                                        'rotation': -7835592060387847447,
                                        'virtual_nw_x_pixel': -728521366,
                                        'virtual_nw_y_pixel': 325292625,
                                        'virtual_width': 538950152,
                                        'virtual_height': 1231001807,
                                    },
                            {
                                        'source_monitor': 3713448,
                                        'source_nw_x_pixel': -2810947075549241423,
                                        'source_nw_y_pixel': -3097464443084227489,
                                        'source_pixel_width': -4007168894461923000,
                                        'source_pixel_height': -2701092928414097831,
                                        'rotation': -1133178217285645898,
                                        'virtual_nw_x_pixel': 498029687,
                                        'virtual_nw_y_pixel': -415123000,
                                        'virtual_width': -672264310,
                                        'virtual_height': 1056895214,
                                    },
                            {
                                        'source_monitor': 2838253,
                                        'source_nw_x_pixel': -8999467322645440175,
                                        'source_nw_y_pixel': -7237862553901239942,
                                        'source_pixel_width': -7699701784448368866,
                                        'source_pixel_height': -8075954192720957887,
                                        'rotation': -1012788390406039493,
                                        'virtual_nw_x_pixel': 1404851505,
                                        'virtual_nw_y_pixel': 128302884,
                                        'virtual_width': 886804775,
                                        'virtual_height': 1931758452,
                                    },
                            {
                                        'source_monitor': 8406062,
                                        'source_nw_x_pixel': -6388329409609467030,
                                        'source_nw_y_pixel': -8073753720278804081,
                                        'source_pixel_width': -3401214623000813149,
                                        'source_pixel_height': -7559976106200557493,
                                        'rotation': -27903058564493511,
                                        'virtual_nw_x_pixel': 707581300,
                                        'virtual_nw_y_pixel': 1523318705,
                                        'virtual_width': -47549278,
                                        'virtual_height': 1500035093,
                                    },
                            {
                                        'source_monitor': 2448959,
                                        'source_nw_x_pixel': -2328996508196414919,
                                        'source_nw_y_pixel': -6627652036538793659,
                                        'source_pixel_width': -2139500027166444060,
                                        'source_pixel_height': -1790849772490912366,
                                        'rotation': -4828868942763744935,
                                        'virtual_nw_x_pixel': -401825717,
                                        'virtual_nw_y_pixel': -843303677,
                                        'virtual_width': -910659953,
                                        'virtual_height': -1994231603,
                                    },
                            {
                                        'source_monitor': 9061880,
                                        'source_nw_x_pixel': -9163206919522572601,
                                        'source_nw_y_pixel': -4898579136090893776,
                                        'source_pixel_width': -5491620885735620707,
                                        'source_pixel_height': -793953579563747406,
                                        'rotation': -6473537806179589352,
                                        'virtual_nw_x_pixel': 161506909,
                                        'virtual_nw_y_pixel': -1802920629,
                                        'virtual_width': -713646828,
                                        'virtual_height': 1032593677,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 2898892,

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
            'request_id': 9443546,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 5637243,

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
            '$': 'ɊŚ\u03a2ԎGӝ·ѭÒϸǑǿҧғčƔȥƪȯґƬĵĬӽӰӟƘͻҐǁ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8460976087366391339,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 263175.54706154705,
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
            '$': '20210224:164112.066791:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ȯö±ӽьŸԐѩʸӘϠǰęȎӝǁіèΖѻǺ·˵æӂ˂ŨҮūͳ',
                'ȦŃōǯѹԇЯ\x86ƌÚȌЧυřХɇҷ˳ď ǎҴlĪұǒƳԐĴÀ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                8980867681765922043,
                -8307894474676126834,
                3687082322572612733,
                1520342497480834773,
                -4471911116696098738,
                4004808875983496227,
                8000170776520337245,
                -5263943575645956955,
                1261674541084217032,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                906293.0011453279,
                839725.6537064835,
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
                True,
                True,
                False,
                False,
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
                '20210224:164112.068005:+0000',
                '20210224:164112.068060:+0000',
                '20210224:164112.068069:+0000',
                '20210224:164112.068076:+0000',
                '20210224:164112.068081:+0000',
                '20210224:164112.068087:+0000',
                '20210224:164112.068092:+0000',
                '20210224:164112.068098:+0000',
                '20210224:164112.068104:+0000',
                '20210224:164112.068110:+0000',
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
            'name': 'ώÝɵτĕϊâѠӴҐӷFԨШϕ\x81ͳҥԊӽɬҊӼӈΟϲ',
            'value': {
                '^': 'float',
                '$': 268632.6528797847,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӽ',

            'value': {
                '^': 'float',
                '$': 751077.7923033217,
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
            'catalog': 'γҵѳѳˡiȧʿɞƏėɃԄǕ΅ǃԚкɧӓЉĥŏԌЛ˸Ĕ˵Ѯǡ',
            'message': 'ѻ\x7fǊξŽ˓ĨɞԔйϻCǄʍˏϒǐȊäɰΩ҃\x85ʙϮƒўŢɘĆ',
            'arguments': [
                {
                    'name': 'ȬÜ˯ç˼ɛĄˬ\x9eΪҭǀʃĕáΆŸļӭĞĤxĻˏ϶',
                    'value': {
                            '^': 'int',
                            '$': -3710278106863135952,
                        },
                },
                {
                    'name': 'ɊÜӔюɲĘ˳ĮԤҽΠҴώǧġ˧ƿѼ\x8fŚǐƀѾȴŲϚЁʹԡ˖',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'јХȰȋдϔˑϾɳÂҙʳȑόêЧƃãƐaϖЫҹʛ\x9aʹƒýȈΆ',
                                        'ØΤŴǤ¢ɢӀǄη·ƂǂͶɥ4ӝϨӉ1ǎ7ԏЏȶřыĦÃИȬ',
                                        'ý˴ҮŹˣШӰɋѓѬǞй˓˵ÑÏŭǰӨŎƦˌű-їϒWĝϡí',
                                        'ǽ҇ɓҹ\x8aīбiǝ¤ŗϠѭԤΎ2ŀǕŷѤѮԭϣ\x9eѣХÆʶҗԏ',
                                        'г\x82ѷƟĵàѿĈÜěˡϕɃӀѧɎӺ$ѢĤёӗǐBʕԊ˲ҮƮť',
                                        'ǅȕɮłңҎԈɭ˶\x9aɇVЁЁΧ˓ʻӦƫʿђΦȮҴCΘȌӝѱд',
                                        'ԫˡǥϑ\x82ʗӢŇØĊƺ˂ΌԘȘĂÊ˹ñ¼ƸƱѲІǳϧҡèхȫ',
                                        'ħ\x7f˲ȟĳ˯Ǟļɰ¦˰ϡʶʨɟЎɤȇēÀȩ0ˇÇ˨˗\x84ӛ˧ҝ',
                                        'ɁǀƥȌř\xadƿԛϨǥҝŔҖɫȨηТƺ=ѐºHMĜǢΧȬԮVҸ',
                                        "ę˻'ʰŷĔԂͿãԕǯǍĊģɓΑƫǉѧӲÙӵ\\ėͷÁºԌԔƺ",
                                    ],
                        },
                },
                {
                    'name': '\x93:ƣĹʩϢ1ÄҮƝmΆԨΥþҺӛʻԏͶīòˢŚΦĦʣľǤԘ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210224:164112.064874:+0000',
                        },
                },
                {
                    'name': 'ʢ³ʤӑÿÔƯʯŋʂʡÑçśЉ˛hϜȆщ´ȱшѽƱśι\x96ώ˅',
                    'value': {
                            '^': 'int',
                            '$': 4192073890923536175,
                        },
                },
                {
                    'name': 'ƴuϣіƌϤ\x9dV˲ԍЩйÚ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        1991262658801757647,
                                        -3948665970318709216,
                                        -1463059331248435567,
                                        3486657460841659574,
                                        -498532000281885166,
                                        3620769430871929177,
                                        878052370200989871,
                                        4900882745098859517,
                                        4974603600000400066,
                                        4407969790358759927,
                                    ],
                        },
                },
                {
                    'name': '˼ύqȷͳå\x91%ϜˎͱʨˠɫƃŴ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210224:164112.065414:+0000',
                                        '20210224:164112.065426:+0000',
                                        '20210224:164112.065435:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ʦιΤό\x9eӰΐfõӲΈ\xa0ͰӞβҍњΞ1ͼʃІƑΨΡЏϿ',
                    'value': {
                            '^': 'string',
                            '$': 'ƉԌŅɈϯɦθŖ7ȏ˛Ȉ˸ȗãŝìнԉЦԄʹʫφŞΰ³Ϋȇʋ',
                        },
                },
                {
                    'name': 'ƪǹ\x97ʷӁНд×әɴɖʔљʾӏØƍϬѸ',
                    'value': {
                            '^': 'int',
                            '$': -6899970602821860978,
                        },
                },
                {
                    'name': 'Áș˥ԬҰˌѣԗ¸Ο-\x9eрō\x91ӆƫԮȅǥÚО&ЄЮęѤāȱϣ',
                    'value': {
                            '^': 'int',
                            '$': -4394972447026379439,
                        },
                },
                {
                    'name': '%Ũ\u0383pˊʗҰж҆6ΓǙɖ,љϒӉ\x91ӿĳТʸ\u0379`ΏţŰӪтR',
                    'value': {
                            '^': 'string',
                            '$': 'δŘΊʘŅʐЋʭˠŌʪpϫ;ϩhϰΓˌвԞfŁϴNԨĻɄąш',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'UϷ',

            'message': '\x96',

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
            'identifier': 'ѠȫȄŋкßЃųϚHϊнӊлӍĞǛmüôőӌȉʯÊӎςơҋȻ',
            'categories': [
                'invalid-user-action',
                'network',
                'access-restriction',
                'internal',
                'network',
                'access-restriction',
                'invalid-user-action',
                'network',
                'file',
                'network',
            ],
            'source': 'ĢɮĚǇPΗʺ҃¸ZůĜИѴШȶƾǫôƭҔɅͽƅɗ?҄*Ѹˑ',
            'messages': [
                {
                    'catalog': 'Zȶ\x87ȱîԓ\x9bȵΧȼ/Ӛ΅Ώ\u0382ʶƓё҂˽\x86Ȳ˳ӈɨϮɎ\u0379Ţ\u0383',
                    'message': 'ʓƝӢ×ҼǕćϤǻǜҸ\x88ÀĐh˨īԏКԙɪŧʹ%ίΖωƲɬΖ',
                    'arguments': [
                            {
                                        'name': '˼;ѬâƞӐһҪī\x90ś\x89ҘqϲƼςɸǴʒ©ɀг\u0381ÕĉǇαɊɓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4429842797557602904,
                                                    },
                                    },
                            {
                                        'name': 'ƙrЙԐȍƍҮąǡʤâΚȐȓ\x87ԉȇɏ\x80ԙɱПφЅӼη\u0379\x9b\\',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.033579:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɗìЙ&\x96ɹϭԭȏ÷\u0382ЉĽưӂɻæȚΞ¯ЇşұVĊεÁ\x8fũ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6123771884907486498,
                                                    },
                                    },
                            {
                                        'name': 'υč',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.033832:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʙžЯǈnǸЅϯ;ȵ˻ӫžǦΘ³ū«ˆ˫ϛͼΝзÖԅȎɺȡń',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˀǔąļˡαΔԈªƲάſҁĂÄ\x8bɂΙϯˍѩɑΰΝҖEԝΧɒͿ',
                                                                            'ԃΥɹɴìѪÜɭҚґ\x8dȬ\x9fϟɳƭÕѪξтο°йőԏŻ˄Ǒ¹а',
                                                                            'ҸƧ˲ѝΚĵǝīτӸƬɋϜѰļ#ÆɈźƙ˧ʴҊīɚǡҏá\x81Ð',
                                                                            '\u038dȬʱӨņğɲŔŻМď\x98ʢłͳċϨƾ˭ξǙĹǺŊҤҵŤǴЮǽ',
                                                                            'ͼ\x9bҽɦЮÅjĢԉüO]āōҙʆě÷ɡяʂ˼Ɨ`ΘÀķxҰϣ',
                                                                            'n$ɥǾ˞ÿѸǹ\u0383aσňǇ\x8aљѲİĐ\x95ĺϰʡӏȬǝƦʴӐöƸ',
                                                                            'ҜϯӎʣΦӼԊ˂˶ȅʧӏɉԕ˪Ǿǎŵ`˞Ќɳʳ\u0380mμɐ\u03a2;Ɖ',
                                                                            'ƋЫӀçχ·ŒÐΨƽȘĭ˼Eɩ҈ï\x96Ëdҝ´·˶Я\x84ƕsЬÞ',
                                                                            'ʙʖ\x88ΓΏːќƴ\u03a2ҵȃѕԔƅĤͳŊŃ\x91ӼѸŰӀі˥Pʅѽ.ϩ',
                                                                            'ϼ\x9dӠШΩ\x8fи˷ˋűөΝ5îĮЌ¡ӾĝǒԭѥÉőѭĦľȊБӓ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Đɰѝ´Ʀϯ×ԪιĬϤɡѫЂ\x93ԠϜ\x9dϑȍǏĀvëɕΨ·',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7188439825745130712,
                                                                            2798376055716579304,
                                                                            -6345646806530029342,
                                                                            1371059978068134443,
                                                                            1781218926225302997,
                                                                            1052125613188536446,
                                                                            -6559272310884476792,
                                                                            -185689355444347622,
                                                                            -1320670927206100119,
                                                                            -6477910196480407263,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÎӮѨԅŰϴӢR]ˀĮœӿҼÖРƂ$лȶȟ¬ϐһԑеϘ\u03a21\x7f',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 67306.3425899104,
                                                    },
                                    },
                            {
                                        'name': '\u0381ҒèȐŬШѥт½ďӨÅΨфͶŠҫԓǉ˒³ƞʹæǦϋѤӾѱɮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4729738205309812902,
                                                                            -5140954598783285258,
                                                                            -8409804287742256253,
                                                                            7738601772956396177,
                                                                            -2330271721722166747,
                                                                            7044000481431041852,
                                                                            -4837278023080267948,
                                                                            -8690777394792678124,
                                                                            2035254637783080055,
                                                                            2818025006614708302,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĩůʓаϠũΦͻҝϟǚÊȃχϛƑŠ¿ЭƙǭĘє;ţϤԘŏѶо',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -50220.532493395694,
                                                                            826391.7990171806,
                                                                            635833.9820537941,
                                                                            597412.226473869,
                                                                            640364.0912858844,
                                                                            -44161.884588345645,
                                                                            -93868.74748477875,
                                                                            -62458.28411704084,
                                                                            25860.0853860691,
                                                                            213758.46977043344,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'f҈ѿ\x94ÍЍаśŘɵʔÑӫ×μ˨ɤ˗ƹάkȡVөąиƵһ>Ŏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            814990.1936147779,
                                                                            -24472.76997801941,
                                                                            605737.2288822236,
                                                                            112826.43198663753,
                                                                            232870.8801919747,
                                                                            140020.31466411412,
                                                                            294770.13001467794,
                                                                            80074.45684253471,
                                                                            467344.20102356095,
                                                                            414738.64964376966,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȧБPƱűÜŉӊăĕł˓ƸʕùҝѻϹ¸ӑƨŐɳΨ¾\x96˧ѕεŸ',
                    'message': 'ɚϥȀȼĳ˕ʻΈѩȊ˯ӤδҁŔŃɮČ9ҿeНҎьҒíȺbʅƟ',
                    'arguments': [
                            {
                                        'name': 'ɼǯľѝΒԀϿƜαƞȇƙ×ºƎѠƹĭ\x9bñKҀǈȆͽƇĈɶѝŨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ǅͺȲԝϦѺԄɸγͻыԘȜǅĂɭ\x8eҀɖȕ'ԝʻŵ¬˳ęȃǷЪ",
                                                                            'Ǔ҇ďȨ\x8bϊĦéƠˈ4ŚӞԄˡѓŚҼɯȮɐόҤ¤}ԕ¯ԂàȖ',
                                                                            'p\x92ҖʋӞĳǚҧ§ʜʁ͵θӆΤϠŦϕвԣωƹǭȋğŴϳˡŤó',
                                                                            'ƧѪʬҸɦȱόчС˖ŕËJͲÈ\x9eȕΌƿіlħϨōvǑОǭÅ\u03a2',
                                                                            'ÁǕÚŽâɳӯćԀɞƪɧ¹µҖΪÂԝ\u0383ȇȼǆ˚ҪCʰȻȜϖω',
                                                                            'ԠȱҥΉƧЂɰÞϻďәϦĬпйäѷŭΆȨ3ˌʵŌГнǭDȽŽ',
                                                                            'ŀT˝ÆȡηҾϜвҪȢZӖŹͽҶƋˢɘΕӀɠƢſɠ¼ŘƭUȇ',
                                                                            'ėƍΡȜˮΉʀ;ŶǁΘԥșˡǝ¥ŘɆĠ˺ҬΕƔҨN¯ƄȽʞǊ',
                                                                            'ʫ˅Ϣȴĕƃōȍϱ\x85Кʩ\x84ԨΏɍƐ)úģζ҉\x8cƕBǬǴͲEХ',
                                                                            'ԣϖҵƌȝêŇ҅˻ӃʿČСσԍҖŰķѪǍтϋИÀэŁӉʁĈӕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɵ\xa0ƻçҐυȳɧ6ȊѲƭЇΎˏҿѵӽ\x9d',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6681335800849349522,
                                                    },
                                    },
                            {
                                        'name': 'ѮƼϸģѪğĊӓĶԃŬͷ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ͳ¹ϐ˺˟ªѠʡϐӿӴӌŰʴÊϟ˒ʐσÿǝҚ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 357278.1583741047,
                                                    },
                                    },
                            {
                                        'name': 'ѱӀҞ\u038dʄʦ˳$\x94¤ҫϒăȄ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȯΐ˔Ȍώɽùś˛ƕηƎƂѭĕиǠΔθȈ˴ƎĶ\x9eăΘϺЦ˨ҿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            694354.5107853875,
                                                                            823814.9750008397,
                                                                            141049.995557489,
                                                                            89705.89250542352,
                                                                            869285.8355244804,
                                                                            232518.78628628468,
                                                                            276922.01087715913,
                                                                            -62710.505044770296,
                                                                            591559.4336570369,
                                                                            316159.6534200094,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "҉ªɝҙЀīħ˺Ƽǡ˶ԔұѢɄ'ÙÁȽѻŢҬ@ʞ\x87ʠƽҝ³[",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.037670:+0000',
                                                    },
                                    },
                            {
                                        'name': 'јğÝUśϟɚԅȦНČвǽɯͰϙΛÑԧƞƴШbԍľǬǑʛӞū',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ϧëšƕ˅тϡ˫ĺѼƲ\u0380ȇǲŶ=ëːİ˛ǞҸÄʨȺʪ:Ą˒ǵ',
                                                    },
                                    },
                            {
                                        'name': 'ΧӨí',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЮķϾƽęȎӫûȭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӕώͺҏҲ\u0383ǺԭΑϵȏԨ҅ʯҷ˭uӇΪ϶ΨǺЦŔĨǑƳӰԀВ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƺњͺĬɗĭԕώŲţҌѕͺŁӯ˗ťԉϲeҼэѭѭEȚÉУáX',
                    'message': 'ƒŋɏӅ\x8eΑ¼Ǫ\x9fƛƷ\x8cˎɦӋϭǖŔԘě˗мəʙĉёҴĵE¦',
                    'arguments': [
                            {
                                        'name': 'ȾȬƋ¼ҩʛŬɗ˗ΦɄaχ*ѝ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': '!ňӇǴŎ҃ԟƉāƾĦŠķԚ|ԇӌКåθϘɤȮҰ˕Ǜˎ˘ĚƖ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': 'ļΩÚԐ*ʛą8ńІųѨ·ʈȟԦŘƴϾѹÿç\x85Ҧ"ùυÂū¬',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'рǹӰ®Œƫĝ¸ҥ˚уǓ<Ǵǒ$ʂdɖӬҸü)ȧŖȷӡӐώĒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѮW(ϥΊ;рÁӗůǜXŀԍʾɘɠϴBԄθЙԫϨĒΔrϒɔæ',
                                                                            'ɔЗˢƺҮςûũε±?äʃ×ΏѤБϖăзķΜϴ¦\x8dэƈīɌĦ',
                                                                            'ɵʸTǨρϱʽѢǦǳЦɶ½PӸ\x90ƟǉвͲÌĿђѿ<ҳǮɺʑH',
                                                                            '÷ϏµŚƦԝǄӾşŏè˳Ķ\x9cӏØ\u0381ԬҺϷжƚԦаЋҒYΉɊӼ',
                                                                            'ƜԪīԬӑˡǗΠßʷeӋʧѮӑȨËѠQĩaʆƷˏœ˞ӟƵώϋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'θȸȐǂbÚŗе',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƨӵФRЋΚȷʹԚKέǥдѯҺÛӵψ\u0382¢ʵóȅJϢФʊƘʫω',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '5ɲαÝāѿãЉÇƶÞτΧ\x85Ȥ˾Ԟ¬ӈςϺĵɊ(Ǯԋ6ӒЉά',
                                                                            'ǁțΝ[ţāȤǮЩwŪĽʫǙƅԋˎęŝ\u0380ȄΞ$śĄӭȨӂĒҏ',
                                                                            'ſÚƯʙф¡ƻӤђǴȆҟƖόҕĪˣΡƜϲџȭŤˏЎƴQҦaɘ',
                                                                            'Ѫ˶£ǏȁɁ\x92˅˜ʉҤҪӗg¿ȞΚ*ʓ<\x9e˸ťȉɌюƼαҝƪ',
                                                                            'ʱΚǷŚƚɀǠ~ƘԕʌҖԌɡÕЁτɈÌЊæҟːšϻϖѮ˝Ӧǡ',
                                                                            'ΜԪђϽȶѮԬõ(φϱҮӧИЁ҅ӪòeUÄӧЍͼјѾӫūWȀ',
                                                                            'ƔhΨƼӄѴ[ȏƧǎԢʴҍΌĠӣЬvƻʍЭ"ǴĬЏȶƈӥá\u03a2',
                                                                            'ǫȟϬȬ˂ñтҺʩȃͳүϿƘƔ΅ӭȋЖñÎӮȂѐƕ>Γ8ŪȂ',
                                                                            'ԘȀʎ\x9fɦ~ȥƿƾϸӒȁǦeɢşƭœӎθçϖгǉʭЦIȴ˯\u03a2',
                                                                            'äWϯѫĐɤMУρҾĭȴčԛԓћÛîxз҃рvYчĞϾӌӺӤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЪѷɠԋƮŨƤΟͶ˖Х\x92Ť',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -78170.66975339918,
                                                    },
                                    },
                            {
                                        'name': 'ˢԪӉ\u038b\x87%ȴ"ǤͽԓîɲћȄ.˴ϊÿȿҐfȨΌθѻƟ˖ԐǶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            320185.65482789685,
                                                                            918957.0590455814,
                                                                            420250.94065947155,
                                                                            463257.1829279874,
                                                                            794129.3012893796,
                                                                            825005.186116463,
                                                                            963647.6694737133,
                                                                            611437.8456465289,
                                                                            632356.2810292051,
                                                                            53217.95676855964,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɧͰзKΐǾmҝҍŵб\xa0қҝĩ\u03a2Ʌ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            897991.214210353,
                                                                            58758.90237226221,
                                                                            24193.745860514988,
                                                                            217537.23948415765,
                                                                            -82722.47770351963,
                                                                            -44610.81154533874,
                                                                            443589.1215095845,
                                                                            365518.8137678363,
                                                                            80071.61776015587,
                                                                            591695.6648740574,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϗ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.040740:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x89ҕМÌҭȽαϩԋȔŝ˜еҫƓΘnūΩӎÏѿ˼ԅӄ҆Нϡȫ҈',
                    'message': 'гӾȣѝßҭ˨ƔȯʛĪЕĭɬ˖ʓ\x99ĻɰӟäŷϱɂVU©ŦɈм',
                    'arguments': [
                            {
                                        'name': 'ɡ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            627341.7038838656,
                                                                            157167.74457888713,
                                                                            489653.82488850073,
                                                                            716428.0763684177,
                                                                            146881.43729496474,
                                                                            578310.7097881575,
                                                                            59071.06195785894,
                                                                            -71859.08545917599,
                                                                            730481.9246385754,
                                                                            -87140.1666521031,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¾ˮˊŜӤȡÃе˲ЩȌɗǂԜЖŗˍ¢ǌȕƟΪѪ\u0383ΕþӴȔѝǳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'šʍĸεĎħϘ\x8fÖ6ΘØĝΗҙшΗ\x99ϬʾҼƣºϗ\x93ԑŬśҎƭ',
                                                                            '0Рʳӎ\x9bʛʾï˸˱ůȖ\x9bгҠŸѸŤƫӧʗǵ˧ώ,\u038dŽҙρҔ',
                                                                            'ˆѥíěӍӲԇȅӄƋłǰЕϨŤǽҾ2Ë°πҏ%Ѓą϶ÍμĆƚ',
                                                                            'Ϻ\x98Ӕȩӫ\x93PʟЩӕӓ˪ΫŋϏˠұΏɍҝȬŠ!ɒΠͿӮğўΫ',
                                                                            'ӳƟЭ\x89иgâͶȃˤ˚ǝȧʾ:ϕԖ\x9eăǆѱŞЁˆÞkƇÁǣτ',
                                                                            'Ҹ΄ƖĪÚƙÃϏϔѥςԭȐћʟŽ҇ŐĨŔІ4Ϗ\x8dΪˬЩĀȰ\x93',
                                                                            'ēѾ\x97ǆǥ¯:ȟɩӻԑƕƷŖzЉfӨò˙ЌʗЙ§Зӽŵʊȋ¨',
                                                                            'ΛҌӦňÊĿҡӹɛϖſʡŧӇĝΈŋђÂȴӽģĺтáſѵҞΰĔ',
                                                                            'ǓɲϜϳЙ\x85ԍȽŽϳϾϭʱǅřbĻňӷȘŊƨ³δlщŋɻΌѴ',
                                                                            '·ҴʞǉȂXƑӥ³ΌȁʷϘʪčΊѵԙďЍ˦ŸϩδԦƖʮÁсʒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ъɋɻĻΘĽԨ#ʩЊӯˀ,юÙ£ñźʕ¬ŎĚaʼƠĨɱӴȾо',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 327281278133472224,
                                                    },
                                    },
                            {
                                        'name': 'ǧnŬίɌĦϴˀМUƁȄЧȌ·\x82ʊαċ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.041999:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѮɃʞE½ū\x8e¤ΜɿԉɩʈÐѹʬɄЮÏ˚ǎȼӢҕ˕ԗM¾ĵˣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1451845212094569227,
                                                                            795168773885164576,
                                                                            7595972517924306616,
                                                                            -4902822998992671363,
                                                                            -2033750656337697666,
                                                                            733179137561974143,
                                                                            705671773978092281,
                                                                            3131764176775193673,
                                                                            -2271771694764102938,
                                                                            -1353014098222740728,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0380ґw¹˰ӆǀͶǭҲҢķϝkӱŢëšƵ\x86ʬӮғ°áĘğɻԝз',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǘĺШˇҶёғFϾӮǞϨšϐôԇɛӘ[\x84ǎɊ˴ȚÞеԆϛӝΪ',
                                                                            'ί1҇˃СʱЮƮȶрȶɔȢɧΝԛҩ¤ˆҀӓԌÊϜђɅȸρϙƢ',
                                                                            'ɼɰĢӯʬʗϬсҧŜŜŬИӿɬăˎ_Сǋ/Ɍrҭ˖ǦҔΈʻǁ',
                                                                            'ўʸʡ˹ÔʊŕѠƞԔƼϢəʰŗԚ˩ӣшŲҜϤŹʯɾǫҙƲϟɒ',
                                                                            'ЀΤȉѥũNȖχõӘӽǾƊǎ\u0382ȨϨΕѡʟĴʨЪǎCɞʁѓԛʑ',
                                                                            'ƫ¹͵ƈ\x82ͶʱȅǗѮţ?ɷtˋɾҘ҅İɹŏƱǀӓǌ΄ѳǷЙǺ',
                                                                            'ĬɗӯåƈȜЅ˷į,u^5ȥ\x9bC~ǓŵӂчӭϱѯІâȎέ˟Ҁ',
                                                                            'іɻͿ[ĽȆĎȭҁÙǯ¿iРԙ˱ǷБϸͼ¶¨ψȬÌȺΧ\u038dĦԙ',
                                                                            'ǩȤbƵʕȋԓ˞Ģμ\x99ӌҙùψȒǌˇѻǾͱĖˈɃŋƕҭĚ)W',
                                                                            '<ìҫ˕ЧԤϢÆӮǎͲȿǨĥƨуƒӐǳɗӻҰǑǶɿő(jԖϬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÕòŶ"ƓʥʲêГ˧ǭˑšȱ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ақӲӢӯ\x81ˁΆ°ͳѓ&ˡÄϦӫŶȀЯŶÀ:ǙӧɎԮҮΰӀƌ',
                                                                            '˳˛ƤsǀПĲɯƒЪɶǸˤәōȶ҉ЬʵЛϵ˓Q>zhþ҄ʕ)',
                                                                            'rΉѭ\x99ƢԄӌҷ%ˈБӾЌF4ԛÝ#φ´Ďў®ɴӶԗШϻȧó',
                                                                            '}ϛǄ˘кf²\x88ƛӠӪϒſƇϘƊŘ³ʱƫ½ʹˆȓІƕɑʉi\x8c',
                                                                            'źȔԜΎПɁӰʅÛԝ2ԗʏ]æ\x82Ɵ<ɌӚНһƒʬϼΌ\u0379шŊɵ',
                                                                            'ƆԅtŕəӑȢȐɸўɊuθόϮ}ǑŧĝΟ\u0379ˡӘɅѱ*àϯgŬ',
                                                                            'Ӳ¢[Ҟԥԭԑ\x8eЈϖ¡O\x8aҶ{æӴƴȩӀѮĲ6ɜԆĿ҄ĀέϜ',
                                                                            'ǂƦСÙ\x85ȰҏϣˌѯŰȳ˘Зʺ˟ɼЛ1ҷŬ\x81Ϲ\x93ѯζЩaӑΓ',
                                                                            '²ЬPλ¶ԃ\x9aȑпНÊĆΫɓԕғСӊƱĒҬϢŗӋƀϥɫhǼҥ',
                                                                            'ΠԙɟϷǀ˴ʞѣЬӝΌԝǚΧƯʽϻӊëɳ]ǞæΏtДѻʧҺѓ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9b\u038dϱϒуĞKъέýҙɹҫƺĄҲ-ɆԔќЍº\x8bщΪƄЊӻϓҮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -909283807456154885,
                                                    },
                                    },
                            {
                                        'name': 'ʙп',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˫ӍƼғãɡͱԏ͵ΠԖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.043371:+0000',
                                                                            '20210224:164112.043384:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ðpĻ¥қËęԧĽЙ¦pǲԧ4MѭЊʜwʻ·ѭҌõѶĕϭƔλ',
                    'message': 'ËȃӁʇˣʉѭʽѳ½ƻʯάŜʋƴƙʲϧʕ˵υϚøҏϸĿ6ȏһ',
                    'arguments': [
                            {
                                        'name': 'ĆȶϸǱǩΞĐδ"ĥïЌ˂Ė;ÑÏɵӠѶčϵ5ʯҥά«˾Ěϖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            812331.8444725657,
                                                                            139424.64751945867,
                                                                            503798.5931353058,
                                                                            164982.8759506315,
                                                                            397317.34249134053,
                                                                            300199.3286791652,
                                                                            970823.2887145604,
                                                                            -62026.475527398376,
                                                                            -63865.354044125444,
                                                                            558135.4875889096,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĻѴλƹҕĳǦзСԘǣĠѤ+Ӧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.044156:+0000',
                                                                            '20210224:164112.044171:+0000',
                                                                            '20210224:164112.044179:+0000',
                                                                            '20210224:164112.044186:+0000',
                                                                            '20210224:164112.044193:+0000',
                                                                            '20210224:164112.044199:+0000',
                                                                            '20210224:164112.044205:+0000',
                                                                            '20210224:164112.044211:+0000',
                                                                            '20210224:164112.044217:+0000',
                                                                            '20210224:164112.044223:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЉԁзȀԘ-¥xԏŃҢΏҲŋήɟǹ΅Сη}˵Ԩ»ͿƥÎѣŚĝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'βμÝˎ\u038bôҡŷюϟϙͿӌʜȍ\x87сʒČ©',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5366550276644916623,
                                                                            -7334988115689935387,
                                                                            5119720857730491817,
                                                                            626801615286539244,
                                                                            2662073427678680375,
                                                                            -8128178327393566162,
                                                                            -1795767378359054507,
                                                                            7272672194417987514,
                                                                            -3329948105438120094,
                                                                            5113946777327326989,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʮίҿԁkѾϔѻӟ҆ʹҀ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ҞΩБïˈҥǲˋƼ¸ˈ΄ʥƸƫӊȡцĨ҅ťðǓѴ\x88',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɊΈΣѴĚΩŰŝºǪԂ\x94Гʌè2ӁñҒ-»ʚɦԡӞʐҁ²ǧ\x86',
                                                                            'ҪʏĄɴȉӱɃ˚әɬşӥ,ȻΝĻέШīԐǸΗҮˢȏϲĚ¬ʝѵ',
                                                                            'ҸѼӻǷʞѺԄIŨ\u0382яȜϒҩ\u03a2ȋӭП΄Ѵʄєɥ˯Ц\x94ͿïӀ\x9a',
                                                                            'ʮʋѬ¬ɅåӮСɩԅІϽˑӁɡϼДȸΠƴӰ5Ѳǽ҂ǟɘŐŻ\x9b',
                                                                            '҃ĝɔнӤӏϧũŝґądʖɳəȤǨȰʋÁоíѠƁ@ҁʄŽòІ',
                                                                            'ÍğʻɯȕŊ͵ÑʟЂӾ\u03a2ˬtŬԬ´ΨˉɰӠĆ·ӫÂҭҺҮ!ß',
                                                                            'θlӾȞПƏ˟ƍǝЈԛ¬ԑтɳ˱ŃˉѴoȤ5ʧȷѽ·ŰiԎr',
                                                                            'ƺʥɨƘҮǮ-Ʉϥð˕ȼǡȆӳȠȵϣɆOɝҼӞҾɿLʅЯ˝Ѻ',
                                                                            'ЖҞɮыѬӆϣҡȽĭƭџj˂ўҀʰяƼųƉԐ˽Ǽһ˨Ƒͽðâ',
                                                                            'ȔͳτОӡχКҩӋзC£ƣEӐƜӍÒӥʙ!ʩϪ˼ΰǓmοŴҨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'њϰĈхүĶ7ʬǎĶҀǚԩԟȘΎɭњ\x87T«ʂÈϧщþнϕлԡ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                    },
                            {
                                        'name': 'ϩJ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            253269.82020304713,
                                                                            459354.194539157,
                                                                            675468.139785439,
                                                                            513074.2154623744,
                                                                            342067.3610027164,
                                                                            696099.670652415,
                                                                            381104.7883322442,
                                                                            -78879.48567223288,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'εЇƱ˙ϾǏхΏѮƊŜгΨʗ|Ť]îƦɘʱӱxŶΏșлͽƉ}',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.046014:+0000',
                                                                            '20210224:164112.046027:+0000',
                                                                            '20210224:164112.046035:+0000',
                                                                            '20210224:164112.046041:+0000',
                                                                            '20210224:164112.046047:+0000',
                                                                            '20210224:164112.046052:+0000',
                                                                            '20210224:164112.046058:+0000',
                                                                            '20210224:164112.046063:+0000',
                                                                            '20210224:164112.046069:+0000',
                                                                            '20210224:164112.046074:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƙ?ưÇ\x9bӱ¤҃\x99QƢӳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5954911371847324897,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'рόȏĞʇҎZ&¾ҎȗȢƍҤĸͻĸѳ',
                    'message': 'ӖĭȾΰ',
                    'arguments': [
                            {
                                        'name': '\x8cɘUʗɯйҦʸƞƦƬΝʵêϬņѱŕμǑЎϛF³µƅǐʹК;',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2138501681777401034,
                                                    },
                                    },
                            {
                                        'name': '}ɛåҐ˛\x90ɔʷ;öǼΧǖҞeś\xad«)bЅӕ³¢$¶\x96ɹȒӨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.046810:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x7fхƷƢɉӲȉͰʑ˟ǡŖ¡\x90\x87ŠФɄ\u03a2ԡƚӈ˲ʸ¼јƈÌǝԣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 293498.47232668893,
                                                    },
                                    },
                            {
                                        'name': 'рђЬĶB°Ėúԝѱ\u038dω1C',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3654906769536686321,
                                                                            1944321851909998263,
                                                                            2711582965467863627,
                                                                            -197446331691729839,
                                                                            -8050052887928441752,
                                                                            4081121107906353840,
                                                                            6590872922687727918,
                                                                            -3806425586748615788,
                                                                            -4013627292798644281,
                                                                            -873530282947683307,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'VЕƖψоYЮŬƎȦɝζЯU˙',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.047284:+0000',
                                                    },
                                    },
                            {
                                        'name': '˝ȏЂŗӑԣȯɉԛʆǖƋЉÞȄͿĎӆԂǑ˅ƛ˰ԚżЁС\x8dŵ\x83',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.047423:+0000',
                                                                            '20210224:164112.047434:+0000',
                                                                            '20210224:164112.047440:+0000',
                                                                            '20210224:164112.047446:+0000',
                                                                            '20210224:164112.047452:+0000',
                                                                            '20210224:164112.047457:+0000',
                                                                            '20210224:164112.047463:+0000',
                                                                            '20210224:164112.047468:+0000',
                                                                            '20210224:164112.047473:+0000',
                                                                            '20210224:164112.047479:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʜϦ=Ȫ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4263880354351171731,
                                                    },
                                    },
                            {
                                        'name': 'Α\u0382˄ͼɶƞȪǀȏЅĤͰϷťľǆѬÕЊЗɥԔѥҏμӀǼӦǃЪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7311770127340321718,
                                                    },
                                    },
                            {
                                        'name': 'ƱƗкī3ԆҸ\x94ΨҢĵ«ΟĠԚșˁ\x8cљēƷΧɮΞǟÛíӷDȱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2568222629680527383,
                                                    },
                                    },
                            {
                                        'name': 'ĤӓѶʜâʗτѤҀѬɧȸȻȈȖʊįΆˇɗƬҰϸǎѪÿ˂ϚѬ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.048047:+0000',
                                                                            '20210224:164112.048059:+0000',
                                                                            '20210224:164112.048067:+0000',
                                                                            '20210224:164112.048073:+0000',
                                                                            '20210224:164112.048078:+0000',
                                                                            '20210224:164112.048084:+0000',
                                                                            '20210224:164112.048089:+0000',
                                                                            '20210224:164112.048094:+0000',
                                                                            '20210224:164112.048100:+0000',
                                                                            '20210224:164112.048105:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˴ÍͼĠɂρϦӥɺzӔȘҀǗΆ˾ţьіӇӨЙèɬʥĒєǑљȯ',
                    'message': 'ԁʁя¿ҢĴëȥÝԑº©`ҝЖԃϏʔΈǪ9/ͳɟ˞Ѿ˟~ǇĻ',
                    'arguments': [
                            {
                                        'name': 'с\x86ŇӔӢӞȃҫD҅ҡӞ˫Ӥӗʔ(ξ\x95óɼƈCͼБ˞ʺ˵ƮΟ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.048562:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӭȳΠáľʎz҉љǔђ«Ұʜ7Цɍлˋϓ\x85ӉҷŊЛ˓ЄŲq{',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1769051741061699638,
                                                    },
                                    },
                            {
                                        'name': 'ȦԒĮ.ĦШȽŝˁ\u038bɿʹƴӛӷÊ\u0378үҾђƔĮÓВ\u038dȎ9˙ͲX',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.048957:+0000',
                                                                            '20210224:164112.048974:+0000',
                                                                            '20210224:164112.048982:+0000',
                                                                            '20210224:164112.048988:+0000',
                                                                            '20210224:164112.048994:+0000',
                                                                            '20210224:164112.049000:+0000',
                                                                            '20210224:164112.049005:+0000',
                                                                            '20210224:164112.049011:+0000',
                                                                            '20210224:164112.049017:+0000',
                                                                            '20210224:164112.049023:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Æ_ԧƴǍʍ\x83ԨζƀĘ\x83ǈŁôʋʐȐҘҪȏͲ҆\x80ҞŀéЧҁø',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.049265:+0000',
                                                                            '20210224:164112.049277:+0000',
                                                                            '20210224:164112.049284:+0000',
                                                                            '20210224:164112.049290:+0000',
                                                                            '20210224:164112.049296:+0000',
                                                                            '20210224:164112.049302:+0000',
                                                                            '20210224:164112.049308:+0000',
                                                                            '20210224:164112.049314:+0000',
                                                                            '20210224:164112.049319:+0000',
                                                                            '20210224:164112.049325:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ș˼ІѢåԜʇЀ.\x9bÀ¼Á',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѱ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ёÛMБϬɮXЫƄˣÞÚɬwѪȫÎʎƱºȄ\x9bSԉΜÍʱ\xadоʹ',
                                                    },
                                    },
                            {
                                        'name': 'ΪØ-ОKӀʆԚԩĮǫЗлÐͺŸȍЕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӵɞ/ӵҵƴͳшÆƨТ˴öƨϢĽ´¹љΗ_ЇӞЭ˚ɠjĿÙг',
                                                                            'ƭӞԋÝːΝt҆ģѕҝŚŧ·ŇWӊ¶\x9eÂņĈ0ϝŎȂχϺʂШ',
                                                                            'Й˙ϭ˴ΝɟҨ\u0379ǭкӗ˜ȾϝɠγΔ\x90˰Ш͵6ӡЪƽѻȗѶЖî',
                                                                            'ρΚϡѕǒӤǟć`Ȣǽưʒ"ȸ\x83ũĹƪ˶ȏʀϭŭ#ȆзɟŤΏ',
                                                                            'ǿTǙÍҰӍѣHƬԃЭǣŢǙ\xadűǁŹҞ˛ɻˉ²БӌĺƚǃϵƤ',
                                                                            'Ǳ2βŊǞѲʦєĮ˭˯Ѩѐ\x8eʿӧӿиӷʪđλjɢũ϶ςѹеЇ',
                                                                            'ΎįŬxРȦӖİƠҸūГŧʗԣĉɂіИ\x98ŵӗ˃ӯǔ\\СOkș',
                                                                            'ťɊѵŹТÅˡĢƥğԢɹ\u0383ВΏWų6ԩΘ§ɡǋ˰ǰćɆȏ\u0381Ѻ',
                                                                            'ĭҔӽˬCʄЙïΛÙԓ_Ӌ˨χȣ¶Ӟѫ&ӛƊȅʻßɐʹњŇĵ',
                                                                            'ԎƮʀѫˣɮ˝ƴŜКԊϑɠԭԆΖȁSүӿʹϡƊϸԈиbӲĭ%',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'üȗβĊ\x87Іɥ\x84ɢŝ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4495856932474136222,
                                                    },
                                    },
                            {
                                        'name': 'ƹɥ˻ŌёхBԋɝӾϮŘʓͷͺ\u03a2ЋĖ΅<ԓbҖŲҜДԔӥˏѪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6025035861754899066,
                                                                            -9141717779315311381,
                                                                            1100006215901356459,
                                                                            -5176130295903676322,
                                                                            -6606544499356095111,
                                                                            7336826807048142143,
                                                                            4981710735041209561,
                                                                            9116531424036010835,
                                                                            -7644827871612789219,
                                                                            -7734802483884417807,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӄȘ҂ǈĊѣ˙θΫʂ\x93Ҕȭ\x89ȇɛʱɒѥ˪ũʾќһOƭғǐdƸ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.052742:+0000',
                                                                            '20210224:164112.052772:+0000',
                                                                            '20210224:164112.052782:+0000',
                                                                            '20210224:164112.052794:+0000',
                                                                            '20210224:164112.052805:+0000',
                                                                            '20210224:164112.052814:+0000',
                                                                            '20210224:164112.052824:+0000',
                                                                            '20210224:164112.052833:+0000',
                                                                            '20210224:164112.052843:+0000',
                                                                            '20210224:164112.052851:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ͽЛњɶƐˈ\x8bǩ\x88Ԥ\u0382ƾś˟ѣҰÜЀńϫłӵŻϚΜӕϬɑʅЈ',
                    'message': 'ɽȁәƁëү¿ӨЉϫʞUгNԔĹɝƦ\x94ǁ\x8eª=ŏФʍǫĜʅȒ',
                    'arguments': [
                            {
                                        'name': 'ҝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            6280.83025795476,
                                                                            353692.34970813675,
                                                                            968522.6784073161,
                                                                            325325.83221545466,
                                                                            219000.3487520478,
                                                                            839394.2377437769,
                                                                            929937.1288306763,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƭ˥фȽāηϘÎƖĽѴʅβ\x81ŘӐλƀϹӛʐǚƶ©чɧˆҀƮǛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            457898.2384575313,
                                                                            167450.29288762767,
                                                                            995323.3189010345,
                                                                            272067.0365766317,
                                                                            405638.45493048953,
                                                                            823433.2619756246,
                                                                            644159.8934626558,
                                                                            912041.8334859549,
                                                                            370290.3556349476,
                                                                            518235.8217629398,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'КÈƓËЧĄǳşåʖǌD\x90γЋʅ˒ÝъȼψɮЬƝ7Ҕɏ\xa0vj',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            232287.96094361722,
                                                                            409304.6361740866,
                                                                            593972.1126404388,
                                                                            679584.7633666971,
                                                                            -2461.8631932330027,
                                                                            801038.1566383856,
                                                                            540933.2999756496,
                                                                            -1290.0112338663603,
                                                                            355057.3361900392,
                                                                            175601.0358630519,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ėǂФɳϹΖѸªƖʰǲUԜȄ³ĝɫ,\u0383ŝӰʌԖù'\u0378Ǧԍŭ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԀƇŮ£ōΏǢӛǴҭ!ʺ˳',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            885874.8967492757,
                                                                            260727.55799112056,
                                                                            520226.80350450333,
                                                                            384414.6639175076,
                                                                            339369.6492068202,
                                                                            507248.6082345847,
                                                                            -33439.175620026086,
                                                                            829852.799848356,
                                                                            662368.8656999703,
                                                                            875488.4485822438,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɓ ОĬНƗɰԣōҕŗʄ\x84Ìвғϧˏì˩ϲԍҴǑÑÌҋǎЇǆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.055512:+0000',
                                                                            '20210224:164112.055539:+0000',
                                                                            '20210224:164112.055548:+0000',
                                                                            '20210224:164112.055554:+0000',
                                                                            '20210224:164112.055560:+0000',
                                                                            '20210224:164112.055566:+0000',
                                                                            '20210224:164112.055572:+0000',
                                                                            '20210224:164112.055577:+0000',
                                                                            '20210224:164112.055583:+0000',
                                                                            '20210224:164112.055589:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǍԗˮǲɊʓЊʋ0©Ġ£Αȍ½ŝɿ7ΆұʟĜƲӲʙċŇʔĤʾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -867024267160909098,
                                                    },
                                    },
                            {
                                        'name': 'ŝөƨԇ\x84ɍ˦uуҗÙ˖җŢεȖʺϭӯв\x93õİ\x96ǽҦɳɡǿи',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ïζ\x81ǉӨҷɍƷԎƸΥϻ\x8bǍΥüųʖǴǿɉɊėĜ\x88ǱìӝNȿ',
                                                                            "¦ˏҽĖЎ\x88ѩдӸ9%ɑȒϻÄ'Ȇƿ\x8eșǃƝ×ɨԄȠӺӇºȪ",
                                                                            '¢ѱǵlķ\x9dŸɺũԢӺȞHι¬ĆԮԪǀҭԋǛĒŇɸˣȑʐ\x8cĽ',
                                                                            'Ė|ŮϱȼφәѥҊʀƴ˲нǧƨӑȊƠƐʥŮľǯʺèţ҄ǡљҌ',
                                                                            'µǻĶӯҶųĔįZЮѲ±ʉɁù\x8aԖИɅ\x9f§όqЂǯλʀӹȐԒ',
                                                                            'R¹ȅϻː£ԨϰƦӣɠĝɢЯaХѤ˭ƂήɳϘĄĥƷ«jȗÊƀ',
                                                                            'ӔӫʳŁИ˪ӻȞҺș]ȟϋї}ӄ°qΚǏǩPȒυŧɑ\x95\x82ƔΨ',
                                                                            'ϰ_¡ѸԝƸǁƍǙÍªǠĎʵбǃRΔԨʤʆèѝʕȅ¤ѕPʿ\x97',
                                                                            'ӳӛȇϕ\x8dGȯÌҊ˃ÄGƑ˯qΕʱNCȣȜΪɑϋʪhƇŮķ\x9b',
                                                                            'ǄŀίƋǱĝȾ¾ԭŽαƂWϬɂ\x97ԆіėɏѶїɝɥtqԣԀĤͲ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҅Ī&ȵƤµӐɩӥΕԄ&ԟ˃ĀʋĽѣİżďȥӒīƌɏ˥ӆǦ˧',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7967921763403603408,
                                                    },
                                    },
                            {
                                        'name': 'ψ\x95ӄŤϼÈøϔãɹіʾ¾\u038bǵľŝяϙҢʁȟ ϛÎŸ˰ɪȽϛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2443890124350460965,
                                                                            3534521261351689600,
                                                                            -4348725114035104361,
                                                                            2667577689698607603,
                                                                            -6778662628740682823,
                                                                            -5425366726364699074,
                                                                            96814810035050389,
                                                                            -7034435857170251164,
                                                                            5277447421407865233,
                                                                            -1761475733466830167,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŒįŘĘԉʡğɡſЪǹϏ˽ʆǢħӳҺϬžȿҰ҂ʗЁªͺǟ¥ҡ',
                    'message': 'ΩȈ¨τņʧӖǙњDǈîԜťϨØ϶Ӏ\u0380ÖϢτ˕өÑŞ?Ǉ˄ҹ',
                    'arguments': [
                            {
                                        'name': 'ћ£ɜ\x99ÙǔÛǏʠƟÀšǀ¸Ħq',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʀɋсϥԨϋэ\x94ΠʆőfǶƱǀʕˋɼơͰ˰ɸѵé8Ƃ\x8bȐʫԫ',
                                                    },
                                    },
                            {
                                        'name': 'ңĚΐԚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ɂԢ¿ƼԬǥҡĝǼȭɝϫƷ\x87Ʊ˵Ą'ϏŋĪΗЭ϶˲ɮƷǱћŧ",
                                                                            'ӊӓ®ӎӆŴƒſ;ǝˇǨџŲŃŞϏƽǻƟ˻éȲɝʹːȌŶ;ȯ',
                                                                            'φɨԫ°ńŗɞȨɺϛţЍřȜԬΚЌжϿȳЂÜѻԠtÛN`Δѹ',
                                                                            'Ӧ3ü\x8f\x88ȞѱYͿΎȉùʣɒѧJҬMӴэŅɪqƫŞϯ\x97ǩɦˡ',
                                                                            'Ԣѥ ȽˏҴR˗Ҭ&ă~˓ƪΉɊØķΈì\x8aĞξĭϺȣƌĠQɞ',
                                                                            '˅ѩǏκʕƳvȓƚƱ\x93Ɋ\x9aNϥЖƝҼуǦʽ˔çңȘ^Ƹɸџɘ',
                                                                            'ϕŔȅνϔƩ\x90ŮҸϥώƇƯ\x97ӇвӿƢ¶жƎÉʹά˜ćÉ¡ϵҖ',
                                                                            '3ȣĔɉҮʝΩëƗʪѬʥʻҙɏϮCʸϣѱ˴ʗԑƺӽρμÊÀº',
                                                                            'ƼƝԌѱǊɸŤƍŰƝ÷ӝ͵ĦìʼνɌѴŻӻωɓɸȾԎѝϭȉ(',
                                                                            'ЌδûŮͰōɉϑH\x81\x9bʑԫφʹ϶ΑʮƜ¸ȥȫ\x81¤Ѵɟ·hǹİ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԯ҂ʣǞΏ\x92˟ɵȠ\x84ÏӔȽқͰ»ȔʆƹAȲƶ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȯѽԢѱõƟнӺӽȢА˄ƾľѪŗŴ\xa0Ѽҧ.ϸьĢɷȎҌӥȨˌ',
                                                                            'ľˍҧԃлυǐӧӈƄ~ϼÔÉĻȆұáѫŜD\x9cΘƈƯƒϿŀ`Ч',
                                                                            'óηβҥʇαĊάʤț+χѩƼҭŏ˰э\x84ҡһɢҫˢɿӓϋŵ˙ɱ',
                                                                            'ήζ&ƳuǞϊċҽоǞюμǳˈɥҀ\x88ÏԄͻѱˋγʷ6ϤņȆӑ',
                                                                            'ˑʱѲǰıǲØȆ˲ΡχѦƶӈѤѷ\x95ňǭʚΆ˨ƜƮΨʠӼʇҼǊ',
                                                                            'ԝAũʏȪ˔ǲȎŝȻӽ³ΙϕŅďϜѾˇӜ±Ϸƕ˘˟ԏʙӆБɫ',
                                                                            '0ɕ:șӓĀˏҺ˟ͳǀšЂŉ0ˎ\x9bіəǱ\x95ɋƭ\x86ѶЅО\x85>ņ',
                                                                            'ĢΟɁɩɴŠϑЋȿ&\x8eƪѥǯʯǖȏϦɧ˖ɗƅӄˇφùΣϒҌЂ',
                                                                            'ʀθӚǡēЛМВ¥Ĝ\x96ХƥԝРϱLìͺеѿƨʇ\x98ѮˆȌkϲе',
                                                                            'ǕǲϢżɇԏŋͰȅǠˋƙʏǁ҄ťӹơŦªқ±ϛÈîɼˮƂԢè',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʃӳӷҳďԅĖȧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            466601.3848510514,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x86Ĩӭ ѹΗòƤʧѲȴԕʺƉПзѓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŲπЫӿɨϖӏҲӋ˛}ӀҸÀѠ_Ӯ¤ĠƢνǔӎ˝\x8bƋ˧ŭ˵˒',
                                                    },
                                    },
                            {
                                        'name': 'ғǘëҚйԤϺRŰˀ\x9bϔƒӝ!Ƨʒŝ\u0381Ɋ\x84ǾǺŘѾAӏԗƭԉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 823019.369175484,
                                                    },
                                    },
                            {
                                        'name': 'Ԁąə|ŝҸѕŔʦƁʻ\x9eʫҶяңӓʿʜ¨ΧǇϩĵŴ˘\u038dԂſщ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȎɃϥ*ӻ˶çƻЌ˵ʃnύХїϑ¹ìΓȰ\u0379:ӲϷƪӤ˶9¨ӿ',
                                                    },
                                    },
                            {
                                        'name': 'ÿʊďӰɟȩâΤ\x95ΐȈʛ¯ǲνņɡëÊ\x86˂ĬˍѼĮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʷαŚɧʫǒ˯Ж\x90ƠŠ\u038b¤ѹiΆŢ7#ӮƉϒ9˔εŒѦӟȓɡ',
                                                    },
                                    },
                            {
                                        'name': 'ԉʟ\u0378ŸˈɽåÑʡϱѠРʟȖΩķȸȊǦӉҾҁӄ\x99Ōϛƌԅ\x90',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.059988:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʸѡŹǗĶLßԖȷԧӄҵţłʛҟюƟԀîȕԇςɛЈƉň҃Ԙű',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.060141:+0000',
                                                                            '20210224:164112.060153:+0000',
                                                                            '20210224:164112.060160:+0000',
                                                                            '20210224:164112.060166:+0000',
                                                                            '20210224:164112.060172:+0000',
                                                                            '20210224:164112.060177:+0000',
                                                                            '20210224:164112.060183:+0000',
                                                                            '20210224:164112.060188:+0000',
                                                                            '20210224:164112.060193:+0000',
                                                                            '20210224:164112.060199:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'żĶѺVрҗgėȔжɖɣҬT+ҭpŜɬ˙ɝĖŵԙѯωũȕżϠ',
                    'message': 'ϢғӬҾәϏͳǈ\x80ΝɩКŏȐ+\x89ȸ\x84ɑѼѦΜ˩ήďФʬϊЯʯ',
                    'arguments': [
                            {
                                        'name': '\x89ΏȊԕ˂˞Īҿǆҧ@ΐĞžМȜƦÅɳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x90\xadѲˋҕӣλьÜħŗўɇǸɱбʤ϶ʋƅԍϿoŔņоԦĦβҀ',
                                                                            '°Ŧ˫tƷ˹λLΞˀ\x82θτɕñԪҬƕʋōʯ;Ǩʤӱ˖Ûïɯʜ',
                                                                            'ԥΧ\x8bчǢÚqøşϞк\u0379EˏžĲŭêԢʾŪ҄ɴԚωѝ©\x84ӌ}',
                                                                            'ɢzӯҼάĈJґçʬAӮůͱüŚʕÓԐƸŮŷ˩Ў$еӖϘң҄',
                                                                            'ҍΩ\x88ЏƱɸ£¶Ӱ˔ҽ\x92ΣѐșЮÖĨɞ8ˑЬ¥ŢĦ˱·xЙÑ',
                                                                            'уκƩŤӉNȹʖԦԋcŰÃ1ʋǤϝӘǓhѦƮǱԍƝĐƗı\xadр',
                                                                            'łȭӨӣvƻҡҌɛώϠĸÙÀўŵɤɤȊĴ½æøґǴ*ɍŲ¢ɋ',
                                                                            'MЮȼѶɿв\x8eǥĦ-ґБŴμŠǰ"ƻԛиʲӑƸǶįҏϦ҃\x83ɮ',
                                                                            'eʴȊøõԬˍʼӻВЩҼhȳƖҡăәԭǛĩĉӃϝЇ×ÌňɎŀ',
                                                                            'ěXǇ\x82ξʺǦԊɧʖřлΞΑΚҎͻΎ$ςǙÝțχƏƍϰɅȭÆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǻҗͿϮşЫϿ.Ʃԍh\x89˨\x87`ÜɮΏ§ңԂҋѓо˄ҧδǐƊ˯',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.061075:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ґ\u0383мωʇԟɧƒ˂ΪƎǘǲАԛЍ{ҹԧɪӉΠњ͵ʝǪъɟʣɮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Â˯ǟʫȂʓŪŬǠªͳҐ(ŰѨʧĔ\u0381ϤàɪήҸҫΝы¯Ӏ˰\x9d',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˠòВŜ\xadĖŃѬǇћĴʳΌƟѯәԫŐÕmԊŔpǐ:ªԊąʬĐ',
                                                                            'èȂϟ²˵҉ѰǍɖŹr\x81ƚԚͺ\x82ҘCϵсʍxɿðǃÊ΄ǩ˨Ͱ',
                                                                            'ţǔʣјƒЖԇŵăɪ!ːκѨҰ"ǭɏѠ½Ґ\x87ӄ³ɸˆѯǩƬɀ',
                                                                            'ʙɍrЀϤӛҹƷƆΕїӅɯɫΆʈKȨKƦɧčŋҌ҂ԛ˞ǐѸA',
                                                                            '\u0383ǽԢвúШˀƥʋҕѬλШԊĂQɟӽ¦7óSϗDόȰϻƕOҭ',
                                                                            'ƴm˷Ũʧ\x89ТӞÓЂɤˮƲŹωӸń³ϽɣňǱ˧ÿ;рНŔþǒ',
                                                                            '\x9bǇßŰZÕϮɟЊØýΊѰЯʾ¿ʮ҅ȍĂбЂ\x9bβΕŘӱʋ)ƣ',
                                                                            'ƝѯžɧYȿZęͽԜƀȷЕē\x80ć˂\x85҆ƣˬˈʱґǜпƅϺΕŽ',
                                                                            'Еɐ˨ϧԞĊφѩɾӛĬνѹϒɘcԟѿнʚʐȁҋΕͽĽ˓ΛƅҔ',
                                                                            'Ɇ˴ўѐϣž!ƙĮЇȾҒқRмgĻІǴѮτȯΒɡ>ʫɒʤ\x86ү',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŵdƑŢΰԍмºϊ°рҨͻɂˎЫə£Ƞcd',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            120981.3163996787,
                                                                            706719.7655580124,
                                                                            537246.3141063477,
                                                                            398458.8875653236,
                                                                            392736.6419182979,
                                                                            265701.18386944983,
                                                                            706328.107208055,
                                                                            135375.7202401613,
                                                                            285481.186577422,
                                                                            893770.5872088278,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '_ņҨӓǿøƚҮΕH\x92ȔŦԥȼàȢ҈ƜÌҒǳŭɗѮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164112.062053:+0000',
                                                    },
                                    },
                            {
                                        'name': '˳ĸѵ͵ʳïbʥI˥Чάɏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 945536296029216560,
                                                    },
                                    },
                            {
                                        'name': 'ƢÌ˦˷˯ѮϨƮˈιñLͻ4wϖЩϯƴĭͳǋʄǖӟϓё',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "\x89ӔʤġʡƏӶ\x8eɒ'ιBŴϹʮЕˏŕŏJͶʢŭφҶʹћϝ˭ǋ",
                                                                            'ǍǈԫȖɤууȏш.Ь\x84Å÷Í\u0378ԊԕӅðӣȔӾôȱɻˏΦҁЎ',
                                                                            'ȻϪşĈϜȇǘĜҵkӎʶԪЉǿŖiӋïΗԃģ˷ӉҒˆėáϤĳ',
                                                                            'Т˩Ȇ\x7fӵŀϔʣȽşʾňſӃӊӃţVɃƠ©ӇƟҽʭҚ˰ϕĘȎ',
                                                                            '\x98ɚ0йɬȠŮıɓЋɊѻ˅ʶȰЮù1ʟ\\ҵʗǼ϶ҏЈǑǿαÄ',
                                                                            'jȣͰ¶:ΕΝMțӓӪѝŊƐɜ˫ʠɢϷȅ\u038dж(ʤǡƏļͲїw',
                                                                            'ΞŝǱļҲʕĄʬ˄ѷӂïǲŝΕLԭξҜŒ,ȂɏӃˑ9ӼʔţҜ',
                                                                            'Е˳ŃҠȆ\x95ŊɒҌӥ¨jƐƜɾɌĖϧϦѣ1ƒʱN0ϻΐԑŧƘ',
                                                                            'ʕȥǪʶЍǏ\u03798ǌĠəč˜ŵúѷӍҋɗˬΟǼ\x99ƶ',
                                                                            '5Ѿ˵Ϯ\x7fɑЗƼͿǍӌđϚxFʨёƄȂ\x9cǲ˶ʘЀφʮȔʘǒ\u0382',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҂ʅ·Iή',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʝźǋɔјҴө±˲ļζ;ŷ#ˤĔƪʌĖμťǽД˒AƽѷҠȒρ',
                                                    },
                                    },
                            {
                                        'name': 'ҭʞϤxϲΛ҆ȗчѪдĊ¾ˋŏ\u0382Ф',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164112.062866:+0000',
                                                                            '20210224:164112.062881:+0000',
                                                                            '20210224:164112.062890:+0000',
                                                                            '20210224:164112.062897:+0000',
                                                                            '20210224:164112.062903:+0000',
                                                                            '20210224:164112.062910:+0000',
                                                                            '20210224:164112.062916:+0000',
                                                                            '20210224:164112.062922:+0000',
                                                                            '20210224:164112.062929:+0000',
                                                                            '20210224:164112.062935:+0000',
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

            'identifier': '·Ζ+\u0379И',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': '6ǜ',
                    'message': 'Ą',
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
            'request_id': 2739030,
            'error': {
                'identifier': 'ĕɇҩψhэĀīTҷǻӖ¼Д+ưŕ\u03a2Ӣ7ũšŦǒƒ˯˪ΙĀε',
                'categories': [
                    'access-restriction',
                    'invalid-user-action',
                    'file',
                    'network',
                    'network',
                    'os',
                    'invalid-user-action',
                    'network',
                    'invalid-user-action',
                    'access-restriction',
                ],
                'source': 'įɻȜӓϸнǷɈΌ½ŢέƱŵҞŁɋŇȩː˅ϸśǹ%_ʺǠΔҪ',
                'messages': [
                    {
                            'catalog': 'éƳƅҟфŬґҍŐsǖːӵzoîɅ\x8dʶҾfɉ¨Ρԏ΄ζќͼϰ',
                            'message': '0Ȍ˾ʟңҌzĩљгĞˢ³ǂHӌĈӫǴқԨЂƁØňɇъòŧ`',
                            'arguments': [
                                        {
                                                        'name': 'ЮҚnɪǝãЀѬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϖ¨зǺ/ʾ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164112.012942:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '/ΟĞԍύřȓɵмΕ¡Ԗԟ3¶Ѳɳν»Нϯ¬æƚͰȆԚԥ˒˖',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥςŇʔţWÖҗМҗŮúѓхǠǽɶЦĂðƴӻÎŘɰЍêѓ˦>',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 433940.3270007712,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÎϔΈʱǂ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƙ×',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȼӶпЫ\u038bХƐ^©',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΥĿ\x94ϞhoʏԬɋȧśǼӥҒԑϨÉēϪӇ˼êњШȍԖʛѧ҈Ҧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164112.013872:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x91Įť\x8cʵįϳɖҌϏƘΧLԓ˝ΛÎɩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'өŷœͱǒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Τӳɻ¶ӊ҂ķ˴ӶĽȲʃȉόҬШ\x8d\x9dŲƣиνӒӎİČЕз˺=',
                            'message': "ԨǄѽȭƄԈ\x99mƎԑÄϨĭќć'FùЁȡΡǥųѦíŕο˞\x97Ɯ",
                            'arguments': [
                                        {
                                                        'name': '\xa0Õ\u0378Ԫǋυ!ɼ°\x8aÞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛӲƝœТ˖ӄɓȎ˝ˋȐɊŠЁȂ8ƈЩџǠӺұϩӜƍ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "'Ɓҿ¨\x97ȱōŮǝӻĠʗĈʨəѴɄvƁэѫҗӬΣ\x8fŭƔѦВȩ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x9e\x92ȚɹŠtυÒκΐ,ǕŁé˃ӛÁˍǋӤʲ˫ǋÿё[Ąˁŕš',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĦҏωʔҁǁѭӅ\x94 ʠӽЏ˦',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 544903.3369567284,
                                                                        },
                                                    },
                                        {
                                                        'name': 'uƕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'EӽǗ;ɂˠћ˽ϧұƘϴԡи(ʮШȌюȩSϔИÛԪɣǰďҋӋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǾɒŞäHaΟĖ¢ԐƼʶǨïɾ˝ěϫˉ˃ΟʈÖʨп˘ҫŖǘͷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'υҺӓ˪ÉyԉÅіřȂм˷ӵόϡɯʗȮӾѻɘϠ\x9dȏԘҺǡĬҌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԞҢȹϩƱǁηˡ7қ¨ÆǲҖʬҋʿʼӒɏĚӸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164112.015646:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΞƔđDӒА¹ѡ\u038b',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x8dàŜ˨эq|юȠşхǱӹӚǬӴϺˀŚQ˼ϧ\x92ѿȌҧЇÛΎɞ',
                            'message': 'жǲ\x96ÓԃūεǙзɏòҵËԄϯ#ԃ\x82ЃĆїˉʇ˲@ӌѵĹßƀ',
                            'arguments': [
                                        {
                                                        'name': '+ƐԟΝěЕͺB#ПÖʽŔǉԦԔθʺύ;ȱϞŸƃ҆˳ǯҹϞӢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȼԑцоăϖӰЇɫлɦ\x9eȶą@ɶˣμπҞȶ͵ҹǔăԢĦǐΣŝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\xa0',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6067092619456174452,
                                                                        },
                                                    },
                                        {
                                                        'name': ')Ж^\u0381ȋӚϮlĒГӍɞҶȒkɔӘΆVӪŰȚɾȇҢӕͻі_y',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÏĵƫѧһÌɴȈNİɳИǲ\x9aϖˀǆѰzɐЛ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1456977567219680447,
                                                                        },
                                                    },
                                        {
                                                        'name': 'иɀƲǾŬʲ˫ҜΒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'яә˨°qǛбưԑ©ӧßͺȹҮq΅ɕĿ®ƢȨѓҦh*Ò',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164112.016922:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '¨ӒXдǼĄӶŵȸ\u0383\x9dјÇŢȰį9ȷɆɂŸ.ȈǆӥϟΈ}ƒ\u0383',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϥгɩϕгˠı9ƒȆŤТзåŷ©ʩƉsĀƁ˯ϱО˯ǜϠÁǨƩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'NƝƉпʷӾȿȐӞ¯Ўм\x93ˉăɐ˗өбӁƹ±ȮЈεƉˏɮԛŋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȉԩ\x8dѪιŤĉΛĘƆω@ƀԞ˱ѣċýČyԗ+лɳӼ˭ȦɰΟU',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164112.017349:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˦ҡЀϯѵȤĘ"ңϖɰǦӼУˑ$ϚɘɥŌţ8ґĪԥҐ˩ǝ±V',
                            'message': 'ГбҨʄΖӮȉЗˤȟϒtƮə\u0383ʷʘȉӖƶʠѧ8уɇÑěϲş˟',
                            'arguments': [
                                        {
                                                        'name': 'ȰѾϮÞΥc¹ÜӬғȟΕж³ĈӗǅļЋћ\x87',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſϫǘQ³ϹɛØˈȢÜǎ˼҈өʬƯʾɡì\x97Ŝuŧ<ǧμßiҎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗ\x92ϽϰʹӬʙӜ\x99ƺЍæʃƽƢȉHԏɡŞÅǨʳÚũ6ǞφVơ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'źˤʹ˂ļ˜ƩŝȉÁщ]ʺ˻ɨӨʩʹɌӠʃÌȿέԘ\u038dŒќɘҔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɞȐtʠηӪԬҚɜʹμͷF\u0378ʵʶőӱŲċĊəHʢţțҷyϘҊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '½˷āӺЃɛjʾȒˎĬ\xadvˌƓǥӈςʡǅ\x8e',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˣ\x99нÜӎӂ˂ϛϟԦԌ˱%ǨљʈҬŉȗԑȷӉҋЀкӴ°ˆ1Ų',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˹ÿˣЀsÉ˰§ʌôтѠʥŎƧ\x92ϫ\x8aƘҪƶβθš˞ŝʨO\x9dʷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʪЄäHц˰',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁҺ˰ʯƪhҕĝ\xa0',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -435358953527896149,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǼҶίËʼǨЂǊƨӷӴȪϖìѮτȺņΓŧӿǒʄȇáɣϱНś\u0382',
                            'message': 'ϙЪ^©\x8dϋ˫ϴƢǖ|\x89ʟϒϔ\u038bãϺӲ˧\x90ȲӜƯȩИϣӭѼû',
                            'arguments': [
                                        {
                                                        'name': 'ą\x8aɤť\x92ɔĪ˩ϧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ǵ÷ǧ˪l˚ʋҍ˝˭ϋÚÖӈӱ×ϞϜƯƏԎӯƸϴȏǢӉƂ5ӓ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¤ĢԀEť©ӕɵК@ӝʌãƾˮΔɘƻгϯq˟¹ƝěθˮĮÐè',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'л˝šЀ5țѻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164112.023376:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ß\x82ͺк\x9aҀ¸fͷȶīȿԫу˲įfƬȅʌĆΐÓϮϰɶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164112.023530:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʞdТ=¨ΨȔόȲЗƎ6¦ЊŢŽ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5830785918106572595,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x84ѥҤ¯άōŊıǫҟǶɌ϶ʄÎ[»\x8aŻΞƷçȃ¸ò˥ωŭ\x93ģ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6559620702443100327,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǳ¹ϴƘĪ^S|\x98҅ԥ\x91ʥÀѷ˷ƨӬ˖ªӚ¥ŨԈÅÖǞ2Ĝʵ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -65593.5723166904,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҿʜЙí˗ǉтӔѬsĸφщїƪύǣӃΦeέƨѩl˹ƩāӸΪф',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 832391.7390014472,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0381ɔϹQн1ͿƻȬʽѢҝ˛ѕǗĭЕʹǸɔʜȁɿʈgɑʻԄŪŀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧ8њųΫǩʕº',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 474022.2773455165,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӲƤrҰ˙˪ħůыҤˌΦʚʀ\x89oΗKЄΎрˮ\x95Ǩvƈˬе˳!',
                            'message': '{\x9eϩBJɖѣϾӿҗȪϟѠÊmŕÑҌɑȎͱƆαʆǜˊМѷѸХ',
                            'arguments': [
                                        {
                                                        'name': 'ƨяȭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҰҚƒЪNŇʥзʜӀҜɴƷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƙӡǒҫҒȥbǂʧЊğѾſő˼ƟƯˉÎ˂ѿĦʧƇһΏƴήʧp',
                                                                        },
                                                    },
                                        {
                                                        'name': '(dӹέ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 12728.607844679107,
                                                                        },
                                                    },
                                        {
                                                        'name': 'MѷӶȖϽƖͺ/Ä͵ЌrѶϷҿŐϗUИΚǓZÏҵƻӷͺΩҊS',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 119459.07909458518,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЭǞȄȧ\x8eǳʹ\x89ҋԄǳĽɂʵ˟БɍАʘΠ<ɱǐƙ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8937740566365970356,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȲϐԓјȝˣĞȉΎ\x9fǐPюÜΑƱˁșıÔԚƕʍԠǽЭǞƽԏɯ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґ˘ɯƪũȽȽϫъ\x8eΠʯȬƮ4ϤΐԖ3ǑŖ͵ҳӐƢ\x95ʶúɎO',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠȱųʍϽӶ˵˘ϫÍψаɮϴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'MӖұĨƼňȈŉƎ"Ѽû.ҰǷ˕Ѳ\x7fɸԑŷӃ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 795732.3487347685,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǱѫĚяϻ˦ήϴǂĖԠʫԈ\u0383ΑɛЖíӰÛԟɕгɳўɅѸѢɐũ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԧҥňǻ҈_ИϨ¿ӑҶ¡\x80ȩË͵ħҡ\x85Ɨ6ϹΥȏ ģϘ˔ťÿ',
                            'message': 'ИєʖƍќҦʶǲ˒˵ɻҜoǩҺȽƯǂήȴ˓Ѷҿ\x84ӾћїѩԨɨ',
                            'arguments': [
                                        {
                                                        'name': 'ƈőɋx˹Ƚ}',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӥ\x94\x92ˎнǭ˕ѠʂÌҌŽ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƽȺăӵ´ӺŢʯƎʴΧѿԘϝŉ\x87όìÈ˨Ǝѕϔ\u0379Ķӆó˗сь',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѸVĈţȝğáʡUƳΞʔη\u0378|Şʨ\x96?ӇҞõϴɼԩЁ˅',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɝљƚ¸ԨÜǗ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'МĐųВɀǉȆʡԙùҭðʘ\xadɰŏ˸˜ɿñɼƉΜ\x93ȦɢϺиϑɻ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɲ¸ĎӦ\x88ǩzĮʂ\x88āĝԈθ·ɡȸ¤ίÀĻôҬВW',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˳ǝƯϓ¶ȴƹȝӕɬʂϙǢԅŠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2109362995048908797,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ËƶɭŌÉkɂЄ,ʑèϋǖһɪɲȄИˮԚΒ\x89Г\u0378ԊǪӬɳȕŭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝɂөѷŝʅξĺϣ\x91ѿŚΕĸơшУżȐıŠđӠѽȕФҶßРȭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\xa0ˌú\x82ǰńǛԐэȎԩȺ\x9fӝГSє\u03a2ҹгӹ\u038b',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'à˶ǄѢμӆԠ˺ϾѳМдΫУȺȐҲª',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'óŝŋӏэϷГ˟АėȢʁєĈͲнʤÝ\x97ΕēɹΘ\x8a¿\u0380ҜӈϣΟ',
                            'message': 'ӓμϼǀǫġѪпɯҍϹȆĄѸƂԍͲ˝IƅуĖɉѢǫӖ҂ӟʎǂ',
                            'arguments': [
                                        {
                                                        'name': 'ŲưӪ˄ļԩɛϋǋĊԟҟӎȷƿЬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠɧёҌ˷ȂæԃƣϘӛ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 865243.6326725282,
                                                                        },
                                                    },
                                        {
                                                        'name': '©ǿӡτȊӐƿΠΪ˶ȌƦĈƓƳѵoŎөԭƔǿɵŜǫҬͲȔԔӡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 697357.2123259938,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ì',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8632876149567540512,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǲϾʹʵŝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -231328766933259059,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҋ\x93ϵ\x88ћşӕũӅȣТӀΐфѣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'пӑԧɟћ\u0380ҹǳ\u0380ǊόӁJ\x8dʿӚя\x81\\ŐҵSɠԁģҳʁĊԃˁ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӏǦҭȺԢȄԭЦ˓ñIЧɴҝ˴ϓƫƩƥģŚϨȞȁͻþԖƣī ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΪƠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164112.029434:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҕöśƻê',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 635931.8471800039,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Åȭèԗԇӿɮά¨ÿÃǔˎСģ˰ԛϊҔӨИƲʳӰƅʕÏɆӵò',
                            'message': 'ʺóǘğɼԁВƮ^l9Ҡ˭ʧҝʭ˦јΊΞć\u03a2ȾψЂаāʱɯӘ',
                            'arguments': [
                                        {
                                                        'name': 'ȀԨɒӽ7ʈƕàt0ԥȗҊÍʃԓǛƫˢƟҳ\x9eėɧӞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԊǬ`ȾѮӅ;Ȩ$×\u038dÑԩҙǢϧŨðȮłǸǝГǂʘşӆŞʔʺ',
                            'message': 'ǺɍӗñÐЖҡŨԛϟ3ИѨОƵȣКǂʟķ\x80·®ŝ\u038dʃǕʼ\x96Ů',
                            'arguments': [
                                        {
                                                        'name': 'ΏӔѥԠԊàȮϯ´Ó',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɛɷϠрήϫҖϢ·GӇРРŞƫæǃ\x87ҨɷñȌє{шɓŤoɺˉ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁҐɖ˻ӇӖƕΫȺȱˁĺһҡɭƚJOѽПŭѾϟ\x9cȃȬʾŵςǪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɺ)ͺřÊHҙŀэƙɲɔƑґαɹσʜƊǛǐΞǭƙӭҠӎ˾\x8cȘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˦ȹӆđǘÇȡύєҙǏĐǈы\x89ɫĵđ¢Ͼ҆ʃĒѪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϬƏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍӚQČʤҝØȡƳǦѓˏaҵǔƻɵOãƪÅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ίīϝ˚\x94ЂŊԃäԍęȀöʆĈȨőίäЄnþƪчӂԓўÒǊά',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕȩԣΡȇÚŋŌ*ϺƴҪʥҧАƃýmɘϫˏԚԃ˜˱βó@ѺϪ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɹ˗Êξɡ\x89´цĻ§ĎƫʰӑĀǲFǤ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164112.031580:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȔͷĐÜĩɴϤ@ʂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2289084824907824634,
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

            'request_id': 2957218,

            'error': {
                'identifier': 'Ɏʕǁϑε',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ʒұ',
                            'message': 'Z',
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
            'nw_x_pixel': 1369097501,
            'nw_y_pixel': 1913875710,
            'width': -1782303239565123578,
            'height': -3639840976818434658,
            'ratio_x': 3663975142365115850,
            'ratio_y': -236620875324821841,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 1360416386,

            'nw_y_pixel': 313034601,

            'width': -6470378939597132967,

            'height': -5952817303975472118,

            'ratio_x': -7021889265818858083,

            'ratio_y': -1337802545274385395,

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
                    'nw_x_pixel': 980054027,
                    'nw_y_pixel': -1737823457,
                    'width': -7561388426474631423,
                    'height': -4967305234075558031,
                    'ratio_x': 4940925967575429218,
                    'ratio_y': -7627468357746748446,
                },
                {
                    'nw_x_pixel': 648376707,
                    'nw_y_pixel': -899166837,
                    'width': -8785498582625086541,
                    'height': -4528864340009199033,
                    'ratio_x': -7454468313308516338,
                    'ratio_y': -3759158986910517750,
                },
                {
                    'nw_x_pixel': 1901414785,
                    'nw_y_pixel': -440313431,
                    'width': -4449122951923863601,
                    'height': -8675097770233086061,
                    'ratio_x': 4263202281706836161,
                    'ratio_y': -6966202368138821624,
                },
                {
                    'nw_x_pixel': -902164045,
                    'nw_y_pixel': 1085815292,
                    'width': -906065888924381382,
                    'height': -178786487366575071,
                    'ratio_x': 3430168672075884182,
                    'ratio_y': 5478464651225745566,
                },
                {
                    'nw_x_pixel': 1761161254,
                    'nw_y_pixel': 1746631933,
                    'width': -5576101131128803286,
                    'height': -8792844639166277069,
                    'ratio_x': 1619372954392254213,
                    'ratio_y': 1752306162696441507,
                },
                {
                    'nw_x_pixel': 1650412677,
                    'nw_y_pixel': -555917807,
                    'width': -5639719133116492958,
                    'height': -8902707692063939421,
                    'ratio_x': 9014554289257982331,
                    'ratio_y': 2208663642469425524,
                },
                {
                    'nw_x_pixel': -1397433237,
                    'nw_y_pixel': -1580417694,
                    'width': -30973855137186634,
                    'height': -6420306749318092543,
                    'ratio_x': 7893435331866226964,
                    'ratio_y': 2681340424610477206,
                },
                {
                    'nw_x_pixel': -1039663222,
                    'nw_y_pixel': 121314176,
                    'width': -2267622946678564514,
                    'height': -1297121368388922348,
                    'ratio_x': 6031193810867166748,
                    'ratio_y': -1971324749139259132,
                },
                {
                    'nw_x_pixel': 1286694999,
                    'nw_y_pixel': 961318411,
                    'width': -1205344768026568102,
                    'height': -4167239134735345300,
                    'ratio_x': -64118876987700374,
                    'ratio_y': 3857640348885875230,
                },
                {
                    'nw_x_pixel': 1434286160,
                    'nw_y_pixel': -1036713915,
                    'width': -5589025347993480592,
                    'height': -8273322204288084725,
                    'ratio_x': 3986727190774669790,
                    'ratio_y': 5156713795552463368,
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

class ConfigurationStateTest(unittest.TestCase):
    """
    Tests for ConfigurationState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.ConfigurationState.parse_data(test_data)
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
        for test_name, test_data in CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = screen.ConfigurationState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='mapped_screens_by_monitors', name='ConfigurationState'),
            ),

        ),
    ),

]


CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'mapped_screens_by_monitors': [
                {
                    'description': 'ԇȵǞȯŮϜʷ\x84ƿʾǦϳWÆ#ΫȨΝţȯǞʰƑϥ\u0379\u0379Øй˔ű',
                    'monitors': [
                            {
                                        'identifier': 3411079,
                                        'width': -1710393673489251513,
                                        'height': -2746204111599857183,
                                    },
                            {
                                        'identifier': 6138979,
                                        'width': 3477845061784165511,
                                        'height': 5762897998344508288,
                                    },
                            {
                                        'identifier': 2344083,
                                        'width': 3668463403503174313,
                                        'height': -4548870663293776220,
                                    },
                            {
                                        'identifier': -462738,
                                        'width': -6591439555900842545,
                                        'height': -1132925910627086088,
                                    },
                            {
                                        'identifier': 1626892,
                                        'width': -7244224730192946610,
                                        'height': -8413832450033906223,
                                    },
                            {
                                        'identifier': 1715800,
                                        'width': -202230012706972196,
                                        'height': 2312796364496680391,
                                    },
                            {
                                        'identifier': 4347240,
                                        'width': 3707265486274895742,
                                        'height': -6898060169541754681,
                                    },
                            {
                                        'identifier': 3609464,
                                        'width': 5024122667922504168,
                                        'height': -1039180833214673238,
                                    },
                            {
                                        'identifier': 1763900,
                                        'width': 5203028356541401529,
                                        'height': -7329746100885066643,
                                    },
                            {
                                        'identifier': 5202248,
                                        'width': -2750799515882336359,
                                        'height': -8186858191235998602,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -136180,
                                        'source_nw_x_pixel': -5936967689244830366,
                                        'source_nw_y_pixel': -4290832042378023559,
                                        'source_pixel_width': -4585729294536444053,
                                        'source_pixel_height': -6960884990583313192,
                                        'rotation': -5745537421822726392,
                                        'virtual_nw_x_pixel': -425205189,
                                        'virtual_nw_y_pixel': -1884885525,
                                        'virtual_width': 336475531,
                                        'virtual_height': -475409886,
                                    },
                            {
                                        'source_monitor': 3984351,
                                        'source_nw_x_pixel': -9109589217496134605,
                                        'source_nw_y_pixel': -8754493711752011719,
                                        'source_pixel_width': -3505765005708049195,
                                        'source_pixel_height': -5954745826828662371,
                                        'rotation': -3547647466980456341,
                                        'virtual_nw_x_pixel': -1208600390,
                                        'virtual_nw_y_pixel': -231295926,
                                        'virtual_width': 1126373637,
                                        'virtual_height': -427208661,
                                    },
                            {
                                        'source_monitor': 719761,
                                        'source_nw_x_pixel': -3834164176424989718,
                                        'source_nw_y_pixel': -1499369490046249257,
                                        'source_pixel_width': -8507886592358684837,
                                        'source_pixel_height': -5150838387942432656,
                                        'rotation': -4630490492261920883,
                                        'virtual_nw_x_pixel': 1087654824,
                                        'virtual_nw_y_pixel': -1884279802,
                                        'virtual_width': -240656295,
                                        'virtual_height': 1847032573,
                                    },
                            {
                                        'source_monitor': 1026407,
                                        'source_nw_x_pixel': -6699031158218419698,
                                        'source_nw_y_pixel': -8014109519629415084,
                                        'source_pixel_width': -1482459545572885765,
                                        'source_pixel_height': -6540158038345526875,
                                        'rotation': -3029102521867513046,
                                        'virtual_nw_x_pixel': -472110499,
                                        'virtual_nw_y_pixel': 1596388507,
                                        'virtual_width': 1759691443,
                                        'virtual_height': 832254597,
                                    },
                            {
                                        'source_monitor': 6357127,
                                        'source_nw_x_pixel': -3585529863547172310,
                                        'source_nw_y_pixel': -8059101005187874761,
                                        'source_pixel_width': -4194912572312764628,
                                        'source_pixel_height': -1307341323425302656,
                                        'rotation': -1327681739708448272,
                                        'virtual_nw_x_pixel': -781190308,
                                        'virtual_nw_y_pixel': -1165102183,
                                        'virtual_width': 621130111,
                                        'virtual_height': 407777078,
                                    },
                            {
                                        'source_monitor': 2554752,
                                        'source_nw_x_pixel': -2081037119133726242,
                                        'source_nw_y_pixel': -261224418717762848,
                                        'source_pixel_width': -2356783632838776500,
                                        'source_pixel_height': -6979371733036383399,
                                        'rotation': -4019860812884468315,
                                        'virtual_nw_x_pixel': -1318794510,
                                        'virtual_nw_y_pixel': 1120025135,
                                        'virtual_width': 1966533171,
                                        'virtual_height': 181643135,
                                    },
                            {
                                        'source_monitor': 482266,
                                        'source_nw_x_pixel': -8371422133577286008,
                                        'source_nw_y_pixel': -752381043647836918,
                                        'source_pixel_width': -2920033037463827551,
                                        'source_pixel_height': -6613583325694117546,
                                        'rotation': -372027950497574473,
                                        'virtual_nw_x_pixel': -1359166911,
                                        'virtual_nw_y_pixel': 1559779113,
                                        'virtual_width': -839919469,
                                        'virtual_height': -1657543308,
                                    },
                            {
                                        'source_monitor': 3785742,
                                        'source_nw_x_pixel': -1140384468306363542,
                                        'source_nw_y_pixel': -1784544886471448224,
                                        'source_pixel_width': -510843941005774720,
                                        'source_pixel_height': -4549641204609096070,
                                        'rotation': -1198012057997803963,
                                        'virtual_nw_x_pixel': 1617264922,
                                        'virtual_nw_y_pixel': -1380421165,
                                        'virtual_width': -1124696485,
                                        'virtual_height': 1110063854,
                                    },
                            {
                                        'source_monitor': 6821266,
                                        'source_nw_x_pixel': -6437340503541580619,
                                        'source_nw_y_pixel': -2091152198261764934,
                                        'source_pixel_width': -604869333629723592,
                                        'source_pixel_height': -5112584270615366115,
                                        'rotation': -4687124067000373743,
                                        'virtual_nw_x_pixel': -167061568,
                                        'virtual_nw_y_pixel': 465449276,
                                        'virtual_width': -901078932,
                                        'virtual_height': -1319082092,
                                    },
                            {
                                        'source_monitor': 8942229,
                                        'source_nw_x_pixel': -7325370784671390558,
                                        'source_nw_y_pixel': -3820542070678000750,
                                        'source_pixel_width': -1124725418739064251,
                                        'source_pixel_height': -8663747022289986193,
                                        'rotation': -9159874325389403416,
                                        'virtual_nw_x_pixel': -316273628,
                                        'virtual_nw_y_pixel': -1321213377,
                                        'virtual_width': 1641818631,
                                        'virtual_height': -1502681101,
                                    },
                        ],
                },
                {
                    'description': 'ӦΏԅ:ѦыǬ\xa0Ќ5ɜ˛ǕћɄŻӏөǅϯnӴҳ˾ӾõӥүÒʑ',
                    'monitors': [
                            {
                                        'identifier': 6308363,
                                        'width': -7919147070310685386,
                                        'height': -4276433678617245144,
                                    },
                            {
                                        'identifier': 2751938,
                                        'width': 9052193952629729408,
                                        'height': -8227838867739140127,
                                    },
                            {
                                        'identifier': 9247912,
                                        'width': -1068075539081910672,
                                        'height': -1630406355251744023,
                                    },
                            {
                                        'identifier': 7119507,
                                        'width': 9081141157880746802,
                                        'height': -5515047312995623576,
                                    },
                            {
                                        'identifier': 2914623,
                                        'width': 4417119427544692289,
                                        'height': 3086673933271287044,
                                    },
                            {
                                        'identifier': 3193787,
                                        'width': 1753811657753406807,
                                        'height': 4305149162262225320,
                                    },
                            {
                                        'identifier': 7927782,
                                        'width': 8768508991200101872,
                                        'height': 29102322447070573,
                                    },
                            {
                                        'identifier': 6314615,
                                        'width': -5088059993734387965,
                                        'height': -5214963475552806220,
                                    },
                            {
                                        'identifier': 872198,
                                        'width': 801137814217794984,
                                        'height': 6074644842541674732,
                                    },
                            {
                                        'identifier': 6199036,
                                        'width': 5721535996495456807,
                                        'height': -2028257025778639387,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1309104,
                                        'source_nw_x_pixel': -7005712734759684682,
                                        'source_nw_y_pixel': -4194372022945936863,
                                        'source_pixel_width': -7520794770037562415,
                                        'source_pixel_height': -3183714639847099805,
                                        'rotation': -5742245820338169602,
                                        'virtual_nw_x_pixel': 351711914,
                                        'virtual_nw_y_pixel': -37684339,
                                        'virtual_width': -1049218150,
                                        'virtual_height': -637036117,
                                    },
                            {
                                        'source_monitor': 4143169,
                                        'source_nw_x_pixel': -3329066459199971480,
                                        'source_nw_y_pixel': -4101867957793035224,
                                        'source_pixel_width': -4746437737029047062,
                                        'source_pixel_height': -5722752955735779884,
                                        'rotation': -6445398427824990455,
                                        'virtual_nw_x_pixel': 1079956785,
                                        'virtual_nw_y_pixel': 515289957,
                                        'virtual_width': -1646590490,
                                        'virtual_height': 725586831,
                                    },
                            {
                                        'source_monitor': 5948470,
                                        'source_nw_x_pixel': -7593653039118340781,
                                        'source_nw_y_pixel': -2647747147899131743,
                                        'source_pixel_width': -4215097706939543630,
                                        'source_pixel_height': -5076508509233658855,
                                        'rotation': -6325846108270783461,
                                        'virtual_nw_x_pixel': -1622616653,
                                        'virtual_nw_y_pixel': -1057871409,
                                        'virtual_width': -837042236,
                                        'virtual_height': 605749475,
                                    },
                            {
                                        'source_monitor': 8515652,
                                        'source_nw_x_pixel': -1021931088774321745,
                                        'source_nw_y_pixel': -4472697074704423806,
                                        'source_pixel_width': -1652610997283208989,
                                        'source_pixel_height': -7409559481914165064,
                                        'rotation': -2716859458485190973,
                                        'virtual_nw_x_pixel': -1454078070,
                                        'virtual_nw_y_pixel': 1771910536,
                                        'virtual_width': 1225677495,
                                        'virtual_height': -1788664166,
                                    },
                            {
                                        'source_monitor': 4403455,
                                        'source_nw_x_pixel': -1753679122350826827,
                                        'source_nw_y_pixel': -5981732794131962805,
                                        'source_pixel_width': -7617077438624799201,
                                        'source_pixel_height': -8245883565984990815,
                                        'rotation': -1177465685257202609,
                                        'virtual_nw_x_pixel': 592921709,
                                        'virtual_nw_y_pixel': -165783156,
                                        'virtual_width': 1537664638,
                                        'virtual_height': -1393134095,
                                    },
                            {
                                        'source_monitor': 8944855,
                                        'source_nw_x_pixel': -1016814363069264715,
                                        'source_nw_y_pixel': -2957644514805094636,
                                        'source_pixel_width': -8837621452242176962,
                                        'source_pixel_height': -4085630429566576220,
                                        'rotation': -6545572384063702631,
                                        'virtual_nw_x_pixel': -1444078198,
                                        'virtual_nw_y_pixel': -747485072,
                                        'virtual_width': 101425905,
                                        'virtual_height': 1330293978,
                                    },
                            {
                                        'source_monitor': 8647163,
                                        'source_nw_x_pixel': -5175795795154340478,
                                        'source_nw_y_pixel': -9115072736493022130,
                                        'source_pixel_width': -5975313276779947932,
                                        'source_pixel_height': -382197383225190187,
                                        'rotation': -3208668572525704418,
                                        'virtual_nw_x_pixel': 838554656,
                                        'virtual_nw_y_pixel': 1336101740,
                                        'virtual_width': -800468326,
                                        'virtual_height': -1415563552,
                                    },
                            {
                                        'source_monitor': -933385,
                                        'source_nw_x_pixel': -3584506015672075117,
                                        'source_nw_y_pixel': -4474568606474327866,
                                        'source_pixel_width': -4519815996259796458,
                                        'source_pixel_height': -1952135454570815993,
                                        'rotation': -524562190373828357,
                                        'virtual_nw_x_pixel': -342972875,
                                        'virtual_nw_y_pixel': 1281637326,
                                        'virtual_width': -1584967997,
                                        'virtual_height': 1526905676,
                                    },
                            {
                                        'source_monitor': -160911,
                                        'source_nw_x_pixel': -1928251454718295763,
                                        'source_nw_y_pixel': -8468004293695823281,
                                        'source_pixel_width': -7497931765060338164,
                                        'source_pixel_height': -7862589390908826851,
                                        'rotation': -2370237568327137857,
                                        'virtual_nw_x_pixel': 1563919938,
                                        'virtual_nw_y_pixel': -123138283,
                                        'virtual_width': -1178537962,
                                        'virtual_height': 169943783,
                                    },
                            {
                                        'source_monitor': 7956888,
                                        'source_nw_x_pixel': -7799091291895973389,
                                        'source_nw_y_pixel': -8660168330212893848,
                                        'source_pixel_width': -7900736160267306205,
                                        'source_pixel_height': -3501274614804316582,
                                        'rotation': -8818856518283975650,
                                        'virtual_nw_x_pixel': 1820141510,
                                        'virtual_nw_y_pixel': 84119343,
                                        'virtual_width': -1400898872,
                                        'virtual_height': -118145730,
                                    },
                        ],
                },
                {
                    'description': 'ϩʐяɷ˖п8ȱ˓ҰӎŔɭĞǷ\x83ґŹʝ',
                    'monitors': [
                            {
                                        'identifier': 3260529,
                                        'width': 4479520215551970036,
                                        'height': 3285079097513430107,
                                    },
                            {
                                        'identifier': 2053855,
                                        'width': 1155823084183564949,
                                        'height': 4472167681888424758,
                                    },
                            {
                                        'identifier': 5206637,
                                        'width': 9026917411302202115,
                                        'height': -7370276806671619443,
                                    },
                            {
                                        'identifier': 5089889,
                                        'width': -8187707782905504748,
                                        'height': 1753681236732718914,
                                    },
                            {
                                        'identifier': -31279,
                                        'width': 4422616462023391657,
                                        'height': 2605583854676605758,
                                    },
                            {
                                        'identifier': 3620308,
                                        'width': 3683359829194417424,
                                        'height': -4467843263049543119,
                                    },
                            {
                                        'identifier': 9183922,
                                        'width': 3726760670177134883,
                                        'height': -2135766461886454777,
                                    },
                            {
                                        'identifier': 9782241,
                                        'width': 170824135850439134,
                                        'height': -6056539019301264317,
                                    },
                            {
                                        'identifier': 5048480,
                                        'width': 8726916044212460764,
                                        'height': -1177936069959464392,
                                    },
                            {
                                        'identifier': 7823296,
                                        'width': 5244784593336760457,
                                        'height': -1714617993513894800,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3585204,
                                        'source_nw_x_pixel': -6403133464390366805,
                                        'source_nw_y_pixel': -3915155687349024220,
                                        'source_pixel_width': -435922561890880289,
                                        'source_pixel_height': -494086319762780493,
                                        'rotation': -717703491471195858,
                                        'virtual_nw_x_pixel': -1259300871,
                                        'virtual_nw_y_pixel': -1537524391,
                                        'virtual_width': 1085460206,
                                        'virtual_height': -472769751,
                                    },
                            {
                                        'source_monitor': 7734803,
                                        'source_nw_x_pixel': -6189599503917138225,
                                        'source_nw_y_pixel': -6834639087105010664,
                                        'source_pixel_width': -4776387695872619753,
                                        'source_pixel_height': -630121143697188202,
                                        'rotation': -1708650996626921992,
                                        'virtual_nw_x_pixel': -1586154020,
                                        'virtual_nw_y_pixel': 641400673,
                                        'virtual_width': 1836478790,
                                        'virtual_height': 236527873,
                                    },
                            {
                                        'source_monitor': 9757656,
                                        'source_nw_x_pixel': -5668502919013093935,
                                        'source_nw_y_pixel': -7306437721257590284,
                                        'source_pixel_width': -3021559412183139942,
                                        'source_pixel_height': -69533398319538414,
                                        'rotation': -5579862820333104061,
                                        'virtual_nw_x_pixel': 971924435,
                                        'virtual_nw_y_pixel': 856624230,
                                        'virtual_width': -709358965,
                                        'virtual_height': -1631235397,
                                    },
                            {
                                        'source_monitor': 7176815,
                                        'source_nw_x_pixel': -2878443124929445033,
                                        'source_nw_y_pixel': -4486157481322758793,
                                        'source_pixel_width': -6308780392622995488,
                                        'source_pixel_height': -8760563396975761727,
                                        'rotation': -378113266861333603,
                                        'virtual_nw_x_pixel': 235269113,
                                        'virtual_nw_y_pixel': 1478960655,
                                        'virtual_width': -1955871652,
                                        'virtual_height': -1930138005,
                                    },
                            {
                                        'source_monitor': 4243111,
                                        'source_nw_x_pixel': -4097835419412789170,
                                        'source_nw_y_pixel': -3153103467126585595,
                                        'source_pixel_width': -5330420038918967990,
                                        'source_pixel_height': -1097700889762464670,
                                        'rotation': -437615159046964628,
                                        'virtual_nw_x_pixel': -306161408,
                                        'virtual_nw_y_pixel': -1072073338,
                                        'virtual_width': -743192614,
                                        'virtual_height': 1498927080,
                                    },
                            {
                                        'source_monitor': -487962,
                                        'source_nw_x_pixel': -7847898165277971025,
                                        'source_nw_y_pixel': -1109215389046617125,
                                        'source_pixel_width': -7765229764548515337,
                                        'source_pixel_height': -6185308643846325665,
                                        'rotation': -5863795105984094839,
                                        'virtual_nw_x_pixel': 1149833219,
                                        'virtual_nw_y_pixel': -1842358458,
                                        'virtual_width': 753032557,
                                        'virtual_height': 1486591236,
                                    },
                            {
                                        'source_monitor': 6668748,
                                        'source_nw_x_pixel': -6327682388124160995,
                                        'source_nw_y_pixel': -4627177066444787544,
                                        'source_pixel_width': -3252470335088866359,
                                        'source_pixel_height': -2785667195991162861,
                                        'rotation': -3562696717559311347,
                                        'virtual_nw_x_pixel': -1046397583,
                                        'virtual_nw_y_pixel': -1481378679,
                                        'virtual_width': -1063566798,
                                        'virtual_height': 1335693830,
                                    },
                            {
                                        'source_monitor': 5002692,
                                        'source_nw_x_pixel': -5572329797251902168,
                                        'source_nw_y_pixel': -3534551975959929187,
                                        'source_pixel_width': -1996209833914429545,
                                        'source_pixel_height': -9047773953282395199,
                                        'rotation': -256063172976069648,
                                        'virtual_nw_x_pixel': -1912902235,
                                        'virtual_nw_y_pixel': -1336215959,
                                        'virtual_width': 925755417,
                                        'virtual_height': 1370352456,
                                    },
                            {
                                        'source_monitor': 8529852,
                                        'source_nw_x_pixel': -3352023402990278748,
                                        'source_nw_y_pixel': -2537241443407215435,
                                        'source_pixel_width': -1744285537780463965,
                                        'source_pixel_height': -3107552612416322360,
                                        'rotation': -1993163392596232538,
                                        'virtual_nw_x_pixel': 1214830965,
                                        'virtual_nw_y_pixel': -1016916606,
                                        'virtual_width': -1559537619,
                                        'virtual_height': 1283109602,
                                    },
                            {
                                        'source_monitor': 3237491,
                                        'source_nw_x_pixel': -3218437300429026952,
                                        'source_nw_y_pixel': -8726515228244640212,
                                        'source_pixel_width': -8176421337025495995,
                                        'source_pixel_height': -6394690303308235443,
                                        'rotation': -7723567921218282230,
                                        'virtual_nw_x_pixel': -1737903084,
                                        'virtual_nw_y_pixel': -765871602,
                                        'virtual_width': 1944851980,
                                        'virtual_height': 1175096049,
                                    },
                        ],
                },
                {
                    'description': '\x97ɽүǙӔΜØԜŖϼнəĵмΆǒ˦ҙĬͼϤ\x98ǌҩʿƉҹȾ©i',
                    'monitors': [
                            {
                                        'identifier': 7355161,
                                        'width': 8537978991489573859,
                                        'height': 7222112864399662353,
                                    },
                            {
                                        'identifier': 887906,
                                        'width': -6806319230650966501,
                                        'height': 2194581170512403315,
                                    },
                            {
                                        'identifier': 6291392,
                                        'width': 5089381694009722459,
                                        'height': 5072602612427386419,
                                    },
                            {
                                        'identifier': 672134,
                                        'width': 129201776461849287,
                                        'height': -4641544364177422258,
                                    },
                            {
                                        'identifier': 4324309,
                                        'width': 3350113077449891549,
                                        'height': -1417460756588925511,
                                    },
                            {
                                        'identifier': 8426250,
                                        'width': -6824482297894966776,
                                        'height': 4795984813623397312,
                                    },
                            {
                                        'identifier': 6506746,
                                        'width': -6987262788505792890,
                                        'height': 4328417343482057035,
                                    },
                            {
                                        'identifier': 294583,
                                        'width': -8599656625504190693,
                                        'height': 7434880461952984739,
                                    },
                            {
                                        'identifier': 4049714,
                                        'width': -955137318350831992,
                                        'height': -3034894694043557724,
                                    },
                            {
                                        'identifier': 6601535,
                                        'width': 4933254125782817392,
                                        'height': -3157655139394720449,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6507725,
                                        'source_nw_x_pixel': -3754407322683113653,
                                        'source_nw_y_pixel': -2868886588968284295,
                                        'source_pixel_width': -8622777342975803266,
                                        'source_pixel_height': -6995130636936077343,
                                        'rotation': -6377068075846306225,
                                        'virtual_nw_x_pixel': 194178691,
                                        'virtual_nw_y_pixel': -1523402566,
                                        'virtual_width': -1619691191,
                                        'virtual_height': 969036980,
                                    },
                            {
                                        'source_monitor': 1990051,
                                        'source_nw_x_pixel': -4790751964625447279,
                                        'source_nw_y_pixel': -949880657398695281,
                                        'source_pixel_width': -8428991951932595235,
                                        'source_pixel_height': -7866310743958632003,
                                        'rotation': -5074715588913270719,
                                        'virtual_nw_x_pixel': -1362931558,
                                        'virtual_nw_y_pixel': 358656740,
                                        'virtual_width': 796548790,
                                        'virtual_height': 462408477,
                                    },
                            {
                                        'source_monitor': 9169587,
                                        'source_nw_x_pixel': -5398968695810676637,
                                        'source_nw_y_pixel': -3092067932144169130,
                                        'source_pixel_width': -2442010982691721969,
                                        'source_pixel_height': -6721191357045867914,
                                        'rotation': -3860398881590821944,
                                        'virtual_nw_x_pixel': -1733589817,
                                        'virtual_nw_y_pixel': -958588681,
                                        'virtual_width': -1722901634,
                                        'virtual_height': -227490129,
                                    },
                            {
                                        'source_monitor': 475953,
                                        'source_nw_x_pixel': -2542676143597136446,
                                        'source_nw_y_pixel': -785129690626482221,
                                        'source_pixel_width': -8488009618111123789,
                                        'source_pixel_height': -3667537125673998518,
                                        'rotation': -4172961572043107142,
                                        'virtual_nw_x_pixel': 189754859,
                                        'virtual_nw_y_pixel': 1038516273,
                                        'virtual_width': -1647511593,
                                        'virtual_height': 799778925,
                                    },
                            {
                                        'source_monitor': 553720,
                                        'source_nw_x_pixel': -6727113792388015536,
                                        'source_nw_y_pixel': -8709159266379139438,
                                        'source_pixel_width': -2822848909825964612,
                                        'source_pixel_height': -5287051888947752733,
                                        'rotation': -6092639900538447343,
                                        'virtual_nw_x_pixel': -459263781,
                                        'virtual_nw_y_pixel': -1664548924,
                                        'virtual_width': -707428350,
                                        'virtual_height': 640348845,
                                    },
                            {
                                        'source_monitor': 8954708,
                                        'source_nw_x_pixel': -7252022282154755258,
                                        'source_nw_y_pixel': -3841868139824316583,
                                        'source_pixel_width': -737451637877395722,
                                        'source_pixel_height': -3331033907349009015,
                                        'rotation': -415449269785253442,
                                        'virtual_nw_x_pixel': 1671544340,
                                        'virtual_nw_y_pixel': 802257327,
                                        'virtual_width': -473853446,
                                        'virtual_height': 1452364031,
                                    },
                            {
                                        'source_monitor': 6339012,
                                        'source_nw_x_pixel': -3478186914368604916,
                                        'source_nw_y_pixel': -8969225295772316024,
                                        'source_pixel_width': -6323930706075816523,
                                        'source_pixel_height': -5276193842818250915,
                                        'rotation': -6655515860135580886,
                                        'virtual_nw_x_pixel': 1487074436,
                                        'virtual_nw_y_pixel': 1906344742,
                                        'virtual_width': -1618109846,
                                        'virtual_height': -797715374,
                                    },
                            {
                                        'source_monitor': 9000936,
                                        'source_nw_x_pixel': -6751603230222438827,
                                        'source_nw_y_pixel': -7807159949362360910,
                                        'source_pixel_width': -1400181695542126749,
                                        'source_pixel_height': -3987910531788832004,
                                        'rotation': -8295349455918303461,
                                        'virtual_nw_x_pixel': 358257221,
                                        'virtual_nw_y_pixel': -1344899504,
                                        'virtual_width': -72918875,
                                        'virtual_height': 381325904,
                                    },
                            {
                                        'source_monitor': 4679296,
                                        'source_nw_x_pixel': -1451963698054719504,
                                        'source_nw_y_pixel': -1905313916992954844,
                                        'source_pixel_width': -4498492106722083787,
                                        'source_pixel_height': -2076976592620779463,
                                        'rotation': -3866443191968047909,
                                        'virtual_nw_x_pixel': 384862980,
                                        'virtual_nw_y_pixel': 1931887949,
                                        'virtual_width': 1022179026,
                                        'virtual_height': -1450635256,
                                    },
                            {
                                        'source_monitor': 4212576,
                                        'source_nw_x_pixel': -7381761426196751989,
                                        'source_nw_y_pixel': -9118431002732104115,
                                        'source_pixel_width': -5779666171936563963,
                                        'source_pixel_height': -7607678542816605502,
                                        'rotation': -6474909318628261990,
                                        'virtual_nw_x_pixel': -1166649048,
                                        'virtual_nw_y_pixel': 5121868,
                                        'virtual_width': -630487637,
                                        'virtual_height': 657339499,
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
                                        'identifier': 1671991,
                                        'width': 5730171640018884328,
                                        'height': 695879640402038399,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -8418537247081219156,
                                        'source_nw_y_pixel': -1835753324316817555,
                                        'source_pixel_width': -1898384958150513496,
                                        'source_pixel_height': -7410517947951799129,
                                        'rotation': -9009231790791447418,
                                        'virtual_nw_x_pixel': -656229711,
                                        'virtual_nw_y_pixel': 788661805,
                                        'virtual_width': -1402519523,
                                        'virtual_height': -263518699,
                                    },
                        ],
                },
            ],

        },
    ),
]
