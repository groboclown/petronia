# GENERATED CODE - DO NOT MODIFY

"""
Tests for the screen module.
Extension petronia.core.api.native.screen, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
            'identifier': 6114583,
            'width': 3710861057177865069,
            'height': 8370081409216097385,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 6952607,

            'width': 147163987990095041,

            'height': -475833933400631966,

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
            'source_monitor': 2382989,
            'source_nw_x_pixel': -1353571020316399224,
            'source_nw_y_pixel': -4156905715169561740,
            'source_pixel_width': -6691804968610181902,
            'source_pixel_height': -1547177138417248192,
            'rotation': -7819839079133085381,
            'virtual_nw_x_pixel': 1039869528,
            'virtual_nw_y_pixel': -22277173,
            'virtual_width': -955253260,
            'virtual_height': -772209631,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -1400656968826873733,

            'source_nw_y_pixel': -2739018899583333967,

            'source_pixel_width': -1745773141876827476,

            'source_pixel_height': -5827328079121658882,

            'rotation': -6922548073564683042,

            'virtual_nw_x_pixel': 371319059,

            'virtual_nw_y_pixel': -75892847,

            'virtual_width': 1745717017,

            'virtual_height': 1348428813,

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
            'description': 'ɍөӅª\u038dгȜϦĥҸÖȑưӈшÏɞϏӣşȓѣԎЅŁϺjɜƸȶ',
            'monitors': [
                {
                    'identifier': 3815314,
                    'width': -8512669314335768653,
                    'height': 549761676848654934,
                },
                {
                    'identifier': 6501276,
                    'width': 482426688338755102,
                    'height': -4735901648097971708,
                },
                {
                    'identifier': 1838798,
                    'width': 2503535646437426129,
                    'height': 1402818073465947357,
                },
                {
                    'identifier': 9978813,
                    'width': -7812806289579127009,
                    'height': -7297639635553725960,
                },
                {
                    'identifier': 84728,
                    'width': -2226885016254828551,
                    'height': 3483736374498026042,
                },
                {
                    'identifier': 3747391,
                    'width': 285602852449447172,
                    'height': -4575720787366847928,
                },
                {
                    'identifier': 3291400,
                    'width': 3244080239310984179,
                    'height': -7450433531270198209,
                },
                {
                    'identifier': 5726133,
                    'width': 6651176124141778327,
                    'height': 4786087667902817208,
                },
                {
                    'identifier': 9476003,
                    'width': 7320964541419920129,
                    'height': -3727574551526318506,
                },
                {
                    'identifier': -578804,
                    'width': 7303592467376570160,
                    'height': 8219264405614145710,
                },
            ],
            'screen': [
                {
                    'source_monitor': 9794838,
                    'source_nw_x_pixel': -6688422539076987081,
                    'source_nw_y_pixel': -6109272043036608835,
                    'source_pixel_width': -8459285475190900639,
                    'source_pixel_height': -7668760274095769916,
                    'rotation': -437705973405680855,
                    'virtual_nw_x_pixel': 66827141,
                    'virtual_nw_y_pixel': -832344184,
                    'virtual_width': -402926704,
                    'virtual_height': -347133886,
                },
                {
                    'source_monitor': -581044,
                    'source_nw_x_pixel': -5738697564762797909,
                    'source_nw_y_pixel': -4570145181761889003,
                    'source_pixel_width': -4520613662486826564,
                    'source_pixel_height': -3859627419583472940,
                    'rotation': -6498890418761092358,
                    'virtual_nw_x_pixel': -1728503726,
                    'virtual_nw_y_pixel': -1614050000,
                    'virtual_width': 1565255926,
                    'virtual_height': 473460535,
                },
                {
                    'source_monitor': 535850,
                    'source_nw_x_pixel': -244870321849674889,
                    'source_nw_y_pixel': -4927365055422872856,
                    'source_pixel_width': -3939240099015261037,
                    'source_pixel_height': -4263171634182771807,
                    'rotation': -8647108786545353834,
                    'virtual_nw_x_pixel': -1935641922,
                    'virtual_nw_y_pixel': -1207797363,
                    'virtual_width': 840783015,
                    'virtual_height': 1910685804,
                },
                {
                    'source_monitor': 7700596,
                    'source_nw_x_pixel': -1125546378654937193,
                    'source_nw_y_pixel': -2498900426024957799,
                    'source_pixel_width': -5409963296272190092,
                    'source_pixel_height': -811166654339885732,
                    'rotation': -3274381001776148656,
                    'virtual_nw_x_pixel': 1093638323,
                    'virtual_nw_y_pixel': -1211091932,
                    'virtual_width': 509270136,
                    'virtual_height': 237756162,
                },
                {
                    'source_monitor': 1154353,
                    'source_nw_x_pixel': -1418405711618086654,
                    'source_nw_y_pixel': -5866025236905787793,
                    'source_pixel_width': -6230473406798360295,
                    'source_pixel_height': -3291662121226138418,
                    'rotation': -5047659288903447955,
                    'virtual_nw_x_pixel': -70805882,
                    'virtual_nw_y_pixel': -992146305,
                    'virtual_width': -605156167,
                    'virtual_height': -438415385,
                },
                {
                    'source_monitor': 662524,
                    'source_nw_x_pixel': -3068482537404114421,
                    'source_nw_y_pixel': -597939472462963064,
                    'source_pixel_width': -7305556748826167699,
                    'source_pixel_height': -8568055153202720575,
                    'rotation': -7622230512606660199,
                    'virtual_nw_x_pixel': -1691113580,
                    'virtual_nw_y_pixel': -1544737352,
                    'virtual_width': 1108175476,
                    'virtual_height': -2833288,
                },
                {
                    'source_monitor': 9355272,
                    'source_nw_x_pixel': -6737691429170463544,
                    'source_nw_y_pixel': -8661114950014736453,
                    'source_pixel_width': -355683975962750948,
                    'source_pixel_height': -4446493999931100098,
                    'rotation': -1286786552693274015,
                    'virtual_nw_x_pixel': -390593206,
                    'virtual_nw_y_pixel': 349012101,
                    'virtual_width': 1297864252,
                    'virtual_height': -603110196,
                },
                {
                    'source_monitor': 9894826,
                    'source_nw_x_pixel': -3262317485877427247,
                    'source_nw_y_pixel': -106079372049789409,
                    'source_pixel_width': -6275722060750027580,
                    'source_pixel_height': -2612707988822222968,
                    'rotation': -2627856034308177281,
                    'virtual_nw_x_pixel': -991733597,
                    'virtual_nw_y_pixel': -1305413292,
                    'virtual_width': -929271550,
                    'virtual_height': 1318229716,
                },
                {
                    'source_monitor': 7612430,
                    'source_nw_x_pixel': -4531366426375027824,
                    'source_nw_y_pixel': -4026583001587365584,
                    'source_pixel_width': -4754597540246336030,
                    'source_pixel_height': -4942699750592788442,
                    'rotation': -9010561877859670720,
                    'virtual_nw_x_pixel': -1149975409,
                    'virtual_nw_y_pixel': 1743413298,
                    'virtual_width': -1650763141,
                    'virtual_height': -198791582,
                },
                {
                    'source_monitor': 8765676,
                    'source_nw_x_pixel': -4889519437612028941,
                    'source_nw_y_pixel': -4103975093207566470,
                    'source_pixel_width': -465852913348406800,
                    'source_pixel_height': -6186563033440371467,
                    'rotation': -2314649057085769440,
                    'virtual_nw_x_pixel': 1721932254,
                    'virtual_nw_y_pixel': 15755041,
                    'virtual_width': -1998692790,
                    'virtual_height': 1193886890,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 8444338,
                    'width': -1027108343211094317,
                    'height': 2699252073486601985,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -5534191170690185056,
                    'source_nw_y_pixel': -4463422388686420042,
                    'source_pixel_width': -1679654892008299804,
                    'source_pixel_height': -4313980299259915221,
                    'rotation': -2922658818501028989,
                    'virtual_nw_x_pixel': 769499594,
                    'virtual_nw_y_pixel': -1709616145,
                    'virtual_width': -606654773,
                    'virtual_height': -1184030022,
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
            'request_id': 9835739,
            'mapped_screens_by_monitors': [
                {
                    'description': '˪ȟȣǈÕȇЙʹКӿӘÛȟÍɞÌ\x92ʳЂϺόςҤШѕƘƉӄВλ',
                    'monitors': [
                            {
                                        'identifier': 1414552,
                                        'width': -4543503501897149426,
                                        'height': 4010160084704438042,
                                    },
                            {
                                        'identifier': 6727864,
                                        'width': -1225329242030343134,
                                        'height': 5922611036605863181,
                                    },
                            {
                                        'identifier': 425715,
                                        'width': -2177529423720587077,
                                        'height': -6819176108325396738,
                                    },
                            {
                                        'identifier': 5625228,
                                        'width': 7847509724903383868,
                                        'height': -1778001563403439241,
                                    },
                            {
                                        'identifier': 9491035,
                                        'width': 8442367221748140634,
                                        'height': -9044292343047097836,
                                    },
                            {
                                        'identifier': 2359029,
                                        'width': -1168768198746903349,
                                        'height': 7019029930884251045,
                                    },
                            {
                                        'identifier': 1175730,
                                        'width': -8730975915759861381,
                                        'height': 1384608384717691850,
                                    },
                            {
                                        'identifier': 7083701,
                                        'width': 4351608405207145914,
                                        'height': -3056496402554443933,
                                    },
                            {
                                        'identifier': -582914,
                                        'width': 2734618848080293548,
                                        'height': 8266927971627200844,
                                    },
                            {
                                        'identifier': 7023816,
                                        'width': 7685578163757880904,
                                        'height': -5941265889540831293,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1716158,
                                        'source_nw_x_pixel': -1323510469030007096,
                                        'source_nw_y_pixel': -6408533627604242930,
                                        'source_pixel_width': -5688845381521886867,
                                        'source_pixel_height': -6935027836674197906,
                                        'rotation': -462943229420856000,
                                        'virtual_nw_x_pixel': -71879836,
                                        'virtual_nw_y_pixel': 447536213,
                                        'virtual_width': -537410448,
                                        'virtual_height': -1779176778,
                                    },
                            {
                                        'source_monitor': 6044169,
                                        'source_nw_x_pixel': -5999122671940274425,
                                        'source_nw_y_pixel': -6212158883186041145,
                                        'source_pixel_width': -5495472173447930269,
                                        'source_pixel_height': -7266122807783185307,
                                        'rotation': -6985380269816211390,
                                        'virtual_nw_x_pixel': 1724184992,
                                        'virtual_nw_y_pixel': -83580069,
                                        'virtual_width': -567002372,
                                        'virtual_height': -1076231217,
                                    },
                            {
                                        'source_monitor': 2143794,
                                        'source_nw_x_pixel': -3728640812040739236,
                                        'source_nw_y_pixel': -1241350006149278942,
                                        'source_pixel_width': -98058425302509493,
                                        'source_pixel_height': -7762460260770394528,
                                        'rotation': -5046604186602889580,
                                        'virtual_nw_x_pixel': 578166654,
                                        'virtual_nw_y_pixel': 1004086573,
                                        'virtual_width': 1091437192,
                                        'virtual_height': 1184222854,
                                    },
                            {
                                        'source_monitor': 1654630,
                                        'source_nw_x_pixel': -9192669934706970097,
                                        'source_nw_y_pixel': -5285871852582156489,
                                        'source_pixel_width': -9114007856497973585,
                                        'source_pixel_height': -8770205647505913829,
                                        'rotation': -2364350637509862853,
                                        'virtual_nw_x_pixel': -1715969,
                                        'virtual_nw_y_pixel': 47644389,
                                        'virtual_width': 90421047,
                                        'virtual_height': -1208212617,
                                    },
                            {
                                        'source_monitor': 3537598,
                                        'source_nw_x_pixel': -2694177871089333454,
                                        'source_nw_y_pixel': -1075239276344565217,
                                        'source_pixel_width': -291182690441792672,
                                        'source_pixel_height': -6412020540853376793,
                                        'rotation': -3116381428254045496,
                                        'virtual_nw_x_pixel': -342999356,
                                        'virtual_nw_y_pixel': 797497476,
                                        'virtual_width': 26339223,
                                        'virtual_height': -792116555,
                                    },
                            {
                                        'source_monitor': 8120111,
                                        'source_nw_x_pixel': -9151797121793659574,
                                        'source_nw_y_pixel': -8142682923854845860,
                                        'source_pixel_width': -1592230446240010314,
                                        'source_pixel_height': -1969344598201445393,
                                        'rotation': -3518742184589570613,
                                        'virtual_nw_x_pixel': -528092230,
                                        'virtual_nw_y_pixel': 1619730050,
                                        'virtual_width': 1097563392,
                                        'virtual_height': 1335078038,
                                    },
                            {
                                        'source_monitor': 7050264,
                                        'source_nw_x_pixel': -4056592316370514759,
                                        'source_nw_y_pixel': -825087191717802283,
                                        'source_pixel_width': -296045572524985678,
                                        'source_pixel_height': -1670569589472538817,
                                        'rotation': -878490879276789562,
                                        'virtual_nw_x_pixel': 1508122000,
                                        'virtual_nw_y_pixel': -1104277269,
                                        'virtual_width': -309913600,
                                        'virtual_height': -650056115,
                                    },
                            {
                                        'source_monitor': 21225,
                                        'source_nw_x_pixel': -4247990501057357347,
                                        'source_nw_y_pixel': -455944705065304017,
                                        'source_pixel_width': -5344458862669497244,
                                        'source_pixel_height': -2188739572114131093,
                                        'rotation': -885361280710151429,
                                        'virtual_nw_x_pixel': 1500476549,
                                        'virtual_nw_y_pixel': 948921866,
                                        'virtual_width': -1786215653,
                                        'virtual_height': -1373697868,
                                    },
                            {
                                        'source_monitor': 6010555,
                                        'source_nw_x_pixel': -2320297582693405052,
                                        'source_nw_y_pixel': -8281977764614889061,
                                        'source_pixel_width': -8783741076344920954,
                                        'source_pixel_height': -3625390070076958764,
                                        'rotation': -850695781785992853,
                                        'virtual_nw_x_pixel': 169408264,
                                        'virtual_nw_y_pixel': 579575658,
                                        'virtual_width': -1781345118,
                                        'virtual_height': 1681839495,
                                    },
                            {
                                        'source_monitor': -168930,
                                        'source_nw_x_pixel': -8391436378605834349,
                                        'source_nw_y_pixel': -3289005763369926817,
                                        'source_pixel_width': -1184093423714002142,
                                        'source_pixel_height': -6449753072528077306,
                                        'rotation': -8153695748532368953,
                                        'virtual_nw_x_pixel': -548120870,
                                        'virtual_nw_y_pixel': -1051217586,
                                        'virtual_width': -1323367603,
                                        'virtual_height': 167761063,
                                    },
                        ],
                },
                {
                    'description': 'ЎѣˁԠæԫđʰϾ&ԍФŔɷͰΣӻIȉ\x9eѵʨψƥΥϸЩǹȃ7',
                    'monitors': [
                            {
                                        'identifier': 1739164,
                                        'width': 5361980254779360556,
                                        'height': 7533604014629476316,
                                    },
                            {
                                        'identifier': 3578035,
                                        'width': 5295138298996745602,
                                        'height': -3682777758040960145,
                                    },
                            {
                                        'identifier': 8464181,
                                        'width': 861206064343907765,
                                        'height': 6995023459847055183,
                                    },
                            {
                                        'identifier': 893044,
                                        'width': 4424898009811172676,
                                        'height': -8643081483813571827,
                                    },
                            {
                                        'identifier': 9172471,
                                        'width': -631779194682329188,
                                        'height': 7595220864856273211,
                                    },
                            {
                                        'identifier': 2454459,
                                        'width': -7952135573966275485,
                                        'height': 1090568757078739319,
                                    },
                            {
                                        'identifier': 2080575,
                                        'width': -7637526509081587031,
                                        'height': 783412843343473340,
                                    },
                            {
                                        'identifier': 7265759,
                                        'width': -234692771199623651,
                                        'height': 3944450030750401302,
                                    },
                            {
                                        'identifier': 1579722,
                                        'width': 2202429463541333079,
                                        'height': 1927369370713053760,
                                    },
                            {
                                        'identifier': 4594272,
                                        'width': 6496041490166107419,
                                        'height': 6442624846402290995,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8037376,
                                        'source_nw_x_pixel': -8104250496050970231,
                                        'source_nw_y_pixel': -4911418681658969678,
                                        'source_pixel_width': -2146519424805258033,
                                        'source_pixel_height': -9163763571175420673,
                                        'rotation': -3646225272807808511,
                                        'virtual_nw_x_pixel': 765394067,
                                        'virtual_nw_y_pixel': -79779995,
                                        'virtual_width': 338362703,
                                        'virtual_height': -76427565,
                                    },
                            {
                                        'source_monitor': 5120450,
                                        'source_nw_x_pixel': -5643754423584984220,
                                        'source_nw_y_pixel': -3437892677597249674,
                                        'source_pixel_width': -6184285991341545628,
                                        'source_pixel_height': -2347286233017449604,
                                        'rotation': -1661912057547007010,
                                        'virtual_nw_x_pixel': 970309221,
                                        'virtual_nw_y_pixel': 1122357841,
                                        'virtual_width': 1516878289,
                                        'virtual_height': -1756169501,
                                    },
                            {
                                        'source_monitor': 7096550,
                                        'source_nw_x_pixel': -6927219382342680950,
                                        'source_nw_y_pixel': -6783452480029490279,
                                        'source_pixel_width': -1604696370160678982,
                                        'source_pixel_height': -2710808103920914288,
                                        'rotation': -4746651713229360414,
                                        'virtual_nw_x_pixel': -1336856045,
                                        'virtual_nw_y_pixel': 1778667165,
                                        'virtual_width': 1268534899,
                                        'virtual_height': -1203867723,
                                    },
                            {
                                        'source_monitor': -663744,
                                        'source_nw_x_pixel': -7011089315496455167,
                                        'source_nw_y_pixel': -4731404293384585087,
                                        'source_pixel_width': -7876215364299812959,
                                        'source_pixel_height': -5368231204744407233,
                                        'rotation': -3646262472442538952,
                                        'virtual_nw_x_pixel': -1285446815,
                                        'virtual_nw_y_pixel': 1322350754,
                                        'virtual_width': 545191833,
                                        'virtual_height': -1287163656,
                                    },
                            {
                                        'source_monitor': 8805008,
                                        'source_nw_x_pixel': -7745925982513077348,
                                        'source_nw_y_pixel': -3359323535708160657,
                                        'source_pixel_width': -1193965766827288042,
                                        'source_pixel_height': -7490195232380753635,
                                        'rotation': -1877151989150158628,
                                        'virtual_nw_x_pixel': -1209270416,
                                        'virtual_nw_y_pixel': 1637723592,
                                        'virtual_width': 447918399,
                                        'virtual_height': -73648813,
                                    },
                            {
                                        'source_monitor': 2870348,
                                        'source_nw_x_pixel': -2184201794017196056,
                                        'source_nw_y_pixel': -2246635364166568209,
                                        'source_pixel_width': -3452936459495690342,
                                        'source_pixel_height': -1068554698591363842,
                                        'rotation': -1549025946028985744,
                                        'virtual_nw_x_pixel': -1908639237,
                                        'virtual_nw_y_pixel': -1146389274,
                                        'virtual_width': 1196807985,
                                        'virtual_height': 1093752732,
                                    },
                            {
                                        'source_monitor': -515180,
                                        'source_nw_x_pixel': -2124914607975620423,
                                        'source_nw_y_pixel': -8474917054987935609,
                                        'source_pixel_width': -5317067654356848585,
                                        'source_pixel_height': -6751231799554364570,
                                        'rotation': -8819029039693310748,
                                        'virtual_nw_x_pixel': 156461436,
                                        'virtual_nw_y_pixel': -361912411,
                                        'virtual_width': 1582634583,
                                        'virtual_height': 1140626359,
                                    },
                            {
                                        'source_monitor': 9918280,
                                        'source_nw_x_pixel': -5204648908880147752,
                                        'source_nw_y_pixel': -2878652284036805138,
                                        'source_pixel_width': -1896480178754547350,
                                        'source_pixel_height': -7598290855130464846,
                                        'rotation': -2278557376313137181,
                                        'virtual_nw_x_pixel': -706963841,
                                        'virtual_nw_y_pixel': -474792741,
                                        'virtual_width': 161725167,
                                        'virtual_height': -1864283892,
                                    },
                            {
                                        'source_monitor': 560778,
                                        'source_nw_x_pixel': -3009349373125932264,
                                        'source_nw_y_pixel': -3096462998289294805,
                                        'source_pixel_width': -9061815707804381147,
                                        'source_pixel_height': -5043042243652459095,
                                        'rotation': -2505752024931451922,
                                        'virtual_nw_x_pixel': 852012085,
                                        'virtual_nw_y_pixel': 1881702584,
                                        'virtual_width': 558961924,
                                        'virtual_height': -524191405,
                                    },
                            {
                                        'source_monitor': 2814037,
                                        'source_nw_x_pixel': -4283034850787311749,
                                        'source_nw_y_pixel': -7204356899892782277,
                                        'source_pixel_width': -6338885290958804153,
                                        'source_pixel_height': -7291816894978716514,
                                        'rotation': -2222463983785105414,
                                        'virtual_nw_x_pixel': 1088294689,
                                        'virtual_nw_y_pixel': -1994128985,
                                        'virtual_width': 1838457774,
                                        'virtual_height': 566084311,
                                    },
                        ],
                },
                {
                    'description': 'ÕÆǗУʹøĘѫϡȸӭӎǺɁǶϢγλȤǌҕ\x7fɀǆВŵϋщē÷',
                    'monitors': [
                            {
                                        'identifier': 3948600,
                                        'width': -4292075103491686316,
                                        'height': 4867377922451517202,
                                    },
                            {
                                        'identifier': 9123595,
                                        'width': 3768593743959675895,
                                        'height': -3075399725483506377,
                                    },
                            {
                                        'identifier': 1490017,
                                        'width': 5100622548552751241,
                                        'height': -2379265767502922410,
                                    },
                            {
                                        'identifier': 2489918,
                                        'width': 235601929766540612,
                                        'height': -933504208748102703,
                                    },
                            {
                                        'identifier': 7647674,
                                        'width': 5154238305052183283,
                                        'height': 1107920076659042755,
                                    },
                            {
                                        'identifier': 3797741,
                                        'width': 4239751234495318974,
                                        'height': 8708683934251321066,
                                    },
                            {
                                        'identifier': 6304003,
                                        'width': 198619117390794128,
                                        'height': -6272763888319812690,
                                    },
                            {
                                        'identifier': 1184613,
                                        'width': 8978292855033448968,
                                        'height': 3677385601973267353,
                                    },
                            {
                                        'identifier': 8334776,
                                        'width': -6430603241709312448,
                                        'height': 7767614101273662170,
                                    },
                            {
                                        'identifier': 3736388,
                                        'width': 7423791361962325287,
                                        'height': -6276117210407768808,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9387143,
                                        'source_nw_x_pixel': -8535418674163564564,
                                        'source_nw_y_pixel': -682369090405422234,
                                        'source_pixel_width': -2061148892266094723,
                                        'source_pixel_height': -9099390712422142938,
                                        'rotation': -5870422376463142785,
                                        'virtual_nw_x_pixel': -1233761484,
                                        'virtual_nw_y_pixel': 1246024641,
                                        'virtual_width': 1664090843,
                                        'virtual_height': 1919845537,
                                    },
                            {
                                        'source_monitor': 9722091,
                                        'source_nw_x_pixel': -8228422371761370673,
                                        'source_nw_y_pixel': -7820277899511349096,
                                        'source_pixel_width': -1213123350820576583,
                                        'source_pixel_height': -2417692287502038665,
                                        'rotation': -4935203003931311842,
                                        'virtual_nw_x_pixel': -1528818287,
                                        'virtual_nw_y_pixel': -1430166562,
                                        'virtual_width': -699577992,
                                        'virtual_height': -1722630325,
                                    },
                            {
                                        'source_monitor': 9507702,
                                        'source_nw_x_pixel': -5398612865367139435,
                                        'source_nw_y_pixel': -5270712779008093858,
                                        'source_pixel_width': -8679423160931400464,
                                        'source_pixel_height': -4505979338810921026,
                                        'rotation': -457138468005945763,
                                        'virtual_nw_x_pixel': 114042126,
                                        'virtual_nw_y_pixel': 945185047,
                                        'virtual_width': 1840673304,
                                        'virtual_height': -259445920,
                                    },
                            {
                                        'source_monitor': 7618248,
                                        'source_nw_x_pixel': -729255921385742078,
                                        'source_nw_y_pixel': -6608165778601412645,
                                        'source_pixel_width': -721297851247727768,
                                        'source_pixel_height': -3581389835814480489,
                                        'rotation': -807662959609957296,
                                        'virtual_nw_x_pixel': 1105014905,
                                        'virtual_nw_y_pixel': 1590484322,
                                        'virtual_width': -996350078,
                                        'virtual_height': -632449422,
                                    },
                            {
                                        'source_monitor': -67235,
                                        'source_nw_x_pixel': -736332996992518241,
                                        'source_nw_y_pixel': -2729433893359593177,
                                        'source_pixel_width': -2762942849492911873,
                                        'source_pixel_height': -5937503691209180294,
                                        'rotation': -2798627308685394615,
                                        'virtual_nw_x_pixel': -1503448304,
                                        'virtual_nw_y_pixel': 575874611,
                                        'virtual_width': 582585313,
                                        'virtual_height': -1470410639,
                                    },
                            {
                                        'source_monitor': 8186376,
                                        'source_nw_x_pixel': -4856508398774134707,
                                        'source_nw_y_pixel': -820185042542726247,
                                        'source_pixel_width': -8763870517702189054,
                                        'source_pixel_height': -3952253796903850066,
                                        'rotation': -6795819194795241521,
                                        'virtual_nw_x_pixel': -264416330,
                                        'virtual_nw_y_pixel': 1543153970,
                                        'virtual_width': 1841516342,
                                        'virtual_height': -1799390966,
                                    },
                            {
                                        'source_monitor': 5412275,
                                        'source_nw_x_pixel': -538421609621511003,
                                        'source_nw_y_pixel': -1405191450129350296,
                                        'source_pixel_width': -9155645106123057200,
                                        'source_pixel_height': -6465171971076299529,
                                        'rotation': -3660167733755085122,
                                        'virtual_nw_x_pixel': -1498203899,
                                        'virtual_nw_y_pixel': -1650965850,
                                        'virtual_width': 868125203,
                                        'virtual_height': 1868910992,
                                    },
                            {
                                        'source_monitor': 2001974,
                                        'source_nw_x_pixel': -2142533699317313660,
                                        'source_nw_y_pixel': -9154351409756833051,
                                        'source_pixel_width': -1211279627694839216,
                                        'source_pixel_height': -3958186410347844175,
                                        'rotation': -1613030005242725167,
                                        'virtual_nw_x_pixel': -624825553,
                                        'virtual_nw_y_pixel': -1382011138,
                                        'virtual_width': 307887512,
                                        'virtual_height': -1233042796,
                                    },
                            {
                                        'source_monitor': 8763234,
                                        'source_nw_x_pixel': -3828918105467102247,
                                        'source_nw_y_pixel': -7498179856610714035,
                                        'source_pixel_width': -3592131999075488593,
                                        'source_pixel_height': -994665369034739163,
                                        'rotation': -4528597520976744315,
                                        'virtual_nw_x_pixel': -1411531944,
                                        'virtual_nw_y_pixel': -1821543768,
                                        'virtual_width': -1873183195,
                                        'virtual_height': 900856404,
                                    },
                            {
                                        'source_monitor': 2334247,
                                        'source_nw_x_pixel': -7733940177269523301,
                                        'source_nw_y_pixel': -211134463701680582,
                                        'source_pixel_width': -6521977615599606396,
                                        'source_pixel_height': -6567628736454429566,
                                        'rotation': -2187690753154122575,
                                        'virtual_nw_x_pixel': -357573001,
                                        'virtual_nw_y_pixel': 1247025267,
                                        'virtual_width': 1443480366,
                                        'virtual_height': 16729567,
                                    },
                        ],
                },
                {
                    'description': 'ǯƻ҆ϹԉāȮɕŞҍѵƥѨƭļвϐʥԚʼȉCЮіɠԄȶþнĿ',
                    'monitors': [
                            {
                                        'identifier': 6773223,
                                        'width': -5141920150421639235,
                                        'height': -1900334738056441696,
                                    },
                            {
                                        'identifier': -131826,
                                        'width': 5285465336943766128,
                                        'height': -1600884151604613393,
                                    },
                            {
                                        'identifier': 5942078,
                                        'width': 8073278674313971110,
                                        'height': -6892557654459568413,
                                    },
                            {
                                        'identifier': 5165922,
                                        'width': -4092165163918916808,
                                        'height': 3880504986802080764,
                                    },
                            {
                                        'identifier': 9810274,
                                        'width': 1759941106579757693,
                                        'height': 1827698608241968373,
                                    },
                            {
                                        'identifier': 2645754,
                                        'width': 7571385060745202039,
                                        'height': 6722234107130565197,
                                    },
                            {
                                        'identifier': 4025402,
                                        'width': -8815300049938669926,
                                        'height': -5642461051038284961,
                                    },
                            {
                                        'identifier': 850071,
                                        'width': -1776200168054596249,
                                        'height': -8090120392582036303,
                                    },
                            {
                                        'identifier': 141455,
                                        'width': 7046461648658518261,
                                        'height': 7495842644749665734,
                                    },
                            {
                                        'identifier': 8310158,
                                        'width': 6249381764503997877,
                                        'height': 779607738264597065,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8114458,
                                        'source_nw_x_pixel': -2426322929545124499,
                                        'source_nw_y_pixel': -2453601197255646959,
                                        'source_pixel_width': -4190247878722640780,
                                        'source_pixel_height': -7757823224284008980,
                                        'rotation': -2803107219052259715,
                                        'virtual_nw_x_pixel': -250971951,
                                        'virtual_nw_y_pixel': 1506640280,
                                        'virtual_width': 294361959,
                                        'virtual_height': 1420479958,
                                    },
                            {
                                        'source_monitor': 1884717,
                                        'source_nw_x_pixel': -7791315254461089932,
                                        'source_nw_y_pixel': -7156506432554312377,
                                        'source_pixel_width': -8192474400453558305,
                                        'source_pixel_height': -1846189533800125794,
                                        'rotation': -1542531043378805562,
                                        'virtual_nw_x_pixel': 1175811226,
                                        'virtual_nw_y_pixel': 1630022164,
                                        'virtual_width': 954507520,
                                        'virtual_height': 1509251045,
                                    },
                            {
                                        'source_monitor': 3524547,
                                        'source_nw_x_pixel': -8436204719548708221,
                                        'source_nw_y_pixel': -482984765709538685,
                                        'source_pixel_width': -4192080585932710578,
                                        'source_pixel_height': -5022681500090284601,
                                        'rotation': -3089529435605365441,
                                        'virtual_nw_x_pixel': 415112537,
                                        'virtual_nw_y_pixel': -1625395102,
                                        'virtual_width': -183521854,
                                        'virtual_height': 1644266921,
                                    },
                            {
                                        'source_monitor': 7194696,
                                        'source_nw_x_pixel': -5358106705900339902,
                                        'source_nw_y_pixel': -2032281437468709154,
                                        'source_pixel_width': -9146245367760828825,
                                        'source_pixel_height': -5611474885674278633,
                                        'rotation': -7258387238937181660,
                                        'virtual_nw_x_pixel': 610610075,
                                        'virtual_nw_y_pixel': -1735261882,
                                        'virtual_width': -1517096579,
                                        'virtual_height': 1563548682,
                                    },
                            {
                                        'source_monitor': 9292298,
                                        'source_nw_x_pixel': -712284693000642503,
                                        'source_nw_y_pixel': -1980592706146977208,
                                        'source_pixel_width': -6643383244303723298,
                                        'source_pixel_height': -4720802108137820826,
                                        'rotation': -3434533280991634629,
                                        'virtual_nw_x_pixel': -1129047553,
                                        'virtual_nw_y_pixel': -388203548,
                                        'virtual_width': 1138075924,
                                        'virtual_height': 1682125415,
                                    },
                            {
                                        'source_monitor': 5260626,
                                        'source_nw_x_pixel': -5492007472222850158,
                                        'source_nw_y_pixel': -3503249786146296491,
                                        'source_pixel_width': -5892226878194130882,
                                        'source_pixel_height': -6989378602711415125,
                                        'rotation': -5949724143777991421,
                                        'virtual_nw_x_pixel': -1663425575,
                                        'virtual_nw_y_pixel': 526371271,
                                        'virtual_width': -1845660281,
                                        'virtual_height': -804403063,
                                    },
                            {
                                        'source_monitor': 9266002,
                                        'source_nw_x_pixel': -8175709168834772984,
                                        'source_nw_y_pixel': -4835538186215092563,
                                        'source_pixel_width': -3069446819297584590,
                                        'source_pixel_height': -1280347379298091543,
                                        'rotation': -6994667616995919615,
                                        'virtual_nw_x_pixel': -709123565,
                                        'virtual_nw_y_pixel': 1229514027,
                                        'virtual_width': -152282666,
                                        'virtual_height': -913725959,
                                    },
                            {
                                        'source_monitor': 2089084,
                                        'source_nw_x_pixel': -4825914207960307660,
                                        'source_nw_y_pixel': -101540161428744309,
                                        'source_pixel_width': -6748276726971656193,
                                        'source_pixel_height': -891439786326579177,
                                        'rotation': -782891356940569723,
                                        'virtual_nw_x_pixel': -170551044,
                                        'virtual_nw_y_pixel': -67817845,
                                        'virtual_width': -174357378,
                                        'virtual_height': 185394284,
                                    },
                            {
                                        'source_monitor': 6120130,
                                        'source_nw_x_pixel': -3626744296602669058,
                                        'source_nw_y_pixel': -1907772032000108286,
                                        'source_pixel_width': -2485568516106960397,
                                        'source_pixel_height': -1143072937405280037,
                                        'rotation': -6436467219759737920,
                                        'virtual_nw_x_pixel': 1948367484,
                                        'virtual_nw_y_pixel': 834899828,
                                        'virtual_width': -965082077,
                                        'virtual_height': 177971224,
                                    },
                            {
                                        'source_monitor': 5085329,
                                        'source_nw_x_pixel': -2042832382119288402,
                                        'source_nw_y_pixel': -7833696747003106794,
                                        'source_pixel_width': -5571074613046071834,
                                        'source_pixel_height': -8735957292759549595,
                                        'rotation': -5548897399257308027,
                                        'virtual_nw_x_pixel': -750061229,
                                        'virtual_nw_y_pixel': 276796619,
                                        'virtual_width': -119967721,
                                        'virtual_height': -1569505525,
                                    },
                        ],
                },
                {
                    'description': 'ƲЮƍǓ˳ҤýŠʗɮԟ;ÏĵɉÑέРʄͳ\x8cɱЅ˓ńˮҾΟƁΆ',
                    'monitors': [
                            {
                                        'identifier': 2941440,
                                        'width': 5218179820117449291,
                                        'height': 1116836993423999999,
                                    },
                            {
                                        'identifier': 1279474,
                                        'width': 6258519725447830327,
                                        'height': -5485632745333861377,
                                    },
                            {
                                        'identifier': 3944023,
                                        'width': 1578154769815754536,
                                        'height': -8115350497051246540,
                                    },
                            {
                                        'identifier': 7983412,
                                        'width': 7007415935419322649,
                                        'height': -4568972041597094904,
                                    },
                            {
                                        'identifier': 1467484,
                                        'width': -3125822142345888086,
                                        'height': -5335365720747776586,
                                    },
                            {
                                        'identifier': 9583407,
                                        'width': -3947324408461021564,
                                        'height': 2078507142516459123,
                                    },
                            {
                                        'identifier': 2175397,
                                        'width': 5157587741169155396,
                                        'height': 1883414583725471153,
                                    },
                            {
                                        'identifier': 8653581,
                                        'width': -2665573905967442063,
                                        'height': -5746410836364841816,
                                    },
                            {
                                        'identifier': 5476514,
                                        'width': 7835845205636504303,
                                        'height': -1243166088024575813,
                                    },
                            {
                                        'identifier': -875591,
                                        'width': -6834774505208499489,
                                        'height': 3416155009158739134,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5450622,
                                        'source_nw_x_pixel': -8555911460799159547,
                                        'source_nw_y_pixel': -6910616584172351149,
                                        'source_pixel_width': -842330448367609588,
                                        'source_pixel_height': -5547916026342119898,
                                        'rotation': -5481709264884833633,
                                        'virtual_nw_x_pixel': -1353551759,
                                        'virtual_nw_y_pixel': 455560934,
                                        'virtual_width': 1981744946,
                                        'virtual_height': -140627539,
                                    },
                            {
                                        'source_monitor': 680435,
                                        'source_nw_x_pixel': -2762074199036851096,
                                        'source_nw_y_pixel': -2290918892140425105,
                                        'source_pixel_width': -2979189448845231977,
                                        'source_pixel_height': -3741181048605693697,
                                        'rotation': -8310068275954595210,
                                        'virtual_nw_x_pixel': -1580511948,
                                        'virtual_nw_y_pixel': -1034783514,
                                        'virtual_width': -1703761010,
                                        'virtual_height': 86897198,
                                    },
                            {
                                        'source_monitor': -930671,
                                        'source_nw_x_pixel': -4404979741683353670,
                                        'source_nw_y_pixel': -3874898415217495064,
                                        'source_pixel_width': -6557695351160150679,
                                        'source_pixel_height': -2627907353980560970,
                                        'rotation': -9047802279896233626,
                                        'virtual_nw_x_pixel': -1145252842,
                                        'virtual_nw_y_pixel': 929924662,
                                        'virtual_width': 1050388254,
                                        'virtual_height': 527388147,
                                    },
                            {
                                        'source_monitor': 8904513,
                                        'source_nw_x_pixel': -5066629721163631700,
                                        'source_nw_y_pixel': -6862217814785588741,
                                        'source_pixel_width': -3839784921743048102,
                                        'source_pixel_height': -8848428985919096023,
                                        'rotation': -2351164483437912224,
                                        'virtual_nw_x_pixel': 532034410,
                                        'virtual_nw_y_pixel': 234801383,
                                        'virtual_width': 731102751,
                                        'virtual_height': 745765590,
                                    },
                            {
                                        'source_monitor': 2975496,
                                        'source_nw_x_pixel': -4411056482672610795,
                                        'source_nw_y_pixel': -4341956948190502202,
                                        'source_pixel_width': -6038412389847812338,
                                        'source_pixel_height': -4503655967856791802,
                                        'rotation': -6779515342160997905,
                                        'virtual_nw_x_pixel': -196981555,
                                        'virtual_nw_y_pixel': -717670603,
                                        'virtual_width': 926817175,
                                        'virtual_height': 993983859,
                                    },
                            {
                                        'source_monitor': -576043,
                                        'source_nw_x_pixel': -886730935570719827,
                                        'source_nw_y_pixel': -1206138189358772685,
                                        'source_pixel_width': -7340190406407220503,
                                        'source_pixel_height': -8833173145813117306,
                                        'rotation': -1478104982637593266,
                                        'virtual_nw_x_pixel': -1398432905,
                                        'virtual_nw_y_pixel': -1297115510,
                                        'virtual_width': 400778276,
                                        'virtual_height': 220612556,
                                    },
                            {
                                        'source_monitor': 3577550,
                                        'source_nw_x_pixel': -2683509362360815306,
                                        'source_nw_y_pixel': -585336171302878997,
                                        'source_pixel_width': -4897285378266900466,
                                        'source_pixel_height': -955828247788585286,
                                        'rotation': -5221805618675994133,
                                        'virtual_nw_x_pixel': 340724082,
                                        'virtual_nw_y_pixel': -1687903822,
                                        'virtual_width': 235272721,
                                        'virtual_height': -421844618,
                                    },
                            {
                                        'source_monitor': 5912429,
                                        'source_nw_x_pixel': -4717803182938479318,
                                        'source_nw_y_pixel': -7096568495378613676,
                                        'source_pixel_width': -6671179958466093078,
                                        'source_pixel_height': -2612432137672884203,
                                        'rotation': -7748886700078997980,
                                        'virtual_nw_x_pixel': 1872897383,
                                        'virtual_nw_y_pixel': -1445866947,
                                        'virtual_width': 927672099,
                                        'virtual_height': 1823159982,
                                    },
                            {
                                        'source_monitor': 2783741,
                                        'source_nw_x_pixel': -9019981401781207538,
                                        'source_nw_y_pixel': -8704565803551970465,
                                        'source_pixel_width': -7728113584912564147,
                                        'source_pixel_height': -6692356857382577085,
                                        'rotation': -5931235313181543501,
                                        'virtual_nw_x_pixel': 182258625,
                                        'virtual_nw_y_pixel': -1959878029,
                                        'virtual_width': 1641327631,
                                        'virtual_height': 749612584,
                                    },
                            {
                                        'source_monitor': 5300727,
                                        'source_nw_x_pixel': -7032814766529835524,
                                        'source_nw_y_pixel': -7569582625323549045,
                                        'source_pixel_width': -7109272989971933116,
                                        'source_pixel_height': -6099158656233351243,
                                        'rotation': -7372270165856227120,
                                        'virtual_nw_x_pixel': 1520013768,
                                        'virtual_nw_y_pixel': -1422134079,
                                        'virtual_width': 75910151,
                                        'virtual_height': 1204479009,
                                    },
                        ],
                },
                {
                    'description': "ÝΈ\u0378Χǚɱ'юΨτѩŶ\x82ìϰØԦЛɁ˅ʒ˞л·ɲԒǨɶŷ\u0381",
                    'monitors': [
                            {
                                        'identifier': 7860395,
                                        'width': 4732463746988370930,
                                        'height': -7767400848918455661,
                                    },
                            {
                                        'identifier': 2180033,
                                        'width': -5013717399760063797,
                                        'height': -2761263423150714971,
                                    },
                            {
                                        'identifier': 2644462,
                                        'width': -3190757932617867242,
                                        'height': 4189318996309415379,
                                    },
                            {
                                        'identifier': 5960499,
                                        'width': -894198750051167415,
                                        'height': 8638135070886366184,
                                    },
                            {
                                        'identifier': 4537611,
                                        'width': 8764877874381930395,
                                        'height': -5111337316416111894,
                                    },
                            {
                                        'identifier': -29212,
                                        'width': 815650473430781181,
                                        'height': -443948997736427744,
                                    },
                            {
                                        'identifier': 3961073,
                                        'width': 4426933545359136441,
                                        'height': -6195859276107193821,
                                    },
                            {
                                        'identifier': 5706569,
                                        'width': 8092610562656006767,
                                        'height': -4763015517801214356,
                                    },
                            {
                                        'identifier': 2321740,
                                        'width': 2097749686726538570,
                                        'height': -7917431032323125836,
                                    },
                            {
                                        'identifier': 7857416,
                                        'width': -7430982557455989940,
                                        'height': -7037057230161766834,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4333267,
                                        'source_nw_x_pixel': -8277162835594511365,
                                        'source_nw_y_pixel': -472053775707326739,
                                        'source_pixel_width': -8151025236936465114,
                                        'source_pixel_height': -5050182887561270677,
                                        'rotation': -4185030527778410765,
                                        'virtual_nw_x_pixel': -92814969,
                                        'virtual_nw_y_pixel': 84721335,
                                        'virtual_width': -1947075388,
                                        'virtual_height': -1570569072,
                                    },
                            {
                                        'source_monitor': 3341217,
                                        'source_nw_x_pixel': -3349897222867984370,
                                        'source_nw_y_pixel': -4015694542025169226,
                                        'source_pixel_width': -8456584606433851534,
                                        'source_pixel_height': -3616676174681090298,
                                        'rotation': -5339777457227898039,
                                        'virtual_nw_x_pixel': 1518113580,
                                        'virtual_nw_y_pixel': -292773324,
                                        'virtual_width': 593099481,
                                        'virtual_height': 601444079,
                                    },
                            {
                                        'source_monitor': 2091549,
                                        'source_nw_x_pixel': -2739875923954056831,
                                        'source_nw_y_pixel': -4400577453591263836,
                                        'source_pixel_width': -6676844762797982220,
                                        'source_pixel_height': -6439705163788024412,
                                        'rotation': -4503856122314160377,
                                        'virtual_nw_x_pixel': 1135379374,
                                        'virtual_nw_y_pixel': 1894531744,
                                        'virtual_width': -1936629785,
                                        'virtual_height': 133536618,
                                    },
                            {
                                        'source_monitor': 6934505,
                                        'source_nw_x_pixel': -1201298777339759093,
                                        'source_nw_y_pixel': -3104558308674375157,
                                        'source_pixel_width': -3586459457750858436,
                                        'source_pixel_height': -7306092584810272490,
                                        'rotation': -1380154409976919972,
                                        'virtual_nw_x_pixel': -1604767559,
                                        'virtual_nw_y_pixel': -298505434,
                                        'virtual_width': 1127019683,
                                        'virtual_height': 520414279,
                                    },
                            {
                                        'source_monitor': 273908,
                                        'source_nw_x_pixel': -6923416866691375148,
                                        'source_nw_y_pixel': -2264120469780692963,
                                        'source_pixel_width': -4058447144431837436,
                                        'source_pixel_height': -7444327729515932299,
                                        'rotation': -3176281906895094755,
                                        'virtual_nw_x_pixel': -338396245,
                                        'virtual_nw_y_pixel': 346812944,
                                        'virtual_width': 1227704523,
                                        'virtual_height': 49467967,
                                    },
                            {
                                        'source_monitor': 4319339,
                                        'source_nw_x_pixel': -6751546606621079390,
                                        'source_nw_y_pixel': -1330838616725039368,
                                        'source_pixel_width': -8128015191253904751,
                                        'source_pixel_height': -1820698843555520562,
                                        'rotation': -1355987431265704658,
                                        'virtual_nw_x_pixel': -1715090181,
                                        'virtual_nw_y_pixel': -326313822,
                                        'virtual_width': 1441613067,
                                        'virtual_height': -1130789779,
                                    },
                            {
                                        'source_monitor': 3576961,
                                        'source_nw_x_pixel': -591162875518194493,
                                        'source_nw_y_pixel': -4610231478911205823,
                                        'source_pixel_width': -3012360966081043169,
                                        'source_pixel_height': -6280325549806064639,
                                        'rotation': -7633081701277519451,
                                        'virtual_nw_x_pixel': 866439649,
                                        'virtual_nw_y_pixel': 1571434784,
                                        'virtual_width': -1124624729,
                                        'virtual_height': -1410117087,
                                    },
                            {
                                        'source_monitor': 6946957,
                                        'source_nw_x_pixel': -6648916225163900888,
                                        'source_nw_y_pixel': -8171048596905668358,
                                        'source_pixel_width': -5982363244546069144,
                                        'source_pixel_height': -3160403033101113917,
                                        'rotation': -5883397814445147832,
                                        'virtual_nw_x_pixel': -1867092931,
                                        'virtual_nw_y_pixel': 1927031869,
                                        'virtual_width': 1724582031,
                                        'virtual_height': 1496827500,
                                    },
                            {
                                        'source_monitor': 1943216,
                                        'source_nw_x_pixel': -7120894032823144367,
                                        'source_nw_y_pixel': -9059657488058058671,
                                        'source_pixel_width': -7550994427649377760,
                                        'source_pixel_height': -4797050094518394755,
                                        'rotation': -2328378856192271279,
                                        'virtual_nw_x_pixel': 1660327871,
                                        'virtual_nw_y_pixel': 636297690,
                                        'virtual_width': -314752551,
                                        'virtual_height': 1017711487,
                                    },
                            {
                                        'source_monitor': 4664673,
                                        'source_nw_x_pixel': -1230635709049443095,
                                        'source_nw_y_pixel': -2931919958634769954,
                                        'source_pixel_width': -5173086912558380343,
                                        'source_pixel_height': -9124921388885808548,
                                        'rotation': -1355963692193743663,
                                        'virtual_nw_x_pixel': -651308562,
                                        'virtual_nw_y_pixel': -576537529,
                                        'virtual_width': 559891554,
                                        'virtual_height': -927796866,
                                    },
                        ],
                },
                {
                    'description': 'ɗȧɿнăȪӔяҲʏǟҤæҽ\u0378ԎˉsЀΖǁǔ¤ͱ½ϛïhxԞ',
                    'monitors': [
                            {
                                        'identifier': 4345510,
                                        'width': -5294763411033251012,
                                        'height': 5868556855345082054,
                                    },
                            {
                                        'identifier': 3856462,
                                        'width': -8297567329577462915,
                                        'height': -7427319817404777830,
                                    },
                            {
                                        'identifier': 551660,
                                        'width': -5424063055353941804,
                                        'height': 4920983349382761463,
                                    },
                            {
                                        'identifier': 6002033,
                                        'width': 1397377875870005001,
                                        'height': -3434364450699212778,
                                    },
                            {
                                        'identifier': -410996,
                                        'width': -7551221923288941373,
                                        'height': 7264314318250499002,
                                    },
                            {
                                        'identifier': 9202178,
                                        'width': 6484655932648416223,
                                        'height': -6934534037952144262,
                                    },
                            {
                                        'identifier': 4244196,
                                        'width': 2432509838911040511,
                                        'height': 88320507526275459,
                                    },
                            {
                                        'identifier': 656713,
                                        'width': -2374058705562488421,
                                        'height': -3321039840415765472,
                                    },
                            {
                                        'identifier': 6466429,
                                        'width': 6897025593596545296,
                                        'height': 1266594596241764644,
                                    },
                            {
                                        'identifier': 3878304,
                                        'width': 3489275269740934222,
                                        'height': 9176647554986622787,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8661705,
                                        'source_nw_x_pixel': -828643848022800384,
                                        'source_nw_y_pixel': -3529638383420733091,
                                        'source_pixel_width': -2555361141955034113,
                                        'source_pixel_height': -5155898895169762572,
                                        'rotation': -4246919306841619125,
                                        'virtual_nw_x_pixel': 917143814,
                                        'virtual_nw_y_pixel': 1026194449,
                                        'virtual_width': -1373905544,
                                        'virtual_height': -1465978099,
                                    },
                            {
                                        'source_monitor': 6153138,
                                        'source_nw_x_pixel': -7182348359664468245,
                                        'source_nw_y_pixel': -1244365031601226283,
                                        'source_pixel_width': -2750514320185425921,
                                        'source_pixel_height': -8499903496977620990,
                                        'rotation': -7842360071348507715,
                                        'virtual_nw_x_pixel': 1060763720,
                                        'virtual_nw_y_pixel': 1108908198,
                                        'virtual_width': 1324170931,
                                        'virtual_height': 4025140,
                                    },
                            {
                                        'source_monitor': 9274617,
                                        'source_nw_x_pixel': -5309362068427653410,
                                        'source_nw_y_pixel': -4198694596191261769,
                                        'source_pixel_width': -1141683081479158180,
                                        'source_pixel_height': -4445471279352656777,
                                        'rotation': -273443102351327665,
                                        'virtual_nw_x_pixel': 1776945011,
                                        'virtual_nw_y_pixel': -1195481449,
                                        'virtual_width': 995790245,
                                        'virtual_height': -1077823236,
                                    },
                            {
                                        'source_monitor': 6743536,
                                        'source_nw_x_pixel': -966855004207779075,
                                        'source_nw_y_pixel': -3796745585531401326,
                                        'source_pixel_width': -4423049773405062304,
                                        'source_pixel_height': -1020077848398994413,
                                        'rotation': -7969930874380124109,
                                        'virtual_nw_x_pixel': -753343383,
                                        'virtual_nw_y_pixel': -1475003438,
                                        'virtual_width': 992630128,
                                        'virtual_height': -594780502,
                                    },
                            {
                                        'source_monitor': 412575,
                                        'source_nw_x_pixel': -2417255461658387028,
                                        'source_nw_y_pixel': -4559650712520401224,
                                        'source_pixel_width': -1923557308175399757,
                                        'source_pixel_height': -3021050704622321285,
                                        'rotation': -7585049242304746646,
                                        'virtual_nw_x_pixel': 860945247,
                                        'virtual_nw_y_pixel': -506910502,
                                        'virtual_width': -1152873089,
                                        'virtual_height': 51401315,
                                    },
                            {
                                        'source_monitor': 8616309,
                                        'source_nw_x_pixel': -8435279489987579399,
                                        'source_nw_y_pixel': -2869002867891150529,
                                        'source_pixel_width': -1317189359987239336,
                                        'source_pixel_height': -598531220454867323,
                                        'rotation': -6846749297665371682,
                                        'virtual_nw_x_pixel': -1135788259,
                                        'virtual_nw_y_pixel': 259026578,
                                        'virtual_width': 620125981,
                                        'virtual_height': -1768958639,
                                    },
                            {
                                        'source_monitor': -736789,
                                        'source_nw_x_pixel': -5118509645329260163,
                                        'source_nw_y_pixel': -1863279442198547932,
                                        'source_pixel_width': -2545940712815239237,
                                        'source_pixel_height': -6458306603390070655,
                                        'rotation': -5826254946564324509,
                                        'virtual_nw_x_pixel': 427985065,
                                        'virtual_nw_y_pixel': -1858435529,
                                        'virtual_width': 160167273,
                                        'virtual_height': 1997669311,
                                    },
                            {
                                        'source_monitor': 323842,
                                        'source_nw_x_pixel': -7993649578077514302,
                                        'source_nw_y_pixel': -7468809585657640079,
                                        'source_pixel_width': -1288318256852554735,
                                        'source_pixel_height': -2966891639676462242,
                                        'rotation': -5980876806273416556,
                                        'virtual_nw_x_pixel': -1557352608,
                                        'virtual_nw_y_pixel': -1816677794,
                                        'virtual_width': 657178314,
                                        'virtual_height': -1396928063,
                                    },
                            {
                                        'source_monitor': 1689943,
                                        'source_nw_x_pixel': -5352834640453090163,
                                        'source_nw_y_pixel': -6211057488735060228,
                                        'source_pixel_width': -1577181547121963825,
                                        'source_pixel_height': -5546742427400811144,
                                        'rotation': -1183492696906626396,
                                        'virtual_nw_x_pixel': -744107534,
                                        'virtual_nw_y_pixel': 134772537,
                                        'virtual_width': 512538265,
                                        'virtual_height': 20853927,
                                    },
                            {
                                        'source_monitor': 3687578,
                                        'source_nw_x_pixel': -5646668813112504360,
                                        'source_nw_y_pixel': -4338893369879517422,
                                        'source_pixel_width': -1994690258303395075,
                                        'source_pixel_height': -541624111696469236,
                                        'rotation': -7147934303862400109,
                                        'virtual_nw_x_pixel': -249835557,
                                        'virtual_nw_y_pixel': 1801839940,
                                        'virtual_width': -1036186887,
                                        'virtual_height': -138028635,
                                    },
                        ],
                },
                {
                    'description': 'ˈқήưƄӏǧĳˉ¼ȧЅԇɔƙÇʞΆҠǢӢϥ0ΊǥȬҘԢīƝ',
                    'monitors': [
                            {
                                        'identifier': 9094488,
                                        'width': 5890609922933838684,
                                        'height': 9129647477086642787,
                                    },
                            {
                                        'identifier': 2166227,
                                        'width': -4514721583758108761,
                                        'height': -3662635783499484374,
                                    },
                            {
                                        'identifier': 3237576,
                                        'width': 1622966763308699829,
                                        'height': 2535665715912442368,
                                    },
                            {
                                        'identifier': 1177561,
                                        'width': -1164443873942544656,
                                        'height': -1373789174101976429,
                                    },
                            {
                                        'identifier': 4276954,
                                        'width': 3778184713577557669,
                                        'height': 1024561288461493860,
                                    },
                            {
                                        'identifier': 2398020,
                                        'width': -8158497595464909431,
                                        'height': -801370270165845794,
                                    },
                            {
                                        'identifier': 8313874,
                                        'width': -2502037433693027475,
                                        'height': 40545418312566057,
                                    },
                            {
                                        'identifier': 3604174,
                                        'width': -2496679213408688691,
                                        'height': -1270866832208115656,
                                    },
                            {
                                        'identifier': 2182199,
                                        'width': 170282441050557392,
                                        'height': 7821884769165776501,
                                    },
                            {
                                        'identifier': 6178963,
                                        'width': -9185283670860263086,
                                        'height': 8226809423100999512,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9039414,
                                        'source_nw_x_pixel': -4318749250083008444,
                                        'source_nw_y_pixel': -5723948535124642751,
                                        'source_pixel_width': -401584703790667353,
                                        'source_pixel_height': -4318929748729583462,
                                        'rotation': -7306038257814621568,
                                        'virtual_nw_x_pixel': -1278471631,
                                        'virtual_nw_y_pixel': 644402060,
                                        'virtual_width': -592926307,
                                        'virtual_height': -678497395,
                                    },
                            {
                                        'source_monitor': 8606899,
                                        'source_nw_x_pixel': -1640485817977638075,
                                        'source_nw_y_pixel': -1360441864343181996,
                                        'source_pixel_width': -3918525214251570374,
                                        'source_pixel_height': -4380867947291038227,
                                        'rotation': -4332089221003211020,
                                        'virtual_nw_x_pixel': 658579018,
                                        'virtual_nw_y_pixel': -937955852,
                                        'virtual_width': 453975614,
                                        'virtual_height': -49188340,
                                    },
                            {
                                        'source_monitor': 5895974,
                                        'source_nw_x_pixel': -1731746831210855336,
                                        'source_nw_y_pixel': -8467944557444110438,
                                        'source_pixel_width': -2443851206512880631,
                                        'source_pixel_height': -5494570298591128691,
                                        'rotation': -5281250776395680149,
                                        'virtual_nw_x_pixel': 1630073012,
                                        'virtual_nw_y_pixel': 851054460,
                                        'virtual_width': 1221888569,
                                        'virtual_height': 1550219296,
                                    },
                            {
                                        'source_monitor': 3468503,
                                        'source_nw_x_pixel': -3072324159286354527,
                                        'source_nw_y_pixel': -528007359640252713,
                                        'source_pixel_width': -8009849376186993912,
                                        'source_pixel_height': -1890077226256012262,
                                        'rotation': -8012214778996085730,
                                        'virtual_nw_x_pixel': 811041580,
                                        'virtual_nw_y_pixel': 904333319,
                                        'virtual_width': -1853380262,
                                        'virtual_height': -582696718,
                                    },
                            {
                                        'source_monitor': -593251,
                                        'source_nw_x_pixel': -8575901720524496326,
                                        'source_nw_y_pixel': -223807149826496642,
                                        'source_pixel_width': -4579677162901798491,
                                        'source_pixel_height': -717708358673734222,
                                        'rotation': -4570022889297298436,
                                        'virtual_nw_x_pixel': 405156711,
                                        'virtual_nw_y_pixel': 101249856,
                                        'virtual_width': 896539531,
                                        'virtual_height': 1205175999,
                                    },
                            {
                                        'source_monitor': 164153,
                                        'source_nw_x_pixel': -4538695001120719903,
                                        'source_nw_y_pixel': -2541848625035675210,
                                        'source_pixel_width': -1929420325980959689,
                                        'source_pixel_height': -5952665776557646425,
                                        'rotation': -195379739744975899,
                                        'virtual_nw_x_pixel': 41228917,
                                        'virtual_nw_y_pixel': -1725301806,
                                        'virtual_width': -613421624,
                                        'virtual_height': 134143359,
                                    },
                            {
                                        'source_monitor': -962148,
                                        'source_nw_x_pixel': -2893659627852665889,
                                        'source_nw_y_pixel': -5120661086665415432,
                                        'source_pixel_width': -6831021743250575480,
                                        'source_pixel_height': -2684518534362982418,
                                        'rotation': -1394543869753075619,
                                        'virtual_nw_x_pixel': 1088685885,
                                        'virtual_nw_y_pixel': 1411970273,
                                        'virtual_width': -172886715,
                                        'virtual_height': 989331416,
                                    },
                            {
                                        'source_monitor': 8300915,
                                        'source_nw_x_pixel': -4544300124459080452,
                                        'source_nw_y_pixel': -1221618988799122599,
                                        'source_pixel_width': -2143220593984607428,
                                        'source_pixel_height': -5618784673191749011,
                                        'rotation': -4713016649955026301,
                                        'virtual_nw_x_pixel': 1838802435,
                                        'virtual_nw_y_pixel': -414212814,
                                        'virtual_width': -1653882944,
                                        'virtual_height': 1949855107,
                                    },
                            {
                                        'source_monitor': 4945274,
                                        'source_nw_x_pixel': -9151118946539098308,
                                        'source_nw_y_pixel': -5439625991205495403,
                                        'source_pixel_width': -4201618714894186666,
                                        'source_pixel_height': -6718136003985487712,
                                        'rotation': -5620896280049052647,
                                        'virtual_nw_x_pixel': 492219302,
                                        'virtual_nw_y_pixel': -1372929484,
                                        'virtual_width': 415536271,
                                        'virtual_height': 986479938,
                                    },
                            {
                                        'source_monitor': 1064583,
                                        'source_nw_x_pixel': -6003462832632725184,
                                        'source_nw_y_pixel': -5855354013023875290,
                                        'source_pixel_width': -8174336583810556027,
                                        'source_pixel_height': -8800730043121236258,
                                        'rotation': -4226714749593311612,
                                        'virtual_nw_x_pixel': 308827555,
                                        'virtual_nw_y_pixel': -1446785163,
                                        'virtual_width': 1947853604,
                                        'virtual_height': -1867617458,
                                    },
                        ],
                },
                {
                    'description': 'ǵĮҬǛ҇\x87ѠԓǺѶҦɂϰǆ˨ǀʙ҄ѭѬƹҿƍĚɶǑƪȮȅφ',
                    'monitors': [
                            {
                                        'identifier': 5803489,
                                        'width': -1880649023819284227,
                                        'height': 336732163620860911,
                                    },
                            {
                                        'identifier': -335492,
                                        'width': -5392469282529455067,
                                        'height': 9206015887144500835,
                                    },
                            {
                                        'identifier': 5734165,
                                        'width': 1077036473814299813,
                                        'height': 9038869885004664556,
                                    },
                            {
                                        'identifier': -711058,
                                        'width': -8787518489682713747,
                                        'height': 813375410778717370,
                                    },
                            {
                                        'identifier': 8130416,
                                        'width': -6919271335829364961,
                                        'height': 1259287354782654026,
                                    },
                            {
                                        'identifier': 7456049,
                                        'width': -2128996171182382451,
                                        'height': 6538440030396101287,
                                    },
                            {
                                        'identifier': 874274,
                                        'width': 6357601940956339834,
                                        'height': -4867960889090293790,
                                    },
                            {
                                        'identifier': 1687182,
                                        'width': 7555545292682554528,
                                        'height': -1596034847103428737,
                                    },
                            {
                                        'identifier': 8794603,
                                        'width': 4535788241304505764,
                                        'height': 606128300320065798,
                                    },
                            {
                                        'identifier': 6490883,
                                        'width': -5970182464287448923,
                                        'height': -5158862826529520992,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 416801,
                                        'source_nw_x_pixel': -5963349416253170295,
                                        'source_nw_y_pixel': -1256536325239783690,
                                        'source_pixel_width': -5751334933299990341,
                                        'source_pixel_height': -2477405466719823596,
                                        'rotation': -1519979451644923771,
                                        'virtual_nw_x_pixel': 679004506,
                                        'virtual_nw_y_pixel': -1133293068,
                                        'virtual_width': 1278706739,
                                        'virtual_height': -1755957739,
                                    },
                            {
                                        'source_monitor': 5713287,
                                        'source_nw_x_pixel': -5366841050704219656,
                                        'source_nw_y_pixel': -3249257341970072964,
                                        'source_pixel_width': -9182895879889154937,
                                        'source_pixel_height': -3538160315136995911,
                                        'rotation': -6291754651313904488,
                                        'virtual_nw_x_pixel': -623717467,
                                        'virtual_nw_y_pixel': -248000302,
                                        'virtual_width': -1937695793,
                                        'virtual_height': -1969855282,
                                    },
                            {
                                        'source_monitor': 6400212,
                                        'source_nw_x_pixel': -4348906669711772354,
                                        'source_nw_y_pixel': -8242838138295761803,
                                        'source_pixel_width': -2872577318980084789,
                                        'source_pixel_height': -428926852086321299,
                                        'rotation': -8597812317164433048,
                                        'virtual_nw_x_pixel': 766354528,
                                        'virtual_nw_y_pixel': 1681075969,
                                        'virtual_width': 519909937,
                                        'virtual_height': -420891625,
                                    },
                            {
                                        'source_monitor': 6165433,
                                        'source_nw_x_pixel': -7293020369910358833,
                                        'source_nw_y_pixel': -5690117104804883414,
                                        'source_pixel_width': -1490399284025353062,
                                        'source_pixel_height': -1647252712463772551,
                                        'rotation': -2870157585512053580,
                                        'virtual_nw_x_pixel': 1725019175,
                                        'virtual_nw_y_pixel': 1227542803,
                                        'virtual_width': 718349291,
                                        'virtual_height': -1003582788,
                                    },
                            {
                                        'source_monitor': 3375450,
                                        'source_nw_x_pixel': -7256774652344019093,
                                        'source_nw_y_pixel': -7738415630996715177,
                                        'source_pixel_width': -6202491725737154424,
                                        'source_pixel_height': -5756190402605126424,
                                        'rotation': -2038627485147466039,
                                        'virtual_nw_x_pixel': 858445291,
                                        'virtual_nw_y_pixel': 720100100,
                                        'virtual_width': -956141836,
                                        'virtual_height': 1743423256,
                                    },
                            {
                                        'source_monitor': 2095069,
                                        'source_nw_x_pixel': -646688224645245852,
                                        'source_nw_y_pixel': -7435538497173889114,
                                        'source_pixel_width': -5986649827923426223,
                                        'source_pixel_height': -2419894508185299675,
                                        'rotation': -1117649900858732812,
                                        'virtual_nw_x_pixel': 603283928,
                                        'virtual_nw_y_pixel': 1822923532,
                                        'virtual_width': 314748375,
                                        'virtual_height': -646470813,
                                    },
                            {
                                        'source_monitor': 6959099,
                                        'source_nw_x_pixel': -3917390252871624671,
                                        'source_nw_y_pixel': -6034472150543176215,
                                        'source_pixel_width': -7054891293984186569,
                                        'source_pixel_height': -7756102044430067366,
                                        'rotation': -917462372833757602,
                                        'virtual_nw_x_pixel': -938225648,
                                        'virtual_nw_y_pixel': 1494132804,
                                        'virtual_width': -747199454,
                                        'virtual_height': -482331075,
                                    },
                            {
                                        'source_monitor': 2748903,
                                        'source_nw_x_pixel': -6962785860421334172,
                                        'source_nw_y_pixel': -2938862922311242361,
                                        'source_pixel_width': -2742277672418949034,
                                        'source_pixel_height': -6820654811067373932,
                                        'rotation': -4951510717631123405,
                                        'virtual_nw_x_pixel': 52040707,
                                        'virtual_nw_y_pixel': 1817375984,
                                        'virtual_width': -1112662670,
                                        'virtual_height': 568186957,
                                    },
                            {
                                        'source_monitor': 7153670,
                                        'source_nw_x_pixel': -3522202785332873761,
                                        'source_nw_y_pixel': -1586030528475865935,
                                        'source_pixel_width': -8764729702612136351,
                                        'source_pixel_height': -7315546513452227242,
                                        'rotation': -523890733394899275,
                                        'virtual_nw_x_pixel': 719858091,
                                        'virtual_nw_y_pixel': 838675098,
                                        'virtual_width': -1863345350,
                                        'virtual_height': 1909954104,
                                    },
                            {
                                        'source_monitor': 3817573,
                                        'source_nw_x_pixel': -1448802105785445047,
                                        'source_nw_y_pixel': -4180250196359875918,
                                        'source_pixel_width': -712681855614322816,
                                        'source_pixel_height': -3762665643330111608,
                                        'rotation': -3778781080040166855,
                                        'virtual_nw_x_pixel': -1982414391,
                                        'virtual_nw_y_pixel': 1566310991,
                                        'virtual_width': -539912988,
                                        'virtual_height': -1654419384,
                                    },
                        ],
                },
                {
                    'description': "Ӎʆϟχɒz'Ǘ{ԉОɀЛƷҌΏсǛŭέԖќϩЫɗɌƢч˛Ƶ",
                    'monitors': [
                            {
                                        'identifier': 3617287,
                                        'width': -4070799524856951268,
                                        'height': 4167082838296145519,
                                    },
                            {
                                        'identifier': 5992297,
                                        'width': 3899757976596247555,
                                        'height': 3197252513211251857,
                                    },
                            {
                                        'identifier': -750844,
                                        'width': -338865096805025863,
                                        'height': 593098343222725199,
                                    },
                            {
                                        'identifier': 6200559,
                                        'width': 1071841742943094025,
                                        'height': -8797796318385294278,
                                    },
                            {
                                        'identifier': 1714037,
                                        'width': -8444564547195831393,
                                        'height': 8010535667327260518,
                                    },
                            {
                                        'identifier': 9598438,
                                        'width': -6386464196854154364,
                                        'height': 3956696090482641055,
                                    },
                            {
                                        'identifier': 7301769,
                                        'width': 2577811860968322788,
                                        'height': 5293496508533313066,
                                    },
                            {
                                        'identifier': 7492132,
                                        'width': 1633699860513656150,
                                        'height': 6873857582248261140,
                                    },
                            {
                                        'identifier': 1802777,
                                        'width': -4226107064913544184,
                                        'height': -1804169607616482054,
                                    },
                            {
                                        'identifier': 6735203,
                                        'width': 895826215535969415,
                                        'height': -2284032769851187141,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3768531,
                                        'source_nw_x_pixel': -6803241596624125228,
                                        'source_nw_y_pixel': -707860768298794685,
                                        'source_pixel_width': -6537048474950879413,
                                        'source_pixel_height': -881852280864218438,
                                        'rotation': -2851035720725041708,
                                        'virtual_nw_x_pixel': 1011989713,
                                        'virtual_nw_y_pixel': 471957840,
                                        'virtual_width': -30467709,
                                        'virtual_height': 40331811,
                                    },
                            {
                                        'source_monitor': 1372097,
                                        'source_nw_x_pixel': -3862937543275764509,
                                        'source_nw_y_pixel': -5014413526326136268,
                                        'source_pixel_width': -6253472779196404473,
                                        'source_pixel_height': -4068908480243971117,
                                        'rotation': -8105883923215656324,
                                        'virtual_nw_x_pixel': 1883851780,
                                        'virtual_nw_y_pixel': 1426358057,
                                        'virtual_width': -686352818,
                                        'virtual_height': 451861838,
                                    },
                            {
                                        'source_monitor': 1820986,
                                        'source_nw_x_pixel': -5117081178193676321,
                                        'source_nw_y_pixel': -8594329086716784726,
                                        'source_pixel_width': -792887201854140341,
                                        'source_pixel_height': -7762252441694554714,
                                        'rotation': -8589081624020771188,
                                        'virtual_nw_x_pixel': -196196259,
                                        'virtual_nw_y_pixel': 632789098,
                                        'virtual_width': 248358229,
                                        'virtual_height': 259539226,
                                    },
                            {
                                        'source_monitor': 795012,
                                        'source_nw_x_pixel': -2495625591265986289,
                                        'source_nw_y_pixel': -6473023913870022349,
                                        'source_pixel_width': -8460251758305616140,
                                        'source_pixel_height': -8834229815321535898,
                                        'rotation': -7569905430036411600,
                                        'virtual_nw_x_pixel': 756011044,
                                        'virtual_nw_y_pixel': 1024699210,
                                        'virtual_width': -250269934,
                                        'virtual_height': -677929198,
                                    },
                            {
                                        'source_monitor': 9747820,
                                        'source_nw_x_pixel': -3476993140181800504,
                                        'source_nw_y_pixel': -2093542887844138818,
                                        'source_pixel_width': -9182112712344763514,
                                        'source_pixel_height': -2124966258748103198,
                                        'rotation': -6001037969256815005,
                                        'virtual_nw_x_pixel': -440967539,
                                        'virtual_nw_y_pixel': -168461028,
                                        'virtual_width': 232798187,
                                        'virtual_height': 292758513,
                                    },
                            {
                                        'source_monitor': 5183491,
                                        'source_nw_x_pixel': -6236728088975077969,
                                        'source_nw_y_pixel': -4377466354620854647,
                                        'source_pixel_width': -1750499985061499162,
                                        'source_pixel_height': -2240574085223691716,
                                        'rotation': -6883804775775659633,
                                        'virtual_nw_x_pixel': 73041263,
                                        'virtual_nw_y_pixel': -1433621539,
                                        'virtual_width': -1221067860,
                                        'virtual_height': 1372339744,
                                    },
                            {
                                        'source_monitor': 5609004,
                                        'source_nw_x_pixel': -5336345486678246905,
                                        'source_nw_y_pixel': -3611353563552131007,
                                        'source_pixel_width': -7349671005342232520,
                                        'source_pixel_height': -668853952754961683,
                                        'rotation': -8421211982699580954,
                                        'virtual_nw_x_pixel': 1485547607,
                                        'virtual_nw_y_pixel': 710576126,
                                        'virtual_width': 1504162909,
                                        'virtual_height': -109229303,
                                    },
                            {
                                        'source_monitor': 2296188,
                                        'source_nw_x_pixel': -5196558319857966006,
                                        'source_nw_y_pixel': -9177172766493154206,
                                        'source_pixel_width': -606345502528969682,
                                        'source_pixel_height': -6830841338972223998,
                                        'rotation': -3894740147642912151,
                                        'virtual_nw_x_pixel': 1899845552,
                                        'virtual_nw_y_pixel': -1932692061,
                                        'virtual_width': -124670626,
                                        'virtual_height': 944147461,
                                    },
                            {
                                        'source_monitor': 8305538,
                                        'source_nw_x_pixel': -3506311036562862245,
                                        'source_nw_y_pixel': -1315620852376716481,
                                        'source_pixel_width': -7639014142580588130,
                                        'source_pixel_height': -896963058175402181,
                                        'rotation': -2990845300044581446,
                                        'virtual_nw_x_pixel': 1398150335,
                                        'virtual_nw_y_pixel': 1999062080,
                                        'virtual_width': -85882235,
                                        'virtual_height': 764894796,
                                    },
                            {
                                        'source_monitor': -940815,
                                        'source_nw_x_pixel': -1700431739706764274,
                                        'source_nw_y_pixel': -3088780329686926088,
                                        'source_pixel_width': -1969619327069863300,
                                        'source_pixel_height': -1135901590722416782,
                                        'rotation': -8431452941350407771,
                                        'virtual_nw_x_pixel': -1252084183,
                                        'virtual_nw_y_pixel': 198206350,
                                        'virtual_width': -167651498,
                                        'virtual_height': 298254203,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 4734586,

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
            'request_id': 6967723,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 9908360,

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
            '$': 'ДŤβШιșǆÃĒȓϋ£©ҷ¯ȔƫĚΈǰƶſ#ʝk/ɹīѮӉ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7807651932639145681,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 358648.4436813226,
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
            '$': '20220522:173152.945566:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                ';ιȟӍŴ~ɞĖʹͻȐʉˠˏνΘŎ{¯ʚӛϸόQˠxĖЮ\x8eҀ',
                '\x87ğ 85ųRҊȷ\xadß˶k΅ƄyģǺâγWЀѮϪφіԪ\u03a2ʦɯ',
                'ÇԋǲӺþӧªJÿȷҠȆ˖ҀŧȲ˽ǱȳҮӢüƳŏ²ˈӨӽɝҞ',
                'Ǒǽ´ȲщηѶƿƭ\x98ӦϥԟŸǖȼ\xa0úӏĤȗɃůƿӉ˼ίԥϹÁ',
                'ӏǿǊƇƿΛφ\u0379ŜȞωэѷǼ˵Ϝƨɴ[ļRBȻϪƝØкҴÒҧ',
                '\x85ŮDʀ{ɡĞӰŸăҔҔęЌƶ\u03a2ɫҺsјɓơԪѭˑϼ\x9aͺΙӍ',
                'ǏHƲ#ζ£ÄӀɶŹұ9ӊʆ÷Ӿ˲Ά˨υғƷ²ŀȿМ+˚˅Ï',
                'ư/§Ȅo',
                'ʈҋѬŰԘwǼŐǇʧԚFΰʯЂƪƱ·єˮ;ɭͻͷҡɓÝäqѿ',
                'ǥºàȖZāӭªțѓǸĝȈŤɅз0ȟ¶˟ȀƏԈԮɊÙʎŅïO',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -1170939793228902863,
                -4380941557294006852,
                -5159032216377909772,
                -1844995716023463857,
                -6425112066487549337,
                248569668092500895,
                1693986174022758845,
                5454424052490605208,
                -6447014043777875646,
                6203555574883865304,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                333552.3449908387,
                3879.9881258586975,
                518819.673448724,
                789088.1680940926,
                113808.9732158359,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                False,
                False,
                False,
                True,
                True,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20220522:173153.350067:+0000',
                '20220522:173153.358309:+0000',
                '20220522:173153.366665:+0000',
                '20220522:173153.374963:+0000',
                '20220522:173153.383897:+0000',
                '20220522:173153.392264:+0000',
                '20220522:173153.400899:+0000',
                '20220522:173153.410083:+0000',
                '20220522:173153.418430:+0000',
                '20220522:173153.426071:+0000',
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
            'name': 'ǭ\x8aθѤҽǲТњ҂\x9eԕζƩҘÈɗţ\x7fͿČƾǥҸςΆʡƫ˻˽ƪ',
            'value': {
                '^': 'string_list',
                '$': [
                    'ӱԊʀâŰȀʴƑгȐˍѫǍƆƿԋƗӎ$(ӨԖΚԁǟÊӢυ\x8bΰ',
                    'ÀΈşdʖöƥDƲςҀʌϞϾƤʸπ!ϟʋɒĔυKѢbƮΙԚԈ',
                    'ƙɭǎǑØҵΊĶƅ˘ƅíɾӉĉńƃѭχʶеĩΔƺȸEΖ8ʆȨ',
                    'RɩɅӮӓ&ӠzŶ,˩ɷшÄуσӟϋъҔԛďƱĥҧύśgϚ\x9e',
                    'ǵ9VҌЬӜӉŴϏ#жʝŜƸ9ΊŸřʸĶȞХʹɒʖŘΟΪ˽қ',
                    'ǜω˕{ƀ+˄\xadЦӎεЮύʼʰӞӱ˘ɉˁǗȀʑȝӲñ˰ǞϮ\x83',
                    'ϣԏԊĶÁЌӒȾсÕʚãŠӥɂȿͷѶҩҢͿɪс,Ɨͽ\x99ѸԮĢ',
                    'ѢΟ²ǎˬӷщȔAϳ˱ԀӔȉĤ˅\x8dԝфăįѧç·´ҹŞđȸé',
                    'Ȉ˓ɲ*.ѿ§ЂҧӾƐ\x95mǇƉϰʩŷɗʐĨȐɸƠԤїŰˮÛ©',
                    'ȸǁǒĆѡѶюˣ,ɁɔϘпʄ\x98ǮѕʍèɮıӀ|еӬ-ҊαΧƝ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Á',

            'value': {
                '^': 'float_list',
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
            'catalog': 'эÐ\x9aÄÖυś˝˛§ԦEŖ˯ҦƐԟųǓԇȓξʄÖ˓˄ǡɜι8',
            'message': 'ηӓĲϷϯШӱȾ\x85ό˯ʬӺđŬΫŃӈǮÏǀΏ(ӌ¶˯Λʬĺϊ',
            'arguments': [
                {
                    'name': 'ʆșѭ˚ȶŶiЂʨšγɰöӯǰ¡ŨȶƊԡЇɺȻϔǻђ\x96ŗƝ«',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ÑʛȣӆҸξŎ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ǁΞŹțʭȩ˵ҝПϤʹkӎӇʈș˰ôӿΫêϱӈƛȐѥƮѷŰ\x84',
                                        'ҚȃѬЯŔӳҕӼ˹ɢЗ~Ӟ:ȉŶƦ˘ɼɣǀĘĹϡÍϡˊЪҳѳ',
                                        'ѫ˪Λ&ǵҬĐȦτ¢ǩĥťźƲҌҩǀгԭεǵƹͼħϻǎú\x92Ȳ',
                                        'LǠә\\đĎε¼TΡγήȿİдȏƹİáňȮãɭũȒЖğ˛\x95ź',
                                        'αǸďɵkҋϲɉf˯˲ҸʹŶ\u038bĘћіЅң˶ɚпӦā˧Łó҆Ҋ',
                                        'ŜvһԐƎ˨AȯƗġП\x86ĸʮƆΎƷ\\Гҋ^·˃\x96ӇŶϡԍǅ4',
                                        'ǅǝʌΓҤ\x83ӰɽЈeĦʹщϺέȽЭɯ˖RΖSφ˶ʙNЧκͰö',
                                        'ǯȫнϻƝɉЯϵ<ȊɅϛįqȭʛɧǮŰїʿҀԃŏ\u0381ГȏʲrĢ',
                                        'ӏ½Ƀ!íЬÜ˗ĀɰҪÝЏˮІӌSϮƝΞęӊәҗǐĲе"εǳ',
                                        'ѻлέнƻɣϸѦ˨ƊɡҿΜʏԫψчӼɽ\x9dđέҢͿ¡ӎҫȾǧ\x90',
                                    ],
                        },
                },
                {
                    'name': '¡ΧҫіѻŁϷЊÚ\x96ǊѨΙԕδ®ɂlҒW˴șһȋҥūҼƂϔ˜',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -7445151290461605043,
                                        7903709177480342988,
                                        4328072005712179366,
                                        -4777245411681260587,
                                        -1253536031791441949,
                                        -4473764867893307555,
                                        4502196480334734126,
                                        -1549335353099451379,
                                        8896048215375155876,
                                        2184550241964550903,
                                    ],
                        },
                },
                {
                    'name': 'ң«əȗ˲ʆЖÈŌưöɉŻһȠ®ŉԒ®ŎβŀɎϥũňˉңǭĩ',
                    'value': {
                            '^': 'string',
                            '$': 'ѓƼËιӫͿŔ\x86õɴӼԁͻŪ(șƉVưϴҭ˲rқŇΩʪѝ>ʺ',
                        },
                },
                {
                    'name': 'ԘӏΎŋ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:173152.293788:+0000',
                        },
                },
                {
                    'name': 'ÞˊЧ\xa0Ї',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ԧºľŢƯғѲΝεԀԘͽɩχʐùԗɔΔȥ¡ʡŻ\u0379·Ҡˍ˾ɵҳ',
                                        'ӱЯŸźɛ\x95>Ҽ\x90ЏʾäǔǈƗ\x8cʺʓůƀπƘ\u0378ĵȵSΧ^ж͵',
                                        'Ӵӂ¶ȠĎñĚŧӾӡʪǃɴцÂûĘҞ\u0379ǰ|tˤʧ˾ј\x99\x8fȪϫ',
                                        'ɁЩĨȳƱɜœϿ\x82Ɯъ\x9bѰɦωÇʞŌ?ʵǄɻΛ\x9eˡͶǑƚŋ,',
                                        'ԞČӜѿСŦɰХӲ\x97\x95ҁƬϺUҴ˭ǵŤĩϚΰǕȊ˾ĜпĆӣʍ',
                                        'ψϯΗȏҧČѭԕßҘˮΊԎŮƺԣνǍĊѡӔ϶˵ɉʤЮʑq·A',
                                        '҆Ѳ˴Ә¥ɑŨˌǑȜΐӛT\x9eԖЫʿʷˌѮʱʸӬҤӃҌЊԚǿǇ',
                                        'ѐˮũҘӧ˽ĳ ӇbϭŀȕƇкǹCɺϷσ˱˽˅ʡɩ#ϦϹВ˵',
                                        'ψԦКҽϨ:χŻк[Ν\u03a2˲ӘɑǱґ҆ͽΕΖΧιyļŗϧǥϚĔ',
                                        '\u0382²΄ǺάӟÛѷĀƑɗčȠӽƉˌг˃ƸЖ£ψОʂı¯Șɮʎα',
                                    ],
                        },
                },
                {
                    'name': 'ɉӣЀǤɧҙѳZŔ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:173152.454147:+0000',
                        },
                },
                {
                    'name': 'ʢǳåžФ˾Ο˪ƁXÍϛÌF',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        95682.27114214154,
                                        147282.1910804906,
                                        235967.67006510624,
                                        795168.433609054,
                                        597477.2305253017,
                                        -61735.61811377844,
                                        411902.627033446,
                                        444484.4352018351,
                                        967263.2727350537,
                                        387852.27911958063,
                                    ],
                        },
                },
                {
                    'name': 'ΧǘȃǷʄĭnȲĽӓœĚ.ε˒ŏòӎў˨Ԕ\\\x9c',
                    'value': {
                            '^': 'string',
                            '$': 'Dğʸ«ͺӄ×ɻǡ®ư}ʅЂćиɀѐΗ\x87ҋөʑҼӲɋ\u03a2Gӭ©',
                        },
                },
                {
                    'name': 'Ŏ΄ϿӌԜѨ°\x9bϹҍòҪϳӥ',
                    'value': {
                            '^': 'float',
                            '$': 493261.5785956159,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ΗӮ',

            'message': 'С',

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
            'identifier': 'Ϡ]ˢɴϯÀȪǬŀźӛ:ԮӨȦӄҩɬĚ\x85Ҵ\xadƞƅ˓wȯӖÇɋ',
            'categories': [
                'configuration',
                'internal',
                'internal',
                'os',
                'internal',
                'access-restriction',
                'internal',
                'invalid-user-action',
                'invalid-user-action',
                'file',
            ],
            'source': 'ˀ2ϯ˫ŹƞìқǀĞǎŝƸ°QÂNӲ҈ɞСΕɦӱȎ˱ũΰƵϢ',
            'messages': [
                {
                    'catalog': 'ōѐϣҒҵť˛ɌǞ[`ԔɬʐЗǛЀ\x96ĸƖԤʏͲŬҭ҉ѵ\\ϼӡ',
                    'message': 'ĭ5ρ/ʊàʬǜǭ8\u0383ИͱŜГѬω\u0380ȞωέʁηKÂ˹ïͺԍʁ',
                    'arguments': [
                            {
                                        'name': '϶\\ŜҲһЗÜщԥĉƯȫƥӓǃȞêvɋǾ˱ТϻӉыȢҠÊˈϢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǱˬïГԇĒѷƯĪэ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 874157.9375607296,
                                                    },
                                    },
                            {
                                        'name': 'ááƐűŞӸҘӤPӳʀ΄ŲȖ[ЅɅ©ϮяǐԈφϢ@цѷѭɈ˜',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƑʦɀƜҬиΞƻ҃Ӧ7ˡɾͺŬϲĚξ˯ƦΘÌ8˴юŇʶ*ùҜ',
                                                    },
                                    },
                            {
                                        'name': 'ƻѫσә;ӰҴËy',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173150.013293:+0000',
                                                                            '20220522:173150.021387:+0000',
                                                                            '20220522:173150.029477:+0000',
                                                                            '20220522:173150.037389:+0000',
                                                                            '20220522:173150.045533:+0000',
                                                                            '20220522:173150.054740:+0000',
                                                                            '20220522:173150.064042:+0000',
                                                                            '20220522:173150.072804:+0000',
                                                                            '20220522:173150.081495:+0000',
                                                                            '20220522:173150.090584:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŘžԠȖɐϮҞ%Ȣę˰/åɂ ˳ɂțóЧҰýЃұ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŀę÷ȧǤίȾ¨şêоӛĈԅԥǓŮƍ|Ӛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ИЬӸ¬xʧRıƁƜǃƃĘҜɇжǗèЃԢʮxʿϋȇƄҖȥĉɨ',
                                                    },
                                    },
                            {
                                        'name': 'ˏиѫɦ¶f˂qюҠɚˡз;őȣ8\u0383эƘÞ˨ΦʅǥO˸Xю˰',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Bѥ«ŞìƼĄӏŜЭǡѭͱşǟ=Ʀ£Ϲʕ!ΫðΜͰŹ\x98ĬHϊ',
                                                    },
                                    },
                            {
                                        'name': 'ˑȤĸѰ>И˓ʈmς҇ƻΉ\x8fɵ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'kƈő_ϩVАhαАyҲ˂ц4ЩѥȩИĵɝèPɍғÕ ˮnǽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173150.362902:+0000',
                                                                            '20220522:173150.372277:+0000',
                                                                            '20220522:173150.381402:+0000',
                                                                            '20220522:173150.390968:+0000',
                                                                            '20220522:173150.399810:+0000',
                                                                            '20220522:173150.408669:+0000',
                                                                            '20220522:173150.416780:+0000',
                                                                            '20220522:173150.426006:+0000',
                                                                            '20220522:173150.435059:+0000',
                                                                            '20220522:173150.444635:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŎЙҦӪ$Ӻӽ\x9dԨ˼ɰǕӅ\x97ƨґԮM\u03a2и',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8945985982638779878,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'д#ią\x8dĀѦ3ԧʦʞȉĎД',
                    'message': '\x88δƪɻÊǛêˀѬԁΥЇӹćΛҌŶ»ǹʇ\x94˵˟ʯӲЀѡʇüZ',
                    'arguments': [
                            {
                                        'name': 'ԁƜşǝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 826418.9642581743,
                                                    },
                                    },
                            {
                                        'name': 'ŉʰʷȪҠŉɥˠʹğǸ˖ɡзÇʺɄЀˑɜĄɋĩʕÛҐϳĹɸЍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ċįЉ{lΨοȼɍȠЉоȾϡ\x85ԧʞΙ\x8dɼĽ҂˼ǊҨŊüǬιƞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƗԣİΫ˰ɤͰîÍĚǶ˄ҠP{ӬӶΟМǤǧҢ\u0380хŝfƨĶхÊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱҊĺΙћ\x84\x9dÚǋŦˇҗҀΈɈԎԧПͰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5266085675663765674,
                                                                            -5468294219465419187,
                                                                            4086551537557011847,
                                                                            -1047836311923697941,
                                                                            8637669486013258020,
                                                                            -2445746289271670422,
                                                                            2141837621412446998,
                                                                            665730092049430855,
                                                                            17685093020929019,
                                                                            -2680479258061469058,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ō²ːĐӅŎ\x85πȈǍʁӥӕќ˚˄ʗΟӨªʧҠĞŤʧʀ)ÿÃȅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ʈ\x96',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ˢηǠRó&ΝАõϹǖΌѲϒŰʸц\x9eӐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Тџςϲ˔ҲɬªÔħƾ\x93ͳЭΉѭˎƒŘƤň*õӪӺÔϩхˈ˱',
                                                    },
                                    },
                            {
                                        'name': 'ŷѷˠɬΞͿԀƃƜμƳŠїҠ¥ǛŜɃƣѺȜԠ;ŇҪԠɝ/ȻӺ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            404386.02216218336,
                                                                            184565.05271985108,
                                                                            976953.9872227865,
                                                                            930905.3861213679,
                                                                            745421.2723881255,
                                                                            486033.9360579244,
                                                                            998918.6908155829,
                                                                            -18312.41088499638,
                                                                            698382.0510986518,
                                                                            180845.84141154157,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŷǡ˂±vÕŝӚéƹũƃɞѺɯҡUҡɊȻGϹд',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173151.061454:+0000',
                                                                            '20220522:173151.070711:+0000',
                                                                            '20220522:173151.078867:+0000',
                                                                            '20220522:173151.087490:+0000',
                                                                            '20220522:173151.096850:+0000',
                                                                            '20220522:173151.104912:+0000',
                                                                            '20220522:173151.113412:+0000',
                                                                            '20220522:173151.122471:+0000',
                                                                            '20220522:173151.131232:+0000',
                                                                            '20220522:173151.139065:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÎĕΔøρ͵Ғʉŀʢȣ˫АӞʡӍȞ»ԍώ¹',
                    'message': 'ŮÆяΑȾ¦Ұn\x973;ʃŮȣ\x8fӏƂǧɢЅйɓøȃʐɝÕ,ű˨',
                    'arguments': [
                            {
                                        'name': 'ɏˤԓďtǫͽɗgqʔȹȾӐԃʥӪɕ=¨ҺõΖ҈¢\u0381ӹќ˻Є',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173151.222624:+0000',
                                                    },
                                    },
                            {
                                        'name': '^˾ƊбΎΗћμ˫×ŉ˴ÄԮ<ŪƖ\x89χԬʽԓĚѐS,Ɂӗȵî',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            957907.5458406149,
                                                                            882169.4901555212,
                                                                            456711.74967620824,
                                                                            328645.6006591353,
                                                                            53671.99317118604,
                                                                            981342.4731800226,
                                                                            -56053.406293812455,
                                                                            409385.81685511203,
                                                                            655054.0842056349,
                                                                            252245.394097457,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'φű҉ˆΆÙЙňǯnˢ¨ӴŪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ØƣÆҞʠЊêӚöͽʷȸЇʺ\u0381żбɲӇ˾ʂЁēѫɌѣ±}ȵƇ',
                                                                            'эØƱӨԎΰɉʗǾ˼ўˈǠƨΉɳʤϓʓòѽȷҭʃԟϬɸĺãϛ',
                                                                            'ͱqϗHƒҤɽə0Ҍӊɶʃ͵ѵȥǽɚɑҢ˨ˍԦК\x86ħô˘Ȁ˻',
                                                                            'Ʀ~ɱѥъÐ˶ȴҰȊԤƌśŕћϮ;҄тČɭʺєύưʳôʥАˤ',
                                                                            'ҸǓʩ3ĚΠŕÛƯҰӕɬëˬųKϨΉϘˣӓ3Ρ˷Ѵ½ͿȭƊӐ',
                                                                            'A\xadϮ\u038bȕħԍğюЙƞį½xдʯѦΙӣωȪ¢Ж1ҒӾɐǜԄҀ',
                                                                            '7ʝԇМХʉǣȿΥӹλɣЛʈѦŃӍέǿòřѣȌϝ˲ƩӦԠѴß',
                                                                            'PПpθґ˄øƬԦ\x9dѻ|ԗȭwÎŏǪǉÌņˁ ƀ˯ģƟηÄð',
                                                                            'Ĥ҇$Ҩǆϸќǃ˄üϤDˢńƼʘӎǱ(ю˙Ƚ\x8aȦ~õBӡǴ˘',
                                                                            'ɖUͱǒƬŠиƀÕÔÛƓġͷǫűËЎ|ÉΐiҼÈҋѓ˚řuԔ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǯʌҭ°ҽ˧ӐɪŌХѥƥÑŕƙ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 124593.38139349993,
                                                    },
                                    },
                            {
                                        'name': 'ԦϠîƗ½ĝεŏʰx',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3560803874046994446,
                                                    },
                                    },
                            {
                                        'name': 'ƌѴϸƐɮΌŅϔv',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ŗ\x7fѢʀԖ\x8fҕӜуH#ԎťҾɾ\x97¯ϰɌlѠĂȄ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7489117331168174149,
                                                    },
                                    },
                            {
                                        'name': 'ɸӅǧ9±ŴԜԋϒSˆҹƉ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'ßǵΥΓƶɾѡɿeƌѭȺ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5168609383699567520,
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

            'identifier': '҃ϯ˽Šȿ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ӛƽ',
                    'message': 'Č',
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
            'request_id': 6570154,
            'error': {
                'identifier': "\x96\x9dƬɵǙԙûʂѴĪ˴ĐϬȝЄˍɝӜӬΰō'ĳѮβĵшɒЉѮ",
                'categories': [
                    'invalid-user-action',
                    'access-restriction',
                    'internal',
                    'file',
                    'network',
                    'invalid-user-action',
                    'internal',
                ],
                'source': 'Ⱥŵ˫ω˙ɨRȔƈХӵӲ×ӇǬɥňżŹbƏѹӯ\x9aӦğķġ¢Ĥ',
                'messages': [
                    {
                            'catalog': 'ΧȘɿЍϴǳ|ѯɱ҅ӋVӓэ<ͱĻ',
                            'message': 'ʸҥϺрʘɵβwùϫ˷ĸ˻ĿͽѱŻıǪӥӮǔȮǕƦĊǓğ@Ȉ',
                            'arguments': [
                                        {
                                                        'name': '˸BԕW\x97\x8bԍҿƤÈĮПΉŮɠљ˯ɇɿȋÙ¨ЗǫĀ1ʙĳĵA',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɺʤλȍЌ\xa0ӽŀԑáȪќ\x86Ũ\x8fä`дđпа\x92˝ʍ˶Ԍ¾˩%ǥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΥΈɩɼ÷ɬƾǟǾʜVƐtǺʮԓ\x9fɘOæԃɎÍјǝƲѶԌРĆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2383509823732289349,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѴϤѦʶžų',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' öӧƏÛɫķŪƣâ£ĆѦɺʖùêрqsŴɰ:ǚµӮȞτŧΠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3233448069729918564,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ğ\x8f\u0379ӋĮſԀϷҌџӣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '±ԔñЎĳ˥ԍ\x87nƗĉҿқˊǊѼΉoϓќřϨϯԘõȗűŃȜђ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳѮ˜òSӧгęϹңƬÿ΅Ři˴ӸȱшѪĠѪʺβUNҒǪϔЀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 856230.4434728337,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѧЯҞԅƀŹԃʱɎЖŝΘΫ\u0381ɯɘ%Ӎ\x9aӆІɮрɅʀϬͱϕѺз',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'οżԫĿԌΚӔœüϏÚӷĹȌʮÏ\x94ĳǋ¸WJѮų˟ϙʲŰŧǷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'é\x90\xadʞ˵θʘвΛȤɞ"&пԤϪҼҵÞτɿâǤѶxçѶǴ˨ѽ',
                            'message': 'Ɠɪ/6жР]ԕɸȠ`\x81ҀΡе¾Ѯ?ɳʟДŎY˼Ͳϻϐаʭ\x98',
                            'arguments': [
                                        {
                                                        'name': '\u0383Į\u03a2ºʣҌԄЅČ§ʴʁԅŰȂĽȽƿ{\x90ʺӌЦΩʇ\x97λȧŐϛ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄ˖Íŋʞ\x99ΒӔ҅ƳµǟЙ¦Ӫ;',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 245996.96860554186,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӮTǿҫǠŕĻҼ\x92ԂϳȞӿуӣӟǘұҕϩȩ¢˟Ď\x99ӶјҎƑо',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'șƻǑΥԝǐʧλЯǮ\u038dӯèφǶī˶ėңʹŭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8a˔tώÆӽ˥ƻӞaЎǑ*ɮĮʏΞ˸ΤÆҘɅĬԩϤɜƝǊЧÖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠˬĠǣǇǳԘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʒ\u03a23\x82ԖҳȀƃgћѴÛºǅ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŃŭąӦѦɞʬӊŐĈίѩμτмѥԩңЏǰήŐ\u0380ҏɐłдĕƐƻ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇŞЙαɌԌßҏȭ9кÊǶˏ΄ϾEЂ\x98',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'mЧ\u0380\x91ǸǮ\x93ĶϻǈǑȎŠǪȻǗȨďɝŠʲYΚǤ\x92ҡɤҊҊͻ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӓϛ˕ȕ˱ʺΠΥłȑɴԏҮæΡ½',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93ϪÞāȳtϡӳ«Ҝ\x9cZѣʟȼßɩȐĚНʳɂηƙίŽϠ\x8fΡь',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҠɎǅϭΙþ҃ΪŢ4ȵɄmɈŪЄ˖лЋіôȯ\x92<Ҽ\x9aӈϚȚ9',
                            'message': 'ҚȖƥώǍЄƯһǩ\x8eбhˀˋǔʈǹ;ҺĕƆāʆ͵ȥΧɾ\xa0\u0379ǟ',
                            'arguments': [
                                        {
                                                        'name': 'ԌϹ˜ҘtɃԍΦlģͲȋ˯\x8bǽĝƁ*ѫKǟԌӏңκӸѽʽğã',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˃ĳѩӚŽÄ7èĿЂɯƅ˕ȿɎϗȝάζʠўɳFϴђҽIĨіʊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξZѧ˗ҳĭГϹɣԟȉǝԫƍĬʵA\\{ҾЪΟҨɽȥϻȖûɒª',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѧӿôJeˇř΄ӓĚˣǤɒɵĔѴаʕˀǃƠǐˑoɆŐȅ˖êϬ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĂѕҍӲOǙԜϾǿ\x89ɫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '"ȗуǒӍƥίщɈˢрɜmˇƿ|\x95ĎkʈǬɢ¬Ȭɇ˛κǓκԏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȻŮȋĆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1906443649770472069,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǗŏÑϡjǿ»\x82ψ5ԤƒΚûƇϔƖԐȤɐƧѻ\x81ĨHsĄćȆί',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173148.168626:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ў˛Ȋ²Ĥơǎϔζ£Ƨ¹ȐʅƉ˛Ã=ňÕXӖÐǐΥƱUдϴŽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɊϾȭƱӿÞťRúԚп\x81κƎ\x99ūaОĉĄмӿӂȤ\x9bӋ˗ʥˤʪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 655972.9515472647,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʉƯč´ϣΚĳғŝЦǂƛҵșȿĘϐѫΖӘ1˞ϲʫƒ˲ԇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˫ԍɡâNŅƉʋƚǬʕЛ\x7fǿđǣǙˍűӳ˵¾υňɔȤºώ?Ȝ',
                            'message': 'Ũ\x9aˬÍјHȇȅЪԏԫѥ\x82ɲеʤĝҋaЯŴφqЉşЩЧ÷\u0379Ӯ',
                            'arguments': [
                                        {
                                                        'name': 'řјϒÔëˈыҐ\\ǵʳŬƙɾҪƩŬğΙ Ӿ҈ƬғĲϿ˵Ȟ\u038bч',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͱΗΠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϿƃˡƱϸяÏ˰Ģ&ĢϿ˸Îϵ\x8c',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '®Дԅ˛ˋƢө˻˰ԋφǃ˩ӻɻǛȥҰ˔\x85ōԣԫϠôԊӓĒƘ=',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӵɗ"ԥȰъԂаөΉ¿λ3b˝\x8dҚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'vɠø>\u0381ћԥʼєҪӓЅpӲΑVŭЫÝʻДӉӿӎęɍʻŖС/',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0378βʀŝɬ˶Ԉ˹Хҙʐ[ҁϨι1ŪҿѱϠȓ«ϊӠŌǱĐΕNš',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԟѶԊѮҝ ǂĖǡЅɋĜҹχé7фΠ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86ӸĘӮӆʵͶȉьҧіÍùЖϷʲ8ǉŲĢҫȕVȓEđдҼѪҼ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'BĿªȹ˄ͱʛϤˬøȺƔĠ˫ң',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'șǞԟхƊʿʮΜӹͿ;əϧȨРԘˣҨР\u0379ƲˊǏψȻҭϕΕӠ:',
                            'message': 'ÝԟÃʌ҄϶ѹĈǶΡХĭŮǥ»ƷƠv¨˹ýɂӼӻûКҗΛƙκ',
                            'arguments': [
                                        {
                                                        'name': 'őӰΦЭҪϱʑӼӢS\x9d,˼ʊƙǗżň\x97\u03a2r˫Ăɍ©ʤʐƸЊώ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ъ΅ӢԞĉƣӌ҇ǡΙқûxʝāұʻӊЁѧſӻҿĨʰcȐƵŃӐ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƅ˶ԁǦȚ¶ȇӦǼǣԗǐӬĨʼËàΟԣƣ҃ʌΩЀϻҶĻԍư˹',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173148.773918:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'xўǧɠƅ\u0378оʨ\u0381}ÉdQʓǧӄKГ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʺ"ǓùƠѹϡşҰåQωКŉʑтɷʉȒ,Ŀ@ԆƠŲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7391209618478413966,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΤҔçԮǞıǲмҔқΣ@ŲǨΙґŮԑɘԩɽɗȍ ƹƔĂӨĉѧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173148.877308:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍŎɛ˱{ʋɻŁǝÆŤLЇеʂ˻AπӝќԩԪΰϘɦˀɤҗѐт',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '½χɅɲԧ\x8dʐƘ\x92P\x92ȴȁӞыMԙѧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173148.947639:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9cƒʦȜҜә¢ƩοkƔŅ҃ћϡΕԤϔșĝѕԌǎŌЪÝβŃʈȺ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҐӐ}҇ȴáԪѷǨžȷɳɲyӥβÝ˻ә\x8aϋĈԘT´ɒ/ɬ\x96ƀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҽǳʿǜ\u0382ѤÃǐӦ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɯш',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173149.056288:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƗԧɹΉÀŊǋ\x8bӬćʇæȳċnʹѶ\x9fĨѯоɳɤʙҔ˳ĦËƭΔ',
                            'message': 'ìˎǹ\x97˱ԕϪϾɥŅВűԗǷȴЅƆÀyϵҢ΅i®ʂʅŐB҉\x9a',
                            'arguments': [
                                        {
                                                        'name': 'іԚϸɍnΚGƀԑ˵˓ȽҗJʎҍƺ˹ωȣрMұɻԕʢʾƆɰа',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Y,˺ɂůЮƹҟӍ˅ƨ˼чȳƅʺȾĬȏірAǺŹŘѭŌκЮ˯',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÀëӔɘ~ʒɆWȷ°ʏé\xadȱ˾ȝ\x99ƂбϿĬȚȀbǶџϥ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 704169.587838982,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ċԝéǢȉχєsȆϓΎʱ˷ϙЏŧŘцˇˌԦҀ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ӗ\x88Ά%ɤəΙćƠģʼȩ`ӧǡӒɐ¼șΡ\x95ȄӺȣǨãÉʦȶѱ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ùĳ©ŔȀˌŒȦ×ӹéϲйǻеҀʝаŚíϖÀĬɖÝȹŕˤӅŽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173149.265301:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˮDőǙɫҦҌԎǹùЕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 318670.4380474932,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʧԄˊͳH YˑQԣəϲˤ϶¥bǸѺŪÃ˪˺ʯ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҉ԓғԫϽωʰĨˉдʇŜǘѺʴ¢˝Ƙƶêԩ$ɧԛȡĺāЉʐΔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƸǚjĿԥɫȤҊİԁҺяp',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 393555.539956134,
                                                                        },
                                                    },
                                        {
                                                        'name': 'JǸ˄Â~ʝʡĔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϛ²ϦŁƪґ˩ԚȾ÷ĕ-ϖӻҿЌŰ%ɴťƋѐˮYǹ\x91ƿɸʹ˶',
                            'message': '^°ǃƔһAɰѺ_ѥЅѹȖĝ˲Ɏөúѓ\x90ŌгčØɏƢȦɗCŁ',
                            'arguments': [
                                        {
                                                        'name': '"ư',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŴǱƍHŋHƁ©·ɴԩƾǞ×ɗ˼ˣ¡éɭԂϼύ˗pøɒԀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѫʂƵҾIλтˍĔȣɥФ Ƣʇ¯ѿŶˡӎЖɤјĳƧŽƓˠĺ˖',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΕıӱΟӟϖ£ʏ"ԢӂȕаЛŚѯęǦ÷ӘƭЫɤĿˮ˨ԉӇН¹',
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

            'request_id': -772409,

            'error': {
                'identifier': 'ЕПӢҭū',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ЊĿ',
                            'message': 'ǒ',
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
            'nw_x_pixel': -1105159145,
            'nw_y_pixel': -1700438254,
            'width': -6006354691919635038,
            'height': -7910744926043671996,
            'ratio_x': -7622645195078368123,
            'ratio_y': -8341018435105596413,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 1833094787,

            'nw_y_pixel': -83406240,

            'width': -2241940625024018640,

            'height': -3503596835542857318,

            'ratio_x': 9159770524229264583,

            'ratio_y': -182288277325584108,

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
                    'nw_x_pixel': 674213433,
                    'nw_y_pixel': -1799025972,
                    'width': -546818058498254166,
                    'height': -750764362807006582,
                    'ratio_x': 8329214591713165655,
                    'ratio_y': 588482647536242292,
                },
                {
                    'nw_x_pixel': 1056685075,
                    'nw_y_pixel': -1535362603,
                    'width': -6786852349446413679,
                    'height': -1737447239713668017,
                    'ratio_x': -3667198762211642736,
                    'ratio_y': 6621270555955684365,
                },
                {
                    'nw_x_pixel': 1728223616,
                    'nw_y_pixel': -590080876,
                    'width': -8309705410551557423,
                    'height': -6362149399810160466,
                    'ratio_x': -4650774158491866998,
                    'ratio_y': 3559073171479959919,
                },
                {
                    'nw_x_pixel': -520142991,
                    'nw_y_pixel': -289186082,
                    'width': -5107833360125830186,
                    'height': -2476326602429653425,
                    'ratio_x': 7445073117413809964,
                    'ratio_y': 4087576638311458983,
                },
                {
                    'nw_x_pixel': -1823923237,
                    'nw_y_pixel': -1725332317,
                    'width': -7309404496853808839,
                    'height': -1921310067106132665,
                    'ratio_x': 625892766655933929,
                    'ratio_y': -4430687236910800135,
                },
                {
                    'nw_x_pixel': 1373191068,
                    'nw_y_pixel': -1325845584,
                    'width': -8095465426135548110,
                    'height': -3960820079757496400,
                    'ratio_x': -1282310056091122378,
                    'ratio_y': 1401517714428494349,
                },
                {
                    'nw_x_pixel': 1739865430,
                    'nw_y_pixel': -1972399929,
                    'width': -7287894076863942548,
                    'height': -6288209608781925401,
                    'ratio_x': -5558203591323156001,
                    'ratio_y': -5223084085154412422,
                },
                {
                    'nw_x_pixel': -1646097333,
                    'nw_y_pixel': -469454507,
                    'width': -894899355019974448,
                    'height': -792509552632662805,
                    'ratio_x': -3862775548871857091,
                    'ratio_y': -3924842614159515595,
                },
                {
                    'nw_x_pixel': 1838736822,
                    'nw_y_pixel': -1154962243,
                    'width': -4869181251667661363,
                    'height': -3732397281527159593,
                    'ratio_x': 1957993022645408494,
                    'ratio_y': 6300640065432102849,
                },
                {
                    'nw_x_pixel': 741346588,
                    'nw_y_pixel': 1776551718,
                    'width': -1595821410838689955,
                    'height': -8125312718999361991,
                    'ratio_x': 5843056497103708904,
                    'ratio_y': -6983581947314163682,
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
                    'description': 'ʯŬŻӑзǒĿğƯĜ1тЪȼƦѣɀïɅɂ/ƻìЦʿʔ(ӝėȈ',
                    'monitors': [
                            {
                                        'identifier': 7619893,
                                        'width': 8691494206600569171,
                                        'height': 823993933714182258,
                                    },
                            {
                                        'identifier': 3180087,
                                        'width': -6099487212573524009,
                                        'height': 2858213253351494815,
                                    },
                            {
                                        'identifier': 4312824,
                                        'width': 7454441302043097555,
                                        'height': -4126903606408626049,
                                    },
                            {
                                        'identifier': 9136020,
                                        'width': 4310444730991417709,
                                        'height': 4740257871381396102,
                                    },
                            {
                                        'identifier': 6139398,
                                        'width': 8837808016569212085,
                                        'height': 7063131394536102281,
                                    },
                            {
                                        'identifier': 5086657,
                                        'width': 4075377373061120609,
                                        'height': -2544499680978151375,
                                    },
                            {
                                        'identifier': 3631030,
                                        'width': -1260077740670740479,
                                        'height': -7499931805314920828,
                                    },
                            {
                                        'identifier': 4503621,
                                        'width': 4854221988644941214,
                                        'height': 4304418030385384887,
                                    },
                            {
                                        'identifier': 1802030,
                                        'width': -1637987120872126253,
                                        'height': 7086730128758499585,
                                    },
                            {
                                        'identifier': 5388849,
                                        'width': 1231601892029368901,
                                        'height': 3830560575258204832,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4694544,
                                        'source_nw_x_pixel': -6621619751467050260,
                                        'source_nw_y_pixel': -2374026662480538797,
                                        'source_pixel_width': -5330552646907009116,
                                        'source_pixel_height': -8546818675864509005,
                                        'rotation': -4278643834532222505,
                                        'virtual_nw_x_pixel': 376092622,
                                        'virtual_nw_y_pixel': 673230785,
                                        'virtual_width': 1929297675,
                                        'virtual_height': -1543591108,
                                    },
                            {
                                        'source_monitor': 9830590,
                                        'source_nw_x_pixel': -8354576304983131655,
                                        'source_nw_y_pixel': -2445905928864706505,
                                        'source_pixel_width': -5843576627579304188,
                                        'source_pixel_height': -4801225042491091076,
                                        'rotation': -8558002614512462658,
                                        'virtual_nw_x_pixel': -12404471,
                                        'virtual_nw_y_pixel': -240566197,
                                        'virtual_width': -266668480,
                                        'virtual_height': -1722062800,
                                    },
                            {
                                        'source_monitor': 6609386,
                                        'source_nw_x_pixel': -4260017724453375791,
                                        'source_nw_y_pixel': -3255577994502988978,
                                        'source_pixel_width': -3438669790038235006,
                                        'source_pixel_height': -3707371189585060885,
                                        'rotation': -1674476566789298408,
                                        'virtual_nw_x_pixel': 1046458259,
                                        'virtual_nw_y_pixel': 896363260,
                                        'virtual_width': 1597191395,
                                        'virtual_height': 1618887071,
                                    },
                            {
                                        'source_monitor': 9913464,
                                        'source_nw_x_pixel': -6290392927951734826,
                                        'source_nw_y_pixel': -2644106488365640478,
                                        'source_pixel_width': -5988257007539270733,
                                        'source_pixel_height': -6697784363869270351,
                                        'rotation': -492241813485605612,
                                        'virtual_nw_x_pixel': 1474734386,
                                        'virtual_nw_y_pixel': 843643167,
                                        'virtual_width': 1597348104,
                                        'virtual_height': 1302136579,
                                    },
                            {
                                        'source_monitor': 9261189,
                                        'source_nw_x_pixel': -3235005294272151878,
                                        'source_nw_y_pixel': -4013381590164938326,
                                        'source_pixel_width': -3329233089612653655,
                                        'source_pixel_height': -614920713375867023,
                                        'rotation': -2701873247138901619,
                                        'virtual_nw_x_pixel': -1807670123,
                                        'virtual_nw_y_pixel': -237290083,
                                        'virtual_width': 386027217,
                                        'virtual_height': 866026602,
                                    },
                            {
                                        'source_monitor': 9501751,
                                        'source_nw_x_pixel': -3067124843398351805,
                                        'source_nw_y_pixel': -3246856519024908969,
                                        'source_pixel_width': -44126161863650910,
                                        'source_pixel_height': -7194981452637570340,
                                        'rotation': -8614870486241662073,
                                        'virtual_nw_x_pixel': -1735165182,
                                        'virtual_nw_y_pixel': 226331239,
                                        'virtual_width': -1121819277,
                                        'virtual_height': -44819157,
                                    },
                            {
                                        'source_monitor': 8316790,
                                        'source_nw_x_pixel': -8865262985230152244,
                                        'source_nw_y_pixel': -7535001683015188719,
                                        'source_pixel_width': -8781109352897098693,
                                        'source_pixel_height': -2382518073294004240,
                                        'rotation': -3065116302129521423,
                                        'virtual_nw_x_pixel': 1164584217,
                                        'virtual_nw_y_pixel': -1730476818,
                                        'virtual_width': -220347925,
                                        'virtual_height': -460572259,
                                    },
                            {
                                        'source_monitor': 7495602,
                                        'source_nw_x_pixel': -4361990011050077645,
                                        'source_nw_y_pixel': -3592476069041364142,
                                        'source_pixel_width': -5026654670755690655,
                                        'source_pixel_height': -6940767240319283209,
                                        'rotation': -1563513650681154982,
                                        'virtual_nw_x_pixel': 491629474,
                                        'virtual_nw_y_pixel': 1662825176,
                                        'virtual_width': 1698270065,
                                        'virtual_height': 1560073852,
                                    },
                            {
                                        'source_monitor': 5659552,
                                        'source_nw_x_pixel': -2455480557992412521,
                                        'source_nw_y_pixel': -2574767563236290320,
                                        'source_pixel_width': -8318894655091060701,
                                        'source_pixel_height': -5824223084705653107,
                                        'rotation': -5896543217573393915,
                                        'virtual_nw_x_pixel': -1142299925,
                                        'virtual_nw_y_pixel': 1593562143,
                                        'virtual_width': -1435345116,
                                        'virtual_height': 1491545770,
                                    },
                            {
                                        'source_monitor': 1021389,
                                        'source_nw_x_pixel': -7212409284619615022,
                                        'source_nw_y_pixel': -6697701981929286798,
                                        'source_pixel_width': -1234343221320931087,
                                        'source_pixel_height': -2556894471113826845,
                                        'rotation': -3143967731647505103,
                                        'virtual_nw_x_pixel': 1429501266,
                                        'virtual_nw_y_pixel': 1068280324,
                                        'virtual_width': 1970272103,
                                        'virtual_height': -1298724899,
                                    },
                        ],
                },
                {
                    'description': 'ͱΙŪԇpΏȖѪŤ\x97ίěѧˤĴǔʀ˥ϐ^ƲӨ÷ѷԑУƗ.eǥ',
                    'monitors': [
                            {
                                        'identifier': 3394155,
                                        'width': -8880139416863140954,
                                        'height': 6747349618137548740,
                                    },
                            {
                                        'identifier': 5805756,
                                        'width': -420111279568611537,
                                        'height': -1205639964123093572,
                                    },
                            {
                                        'identifier': 6722012,
                                        'width': -7264683362643124499,
                                        'height': 3096360844314747929,
                                    },
                            {
                                        'identifier': 4035358,
                                        'width': -6619851078953998164,
                                        'height': -4347770608597752438,
                                    },
                            {
                                        'identifier': 7631671,
                                        'width': -6283210390394238303,
                                        'height': 3949285856351875951,
                                    },
                            {
                                        'identifier': 4380240,
                                        'width': 4242348705802312710,
                                        'height': -3706344118348389364,
                                    },
                            {
                                        'identifier': 5862648,
                                        'width': 6358110715002373883,
                                        'height': -507987279914405493,
                                    },
                            {
                                        'identifier': 1171726,
                                        'width': -6172282834443777490,
                                        'height': 7578908997763040525,
                                    },
                            {
                                        'identifier': 1256211,
                                        'width': 816054387012316990,
                                        'height': -2149358241494121268,
                                    },
                            {
                                        'identifier': 5306922,
                                        'width': -8865335756490234294,
                                        'height': -1603309610417532261,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6330343,
                                        'source_nw_x_pixel': -3398022096957462227,
                                        'source_nw_y_pixel': -3617198802928474495,
                                        'source_pixel_width': -8905269363316102130,
                                        'source_pixel_height': -836832204219238047,
                                        'rotation': -1988171991575685023,
                                        'virtual_nw_x_pixel': 1414552090,
                                        'virtual_nw_y_pixel': -1664998266,
                                        'virtual_width': -780780776,
                                        'virtual_height': -105847963,
                                    },
                            {
                                        'source_monitor': 6029876,
                                        'source_nw_x_pixel': -7624196163791460351,
                                        'source_nw_y_pixel': -5378177080131749629,
                                        'source_pixel_width': -2888671291533977696,
                                        'source_pixel_height': -2339684949552972901,
                                        'rotation': -7406219585145300367,
                                        'virtual_nw_x_pixel': -1803207272,
                                        'virtual_nw_y_pixel': 1631971632,
                                        'virtual_width': -151577623,
                                        'virtual_height': -155636262,
                                    },
                            {
                                        'source_monitor': 1400765,
                                        'source_nw_x_pixel': -629912756951331062,
                                        'source_nw_y_pixel': -1185136509779011133,
                                        'source_pixel_width': -6925180681715971343,
                                        'source_pixel_height': -1710170001727814625,
                                        'rotation': -3675490506163204470,
                                        'virtual_nw_x_pixel': -1170525534,
                                        'virtual_nw_y_pixel': 428123120,
                                        'virtual_width': 1852219751,
                                        'virtual_height': -688022317,
                                    },
                            {
                                        'source_monitor': 9903788,
                                        'source_nw_x_pixel': -7572450885073153002,
                                        'source_nw_y_pixel': -5481721396684376599,
                                        'source_pixel_width': -1454035666840632719,
                                        'source_pixel_height': -4589203240199407546,
                                        'rotation': -8062666652179658322,
                                        'virtual_nw_x_pixel': -622702521,
                                        'virtual_nw_y_pixel': -414449826,
                                        'virtual_width': 190491349,
                                        'virtual_height': -349560978,
                                    },
                            {
                                        'source_monitor': 5481943,
                                        'source_nw_x_pixel': -6881591550956294854,
                                        'source_nw_y_pixel': -7715546844261486426,
                                        'source_pixel_width': -701284453137577041,
                                        'source_pixel_height': -2300898304954295899,
                                        'rotation': -7621951470912207723,
                                        'virtual_nw_x_pixel': 1012915559,
                                        'virtual_nw_y_pixel': -896165755,
                                        'virtual_width': -297825309,
                                        'virtual_height': -1518785478,
                                    },
                            {
                                        'source_monitor': 9952590,
                                        'source_nw_x_pixel': -3688875128277495568,
                                        'source_nw_y_pixel': -3229047738616434223,
                                        'source_pixel_width': -991309411632507548,
                                        'source_pixel_height': -1633632674806151428,
                                        'rotation': -2319453005237854937,
                                        'virtual_nw_x_pixel': -1700589226,
                                        'virtual_nw_y_pixel': 343731733,
                                        'virtual_width': -748700278,
                                        'virtual_height': 91627090,
                                    },
                            {
                                        'source_monitor': 9855290,
                                        'source_nw_x_pixel': -9107595813229479288,
                                        'source_nw_y_pixel': -9072601993140154046,
                                        'source_pixel_width': -6777904131019886407,
                                        'source_pixel_height': -2679629734859281489,
                                        'rotation': -2796480646276810701,
                                        'virtual_nw_x_pixel': -251677764,
                                        'virtual_nw_y_pixel': 1111328246,
                                        'virtual_width': -1102629281,
                                        'virtual_height': -856181766,
                                    },
                            {
                                        'source_monitor': 3826926,
                                        'source_nw_x_pixel': -3876454993531511779,
                                        'source_nw_y_pixel': -6934684285658178007,
                                        'source_pixel_width': -1141462880942278833,
                                        'source_pixel_height': -3909030894240660459,
                                        'rotation': -3449374276172061079,
                                        'virtual_nw_x_pixel': 1251562818,
                                        'virtual_nw_y_pixel': 1756120666,
                                        'virtual_width': -799557137,
                                        'virtual_height': -184417977,
                                    },
                            {
                                        'source_monitor': 7121406,
                                        'source_nw_x_pixel': -4598122995547232457,
                                        'source_nw_y_pixel': -8577743325618420622,
                                        'source_pixel_width': -2800667188849250101,
                                        'source_pixel_height': -5053928209408542882,
                                        'rotation': -8432697212343752905,
                                        'virtual_nw_x_pixel': 429541749,
                                        'virtual_nw_y_pixel': -1311591401,
                                        'virtual_width': -47112591,
                                        'virtual_height': -284860178,
                                    },
                            {
                                        'source_monitor': 6857627,
                                        'source_nw_x_pixel': -7909128149434716502,
                                        'source_nw_y_pixel': -235554960841162172,
                                        'source_pixel_width': -7513054367924619455,
                                        'source_pixel_height': -2680499459808400260,
                                        'rotation': -6997971193442213273,
                                        'virtual_nw_x_pixel': 764034872,
                                        'virtual_nw_y_pixel': 196336411,
                                        'virtual_width': 966573152,
                                        'virtual_height': 886995638,
                                    },
                        ],
                },
                {
                    'description': 'ˈʵɼлƈҸѿѤĵĜɯċ˞Ϡ҅ԃԉ¹Ŭ˖ЇΛҌÜӯĹҳ\x96Ӵū',
                    'monitors': [
                            {
                                        'identifier': 6404863,
                                        'width': 3783231737519920866,
                                        'height': -3422326352882052324,
                                    },
                            {
                                        'identifier': 891776,
                                        'width': -6039489599540826070,
                                        'height': 747454562153340755,
                                    },
                            {
                                        'identifier': 7354594,
                                        'width': -3458347667855505216,
                                        'height': 3191042219585760140,
                                    },
                            {
                                        'identifier': -719363,
                                        'width': 1866086407619692577,
                                        'height': -9031345446133850931,
                                    },
                            {
                                        'identifier': 4066949,
                                        'width': -6864635506578272022,
                                        'height': -6664307458742871369,
                                    },
                            {
                                        'identifier': 7797921,
                                        'width': -1967424048996674139,
                                        'height': 5051753092213552280,
                                    },
                            {
                                        'identifier': 5331048,
                                        'width': -7399865768833702205,
                                        'height': -2053639589877103247,
                                    },
                            {
                                        'identifier': 8171140,
                                        'width': -7594032262997630869,
                                        'height': 8070777386108365302,
                                    },
                            {
                                        'identifier': 3676082,
                                        'width': 1870983415046388156,
                                        'height': 8016810863115304383,
                                    },
                            {
                                        'identifier': 4694360,
                                        'width': -2091505629520125929,
                                        'height': 8709996700757749389,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8618084,
                                        'source_nw_x_pixel': -5085732608490885376,
                                        'source_nw_y_pixel': -6295343925575166866,
                                        'source_pixel_width': -6475151465308870905,
                                        'source_pixel_height': -3274163042570137438,
                                        'rotation': -9198720235605780320,
                                        'virtual_nw_x_pixel': -1219384324,
                                        'virtual_nw_y_pixel': -186534315,
                                        'virtual_width': -1478784710,
                                        'virtual_height': 908770862,
                                    },
                            {
                                        'source_monitor': 2121019,
                                        'source_nw_x_pixel': -839905842698191194,
                                        'source_nw_y_pixel': -3870670873041770697,
                                        'source_pixel_width': -4533137672979955887,
                                        'source_pixel_height': -7719175300224038838,
                                        'rotation': -3470028080447260236,
                                        'virtual_nw_x_pixel': 1962346997,
                                        'virtual_nw_y_pixel': 156728065,
                                        'virtual_width': 1844806429,
                                        'virtual_height': -992141845,
                                    },
                            {
                                        'source_monitor': 5619052,
                                        'source_nw_x_pixel': -38312887915985003,
                                        'source_nw_y_pixel': -7895466186142982116,
                                        'source_pixel_width': -7091870819938399497,
                                        'source_pixel_height': -5332150244111126312,
                                        'rotation': -3602188865257427436,
                                        'virtual_nw_x_pixel': 1713871147,
                                        'virtual_nw_y_pixel': 762450969,
                                        'virtual_width': 1420622501,
                                        'virtual_height': 1351874423,
                                    },
                            {
                                        'source_monitor': -952145,
                                        'source_nw_x_pixel': -2881980364489763901,
                                        'source_nw_y_pixel': -138406509445143406,
                                        'source_pixel_width': -8380065322289820702,
                                        'source_pixel_height': -6819221788430464090,
                                        'rotation': -7893840699800579260,
                                        'virtual_nw_x_pixel': -1636866255,
                                        'virtual_nw_y_pixel': 575898994,
                                        'virtual_width': 1086211510,
                                        'virtual_height': -993851081,
                                    },
                            {
                                        'source_monitor': 7127240,
                                        'source_nw_x_pixel': -1003519551267456386,
                                        'source_nw_y_pixel': -5865476442480928439,
                                        'source_pixel_width': -1344434872685547657,
                                        'source_pixel_height': -6405093627647812462,
                                        'rotation': -6805662302144629940,
                                        'virtual_nw_x_pixel': 1655881586,
                                        'virtual_nw_y_pixel': 933050453,
                                        'virtual_width': -1667056871,
                                        'virtual_height': 66821290,
                                    },
                            {
                                        'source_monitor': 7615649,
                                        'source_nw_x_pixel': -23120181997642665,
                                        'source_nw_y_pixel': -1813867300233073959,
                                        'source_pixel_width': -6117844665789511344,
                                        'source_pixel_height': -1707833932990231500,
                                        'rotation': -469070264077592096,
                                        'virtual_nw_x_pixel': -1287722836,
                                        'virtual_nw_y_pixel': -1051584913,
                                        'virtual_width': 59090888,
                                        'virtual_height': -1645244742,
                                    },
                            {
                                        'source_monitor': 4318981,
                                        'source_nw_x_pixel': -8277223485124853718,
                                        'source_nw_y_pixel': -1554065628149593315,
                                        'source_pixel_width': -2379009533405438418,
                                        'source_pixel_height': -8083077972247996133,
                                        'rotation': -3753777368748029326,
                                        'virtual_nw_x_pixel': 179950101,
                                        'virtual_nw_y_pixel': -506795511,
                                        'virtual_width': -526427375,
                                        'virtual_height': -130204337,
                                    },
                            {
                                        'source_monitor': 3636286,
                                        'source_nw_x_pixel': -7256629589050055139,
                                        'source_nw_y_pixel': -558560365799734024,
                                        'source_pixel_width': -8159219454564251965,
                                        'source_pixel_height': -222644371263026909,
                                        'rotation': -3267185772464040858,
                                        'virtual_nw_x_pixel': -1070720977,
                                        'virtual_nw_y_pixel': -114106685,
                                        'virtual_width': -153196242,
                                        'virtual_height': 712233540,
                                    },
                            {
                                        'source_monitor': 4332190,
                                        'source_nw_x_pixel': -2436120009405446502,
                                        'source_nw_y_pixel': -4486573575630976139,
                                        'source_pixel_width': -3461061725475301483,
                                        'source_pixel_height': -2697294161552150297,
                                        'rotation': -6027221514257839629,
                                        'virtual_nw_x_pixel': -1188407068,
                                        'virtual_nw_y_pixel': -211980884,
                                        'virtual_width': -1555293877,
                                        'virtual_height': 1839891804,
                                    },
                            {
                                        'source_monitor': 9083685,
                                        'source_nw_x_pixel': -7124821252305424946,
                                        'source_nw_y_pixel': -5646556539883591563,
                                        'source_pixel_width': -4387541116928195435,
                                        'source_pixel_height': -8691847768409072195,
                                        'rotation': -2825083209436227026,
                                        'virtual_nw_x_pixel': 1381200376,
                                        'virtual_nw_y_pixel': 852735464,
                                        'virtual_width': 425191164,
                                        'virtual_height': -1293078679,
                                    },
                        ],
                },
                {
                    'description': 'ÁϣͰėЫ±ԖѰӭěҭĳÌѫQș^ȸĞʦІɚȑżˋȺşϲϚ˾',
                    'monitors': [
                            {
                                        'identifier': 1191492,
                                        'width': -4096185704408038679,
                                        'height': -8407670480950390003,
                                    },
                            {
                                        'identifier': 4386619,
                                        'width': -8103804613966060003,
                                        'height': -4374812418955543053,
                                    },
                            {
                                        'identifier': 8692859,
                                        'width': -3034142493742768822,
                                        'height': -3565696127788839419,
                                    },
                            {
                                        'identifier': 9201912,
                                        'width': 1613138003913731567,
                                        'height': 7505701655198018594,
                                    },
                            {
                                        'identifier': 3443813,
                                        'width': 5687831543788586646,
                                        'height': -2520461758931546280,
                                    },
                            {
                                        'identifier': 7771711,
                                        'width': -3117030413278701963,
                                        'height': -2737257497854289562,
                                    },
                            {
                                        'identifier': 5046545,
                                        'width': -5110696344275105238,
                                        'height': -3363418548831921970,
                                    },
                            {
                                        'identifier': 3083017,
                                        'width': -1149549606613103936,
                                        'height': -5835902214935289841,
                                    },
                            {
                                        'identifier': -32506,
                                        'width': -3152060712441455803,
                                        'height': 5727597830452377290,
                                    },
                            {
                                        'identifier': 7882027,
                                        'width': -6105274628840330957,
                                        'height': -6779088441949129084,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -637818,
                                        'source_nw_x_pixel': -214036752753338553,
                                        'source_nw_y_pixel': -2275150487920949520,
                                        'source_pixel_width': -4878317065887278227,
                                        'source_pixel_height': -1849251772774044589,
                                        'rotation': -9034767862903235130,
                                        'virtual_nw_x_pixel': 1749761139,
                                        'virtual_nw_y_pixel': -880949391,
                                        'virtual_width': 763512506,
                                        'virtual_height': 1821340611,
                                    },
                            {
                                        'source_monitor': 2029902,
                                        'source_nw_x_pixel': -4486182877180345538,
                                        'source_nw_y_pixel': -3945715432148793323,
                                        'source_pixel_width': -3737096155570852680,
                                        'source_pixel_height': -7717407615965067371,
                                        'rotation': -7851627189956805146,
                                        'virtual_nw_x_pixel': -699347052,
                                        'virtual_nw_y_pixel': 38618410,
                                        'virtual_width': 118719960,
                                        'virtual_height': -1507810443,
                                    },
                            {
                                        'source_monitor': 224827,
                                        'source_nw_x_pixel': -3758516344426462902,
                                        'source_nw_y_pixel': -5630790880715096840,
                                        'source_pixel_width': -2104305988330453601,
                                        'source_pixel_height': -9145808902715284915,
                                        'rotation': -523561368865549436,
                                        'virtual_nw_x_pixel': 443458710,
                                        'virtual_nw_y_pixel': 530477695,
                                        'virtual_width': 711068541,
                                        'virtual_height': -1817683343,
                                    },
                            {
                                        'source_monitor': 5016658,
                                        'source_nw_x_pixel': -1302610636111831430,
                                        'source_nw_y_pixel': -3516191365960233951,
                                        'source_pixel_width': -4032078548156414601,
                                        'source_pixel_height': -807655214931789032,
                                        'rotation': -753386122955965400,
                                        'virtual_nw_x_pixel': -1340043576,
                                        'virtual_nw_y_pixel': 335877176,
                                        'virtual_width': -1108603388,
                                        'virtual_height': -1668275209,
                                    },
                            {
                                        'source_monitor': 8646633,
                                        'source_nw_x_pixel': -1622791957693746978,
                                        'source_nw_y_pixel': -523316918376385093,
                                        'source_pixel_width': -225465140494462403,
                                        'source_pixel_height': -8433164235873407260,
                                        'rotation': -5707183426384178314,
                                        'virtual_nw_x_pixel': 838755854,
                                        'virtual_nw_y_pixel': 1404639046,
                                        'virtual_width': -1741967431,
                                        'virtual_height': -1345510798,
                                    },
                            {
                                        'source_monitor': 8913063,
                                        'source_nw_x_pixel': -7854102135781418923,
                                        'source_nw_y_pixel': -4537710526471514494,
                                        'source_pixel_width': -1379280085224504659,
                                        'source_pixel_height': -802295032474593984,
                                        'rotation': -7066469098897296477,
                                        'virtual_nw_x_pixel': -576352924,
                                        'virtual_nw_y_pixel': 1903988760,
                                        'virtual_width': 49797739,
                                        'virtual_height': -1029889009,
                                    },
                            {
                                        'source_monitor': 5318871,
                                        'source_nw_x_pixel': -4025607769441525466,
                                        'source_nw_y_pixel': -1004918547476335127,
                                        'source_pixel_width': -8521586044663023453,
                                        'source_pixel_height': -6159677456865591015,
                                        'rotation': -7406250134015333359,
                                        'virtual_nw_x_pixel': 1643056792,
                                        'virtual_nw_y_pixel': -525153419,
                                        'virtual_width': -310845597,
                                        'virtual_height': 1365584939,
                                    },
                            {
                                        'source_monitor': 5438355,
                                        'source_nw_x_pixel': -7107620597816953705,
                                        'source_nw_y_pixel': -6001495058932710289,
                                        'source_pixel_width': -8624893767053436418,
                                        'source_pixel_height': -7961397287842424234,
                                        'rotation': -5433754855756045608,
                                        'virtual_nw_x_pixel': -628226857,
                                        'virtual_nw_y_pixel': -1685670229,
                                        'virtual_width': -1952511665,
                                        'virtual_height': -1713275926,
                                    },
                            {
                                        'source_monitor': 5661098,
                                        'source_nw_x_pixel': -4516500335695520405,
                                        'source_nw_y_pixel': -9016602466606384491,
                                        'source_pixel_width': -9047901799288702620,
                                        'source_pixel_height': -3252209843605953407,
                                        'rotation': -5860108392734379752,
                                        'virtual_nw_x_pixel': 401148185,
                                        'virtual_nw_y_pixel': 704032334,
                                        'virtual_width': 1155976847,
                                        'virtual_height': -1030384921,
                                    },
                            {
                                        'source_monitor': 1325153,
                                        'source_nw_x_pixel': -6087848999234003893,
                                        'source_nw_y_pixel': -6329264304253128499,
                                        'source_pixel_width': -2368678393974979437,
                                        'source_pixel_height': -4335423733993240435,
                                        'rotation': -7797302814997712001,
                                        'virtual_nw_x_pixel': -486940956,
                                        'virtual_nw_y_pixel': -157082716,
                                        'virtual_width': -467065149,
                                        'virtual_height': -1450747027,
                                    },
                        ],
                },
                {
                    'description': 'ɘƺΖɇŷϧxĮ˃',
                    'monitors': [
                            {
                                        'identifier': 1097151,
                                        'width': 7952825013359181032,
                                        'height': -3913182266635323354,
                                    },
                            {
                                        'identifier': 6008921,
                                        'width': -6005851479841703872,
                                        'height': 3970133597241468116,
                                    },
                            {
                                        'identifier': 7534688,
                                        'width': 1700139803075626681,
                                        'height': 2105308122020139184,
                                    },
                            {
                                        'identifier': 2197730,
                                        'width': -1332383063241638275,
                                        'height': 1895490766918405874,
                                    },
                            {
                                        'identifier': 3011027,
                                        'width': -6671055053352274130,
                                        'height': -7777798149663219657,
                                    },
                            {
                                        'identifier': 485367,
                                        'width': -596438745889663655,
                                        'height': -6002385755052928602,
                                    },
                            {
                                        'identifier': 8566206,
                                        'width': 5250241457403841503,
                                        'height': 1210703247536485098,
                                    },
                            {
                                        'identifier': 6919819,
                                        'width': -7770418746291893136,
                                        'height': -9020687725695500061,
                                    },
                            {
                                        'identifier': 8073784,
                                        'width': -2670117302170364236,
                                        'height': 8145272100015050933,
                                    },
                            {
                                        'identifier': 7187471,
                                        'width': 2688236502928327715,
                                        'height': -1501795661358769123,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8001031,
                                        'source_nw_x_pixel': -936169957377628877,
                                        'source_nw_y_pixel': -6540163021216793300,
                                        'source_pixel_width': -5671969063176406155,
                                        'source_pixel_height': -376626440778268255,
                                        'rotation': -1330157572562647180,
                                        'virtual_nw_x_pixel': 1497583140,
                                        'virtual_nw_y_pixel': -1878117622,
                                        'virtual_width': 1615517527,
                                        'virtual_height': 1482701303,
                                    },
                            {
                                        'source_monitor': 2958868,
                                        'source_nw_x_pixel': -8848378668063626157,
                                        'source_nw_y_pixel': -4966402988642721041,
                                        'source_pixel_width': -6875143532378268787,
                                        'source_pixel_height': -6906473148376647738,
                                        'rotation': -396381579119713014,
                                        'virtual_nw_x_pixel': 1590157490,
                                        'virtual_nw_y_pixel': -946670137,
                                        'virtual_width': 593734030,
                                        'virtual_height': 131061637,
                                    },
                            {
                                        'source_monitor': 240816,
                                        'source_nw_x_pixel': -3010844347293234207,
                                        'source_nw_y_pixel': -1869313501581435810,
                                        'source_pixel_width': -8241409680099134719,
                                        'source_pixel_height': -5376967084758948618,
                                        'rotation': -1220872388941523212,
                                        'virtual_nw_x_pixel': -1900994345,
                                        'virtual_nw_y_pixel': 431664553,
                                        'virtual_width': 1067160771,
                                        'virtual_height': 1831594916,
                                    },
                            {
                                        'source_monitor': 3091852,
                                        'source_nw_x_pixel': -3982021469037493198,
                                        'source_nw_y_pixel': -942551621336474555,
                                        'source_pixel_width': -77649294127927105,
                                        'source_pixel_height': -505787272493064783,
                                        'rotation': -7272437945572332332,
                                        'virtual_nw_x_pixel': -1327788964,
                                        'virtual_nw_y_pixel': 98864329,
                                        'virtual_width': -1673345344,
                                        'virtual_height': -1294383225,
                                    },
                            {
                                        'source_monitor': 5435066,
                                        'source_nw_x_pixel': -984541366387561647,
                                        'source_nw_y_pixel': -5423244549025029393,
                                        'source_pixel_width': -4690029417780711933,
                                        'source_pixel_height': -2948866194820858896,
                                        'rotation': -7542545458505178797,
                                        'virtual_nw_x_pixel': -36780843,
                                        'virtual_nw_y_pixel': -996680184,
                                        'virtual_width': 1722455597,
                                        'virtual_height': -108698412,
                                    },
                            {
                                        'source_monitor': 2187294,
                                        'source_nw_x_pixel': -1296000141754754671,
                                        'source_nw_y_pixel': -1498719409620172305,
                                        'source_pixel_width': -2288078453479871261,
                                        'source_pixel_height': -882703231726146970,
                                        'rotation': -2104665130599493094,
                                        'virtual_nw_x_pixel': 1641180763,
                                        'virtual_nw_y_pixel': 1710133625,
                                        'virtual_width': 1078286436,
                                        'virtual_height': 825023442,
                                    },
                            {
                                        'source_monitor': 7606082,
                                        'source_nw_x_pixel': -7651176980228738157,
                                        'source_nw_y_pixel': -5561574808690221441,
                                        'source_pixel_width': -627437239642451656,
                                        'source_pixel_height': -1609298165010211976,
                                        'rotation': -3341674721809154210,
                                        'virtual_nw_x_pixel': -1310208063,
                                        'virtual_nw_y_pixel': -147405839,
                                        'virtual_width': -84356973,
                                        'virtual_height': -1543410661,
                                    },
                            {
                                        'source_monitor': 9855037,
                                        'source_nw_x_pixel': -765916926618214894,
                                        'source_nw_y_pixel': -460278785315835452,
                                        'source_pixel_width': -8024892396052899662,
                                        'source_pixel_height': -1286393484302783927,
                                        'rotation': -3265029576869686782,
                                        'virtual_nw_x_pixel': 1277299719,
                                        'virtual_nw_y_pixel': -1338069962,
                                        'virtual_width': 1056225221,
                                        'virtual_height': 589822475,
                                    },
                            {
                                        'source_monitor': 2865601,
                                        'source_nw_x_pixel': -1218189323969555626,
                                        'source_nw_y_pixel': -7813719413395763583,
                                        'source_pixel_width': -2946544404498135839,
                                        'source_pixel_height': -7606441036359805012,
                                        'rotation': -2405292758584397229,
                                        'virtual_nw_x_pixel': 1433379595,
                                        'virtual_nw_y_pixel': -824823428,
                                        'virtual_width': 201372351,
                                        'virtual_height': -206744312,
                                    },
                            {
                                        'source_monitor': -958237,
                                        'source_nw_x_pixel': -4377490913834250819,
                                        'source_nw_y_pixel': -1005927669779943570,
                                        'source_pixel_width': -7672090064749313941,
                                        'source_pixel_height': -6365786661827334253,
                                        'rotation': -7202678846395525407,
                                        'virtual_nw_x_pixel': -722385746,
                                        'virtual_nw_y_pixel': -808269479,
                                        'virtual_width': 388984760,
                                        'virtual_height': -498606431,
                                    },
                        ],
                },
                {
                    'description': 'ѤɘPǈɦБԊŀz-þЇźҊʳɧǫʯP',
                    'monitors': [
                            {
                                        'identifier': 9612881,
                                        'width': -4778500559345144478,
                                        'height': 2646448687955115499,
                                    },
                            {
                                        'identifier': 7896892,
                                        'width': -1496085323315318998,
                                        'height': 4354768072353832896,
                                    },
                            {
                                        'identifier': 9832698,
                                        'width': 1545536565973308604,
                                        'height': -8750665430009636650,
                                    },
                            {
                                        'identifier': 8263236,
                                        'width': 7324109524961565683,
                                        'height': 6774149733397891411,
                                    },
                            {
                                        'identifier': 7086893,
                                        'width': -7342129161199952570,
                                        'height': -5751011940386155260,
                                    },
                            {
                                        'identifier': 4061875,
                                        'width': 3803504543064742412,
                                        'height': 2889699696390789574,
                                    },
                            {
                                        'identifier': 1790745,
                                        'width': -2362910194717257684,
                                        'height': -3495363087983471696,
                                    },
                            {
                                        'identifier': 1868931,
                                        'width': -307759347079437824,
                                        'height': -2602200320918143622,
                                    },
                            {
                                        'identifier': 6374370,
                                        'width': -6312970477888055137,
                                        'height': -3020017757640117169,
                                    },
                            {
                                        'identifier': 1616553,
                                        'width': -6893742450920563536,
                                        'height': 6370499678902201932,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8345310,
                                        'source_nw_x_pixel': -3287073989571036592,
                                        'source_nw_y_pixel': -4295110051364431253,
                                        'source_pixel_width': -4570602960230287843,
                                        'source_pixel_height': -464791996009693989,
                                        'rotation': -624876039194660992,
                                        'virtual_nw_x_pixel': -1661113301,
                                        'virtual_nw_y_pixel': 1293753671,
                                        'virtual_width': -1058767517,
                                        'virtual_height': -892591917,
                                    },
                            {
                                        'source_monitor': 9102494,
                                        'source_nw_x_pixel': -7736005433427947200,
                                        'source_nw_y_pixel': -4583400671960172680,
                                        'source_pixel_width': -626498501000113995,
                                        'source_pixel_height': -7812052446571748774,
                                        'rotation': -5735893150292456411,
                                        'virtual_nw_x_pixel': 1777343932,
                                        'virtual_nw_y_pixel': -518889014,
                                        'virtual_width': 1081563234,
                                        'virtual_height': -969071743,
                                    },
                            {
                                        'source_monitor': -777151,
                                        'source_nw_x_pixel': -2381766060170881811,
                                        'source_nw_y_pixel': -29940936117791771,
                                        'source_pixel_width': -4961449032898829447,
                                        'source_pixel_height': -1146140321533014647,
                                        'rotation': -5411557964289380432,
                                        'virtual_nw_x_pixel': 555190423,
                                        'virtual_nw_y_pixel': 1637333862,
                                        'virtual_width': 1754179255,
                                        'virtual_height': -182952277,
                                    },
                            {
                                        'source_monitor': 2102237,
                                        'source_nw_x_pixel': -1485974339762054633,
                                        'source_nw_y_pixel': -9020472662128893998,
                                        'source_pixel_width': -3280271893354048721,
                                        'source_pixel_height': -9045284544886175608,
                                        'rotation': -51600325656745533,
                                        'virtual_nw_x_pixel': -1858443196,
                                        'virtual_nw_y_pixel': 1423026623,
                                        'virtual_width': -905481672,
                                        'virtual_height': 711943524,
                                    },
                            {
                                        'source_monitor': 4833727,
                                        'source_nw_x_pixel': -3359211523910988121,
                                        'source_nw_y_pixel': -1593589133647959249,
                                        'source_pixel_width': -3545341239404616191,
                                        'source_pixel_height': -1423204389900359226,
                                        'rotation': -7478501135034936683,
                                        'virtual_nw_x_pixel': 693697794,
                                        'virtual_nw_y_pixel': 1037550208,
                                        'virtual_width': -515090463,
                                        'virtual_height': 1165451622,
                                    },
                            {
                                        'source_monitor': -490827,
                                        'source_nw_x_pixel': -5031590977777711843,
                                        'source_nw_y_pixel': -1908718215696058291,
                                        'source_pixel_width': -1740641565016889949,
                                        'source_pixel_height': -392454815050024097,
                                        'rotation': -4831208984732654432,
                                        'virtual_nw_x_pixel': -149837379,
                                        'virtual_nw_y_pixel': 704593771,
                                        'virtual_width': -845064074,
                                        'virtual_height': -1671614476,
                                    },
                            {
                                        'source_monitor': 8053783,
                                        'source_nw_x_pixel': -1839163832827895198,
                                        'source_nw_y_pixel': -734856923836375910,
                                        'source_pixel_width': -3417334376297727275,
                                        'source_pixel_height': -3306285285243288714,
                                        'rotation': -7104798745248707787,
                                        'virtual_nw_x_pixel': 6196559,
                                        'virtual_nw_y_pixel': 345383957,
                                        'virtual_width': -1907211620,
                                        'virtual_height': 1526333157,
                                    },
                            {
                                        'source_monitor': 2328443,
                                        'source_nw_x_pixel': -1139223184167660342,
                                        'source_nw_y_pixel': -1788149686105733090,
                                        'source_pixel_width': -4509707872950615152,
                                        'source_pixel_height': -7496267071113585349,
                                        'rotation': -2444575105694380829,
                                        'virtual_nw_x_pixel': 425222453,
                                        'virtual_nw_y_pixel': 1241988168,
                                        'virtual_width': -657047020,
                                        'virtual_height': 177091710,
                                    },
                            {
                                        'source_monitor': 4361417,
                                        'source_nw_x_pixel': -3408921878545863992,
                                        'source_nw_y_pixel': -8031861371402524525,
                                        'source_pixel_width': -6320470883946458348,
                                        'source_pixel_height': -6782066045986411718,
                                        'rotation': -5971398660825264346,
                                        'virtual_nw_x_pixel': 1928747508,
                                        'virtual_nw_y_pixel': 758561362,
                                        'virtual_width': 600392378,
                                        'virtual_height': -1865031688,
                                    },
                            {
                                        'source_monitor': 4786181,
                                        'source_nw_x_pixel': -654597445058512387,
                                        'source_nw_y_pixel': -150001653238599376,
                                        'source_pixel_width': -8257642815704431957,
                                        'source_pixel_height': -905076201615004931,
                                        'rotation': -7919576064296941430,
                                        'virtual_nw_x_pixel': -520235276,
                                        'virtual_nw_y_pixel': -355282874,
                                        'virtual_width': -1588511494,
                                        'virtual_height': 882998997,
                                    },
                        ],
                },
                {
                    'description': '\x83ʜҝÑIĬZȯтŐƓΊϔ҄ҮɆîͿҡ\x89ӌΎϥƈƃư\u0382Ɓһˣ',
                    'monitors': [
                            {
                                        'identifier': 2545307,
                                        'width': -7405877036374813008,
                                        'height': -2298568388866891526,
                                    },
                            {
                                        'identifier': -473186,
                                        'width': -8841321310126553773,
                                        'height': -1866782816716632444,
                                    },
                            {
                                        'identifier': 7134862,
                                        'width': -3932577333491476676,
                                        'height': -2622892840046705577,
                                    },
                            {
                                        'identifier': 6718803,
                                        'width': 5608046435618027566,
                                        'height': 3209685710383117777,
                                    },
                            {
                                        'identifier': 1307953,
                                        'width': 1990425652258361520,
                                        'height': 4879390613429729586,
                                    },
                            {
                                        'identifier': 6800841,
                                        'width': -1663829955508070326,
                                        'height': 5231196927032352805,
                                    },
                            {
                                        'identifier': 4998745,
                                        'width': 7815289060604994683,
                                        'height': 5703148563611628059,
                                    },
                            {
                                        'identifier': 8595578,
                                        'width': -372851864063451989,
                                        'height': 4415985605145896153,
                                    },
                            {
                                        'identifier': 7503354,
                                        'width': 260409429425153573,
                                        'height': 1796129983348819676,
                                    },
                            {
                                        'identifier': 1364340,
                                        'width': 7978969911567703699,
                                        'height': 289166820381432464,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3740789,
                                        'source_nw_x_pixel': -7347026911695937700,
                                        'source_nw_y_pixel': -9194101727207333786,
                                        'source_pixel_width': -1694983024023909636,
                                        'source_pixel_height': -7029012418131351026,
                                        'rotation': -4035296650012466623,
                                        'virtual_nw_x_pixel': -1278937117,
                                        'virtual_nw_y_pixel': -1454006728,
                                        'virtual_width': -1104317250,
                                        'virtual_height': -1400986096,
                                    },
                            {
                                        'source_monitor': -299683,
                                        'source_nw_x_pixel': -8332135922522479963,
                                        'source_nw_y_pixel': -2016968784532794714,
                                        'source_pixel_width': -7221955102530923025,
                                        'source_pixel_height': -7808041211233307633,
                                        'rotation': -3991833975384501917,
                                        'virtual_nw_x_pixel': -1387206668,
                                        'virtual_nw_y_pixel': -1598068808,
                                        'virtual_width': 655381373,
                                        'virtual_height': 559902148,
                                    },
                            {
                                        'source_monitor': 4793034,
                                        'source_nw_x_pixel': -9105628834641202651,
                                        'source_nw_y_pixel': -4013826939704630198,
                                        'source_pixel_width': -5797909521626310930,
                                        'source_pixel_height': -1115817483203579906,
                                        'rotation': -4952744583977722964,
                                        'virtual_nw_x_pixel': -1234476212,
                                        'virtual_nw_y_pixel': -1002546570,
                                        'virtual_width': 219012265,
                                        'virtual_height': -1335802986,
                                    },
                            {
                                        'source_monitor': 3662556,
                                        'source_nw_x_pixel': -7347354638634304789,
                                        'source_nw_y_pixel': -7534327747339003434,
                                        'source_pixel_width': -4772852391720241899,
                                        'source_pixel_height': -8730928758476839487,
                                        'rotation': -8976875911940374016,
                                        'virtual_nw_x_pixel': -1043566194,
                                        'virtual_nw_y_pixel': 1741461087,
                                        'virtual_width': 776470013,
                                        'virtual_height': 1336887307,
                                    },
                            {
                                        'source_monitor': 9867337,
                                        'source_nw_x_pixel': -4861723790880894892,
                                        'source_nw_y_pixel': -3858566473896729539,
                                        'source_pixel_width': -8549183119530948108,
                                        'source_pixel_height': -2968553487507346193,
                                        'rotation': -7040620992828264742,
                                        'virtual_nw_x_pixel': 1106239074,
                                        'virtual_nw_y_pixel': -1509785129,
                                        'virtual_width': 124707373,
                                        'virtual_height': -1793582419,
                                    },
                            {
                                        'source_monitor': 9612065,
                                        'source_nw_x_pixel': -1244965942768285389,
                                        'source_nw_y_pixel': -2590941425544062911,
                                        'source_pixel_width': -1577863790402844747,
                                        'source_pixel_height': -8645722800665492242,
                                        'rotation': -8949852905571438522,
                                        'virtual_nw_x_pixel': -971724286,
                                        'virtual_nw_y_pixel': -1510611423,
                                        'virtual_width': -1937880972,
                                        'virtual_height': 976999643,
                                    },
                            {
                                        'source_monitor': 619824,
                                        'source_nw_x_pixel': -2466467064241669295,
                                        'source_nw_y_pixel': -4959591227378612267,
                                        'source_pixel_width': -3366267073223838044,
                                        'source_pixel_height': -5272923739779841879,
                                        'rotation': -4405555964971595420,
                                        'virtual_nw_x_pixel': -1541639732,
                                        'virtual_nw_y_pixel': 772503678,
                                        'virtual_width': -880797153,
                                        'virtual_height': -1337794968,
                                    },
                            {
                                        'source_monitor': 3451030,
                                        'source_nw_x_pixel': -6526888762539195952,
                                        'source_nw_y_pixel': -409238716649030891,
                                        'source_pixel_width': -1673540306900885141,
                                        'source_pixel_height': -5591855267687505106,
                                        'rotation': -2560375525559659177,
                                        'virtual_nw_x_pixel': 458027357,
                                        'virtual_nw_y_pixel': -990139336,
                                        'virtual_width': -1133914587,
                                        'virtual_height': -81082352,
                                    },
                            {
                                        'source_monitor': 5593219,
                                        'source_nw_x_pixel': -4426166326342310583,
                                        'source_nw_y_pixel': -18346788756888868,
                                        'source_pixel_width': -664823826538173015,
                                        'source_pixel_height': -6307521539283931620,
                                        'rotation': -872733236094382602,
                                        'virtual_nw_x_pixel': 336889951,
                                        'virtual_nw_y_pixel': 1459022298,
                                        'virtual_width': -604640896,
                                        'virtual_height': 1900836551,
                                    },
                            {
                                        'source_monitor': 3550334,
                                        'source_nw_x_pixel': -3893886937932577856,
                                        'source_nw_y_pixel': -6932938430668611635,
                                        'source_pixel_width': -8195824540995570426,
                                        'source_pixel_height': -2551430392592204974,
                                        'rotation': -1904854124047451774,
                                        'virtual_nw_x_pixel': -157122507,
                                        'virtual_nw_y_pixel': 465261013,
                                        'virtual_width': 1854158472,
                                        'virtual_height': -1457077729,
                                    },
                        ],
                },
                {
                    'description': 'Ӌʔ˗4ÑѫʛϊǾҟԡ˪æLϊĞҟҾɆ®ϠǫçЬЍĚϰ˔Ԅ\u038d',
                    'monitors': [
                            {
                                        'identifier': 9019958,
                                        'width': -270657166327257758,
                                        'height': -3149688822251440394,
                                    },
                            {
                                        'identifier': 772640,
                                        'width': 6035928471040742780,
                                        'height': -2021815918637046549,
                                    },
                            {
                                        'identifier': 6021081,
                                        'width': -1188157159126284760,
                                        'height': 4366949879093254520,
                                    },
                            {
                                        'identifier': 1676244,
                                        'width': 575234055897062911,
                                        'height': -8497339815404688861,
                                    },
                            {
                                        'identifier': -138395,
                                        'width': 6472588710135250395,
                                        'height': 7591310917519922385,
                                    },
                            {
                                        'identifier': 4808626,
                                        'width': -6334914992351741522,
                                        'height': 7973641250341876783,
                                    },
                            {
                                        'identifier': 822629,
                                        'width': 6287539560246043334,
                                        'height': 3178598417405582011,
                                    },
                            {
                                        'identifier': 3797317,
                                        'width': -7150680080457427540,
                                        'height': 3800769449162443652,
                                    },
                            {
                                        'identifier': 3769645,
                                        'width': -3279645153391430524,
                                        'height': 4820476152227445729,
                                    },
                            {
                                        'identifier': 1501719,
                                        'width': -8200687625997799110,
                                        'height': 5184245528978157361,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3907433,
                                        'source_nw_x_pixel': -7279839077244629304,
                                        'source_nw_y_pixel': -7503200364399189049,
                                        'source_pixel_width': -5467364180913440972,
                                        'source_pixel_height': -5955847931675035700,
                                        'rotation': -7034356426104547040,
                                        'virtual_nw_x_pixel': -930321442,
                                        'virtual_nw_y_pixel': 553149951,
                                        'virtual_width': 1525172525,
                                        'virtual_height': -579326863,
                                    },
                            {
                                        'source_monitor': 4025893,
                                        'source_nw_x_pixel': -5807986443690088534,
                                        'source_nw_y_pixel': -1614615122714319115,
                                        'source_pixel_width': -7795194265824350027,
                                        'source_pixel_height': -4328153827335962733,
                                        'rotation': -7256155085982161329,
                                        'virtual_nw_x_pixel': -1450360804,
                                        'virtual_nw_y_pixel': -1373200633,
                                        'virtual_width': -946895135,
                                        'virtual_height': 614670467,
                                    },
                            {
                                        'source_monitor': 8416529,
                                        'source_nw_x_pixel': -5678715405327757823,
                                        'source_nw_y_pixel': -3157531271451444791,
                                        'source_pixel_width': -8556587667373871738,
                                        'source_pixel_height': -3557406021451710599,
                                        'rotation': -8688551874559851471,
                                        'virtual_nw_x_pixel': -1478272747,
                                        'virtual_nw_y_pixel': -1683808423,
                                        'virtual_width': 1691014393,
                                        'virtual_height': -961114106,
                                    },
                            {
                                        'source_monitor': 5142915,
                                        'source_nw_x_pixel': -1401200623386231916,
                                        'source_nw_y_pixel': -1880316214920227229,
                                        'source_pixel_width': -2500135115094577799,
                                        'source_pixel_height': -5551361632698122460,
                                        'rotation': -7139494876699202565,
                                        'virtual_nw_x_pixel': 230469874,
                                        'virtual_nw_y_pixel': 21647401,
                                        'virtual_width': 516456649,
                                        'virtual_height': 114702235,
                                    },
                            {
                                        'source_monitor': 4148143,
                                        'source_nw_x_pixel': -2306610285739143537,
                                        'source_nw_y_pixel': -4204666791196817407,
                                        'source_pixel_width': -1632033165231293987,
                                        'source_pixel_height': -6003175666120627690,
                                        'rotation': -6811654893620974671,
                                        'virtual_nw_x_pixel': -1888313459,
                                        'virtual_nw_y_pixel': 214043177,
                                        'virtual_width': 500940935,
                                        'virtual_height': 793102439,
                                    },
                            {
                                        'source_monitor': 632502,
                                        'source_nw_x_pixel': -3496998398166647948,
                                        'source_nw_y_pixel': -3686740903097114084,
                                        'source_pixel_width': -7579780133021320203,
                                        'source_pixel_height': -5588995987215788113,
                                        'rotation': -2538630396008617062,
                                        'virtual_nw_x_pixel': -228195774,
                                        'virtual_nw_y_pixel': -1595486736,
                                        'virtual_width': 620001466,
                                        'virtual_height': 1187601541,
                                    },
                            {
                                        'source_monitor': 2769974,
                                        'source_nw_x_pixel': -4670468464630327151,
                                        'source_nw_y_pixel': -4148447515996346397,
                                        'source_pixel_width': -5347881179028776327,
                                        'source_pixel_height': -7179581902857099913,
                                        'rotation': -9041923933132872458,
                                        'virtual_nw_x_pixel': -1592637954,
                                        'virtual_nw_y_pixel': 125386499,
                                        'virtual_width': 1498861652,
                                        'virtual_height': 153226043,
                                    },
                            {
                                        'source_monitor': 9965217,
                                        'source_nw_x_pixel': -961354402029383053,
                                        'source_nw_y_pixel': -2213006579617089134,
                                        'source_pixel_width': -7842109761472490165,
                                        'source_pixel_height': -962460407628283804,
                                        'rotation': -1395678308446200610,
                                        'virtual_nw_x_pixel': 922964322,
                                        'virtual_nw_y_pixel': 603112078,
                                        'virtual_width': -1571738972,
                                        'virtual_height': 1123645747,
                                    },
                            {
                                        'source_monitor': 9709592,
                                        'source_nw_x_pixel': -4938250483039765523,
                                        'source_nw_y_pixel': -7598642504223610394,
                                        'source_pixel_width': -4654786320672629185,
                                        'source_pixel_height': -5160333125528691419,
                                        'rotation': -6154511120075699135,
                                        'virtual_nw_x_pixel': -877505072,
                                        'virtual_nw_y_pixel': 1722766572,
                                        'virtual_width': 1492377434,
                                        'virtual_height': 605813842,
                                    },
                            {
                                        'source_monitor': 4394133,
                                        'source_nw_x_pixel': -4278380225343077581,
                                        'source_nw_y_pixel': -2709697775491506378,
                                        'source_pixel_width': -7386875560965281187,
                                        'source_pixel_height': -2655159349518604783,
                                        'rotation': -8282068707585482024,
                                        'virtual_nw_x_pixel': 1558304115,
                                        'virtual_nw_y_pixel': 1908981375,
                                        'virtual_width': 496913814,
                                        'virtual_height': 1819574278,
                                    },
                        ],
                },
                {
                    'description': 'ƭī\x9e҆Ćԑ˲ѫΦҠȶǦŵȀȁFˬƘԎðɘľˆҊȅð\x8aɕЕШ',
                    'monitors': [
                            {
                                        'identifier': 1169446,
                                        'width': 236577542858745275,
                                        'height': 7314794685865774364,
                                    },
                            {
                                        'identifier': 7388628,
                                        'width': 6334436438058968690,
                                        'height': 5021757519321082216,
                                    },
                            {
                                        'identifier': -917604,
                                        'width': -1921941593149860123,
                                        'height': -3066136389816670273,
                                    },
                            {
                                        'identifier': 2618701,
                                        'width': 2647908359187719101,
                                        'height': 5507870677743280382,
                                    },
                            {
                                        'identifier': 3775500,
                                        'width': -3057332674679960502,
                                        'height': -7511333302809129417,
                                    },
                            {
                                        'identifier': 8273001,
                                        'width': 7607983909647886376,
                                        'height': 3538901353990617568,
                                    },
                            {
                                        'identifier': 2469419,
                                        'width': -6819252372461879457,
                                        'height': 3307794345935095124,
                                    },
                            {
                                        'identifier': 3450238,
                                        'width': -2657786572428482501,
                                        'height': -8683320802473490891,
                                    },
                            {
                                        'identifier': 9734888,
                                        'width': 206307251263302577,
                                        'height': 4968108208479496007,
                                    },
                            {
                                        'identifier': 2131045,
                                        'width': 7563466740306003754,
                                        'height': 8880248061379544093,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -388598,
                                        'source_nw_x_pixel': -2793568132018520837,
                                        'source_nw_y_pixel': -3832121878369633182,
                                        'source_pixel_width': -2993502601574804200,
                                        'source_pixel_height': -5292246830138937075,
                                        'rotation': -7758140544961616473,
                                        'virtual_nw_x_pixel': -223086635,
                                        'virtual_nw_y_pixel': -118887305,
                                        'virtual_width': -1300451159,
                                        'virtual_height': 789817031,
                                    },
                            {
                                        'source_monitor': 7205983,
                                        'source_nw_x_pixel': -5085499394274144129,
                                        'source_nw_y_pixel': -7146719823938142347,
                                        'source_pixel_width': -904228499126780274,
                                        'source_pixel_height': -7747963587908934271,
                                        'rotation': -4812524422420112547,
                                        'virtual_nw_x_pixel': 1127239984,
                                        'virtual_nw_y_pixel': -112685792,
                                        'virtual_width': -913084991,
                                        'virtual_height': 962892713,
                                    },
                            {
                                        'source_monitor': 1577386,
                                        'source_nw_x_pixel': -7386083720097386953,
                                        'source_nw_y_pixel': -1676485147844007156,
                                        'source_pixel_width': -1135337978020945569,
                                        'source_pixel_height': -7056856806619903474,
                                        'rotation': -1771811315586904703,
                                        'virtual_nw_x_pixel': -598849994,
                                        'virtual_nw_y_pixel': -1100560650,
                                        'virtual_width': -1624870920,
                                        'virtual_height': 1194383522,
                                    },
                            {
                                        'source_monitor': 1872921,
                                        'source_nw_x_pixel': -1300470011923569194,
                                        'source_nw_y_pixel': -6279762158203769041,
                                        'source_pixel_width': -3805181542489806615,
                                        'source_pixel_height': -4092554306690023596,
                                        'rotation': -4364383911221711783,
                                        'virtual_nw_x_pixel': 703717702,
                                        'virtual_nw_y_pixel': -859004088,
                                        'virtual_width': -1683081471,
                                        'virtual_height': -1969396695,
                                    },
                            {
                                        'source_monitor': 701154,
                                        'source_nw_x_pixel': -2064122272916416934,
                                        'source_nw_y_pixel': -3153696584883619662,
                                        'source_pixel_width': -5159519570213365165,
                                        'source_pixel_height': -3024750888117440414,
                                        'rotation': -8057972216497693453,
                                        'virtual_nw_x_pixel': 220765274,
                                        'virtual_nw_y_pixel': 1417805385,
                                        'virtual_width': 1443297141,
                                        'virtual_height': -1845152065,
                                    },
                            {
                                        'source_monitor': 438977,
                                        'source_nw_x_pixel': -8113504499186642768,
                                        'source_nw_y_pixel': -6662633702696314243,
                                        'source_pixel_width': -9139146690279287487,
                                        'source_pixel_height': -2772829732892417630,
                                        'rotation': -5041713931623393003,
                                        'virtual_nw_x_pixel': 738848972,
                                        'virtual_nw_y_pixel': 1464680764,
                                        'virtual_width': -1134214924,
                                        'virtual_height': 464959619,
                                    },
                            {
                                        'source_monitor': 1246134,
                                        'source_nw_x_pixel': -7063515688059536550,
                                        'source_nw_y_pixel': -1745874861318542228,
                                        'source_pixel_width': -3999273346976108983,
                                        'source_pixel_height': -2147449206177731050,
                                        'rotation': -2846804703485612341,
                                        'virtual_nw_x_pixel': -505588441,
                                        'virtual_nw_y_pixel': 1112766714,
                                        'virtual_width': 516802955,
                                        'virtual_height': 1090665451,
                                    },
                            {
                                        'source_monitor': 2795195,
                                        'source_nw_x_pixel': -1210414722703024609,
                                        'source_nw_y_pixel': -5601720007092481807,
                                        'source_pixel_width': -3720951566101052439,
                                        'source_pixel_height': -2879092324598583737,
                                        'rotation': -6164874921577395432,
                                        'virtual_nw_x_pixel': 1652633700,
                                        'virtual_nw_y_pixel': 497898988,
                                        'virtual_width': -1571210756,
                                        'virtual_height': -1644982251,
                                    },
                            {
                                        'source_monitor': 467472,
                                        'source_nw_x_pixel': -7316399915060991001,
                                        'source_nw_y_pixel': -7160942490595333510,
                                        'source_pixel_width': -3605234029476183028,
                                        'source_pixel_height': -5233354665985225118,
                                        'rotation': -4040076385252880150,
                                        'virtual_nw_x_pixel': -1749922905,
                                        'virtual_nw_y_pixel': 1581602684,
                                        'virtual_width': 1395642004,
                                        'virtual_height': -1202164271,
                                    },
                            {
                                        'source_monitor': 811550,
                                        'source_nw_x_pixel': -2723634274837008506,
                                        'source_nw_y_pixel': -6438364715464067083,
                                        'source_pixel_width': -5726769051041604252,
                                        'source_pixel_height': -8582825227841163414,
                                        'rotation': -5712193916916410056,
                                        'virtual_nw_x_pixel': 1335555290,
                                        'virtual_nw_y_pixel': -875861291,
                                        'virtual_width': 560686406,
                                        'virtual_height': -1149318872,
                                    },
                        ],
                },
                {
                    'description': 'ϚȒнȏͳǓˢǋʧǬ˻τÛƎх\x83ȓ\x80ӽҦȱϦљ¹γˬɃϣЇѡ',
                    'monitors': [
                            {
                                        'identifier': 9455136,
                                        'width': -5463226902487012051,
                                        'height': -2753428754430489061,
                                    },
                            {
                                        'identifier': 8506085,
                                        'width': 4451715197076781225,
                                        'height': -6844547886818569550,
                                    },
                            {
                                        'identifier': 8609569,
                                        'width': -5734546741958930261,
                                        'height': -8469539909495890,
                                    },
                            {
                                        'identifier': 3149435,
                                        'width': 8558312174535051946,
                                        'height': -7645055922281941292,
                                    },
                            {
                                        'identifier': 9061104,
                                        'width': 8307241799807301921,
                                        'height': 6699269400538662050,
                                    },
                            {
                                        'identifier': 7831365,
                                        'width': -5373417969796832185,
                                        'height': 21873181867675004,
                                    },
                            {
                                        'identifier': 965962,
                                        'width': -2455766998352227945,
                                        'height': 7875582141143427883,
                                    },
                            {
                                        'identifier': 2999441,
                                        'width': -5685399227932418532,
                                        'height': -5572215755807473013,
                                    },
                            {
                                        'identifier': 6676535,
                                        'width': 4214426123563374525,
                                        'height': -4954213960512809056,
                                    },
                            {
                                        'identifier': 1387870,
                                        'width': 316082750748888308,
                                        'height': 8219162371056466601,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3115281,
                                        'source_nw_x_pixel': -6704332397416841252,
                                        'source_nw_y_pixel': -2805839872490037503,
                                        'source_pixel_width': -8674400672239933968,
                                        'source_pixel_height': -7730689389669067363,
                                        'rotation': -9047303230939931738,
                                        'virtual_nw_x_pixel': -800771909,
                                        'virtual_nw_y_pixel': -618671673,
                                        'virtual_width': -1686589489,
                                        'virtual_height': -1062378930,
                                    },
                            {
                                        'source_monitor': 2919706,
                                        'source_nw_x_pixel': -3318250348936472399,
                                        'source_nw_y_pixel': -469658270127655495,
                                        'source_pixel_width': -3212129180638142392,
                                        'source_pixel_height': -3457429735546382948,
                                        'rotation': -5230523932946830580,
                                        'virtual_nw_x_pixel': -1491898591,
                                        'virtual_nw_y_pixel': 1427403497,
                                        'virtual_width': 71624558,
                                        'virtual_height': 351269047,
                                    },
                            {
                                        'source_monitor': 3526332,
                                        'source_nw_x_pixel': -8481996354233684957,
                                        'source_nw_y_pixel': -4550329622521187046,
                                        'source_pixel_width': -5190001856508804971,
                                        'source_pixel_height': -2447104788747288934,
                                        'rotation': -7095276463659027060,
                                        'virtual_nw_x_pixel': 50962866,
                                        'virtual_nw_y_pixel': -1825050734,
                                        'virtual_width': -70160938,
                                        'virtual_height': 976920454,
                                    },
                            {
                                        'source_monitor': -229765,
                                        'source_nw_x_pixel': -3935491258872475523,
                                        'source_nw_y_pixel': -3413497890998376941,
                                        'source_pixel_width': -7110806516726414585,
                                        'source_pixel_height': -7303596098157410661,
                                        'rotation': -2480685961415311624,
                                        'virtual_nw_x_pixel': 818500972,
                                        'virtual_nw_y_pixel': 473381615,
                                        'virtual_width': 368660131,
                                        'virtual_height': -624899092,
                                    },
                            {
                                        'source_monitor': 9883218,
                                        'source_nw_x_pixel': -3267309565439712803,
                                        'source_nw_y_pixel': -7509310082570732153,
                                        'source_pixel_width': -6983890727847015620,
                                        'source_pixel_height': -2717545148781883770,
                                        'rotation': -1335487831080288842,
                                        'virtual_nw_x_pixel': -187718495,
                                        'virtual_nw_y_pixel': -1181665321,
                                        'virtual_width': 365025990,
                                        'virtual_height': 522869846,
                                    },
                            {
                                        'source_monitor': 5338407,
                                        'source_nw_x_pixel': -2332978029885143114,
                                        'source_nw_y_pixel': -3769401824164037127,
                                        'source_pixel_width': -3867068667995349874,
                                        'source_pixel_height': -4784542020924750456,
                                        'rotation': -6194946013269082204,
                                        'virtual_nw_x_pixel': 393794656,
                                        'virtual_nw_y_pixel': -776550388,
                                        'virtual_width': -285590524,
                                        'virtual_height': 883981906,
                                    },
                            {
                                        'source_monitor': 7951224,
                                        'source_nw_x_pixel': -3592850309802720063,
                                        'source_nw_y_pixel': -4988609189905291857,
                                        'source_pixel_width': -5527946163840570149,
                                        'source_pixel_height': -1884942663968089720,
                                        'rotation': -1113962481225280726,
                                        'virtual_nw_x_pixel': 1629721652,
                                        'virtual_nw_y_pixel': -1646666449,
                                        'virtual_width': -1233288779,
                                        'virtual_height': -100709759,
                                    },
                            {
                                        'source_monitor': 7795239,
                                        'source_nw_x_pixel': -1027294879744689932,
                                        'source_nw_y_pixel': -5313358903571229027,
                                        'source_pixel_width': -1064862618875247737,
                                        'source_pixel_height': -8879564890427895664,
                                        'rotation': -7161524701253868656,
                                        'virtual_nw_x_pixel': 935440348,
                                        'virtual_nw_y_pixel': -1326394880,
                                        'virtual_width': -849849056,
                                        'virtual_height': -908447839,
                                    },
                            {
                                        'source_monitor': 9659158,
                                        'source_nw_x_pixel': -72786874327773489,
                                        'source_nw_y_pixel': -8295043500252365375,
                                        'source_pixel_width': -1507372577265007735,
                                        'source_pixel_height': -4061785974927076077,
                                        'rotation': -430456027960979530,
                                        'virtual_nw_x_pixel': -1109494687,
                                        'virtual_nw_y_pixel': 439341113,
                                        'virtual_width': 508193750,
                                        'virtual_height': -1660104600,
                                    },
                            {
                                        'source_monitor': 4809764,
                                        'source_nw_x_pixel': -363339868261489468,
                                        'source_nw_y_pixel': -7121521555041203117,
                                        'source_pixel_width': -1137478150740289781,
                                        'source_pixel_height': -1147160114485695196,
                                        'rotation': -798659176515960401,
                                        'virtual_nw_x_pixel': -1337269420,
                                        'virtual_nw_y_pixel': -160959733,
                                        'virtual_width': -1075404060,
                                        'virtual_height': 638799798,
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
                                        'identifier': 2762220,
                                        'width': 501638225858696470,
                                        'height': 4251291162916256220,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -486447521330511123,
                                        'source_nw_y_pixel': -7042684240692552971,
                                        'source_pixel_width': -9193287030094380487,
                                        'source_pixel_height': -4199241623982351662,
                                        'rotation': -5051084772649122731,
                                        'virtual_nw_x_pixel': 1581671983,
                                        'virtual_nw_y_pixel': 433758884,
                                        'virtual_width': 1412369271,
                                        'virtual_height': 670880035,
                                    },
                        ],
                },
            ],

        },
    ),
]
