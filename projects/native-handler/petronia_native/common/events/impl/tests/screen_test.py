# GENERATED CODE - DO NOT MODIFY

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
            'identifier': 6652370,
            'width': -1768614077007651586,
            'height': 5096509092568630555,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 2320603,

            'width': -6098765058356678834,

            'height': 3152563001612329545,

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
            'source_monitor': 2544783,
            'source_nw_x_pixel': -5619351501517121734,
            'source_nw_y_pixel': -3761451093523979427,
            'source_pixel_width': -7180020256606555186,
            'source_pixel_height': -1659322333732449239,
            'rotation': -9065873527994350813,
            'virtual_nw_x_pixel': -1570275924,
            'virtual_nw_y_pixel': 458845792,
            'virtual_width': 1325065340,
            'virtual_height': 1679038523,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -1858368279122452758,

            'source_nw_y_pixel': -3032238068579070017,

            'source_pixel_width': -9141950732854580592,

            'source_pixel_height': -1415900569863260182,

            'rotation': -4557807391779160702,

            'virtual_nw_x_pixel': -398235185,

            'virtual_nw_y_pixel': 1596185310,

            'virtual_width': 1802747076,

            'virtual_height': 1442108644,

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
            'description': 'ʟԥĢ\u038d˃\x97уĈĜƕϒğʁοŮĤǀ\u0379ҺýҶˬĢӏȥ`ÁэХǔ',
            'monitors': [
                {
                    'identifier': -704816,
                    'width': -977991171627453669,
                    'height': -3254641902605004596,
                },
                {
                    'identifier': 2467063,
                    'width': 8271854604050371139,
                    'height': -5056272862878224004,
                },
                {
                    'identifier': 3008775,
                    'width': 7042585183460934443,
                    'height': -8555874721041308369,
                },
                {
                    'identifier': 1565496,
                    'width': -554977857688516399,
                    'height': 6363849867846586060,
                },
                {
                    'identifier': 5604168,
                    'width': 5843008510515833485,
                    'height': 2662539532797965559,
                },
                {
                    'identifier': 9821550,
                    'width': -4904817480221095848,
                    'height': -6473588750081729615,
                },
                {
                    'identifier': 1607296,
                    'width': -990029476914903774,
                    'height': 62736405017446734,
                },
                {
                    'identifier': 3808969,
                    'width': 1526788094224131435,
                    'height': -2856561192852201430,
                },
                {
                    'identifier': -605477,
                    'width': -3936381582040179809,
                    'height': 1275072219723729382,
                },
                {
                    'identifier': 4476226,
                    'width': -5083312700903903447,
                    'height': -4830655623306654705,
                },
            ],
            'screen': [
                {
                    'source_monitor': 6076739,
                    'source_nw_x_pixel': -2530429646643623080,
                    'source_nw_y_pixel': -6740887992152663587,
                    'source_pixel_width': -6289763852185980443,
                    'source_pixel_height': -7923145766812801551,
                    'rotation': -7680921851368245729,
                    'virtual_nw_x_pixel': -412045532,
                    'virtual_nw_y_pixel': 287932192,
                    'virtual_width': -1869477927,
                    'virtual_height': -1541187282,
                },
                {
                    'source_monitor': 9078806,
                    'source_nw_x_pixel': -4097073478125802209,
                    'source_nw_y_pixel': -4591170028911069189,
                    'source_pixel_width': -6242694399984666969,
                    'source_pixel_height': -4965450023333974420,
                    'rotation': -1437335205691575145,
                    'virtual_nw_x_pixel': -860104347,
                    'virtual_nw_y_pixel': 1635447032,
                    'virtual_width': 1594919886,
                    'virtual_height': 15180142,
                },
                {
                    'source_monitor': 53716,
                    'source_nw_x_pixel': -852746046303279658,
                    'source_nw_y_pixel': -8586755007083250906,
                    'source_pixel_width': -8805735166530717927,
                    'source_pixel_height': -2359775134314869891,
                    'rotation': -7699806584386749651,
                    'virtual_nw_x_pixel': 1805882129,
                    'virtual_nw_y_pixel': -361880770,
                    'virtual_width': 998194777,
                    'virtual_height': -470580354,
                },
                {
                    'source_monitor': 1500653,
                    'source_nw_x_pixel': -5141784264113020842,
                    'source_nw_y_pixel': -2039686128009081406,
                    'source_pixel_width': -6381109481882611687,
                    'source_pixel_height': -1628362057088873389,
                    'rotation': -8230577013849259498,
                    'virtual_nw_x_pixel': -345484311,
                    'virtual_nw_y_pixel': -1580951972,
                    'virtual_width': -1293072750,
                    'virtual_height': 1675636300,
                },
                {
                    'source_monitor': 1744518,
                    'source_nw_x_pixel': -6024279441420335555,
                    'source_nw_y_pixel': -5588568947262991172,
                    'source_pixel_width': -5052824709074094260,
                    'source_pixel_height': -4461960566975229869,
                    'rotation': -7845067483057863156,
                    'virtual_nw_x_pixel': 284136316,
                    'virtual_nw_y_pixel': 340496219,
                    'virtual_width': -394197782,
                    'virtual_height': -634815363,
                },
                {
                    'source_monitor': 9946947,
                    'source_nw_x_pixel': -2139856880034404693,
                    'source_nw_y_pixel': -2257618917683286574,
                    'source_pixel_width': -1155569483176005760,
                    'source_pixel_height': -4564209184088815054,
                    'rotation': -6847254316824077090,
                    'virtual_nw_x_pixel': -1617716885,
                    'virtual_nw_y_pixel': 1036617955,
                    'virtual_width': -1912398237,
                    'virtual_height': 1809825849,
                },
                {
                    'source_monitor': 6667063,
                    'source_nw_x_pixel': -9199707612863615091,
                    'source_nw_y_pixel': -1173991959946952770,
                    'source_pixel_width': -1325520402388514798,
                    'source_pixel_height': -7211813437831819303,
                    'rotation': -6576380419031460296,
                    'virtual_nw_x_pixel': -1484337866,
                    'virtual_nw_y_pixel': -1599074535,
                    'virtual_width': 1262942450,
                    'virtual_height': -1879087954,
                },
                {
                    'source_monitor': 4862128,
                    'source_nw_x_pixel': -1816067937343255760,
                    'source_nw_y_pixel': -2782470325478301080,
                    'source_pixel_width': -3377150682509942906,
                    'source_pixel_height': -6002252261523775236,
                    'rotation': -5121467281232765864,
                    'virtual_nw_x_pixel': 635356384,
                    'virtual_nw_y_pixel': -1068469353,
                    'virtual_width': 585376905,
                    'virtual_height': 1866825710,
                },
                {
                    'source_monitor': 9002317,
                    'source_nw_x_pixel': -8567036791328884314,
                    'source_nw_y_pixel': -181212532979574362,
                    'source_pixel_width': -8271807635688744607,
                    'source_pixel_height': -5233019419641217577,
                    'rotation': -5879097163566095943,
                    'virtual_nw_x_pixel': -1473534823,
                    'virtual_nw_y_pixel': -783641019,
                    'virtual_width': -1687398956,
                    'virtual_height': -1793168407,
                },
                {
                    'source_monitor': 1086116,
                    'source_nw_x_pixel': -6338857872926638967,
                    'source_nw_y_pixel': -6098324688159158892,
                    'source_pixel_width': -3526216463209754213,
                    'source_pixel_height': -5686396699360160923,
                    'rotation': -517074916657715638,
                    'virtual_nw_x_pixel': -1247510418,
                    'virtual_nw_y_pixel': -1886079729,
                    'virtual_width': -1664283284,
                    'virtual_height': 722819034,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 7997105,
                    'width': -7777965178344825704,
                    'height': -1298632325562980492,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -4938911585478512791,
                    'source_nw_y_pixel': -8562040210986937003,
                    'source_pixel_width': -3920072046571377269,
                    'source_pixel_height': -467168101024322588,
                    'rotation': -224377512967660046,
                    'virtual_nw_x_pixel': -1412639789,
                    'virtual_nw_y_pixel': 756966603,
                    'virtual_width': 1345595860,
                    'virtual_height': -1312736498,
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
            'request_id': 8168262,
            'mapped_screens_by_monitors': [
                {
                    'description': '˱ɘѫʛȾʙǆӛԠńŝ˭ʭUƷӴ{\xadųsɽΖѲȋĹ˩ϣЉЗή',
                    'monitors': [
                            {
                                        'identifier': 8619280,
                                        'width': 1143116705146560445,
                                        'height': -6055750761897858710,
                                    },
                            {
                                        'identifier': -64186,
                                        'width': -7984757198006814382,
                                        'height': 3560655820924026518,
                                    },
                            {
                                        'identifier': 4695552,
                                        'width': 9036849994078944059,
                                        'height': -7362491935487665807,
                                    },
                            {
                                        'identifier': -87015,
                                        'width': 5618158901466885633,
                                        'height': 5189260075208225697,
                                    },
                            {
                                        'identifier': 1728015,
                                        'width': -7587162221347500575,
                                        'height': 8493265637146142912,
                                    },
                            {
                                        'identifier': 6052512,
                                        'width': -3266268666925209208,
                                        'height': -2669230295084464654,
                                    },
                            {
                                        'identifier': 2823959,
                                        'width': 65899081369684473,
                                        'height': -8888536159252324422,
                                    },
                            {
                                        'identifier': 85202,
                                        'width': 4316864209220813747,
                                        'height': 3135651564825160117,
                                    },
                            {
                                        'identifier': 6878793,
                                        'width': -8308222644713057587,
                                        'height': -6158881002636869482,
                                    },
                            {
                                        'identifier': 7187603,
                                        'width': -2082936552773573153,
                                        'height': -3827938111304681651,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8019488,
                                        'source_nw_x_pixel': -611105221682459133,
                                        'source_nw_y_pixel': -1685630137740172094,
                                        'source_pixel_width': -8006451297068818516,
                                        'source_pixel_height': -845605250301228561,
                                        'rotation': -1430649529160162182,
                                        'virtual_nw_x_pixel': 1471249542,
                                        'virtual_nw_y_pixel': 117365419,
                                        'virtual_width': 1944552046,
                                        'virtual_height': 248709988,
                                    },
                            {
                                        'source_monitor': 9624798,
                                        'source_nw_x_pixel': -5841970128787448572,
                                        'source_nw_y_pixel': -2696971430484839480,
                                        'source_pixel_width': -6519316820286902137,
                                        'source_pixel_height': -7568294329240322198,
                                        'rotation': -3033777330975689002,
                                        'virtual_nw_x_pixel': -94599264,
                                        'virtual_nw_y_pixel': 306083352,
                                        'virtual_width': 832298957,
                                        'virtual_height': 1188528138,
                                    },
                            {
                                        'source_monitor': 8045326,
                                        'source_nw_x_pixel': -3629995965037211348,
                                        'source_nw_y_pixel': -3311186864581066126,
                                        'source_pixel_width': -5875656450189585561,
                                        'source_pixel_height': -3383234066332074769,
                                        'rotation': -3290127843428121247,
                                        'virtual_nw_x_pixel': -1972436401,
                                        'virtual_nw_y_pixel': 828489418,
                                        'virtual_width': 1005300075,
                                        'virtual_height': -851835771,
                                    },
                            {
                                        'source_monitor': 1511995,
                                        'source_nw_x_pixel': -3634539911899776349,
                                        'source_nw_y_pixel': -3360237288944547095,
                                        'source_pixel_width': -1333595747827827843,
                                        'source_pixel_height': -1248722449487154031,
                                        'rotation': -2509149670777088986,
                                        'virtual_nw_x_pixel': 560211712,
                                        'virtual_nw_y_pixel': -470087644,
                                        'virtual_width': -1031051822,
                                        'virtual_height': -616399301,
                                    },
                            {
                                        'source_monitor': 856518,
                                        'source_nw_x_pixel': -6325133116515134833,
                                        'source_nw_y_pixel': -4146377241428675612,
                                        'source_pixel_width': -7814966740667425592,
                                        'source_pixel_height': -2540162727674628423,
                                        'rotation': -3355425888215833566,
                                        'virtual_nw_x_pixel': 1999815150,
                                        'virtual_nw_y_pixel': -411948615,
                                        'virtual_width': -1373844091,
                                        'virtual_height': 1926908032,
                                    },
                            {
                                        'source_monitor': 5910606,
                                        'source_nw_x_pixel': -4697829438912723239,
                                        'source_nw_y_pixel': -7864339366012720443,
                                        'source_pixel_width': -7363697438799845195,
                                        'source_pixel_height': -4646922833879041489,
                                        'rotation': -5265830475574168965,
                                        'virtual_nw_x_pixel': 794132513,
                                        'virtual_nw_y_pixel': 1046332553,
                                        'virtual_width': -1056535644,
                                        'virtual_height': -126743447,
                                    },
                            {
                                        'source_monitor': 1111015,
                                        'source_nw_x_pixel': -1705123822365622817,
                                        'source_nw_y_pixel': -1649017428799016737,
                                        'source_pixel_width': -7598583767139743960,
                                        'source_pixel_height': -285832885167975518,
                                        'rotation': -1274666593407714170,
                                        'virtual_nw_x_pixel': -1673368947,
                                        'virtual_nw_y_pixel': -1415211945,
                                        'virtual_width': 1988577170,
                                        'virtual_height': 1389962647,
                                    },
                            {
                                        'source_monitor': 3504367,
                                        'source_nw_x_pixel': -6248760118510251766,
                                        'source_nw_y_pixel': -2336446835272798444,
                                        'source_pixel_width': -6037590425943856144,
                                        'source_pixel_height': -6481029037895471490,
                                        'rotation': -9013924264382401269,
                                        'virtual_nw_x_pixel': -737392747,
                                        'virtual_nw_y_pixel': 131565839,
                                        'virtual_width': 351983070,
                                        'virtual_height': 1158900585,
                                    },
                            {
                                        'source_monitor': 5466722,
                                        'source_nw_x_pixel': -4327950557800347904,
                                        'source_nw_y_pixel': -5707855758579717086,
                                        'source_pixel_width': -8632333717442696108,
                                        'source_pixel_height': -8191358674258242013,
                                        'rotation': -215750207827456598,
                                        'virtual_nw_x_pixel': -1514142797,
                                        'virtual_nw_y_pixel': 24703326,
                                        'virtual_width': -1095934785,
                                        'virtual_height': 449178765,
                                    },
                            {
                                        'source_monitor': -553910,
                                        'source_nw_x_pixel': -6215112379556327044,
                                        'source_nw_y_pixel': -312758166716694811,
                                        'source_pixel_width': -6043758866999080398,
                                        'source_pixel_height': -7168718219009040057,
                                        'rotation': -5325246009523678605,
                                        'virtual_nw_x_pixel': -116894286,
                                        'virtual_nw_y_pixel': 1698337178,
                                        'virtual_width': 1575373725,
                                        'virtual_height': -522209642,
                                    },
                        ],
                },
                {
                    'description': '\u03a2fѥԋξǷºÅԇεȧϤȅžȬęΣѺ\x80µЉͷɑ΅EӨ.ƫ˦Χ',
                    'monitors': [
                            {
                                        'identifier': 7245912,
                                        'width': 5898850199344176083,
                                        'height': 6620401307341768117,
                                    },
                            {
                                        'identifier': -950852,
                                        'width': -3853640883379801029,
                                        'height': 6538931039507894998,
                                    },
                            {
                                        'identifier': 6680114,
                                        'width': 9196307721143354918,
                                        'height': 3840284946451219457,
                                    },
                            {
                                        'identifier': 6474094,
                                        'width': 6544748357200613236,
                                        'height': -7767058175814776951,
                                    },
                            {
                                        'identifier': 3816541,
                                        'width': -8212139933613875445,
                                        'height': 4505507768884877055,
                                    },
                            {
                                        'identifier': 2343080,
                                        'width': -3857853394341459616,
                                        'height': 7157646171488786521,
                                    },
                            {
                                        'identifier': 9246220,
                                        'width': 7033831856817589946,
                                        'height': 5444808717801658580,
                                    },
                            {
                                        'identifier': 9708821,
                                        'width': -7410553871628823701,
                                        'height': 7275775589619881305,
                                    },
                            {
                                        'identifier': 8721977,
                                        'width': 6688161147083927670,
                                        'height': 6628927910123564426,
                                    },
                            {
                                        'identifier': 2546456,
                                        'width': 2823427310454555889,
                                        'height': -9070314114541024208,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 395476,
                                        'source_nw_x_pixel': -5307545093256266405,
                                        'source_nw_y_pixel': -4184093291984194116,
                                        'source_pixel_width': -3721276669575723041,
                                        'source_pixel_height': -5803572291277719682,
                                        'rotation': -5834807740363957409,
                                        'virtual_nw_x_pixel': -398329508,
                                        'virtual_nw_y_pixel': -206780609,
                                        'virtual_width': -919582404,
                                        'virtual_height': -894492057,
                                    },
                            {
                                        'source_monitor': -686545,
                                        'source_nw_x_pixel': -5224578122933721205,
                                        'source_nw_y_pixel': -6898761605540806767,
                                        'source_pixel_width': -5438262963379017095,
                                        'source_pixel_height': -8532406433189899141,
                                        'rotation': -6594095219659005477,
                                        'virtual_nw_x_pixel': 910060668,
                                        'virtual_nw_y_pixel': -483808641,
                                        'virtual_width': 457074034,
                                        'virtual_height': 1089209040,
                                    },
                            {
                                        'source_monitor': -274405,
                                        'source_nw_x_pixel': -9128469645902223146,
                                        'source_nw_y_pixel': -1918359211395295586,
                                        'source_pixel_width': -177610286330127996,
                                        'source_pixel_height': -6065929935291018929,
                                        'rotation': -9014832309718784349,
                                        'virtual_nw_x_pixel': 1155779945,
                                        'virtual_nw_y_pixel': -1675726736,
                                        'virtual_width': -171270587,
                                        'virtual_height': 1217375899,
                                    },
                            {
                                        'source_monitor': 7076398,
                                        'source_nw_x_pixel': -222751967741679985,
                                        'source_nw_y_pixel': -7596954434692902689,
                                        'source_pixel_width': -1871026949726244581,
                                        'source_pixel_height': -116050198092766323,
                                        'rotation': -7216077846202958877,
                                        'virtual_nw_x_pixel': -842226298,
                                        'virtual_nw_y_pixel': -1763388279,
                                        'virtual_width': -140763603,
                                        'virtual_height': 328560629,
                                    },
                            {
                                        'source_monitor': 3290242,
                                        'source_nw_x_pixel': -4207410489950781162,
                                        'source_nw_y_pixel': -2342094813250637784,
                                        'source_pixel_width': -752834989874264915,
                                        'source_pixel_height': -7923260747373050856,
                                        'rotation': -1298607692898210811,
                                        'virtual_nw_x_pixel': -1595192432,
                                        'virtual_nw_y_pixel': -103818635,
                                        'virtual_width': 602930785,
                                        'virtual_height': 1274296586,
                                    },
                            {
                                        'source_monitor': 6477462,
                                        'source_nw_x_pixel': -8060099403979900816,
                                        'source_nw_y_pixel': -4197640956911285414,
                                        'source_pixel_width': -822725535966899125,
                                        'source_pixel_height': -1298767638195810004,
                                        'rotation': -2457013993732344800,
                                        'virtual_nw_x_pixel': 231622689,
                                        'virtual_nw_y_pixel': 696194408,
                                        'virtual_width': 925785558,
                                        'virtual_height': 1129958651,
                                    },
                            {
                                        'source_monitor': 987275,
                                        'source_nw_x_pixel': -1681675351643008420,
                                        'source_nw_y_pixel': -3197327249449550334,
                                        'source_pixel_width': -3963835937049443642,
                                        'source_pixel_height': -2691551306267634133,
                                        'rotation': -2740618892319171971,
                                        'virtual_nw_x_pixel': -393616086,
                                        'virtual_nw_y_pixel': -193866491,
                                        'virtual_width': 162182427,
                                        'virtual_height': 19161182,
                                    },
                            {
                                        'source_monitor': -383425,
                                        'source_nw_x_pixel': -8839515625797319031,
                                        'source_nw_y_pixel': -8901603152867202564,
                                        'source_pixel_width': -6796590775866824365,
                                        'source_pixel_height': -9134624836616529111,
                                        'rotation': -6695495048678401781,
                                        'virtual_nw_x_pixel': 1601979730,
                                        'virtual_nw_y_pixel': -772989350,
                                        'virtual_width': -699632664,
                                        'virtual_height': -508866657,
                                    },
                            {
                                        'source_monitor': 7704155,
                                        'source_nw_x_pixel': -3593512042619412119,
                                        'source_nw_y_pixel': -2969417462301748642,
                                        'source_pixel_width': -6733970102128040142,
                                        'source_pixel_height': -6412633554896238911,
                                        'rotation': -9180100138924206880,
                                        'virtual_nw_x_pixel': 753256548,
                                        'virtual_nw_y_pixel': -1985487039,
                                        'virtual_width': 936185733,
                                        'virtual_height': 214262009,
                                    },
                            {
                                        'source_monitor': 3314151,
                                        'source_nw_x_pixel': -7665224203642741997,
                                        'source_nw_y_pixel': -6115976529934069999,
                                        'source_pixel_width': -1226897380139143223,
                                        'source_pixel_height': -6133531175501156601,
                                        'rotation': -6325569558153198177,
                                        'virtual_nw_x_pixel': 269884950,
                                        'virtual_nw_y_pixel': 1288015065,
                                        'virtual_width': 1980408304,
                                        'virtual_height': -631540201,
                                    },
                        ],
                },
                {
                    'description': 'ԁɶԇȩͳaӼќ·ҟJæÈӨĠҚŭ˯żYӻϱʳϜԄƳɭðƶʩ',
                    'monitors': [
                            {
                                        'identifier': 8730700,
                                        'width': 3304937251368888136,
                                        'height': -1702477061690794647,
                                    },
                            {
                                        'identifier': 5848925,
                                        'width': -3555537928094607265,
                                        'height': -797206479230715237,
                                    },
                            {
                                        'identifier': 3981402,
                                        'width': -7306849604251448338,
                                        'height': -3115978111006320844,
                                    },
                            {
                                        'identifier': 6731986,
                                        'width': 8895192094264305050,
                                        'height': 2017838475064187073,
                                    },
                            {
                                        'identifier': 7447658,
                                        'width': -5631400124737661841,
                                        'height': -7207097406339446585,
                                    },
                            {
                                        'identifier': 4444879,
                                        'width': -6288787351561423571,
                                        'height': -3112454626267224525,
                                    },
                            {
                                        'identifier': 9084265,
                                        'width': 2303262866619195607,
                                        'height': -2982818250246681193,
                                    },
                            {
                                        'identifier': 6267743,
                                        'width': -1433637412947927098,
                                        'height': 400225243772856837,
                                    },
                            {
                                        'identifier': 4160717,
                                        'width': 6919188600040362659,
                                        'height': 6577613864721221108,
                                    },
                            {
                                        'identifier': 7301233,
                                        'width': 7318573695323463199,
                                        'height': -8268336419024017486,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2669224,
                                        'source_nw_x_pixel': -3900497015834803047,
                                        'source_nw_y_pixel': -8160603010541808873,
                                        'source_pixel_width': -3116832887814266138,
                                        'source_pixel_height': -8154405355260489419,
                                        'rotation': -3655977117179127516,
                                        'virtual_nw_x_pixel': -1704738048,
                                        'virtual_nw_y_pixel': 50580405,
                                        'virtual_width': -1946438392,
                                        'virtual_height': 8501092,
                                    },
                            {
                                        'source_monitor': 8096178,
                                        'source_nw_x_pixel': -3299423031278993999,
                                        'source_nw_y_pixel': -2226846490616664565,
                                        'source_pixel_width': -5955514951645954858,
                                        'source_pixel_height': -5219795657987378436,
                                        'rotation': -750246953571471240,
                                        'virtual_nw_x_pixel': -720151737,
                                        'virtual_nw_y_pixel': 591656006,
                                        'virtual_width': -1044992099,
                                        'virtual_height': 835084693,
                                    },
                            {
                                        'source_monitor': 1806260,
                                        'source_nw_x_pixel': -385198950115191958,
                                        'source_nw_y_pixel': -7577924523850015628,
                                        'source_pixel_width': -2917441162274658738,
                                        'source_pixel_height': -8147237131678985268,
                                        'rotation': -3986475383519773354,
                                        'virtual_nw_x_pixel': -1432960013,
                                        'virtual_nw_y_pixel': 1808362780,
                                        'virtual_width': -532790108,
                                        'virtual_height': 1205499506,
                                    },
                            {
                                        'source_monitor': 6271920,
                                        'source_nw_x_pixel': -5223626797332355686,
                                        'source_nw_y_pixel': -8723092960179180345,
                                        'source_pixel_width': -1110284380657361360,
                                        'source_pixel_height': -4408269782030022018,
                                        'rotation': -2808826491651772324,
                                        'virtual_nw_x_pixel': 1864989916,
                                        'virtual_nw_y_pixel': 1407663158,
                                        'virtual_width': 1565750678,
                                        'virtual_height': 553815435,
                                    },
                            {
                                        'source_monitor': 5996509,
                                        'source_nw_x_pixel': -3608666420816160393,
                                        'source_nw_y_pixel': -60269070208271093,
                                        'source_pixel_width': -2603149875749533100,
                                        'source_pixel_height': -7628394510289332231,
                                        'rotation': -2930945556106847155,
                                        'virtual_nw_x_pixel': 210256980,
                                        'virtual_nw_y_pixel': 947806583,
                                        'virtual_width': 515539042,
                                        'virtual_height': -1034806808,
                                    },
                            {
                                        'source_monitor': 2037184,
                                        'source_nw_x_pixel': -6476022927910939639,
                                        'source_nw_y_pixel': -2031445265351360979,
                                        'source_pixel_width': -1761371486678280904,
                                        'source_pixel_height': -4615819320342448422,
                                        'rotation': -4788105883633823620,
                                        'virtual_nw_x_pixel': -1496396828,
                                        'virtual_nw_y_pixel': 1306634766,
                                        'virtual_width': -1837302534,
                                        'virtual_height': -1319552236,
                                    },
                            {
                                        'source_monitor': 6312535,
                                        'source_nw_x_pixel': -7770330266850914201,
                                        'source_nw_y_pixel': -5748212826164556658,
                                        'source_pixel_width': -3751167898032582228,
                                        'source_pixel_height': -22874454524529450,
                                        'rotation': -4676204088146323805,
                                        'virtual_nw_x_pixel': 1484256178,
                                        'virtual_nw_y_pixel': 128904313,
                                        'virtual_width': 276330682,
                                        'virtual_height': 224628255,
                                    },
                            {
                                        'source_monitor': 596010,
                                        'source_nw_x_pixel': -1977766836386687256,
                                        'source_nw_y_pixel': -4939668019003100022,
                                        'source_pixel_width': -4644918757929032381,
                                        'source_pixel_height': -703925136604854774,
                                        'rotation': -8423457477654201146,
                                        'virtual_nw_x_pixel': -673500232,
                                        'virtual_nw_y_pixel': -800758671,
                                        'virtual_width': -285612176,
                                        'virtual_height': -749182272,
                                    },
                            {
                                        'source_monitor': 102753,
                                        'source_nw_x_pixel': -7654579733415478110,
                                        'source_nw_y_pixel': -6162971519616633175,
                                        'source_pixel_width': -3666669406749927411,
                                        'source_pixel_height': -6749654144151763286,
                                        'rotation': -5396723915211614604,
                                        'virtual_nw_x_pixel': -1922148226,
                                        'virtual_nw_y_pixel': 953534282,
                                        'virtual_width': 347296114,
                                        'virtual_height': -297281721,
                                    },
                            {
                                        'source_monitor': 429772,
                                        'source_nw_x_pixel': -457930619020173490,
                                        'source_nw_y_pixel': -67202823669928467,
                                        'source_pixel_width': -6597322948515382054,
                                        'source_pixel_height': -6617962713797688278,
                                        'rotation': -7897574048362072558,
                                        'virtual_nw_x_pixel': 1687415587,
                                        'virtual_nw_y_pixel': 759371599,
                                        'virtual_width': -1623709174,
                                        'virtual_height': 1386927362,
                                    },
                        ],
                },
                {
                    'description': 'ə\x82ļχϋį˩ķɵѯíτӁΙѦĩȏѤʨԀΕˏ˪ѾԧzΨчϴї',
                    'monitors': [
                            {
                                        'identifier': 7211433,
                                        'width': -1467497307572941940,
                                        'height': -7434090773374941577,
                                    },
                            {
                                        'identifier': -902440,
                                        'width': -6783670359721215774,
                                        'height': -6015861547383319787,
                                    },
                            {
                                        'identifier': 9004144,
                                        'width': 1399465156815690142,
                                        'height': -705652920622061222,
                                    },
                            {
                                        'identifier': 4365387,
                                        'width': -1288121760364823223,
                                        'height': -3742337664040197073,
                                    },
                            {
                                        'identifier': 7655955,
                                        'width': -4048055224726844147,
                                        'height': 2601539977232882435,
                                    },
                            {
                                        'identifier': 5678431,
                                        'width': -6316524457072410006,
                                        'height': 3764470082275933314,
                                    },
                            {
                                        'identifier': 1792530,
                                        'width': -5857525663550761355,
                                        'height': 4419741984976264882,
                                    },
                            {
                                        'identifier': 973582,
                                        'width': -8314215635432200757,
                                        'height': 8359411474529943107,
                                    },
                            {
                                        'identifier': 2993341,
                                        'width': -726628570736164790,
                                        'height': -6845779983540532369,
                                    },
                            {
                                        'identifier': 7777094,
                                        'width': -7610142307749873384,
                                        'height': 4493016136847591104,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7887126,
                                        'source_nw_x_pixel': -7062157829875299782,
                                        'source_nw_y_pixel': -1719850703334580402,
                                        'source_pixel_width': -2210375921198821610,
                                        'source_pixel_height': -8550116570476094333,
                                        'rotation': -6547372442968580328,
                                        'virtual_nw_x_pixel': -1662628407,
                                        'virtual_nw_y_pixel': 769832431,
                                        'virtual_width': 1935146233,
                                        'virtual_height': -267092150,
                                    },
                            {
                                        'source_monitor': 9412950,
                                        'source_nw_x_pixel': -7265565409191058505,
                                        'source_nw_y_pixel': -6343264115619234161,
                                        'source_pixel_width': -956412531095253261,
                                        'source_pixel_height': -1498049986928235478,
                                        'rotation': -6731723277829952554,
                                        'virtual_nw_x_pixel': 1831984698,
                                        'virtual_nw_y_pixel': 1923031926,
                                        'virtual_width': 947267960,
                                        'virtual_height': 211131857,
                                    },
                            {
                                        'source_monitor': 5870829,
                                        'source_nw_x_pixel': -1103560928304046209,
                                        'source_nw_y_pixel': -1428648227847153442,
                                        'source_pixel_width': -6293543306682084959,
                                        'source_pixel_height': -5004389337555109923,
                                        'rotation': -441974480495989141,
                                        'virtual_nw_x_pixel': 765117664,
                                        'virtual_nw_y_pixel': 1740890930,
                                        'virtual_width': -1125320226,
                                        'virtual_height': 1445647073,
                                    },
                            {
                                        'source_monitor': -542255,
                                        'source_nw_x_pixel': -7226387399975311791,
                                        'source_nw_y_pixel': -7003338079259547791,
                                        'source_pixel_width': -7976448185550380638,
                                        'source_pixel_height': -8497721834059939050,
                                        'rotation': -4714334328251240537,
                                        'virtual_nw_x_pixel': 367304423,
                                        'virtual_nw_y_pixel': -1622561836,
                                        'virtual_width': 177890437,
                                        'virtual_height': 639814881,
                                    },
                            {
                                        'source_monitor': 107202,
                                        'source_nw_x_pixel': -3322473677928485602,
                                        'source_nw_y_pixel': -1304683943380998986,
                                        'source_pixel_width': -6231403325173811003,
                                        'source_pixel_height': -5384746679051466079,
                                        'rotation': -2109154931464656469,
                                        'virtual_nw_x_pixel': 1707661456,
                                        'virtual_nw_y_pixel': 1145878930,
                                        'virtual_width': 1532800548,
                                        'virtual_height': 1986409932,
                                    },
                            {
                                        'source_monitor': 4861045,
                                        'source_nw_x_pixel': -8848419835990327678,
                                        'source_nw_y_pixel': -1010390829155358792,
                                        'source_pixel_width': -510151175611276382,
                                        'source_pixel_height': -5926866114193054055,
                                        'rotation': -7643734193963726069,
                                        'virtual_nw_x_pixel': 870211963,
                                        'virtual_nw_y_pixel': -1498710840,
                                        'virtual_width': -667858837,
                                        'virtual_height': 1291431839,
                                    },
                            {
                                        'source_monitor': 6290632,
                                        'source_nw_x_pixel': -8104049953601842075,
                                        'source_nw_y_pixel': -2312504111084278888,
                                        'source_pixel_width': -4831338550110294285,
                                        'source_pixel_height': -7950537559326092299,
                                        'rotation': -4081000622776548861,
                                        'virtual_nw_x_pixel': -824399407,
                                        'virtual_nw_y_pixel': -351185111,
                                        'virtual_width': 1367159775,
                                        'virtual_height': 1702024650,
                                    },
                            {
                                        'source_monitor': 8022954,
                                        'source_nw_x_pixel': -565909682926206521,
                                        'source_nw_y_pixel': -3137449766958259197,
                                        'source_pixel_width': -2332012265267369391,
                                        'source_pixel_height': -6356395445115545133,
                                        'rotation': -6896927945801857101,
                                        'virtual_nw_x_pixel': -1143839400,
                                        'virtual_nw_y_pixel': -1843985796,
                                        'virtual_width': -1887212696,
                                        'virtual_height': -1245676441,
                                    },
                            {
                                        'source_monitor': 4103779,
                                        'source_nw_x_pixel': -4221010561488565003,
                                        'source_nw_y_pixel': -8480012322670204041,
                                        'source_pixel_width': -1530239755800538091,
                                        'source_pixel_height': -8038040320482463828,
                                        'rotation': -1976244080578468718,
                                        'virtual_nw_x_pixel': -1689326471,
                                        'virtual_nw_y_pixel': 8953377,
                                        'virtual_width': -14221619,
                                        'virtual_height': -880445874,
                                    },
                            {
                                        'source_monitor': 5701686,
                                        'source_nw_x_pixel': -3607545378330984956,
                                        'source_nw_y_pixel': -7578437572896222892,
                                        'source_pixel_width': -8593030375074806848,
                                        'source_pixel_height': -6524640792679592176,
                                        'rotation': -1838029542065472714,
                                        'virtual_nw_x_pixel': -172905694,
                                        'virtual_nw_y_pixel': -842354489,
                                        'virtual_width': -691161132,
                                        'virtual_height': 1544771068,
                                    },
                        ],
                },
                {
                    'description': 'cɚԈϓļŏ\x90ÏÎδʴҦІ\\ŘӑЀʪȌʜ"ľáдʱȁӧ\u0382Ҁɶ',
                    'monitors': [
                            {
                                        'identifier': 3208768,
                                        'width': 1896541925587911789,
                                        'height': -9072730699962685894,
                                    },
                            {
                                        'identifier': 6787223,
                                        'width': 8135490887795805712,
                                        'height': 2832504845338821916,
                                    },
                            {
                                        'identifier': 9343943,
                                        'width': -7203026415258480802,
                                        'height': -8023684106777864670,
                                    },
                            {
                                        'identifier': 497768,
                                        'width': 3787473978441481735,
                                        'height': -5975514866204699601,
                                    },
                            {
                                        'identifier': 6902460,
                                        'width': -8396677033005048144,
                                        'height': -1695660652838192225,
                                    },
                            {
                                        'identifier': 9767076,
                                        'width': 3820552932939488018,
                                        'height': 208449439176559350,
                                    },
                            {
                                        'identifier': 8669064,
                                        'width': 5779926011674113759,
                                        'height': 7914600339868436324,
                                    },
                            {
                                        'identifier': 9852705,
                                        'width': -8133294226090671306,
                                        'height': 6427312117513348029,
                                    },
                            {
                                        'identifier': 9440532,
                                        'width': -7256161412967968756,
                                        'height': 5160931120009670380,
                                    },
                            {
                                        'identifier': 7180914,
                                        'width': 7146915904023324851,
                                        'height': 4604978137408774739,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1698436,
                                        'source_nw_x_pixel': -123039966100513630,
                                        'source_nw_y_pixel': -7759621238269714115,
                                        'source_pixel_width': -6185321836848917350,
                                        'source_pixel_height': -4969523547547390032,
                                        'rotation': -5285160665543524813,
                                        'virtual_nw_x_pixel': 455387606,
                                        'virtual_nw_y_pixel': 1382748892,
                                        'virtual_width': 1445126178,
                                        'virtual_height': -1493495020,
                                    },
                            {
                                        'source_monitor': 2747558,
                                        'source_nw_x_pixel': -2169055422976448568,
                                        'source_nw_y_pixel': -6502073691932701242,
                                        'source_pixel_width': -6349520232809906585,
                                        'source_pixel_height': -5580189856270253730,
                                        'rotation': -4306930613807711667,
                                        'virtual_nw_x_pixel': 88237144,
                                        'virtual_nw_y_pixel': 123909520,
                                        'virtual_width': -1975299813,
                                        'virtual_height': 941155994,
                                    },
                            {
                                        'source_monitor': 4761276,
                                        'source_nw_x_pixel': -5319972969372011307,
                                        'source_nw_y_pixel': -4093355607213387891,
                                        'source_pixel_width': -5154173669411681412,
                                        'source_pixel_height': -1931869479088094999,
                                        'rotation': -4853741301268284527,
                                        'virtual_nw_x_pixel': 1748001480,
                                        'virtual_nw_y_pixel': 934441029,
                                        'virtual_width': -477421654,
                                        'virtual_height': -841322463,
                                    },
                            {
                                        'source_monitor': -721480,
                                        'source_nw_x_pixel': -8685942512047121549,
                                        'source_nw_y_pixel': -1400457605489373651,
                                        'source_pixel_width': -1782409582901231405,
                                        'source_pixel_height': -7644456606706470167,
                                        'rotation': -805930885046594658,
                                        'virtual_nw_x_pixel': 305551910,
                                        'virtual_nw_y_pixel': -276569063,
                                        'virtual_width': -1266479186,
                                        'virtual_height': 381418503,
                                    },
                            {
                                        'source_monitor': 8794905,
                                        'source_nw_x_pixel': -1299714187918291273,
                                        'source_nw_y_pixel': -5700248036558271657,
                                        'source_pixel_width': -978181778565251473,
                                        'source_pixel_height': -5917137618356255640,
                                        'rotation': -1634640706829035254,
                                        'virtual_nw_x_pixel': -1787853623,
                                        'virtual_nw_y_pixel': 1859283442,
                                        'virtual_width': -1754500000,
                                        'virtual_height': 1089426455,
                                    },
                            {
                                        'source_monitor': 1877266,
                                        'source_nw_x_pixel': -434820064317666077,
                                        'source_nw_y_pixel': -8218939746084133987,
                                        'source_pixel_width': -6633399797772771417,
                                        'source_pixel_height': -3958981739745208091,
                                        'rotation': -9152474797260168332,
                                        'virtual_nw_x_pixel': -1913284760,
                                        'virtual_nw_y_pixel': 442721096,
                                        'virtual_width': 31704583,
                                        'virtual_height': 758308671,
                                    },
                            {
                                        'source_monitor': 5981498,
                                        'source_nw_x_pixel': -3168603736052456635,
                                        'source_nw_y_pixel': -6266284596463117564,
                                        'source_pixel_width': -7892171382709597957,
                                        'source_pixel_height': -2741709576881311815,
                                        'rotation': -4445758301711579633,
                                        'virtual_nw_x_pixel': 328993132,
                                        'virtual_nw_y_pixel': -1351209150,
                                        'virtual_width': 1253779447,
                                        'virtual_height': -1532198307,
                                    },
                            {
                                        'source_monitor': 4932683,
                                        'source_nw_x_pixel': -725999044845347311,
                                        'source_nw_y_pixel': -5150438198443878341,
                                        'source_pixel_width': -7573886463758269433,
                                        'source_pixel_height': -3452618971453031147,
                                        'rotation': -6404579305338447881,
                                        'virtual_nw_x_pixel': 8283592,
                                        'virtual_nw_y_pixel': -1436259606,
                                        'virtual_width': -1434072392,
                                        'virtual_height': 183517988,
                                    },
                            {
                                        'source_monitor': 2444113,
                                        'source_nw_x_pixel': -6512484136650616872,
                                        'source_nw_y_pixel': -8335008249133884289,
                                        'source_pixel_width': -2119855157098297306,
                                        'source_pixel_height': -491307209002644283,
                                        'rotation': -6134295408676004080,
                                        'virtual_nw_x_pixel': 61671423,
                                        'virtual_nw_y_pixel': 68938380,
                                        'virtual_width': 1442058540,
                                        'virtual_height': -1469551727,
                                    },
                            {
                                        'source_monitor': 9514188,
                                        'source_nw_x_pixel': -9134711477167047129,
                                        'source_nw_y_pixel': -527929140308208328,
                                        'source_pixel_width': -7495369903592090510,
                                        'source_pixel_height': -8381419688671862926,
                                        'rotation': -2120731224641896855,
                                        'virtual_nw_x_pixel': 607513802,
                                        'virtual_nw_y_pixel': 1339663515,
                                        'virtual_width': 1686693281,
                                        'virtual_height': 152844474,
                                    },
                        ],
                },
                {
                    'description': 'Ӆƈǔʛ\u0379ɱǎžӨѕȸ{ɬÿėǘɋʫƑșηǏ˺ЦơЎϕԣdӢ',
                    'monitors': [
                            {
                                        'identifier': 6276559,
                                        'width': -2489669609034675613,
                                        'height': 8002974585922908913,
                                    },
                            {
                                        'identifier': 4726843,
                                        'width': 6935306969963625348,
                                        'height': 2364066343005704895,
                                    },
                            {
                                        'identifier': 1831181,
                                        'width': 1481204963710502185,
                                        'height': 1958593617970757282,
                                    },
                            {
                                        'identifier': 9456506,
                                        'width': 6221145767327679907,
                                        'height': 2832704582220956603,
                                    },
                            {
                                        'identifier': 3718857,
                                        'width': 2169792278048047181,
                                        'height': -8026476115670920630,
                                    },
                            {
                                        'identifier': 493475,
                                        'width': -6705173978753334714,
                                        'height': -1736081040716358570,
                                    },
                            {
                                        'identifier': 8334430,
                                        'width': -3350103101855497216,
                                        'height': -4261925088790251632,
                                    },
                            {
                                        'identifier': 3560354,
                                        'width': -7596076597984524294,
                                        'height': -1492368873063116815,
                                    },
                            {
                                        'identifier': 4797614,
                                        'width': -7831827226174790187,
                                        'height': -7239645279781825797,
                                    },
                            {
                                        'identifier': 8643734,
                                        'width': -8297792716071637198,
                                        'height': 5340461418318706879,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 859346,
                                        'source_nw_x_pixel': -4298569377537999354,
                                        'source_nw_y_pixel': -6154490837853302929,
                                        'source_pixel_width': -2329682440442265176,
                                        'source_pixel_height': -3664922275749669203,
                                        'rotation': -4295867197739757873,
                                        'virtual_nw_x_pixel': -1437133395,
                                        'virtual_nw_y_pixel': 1741202607,
                                        'virtual_width': 1370277695,
                                        'virtual_height': -1910871270,
                                    },
                            {
                                        'source_monitor': 7306356,
                                        'source_nw_x_pixel': -6786867657309360478,
                                        'source_nw_y_pixel': -3706370096700671379,
                                        'source_pixel_width': -395564088045103100,
                                        'source_pixel_height': -951800416511428506,
                                        'rotation': -9075056155616817243,
                                        'virtual_nw_x_pixel': -717384155,
                                        'virtual_nw_y_pixel': 1367193828,
                                        'virtual_width': -858933065,
                                        'virtual_height': 1190359429,
                                    },
                            {
                                        'source_monitor': 3661133,
                                        'source_nw_x_pixel': -5092085776024484360,
                                        'source_nw_y_pixel': -4517874993962434063,
                                        'source_pixel_width': -4620912222576149429,
                                        'source_pixel_height': -5553606518967025453,
                                        'rotation': -3355950407639420969,
                                        'virtual_nw_x_pixel': -406662430,
                                        'virtual_nw_y_pixel': -1978689569,
                                        'virtual_width': -1845632121,
                                        'virtual_height': 1988040473,
                                    },
                            {
                                        'source_monitor': 9711707,
                                        'source_nw_x_pixel': -7953257559955923253,
                                        'source_nw_y_pixel': -5277517567778643896,
                                        'source_pixel_width': -6538629625967548432,
                                        'source_pixel_height': -7182978639601321996,
                                        'rotation': -8803003930444052286,
                                        'virtual_nw_x_pixel': 1740037160,
                                        'virtual_nw_y_pixel': 1516099559,
                                        'virtual_width': -1260662175,
                                        'virtual_height': -1340634057,
                                    },
                            {
                                        'source_monitor': 8665405,
                                        'source_nw_x_pixel': -8272538829457191272,
                                        'source_nw_y_pixel': -7327794537640688767,
                                        'source_pixel_width': -3405922911397518724,
                                        'source_pixel_height': -5569654386258472812,
                                        'rotation': -782814437574306865,
                                        'virtual_nw_x_pixel': -385620233,
                                        'virtual_nw_y_pixel': -1995732330,
                                        'virtual_width': 1729598026,
                                        'virtual_height': -1397142942,
                                    },
                            {
                                        'source_monitor': 7209777,
                                        'source_nw_x_pixel': -444189254283214579,
                                        'source_nw_y_pixel': -6801168154479168845,
                                        'source_pixel_width': -541617586921808663,
                                        'source_pixel_height': -1763131805613236633,
                                        'rotation': -6011472973384569126,
                                        'virtual_nw_x_pixel': -1593778442,
                                        'virtual_nw_y_pixel': -1184131469,
                                        'virtual_width': 170967572,
                                        'virtual_height': 1349443234,
                                    },
                            {
                                        'source_monitor': 178809,
                                        'source_nw_x_pixel': -4100860925507884938,
                                        'source_nw_y_pixel': -6629387458567439450,
                                        'source_pixel_width': -5094946621273943644,
                                        'source_pixel_height': -1044274057595620411,
                                        'rotation': -5348222258233264409,
                                        'virtual_nw_x_pixel': -145476369,
                                        'virtual_nw_y_pixel': -1373834066,
                                        'virtual_width': -1268229236,
                                        'virtual_height': -208108471,
                                    },
                            {
                                        'source_monitor': 7435582,
                                        'source_nw_x_pixel': -8739430248246798831,
                                        'source_nw_y_pixel': -2130599397684138316,
                                        'source_pixel_width': -1019004323514733695,
                                        'source_pixel_height': -2064413108998517937,
                                        'rotation': -7864392984981503104,
                                        'virtual_nw_x_pixel': -1488128889,
                                        'virtual_nw_y_pixel': 400496128,
                                        'virtual_width': 1118937959,
                                        'virtual_height': -1014092675,
                                    },
                            {
                                        'source_monitor': 2598182,
                                        'source_nw_x_pixel': -6155141954997351232,
                                        'source_nw_y_pixel': -2012113432377398371,
                                        'source_pixel_width': -7008699020918255639,
                                        'source_pixel_height': -5981145735173497690,
                                        'rotation': -9093896520564933464,
                                        'virtual_nw_x_pixel': 1128142044,
                                        'virtual_nw_y_pixel': -547943919,
                                        'virtual_width': -590029878,
                                        'virtual_height': -1998833604,
                                    },
                            {
                                        'source_monitor': 6466668,
                                        'source_nw_x_pixel': -7569420475707234336,
                                        'source_nw_y_pixel': -3666854945105115289,
                                        'source_pixel_width': -2160154218824521226,
                                        'source_pixel_height': -5686334299906260259,
                                        'rotation': -5404863697536563046,
                                        'virtual_nw_x_pixel': -295467338,
                                        'virtual_nw_y_pixel': 162837095,
                                        'virtual_width': 5206101,
                                        'virtual_height': 1507190090,
                                    },
                        ],
                },
                {
                    'description': 'ȀtςýǦƙȧüԚʦɾңɁԤбЀɔŧȔшφņʺŨϤǐ˷ͿʨƁ',
                    'monitors': [
                            {
                                        'identifier': 12429,
                                        'width': -2708753453564557106,
                                        'height': 7681809075594499067,
                                    },
                            {
                                        'identifier': 6217684,
                                        'width': -3176953439813657704,
                                        'height': 4598799630790134031,
                                    },
                            {
                                        'identifier': 7950670,
                                        'width': 2563263042401038107,
                                        'height': 8373702148614026981,
                                    },
                            {
                                        'identifier': 8599937,
                                        'width': 5067419057938378491,
                                        'height': -7064589386408052110,
                                    },
                            {
                                        'identifier': 360987,
                                        'width': -6796722586561065061,
                                        'height': -5271552726604091119,
                                    },
                            {
                                        'identifier': 2346590,
                                        'width': -5013616621856852677,
                                        'height': -8134098475714056100,
                                    },
                            {
                                        'identifier': 1093485,
                                        'width': -5645555991423607290,
                                        'height': 3291770657383468637,
                                    },
                            {
                                        'identifier': 4587322,
                                        'width': 3683947387960983253,
                                        'height': -8489043565055313111,
                                    },
                            {
                                        'identifier': 7246393,
                                        'width': -7637068997503806294,
                                        'height': -1252047410055289683,
                                    },
                            {
                                        'identifier': -56310,
                                        'width': 8679649967263919132,
                                        'height': -1623724653744301876,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6248848,
                                        'source_nw_x_pixel': -3435942214274092839,
                                        'source_nw_y_pixel': -2137934702965286305,
                                        'source_pixel_width': -9035956670263345731,
                                        'source_pixel_height': -4498034070337502054,
                                        'rotation': -5116087772119968284,
                                        'virtual_nw_x_pixel': -1121128147,
                                        'virtual_nw_y_pixel': 411386087,
                                        'virtual_width': 799853502,
                                        'virtual_height': -1330205761,
                                    },
                            {
                                        'source_monitor': 6103903,
                                        'source_nw_x_pixel': -9044319851765760766,
                                        'source_nw_y_pixel': -6830897757536511251,
                                        'source_pixel_width': -850484346264743969,
                                        'source_pixel_height': -5581686659581889920,
                                        'rotation': -6546713789716867466,
                                        'virtual_nw_x_pixel': 1326059076,
                                        'virtual_nw_y_pixel': 1005928212,
                                        'virtual_width': 51668825,
                                        'virtual_height': -1989895712,
                                    },
                            {
                                        'source_monitor': 4321255,
                                        'source_nw_x_pixel': -8970107330059798352,
                                        'source_nw_y_pixel': -8568114711201123786,
                                        'source_pixel_width': -6397478293241782773,
                                        'source_pixel_height': -400473729883191852,
                                        'rotation': -387759802247193913,
                                        'virtual_nw_x_pixel': -695242527,
                                        'virtual_nw_y_pixel': -773867007,
                                        'virtual_width': 1454983764,
                                        'virtual_height': 421431187,
                                    },
                            {
                                        'source_monitor': 5385760,
                                        'source_nw_x_pixel': -3785888519211423513,
                                        'source_nw_y_pixel': -581590075566550153,
                                        'source_pixel_width': -8540799465496287491,
                                        'source_pixel_height': -5758356950571337814,
                                        'rotation': -8116707998335979188,
                                        'virtual_nw_x_pixel': 199782774,
                                        'virtual_nw_y_pixel': -165007106,
                                        'virtual_width': -1798856938,
                                        'virtual_height': 1817171997,
                                    },
                            {
                                        'source_monitor': 9880364,
                                        'source_nw_x_pixel': -181466744889143251,
                                        'source_nw_y_pixel': -2286357565410808120,
                                        'source_pixel_width': -8859241251064971023,
                                        'source_pixel_height': -4826118288374394409,
                                        'rotation': -194339351033253709,
                                        'virtual_nw_x_pixel': -1738341386,
                                        'virtual_nw_y_pixel': 602540720,
                                        'virtual_width': 472476712,
                                        'virtual_height': -847891198,
                                    },
                            {
                                        'source_monitor': 1270717,
                                        'source_nw_x_pixel': -4426935452476266860,
                                        'source_nw_y_pixel': -3114718256423614931,
                                        'source_pixel_width': -5483262184704817496,
                                        'source_pixel_height': -1307151778560694490,
                                        'rotation': -5374829238556934009,
                                        'virtual_nw_x_pixel': -1399030252,
                                        'virtual_nw_y_pixel': -1369486531,
                                        'virtual_width': 1904174025,
                                        'virtual_height': -1616752447,
                                    },
                            {
                                        'source_monitor': 8118097,
                                        'source_nw_x_pixel': -4071141542166484639,
                                        'source_nw_y_pixel': -2390164293766109112,
                                        'source_pixel_width': -8312827015825178044,
                                        'source_pixel_height': -3235646881622753954,
                                        'rotation': -1272508194433550656,
                                        'virtual_nw_x_pixel': 542529864,
                                        'virtual_nw_y_pixel': -116358785,
                                        'virtual_width': -716334219,
                                        'virtual_height': -1702624632,
                                    },
                            {
                                        'source_monitor': 2187320,
                                        'source_nw_x_pixel': -7209907325892664351,
                                        'source_nw_y_pixel': -2347785110069238921,
                                        'source_pixel_width': -7162955418593702654,
                                        'source_pixel_height': -5129566041101510455,
                                        'rotation': -998235733308889708,
                                        'virtual_nw_x_pixel': -675017366,
                                        'virtual_nw_y_pixel': 1236254344,
                                        'virtual_width': -1138134785,
                                        'virtual_height': 1875079117,
                                    },
                            {
                                        'source_monitor': 5661318,
                                        'source_nw_x_pixel': -6637319003542421912,
                                        'source_nw_y_pixel': -1213355881881485986,
                                        'source_pixel_width': -1913521316327486078,
                                        'source_pixel_height': -4765376933524263574,
                                        'rotation': -2840427474530328004,
                                        'virtual_nw_x_pixel': -186440742,
                                        'virtual_nw_y_pixel': -1600209425,
                                        'virtual_width': 826803512,
                                        'virtual_height': 1761595128,
                                    },
                            {
                                        'source_monitor': 7734128,
                                        'source_nw_x_pixel': -7601080565032443976,
                                        'source_nw_y_pixel': -7782744818979200903,
                                        'source_pixel_width': -8444739899576116748,
                                        'source_pixel_height': -7306706016053027795,
                                        'rotation': -6833727719308017620,
                                        'virtual_nw_x_pixel': -374086809,
                                        'virtual_nw_y_pixel': 1017279778,
                                        'virtual_width': -858240931,
                                        'virtual_height': 888949077,
                                    },
                        ],
                },
                {
                    'description': 'ȋԢҶÃƶÀ΅іαЙӎƽӊɷôϑ\x85Ǚã\u0381¢σ˽҈\x84ҧ\x9aΒҭȼ',
                    'monitors': [
                            {
                                        'identifier': 8673831,
                                        'width': -3175748607080095173,
                                        'height': -1469881067239424419,
                                    },
                            {
                                        'identifier': 8005653,
                                        'width': 6945026968531842289,
                                        'height': -566214076649969364,
                                    },
                            {
                                        'identifier': 4060365,
                                        'width': 2982623957862137003,
                                        'height': -1066296971657983772,
                                    },
                            {
                                        'identifier': 8089939,
                                        'width': 2021602143494661157,
                                        'height': -3505325278574952089,
                                    },
                            {
                                        'identifier': 4109218,
                                        'width': 3354977453983390094,
                                        'height': 1680989765510098065,
                                    },
                            {
                                        'identifier': 7516975,
                                        'width': -1970421310961156139,
                                        'height': 6225030591857455679,
                                    },
                            {
                                        'identifier': 1111144,
                                        'width': -5721833301070787980,
                                        'height': -1957469299527373995,
                                    },
                            {
                                        'identifier': 8151600,
                                        'width': 6497803971406905705,
                                        'height': 5332441533893338358,
                                    },
                            {
                                        'identifier': 7433581,
                                        'width': 550206581527705768,
                                        'height': -3409682724369698609,
                                    },
                            {
                                        'identifier': 8022487,
                                        'width': 2027209577655873704,
                                        'height': 716282289215227075,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7884906,
                                        'source_nw_x_pixel': -8327810615398682035,
                                        'source_nw_y_pixel': -6776626453147155720,
                                        'source_pixel_width': -8651871935511794364,
                                        'source_pixel_height': -6818741992607509691,
                                        'rotation': -7905018804905553631,
                                        'virtual_nw_x_pixel': -941810383,
                                        'virtual_nw_y_pixel': -575587894,
                                        'virtual_width': -968304011,
                                        'virtual_height': -1011267800,
                                    },
                            {
                                        'source_monitor': 7283014,
                                        'source_nw_x_pixel': -2332814770051809938,
                                        'source_nw_y_pixel': -3481739002752299778,
                                        'source_pixel_width': -615553767632353443,
                                        'source_pixel_height': -842230945966417746,
                                        'rotation': -7340534688837254227,
                                        'virtual_nw_x_pixel': -1524053940,
                                        'virtual_nw_y_pixel': 957467062,
                                        'virtual_width': -742035404,
                                        'virtual_height': 1809172146,
                                    },
                            {
                                        'source_monitor': 3464040,
                                        'source_nw_x_pixel': -1179298903209056704,
                                        'source_nw_y_pixel': -3818345807749464972,
                                        'source_pixel_width': -1694018515954532469,
                                        'source_pixel_height': -3457729161791515151,
                                        'rotation': -8166587646389749767,
                                        'virtual_nw_x_pixel': 322191983,
                                        'virtual_nw_y_pixel': 1953190431,
                                        'virtual_width': 1056090305,
                                        'virtual_height': 284900862,
                                    },
                            {
                                        'source_monitor': 7232344,
                                        'source_nw_x_pixel': -2183626281369551826,
                                        'source_nw_y_pixel': -5749440677660199337,
                                        'source_pixel_width': -2245503867153208533,
                                        'source_pixel_height': -1905225172846731551,
                                        'rotation': -5416589791565956561,
                                        'virtual_nw_x_pixel': 423979,
                                        'virtual_nw_y_pixel': -251896293,
                                        'virtual_width': 1869299033,
                                        'virtual_height': 786950743,
                                    },
                            {
                                        'source_monitor': 4344187,
                                        'source_nw_x_pixel': -7243938013410865063,
                                        'source_nw_y_pixel': -8487059019303728377,
                                        'source_pixel_width': -7578542835371405276,
                                        'source_pixel_height': -3973980624588777034,
                                        'rotation': -973985478286695203,
                                        'virtual_nw_x_pixel': -1526992035,
                                        'virtual_nw_y_pixel': -1495089797,
                                        'virtual_width': 1107155516,
                                        'virtual_height': 594852197,
                                    },
                            {
                                        'source_monitor': 1517767,
                                        'source_nw_x_pixel': -581942520490344503,
                                        'source_nw_y_pixel': -8088467701336490240,
                                        'source_pixel_width': -3516687674330242633,
                                        'source_pixel_height': -7251108412968982724,
                                        'rotation': -8011712776763508954,
                                        'virtual_nw_x_pixel': 1525532993,
                                        'virtual_nw_y_pixel': -926356368,
                                        'virtual_width': 1278746845,
                                        'virtual_height': -1334556089,
                                    },
                            {
                                        'source_monitor': 8295706,
                                        'source_nw_x_pixel': -1460149172980161962,
                                        'source_nw_y_pixel': -1387417008512895714,
                                        'source_pixel_width': -5128198780362482449,
                                        'source_pixel_height': -5829625199341127852,
                                        'rotation': -4171274563250328366,
                                        'virtual_nw_x_pixel': 53805385,
                                        'virtual_nw_y_pixel': 1243466798,
                                        'virtual_width': 44857990,
                                        'virtual_height': -905801395,
                                    },
                            {
                                        'source_monitor': 9238988,
                                        'source_nw_x_pixel': -561619650857097429,
                                        'source_nw_y_pixel': -6820727952107790985,
                                        'source_pixel_width': -8154335290015104846,
                                        'source_pixel_height': -7377891387565857306,
                                        'rotation': -5175987009041657665,
                                        'virtual_nw_x_pixel': 955663047,
                                        'virtual_nw_y_pixel': 808142956,
                                        'virtual_width': -1612461368,
                                        'virtual_height': 1293440957,
                                    },
                            {
                                        'source_monitor': 19954,
                                        'source_nw_x_pixel': -6994323190449191100,
                                        'source_nw_y_pixel': -7494126790962766177,
                                        'source_pixel_width': -8619364320940701618,
                                        'source_pixel_height': -8955715441453587390,
                                        'rotation': -6996639130528332900,
                                        'virtual_nw_x_pixel': 835851375,
                                        'virtual_nw_y_pixel': -954646822,
                                        'virtual_width': 947514196,
                                        'virtual_height': 677699432,
                                    },
                            {
                                        'source_monitor': 8070660,
                                        'source_nw_x_pixel': -6216766128954593727,
                                        'source_nw_y_pixel': -5220424303468885158,
                                        'source_pixel_width': -5476951420255061318,
                                        'source_pixel_height': -635826965815973769,
                                        'rotation': -1452089724341910477,
                                        'virtual_nw_x_pixel': -157456708,
                                        'virtual_nw_y_pixel': 1590856470,
                                        'virtual_width': 429292175,
                                        'virtual_height': -1593248390,
                                    },
                        ],
                },
                {
                    'description': 'ԖќŵǙΏmвĐDʸ¿өK\x8döТΦԀʛxӴ]œś˪КкÜʐź',
                    'monitors': [
                            {
                                        'identifier': 336294,
                                        'width': 7685565111688940037,
                                        'height': 8290643808949746983,
                                    },
                            {
                                        'identifier': 6428201,
                                        'width': -7205857576983320830,
                                        'height': 3659379244137161568,
                                    },
                            {
                                        'identifier': 4645225,
                                        'width': -3367307903833379043,
                                        'height': -7152068471580985304,
                                    },
                            {
                                        'identifier': -630434,
                                        'width': 6646445772918524311,
                                        'height': 8015798587425615816,
                                    },
                            {
                                        'identifier': 3149308,
                                        'width': 3665168902616622101,
                                        'height': -3031244534195979004,
                                    },
                            {
                                        'identifier': 1340403,
                                        'width': -6085760410911898771,
                                        'height': 2855989917169681721,
                                    },
                            {
                                        'identifier': 3123816,
                                        'width': 8776481023027137307,
                                        'height': 7018966426432107103,
                                    },
                            {
                                        'identifier': 9561290,
                                        'width': 6938696420290413026,
                                        'height': 6882866887959278600,
                                    },
                            {
                                        'identifier': -213412,
                                        'width': 6351981001640758906,
                                        'height': 8760561532796256488,
                                    },
                            {
                                        'identifier': 4627177,
                                        'width': -6267682661730815889,
                                        'height': -546739897885674446,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7347172,
                                        'source_nw_x_pixel': -6295900873097955000,
                                        'source_nw_y_pixel': -8960842639263393397,
                                        'source_pixel_width': -1627184837136784701,
                                        'source_pixel_height': -3952999067019442365,
                                        'rotation': -6018432160815476042,
                                        'virtual_nw_x_pixel': -628335895,
                                        'virtual_nw_y_pixel': -1240827762,
                                        'virtual_width': -1546385096,
                                        'virtual_height': -683435252,
                                    },
                            {
                                        'source_monitor': 6398370,
                                        'source_nw_x_pixel': -4698313482431401449,
                                        'source_nw_y_pixel': -5701354631735923139,
                                        'source_pixel_width': -2588530503762039901,
                                        'source_pixel_height': -5175766224634615142,
                                        'rotation': -3951197971957073889,
                                        'virtual_nw_x_pixel': 114747181,
                                        'virtual_nw_y_pixel': 872127401,
                                        'virtual_width': -351514621,
                                        'virtual_height': 1789040414,
                                    },
                            {
                                        'source_monitor': 7123012,
                                        'source_nw_x_pixel': -9130652013272962774,
                                        'source_nw_y_pixel': -3041134791559640746,
                                        'source_pixel_width': -8851177002030197312,
                                        'source_pixel_height': -5018764158359967363,
                                        'rotation': -7529880739081642298,
                                        'virtual_nw_x_pixel': 663508898,
                                        'virtual_nw_y_pixel': 1507644385,
                                        'virtual_width': -610235777,
                                        'virtual_height': 531900225,
                                    },
                            {
                                        'source_monitor': 7383975,
                                        'source_nw_x_pixel': -2743816852131093211,
                                        'source_nw_y_pixel': -1083753887590289850,
                                        'source_pixel_width': -7856484461110309880,
                                        'source_pixel_height': -8257830447677511871,
                                        'rotation': -7475673222958545528,
                                        'virtual_nw_x_pixel': 1986571504,
                                        'virtual_nw_y_pixel': -1782192440,
                                        'virtual_width': -809402969,
                                        'virtual_height': 1922122098,
                                    },
                            {
                                        'source_monitor': 7132950,
                                        'source_nw_x_pixel': -6914489224275983721,
                                        'source_nw_y_pixel': -1639448715894373765,
                                        'source_pixel_width': -5546136990512184307,
                                        'source_pixel_height': -6026573015243431710,
                                        'rotation': -1541059450937019507,
                                        'virtual_nw_x_pixel': -1458371671,
                                        'virtual_nw_y_pixel': -1837810639,
                                        'virtual_width': 1820001821,
                                        'virtual_height': 960616961,
                                    },
                            {
                                        'source_monitor': 8842073,
                                        'source_nw_x_pixel': -3600121667013619957,
                                        'source_nw_y_pixel': -8316899644242260505,
                                        'source_pixel_width': -1307461600024456663,
                                        'source_pixel_height': -3665985656732908849,
                                        'rotation': -1135472488282696758,
                                        'virtual_nw_x_pixel': -603467922,
                                        'virtual_nw_y_pixel': -532231787,
                                        'virtual_width': 802073127,
                                        'virtual_height': 645847330,
                                    },
                            {
                                        'source_monitor': 941277,
                                        'source_nw_x_pixel': -2958065151725108167,
                                        'source_nw_y_pixel': -1713273548922566605,
                                        'source_pixel_width': -883525687087511333,
                                        'source_pixel_height': -7411090375934404833,
                                        'rotation': -7642860265816187099,
                                        'virtual_nw_x_pixel': 1899307679,
                                        'virtual_nw_y_pixel': -143797887,
                                        'virtual_width': -1169582933,
                                        'virtual_height': 1170139614,
                                    },
                            {
                                        'source_monitor': 2604756,
                                        'source_nw_x_pixel': -1732621113537277450,
                                        'source_nw_y_pixel': -3393903002979996875,
                                        'source_pixel_width': -5377586706723688542,
                                        'source_pixel_height': -6882050070714355592,
                                        'rotation': -8346112214195201776,
                                        'virtual_nw_x_pixel': -12946951,
                                        'virtual_nw_y_pixel': -764215910,
                                        'virtual_width': -649474367,
                                        'virtual_height': -74516305,
                                    },
                            {
                                        'source_monitor': 7944755,
                                        'source_nw_x_pixel': -4372296994588618260,
                                        'source_nw_y_pixel': -8229308150917662504,
                                        'source_pixel_width': -3915546275188343749,
                                        'source_pixel_height': -1531920209059463388,
                                        'rotation': -6974352951266762833,
                                        'virtual_nw_x_pixel': 31060061,
                                        'virtual_nw_y_pixel': -1424585399,
                                        'virtual_width': -1001277066,
                                        'virtual_height': -1411061335,
                                    },
                            {
                                        'source_monitor': 7549999,
                                        'source_nw_x_pixel': -3660151351470637091,
                                        'source_nw_y_pixel': -3927972944457355950,
                                        'source_pixel_width': -2539222043405375050,
                                        'source_pixel_height': -5388896505592383381,
                                        'rotation': -2778629204622292899,
                                        'virtual_nw_x_pixel': 1362759121,
                                        'virtual_nw_y_pixel': -250123178,
                                        'virtual_width': 1322688206,
                                        'virtual_height': 927870858,
                                    },
                        ],
                },
                {
                    'description': 'ΰАŹáıǌâѫЎ\x99ɊґʘτÊȫѐˈƬ΅Ңҵ҉˓\x8eγΞȂјʾ',
                    'monitors': [
                            {
                                        'identifier': 6011136,
                                        'width': -892811513495661010,
                                        'height': 7355309722080092102,
                                    },
                            {
                                        'identifier': 1540433,
                                        'width': 8220967461530201886,
                                        'height': -3313807146746848418,
                                    },
                            {
                                        'identifier': 4442162,
                                        'width': -2030675769105171916,
                                        'height': 6671162884030569483,
                                    },
                            {
                                        'identifier': 3760912,
                                        'width': 3185123927426314576,
                                        'height': -3903587058245346422,
                                    },
                            {
                                        'identifier': 9350182,
                                        'width': 8028890280811680358,
                                        'height': 1707671799783433496,
                                    },
                            {
                                        'identifier': 3801300,
                                        'width': -3502179678167657451,
                                        'height': -5540795975798250517,
                                    },
                            {
                                        'identifier': 4934575,
                                        'width': 5985551015670044570,
                                        'height': 3690127544348319228,
                                    },
                            {
                                        'identifier': 3562746,
                                        'width': -8369954725990480804,
                                        'height': 3056243860435541326,
                                    },
                            {
                                        'identifier': 5175809,
                                        'width': -8131067705287449234,
                                        'height': -4592765350784973460,
                                    },
                            {
                                        'identifier': 5213474,
                                        'width': 2142278878551047711,
                                        'height': 7245831568857621898,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2495131,
                                        'source_nw_x_pixel': -7483229240755617132,
                                        'source_nw_y_pixel': -404106015118133026,
                                        'source_pixel_width': -4685707274216787358,
                                        'source_pixel_height': -5352524844388179487,
                                        'rotation': -8875842036026047093,
                                        'virtual_nw_x_pixel': 1311108861,
                                        'virtual_nw_y_pixel': 128177387,
                                        'virtual_width': 798662974,
                                        'virtual_height': -495633856,
                                    },
                            {
                                        'source_monitor': 6268343,
                                        'source_nw_x_pixel': -4777098498113011652,
                                        'source_nw_y_pixel': -7130325729768408407,
                                        'source_pixel_width': -7200868801347727272,
                                        'source_pixel_height': -3264028713454791528,
                                        'rotation': -1590412246004594435,
                                        'virtual_nw_x_pixel': -1769546351,
                                        'virtual_nw_y_pixel': -1475058467,
                                        'virtual_width': -1371006781,
                                        'virtual_height': 88129709,
                                    },
                            {
                                        'source_monitor': 2180628,
                                        'source_nw_x_pixel': -7559209167583202345,
                                        'source_nw_y_pixel': -5416816696605573704,
                                        'source_pixel_width': -473130434266722246,
                                        'source_pixel_height': -1055498546586088548,
                                        'rotation': -5210408589440180156,
                                        'virtual_nw_x_pixel': -371859717,
                                        'virtual_nw_y_pixel': -859927198,
                                        'virtual_width': -1713962477,
                                        'virtual_height': 1700069523,
                                    },
                            {
                                        'source_monitor': 8343404,
                                        'source_nw_x_pixel': -6768613822062312673,
                                        'source_nw_y_pixel': -2007615776277231959,
                                        'source_pixel_width': -3499490300629158048,
                                        'source_pixel_height': -192327011379030962,
                                        'rotation': -7724627382109989041,
                                        'virtual_nw_x_pixel': -813433265,
                                        'virtual_nw_y_pixel': 1426241082,
                                        'virtual_width': 1240813368,
                                        'virtual_height': 1169508490,
                                    },
                            {
                                        'source_monitor': 396189,
                                        'source_nw_x_pixel': -5093318663667598104,
                                        'source_nw_y_pixel': -6582568272080133352,
                                        'source_pixel_width': -4711675019389154923,
                                        'source_pixel_height': -5835456120158716427,
                                        'rotation': -5353642313893820022,
                                        'virtual_nw_x_pixel': 822167847,
                                        'virtual_nw_y_pixel': 1520725302,
                                        'virtual_width': 392425318,
                                        'virtual_height': 1153262688,
                                    },
                            {
                                        'source_monitor': 5236866,
                                        'source_nw_x_pixel': -2165524213616895761,
                                        'source_nw_y_pixel': -8505397971862905634,
                                        'source_pixel_width': -1855455992283281061,
                                        'source_pixel_height': -5634442238564262859,
                                        'rotation': -6879593788904437993,
                                        'virtual_nw_x_pixel': -1508742444,
                                        'virtual_nw_y_pixel': 715049641,
                                        'virtual_width': 543740875,
                                        'virtual_height': 449837530,
                                    },
                            {
                                        'source_monitor': 3036750,
                                        'source_nw_x_pixel': -7230839124427428213,
                                        'source_nw_y_pixel': -502654002981770513,
                                        'source_pixel_width': -2464958737200197041,
                                        'source_pixel_height': -1532951767662414508,
                                        'rotation': -912143801021577987,
                                        'virtual_nw_x_pixel': -1195927040,
                                        'virtual_nw_y_pixel': 752224053,
                                        'virtual_width': 797284054,
                                        'virtual_height': -1760433363,
                                    },
                            {
                                        'source_monitor': 224381,
                                        'source_nw_x_pixel': -5643493170255454465,
                                        'source_nw_y_pixel': -1534004288481940415,
                                        'source_pixel_width': -2495784210081638409,
                                        'source_pixel_height': -3013633782878809885,
                                        'rotation': -3783541829651496684,
                                        'virtual_nw_x_pixel': -878292428,
                                        'virtual_nw_y_pixel': -284148826,
                                        'virtual_width': -1365309453,
                                        'virtual_height': -460104302,
                                    },
                            {
                                        'source_monitor': 9979335,
                                        'source_nw_x_pixel': -7962038022590514587,
                                        'source_nw_y_pixel': -3797372055670965340,
                                        'source_pixel_width': -1303463692486249641,
                                        'source_pixel_height': -1595543562342335746,
                                        'rotation': -5565140767431598770,
                                        'virtual_nw_x_pixel': -335487369,
                                        'virtual_nw_y_pixel': 1207572849,
                                        'virtual_width': -1465660485,
                                        'virtual_height': -898102389,
                                    },
                            {
                                        'source_monitor': 1933072,
                                        'source_nw_x_pixel': -4032767105995448143,
                                        'source_nw_y_pixel': -8679713212591096828,
                                        'source_pixel_width': -3019443669613481811,
                                        'source_pixel_height': -3659466427981131787,
                                        'rotation': -685303131702869107,
                                        'virtual_nw_x_pixel': -1246326028,
                                        'virtual_nw_y_pixel': -1694586611,
                                        'virtual_width': 1488654418,
                                        'virtual_height': -1797043643,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 8059874,

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
            'request_id': 2739288,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 8813155,

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
            '$': 'lâǾДѰZĀʡʐǔͱϬ҈˷ˬΈҊѤѧX¢ǵϳѣ҇ȴЌpмΙ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4910203625145748192,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -58781.12133854101,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': True,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20210309:035952.609796:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ΑӶXϳ˪ǟřpӺʕćѼ\x95ōƦ"пÈѬˮ«ϒwΖҞӨĎͻ˔Ŵ',
                'ƧΩŤпǣɺӜҦίгɒˠӷ\x80\x85ʎǵʊƇΆΨšԐˡ˓ԝʬ˫ϑƶ',
                'ȇєłңȄғϺʇχѷʏȪȜ/ƱƠӮĢͲԄƃӟӤғѤȚʊсθã',
                '҉ХɯɆɻÐKИȁίбΔʏĞÊ\x9cқҧÜűңˤвƄ\x99ȕźԅƙ£',
                '?ϽϰmϩМЅиӄÎȾöɂЅɲԌƈӃǐķγưҶҙħқʖˤ®ͳ',
                '7uˬʵ\u0381ƥиĳ\x8cͳɣȮɘÂÁơоàŽοŅīүºˬΝΥȍ\x98ͳ',
                'ƝŌŝЁӴů)ɶɨϥӇŮǂ˭ԎˤŕԣӗϯИ\x9aǑÞ¨˹κΎʬҾ',
                'ԂğԪ1ӜŖҰˈËˈȬɋR\x87σAьӣȬɚԘɬÛɷʶԬș>ȫĘ',
                '҇ŗǤԚîũО˭ȽġɝкʖЂ\x81ſzƄѐҜ͵tэϴPɥԌɐɱˌ',
                'ІĳśÊƃȣѥҊȄϽӺȒ«ñ`ËǬƞ҆ĵӣGĮϙ\x94Æĝԩӣυ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -5572845240556125401,
                8366301302154565920,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                205704.11308481108,
                720377.9525618636,
                -53177.50673868946,
                974690.4911083579,
                933652.2319367423,
                -41997.18523945056,
                707142.2947414339,
                97532.70203226808,
                579212.1700096969,
                614908.8344778541,
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
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210309:035953.580563:+0000',
                '20210309:035953.602285:+0000',
                '20210309:035953.628260:+0000',
                '20210309:035953.649888:+0000',
                '20210309:035953.672741:+0000',
                '20210309:035953.694779:+0000',
                '20210309:035953.715906:+0000',
                '20210309:035953.736887:+0000',
                '20210309:035953.758720:+0000',
                '20210309:035953.780382:+0000',
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
            'name': 'Ю[ʬϋĢκԄĐǴƃĚϐӧČpʟԑһɱьc˖\x99ĮŽФӦѸЬӶ',
            'value': {
                '^': 'float_list',
                '$': [
                    186935.76181709563,
                    628997.5459017316,
                    972024.4642732244,
                    98779.54802059746,
                    -78559.4433622426,
                    659358.4534299345,
                    663126.6613791639,
                    68033.65218987782,
                    880348.7051850058,
                    446943.91755147465,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ŧ',

            'value': {
                '^': 'int',
                '$': -4531413558500870648,
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
            'catalog': 'ȼH\x93Қ¨ϻf˯Ǘ.˩ЁȶʖЌϛĴҷǺӇˀƅˇԍ˱JŦӍŚǨ',
            'message': 'ΩČόϮșƗ˗ЋϖƁѿŷϫƥϚʝү\u0382ɸϜ¯ĐӑƌĊü΄ɻъ˵',
            'arguments': [
                {
                    'name': 'Ӫяĩ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        596402.6484797086,
                                        415377.9762703238,
                                        -90906.33461654157,
                                        257990.56132266152,
                                        347027.37920342875,
                                        886789.4333749866,
                                        983958.4942257148,
                                        731670.8159208824,
                                        693285.5865688152,
                                        69219.49199771485,
                                    ],
                        },
                },
                {
                    'name': 'βԅ˙ɼҤӳч҃ĦҔлÑҒ˜ƦφȀAԒƱг\x85ԀǊӒ˪у|',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210309:035950.531994:+0000',
                                        '20210309:035950.552604:+0000',
                                        '20210309:035950.575613:+0000',
                                        '20210309:035950.595373:+0000',
                                        '20210309:035950.614925:+0000',
                                        '20210309:035950.631807:+0000',
                                        '20210309:035950.649892:+0000',
                                        '20210309:035950.670060:+0000',
                                        '20210309:035950.688031:+0000',
                                        '20210309:035950.705353:+0000',
                                    ],
                        },
                },
                {
                    'name': "ɴǃ*iȠҌ\u038b'",
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210309:035950.808715:+0000',
                                        '20210309:035950.830246:+0000',
                                        '20210309:035950.855177:+0000',
                                        '20210309:035950.880902:+0000',
                                        '20210309:035950.906090:+0000',
                                        '20210309:035950.930259:+0000',
                                        '20210309:035950.954091:+0000',
                                        '20210309:035950.976496:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ιäĳƠϤȕˌǢÿ',
                    'value': {
                            '^': 'int',
                            '$': 8952018272304870409,
                        },
                },
                {
                    'name': 'ȮÙŞIӰ',
                    'value': {
                            '^': 'string',
                            '$': 'ԐiËÏˆǡȀĔǋϴƝϑкı˺ˎɢĆ\x87ѤȢʞӁҞ\x94Ԓ7ʜĽϒ',
                        },
                },
                {
                    'name': '·ЅOôϖҌǉƾёĭȲō¾ӍƈӊˇȋaŘɺʶҙ˯ǸŏГ\x95Çχ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'LɞkϠɼ˥ʳƊG˭ˉˁǾr\x8cтπ΅ȚԆȸʞŞǐϬόЪ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        143423.29719911376,
                                        259953.93698511418,
                                        514448.5409337104,
                                        464060.0438960168,
                                        711600.055497035,
                                        893173.0227038112,
                                        819609.4760023708,
                                        393837.5789687109,
                                        125761.00133687118,
                                        842495.0754377514,
                                    ],
                        },
                },
                {
                    'name': '¹ϿĴԟɪѐȧьĩɔяӰӻХ;Ɲӳϕ\x81ґѫƶƐӾΥtƞѣӍ˕',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
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
                    'name': 'сӷͷǴ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ȽԘƣĞǧǏЏĐʲҺϡԈƜέϺɴѤŦǚɷĆø²Ǒ҇Ͳ˦ώВϊ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ȕț',

            'message': 'Ы',

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
            'identifier': 'ѢÓоыѲҞǶõʶ;ѷǭǍȅ\x9d`ӤǶԥѸɟμÐĹοЕȔԪíǍ',
            'categories': [
                'internal',
                'file',
                'configuration',
                'file',
                'os',
                'access-restriction',
                'invalid-user-action',
                'file',
                'invalid-user-action',
                'file',
            ],
            'source': 'ȼԎҸ^ŏ\x91ϗӢ~ȒǩϠǦӮӂʡ\x8fÀЋӳғ\x84uʴЀǗªϮѓУ',
            'messages': [
                {
                    'catalog': 'ÛӼ˓ɂϧȊζϽʄoėίϩȬΣʱBδȴˡГΜŌ{мɿȕҖĿ˄',
                    'message': 'ƄÚxЇίßȜϓϚǶУӪʑ˚4\x91˼ÉƝǼϩϨѳΟ,ǫõКɈ˰',
                    'arguments': [
                            {
                                        'name': 'ј˲ɬҦʑˣȚϦĄ\x82ѿŪФ\u0383˒УiŸǣʍѸŢ˩ǬȦѴӺϖ˰Ш',
                                        'value': {
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
                                    },
                            {
                                        'name': 'ӂ}҂î˾ÀҖВƃπoҀ\x83ƓʘԣD',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ӽѫ\u0381īӌʊѽƊσ\x95ɬ}ʔСɘ˞ɼŬÊнɟѵɝѶԆԡѲҲÍż',
                                                    },
                                    },
                            {
                                        'name': 'ĻʚˎмǧŘ\x9füʡУƩˏҵӌ+˽јȱƀНςΚϨΑǦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            745074.9579683314,
                                                                            222478.5219607955,
                                                                            550167.3170893618,
                                                                            853927.7545983301,
                                                                            962204.8046372738,
                                                                            587640.7684804031,
                                                                            236607.82959031564,
                                                                            324191.5247344278,
                                                                            916479.6725663,
                                                                            548983.6568135393,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'śɬ϶ȗɥįЕ¯ъʗӶϖѧŊϘ&мƸÁҋǈ+āʝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035931.266041:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǣѸˠӝżÀɹəą\xa0ʷôǷČϣjͱķ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 190555.738902018,
                                                    },
                                    },
                            {
                                        'name': 'γ,ѪɮӪįːӽÁϬκӰҏΟņˢǳАķŧɚҹɝЀʷϊӉùҊy',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ԬǢѝ:ӄʗϵˆ0ÅʫǧÏyҎȗiӂˈ)ˈZ0н҆\x83υŇŧŐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ħǢҧĂĴѻǘȆɞÓőѸʖǺθώĕґſ΄ǈԪƘΨЕφԞӲǾĠ',
                                                                            'ĬÃŷù\x9dƐŴԤи¥ЫÞԕЮҤǞĘʏ_җû$\u0381MʿÉƺä\x7fʼ',
                                                                            'ьÎԙÍ%ȵGźʉԜəȱ˝ʲūƍ҄ǿ˞ӸΑƔʧ҃ɕНцЮѳϋ',
                                                                            'ԋӝǛӫεˤιƬͼǤӭ҉ϴɝѫѪ\x82ʞș{ѩʫʇĞȗԂїǿʨx',
                                                                            'SʀԁʊϗœΊɭĔˮżħƚΊĈ¶7Ҳ˔\x8f\\ðjŉȷϨӔ>é˕',
                                                                            'ȡĖȓǁɅεԙŽηwŅȉĵƭˠδƀT˚ЗˣÂѱӔ$ˤιěǌϨ',
                                                                            'ÆԌʕƿ+%ØјɣǩȎƱųѼ]дʁҰБё˖шѰ5Úɭϧӂˡʘ',
                                                                            'ąοуЍεʋ˦ҍęȢòȔ˚ȽȘƒɴξɪϋĸǃůɇʰɞϽԀƱƶ',
                                                                            'Ϩʐ§ΩăʒƹЮĊΏŊĥоɵЬȲЁѠƀɻıɯȟŲӤȂҍѭ҅Ǧ',
                                                                            'ϬІUЬ\x8dĈɱр҄½ϕ\x9dˏчωȰϋŮЃЃǚǈӉƲ\x9dʄ~\u0383ԫα',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҩɋѷШӟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            859476.8612071999,
                                                                            918900.1428102405,
                                                                            68881.0083892725,
                                                                            375657.6026045172,
                                                                            429194.338308687,
                                                                            137692.17202378437,
                                                                            945610.6726076056,
                                                                            862787.8767317843,
                                                                            734026.089265227,
                                                                            252097.2590263915,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϚgџĵȹϾRö«ŢӁЀ"ũЦďԢǴ<ÐŮҋʠ¸Rϣƹɐ˃ҡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǴâȬäĕN*ςŊʩ˵İļҦҶ=ӝƾɵRҿǸϧΚԖqĂcΩˮ',
                                                                            '`ä£\x89ϻ͵ǢоɺрНԓɈǝZǓӤҲ˲ӝƍƐҝƔԈ˲RPʽв',
                                                                            'ɊґǧɴһΉǁǫĊƋӊЁ\x94Ӹǔ/ƨǁӧԬƜĢµԄȼ¡÷ιʼѴ',
                                                                            'ƥĐ®щ҂ϝҁƨ»ϡǡƦɍ˺ÙЛŔɜh\x8bˡʕȋȉȿȔҭԩïǑ',
                                                                            'DǴΣҡÏӘǍȭЬÄƦmȁĵћ´\u0382-ŖҶɫlüǧ¿ǩɩԖ˵ʱ',
                                                                            'ʱɄϢǑдйӼƘǘԙҏŚΞиŦɥϽťȮ˷϶¾ȪѠĆʚɣҟǻ\x84',
                                                                            'Źϥ˷ŦȎϦǸǪЉƘѰǒɯ¬Ľ¢˖Đ¤¿ƀъ\u038b\x80ψӷӜŷϷƛ',
                                                                            'ѯͿ{ʱÈӍĖÿϋҔʛǈǸɃʾϿċϤΨƵːӵ@c3ǡHƮӶϾ',
                                                                            'úԘǁыɓʆȀԡ+ǮȪͼЇȖ\x85ҮǩvîӨ\u0383ɧƠϰКâϽKҥԎ',
                                                                            'лϷ\x92ȘǐȄʘζѯʰӇuȻʄŸɲн7»Ҽҙʸ]авȩϮΤϼȁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ј½w˲ϫ:ŦƫʃúϗƓУȟʐŒԡɀӤȔȹuȨӫкǸɭ<Dȹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˬɦѷ˝ӇГ\x9fӂÙҩɉǊ\x87ѲϾŸ¸ӨǎΟʜʟrêɯюǩбїǆ',
                                                                            'ɼʛ,ĒӽzɦFOѲϸ˩АƧʈπʌɰԃgňƾʞµϹĈʛȺӊΌ',
                                                                            'ÄƦӠӆ˅ƑǜΎç2Y:_ҍǊŷĒеjĆмҏ¯ΙĨ\x85ôƯ˔ͷ',
                                                                            'ѬŢ3ˋƮƔί\x84ϑХȑěȲˉ¥ӌõНʔñsɧΗȃ˲Ȱʭ\\9Ӕ',
                                                                            'ГσȏĵЫ˹ϧɫòJ\x80˄ɶçǊҎʩäĄЏы|ҋ˩ϟѮ˥ҨȆҨ',
                                                                            '˟ßzԩƤͰϻ҈³ӪŰ˓ɸ\x83ǶðхэǕƩǰФçΥŎѡҸʫϭˤ',
                                                                            'Ι˦ƇdϢѲВʍˎҋЪЭҸԓŀĐĮEԎӞҚБѸӷx\x99Ћėēʬ',
                                                                            'юʍҭ\x8fЅ˔ӶĦ¦ӭʌɃȎƩЍԝȦȩϋЮΤӅʛˡ\u0382ų˷Ɍ˻Ñ',
                                                                            'ÝöŨȀӗАәѷʇоŲϠѸЕӒˉȝʀVdbş8˱7żǝłǔǟ',
                                                                            'D\\ÒbÍВҭ˶ӠˁƃƃїЉɘ;\x83ͺԓӱéˀͱӝĽϜʁɃΒԍ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ğƃ˵ʹ1ˉļĈӇ˚YӐһÊԥ\u0379ҌɅ¡ΡnΩ.SӸˌĦкȇǢ',
                    'message': "ϩ\x85ƠќϺĸ\x96ϭǐɠΝȂы\x8bХЏÊŃ\x90јĔɕӊɻ'Λʌͳчɚ",
                    'arguments': [
                            {
                                        'name': 'ҟƿǝϋӨϠЭǒ˽ş÷џ˒ĖĜГȽǧӹvӳӸĻѦȼȰҶϐρĨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϺïȣɒҋƵԝ\x9așȨƔŸҼĥίā\u0382ΝÇѢӆң ˟ˣӑȅ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʻԚҿϋϘм˦ȓŜǒhVБƫ҈!²Ԇ<ŋǌˍʸ˞\x9fʲůǍž\u0381',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            339394317469168437,
                                                                            -6740423084105919594,
                                                                            6731364309618178830,
                                                                            4400240103369227058,
                                                                            5043140115598412721,
                                                                            -5102228378206428575,
                                                                            3836521446819502602,
                                                                            -5756783795327317376,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ãǒƜёǶɌƻėΫˁ˸¦˛ȰλˈĭƂѭŌƯΎʳǯċɏ˜'ǣȦ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ČҘɆɱăǬ ВʝȹýӤӜæҥɞ®ȘƃӞиŘhялώĩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            821011.7562031406,
                                                                            265003.5840758712,
                                                                            27162.910937807,
                                                                            762294.5264533235,
                                                                            344515.7211300802,
                                                                            413792.3860385177,
                                                                            448129.297387691,
                                                                            110001.14971569559,
                                                                            118970.99493590143,
                                                                            281023.14262613695,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'əÍ˔ҹіðҨҼӼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˣǙλŧɷŀαΩЭɚĵσëŭTƉǭχ\x99÷ñԝѦĆǯІϕ>ӱÂ',
                                                    },
                                    },
                            {
                                        'name': "ÅȖӂɇУƋ×'Ͽҡǅ҈ѢũˀΨěԮщ϶ȺԬГжАɞ/ƓƸβ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035934.233850:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ưȺO˞ŔͼԜϯÈ\u0383ǏʥƜ})ѕӺ¿ѕȒōӴȧԄϱűŉʤѠŦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 700707.1189949482,
                                                    },
                                    },
                            {
                                        'name': 'p |ĳ˫ʢˉˈǫɶɯȆҫт~ҽӚȮѫ\x9aÞʾӬӅá˲Oӳħ˰',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2499910060487702604,
                                                    },
                                    },
                            {
                                        'name': 'у«ũʍԭҁͿԒľ:ɦсĂуЊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 504157.2853527431,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ҐжǎK3ßÚ8ӰӂҝǉϽėГρ'ңɼƽǂüǢϹҚԛ¥ƄÜ\x83",
                    'message': 'Ђý\x9d¼\x8dɡŅҿN҄ϕƹΖԆӲԍȤf\x87ɟǉ4ǁŗԚñčȽţĔ',
                    'arguments': [
                            {
                                        'name': 'гʭëǸϻŮ8ѱļʗȄåҚ˝ćȝēˀ"ǗʳƎБоŧʡƷԔϫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035934.684302:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x96љêӨӆtѩюȼ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4725782981060976202,
                                                                            3416413132527264699,
                                                                            8190300345979317411,
                                                                            6254433429555408545,
                                                                            -3473628488479746505,
                                                                            3201210699325735314,
                                                                            -5664256757792383517,
                                                                            4612181857761759472,
                                                                            3287647137910643076,
                                                                            9126729762377650814,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЌЪªҘҕƼ\x89',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035935.032347:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ұơ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӼȦβ×\x97ɐʫԜΨŅȐŽΦƥň\x95ʗԂúΜyӛȞЕʁǚǪȹDϷ',
                                                                            'ȻƷwƆȺpΐώȺȄŭȜƙ\x91ХӼʹʼĠΟҚP÷ôAɅ\x95ëЕǣ',
                                                                            '˼ǥǎ]Μɚ\xadЖİȻЯɝɳɡщĲǨ¼ȚÉuƫЭİƧʧǀм´Ƙ',
                                                                            'ӃƂIʲ҃ǣҷʾοɍԙûʧĶÎϱ%ҀϽЖϥѻ¬^ϨãɡϔяҲ',
                                                                            'ȝ5Ʒ¡ĢGа\x97ͰψȤňǒƇʦҞχəƕχŎӵпųҍ҇ѬʙҤѡ',
                                                                            'ԒѲòɄ\x9cϹÎȃΚ˚1Ē5ԬξΏ˨ƦȖƟŵȒФӉϞйЖӅЄɮ',
                                                                            'ΖѴԞʅ«ˀ_ҡˈĔȊζ\x9eĨȱӘ·ԮĿєǅϿӔȴƮӪļ{ȕƣ',
                                                                            'ӥƌƘϣΟДЇƙǪːѭĞХȺĜѬҢɣ˽αӅµ\x92ƽԢЖ\x9bҲɒǥ',
                                                                            'ŲЋĶǎŶҔԪэƢłҦҪ§1ĵˎǴҴȂĶҬЈuϵŕʹҮѺʩġ',
                                                                            'ƾťŻÒӌϿɤӾ\x89ҝύ\x94Ҽ\u0378IɓҧʟШSЮƔʹÉԦƿǎҸŞӫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӿT˯\u0379ľÛҍΏĘԜä\x8fʺљÕǭίʹϏΨӠƝџҬβȲԤƪżѽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035935.550070:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ҷñ˧˳φ˚ϻӓĐ\x9a¹ӆϐƕ¹ӵƣ(Ĥѳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӪũЪǋʨθӒȯÓЍƜƭӢӝϩïѸЏӨĿȾӳ˫óлǕϘʓƽ҅',
                                                    },
                                    },
                            {
                                        'name': 'Ÿԉ˙π\x96Ϧ҃EѿуʊǕͼӗǀƸÞƈɷӽͱɎʟʣʭϷ\u03a2źЧ\x95',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x91ґӳϋØӏƯƪԛǜеƚΞɎҾӽùżm{ɩǍĻŀûː!пęĎ',
                                                    },
                                    },
                            {
                                        'name': 'ǮϘɒҰǽϱlʨīÉӥȩĦъVȺɞ\x83ұȘ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5794456617119323061,
                                                    },
                                    },
                            {
                                        'name': 'R',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035935.861034:+0000',
                                                                            '20210309:035935.885690:+0000',
                                                                            '20210309:035935.907320:+0000',
                                                                            '20210309:035935.927435:+0000',
                                                                            '20210309:035935.950993:+0000',
                                                                            '20210309:035935.972784:+0000',
                                                                            '20210309:035935.993860:+0000',
                                                                            '20210309:035936.016754:+0000',
                                                                            '20210309:035936.037195:+0000',
                                                                            '20210309:035936.057330:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƴ5ɶĘӰҶԞϔċĝφϳąϟÓõԊƣ\x93ħɐŕԡ҄£ƏнўȆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035936.165007:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '?χȍљқǚαŸԄžӈǪƩѾԦ£˛ȓŮЙЇӵ^ΰǮǖÁԏũϘ',
                    'message': '\x8cΑӋȪӘ\x88ȺӬʐɖȧȬĪǙƞҙķiƷΆʘҖ\x81¿Ĺǚ}ďĥϱ',
                    'arguments': [
                            {
                                        'name': '®Ͳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            268193.3182872583,
                                                                            10509.274313929258,
                                                                            587353.3463458787,
                                                                            478927.08343004354,
                                                                            522994.81390820956,
                                                                            830203.8000280624,
                                                                            349988.0700381766,
                                                                            828295.2146547523,
                                                                            737998.8296200228,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9fїFéńǭƬѥʀѱɋŪN',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƾŒǪІӟ˼гȥΗǝ˼ɘsͲŌØӱȾѳб\u0380ӥǪŻΠԤƊӂȮӤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            129751.89988114685,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ėhPŤ¹˻ʙ!Ѥ+ˌѿ\x9eҰČɡũˈӱӡʉƘѽMԇɷʮԒӌԘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            923710.935911862,
                                                                            518884.4741448676,
                                                                            758813.5002010111,
                                                                            718567.9968397429,
                                                                            660871.8823774623,
                                                                            291255.90123144153,
                                                                            686766.575881447,
                                                                            255429.68434425263,
                                                                            35899.790445877414,
                                                                            677128.1818206832,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʌʵġΙšΚƇƿя',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4637366085235018463,
                                                                            1949323830423133296,
                                                                            8364251381609496638,
                                                                            -6873898706227405867,
                                                                            -5088937591052054351,
                                                                            -2127748765876945340,
                                                                            -7253849452338210741,
                                                                            6470723827075130919,
                                                                            -4477533219713478553,
                                                                            7845926291804727647,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɫѮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            161604.6748556133,
                                                                            479025.80855890387,
                                                                            264771.72619852144,
                                                                            8134.887741449857,
                                                                            248507.8545133365,
                                                                            844935.7078375652,
                                                                            477827.19573798054,
                                                                            353416.49151293095,
                                                                            933657.8520583437,
                                                                            525246.2820980562,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¿ϢӈĶΈͷ˧ЪXӂЦ©ΘυɝΛɢǒȧ˶ƶӋβǛӻĳʔśɖö',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            829609.1416846653,
                                                                            522422.5971372087,
                                                                            935513.5636361686,
                                                                            57669.131484209094,
                                                                            -80012.15263008003,
                                                                            -94889.17278715334,
                                                                            269911.1731990876,
                                                                            520647.6536406481,
                                                                            854420.2089006042,
                                                                            627939.1904984186,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȫҶȢʢԮŬʞΩӚȉχǔǖӭƘʐ£ìҳcӭŀ?ҝΪŚαʈ\x80ϑ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6776162688149544239,
                                                                            4164264852913151002,
                                                                            -6503226732682099786,
                                                                            -3291784536161668976,
                                                                            8548268819066214353,
                                                                            2056596905802140057,
                                                                            7663534762615853661,
                                                                            3791909574226540479,
                                                                            5857836877426674608,
                                                                            -8804031612271976711,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҵ}ƣƅпSȧmҘϰƵìƯʈyʾŴԆȖɾRŠzWІԂѼțƿǸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            977070.9161668769,
                                                                            -93375.47840674332,
                                                                            267932.58011847804,
                                                                            814316.2361723525,
                                                                            982301.7347260711,
                                                                            567722.6245209503,
                                                                            920510.9155805091,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǐѦóê϶\x8dǭԅԈȵӌҼȇŵȚӗЎŋȺЂбˉӈžŗˠѡҜËʆ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '҆ё˝Үb˞ϡǦȬΙʤΉȸʵаӍɞƟӟɻƋÙңϧâó3ӵ\x93А',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ӂǜȁˆh¡ͳŇʂγӋģӆ\x9f¤ίȉƄǲ3Ѳˠѓóǔpпςåä',
                    'message': 'ǪԓӓɌƿeœōϷǴʿЛԝԒЛӴΕϊɊԋјϙ°нΡ¿cƧυӧ',
                    'arguments': [
                            {
                                        'name': 'f',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 1622.7615727323137,
                                                    },
                                    },
                            {
                                        'name': 'ӭΗĕ˟бӧԈfϑ\x80|ԭƅƹő',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȫϺćˍʢɨϜӃϛоʃžõ˱\u0378˯ɔ<ӠɷθʟŘÇȳɁȁ./Ǭ',
                                                    },
                                    },
                            {
                                        'name': 'σ˦ěğŶѼԟʷƲŃњɩǧƽӀԃԟƝ÷ѶȞƱ\x8eƞҮɋЪƢӨƉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035939.074247:+0000',
                                                    },
                                    },
                            {
                                        'name': 'αƵʞȺɱŗLʵoƥ\x82ʍȦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8108491892241634931,
                                                                            -1514008715040481242,
                                                                            -4804459206824187944,
                                                                            -2976694015018820237,
                                                                            -4552722451896343926,
                                                                            -4255080122471906526,
                                                                            -3462324791334595067,
                                                                            -2580983210081187530,
                                                                            6347643821883982615,
                                                                            2087377627780834387,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǟ:ҮĳпÏÆȘ;i¼Їʬ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ūǁƹųɤuӐʭǕѠǚͶʜĜϧǀңҔQѥоʶĮɷɧԀάҍ¦Ӟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2198746738111594470,
                                                                            -8402987707579151185,
                                                                            3013478113693973824,
                                                                            -8443332120512921398,
                                                                            5113928844911997540,
                                                                            2075874439492718098,
                                                                            4302802212846617844,
                                                                            -8671304976535889930,
                                                                            339370607152296016,
                                                                            -263112865994480278,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʤƞϗ˺ϬŔӤǮɣТgϟѕԤöŞҰ\x89ϪԭЅɭɵƘм',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "˪ɵԭ'ԭЪ¦Ɓю˲ǤȜшİµѷЌ¼ʍϬòҴ˕Åʇӷҗ˰ʸϩ",
                                                                            'ҷȘțôӻ»ЂыΚΘ,ȝÅѸŔɸҙҞɺˁƺϬßɠ˫ęѶơéԇ',
                                                                            '=˯ýŮʊɕjǯȅǎŐҵ҂ʼȐѩ%ҡԦɑ΅ӑNрӏ_ĒрɈŹ',
                                                                            'ŴŏкЗʩєВţAФӄ˴θ,ɸʡӄΞ?ȏЋɛßΒΆ\x93ɦΡϾӽ',
                                                                            'éʍԩŇKɭƊҟ\x9co;ɓƚȌĻɊʐ˻лʆ˒eн͵КыҢӁŢԄ',
                                                                            'ʒɎƼьмӅȽ´ǼʤӹɛĂŗҋɮÓʶïҘ\x9fǛ×ƟѭÂπ˞ɗŐ',
                                                                            "цÁʔGϽťӑʷӫƆˋņřμӀȯҍ϶ǾνɛԢвʽ=Ƀ\x9cŻ'ɼ",
                                                                            'ѾðǽƜїƂΌфüʫΕӧжΙҠӑʚ«õʴƽG<ϊτȲƍȻ˝\u0381',
                                                                            'ғӢԏΌλľħyǈϐъ˵ɭԂʥϾɲǕȣƀǈqǚǠȩŎҹӃЪǅ',
                                                                            '˙ͷÆˀKѱ7ӔНĿԋǔ˒ǘû ϭ\x8e\x98ɱӅǛɪi1όŖȲϢƉ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƵӂХ\u03a2ϲƻϟĘϥϑÁǒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035940.512755:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǵЯϕёϒ\x91ԪѸѶҦř\x93¤®ȂζĉѫïбƶњҳԚĲĹѹƨȍң',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˻ƋĻȴțɍƛʮ\x95čHIƫҥҖ˻ˉ\x97ʷƣӂхˑÔџɽ˧ђ\x9aќ',
                                                                            'ȍч˷ԖҡÑÆίѩoʲʜ"»ɭ&ϻ˚ԨLӪΑĨŋϟύӷσ£ț',
                                                                            'țЮ˰ķ\x8bˈȕħʐнѻġΉɚȯѡ˘ĘϠƽϿƩԭɰʬē˓ˑ÷Ǧ',
                                                                            'ԕńȪ¬ȀшӾϭÑŷǚǊȠӔƼдƺˇȄPћǿϖеϼʣȫЏΠԡ',
                                                                            "ԝЏãbӬ˞ĥɇʻǿәӇ³ҲˉĶǒȰԢxʝ'ŠѭȤʯ\x80đјǹ",
                                                                            'ĪНóƄŹʘǫ͵ĠǧҙŎŐ1ƙɻѢ7ĕӼϫǏεԬϩǠ;΅ÒŇ',
                                                                            'Ï`ɕʔGɴҝÖȞǒӅɭΚĤҴƃΨпǷҨИөǷƪʮҕȠǫőˋ',
                                                                            'ĔʆѲɯԈϏϽŘϕÃΒĊƥǩűϳκďĶȋČӨυƢ.ŰũȯĘӗ',
                                                                            'ѕӌ\x7fΌ§ɄĬʩΝѡЀ·ʌŭȅξâԏÉʉАâ\x88һѐǄƀǅŽƌ',
                                                                            'ǟѣ=њҢʽɧ2:ʗ«К¡нњΛѩɆŅŔ˸љɗωàˁƈfŹΗ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'сМŞҴωɑͿΉ{îȫœÆµȠӃҽɪϗһκҙΛƼˡĉН҅Ïԑ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035940.895274:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϒáĲǙͻ˩ƋϝȦ\x8dçåʝčaūˁǈπа',
                    'message': 'wδнȃï£·Ԧŝˬȣŝ\x8bǝʜȣċ҈ŝȚśкЛďʐϹΊ\x92ϟČ',
                    'arguments': [
                            {
                                        'name': 'ÚЛȐȓϣΐ!ĶŁƺҭÉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035941.060698:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ėʄҳмgūǟѴČϕǈʸҐӽϖѽ\x88˅ŐΪǜԕηjʤQϪ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȽƅЮÍʉфҐȨ\x88уаËφЙǳϝ.˦u',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɰǬϦ&Ӛʳԅďѫšԉ¬Û¯ǝǫԪͰű\\ëͷҨԜŞіɏmȷÙ',
                                                                            '/ʖвҎŁҳ"ЏɼƄȁʙѐĔĕԑԫɔˤĽ˭ϮMƘӓͰЩɑʙǵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ъ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035941.540374:+0000',
                                                                            '20210309:035941.560363:+0000',
                                                                            '20210309:035941.579915:+0000',
                                                                            '20210309:035941.600795:+0000',
                                                                            '20210309:035941.621358:+0000',
                                                                            '20210309:035941.642058:+0000',
                                                                            '20210309:035941.662186:+0000',
                                                                            '20210309:035941.681407:+0000',
                                                                            '20210309:035941.701433:+0000',
                                                                            '20210309:035941.721782:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϛ\x99ȘkƎñ˰ΥҵyʔˌŝЎҺƜýŷńҚȸȚΒǍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6505896025221612495,
                                                                            2476603637337595618,
                                                                            -8376369596494196075,
                                                                            8005412723456276928,
                                                                            -5394185710938815495,
                                                                            9102856513224845617,
                                                                            230841446862889504,
                                                                            2913541466151922136,
                                                                            -1734103423539585861,
                                                                            4235346720758361220,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¯xҡӮҖi¡\x99\x81ˣԐǇʖƱԡϏąĴЂͶжɢVЎ}ʻҫ±ѐʷ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035942.132864:+0000',
                                                    },
                                    },
                            {
                                        'name': '@ɕȐˮĊğĦϤΒɦĮň',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            920937.1218501343,
                                                                            835189.2017505168,
                                                                            800518.2597715324,
                                                                            -54859.389819299875,
                                                                            904707.5230263218,
                                                                            390546.488547146,
                                                                            757008.7252199725,
                                                                            975775.4702455944,
                                                                            664969.3906041031,
                                                                            566952.8616451308,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĒΡϮ(ӛЛϚɘ9Ƭ\x96Ӏȹ,ͼʌħƌ±ҋCȈӼԡυtčíÛȥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x96ƩԅĦΤȶϹѤǁÆΞѴңŔÛÒҺ\x98ӨѢ2ǟӄáWɎ(ТΦʙ',
                                                    },
                                    },
                            {
                                        'name': 'ŲϲтѡҮӃʚњҮĸŬҞӁǭʘϊҥƔОХǢ\x85\x84ǽéҠӁӠԢʚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 579704500336680042,
                                                    },
                                    },
                            {
                                        'name': '7˫ő?-ӄ˻αшрȒɻˆŗ/ҠʮөθʄŃѤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '«\u038bı_ԟ!СʓĮъԡȪшӤ\\ȡҁПͰûϦϛŊԏеΰǽþϿʟ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'е˚фţӥǹʋΫҏȃƆϫ˫ɗӯ',
                    'message': 'íѻş|ʀǌZԧ:°ƛΘӏʿƢЏЀԩӥνюŵЫÉĭÀЮӬѼü',
                    'arguments': [
                            {
                                        'name': 'ǈҵ˭ȄʶԈйΞəDƵǯȴӧѭ¾ЭöΉ\x92ӨȧǨ¥ʟԍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035942.858510:+0000',
                                                                            '20210309:035942.879501:+0000',
                                                                            '20210309:035942.900360:+0000',
                                                                            '20210309:035942.924485:+0000',
                                                                            '20210309:035942.945032:+0000',
                                                                            '20210309:035942.964806:+0000',
                                                                            '20210309:035942.984650:+0000',
                                                                            '20210309:035943.006684:+0000',
                                                                            '20210309:035943.029330:+0000',
                                                                            '20210309:035943.051501:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԆKӈϝźg\x87˼ӤɺǯыΕ«˕ǀǌȉȪˠҚfΑɹҞѮʜͻļċ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ę\\ȧǰţјƨˢrÏΐΓŤ?ӥŌ\x96 ІɖϏɦĝ¯ƽщͿȋӼԏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'еĲǣýŕѻќԢȢĽɞЦáƲҝЌЈϡϮѽјԂΧŅŞΘς˽ʄД',
                                                    },
                                    },
                            {
                                        'name': 'ƧҟʀԖҶ˾é%ΊԥӰ;ǦԨЬӷӦ¿\x8a£ιũɲ_\u0380ņàʴWʹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            428858.1077962145,
                                                                            799878.2518280448,
                                                                            930823.1751179001,
                                                                            784120.3018173602,
                                                                            236510.54849197844,
                                                                            124381.91686468438,
                                                                            276131.43376772996,
                                                                            20591.419173232178,
                                                                            -87792.32170172372,
                                                                            306833.1713772224,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǆѯƈϤˀɖ½·ʣÓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4895503073458997189,
                                                                            -5016037461264291284,
                                                                            -1934661741734791152,
                                                                            -2953383631539524698,
                                                                            -6636108239435315594,
                                                                            -5652311340449245048,
                                                                            4581685745784787306,
                                                                            -8109244460487958207,
                                                                            2302264330695033869,
                                                                            -8432790380964605596,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȯ˩ŝԂѐHЕр\x7fɋŢtѫȎӆÉɇòԐʩ1B³˶ǋ8(ƢÉ¨',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6790382927662973553,
                                                                            3257330640645812794,
                                                                            9071731799603932914,
                                                                            3487703068638917265,
                                                                            -4382235884634356109,
                                                                            3720870161368555962,
                                                                            1111828014589505840,
                                                                            -8703943835360957704,
                                                                            1227588188116688061,
                                                                            -7706882989462805263,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǻ˥;īȴʷӷǰ´Ȉ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "øƲʯɌӮϋП,ʗǚȊђ'ԝӭçӌƗԑʼͰ\x88r'Д¤ǯӌƍ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8335170841020277001,
                                                    },
                                    },
                            {
                                        'name': ')ɏϭΡƐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĻԙͶȰŋѴςȔɩΉŗɑԭˊӻΘƼҪŝľʬ>Ѩʶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1257002833676516604,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Џ;ȩ0\u038d\x8fʃѴ=ƮàE©ĉκķʧχƗ4ȪƝɍ5ʁΏʩȹӌď',
                    'message': 'τԊέӯ˙ӧɁƶЧϤңԁǑ˺µȡņҢζԛϻIƅ>UˬҶʨ\x93ƭ',
                    'arguments': [
                        ],
                },
                {
                    'catalog': 'ǃӋƶЂͻԫƻӃ²ϕʺЍ˩ӇșГȹӧʘʙĻōΊӳҗ;ɒà:Ɋ',
                    'message': "Ҩң\x94ŠDϵǃƢƨɼҋυҴ˫ˆʲrΎ\x87±ГП˼ůĨ\x9eʍӚÓ'",
                    'arguments': [
                            {
                                        'name': 'ЙǱӭˏҍwғ2м˕˃ҥϣl҄ќɩ˖',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035945.277823:+0000',
                                                                            '20210309:035945.297561:+0000',
                                                                            '20210309:035945.318032:+0000',
                                                                            '20210309:035945.336546:+0000',
                                                                            '20210309:035945.355266:+0000',
                                                                            '20210309:035945.372022:+0000',
                                                                            '20210309:035945.388725:+0000',
                                                                            '20210309:035945.406384:+0000',
                                                                            '20210309:035945.423353:+0000',
                                                                            '20210309:035945.441677:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʽɚAɐԦªҹɒϑż_ӐѻӂǹВ˟ӛŤҷӨҚ¬Řϧ҃ҰӃɟÀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5125828889391051960,
                                                                            5552893534095778,
                                                                            1446092437565347215,
                                                                            4701488697963794173,
                                                                            -5953916740808724753,
                                                                            -8930119148936996976,
                                                                            927495102310500073,
                                                                            4718103716466954435,
                                                                            6137615498962097514,
                                                                            -4459321859364823743,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʤɐŠǗĆʀŚʲͶҔώæΆùрʹˏӦТĎɦǴʲрʁțНƠƋb',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4375628502791368187,
                                                                            -1485856396923726584,
                                                                            -4642974123093505284,
                                                                            -6848061905886806569,
                                                                            -7482950369463978337,
                                                                            -1729910280430154647,
                                                                            -4800788306938990390,
                                                                            -3662558855705144687,
                                                                            724536400248644705,
                                                                            994337951548914119,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҷęэӂͲԬ§Ԧҫ\x98ǙĒǷ\x81˦ОԖͷ\x8dȷHÎs!ҳǛľʳҨù',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2363582635078249306,
                                                                            396377311185854849,
                                                                            -6599899684456384024,
                                                                            7024515510619599715,
                                                                            4968399518535996382,
                                                                            -1303218924482694473,
                                                                            -8424565245076571451,
                                                                            -2965492438619199942,
                                                                            -6989480423684469361,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĺʦ¡ǍӡĮԗіĺǰPʃŃ5Ţŭʹ\x96jкȻ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035946.461789:+0000',
                                                                            '20210309:035946.489233:+0000',
                                                                            '20210309:035946.509938:+0000',
                                                                            '20210309:035946.532394:+0000',
                                                                            '20210309:035946.551904:+0000',
                                                                            '20210309:035946.571465:+0000',
                                                                            '20210309:035946.594187:+0000',
                                                                            '20210309:035946.615248:+0000',
                                                                            '20210309:035946.639236:+0000',
                                                                            '20210309:035946.663216:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǭʹϷŹϭĕgͺƻϯƜɚɌƠϕϨγȇʰŤIӅƅɱҶʬҤƈ\u0378Ð',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЇѴĚƒ˘вoƊԊҖʥˮŨɓÂĘʠΊԤɧһƾÝɫҋϟĕȖ˻¢',
                                                    },
                                    },
                            {
                                        'name': 'еҎ\x97ӰϾŸªϕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 739297.1490226131,
                                                    },
                                    },
                            {
                                        'name': '$ŞνҳȪƁѝÊʮϏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035946.994873:+0000',
                                                                            '20210309:035947.011610:+0000',
                                                                            '20210309:035947.028422:+0000',
                                                                            '20210309:035947.046397:+0000',
                                                                            '20210309:035947.065505:+0000',
                                                                            '20210309:035947.084520:+0000',
                                                                            '20210309:035947.105442:+0000',
                                                                            '20210309:035947.125491:+0000',
                                                                            '20210309:035947.149035:+0000',
                                                                            '20210309:035947.172679:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͿǌƇ\x98ĵǾȡȕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7741062795774806105,
                                                    },
                                    },
                            {
                                        'name': 'Ɣ\x8aɭˮōȿ©ͲqҤԒʹˤj·ԄĻԇǁƚ{ƉaӣġϷ.Џnʹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǥŭǻ˼Ќ˳ʉ¼jŊ.¾Ѵ҄ƙíʿӛÇυϖ\x87шcԜΜȞύëт',
                    'message': 'ʘόѝȹÍǶʤĽӇǼ³ц|ʱӤɋŅ˜Θ˅\x92ćқğҸʶŉŬùċ',
                    'arguments': [
                            {
                                        'name': 'aĦњ~ùʿԌҲ\x8aɤпҢԎЀҭɹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035947.752545:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϠʊԀčΗ\u0380ʩÛïƋÑϸԖșΑҮəŷ\x88ѦѸç~ÉȦɷѤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1478970697697703699,
                                                                            1722493006875399290,
                                                                            7558721382658333630,
                                                                            6637890045826770608,
                                                                            -7673084910520584621,
                                                                            -992053261410146592,
                                                                            6135804448966288586,
                                                                            -1461772302961056918,
                                                                            -7817282492346249637,
                                                                            -3688899253207710685,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŔFǪΧγԄ#j҅çĵěРsʧƎϧǅU˵ѪϩΝΣɐϵ\\\u0381Ѝӊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            605561.0590166943,
                                                                            235419.736561395,
                                                                            190452.5707939425,
                                                                            336738.28934481554,
                                                                            81198.37406197845,
                                                                            190300.61347949592,
                                                                            122376.71055434161,
                                                                            64938.06958533288,
                                                                            780310.9767924171,
                                                                            818129.0147776448,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʮʶĂͼÉȶXcюԔħԚӨԕʌΌҸ˾ɗƐǓѐɜѢϛˍ˹ɅÈ÷',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035948.416220:+0000',
                                                                            '20210309:035948.434249:+0000',
                                                                            '20210309:035948.452104:+0000',
                                                                            '20210309:035948.470249:+0000',
                                                                            '20210309:035948.488377:+0000',
                                                                            '20210309:035948.506802:+0000',
                                                                            '20210309:035948.525506:+0000',
                                                                            '20210309:035948.555683:+0000',
                                                                            '20210309:035948.576518:+0000',
                                                                            '20210309:035948.595197:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƵĆɶľƇʛʯϺΛ\u0383Ώ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            774983.5034958344,
                                                                            387333.7119569309,
                                                                            359792.5434968679,
                                                                            288081.6466219878,
                                                                            515578.02289133845,
                                                                            462178.99015616137,
                                                                            224078.79430158518,
                                                                            485985.55921283294,
                                                                            374800.71982070827,
                                                                            357374.4290177666,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ґÐȺèŖʥɿɳѐ^żãȵӢ˟Ʉȟ×sΎȭӏφǪĢƉYǇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035948.978713:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӕ#',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035949.066393:+0000',
                                                                            '20210309:035949.086137:+0000',
                                                                            '20210309:035949.107410:+0000',
                                                                            '20210309:035949.126754:+0000',
                                                                            '20210309:035949.147875:+0000',
                                                                            '20210309:035949.169552:+0000',
                                                                            '20210309:035949.190456:+0000',
                                                                            '20210309:035949.210166:+0000',
                                                                            '20210309:035949.232288:+0000',
                                                                            '20210309:035949.252207:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǒ\x81Ϋʋ\\Шʌύˠǖ¿Ą\x8dŅ˩ʹɒжƫԡԦԅğ&ɾҿҋԕƥX',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035949.346161:+0000',
                                                                            '20210309:035949.362901:+0000',
                                                                            '20210309:035949.379667:+0000',
                                                                            '20210309:035949.396420:+0000',
                                                                            '20210309:035949.414703:+0000',
                                                                            '20210309:035949.433435:+0000',
                                                                            '20210309:035949.452733:+0000',
                                                                            '20210309:035949.472692:+0000',
                                                                            '20210309:035949.492278:+0000',
                                                                            '20210309:035949.512317:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˰ÕЃʛǱҭԚ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 571303.2241273288,
                                                    },
                                    },
                            {
                                        'name': '\x88ƩƱȢΆʗ҈\x94ъҸÃ˛Ԟˆϫΐԋɲ\u038bϒʫ˨˾Ӳŧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            571781.2256410009,
                                                                            364290.1831071214,
                                                                            438975.8730689038,
                                                                            320195.5529475882,
                                                                            716602.9036567125,
                                                                            502652.6590048359,
                                                                            992573.91393211,
                                                                            618299.3679995879,
                                                                            -83705.91699334864,
                                                                            80409.90729666234,
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

            'identifier': 'Ԛѻ\x8bɻŰ',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'Ŀ£',
                    'message': 'ʓ',
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
            'request_id': -892472,
            'error': {
                'identifier': '?ҥɞǟƞη\x8e˶ưϡ¬ÐÅЃƣӤÆɺ\x9fѴ\x93ɍ4ȷɰˊmÁʋʃ',
                'categories': [
                    'network',
                    'invalid-user-action',
                    'os',
                    'os',
                    'file',
                    'network',
                    'invalid-user-action',
                    'internal',
                    'file',
                    'access-restriction',
                ],
                'source': 'ȎƈЍϵϋΑɌ\x83ˬϲ\x8c·҃ҭǲԏƯӧю҃\x99őGЅˮ',
                'messages': [
                    {
                            'catalog': 'ǁ[ƟĖɣɳ:ʺԁăӅϮЇǿ˲ŲȪŋˆ$\x80ԓ˰ɼǱ˵ˢđ\x87¥',
                            'message': 'ɬɨ˯ưÂΝÑδ\u0378Ǎģ!ǜґĦʜĈӏηʜēɾ҈ІҰЁΞ×ƨȵ',
                            'arguments': [
                                        {
                                                        'name': 'ÝτǄǨʳġѳ҇ĳ˳ɾӕэȁԀūˁäϷɫ]Ѣ\u0381ԐµǍƴĥǏҳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '>4ʐøҘο',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˱OĲǎŢΨˆǤǜSԜɇǚӵɽªД˫ϝɏԅĭŜϢǡΈĳƸɑϊ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¥{ÃÞӷUɌԂƌϙĲʺӢ\u038dӑʳŃрѮʲӔUŞdѶėʙķûϱ',
                                                                        },
                                                    },
                                        {
                                                        'name': '1FƢΜӁȧəƬȃđŗΗwǧҰŒѐЎΐʜ\x9e҈\x80˅Ə˕JϪϿè',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϨĂϸӿ5ɯʒ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԦэΧǑŐ(ʫˢљʃΞõ˗ϋĝԫ\x8bѰӬïӦûԧɲĪҘūҠ¿<',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӺɛʷЊʭ¬ΒӜÉΏ0ôϧԀɟԍȯ$¢\u0380ʒDҰǫȭϡÈĎ\x8a¡',
                                                                        },
                                                    },
                                        {
                                                        'name': 'пЌҴ҅|ǻĢϑν×ԛǧŬҕĮ\x8aҫѮԀТ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 814225.5566717162,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ңԕҸΑ˹ʘȟѢӖѰӝƔǆȉɾ˗вРXłƋȳɵůn',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '³ʭҢŸϱūԂʚʷʐͿɂȹίҼȐҽӕαѾώɞҕѩ\u03a2ΉðαϺĂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͱÃϞl˫\xadƀЯʌǓÛԀơΘҚƑЧȲҍπèʼǑVғ¦Ŕɨ©˶',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035921.182632:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѠфэҽȖɯԘ\u0382ĻÆǓҐðΆřʾΙȭƌԧ7ĕЭҧоÃϳǙɼӿ',
                            'message': 'лЖ϶˞ΪЫЌøɂ¢Ѱʹ\x91Ńʖе:3Ԛ˰ΰΡʛўƁņԓƲЋӼ',
                            'arguments': [
                                        {
                                                        'name': 'Ź˯˯ŕ΄ύɮ˰&ǬȭȅԪƊϲԃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬvɰҀɠX\x7fҗŹ¬ɉĊ\x9d0Űǉ҃TǧȕaҺţ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȡ¯',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 955685.4493224784,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёεЌƇʾĕԭūȸˆΣ˯¶¹ΦɐˋʯѦ˧ԐΛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԨũНӼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊҶȹNĊӻӯ-"ȬǼŹˉǕôѯȞџƈԔЇȁί',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉϑɪ¡ԛњЋȤ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϋǘ˛ɋʫUƕÔςҋ°ŗɷǹƟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'èқƠĐιƮŹǝφ¯ћщʡӓüǕ˰=ё\x93ǘөŐĶҳԟԢϹЀz',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӃAx_яĲļȡʚʼMʅƽŝ©Ҝϝƥԫ/íƍɭƀ¾ưϣѻł·',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯ\x91ţèǻΤҳĠɑӘӳ×ǿͻҺ½ҊζǅŘҒчÕɿ҃еȨġƦĠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035922.136317:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '҂5ĳDǹȎƿγɿӕ˜ђèϐ q0əǦϼćƾ ІƩɻѶηȖф',
                            'message': 'ëȮѼɆȒƔ¦ɻӫQџҦ7ӗǢîӆʾϮΉάЫЂ˘ǔȺȽƇғ(',
                            'arguments': [
                                        {
                                                        'name': 'źǧʤь\x99ʔ˭ȰMʵˇˠҪҎԏ>ʢǞѲåiϝȭεɖӚ\x80ϑϪ¡',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 589218.4589140767,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȏ\x81ƐƝɍ˫˸ϬǦȮ`',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035922.396486:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĄĂ˃cɿǪ˜ЈÇѦǔ\x8bǧɏιƾѢϼɞɖāȨҙ²ҩǜӜÎȜȃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝƞԂŋԩǻԗƘȯ5ϧÅԄϨŭϓԃϖгҤл˰%ԫӺ\u0381gͻԚѓ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'đ\x9cͱʄԕȷǶƉΒ[óԀΞ˦ŏŬɟАΔϣ¾Ðʹʻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҍ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԖӜΏБϙΦьΨҔӬƬѫҵȑȫƔоƍŀ˥ѽҷĮļ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "WΎȨОτEuȐѨʭ'ľɱӻТŔԕŘȳЏΙĚюͻԆѭж˃",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4265997928875583011,
                                                                        },
                                                    },
                                        {
                                                        'name': 'р¶',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǗđȔȗMҘłǵϢώӃĒƟƳŘǟȘȤˊιǆˤĖϴήϒʏХǸɛ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ćўκ×ĄҥΌěʜͼЛԍÇаïʉ©§ǖԦʢCҨ˹ϣӿ¿Эˮō',
                            'message': 'Ä+Ɍ\x98\u03a2ӾžÜTԍɶĶʙśĈƪŝɢŤӮKԀР.jƀˌ˓ǺΏ',
                            'arguments': [
                                        {
                                                        'name': 'ŷζưǾҍ³ΗʽŶ3Ԯ˄Ϛ˒ǷČӆŔҌҬ+ȖȮԐΥŎΝșϏԝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͲɘŉĖϗɨ&ϧ˰ѐƮĴȣƤэɅӂūԩЭ/ѓ¼ƦʋĉͲĩo\x7f',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȏƴɑԄфίƧƫîǽʻ\u0378ѝЦÙĘɪɾ°˴ԠΒԞqȔѾˮнŗǂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9cӜҪɊѺÁɳΉǖ7ʙ×οƣ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȚüɐɬPӜƖ~ǻκӿϵμɅЖŅĪͶˌцɼQƝʜȥ±Ԡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƺ˗ԃХÄɄEǁƌȓψρԘĶ>Ǿ¦ď1˜\xadɎϫǢʔбaϿʆú',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʳ҅ɗїӹÖģʖț\x96ϼmğ\\ǜǴάàѿǂʴʑȹϓԔʁӴË[˺',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035923.674662:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƴ˷VŠШΰýɔɷēƞʏʲɤоYѱӋҚϯ˲ΝʳƮɷз',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035923.763970:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɓ\x9cԆѥ˘ʭϾӯ϶ɕžӏϘΛǒȉ©˸',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЎѰοȨɶĝƀ8ʙЬ\x91gȿØǹд˟ǾǧʪφȍȵĹΝ\x8cɫč\x8cȧ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'õҏýƀѱҽ\u0382ĤТΝȉԖϤϕŔȡ¥ȯʅʾϬɿfзͷƫƕŋЫĸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x84ɘ1ǳƴɁZӦϲǕîʻҴ.ҴȩһʠÇʹȜ\x8dǖǏXĨΕ\x87ʧҒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035924.005692:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ƶŴʒԌʻ'ēǛә§ƿκāԤȴѪÚɆҦʞшѷɈŕɭ\x8aҺŘуɺ",
                            'message': 'ӍǠʜѕñɬǙĖӸHѲѯЧī˝ɳ\u03a2ɚɗԓƤ|ŪҐӷλ¦οϐӚ',
                            'arguments': [
                                        {
                                                        'name': 'ʮɘɗɜ·ʽƪ˰ĕĄӘȆЍJσ¾ʓ΅ԁÄǉӧę˳\x8dӺĪͲ;',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2060266773209096364,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȔƥϢ©Ǭ҉F˲ҔǧҌʣKƿƌϏƢюǁƨӤ\x9a!ͼΗƳúǕĻþ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɀˆţtǪ>\x88\x9bʄԎѴʅΗɍƳН¢ȸӉĀѸƁ˸ŁɔϨǧԖҲŋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΐɜǋþɃϹгÐӲʩϼŅŪϷІmϕʼʛҎÙѡȁΪϝȞɑʻʌ\x97',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035924.363024:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0380˵ʏ˝ρȔDϋ˷Ӽ±ͿǔΑǵϫЕɇɷ˵¦',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 330831.1304418683,
                                                                        },
                                                    },
                                        {
                                                        'name': '҅őō>ƗƶςҨϋˮǞ҂ɺʑӣ£҃ŝƁԛʑSǎХŵİЋȑȑɖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035924.522704:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶёԮȺàȵǮϖęҳͲѰĘвțѦұϮ\u0380ε£˜ЖϮѣɌҢˋԉȲ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϓʝ¦\u03a2ІÃ\x92¬8ͲӐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6612470418498487911,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8fȳϠƑʹzϔϡŅWϙӰÂԂǢƴɖ˂ҭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7433554169120751512,
                                                                        },
                                                    },
                                        {
                                                        'name': 'őÄĤQΰ˾əĭӮά',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 414928.0797210565,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƴ\x9dӥҭԟ¬ĥȑ˘',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΣϝӞЕϬȸǅ(ǠȢˬćõԌϰЕӒāǢȟ|Cˠ˥ʱϿʖˉĀŁ',
                            'message': 'ҚÚĳǹʕżѪgӶӐǆÓÏƼǀѲƕƻԟƀԄ6ѤӤ˛ЩʜӵȕЯ',
                            'arguments': [
                                        {
                                                        'name': 'ɌЈϾӊʸȨǌĮʝϵƄZ\u0383҈ǸĎʶ˪j',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 962609.992733218,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁŊŚőѾ}оïǇƥĔȟǚĎĊѐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98Ѧєƒ8ԭҨϩѬ˸ӸĳɚĚРñȠlĊІǬǎΩРӬ¸ʈɚ˭ˣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Φĭ-оЄρʲuЌӦÅuұʞ?ûȩȟқҡȌǀɞϒɢó˺ҎƳϖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØӭдǒНȐŨҤԥƓӇƱ*Һί°ɤœԒԎЪӵčЉ×ȱӗƶÀτ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǛƸЇ\x93ƃӿĕЯǻԡɹҙʮć*ǜˡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔďόDǹ˙Ŀ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘϵǸϸĸǪ˂0ЇÄΛзҸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʧƯҶЫКӑƿХ·ԒӠĘ҇ԙ҈\x95ŏ®ҿё\xa0ъċļƭ¦ɻǻ˒ʮ',
                            'message': '҃ȦΉ\u0383σǇ˘]ͱ9\x8dɌȗͽ¾ϔɶʷӿǨШàАʼѩɓо`Mʖ',
                            'arguments': [
                                        {
                                                        'name': 'ΧԔǇƝĒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѤÞҪ£Ǒ¸ʴÒӭøӣƽƷЉҞĆϕҞӛÒőΓǪʺģϩʊϴɠ®',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'aUж˃yǯԪ˭ӓҚѓΝƹï1ŴÑϖϪԐĨʅϚĴʺ5h',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038bӣŞ΅Ƀ)Ѵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '§ɻÆˌʑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 618480.4948289597,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃѴ˰К5˶/ΌȸŪŽ2ɫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'āɤϓȗƚƙЎʇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƜЮȍϔ˄ƲĖƶŽøƷ\x86ҸϨɏ͵ʡхǼˁƠ¾ǸҾѰŪџϊχ@',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɰҮǭ˙Ӯ§ΓВÀęЯ\xa0âõԉΕȁ˽šǺλǨǼoҀ!ЋԅԚɗ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǈԩϼǃʚȪѺőĭ\x98³+ɾҰķ~\\ԥˊɝƹġ\x9fƁњɃμΒȹĚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѤϚԮŹΠý҃κ˾Ϲ˸Ԡãʂĝʙǫӏѭƛuκȸ˰еƘ˒ëǨζ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇԃĕȳCɧѧƸƩϜʔǇˎȦϭǃ\x99vӅ\u0378ÚӁ|ӭA',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƭ¢ӄ˺ŴϞǟНϦ˘ĭɼϋӭKƓĹөǏан\x89{¬ϞѯœѿŬņ',
                            'message': 'ƼiWǋԘǭǴѷҎōLȚ\x87өFý½sƖ˃Ťʱ҇ȿЏº\x9aéДĳ',
                            'arguments': [
                                        {
                                                        'name': 'Ɓή\x9fэtu\u038dȖ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÝӇϊɶҩΣȂƏԒŃĵȇΡʢԁʢȖ¹ãҰђBŖөϧϷù5ʳԫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Nǖҏҵτǳ<ŽźΌˎΛΑ\x8fǠΦgʒ9ЋҗrƂʢҖśΤҪԎŹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4822152175048124720,
                                                                        },
                                                    },
                                        {
                                                        'name': 'FǹƒҏʰÞ\\ȔˈчV9ŦΙƪҦƝѭŪžǦǸYЬʧʱʘ˺Ȣҵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'άÊƂɣ.ҍȠ\\ŲңJƃȖRμǱɄƽΒǁΆЅΑʁɷѭʜʔʸĉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035927.319894:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'i`9íƼʦȯ΅ĮƦǌȯ}ѝӷшĪ˶ҾʑһȏΕbüϏӅ7ԥŗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƖáѥąƧõȮ\x89ЫЀˌƑʻɂςǠȹȞçжʤŬʼģȐčƮǁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Έ˩G¨ȼдԈȟ϶ÏȺŎ[ԗГsϙ\x86@ΔͱԗūȌʅѕϭϋƛԙ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŊɕЦӘ˸ǯì\x82ϟǝpȓ҅ʔ}єΙë˛ӒӦөȗ?ԃɿu҃Ԋy',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƈżʽȤȢΖӝ҄ɰķɀґ~žØĆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7099874690935668477,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԀȠ\\ȩҘǛÿϚѪǻԂĦԝҾӽ·OӲОQӌȣԇɊʊɜ²ԫĐȟ',
                            'message': '^Ǌ˩ɧΔҙÚĥ\x8c\u038bӺƽԟɯƹЀўƓԗuäĳϕҿљ·ʹЖeǶ',
                            'arguments': [
                                        {
                                                        'name': 'ҡ˟œƁĈϛϮʤʪΜҾʧϨąиљҖσņǆƦ\x9bJϱ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3059795989212222725,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØŨǺʀѨɱхʴʼΑ\x7fԥƪ×ɩԄĦʼР҅ȷү)ɃϪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'jʶŎϣŌнЗŖљβ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƃԗЦ\x94ÄӨwͼâɰɨÓŔÍȀѰϑžԙɅcĖǂԄЬͻɒVǆЀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÆǃƎӒǡʜϏˀȾ˄įǔģÚ®´\x81ңY;ҝǓŎ|˾ѤƓєҺƗ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ý×fęОžɳЃ©ć҂ӼПӆǛćӃȝɡЋȋøӸѤĆȫ°ҭȰŭ',
                                                                        },
                                                    },
                                        {
                                                        'name': '@Ơѳċ˓ɁԦѶ$й\u0379ʺʉƻƁΫ˕˻ǒxΗҏʪÐĊ˔',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035928.294180:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ťМƛ¢æӸNɱǞӎÈͳѯϷʼʬµſϣĊʏЯɌўԁËǚǴͰȷ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊšƗǋιĢƹрғȷΛØΪΰ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035928.547785:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҘƸϨѧѝŷԜðFӈ5Њſ˻\x93ќã\x81уμԢöӌʰʙ\xa0½lȬw',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӸĖԭʆΖɔȼƐϡÊԍϡҲǪϵѣƜϹˢ\\ҹʳ\x95ԉͺƧӴˌʄӮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Δ˥ΰ\x85ҋ\u0380ë˷ωһǋǀϽˀģȹӃѴáɧďҘӑEǊ\x9bв²ŏͶ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Еšу`ǏɏηǦ»XůҊʒҁźzӅϳ,˴ºŇĵȢƇ˟ӬǚɛŃ',
                            'message': 'ԥΗӡ\u0378ʔŷǋʙҫȃdʦƯӥčʃäqǻƩԖ0í҃ɋәɍ¤ʸȍ',
                            'arguments': [
                                        {
                                                        'name': 'њҍƌ˺;˙Č©NÆƫJˁӌȝˇCЩĎ˪Ƀǟ{ČҔȅ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035928.944266:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'âŒʒ\x93Gʛ/ЇԄэŕĊȔͲǑ\x83ȑĄӹɼō˅ȓǶřʒϯϜеҹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Νӻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7982306366530232937,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύxƁɖȩEҟҾͳĢӚvɡƍЍφĚǍƭҼҪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 308821.3368762318,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭ;ɊнŎˮӜ£ʹrӤŢʁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '5ɵǼshƩĦѧ\u03a2ѧȻǀBȃėFҿѢЈǪĠŤϐνCʹĚϺЫʌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ͼǜɆЂҽȜԎ|¾γϳ!ˑхϫʩİĻϔʃ5ѪȞśXƢ˫ѓÇ½',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӼΟϴȸʝѦѸƢëҖԞʽ϶ͺːɎÈǾ҇ɳԊһӎФњ\x8cűɎӵӦ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǙbĵßԋҢүïԖʖԌѰɔψκƶÙµ˓ȤϋϰΆӴˊǼЗϯʜʙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛңŃɦϪ˜ӤĔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 857111.2102700233,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x90Ƿӷ~ІY',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035929.706829:+0000',
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

            'request_id': 2784405,

            'error': {
                'identifier': 'Ҋǂ˶ψK',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ϯҀ',
                            'message': 'Ź',
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
            'nw_x_pixel': 453759125,
            'nw_y_pixel': 134129493,
            'width': -652568445206682491,
            'height': -8314959296375362876,
            'ratio_x': 6673246089614439995,
            'ratio_y': 748049747883420770,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 101206754,

            'nw_y_pixel': 1743608049,

            'width': -7152745350475288076,

            'height': -3318829321148854182,

            'ratio_x': -944855175161406280,

            'ratio_y': -7665514021247754817,

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
                    'nw_x_pixel': -350028800,
                    'nw_y_pixel': 1146999418,
                    'width': -8414631455385534561,
                    'height': -5751126014868391899,
                    'ratio_x': -2014669771218704548,
                    'ratio_y': -1250140954348854325,
                },
                {
                    'nw_x_pixel': -757892299,
                    'nw_y_pixel': 177118868,
                    'width': -4205648588508220889,
                    'height': -2861444672956887325,
                    'ratio_x': -5799465630877339656,
                    'ratio_y': -2155370119150987003,
                },
                {
                    'nw_x_pixel': -1847162857,
                    'nw_y_pixel': 745519892,
                    'width': -6032256328409461187,
                    'height': -8054383463052606471,
                    'ratio_x': 7271963676379451635,
                    'ratio_y': -8865359485402634749,
                },
                {
                    'nw_x_pixel': 1592482969,
                    'nw_y_pixel': 1973747164,
                    'width': -7443290362334370466,
                    'height': -6103616925547826646,
                    'ratio_x': 1858822755060153637,
                    'ratio_y': -6812755893747958047,
                },
                {
                    'nw_x_pixel': 620037099,
                    'nw_y_pixel': 323873124,
                    'width': -4471789338821105749,
                    'height': -3020581376297193321,
                    'ratio_x': -5300983364334545856,
                    'ratio_y': 6634532128203758652,
                },
                {
                    'nw_x_pixel': 623072994,
                    'nw_y_pixel': -1721818210,
                    'width': -2249769693718107884,
                    'height': -3795588100714080677,
                    'ratio_x': 2309035299822610609,
                    'ratio_y': 7906630569172526686,
                },
                {
                    'nw_x_pixel': -125645640,
                    'nw_y_pixel': 221069159,
                    'width': -4630286766691097699,
                    'height': -5907732049703617489,
                    'ratio_x': 7325816330133243265,
                    'ratio_y': -65597515951976311,
                },
                {
                    'nw_x_pixel': -1558520565,
                    'nw_y_pixel': 1050719885,
                    'width': -7984401541065479680,
                    'height': -3363654248218437141,
                    'ratio_x': -5161884337765022570,
                    'ratio_y': -2655919982313227060,
                },
                {
                    'nw_x_pixel': 802476837,
                    'nw_y_pixel': 922279774,
                    'width': -1539602317162388415,
                    'height': -1929219159683270234,
                    'ratio_x': -2975386593496218372,
                    'ratio_y': 7451491776092453697,
                },
                {
                    'nw_x_pixel': -426511538,
                    'nw_y_pixel': -1528160823,
                    'width': -2673455845272659943,
                    'height': -4337387846327307330,
                    'ratio_x': -2652610987027771635,
                    'ratio_y': -4719383490217797937,
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
                    'description': 'Ƚ|ʀЇξӢQźӬˀì·ʺɀĔҺČɇǀǛŇ_˘ƒƛˑ˫IĈĻ',
                    'monitors': [
                            {
                                        'identifier': 4772675,
                                        'width': 5848848969190893513,
                                        'height': 5338113964599246555,
                                    },
                            {
                                        'identifier': 4704145,
                                        'width': 5005637252772966031,
                                        'height': -5801814365716359480,
                                    },
                            {
                                        'identifier': 9620399,
                                        'width': -4074790061566008293,
                                        'height': 2785532424286099123,
                                    },
                            {
                                        'identifier': 2022862,
                                        'width': -4285119810681602233,
                                        'height': 6595793760427614019,
                                    },
                            {
                                        'identifier': 4282710,
                                        'width': -339867091031756530,
                                        'height': 8729425777433291935,
                                    },
                            {
                                        'identifier': 2512648,
                                        'width': -6797658299262047809,
                                        'height': 7393563490308622703,
                                    },
                            {
                                        'identifier': 9174774,
                                        'width': 98982782534656093,
                                        'height': 2386968104549264927,
                                    },
                            {
                                        'identifier': 238411,
                                        'width': -544456976326973397,
                                        'height': 1718502578135509104,
                                    },
                            {
                                        'identifier': -302748,
                                        'width': 5453849933340306708,
                                        'height': -8730190891905270435,
                                    },
                            {
                                        'identifier': 1856796,
                                        'width': 3028123218028628955,
                                        'height': 6935092231089016960,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7909397,
                                        'source_nw_x_pixel': -1711508129765513793,
                                        'source_nw_y_pixel': -2577301760239037631,
                                        'source_pixel_width': -2691714793112853183,
                                        'source_pixel_height': -8122726618586614705,
                                        'rotation': -1397146341348768414,
                                        'virtual_nw_x_pixel': 400669678,
                                        'virtual_nw_y_pixel': -1320689095,
                                        'virtual_width': 126940149,
                                        'virtual_height': 903039572,
                                    },
                            {
                                        'source_monitor': -256591,
                                        'source_nw_x_pixel': -5850122610549650885,
                                        'source_nw_y_pixel': -7405104563860798170,
                                        'source_pixel_width': -450522912093186424,
                                        'source_pixel_height': -3715418445745841028,
                                        'rotation': -4244843143322044123,
                                        'virtual_nw_x_pixel': -1198835663,
                                        'virtual_nw_y_pixel': 533628858,
                                        'virtual_width': -26564466,
                                        'virtual_height': -1337845652,
                                    },
                            {
                                        'source_monitor': 1806727,
                                        'source_nw_x_pixel': -8489673362302240731,
                                        'source_nw_y_pixel': -9133036424550777342,
                                        'source_pixel_width': -1738090582399737411,
                                        'source_pixel_height': -2613752153454798944,
                                        'rotation': -5218754095364755893,
                                        'virtual_nw_x_pixel': -210453695,
                                        'virtual_nw_y_pixel': -1718932925,
                                        'virtual_width': 154328674,
                                        'virtual_height': -533738101,
                                    },
                            {
                                        'source_monitor': 7816736,
                                        'source_nw_x_pixel': -5045869751374391323,
                                        'source_nw_y_pixel': -7947315080589708725,
                                        'source_pixel_width': -6185816738908277667,
                                        'source_pixel_height': -5884694824891135187,
                                        'rotation': -245103894830991047,
                                        'virtual_nw_x_pixel': 584437995,
                                        'virtual_nw_y_pixel': 770196999,
                                        'virtual_width': -1526775260,
                                        'virtual_height': 563618868,
                                    },
                            {
                                        'source_monitor': 2703691,
                                        'source_nw_x_pixel': -5318493120276090884,
                                        'source_nw_y_pixel': -4017840689773879997,
                                        'source_pixel_width': -590226921166846543,
                                        'source_pixel_height': -2653951557073118795,
                                        'rotation': -3829348837318066601,
                                        'virtual_nw_x_pixel': 1721044,
                                        'virtual_nw_y_pixel': -1537521686,
                                        'virtual_width': 740830332,
                                        'virtual_height': -1336161983,
                                    },
                            {
                                        'source_monitor': 7869267,
                                        'source_nw_x_pixel': -7284725535427571767,
                                        'source_nw_y_pixel': -7782519643540717523,
                                        'source_pixel_width': -7178540573736295320,
                                        'source_pixel_height': -3509422634473345772,
                                        'rotation': -4290607514393240404,
                                        'virtual_nw_x_pixel': -518608329,
                                        'virtual_nw_y_pixel': 1752626295,
                                        'virtual_width': -1095464092,
                                        'virtual_height': -1172083570,
                                    },
                            {
                                        'source_monitor': 823585,
                                        'source_nw_x_pixel': -8946775936836662292,
                                        'source_nw_y_pixel': -1168257652204814301,
                                        'source_pixel_width': -7927401011033668140,
                                        'source_pixel_height': -4983759879960516788,
                                        'rotation': -5424552835741668110,
                                        'virtual_nw_x_pixel': 544736706,
                                        'virtual_nw_y_pixel': 829037733,
                                        'virtual_width': 664577514,
                                        'virtual_height': -43503326,
                                    },
                            {
                                        'source_monitor': -651021,
                                        'source_nw_x_pixel': -8510088271056952901,
                                        'source_nw_y_pixel': -382569462060428604,
                                        'source_pixel_width': -3607550094156109561,
                                        'source_pixel_height': -9123518743102409726,
                                        'rotation': -4886342389156929772,
                                        'virtual_nw_x_pixel': 1761084534,
                                        'virtual_nw_y_pixel': 1945515483,
                                        'virtual_width': -276438550,
                                        'virtual_height': 1972868013,
                                    },
                            {
                                        'source_monitor': 9183865,
                                        'source_nw_x_pixel': -1131127203838412227,
                                        'source_nw_y_pixel': -6339910536643929399,
                                        'source_pixel_width': -1990203919282392510,
                                        'source_pixel_height': -8698662865465486841,
                                        'rotation': -1031610296970163750,
                                        'virtual_nw_x_pixel': 1419613859,
                                        'virtual_nw_y_pixel': 1101631610,
                                        'virtual_width': -1572002045,
                                        'virtual_height': -277856851,
                                    },
                            {
                                        'source_monitor': 7381598,
                                        'source_nw_x_pixel': -8065741935847274595,
                                        'source_nw_y_pixel': -5941282283758801405,
                                        'source_pixel_width': -3192154918584738031,
                                        'source_pixel_height': -1359311976957275448,
                                        'rotation': -4432873592714574602,
                                        'virtual_nw_x_pixel': 1636023242,
                                        'virtual_nw_y_pixel': 826812709,
                                        'virtual_width': 1069337811,
                                        'virtual_height': -759726326,
                                    },
                        ],
                },
                {
                    'description': '҈\x9bҌӗįә\xa0A"ˍőʇî\x83Ҏ\x8f\x97ҚĵĲ\x89ǱѼʿǓёÏĀʯɅ',
                    'monitors': [
                            {
                                        'identifier': 911755,
                                        'width': -1251674734633690588,
                                        'height': 8357442185795694490,
                                    },
                            {
                                        'identifier': 7556492,
                                        'width': 581256608439805131,
                                        'height': -2831155244643253099,
                                    },
                            {
                                        'identifier': -774355,
                                        'width': 3037242952634568784,
                                        'height': -7893947963457541923,
                                    },
                            {
                                        'identifier': 7118015,
                                        'width': -5088528678410093731,
                                        'height': -6226685553574720870,
                                    },
                            {
                                        'identifier': 7843316,
                                        'width': 2210036698382064093,
                                        'height': 5704134873908633478,
                                    },
                            {
                                        'identifier': 6463200,
                                        'width': -116998550539027696,
                                        'height': 4690199180165211114,
                                    },
                            {
                                        'identifier': 3159439,
                                        'width': 4889566667629190781,
                                        'height': 8862510770047685693,
                                    },
                            {
                                        'identifier': -707775,
                                        'width': -8083731560785793622,
                                        'height': -4933256348683435899,
                                    },
                            {
                                        'identifier': 7384076,
                                        'width': 5661767880601365152,
                                        'height': 8151579086936892236,
                                    },
                            {
                                        'identifier': 9286210,
                                        'width': -8203422209149844237,
                                        'height': 5892528658086645395,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 99351,
                                        'source_nw_x_pixel': -3162632032055992277,
                                        'source_nw_y_pixel': -8050876969847304430,
                                        'source_pixel_width': -7374741479830154055,
                                        'source_pixel_height': -5335746149799093963,
                                        'rotation': -7668369513836792616,
                                        'virtual_nw_x_pixel': 473175132,
                                        'virtual_nw_y_pixel': -347606598,
                                        'virtual_width': -1387195833,
                                        'virtual_height': 1974714068,
                                    },
                            {
                                        'source_monitor': 3479728,
                                        'source_nw_x_pixel': -3229458760160795080,
                                        'source_nw_y_pixel': -198181717508600872,
                                        'source_pixel_width': -7017704006068760618,
                                        'source_pixel_height': -8532311102487587593,
                                        'rotation': -9163191257649910170,
                                        'virtual_nw_x_pixel': -476635167,
                                        'virtual_nw_y_pixel': 598906631,
                                        'virtual_width': 1713698027,
                                        'virtual_height': -1123815887,
                                    },
                            {
                                        'source_monitor': 5692837,
                                        'source_nw_x_pixel': -5144314989428234740,
                                        'source_nw_y_pixel': -2103394791349714195,
                                        'source_pixel_width': -1479646215847779325,
                                        'source_pixel_height': -4728304143738904737,
                                        'rotation': -3268338717408786961,
                                        'virtual_nw_x_pixel': -1941053939,
                                        'virtual_nw_y_pixel': 1253675494,
                                        'virtual_width': -806552828,
                                        'virtual_height': -1858635218,
                                    },
                            {
                                        'source_monitor': 5847081,
                                        'source_nw_x_pixel': -8233959261450354516,
                                        'source_nw_y_pixel': -3662841628354984617,
                                        'source_pixel_width': -1794226697200814566,
                                        'source_pixel_height': -2124917719562521666,
                                        'rotation': -2545134871620263615,
                                        'virtual_nw_x_pixel': 1400462396,
                                        'virtual_nw_y_pixel': -1367125648,
                                        'virtual_width': 17212352,
                                        'virtual_height': 1889847697,
                                    },
                            {
                                        'source_monitor': 8096351,
                                        'source_nw_x_pixel': -6938239777589144052,
                                        'source_nw_y_pixel': -5876637385124030450,
                                        'source_pixel_width': -2361963342038531497,
                                        'source_pixel_height': -6257163424190178961,
                                        'rotation': -66274979889596403,
                                        'virtual_nw_x_pixel': 1904856854,
                                        'virtual_nw_y_pixel': 1674448055,
                                        'virtual_width': 1965033305,
                                        'virtual_height': 1356844761,
                                    },
                            {
                                        'source_monitor': 7880410,
                                        'source_nw_x_pixel': -3835874578623890004,
                                        'source_nw_y_pixel': -4571247926548534091,
                                        'source_pixel_width': -7094335637451996157,
                                        'source_pixel_height': -3646850873779171339,
                                        'rotation': -2274150893441535988,
                                        'virtual_nw_x_pixel': -783592050,
                                        'virtual_nw_y_pixel': 743782083,
                                        'virtual_width': 1729751029,
                                        'virtual_height': -1933001938,
                                    },
                            {
                                        'source_monitor': 296173,
                                        'source_nw_x_pixel': -1148462836209691645,
                                        'source_nw_y_pixel': -2634502724576749939,
                                        'source_pixel_width': -5073788066518931852,
                                        'source_pixel_height': -2756994657848090984,
                                        'rotation': -6481290308033724825,
                                        'virtual_nw_x_pixel': -1533368908,
                                        'virtual_nw_y_pixel': 1089027490,
                                        'virtual_width': -979281856,
                                        'virtual_height': -115219886,
                                    },
                            {
                                        'source_monitor': 6776133,
                                        'source_nw_x_pixel': -366011549184652972,
                                        'source_nw_y_pixel': -5928574037099169288,
                                        'source_pixel_width': -5959735656587852849,
                                        'source_pixel_height': -6006156212336042509,
                                        'rotation': -8559824362369353467,
                                        'virtual_nw_x_pixel': 66339836,
                                        'virtual_nw_y_pixel': 588547372,
                                        'virtual_width': 49506057,
                                        'virtual_height': 1616634940,
                                    },
                            {
                                        'source_monitor': 2181738,
                                        'source_nw_x_pixel': -1052664731141522593,
                                        'source_nw_y_pixel': -7700775387358666941,
                                        'source_pixel_width': -1303680203447369416,
                                        'source_pixel_height': -3336325029536225035,
                                        'rotation': -8699679817904547189,
                                        'virtual_nw_x_pixel': 1571505126,
                                        'virtual_nw_y_pixel': 1471831668,
                                        'virtual_width': 1351903926,
                                        'virtual_height': -1136107641,
                                    },
                            {
                                        'source_monitor': -931213,
                                        'source_nw_x_pixel': -1510590413460587118,
                                        'source_nw_y_pixel': -9212395456963365265,
                                        'source_pixel_width': -1098872061801171317,
                                        'source_pixel_height': -2637663487539928178,
                                        'rotation': -3298217289294712241,
                                        'virtual_nw_x_pixel': -1027033328,
                                        'virtual_nw_y_pixel': 635574234,
                                        'virtual_width': 1650943003,
                                        'virtual_height': 502977728,
                                    },
                        ],
                },
                {
                    'description': 'Ӊϊ)ƣɧmέkgɲͶÌ4ƥɟɊϊɈɑҼƮoȃb³ɌŮӇMѡ',
                    'monitors': [
                            {
                                        'identifier': 3861301,
                                        'width': 8520588832772043401,
                                        'height': -7931488767777865845,
                                    },
                            {
                                        'identifier': -606776,
                                        'width': 7655242990502613860,
                                        'height': -4104770828756342014,
                                    },
                            {
                                        'identifier': 8559293,
                                        'width': 2893929507108503520,
                                        'height': 1627557615482917307,
                                    },
                            {
                                        'identifier': 4390251,
                                        'width': 8107008527274621682,
                                        'height': 7183391707691897861,
                                    },
                            {
                                        'identifier': 3375964,
                                        'width': 8545516389027106014,
                                        'height': 6162740273159826117,
                                    },
                            {
                                        'identifier': 7309951,
                                        'width': 1752078444319409283,
                                        'height': -4545030369889073808,
                                    },
                            {
                                        'identifier': -535440,
                                        'width': 7021150015052439057,
                                        'height': -3145696919849179257,
                                    },
                            {
                                        'identifier': 157512,
                                        'width': -3304307143276182634,
                                        'height': -6652768272863702591,
                                    },
                            {
                                        'identifier': 7109489,
                                        'width': 8681796054052926177,
                                        'height': 3715018298716793785,
                                    },
                            {
                                        'identifier': 8028223,
                                        'width': -4409187869274060436,
                                        'height': -1225269979788544425,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2351841,
                                        'source_nw_x_pixel': -4736905203796141581,
                                        'source_nw_y_pixel': -2124923588738392947,
                                        'source_pixel_width': -2115022208594487432,
                                        'source_pixel_height': -7281112510539882536,
                                        'rotation': -7616736251793779107,
                                        'virtual_nw_x_pixel': 464141580,
                                        'virtual_nw_y_pixel': 1857045966,
                                        'virtual_width': -300094796,
                                        'virtual_height': 506109516,
                                    },
                            {
                                        'source_monitor': 9209923,
                                        'source_nw_x_pixel': -6536799284778638077,
                                        'source_nw_y_pixel': -273434272956391978,
                                        'source_pixel_width': -158196257453045788,
                                        'source_pixel_height': -499643052466653640,
                                        'rotation': -315503198389640771,
                                        'virtual_nw_x_pixel': 1465221074,
                                        'virtual_nw_y_pixel': -1919784182,
                                        'virtual_width': -1980063708,
                                        'virtual_height': -642139781,
                                    },
                            {
                                        'source_monitor': 1294257,
                                        'source_nw_x_pixel': -9124229983030502951,
                                        'source_nw_y_pixel': -2834758023832669951,
                                        'source_pixel_width': -1900038557333037288,
                                        'source_pixel_height': -680087196148632582,
                                        'rotation': -10320611888061304,
                                        'virtual_nw_x_pixel': 1724778854,
                                        'virtual_nw_y_pixel': -1497348901,
                                        'virtual_width': -1781283658,
                                        'virtual_height': 1972732305,
                                    },
                            {
                                        'source_monitor': 1491494,
                                        'source_nw_x_pixel': -3960756967149524721,
                                        'source_nw_y_pixel': -3200436426380408129,
                                        'source_pixel_width': -5955378921306516403,
                                        'source_pixel_height': -8700835081942197547,
                                        'rotation': -4036510632108058479,
                                        'virtual_nw_x_pixel': 450205950,
                                        'virtual_nw_y_pixel': 1402182938,
                                        'virtual_width': 300537574,
                                        'virtual_height': -130417966,
                                    },
                            {
                                        'source_monitor': 6730084,
                                        'source_nw_x_pixel': -8588780537402839741,
                                        'source_nw_y_pixel': -7488087788837421193,
                                        'source_pixel_width': -4322125858414165489,
                                        'source_pixel_height': -1325115047504987913,
                                        'rotation': -1600119965002804564,
                                        'virtual_nw_x_pixel': 1949153100,
                                        'virtual_nw_y_pixel': -98024786,
                                        'virtual_width': -1497620637,
                                        'virtual_height': 1151944502,
                                    },
                            {
                                        'source_monitor': 5334822,
                                        'source_nw_x_pixel': -2221004827108716008,
                                        'source_nw_y_pixel': -5443882760753384552,
                                        'source_pixel_width': -2984073796903954757,
                                        'source_pixel_height': -1114933655894874265,
                                        'rotation': -2057328699857233754,
                                        'virtual_nw_x_pixel': 80379253,
                                        'virtual_nw_y_pixel': 1765576459,
                                        'virtual_width': -571524123,
                                        'virtual_height': 1474036043,
                                    },
                            {
                                        'source_monitor': 9796674,
                                        'source_nw_x_pixel': -7219687635717063221,
                                        'source_nw_y_pixel': -6681094592726626623,
                                        'source_pixel_width': -8844534185049824666,
                                        'source_pixel_height': -2704588574448396297,
                                        'rotation': -2725886689388151047,
                                        'virtual_nw_x_pixel': -1769410733,
                                        'virtual_nw_y_pixel': 801922385,
                                        'virtual_width': 897889398,
                                        'virtual_height': -44723229,
                                    },
                            {
                                        'source_monitor': 5350653,
                                        'source_nw_x_pixel': -1304072962494745591,
                                        'source_nw_y_pixel': -7785343683374018104,
                                        'source_pixel_width': -4209189787385946065,
                                        'source_pixel_height': -1539222642723607847,
                                        'rotation': -3659567665800745609,
                                        'virtual_nw_x_pixel': 149855127,
                                        'virtual_nw_y_pixel': -1359844316,
                                        'virtual_width': -26369591,
                                        'virtual_height': 1588882586,
                                    },
                            {
                                        'source_monitor': 4059033,
                                        'source_nw_x_pixel': -4014786384035909523,
                                        'source_nw_y_pixel': -315242634002405665,
                                        'source_pixel_width': -5056602623497149176,
                                        'source_pixel_height': -4522056539982504249,
                                        'rotation': -2369128144481795192,
                                        'virtual_nw_x_pixel': 686732922,
                                        'virtual_nw_y_pixel': -946575554,
                                        'virtual_width': 1951598621,
                                        'virtual_height': -1891098945,
                                    },
                            {
                                        'source_monitor': 7291636,
                                        'source_nw_x_pixel': -928860906290473623,
                                        'source_nw_y_pixel': -4053241069070869604,
                                        'source_pixel_width': -7235852801175111306,
                                        'source_pixel_height': -1193110561273556858,
                                        'rotation': -3091135680957027575,
                                        'virtual_nw_x_pixel': -1122723895,
                                        'virtual_nw_y_pixel': -679402364,
                                        'virtual_width': 1816312224,
                                        'virtual_height': 836109065,
                                    },
                        ],
                },
                {
                    'description': 'ƧΧԂɄӲҘÔMɵªȵT\u03a2ѭҞĪǪǃψѨƫEӛǭsɺ¶ЩЯ˴',
                    'monitors': [
                            {
                                        'identifier': 7048164,
                                        'width': -2190207831256574565,
                                        'height': -2035568636785171296,
                                    },
                            {
                                        'identifier': 4911643,
                                        'width': 3056348203068345412,
                                        'height': -4264718948789971861,
                                    },
                            {
                                        'identifier': 985419,
                                        'width': -3745783923909268283,
                                        'height': 6837808049829564660,
                                    },
                            {
                                        'identifier': 4301975,
                                        'width': 5881116506402875103,
                                        'height': -4751488597811779716,
                                    },
                            {
                                        'identifier': 5166398,
                                        'width': 6566078208609544624,
                                        'height': 8203928624886628061,
                                    },
                            {
                                        'identifier': 1799433,
                                        'width': -1491774873700702283,
                                        'height': -6845580455007467098,
                                    },
                            {
                                        'identifier': -792008,
                                        'width': 6050201612697510518,
                                        'height': -1847501792277332232,
                                    },
                            {
                                        'identifier': 6859473,
                                        'width': 7107648618509530290,
                                        'height': 593492895679592872,
                                    },
                            {
                                        'identifier': 7169863,
                                        'width': 591314385706917908,
                                        'height': -1785465762376236212,
                                    },
                            {
                                        'identifier': 3570419,
                                        'width': -9156531539646549991,
                                        'height': 5377462414686708802,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8602248,
                                        'source_nw_x_pixel': -2317027073122059275,
                                        'source_nw_y_pixel': -2465383880229121800,
                                        'source_pixel_width': -3934973213401646273,
                                        'source_pixel_height': -8744357614497478889,
                                        'rotation': -6821491407117668346,
                                        'virtual_nw_x_pixel': -1275039605,
                                        'virtual_nw_y_pixel': 270934565,
                                        'virtual_width': -401411685,
                                        'virtual_height': 1781043522,
                                    },
                            {
                                        'source_monitor': 8756660,
                                        'source_nw_x_pixel': -1381337813232618634,
                                        'source_nw_y_pixel': -4363176989506413394,
                                        'source_pixel_width': -1147978424771852240,
                                        'source_pixel_height': -8931154790628504665,
                                        'rotation': -5154458672579323733,
                                        'virtual_nw_x_pixel': -690652941,
                                        'virtual_nw_y_pixel': -1747206060,
                                        'virtual_width': -1900177836,
                                        'virtual_height': -852648458,
                                    },
                            {
                                        'source_monitor': 5350724,
                                        'source_nw_x_pixel': -5093596238110049594,
                                        'source_nw_y_pixel': -6255550496530376815,
                                        'source_pixel_width': -6503793983208439591,
                                        'source_pixel_height': -8689948019341019593,
                                        'rotation': -5780158898686253849,
                                        'virtual_nw_x_pixel': 368855060,
                                        'virtual_nw_y_pixel': -237003570,
                                        'virtual_width': -1979894626,
                                        'virtual_height': 987029869,
                                    },
                            {
                                        'source_monitor': 3408615,
                                        'source_nw_x_pixel': -4698193371173030987,
                                        'source_nw_y_pixel': -1553167848731431698,
                                        'source_pixel_width': -713920802106657283,
                                        'source_pixel_height': -7037907856436218204,
                                        'rotation': -5764389946128916413,
                                        'virtual_nw_x_pixel': -1937496828,
                                        'virtual_nw_y_pixel': -1081722667,
                                        'virtual_width': 247499234,
                                        'virtual_height': 1075401685,
                                    },
                            {
                                        'source_monitor': -906875,
                                        'source_nw_x_pixel': -6281558313306147844,
                                        'source_nw_y_pixel': -8158144547040464824,
                                        'source_pixel_width': -6549358667777694843,
                                        'source_pixel_height': -4241344080493236444,
                                        'rotation': -6676483209641356822,
                                        'virtual_nw_x_pixel': 370556624,
                                        'virtual_nw_y_pixel': 1497829489,
                                        'virtual_width': -1899356430,
                                        'virtual_height': 1559169952,
                                    },
                            {
                                        'source_monitor': 2126595,
                                        'source_nw_x_pixel': -8318871529879283085,
                                        'source_nw_y_pixel': -6214004231485613182,
                                        'source_pixel_width': -8065026523928484328,
                                        'source_pixel_height': -8804033841710286302,
                                        'rotation': -4187757258448604633,
                                        'virtual_nw_x_pixel': 1280855870,
                                        'virtual_nw_y_pixel': -942700117,
                                        'virtual_width': -864511962,
                                        'virtual_height': -1037151180,
                                    },
                            {
                                        'source_monitor': 7980500,
                                        'source_nw_x_pixel': -4513215798813670686,
                                        'source_nw_y_pixel': -4685671982728392252,
                                        'source_pixel_width': -4247122267684135672,
                                        'source_pixel_height': -7888272138976205071,
                                        'rotation': -1515041706198206600,
                                        'virtual_nw_x_pixel': 638720111,
                                        'virtual_nw_y_pixel': -1486815887,
                                        'virtual_width': -778023571,
                                        'virtual_height': -225285954,
                                    },
                            {
                                        'source_monitor': 7551498,
                                        'source_nw_x_pixel': -1383134366687202591,
                                        'source_nw_y_pixel': -8990823217894968510,
                                        'source_pixel_width': -3741592547185902827,
                                        'source_pixel_height': -4670074425497404298,
                                        'rotation': -6284904688811863269,
                                        'virtual_nw_x_pixel': -1366617525,
                                        'virtual_nw_y_pixel': -816776440,
                                        'virtual_width': -366850099,
                                        'virtual_height': -864259175,
                                    },
                            {
                                        'source_monitor': 7420890,
                                        'source_nw_x_pixel': -1963012394859636697,
                                        'source_nw_y_pixel': -3315796132186056578,
                                        'source_pixel_width': -8420562142947841602,
                                        'source_pixel_height': -7018271944858399714,
                                        'rotation': -8951483269988521079,
                                        'virtual_nw_x_pixel': 1192543627,
                                        'virtual_nw_y_pixel': 864794092,
                                        'virtual_width': -248855476,
                                        'virtual_height': 49246669,
                                    },
                            {
                                        'source_monitor': 7987453,
                                        'source_nw_x_pixel': -23503829786795376,
                                        'source_nw_y_pixel': -5050057459097214376,
                                        'source_pixel_width': -8478267363886995260,
                                        'source_pixel_height': -364433035401899962,
                                        'rotation': -5810167605263874316,
                                        'virtual_nw_x_pixel': -667716260,
                                        'virtual_nw_y_pixel': -1835654181,
                                        'virtual_width': 733895810,
                                        'virtual_height': 761749148,
                                    },
                        ],
                },
                {
                    'description': 'ɋƶŬĚαЌÕǌńșţΓʣϯà˻Úϓ˼uпʎǙθұќύϴѰN',
                    'monitors': [
                            {
                                        'identifier': 9298019,
                                        'width': 883964447297102037,
                                        'height': 7511685663707356184,
                                    },
                            {
                                        'identifier': 3958796,
                                        'width': 6938610805199816978,
                                        'height': -6348719390522430630,
                                    },
                            {
                                        'identifier': 3239562,
                                        'width': -6785077194271497384,
                                        'height': -1633810977812701095,
                                    },
                            {
                                        'identifier': 4874550,
                                        'width': 2373602784420993776,
                                        'height': -1787505444839525510,
                                    },
                            {
                                        'identifier': 4259603,
                                        'width': 5988658445951399546,
                                        'height': 5381831534604401178,
                                    },
                            {
                                        'identifier': 1702491,
                                        'width': -1172984298697861033,
                                        'height': 197692102388199757,
                                    },
                            {
                                        'identifier': -493981,
                                        'width': -4944447298112929624,
                                        'height': 7001039110825274646,
                                    },
                            {
                                        'identifier': 3332949,
                                        'width': -8244836413870490469,
                                        'height': -8587806013248652148,
                                    },
                            {
                                        'identifier': 6160965,
                                        'width': -6727556642457604884,
                                        'height': -2494751398657977900,
                                    },
                            {
                                        'identifier': 8093731,
                                        'width': -2757647516309673721,
                                        'height': -1317431236746681757,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4668038,
                                        'source_nw_x_pixel': -2843873473928090041,
                                        'source_nw_y_pixel': -6498471852802282975,
                                        'source_pixel_width': -180407977850041221,
                                        'source_pixel_height': -2356054974482771962,
                                        'rotation': -2363409085169482692,
                                        'virtual_nw_x_pixel': 1717248653,
                                        'virtual_nw_y_pixel': -282199562,
                                        'virtual_width': -1978630392,
                                        'virtual_height': 996659948,
                                    },
                            {
                                        'source_monitor': 2674259,
                                        'source_nw_x_pixel': -3019108484671313776,
                                        'source_nw_y_pixel': -8523525305192011591,
                                        'source_pixel_width': -6474589859650976194,
                                        'source_pixel_height': -3405580434396308770,
                                        'rotation': -1896490218177936282,
                                        'virtual_nw_x_pixel': 1395235334,
                                        'virtual_nw_y_pixel': -736119057,
                                        'virtual_width': -1943589829,
                                        'virtual_height': -418197951,
                                    },
                            {
                                        'source_monitor': 5079992,
                                        'source_nw_x_pixel': -6346705744748925022,
                                        'source_nw_y_pixel': -4737048177712739478,
                                        'source_pixel_width': -3073772818978472438,
                                        'source_pixel_height': -459641791786149183,
                                        'rotation': -335044537177349239,
                                        'virtual_nw_x_pixel': 1236388294,
                                        'virtual_nw_y_pixel': 558824570,
                                        'virtual_width': -1721934114,
                                        'virtual_height': 1360112278,
                                    },
                            {
                                        'source_monitor': 4454941,
                                        'source_nw_x_pixel': -1626573454184941311,
                                        'source_nw_y_pixel': -1490004592122246502,
                                        'source_pixel_width': -7538905736089795184,
                                        'source_pixel_height': -7927575615310448862,
                                        'rotation': -7384282261663360765,
                                        'virtual_nw_x_pixel': 1346165164,
                                        'virtual_nw_y_pixel': -630126509,
                                        'virtual_width': 695727654,
                                        'virtual_height': -144573195,
                                    },
                            {
                                        'source_monitor': 784292,
                                        'source_nw_x_pixel': -3926308420792476816,
                                        'source_nw_y_pixel': -7198927110286082444,
                                        'source_pixel_width': -8559821345900893061,
                                        'source_pixel_height': -7822677510662503579,
                                        'rotation': -5014677786555331372,
                                        'virtual_nw_x_pixel': -601453694,
                                        'virtual_nw_y_pixel': -176011858,
                                        'virtual_width': 47103226,
                                        'virtual_height': 464546001,
                                    },
                            {
                                        'source_monitor': 105945,
                                        'source_nw_x_pixel': -1945964015469213169,
                                        'source_nw_y_pixel': -1718927301528705483,
                                        'source_pixel_width': -2685283842245215572,
                                        'source_pixel_height': -2140722696065170846,
                                        'rotation': -4017790360820183818,
                                        'virtual_nw_x_pixel': 1898433244,
                                        'virtual_nw_y_pixel': 1360397014,
                                        'virtual_width': 1696377712,
                                        'virtual_height': -503076397,
                                    },
                            {
                                        'source_monitor': 1961634,
                                        'source_nw_x_pixel': -6302591721423327453,
                                        'source_nw_y_pixel': -1243600509937049088,
                                        'source_pixel_width': -3041504371704191007,
                                        'source_pixel_height': -4177086289791195271,
                                        'rotation': -5210859831907345226,
                                        'virtual_nw_x_pixel': 283706938,
                                        'virtual_nw_y_pixel': -43849137,
                                        'virtual_width': 190923831,
                                        'virtual_height': -106699832,
                                    },
                            {
                                        'source_monitor': 646698,
                                        'source_nw_x_pixel': -2783464647041996765,
                                        'source_nw_y_pixel': -1655873354845528111,
                                        'source_pixel_width': -2020838704786362417,
                                        'source_pixel_height': -294890465850984077,
                                        'rotation': -2019920757103820582,
                                        'virtual_nw_x_pixel': 392985771,
                                        'virtual_nw_y_pixel': 1238456906,
                                        'virtual_width': 1578973437,
                                        'virtual_height': -205226128,
                                    },
                            {
                                        'source_monitor': 3023415,
                                        'source_nw_x_pixel': -6820817851163212428,
                                        'source_nw_y_pixel': -1571391479318962367,
                                        'source_pixel_width': -3471016475320358494,
                                        'source_pixel_height': -5788817992690432417,
                                        'rotation': -4498110463147237989,
                                        'virtual_nw_x_pixel': 1248175683,
                                        'virtual_nw_y_pixel': -951677777,
                                        'virtual_width': 1578260637,
                                        'virtual_height': -250207780,
                                    },
                            {
                                        'source_monitor': 8484838,
                                        'source_nw_x_pixel': -8480729433533286618,
                                        'source_nw_y_pixel': -3270117954044919864,
                                        'source_pixel_width': -7857652781246602640,
                                        'source_pixel_height': -1716072141215977097,
                                        'rotation': -373113929952764271,
                                        'virtual_nw_x_pixel': -133975569,
                                        'virtual_nw_y_pixel': 104784904,
                                        'virtual_width': 408461291,
                                        'virtual_height': 926894706,
                                    },
                        ],
                },
                {
                    'description': 'ӄюԨÐ˒ȱŧăѦӔ1ƍǩȐ˟ҕǦǉǵӣ"˵Ǻҝ~йԅѮJӈ',
                    'monitors': [
                            {
                                        'identifier': 4018512,
                                        'width': -7360854716892388079,
                                        'height': 6218220802943826813,
                                    },
                            {
                                        'identifier': 7468851,
                                        'width': -5882456545750643815,
                                        'height': 6162970847238098998,
                                    },
                            {
                                        'identifier': 3401380,
                                        'width': -497057979087847504,
                                        'height': -4134172631647895787,
                                    },
                            {
                                        'identifier': 5991013,
                                        'width': 2269348147561265904,
                                        'height': -2655219390432167565,
                                    },
                            {
                                        'identifier': 3961176,
                                        'width': 2028404669161091577,
                                        'height': -7264138724090020716,
                                    },
                            {
                                        'identifier': 6449692,
                                        'width': 1416256834776349209,
                                        'height': 6812028353800475532,
                                    },
                            {
                                        'identifier': 1400263,
                                        'width': -5818211143878158467,
                                        'height': -7344543452587158623,
                                    },
                            {
                                        'identifier': 9210666,
                                        'width': -6002480047959768164,
                                        'height': 1911246214872555615,
                                    },
                            {
                                        'identifier': 5071653,
                                        'width': 2936400640115648942,
                                        'height': -1226861051015988047,
                                    },
                            {
                                        'identifier': 6867992,
                                        'width': -6018212328180981088,
                                        'height': -2862860082137590540,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8644652,
                                        'source_nw_x_pixel': -8698797863867922566,
                                        'source_nw_y_pixel': -8774081778648171664,
                                        'source_pixel_width': -521402689871002848,
                                        'source_pixel_height': -9007556224290401757,
                                        'rotation': -77792834803914814,
                                        'virtual_nw_x_pixel': 212406020,
                                        'virtual_nw_y_pixel': 1271544593,
                                        'virtual_width': 813072719,
                                        'virtual_height': -676021460,
                                    },
                            {
                                        'source_monitor': -461631,
                                        'source_nw_x_pixel': -1450649956794344069,
                                        'source_nw_y_pixel': -2856697280788389856,
                                        'source_pixel_width': -4264945676715022615,
                                        'source_pixel_height': -7961220244875578319,
                                        'rotation': -5480229703129150195,
                                        'virtual_nw_x_pixel': -830414944,
                                        'virtual_nw_y_pixel': -1811816537,
                                        'virtual_width': 250789089,
                                        'virtual_height': 1790109550,
                                    },
                            {
                                        'source_monitor': 4948368,
                                        'source_nw_x_pixel': -5032356169447247153,
                                        'source_nw_y_pixel': -5109632217893595187,
                                        'source_pixel_width': -7955514403201040623,
                                        'source_pixel_height': -4679671652031103475,
                                        'rotation': -4311796090537458906,
                                        'virtual_nw_x_pixel': 59764934,
                                        'virtual_nw_y_pixel': -9254865,
                                        'virtual_width': -1095783087,
                                        'virtual_height': 350040996,
                                    },
                            {
                                        'source_monitor': 8000355,
                                        'source_nw_x_pixel': -4553273818800579114,
                                        'source_nw_y_pixel': -596039939597016507,
                                        'source_pixel_width': -599729981189260116,
                                        'source_pixel_height': -2787351140348975294,
                                        'rotation': -6195271334903151126,
                                        'virtual_nw_x_pixel': 782018672,
                                        'virtual_nw_y_pixel': -1399860400,
                                        'virtual_width': 1694027630,
                                        'virtual_height': -858333905,
                                    },
                            {
                                        'source_monitor': 5151414,
                                        'source_nw_x_pixel': -1801108900184937429,
                                        'source_nw_y_pixel': -1138728316309765814,
                                        'source_pixel_width': -3492223028585175920,
                                        'source_pixel_height': -7803797897851398716,
                                        'rotation': -7073133147302697308,
                                        'virtual_nw_x_pixel': -1122945426,
                                        'virtual_nw_y_pixel': -1044582161,
                                        'virtual_width': 1268554658,
                                        'virtual_height': -1147502035,
                                    },
                            {
                                        'source_monitor': -733466,
                                        'source_nw_x_pixel': -1784850616479260885,
                                        'source_nw_y_pixel': -2990601225778046118,
                                        'source_pixel_width': -4440452993289117647,
                                        'source_pixel_height': -8857711058197682518,
                                        'rotation': -2405290731878964523,
                                        'virtual_nw_x_pixel': 916993935,
                                        'virtual_nw_y_pixel': 883984870,
                                        'virtual_width': 236948762,
                                        'virtual_height': -407842513,
                                    },
                            {
                                        'source_monitor': 2561298,
                                        'source_nw_x_pixel': -3379201987581551530,
                                        'source_nw_y_pixel': -2059364199401563298,
                                        'source_pixel_width': -2461820513590494865,
                                        'source_pixel_height': -218179351199661291,
                                        'rotation': -4194822280409153317,
                                        'virtual_nw_x_pixel': -934834115,
                                        'virtual_nw_y_pixel': 497522075,
                                        'virtual_width': -765760811,
                                        'virtual_height': 1766869662,
                                    },
                            {
                                        'source_monitor': 583842,
                                        'source_nw_x_pixel': -5683405129941193927,
                                        'source_nw_y_pixel': -8860590310459697111,
                                        'source_pixel_width': -9027924150972084705,
                                        'source_pixel_height': -7954811860605600550,
                                        'rotation': -8173937984442959697,
                                        'virtual_nw_x_pixel': 586366412,
                                        'virtual_nw_y_pixel': 1001731933,
                                        'virtual_width': -208471168,
                                        'virtual_height': -36154182,
                                    },
                            {
                                        'source_monitor': 5271587,
                                        'source_nw_x_pixel': -2471101762774823530,
                                        'source_nw_y_pixel': -2449441900344128662,
                                        'source_pixel_width': -3801325546051386667,
                                        'source_pixel_height': -3546922868147887704,
                                        'rotation': -6102720651490066058,
                                        'virtual_nw_x_pixel': -576970998,
                                        'virtual_nw_y_pixel': -515641139,
                                        'virtual_width': 498590860,
                                        'virtual_height': 1377258368,
                                    },
                            {
                                        'source_monitor': 8651090,
                                        'source_nw_x_pixel': -9008471904467808840,
                                        'source_nw_y_pixel': -1502244841735692878,
                                        'source_pixel_width': -8588515538075021868,
                                        'source_pixel_height': -5665709277918112850,
                                        'rotation': -1802854594636670480,
                                        'virtual_nw_x_pixel': -1877214072,
                                        'virtual_nw_y_pixel': -1448567160,
                                        'virtual_width': -1683408413,
                                        'virtual_height': 440929669,
                                    },
                        ],
                },
                {
                    'description': 'ϘůĒϯϰ^ѯҋQˀԢǷƦˠșΉƭҗҵˈÎ7ɽςùϦaǌεʯ',
                    'monitors': [
                            {
                                        'identifier': 4553926,
                                        'width': 4241880595408065420,
                                        'height': 654210581968614782,
                                    },
                            {
                                        'identifier': 5463047,
                                        'width': 1228395659929423531,
                                        'height': -3802016835499169278,
                                    },
                            {
                                        'identifier': 3621896,
                                        'width': 8106696336692493915,
                                        'height': 2743509504008707412,
                                    },
                            {
                                        'identifier': -227170,
                                        'width': -8897222287091859639,
                                        'height': -3999911222941974803,
                                    },
                            {
                                        'identifier': 1126133,
                                        'width': -3436969872104272578,
                                        'height': 3430523446823271451,
                                    },
                            {
                                        'identifier': 3208622,
                                        'width': 4035793047341228687,
                                        'height': 1010030399327538659,
                                    },
                            {
                                        'identifier': 1987286,
                                        'width': 5174862455621883185,
                                        'height': -6017646636229325687,
                                    },
                            {
                                        'identifier': 9605878,
                                        'width': 259830029491769650,
                                        'height': -322992813589851053,
                                    },
                            {
                                        'identifier': 1844328,
                                        'width': -51074295040291657,
                                        'height': 2152849683104266502,
                                    },
                            {
                                        'identifier': 8687095,
                                        'width': -5944010624892158155,
                                        'height': -4323169755005418625,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2101842,
                                        'source_nw_x_pixel': -1734294295671729616,
                                        'source_nw_y_pixel': -6267138729818537318,
                                        'source_pixel_width': -8852160727540118314,
                                        'source_pixel_height': -6178158026427904092,
                                        'rotation': -5840555832636598780,
                                        'virtual_nw_x_pixel': -1387865192,
                                        'virtual_nw_y_pixel': -1673645297,
                                        'virtual_width': -995025470,
                                        'virtual_height': 1409034880,
                                    },
                            {
                                        'source_monitor': 5304872,
                                        'source_nw_x_pixel': -3860419917042510682,
                                        'source_nw_y_pixel': -2821702045597853228,
                                        'source_pixel_width': -8526238702426964641,
                                        'source_pixel_height': -8884479818259367021,
                                        'rotation': -4771966561916240858,
                                        'virtual_nw_x_pixel': -1259328951,
                                        'virtual_nw_y_pixel': -564699453,
                                        'virtual_width': 466017896,
                                        'virtual_height': -1646322040,
                                    },
                            {
                                        'source_monitor': 3125443,
                                        'source_nw_x_pixel': -5131781082597668702,
                                        'source_nw_y_pixel': -6913485091449919439,
                                        'source_pixel_width': -3449457891121539972,
                                        'source_pixel_height': -7343091714005370980,
                                        'rotation': -760845777552472076,
                                        'virtual_nw_x_pixel': 1997632570,
                                        'virtual_nw_y_pixel': -628188879,
                                        'virtual_width': -1825889022,
                                        'virtual_height': -1593120091,
                                    },
                            {
                                        'source_monitor': 5924888,
                                        'source_nw_x_pixel': -962207236035612783,
                                        'source_nw_y_pixel': -5414334061608311966,
                                        'source_pixel_width': -5811040278409482380,
                                        'source_pixel_height': -8594409712682422081,
                                        'rotation': -5109368640596888,
                                        'virtual_nw_x_pixel': 1924820807,
                                        'virtual_nw_y_pixel': -693459583,
                                        'virtual_width': -1300159631,
                                        'virtual_height': 413133057,
                                    },
                            {
                                        'source_monitor': 2667516,
                                        'source_nw_x_pixel': -1258922932250564636,
                                        'source_nw_y_pixel': -731502914165404465,
                                        'source_pixel_width': -2950877078214999389,
                                        'source_pixel_height': -8894967222379375522,
                                        'rotation': -3503026946775132930,
                                        'virtual_nw_x_pixel': 1662608063,
                                        'virtual_nw_y_pixel': -1121523811,
                                        'virtual_width': 1777074102,
                                        'virtual_height': 1211466172,
                                    },
                            {
                                        'source_monitor': 9740423,
                                        'source_nw_x_pixel': -4444347797958535510,
                                        'source_nw_y_pixel': -5627523440430505961,
                                        'source_pixel_width': -2014982504628734971,
                                        'source_pixel_height': -1279378464379436865,
                                        'rotation': -6624934420367894481,
                                        'virtual_nw_x_pixel': 1138880792,
                                        'virtual_nw_y_pixel': -824145659,
                                        'virtual_width': 578334184,
                                        'virtual_height': -1997473855,
                                    },
                            {
                                        'source_monitor': 2550748,
                                        'source_nw_x_pixel': -5256779980533482361,
                                        'source_nw_y_pixel': -7405674556640152043,
                                        'source_pixel_width': -2072391898720717507,
                                        'source_pixel_height': -7224740693627202015,
                                        'rotation': -923180930950964991,
                                        'virtual_nw_x_pixel': -485173644,
                                        'virtual_nw_y_pixel': 802735362,
                                        'virtual_width': -71108671,
                                        'virtual_height': -734404948,
                                    },
                            {
                                        'source_monitor': 3728682,
                                        'source_nw_x_pixel': -2425495498689488973,
                                        'source_nw_y_pixel': -3271199618001806438,
                                        'source_pixel_width': -5932558052927609663,
                                        'source_pixel_height': -3573063100267752877,
                                        'rotation': -3575052103958583576,
                                        'virtual_nw_x_pixel': 1504089694,
                                        'virtual_nw_y_pixel': 1996336451,
                                        'virtual_width': 1489111685,
                                        'virtual_height': -1693309347,
                                    },
                            {
                                        'source_monitor': 990710,
                                        'source_nw_x_pixel': -118446506208875846,
                                        'source_nw_y_pixel': -7952641403623171524,
                                        'source_pixel_width': -1265852147919137792,
                                        'source_pixel_height': -3403444339324113968,
                                        'rotation': -6849686085329007935,
                                        'virtual_nw_x_pixel': -1317679570,
                                        'virtual_nw_y_pixel': -1733626518,
                                        'virtual_width': -1643863785,
                                        'virtual_height': 953229004,
                                    },
                            {
                                        'source_monitor': 4784823,
                                        'source_nw_x_pixel': -4951640616036841014,
                                        'source_nw_y_pixel': -4600338909053044145,
                                        'source_pixel_width': -3864032139670857339,
                                        'source_pixel_height': -7399594982019046570,
                                        'rotation': -1707523102240529867,
                                        'virtual_nw_x_pixel': 394722862,
                                        'virtual_nw_y_pixel': -451742518,
                                        'virtual_width': 1001670239,
                                        'virtual_height': -772597446,
                                    },
                        ],
                },
                {
                    'description': 'лθǮãμʞųŚ~dҺų˞˛Gøʚżҽ·ĘȌˇŪ+ΠʵɎ\x84Ǹ',
                    'monitors': [
                            {
                                        'identifier': 572865,
                                        'width': -8666161263415542017,
                                        'height': 2459276689074312923,
                                    },
                            {
                                        'identifier': 1974167,
                                        'width': 1711995587161336658,
                                        'height': 8912861043443286634,
                                    },
                            {
                                        'identifier': 5258284,
                                        'width': 4099506611480497479,
                                        'height': 3587844693843701628,
                                    },
                            {
                                        'identifier': 9093758,
                                        'width': -2729250576798847706,
                                        'height': -7277604914403994969,
                                    },
                            {
                                        'identifier': 8056051,
                                        'width': 7613512483979231719,
                                        'height': -7246167498219887830,
                                    },
                            {
                                        'identifier': 2721181,
                                        'width': 555558627804811405,
                                        'height': -6897288790225795076,
                                    },
                            {
                                        'identifier': 2265663,
                                        'width': -5590022038044238204,
                                        'height': -734511147707272234,
                                    },
                            {
                                        'identifier': 2257744,
                                        'width': -1028682304721666026,
                                        'height': 7217999354151914647,
                                    },
                            {
                                        'identifier': 8633694,
                                        'width': 4105748853684986433,
                                        'height': -4163143710354157049,
                                    },
                            {
                                        'identifier': 4550584,
                                        'width': 575290562726064037,
                                        'height': -9210920844179857260,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8350259,
                                        'source_nw_x_pixel': -1807602126645136008,
                                        'source_nw_y_pixel': -4236875712126612266,
                                        'source_pixel_width': -8008704357592584539,
                                        'source_pixel_height': -5686938065718127426,
                                        'rotation': -8568472986952143851,
                                        'virtual_nw_x_pixel': 977974096,
                                        'virtual_nw_y_pixel': 1936713435,
                                        'virtual_width': 391217082,
                                        'virtual_height': -1544974132,
                                    },
                            {
                                        'source_monitor': 7532442,
                                        'source_nw_x_pixel': -4759361800919981572,
                                        'source_nw_y_pixel': -3547271983609133842,
                                        'source_pixel_width': -7158089551912127518,
                                        'source_pixel_height': -1325984986254423316,
                                        'rotation': -1539805299517038288,
                                        'virtual_nw_x_pixel': 649213203,
                                        'virtual_nw_y_pixel': -1484357267,
                                        'virtual_width': -905646312,
                                        'virtual_height': -1171154626,
                                    },
                            {
                                        'source_monitor': 4871153,
                                        'source_nw_x_pixel': -3070324171654171158,
                                        'source_nw_y_pixel': -9188121357536221256,
                                        'source_pixel_width': -3814902885427921036,
                                        'source_pixel_height': -3517749893121490403,
                                        'rotation': -892364500728001384,
                                        'virtual_nw_x_pixel': -1077192761,
                                        'virtual_nw_y_pixel': 1674311620,
                                        'virtual_width': -783825010,
                                        'virtual_height': -1550003555,
                                    },
                            {
                                        'source_monitor': 3737408,
                                        'source_nw_x_pixel': -94297130687887915,
                                        'source_nw_y_pixel': -8635075371140758101,
                                        'source_pixel_width': -3696035332491317991,
                                        'source_pixel_height': -6065149563234037054,
                                        'rotation': -6308292606837646990,
                                        'virtual_nw_x_pixel': 706973589,
                                        'virtual_nw_y_pixel': 954073302,
                                        'virtual_width': -1441158111,
                                        'virtual_height': 442740209,
                                    },
                            {
                                        'source_monitor': 4717181,
                                        'source_nw_x_pixel': -4405104820251480685,
                                        'source_nw_y_pixel': -3672302993523326633,
                                        'source_pixel_width': -560999082351796715,
                                        'source_pixel_height': -8714236622856562868,
                                        'rotation': -3262060361351813818,
                                        'virtual_nw_x_pixel': 512366334,
                                        'virtual_nw_y_pixel': -1541529128,
                                        'virtual_width': 517042941,
                                        'virtual_height': 215086951,
                                    },
                            {
                                        'source_monitor': -487483,
                                        'source_nw_x_pixel': -7899594156587436600,
                                        'source_nw_y_pixel': -5716290037029856611,
                                        'source_pixel_width': -5893562577953026192,
                                        'source_pixel_height': -5305628566223832856,
                                        'rotation': -3349921974123356276,
                                        'virtual_nw_x_pixel': 1514777638,
                                        'virtual_nw_y_pixel': -1453634099,
                                        'virtual_width': 1138616473,
                                        'virtual_height': -726177238,
                                    },
                            {
                                        'source_monitor': -250938,
                                        'source_nw_x_pixel': -6515503565169583408,
                                        'source_nw_y_pixel': -1641298688795562546,
                                        'source_pixel_width': -8795490713566762017,
                                        'source_pixel_height': -3532979816288645170,
                                        'rotation': -1828167141278297698,
                                        'virtual_nw_x_pixel': -960654758,
                                        'virtual_nw_y_pixel': -107375222,
                                        'virtual_width': -1167630522,
                                        'virtual_height': -284603335,
                                    },
                            {
                                        'source_monitor': 5623791,
                                        'source_nw_x_pixel': -4839389961662781217,
                                        'source_nw_y_pixel': -5082978702387776734,
                                        'source_pixel_width': -821351766523910468,
                                        'source_pixel_height': -7938479373318400179,
                                        'rotation': -3170059523237216067,
                                        'virtual_nw_x_pixel': -633524242,
                                        'virtual_nw_y_pixel': 1208847054,
                                        'virtual_width': 1241648954,
                                        'virtual_height': -151589832,
                                    },
                            {
                                        'source_monitor': 7920081,
                                        'source_nw_x_pixel': -778686229404864540,
                                        'source_nw_y_pixel': -5025733214826662513,
                                        'source_pixel_width': -9136180679610667378,
                                        'source_pixel_height': -8502351177823607655,
                                        'rotation': -6475158442565900031,
                                        'virtual_nw_x_pixel': -539846675,
                                        'virtual_nw_y_pixel': -1998191905,
                                        'virtual_width': -357145259,
                                        'virtual_height': -361542760,
                                    },
                            {
                                        'source_monitor': 399499,
                                        'source_nw_x_pixel': -8617461330898742478,
                                        'source_nw_y_pixel': -2193175486710314372,
                                        'source_pixel_width': -257125935250738284,
                                        'source_pixel_height': -4739048362216705861,
                                        'rotation': -4743027123239083528,
                                        'virtual_nw_x_pixel': 601005369,
                                        'virtual_nw_y_pixel': 780141648,
                                        'virtual_width': 796876044,
                                        'virtual_height': 590969036,
                                    },
                        ],
                },
                {
                    'description': 'ђяϬҋх˙ƤǭŻϴѪˀ˟ʫƿ˺ħīǃ\x91{чF˞\x95ԩďÊҒї',
                    'monitors': [
                            {
                                        'identifier': -255014,
                                        'width': -5373520437636091533,
                                        'height': -1568213691011578856,
                                    },
                            {
                                        'identifier': 5715447,
                                        'width': 3330886097512361860,
                                        'height': 7715751195521617754,
                                    },
                            {
                                        'identifier': 3178456,
                                        'width': 3832703515108608625,
                                        'height': -5256702228126955517,
                                    },
                            {
                                        'identifier': 3598293,
                                        'width': 4627730255444171050,
                                        'height': 334383547119581583,
                                    },
                            {
                                        'identifier': 5150611,
                                        'width': -1400385752634181858,
                                        'height': 1814521851768597232,
                                    },
                            {
                                        'identifier': 3807302,
                                        'width': -8407646705534920612,
                                        'height': -5472918393944233979,
                                    },
                            {
                                        'identifier': 9738573,
                                        'width': 8924015047365812895,
                                        'height': -72602769765199565,
                                    },
                            {
                                        'identifier': 5147639,
                                        'width': 2681794851520280012,
                                        'height': 715608979186873536,
                                    },
                            {
                                        'identifier': 9177928,
                                        'width': -4455017335830510532,
                                        'height': 6880391849655995501,
                                    },
                            {
                                        'identifier': 8093729,
                                        'width': -7894616881314984674,
                                        'height': -9069802090188693290,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4705232,
                                        'source_nw_x_pixel': -8703121156812990413,
                                        'source_nw_y_pixel': -3178793726313767083,
                                        'source_pixel_width': -4122093976422922877,
                                        'source_pixel_height': -7461465998437058175,
                                        'rotation': -7590826759849586141,
                                        'virtual_nw_x_pixel': -134991841,
                                        'virtual_nw_y_pixel': -375994326,
                                        'virtual_width': -295179991,
                                        'virtual_height': 746622981,
                                    },
                            {
                                        'source_monitor': 3503179,
                                        'source_nw_x_pixel': -3318837910808993032,
                                        'source_nw_y_pixel': -2819444054737168367,
                                        'source_pixel_width': -4564450169907618934,
                                        'source_pixel_height': -7602427527071560443,
                                        'rotation': -5452077010670916686,
                                        'virtual_nw_x_pixel': 620711827,
                                        'virtual_nw_y_pixel': -602622822,
                                        'virtual_width': 204560064,
                                        'virtual_height': 170576680,
                                    },
                            {
                                        'source_monitor': 2830498,
                                        'source_nw_x_pixel': -7994420188458947891,
                                        'source_nw_y_pixel': -7764112082576688530,
                                        'source_pixel_width': -7318911901872431271,
                                        'source_pixel_height': -2311404775210905724,
                                        'rotation': -5906066795001803241,
                                        'virtual_nw_x_pixel': 836812592,
                                        'virtual_nw_y_pixel': -74874189,
                                        'virtual_width': 901339270,
                                        'virtual_height': -1177759746,
                                    },
                            {
                                        'source_monitor': 5281630,
                                        'source_nw_x_pixel': -1628423054942828644,
                                        'source_nw_y_pixel': -5457381264404015366,
                                        'source_pixel_width': -8550497025666319607,
                                        'source_pixel_height': -1604266044689600625,
                                        'rotation': -157757356974748294,
                                        'virtual_nw_x_pixel': 1324888937,
                                        'virtual_nw_y_pixel': 1957578288,
                                        'virtual_width': 172679343,
                                        'virtual_height': 1973317122,
                                    },
                            {
                                        'source_monitor': 855869,
                                        'source_nw_x_pixel': -5719322846719715611,
                                        'source_nw_y_pixel': -2693148819094546137,
                                        'source_pixel_width': -4086678477426938208,
                                        'source_pixel_height': -4771784936519739433,
                                        'rotation': -256461215702144474,
                                        'virtual_nw_x_pixel': 1561464699,
                                        'virtual_nw_y_pixel': -1971837734,
                                        'virtual_width': -379606964,
                                        'virtual_height': 632135052,
                                    },
                            {
                                        'source_monitor': 6351866,
                                        'source_nw_x_pixel': -1497545034009771066,
                                        'source_nw_y_pixel': -5753046778871618796,
                                        'source_pixel_width': -8352847367628388305,
                                        'source_pixel_height': -8082605518198900696,
                                        'rotation': -7498258901477351521,
                                        'virtual_nw_x_pixel': 377191889,
                                        'virtual_nw_y_pixel': 1446807954,
                                        'virtual_width': -617479347,
                                        'virtual_height': -441441405,
                                    },
                            {
                                        'source_monitor': 1586806,
                                        'source_nw_x_pixel': -697941814735926426,
                                        'source_nw_y_pixel': -5826045657107099309,
                                        'source_pixel_width': -7824911263471825752,
                                        'source_pixel_height': -5675964449117668183,
                                        'rotation': -7713417406910248030,
                                        'virtual_nw_x_pixel': 57770074,
                                        'virtual_nw_y_pixel': 1151407311,
                                        'virtual_width': 1186657261,
                                        'virtual_height': 752581172,
                                    },
                            {
                                        'source_monitor': 8971988,
                                        'source_nw_x_pixel': -6731766672992247914,
                                        'source_nw_y_pixel': -4541193508761952671,
                                        'source_pixel_width': -4436131423563852557,
                                        'source_pixel_height': -5441050738485866342,
                                        'rotation': -1334021929813440371,
                                        'virtual_nw_x_pixel': 43150881,
                                        'virtual_nw_y_pixel': 1589348946,
                                        'virtual_width': -40665181,
                                        'virtual_height': 1342247192,
                                    },
                            {
                                        'source_monitor': -667408,
                                        'source_nw_x_pixel': -580963235732510720,
                                        'source_nw_y_pixel': -5774035832712867387,
                                        'source_pixel_width': -2885895782346576430,
                                        'source_pixel_height': -4106009443510470351,
                                        'rotation': -3446186287989727746,
                                        'virtual_nw_x_pixel': 456334434,
                                        'virtual_nw_y_pixel': -1394806876,
                                        'virtual_width': -1338456336,
                                        'virtual_height': -230305610,
                                    },
                            {
                                        'source_monitor': -452155,
                                        'source_nw_x_pixel': -7127098256221957372,
                                        'source_nw_y_pixel': -9041086359240335091,
                                        'source_pixel_width': -547098768353112153,
                                        'source_pixel_height': -657968407443430671,
                                        'rotation': -5559464195562801758,
                                        'virtual_nw_x_pixel': 1446409651,
                                        'virtual_nw_y_pixel': -141467890,
                                        'virtual_width': 1006522035,
                                        'virtual_height': -127458041,
                                    },
                        ],
                },
                {
                    'description': 'ȩêԆЯıӵ\x8fҒ°ҍҍŲǑȽϡ^JԍԥςΟHƎǦˮĿЦ¾ǂˣ',
                    'monitors': [
                            {
                                        'identifier': 3992165,
                                        'width': -8807878843613236641,
                                        'height': -1971521278805752895,
                                    },
                            {
                                        'identifier': 8422422,
                                        'width': 3904596443269395650,
                                        'height': -3720992989506177796,
                                    },
                            {
                                        'identifier': 4186943,
                                        'width': 6925319161281675904,
                                        'height': -1599925992162715948,
                                    },
                            {
                                        'identifier': 59969,
                                        'width': -7029340397150147952,
                                        'height': 3505004857124040850,
                                    },
                            {
                                        'identifier': 2505120,
                                        'width': -1386174124009900626,
                                        'height': 2437496760145906008,
                                    },
                            {
                                        'identifier': -558469,
                                        'width': 3237711717950064140,
                                        'height': -4814387651610923627,
                                    },
                            {
                                        'identifier': 88482,
                                        'width': -2839102172848078331,
                                        'height': 105951506639630743,
                                    },
                            {
                                        'identifier': 7413937,
                                        'width': -6727592204717720306,
                                        'height': -7890121625940865472,
                                    },
                            {
                                        'identifier': 3416605,
                                        'width': 2849176817985602807,
                                        'height': 8774754343904048956,
                                    },
                            {
                                        'identifier': 8292441,
                                        'width': 4535981707313821951,
                                        'height': 6549832238154814279,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3127118,
                                        'source_nw_x_pixel': -8328362613176335798,
                                        'source_nw_y_pixel': -5120116258021638827,
                                        'source_pixel_width': -2099824770368054319,
                                        'source_pixel_height': -5095101799374568228,
                                        'rotation': -8046281035532540123,
                                        'virtual_nw_x_pixel': -231905411,
                                        'virtual_nw_y_pixel': -604560684,
                                        'virtual_width': 1152476608,
                                        'virtual_height': 101225030,
                                    },
                            {
                                        'source_monitor': 9832016,
                                        'source_nw_x_pixel': -4015669577638208265,
                                        'source_nw_y_pixel': -8021807864730042713,
                                        'source_pixel_width': -3247298910285664568,
                                        'source_pixel_height': -4883320314027335088,
                                        'rotation': -5388180079695512323,
                                        'virtual_nw_x_pixel': 69032200,
                                        'virtual_nw_y_pixel': 113246788,
                                        'virtual_width': -833486719,
                                        'virtual_height': -1516387071,
                                    },
                            {
                                        'source_monitor': 4191913,
                                        'source_nw_x_pixel': -7424528903263152143,
                                        'source_nw_y_pixel': -7631002517450881932,
                                        'source_pixel_width': -8131514495712832793,
                                        'source_pixel_height': -9199349839652627288,
                                        'rotation': -4246704147985081710,
                                        'virtual_nw_x_pixel': 1746982750,
                                        'virtual_nw_y_pixel': 316155626,
                                        'virtual_width': -1642922734,
                                        'virtual_height': -1061197462,
                                    },
                            {
                                        'source_monitor': 4366207,
                                        'source_nw_x_pixel': -5456027458714067165,
                                        'source_nw_y_pixel': -4826436055645527278,
                                        'source_pixel_width': -2122998404197288759,
                                        'source_pixel_height': -5672191582745494419,
                                        'rotation': -3912449190208084172,
                                        'virtual_nw_x_pixel': 541899206,
                                        'virtual_nw_y_pixel': -948977668,
                                        'virtual_width': 1435919976,
                                        'virtual_height': -1211378448,
                                    },
                            {
                                        'source_monitor': 9754437,
                                        'source_nw_x_pixel': -2993901963999543779,
                                        'source_nw_y_pixel': -3158254435226965088,
                                        'source_pixel_width': -3127780530996007253,
                                        'source_pixel_height': -8722457107919122280,
                                        'rotation': -7464699832317491220,
                                        'virtual_nw_x_pixel': -1945539698,
                                        'virtual_nw_y_pixel': -403733308,
                                        'virtual_width': 814386289,
                                        'virtual_height': -1792245430,
                                    },
                            {
                                        'source_monitor': 3452772,
                                        'source_nw_x_pixel': -8336306020696045072,
                                        'source_nw_y_pixel': -8969597081512626138,
                                        'source_pixel_width': -6705051607638986116,
                                        'source_pixel_height': -9213598476464732302,
                                        'rotation': -322967193520394543,
                                        'virtual_nw_x_pixel': -1379844097,
                                        'virtual_nw_y_pixel': -1553018607,
                                        'virtual_width': 351420873,
                                        'virtual_height': 1142297060,
                                    },
                            {
                                        'source_monitor': 5198192,
                                        'source_nw_x_pixel': -6615349315985341601,
                                        'source_nw_y_pixel': -6622293877562371607,
                                        'source_pixel_width': -1985140258893533468,
                                        'source_pixel_height': -7466773524867698230,
                                        'rotation': -7312892176528574244,
                                        'virtual_nw_x_pixel': -645114189,
                                        'virtual_nw_y_pixel': 909631922,
                                        'virtual_width': 90533895,
                                        'virtual_height': -843841789,
                                    },
                            {
                                        'source_monitor': 1357572,
                                        'source_nw_x_pixel': -298262647172040178,
                                        'source_nw_y_pixel': -1601271747204283366,
                                        'source_pixel_width': -2798586673605216368,
                                        'source_pixel_height': -4866102117352865668,
                                        'rotation': -227670638367364646,
                                        'virtual_nw_x_pixel': 1795753477,
                                        'virtual_nw_y_pixel': 864350016,
                                        'virtual_width': -271719537,
                                        'virtual_height': -1471375435,
                                    },
                            {
                                        'source_monitor': 4673566,
                                        'source_nw_x_pixel': -4544381824004531305,
                                        'source_nw_y_pixel': -5394071637793166370,
                                        'source_pixel_width': -2916126066476446815,
                                        'source_pixel_height': -1600597688644070180,
                                        'rotation': -8746386351078421377,
                                        'virtual_nw_x_pixel': 221278805,
                                        'virtual_nw_y_pixel': -1392049401,
                                        'virtual_width': -1658512018,
                                        'virtual_height': -834351890,
                                    },
                            {
                                        'source_monitor': 8484850,
                                        'source_nw_x_pixel': -9216950598125864078,
                                        'source_nw_y_pixel': -6503666030780346055,
                                        'source_pixel_width': -5560581498441511898,
                                        'source_pixel_height': -7374129806105341379,
                                        'rotation': -5941361299551987128,
                                        'virtual_nw_x_pixel': -1674698435,
                                        'virtual_nw_y_pixel': 1604943315,
                                        'virtual_width': 19128912,
                                        'virtual_height': -1689657831,
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
                                        'identifier': 261142,
                                        'width': -8045922606240884346,
                                        'height': 2787532909715377928,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -363177118400970304,
                                        'source_nw_y_pixel': -8077930254636397015,
                                        'source_pixel_width': -8507633536024372679,
                                        'source_pixel_height': -8350081796441539190,
                                        'rotation': -8600404230862127386,
                                        'virtual_nw_x_pixel': 367048398,
                                        'virtual_nw_y_pixel': -570806830,
                                        'virtual_width': -1348308190,
                                        'virtual_height': -1429400545,
                                    },
                        ],
                },
            ],

        },
    ),
]
