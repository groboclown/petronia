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
            'identifier': 3897385,
            'width': -6131400956493771323,
            'height': 7485415661562185116,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 8315770,

            'width': -2386999230432072141,

            'height': -7010957794607640020,

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
            'source_monitor': 9318502,
            'source_nw_x_pixel': -5651535888689734895,
            'source_nw_y_pixel': -7273323417770701236,
            'source_pixel_width': -1449730999286531777,
            'source_pixel_height': -3569403669306386247,
            'rotation': -2682884556768500668,
            'virtual_nw_x_pixel': -1268632280,
            'virtual_nw_y_pixel': -184221764,
            'virtual_width': -1012477191,
            'virtual_height': 643002816,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -683463060885268553,

            'source_nw_y_pixel': -7780189915401219622,

            'source_pixel_width': -7321986820164807904,

            'source_pixel_height': -8442659871080400312,

            'rotation': -7704487984217145890,

            'virtual_nw_x_pixel': 269609502,

            'virtual_nw_y_pixel': 1962023335,

            'virtual_width': 1983023152,

            'virtual_height': -1413157327,

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
            'description': ';ΕӚȤʗÚԎȈɅƃ҂Ʈʷ÷Β˹ǖŐìˡΫ\u0383˂Ǔ\x94TǬoεʳ',
            'monitors': [
                {
                    'identifier': 7352594,
                    'width': 3046381828629012815,
                    'height': -2975899427431956868,
                },
                {
                    'identifier': -107872,
                    'width': 8010443831623789056,
                    'height': 6519180862906235192,
                },
                {
                    'identifier': 2319471,
                    'width': -1602971838203456475,
                    'height': -5693424716483038698,
                },
                {
                    'identifier': 6454022,
                    'width': -3692653650560095838,
                    'height': 5871569867134447192,
                },
                {
                    'identifier': 708020,
                    'width': 7576222479417544942,
                    'height': 7076239181081338546,
                },
                {
                    'identifier': 6622856,
                    'width': 3557790826472028935,
                    'height': 3064584773394072544,
                },
                {
                    'identifier': 8331716,
                    'width': -1385221154907110182,
                    'height': -285467500145539071,
                },
                {
                    'identifier': 7388194,
                    'width': -8685989322005934080,
                    'height': -77207416698572099,
                },
                {
                    'identifier': 934307,
                    'width': -6765187003130867636,
                    'height': -9051162493025955254,
                },
                {
                    'identifier': 2119780,
                    'width': 1676705809940595355,
                    'height': 7463633375806609666,
                },
            ],
            'screen': [
                {
                    'source_monitor': 5935769,
                    'source_nw_x_pixel': -5539572149598874789,
                    'source_nw_y_pixel': -5471606684957253250,
                    'source_pixel_width': -6708279018737690462,
                    'source_pixel_height': -8831192116917303713,
                    'rotation': -9035326720619529482,
                    'virtual_nw_x_pixel': -890510407,
                    'virtual_nw_y_pixel': 1763823717,
                    'virtual_width': -804557128,
                    'virtual_height': -1680941589,
                },
                {
                    'source_monitor': 8410505,
                    'source_nw_x_pixel': -4269276547055394295,
                    'source_nw_y_pixel': -4018482638591713482,
                    'source_pixel_width': -2162003609415281759,
                    'source_pixel_height': -7747377321343326570,
                    'rotation': -3194171554116733562,
                    'virtual_nw_x_pixel': -1383356451,
                    'virtual_nw_y_pixel': -952367213,
                    'virtual_width': -1234844455,
                    'virtual_height': -1315790337,
                },
                {
                    'source_monitor': 4513981,
                    'source_nw_x_pixel': -7928926881598380157,
                    'source_nw_y_pixel': -1857014045424470545,
                    'source_pixel_width': -6457719164233701403,
                    'source_pixel_height': -6713952640814270180,
                    'rotation': -3727748749927208043,
                    'virtual_nw_x_pixel': 669232423,
                    'virtual_nw_y_pixel': -1139202039,
                    'virtual_width': -1916992641,
                    'virtual_height': 281439407,
                },
                {
                    'source_monitor': 4833400,
                    'source_nw_x_pixel': -156705140762526467,
                    'source_nw_y_pixel': -7368177343722660358,
                    'source_pixel_width': -8029929618221970511,
                    'source_pixel_height': -3434614889860187760,
                    'rotation': -6344707947639898295,
                    'virtual_nw_x_pixel': 339687082,
                    'virtual_nw_y_pixel': 278569486,
                    'virtual_width': 76996825,
                    'virtual_height': -1222064171,
                },
                {
                    'source_monitor': 4595831,
                    'source_nw_x_pixel': -6433603646507401502,
                    'source_nw_y_pixel': -3549796355109224320,
                    'source_pixel_width': -346682446268500496,
                    'source_pixel_height': -2252981829928615404,
                    'rotation': -8841561908082463944,
                    'virtual_nw_x_pixel': 835222291,
                    'virtual_nw_y_pixel': -926198311,
                    'virtual_width': -1576217689,
                    'virtual_height': -798510049,
                },
                {
                    'source_monitor': 305762,
                    'source_nw_x_pixel': -7319528938384098961,
                    'source_nw_y_pixel': -33729715390897200,
                    'source_pixel_width': -1802796781134024582,
                    'source_pixel_height': -2764411419652751850,
                    'rotation': -906574893367651795,
                    'virtual_nw_x_pixel': 1031045452,
                    'virtual_nw_y_pixel': -1806302375,
                    'virtual_width': 669435637,
                    'virtual_height': -942891999,
                },
                {
                    'source_monitor': 5980900,
                    'source_nw_x_pixel': -4196985336751253789,
                    'source_nw_y_pixel': -5090115662109228421,
                    'source_pixel_width': -32677603524048162,
                    'source_pixel_height': -740547338346853329,
                    'rotation': -4247137602614417809,
                    'virtual_nw_x_pixel': -46566341,
                    'virtual_nw_y_pixel': 1244638151,
                    'virtual_width': 1617897370,
                    'virtual_height': -674029777,
                },
                {
                    'source_monitor': 2863740,
                    'source_nw_x_pixel': -8761640147537708447,
                    'source_nw_y_pixel': -8262482878937296669,
                    'source_pixel_width': -5896101577313351419,
                    'source_pixel_height': -1123009239918510100,
                    'rotation': -7184285677700360050,
                    'virtual_nw_x_pixel': -219546190,
                    'virtual_nw_y_pixel': -38551104,
                    'virtual_width': 845710551,
                    'virtual_height': 175010854,
                },
                {
                    'source_monitor': 7722763,
                    'source_nw_x_pixel': -9174753292207635203,
                    'source_nw_y_pixel': -7214962772417165734,
                    'source_pixel_width': -3860524226699266417,
                    'source_pixel_height': -7265695184340637611,
                    'rotation': -4577668010688121629,
                    'virtual_nw_x_pixel': -390691601,
                    'virtual_nw_y_pixel': -1861202167,
                    'virtual_width': 1429954257,
                    'virtual_height': 1491249378,
                },
                {
                    'source_monitor': 9842631,
                    'source_nw_x_pixel': -2874158217927658734,
                    'source_nw_y_pixel': -8831942177461693514,
                    'source_pixel_width': -6750556397609705018,
                    'source_pixel_height': -1493898235215527214,
                    'rotation': -7760873935470786009,
                    'virtual_nw_x_pixel': 186213484,
                    'virtual_nw_y_pixel': 1971621863,
                    'virtual_width': -768361528,
                    'virtual_height': -1785266522,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 9580647,
                    'width': 5882613880836824944,
                    'height': 6775796599406556155,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -7952696962062452352,
                    'source_nw_y_pixel': -5468918869253952859,
                    'source_pixel_width': -3941657968002713041,
                    'source_pixel_height': -1055843053198886779,
                    'rotation': -856684936271746550,
                    'virtual_nw_x_pixel': -1396593514,
                    'virtual_nw_y_pixel': -1676046947,
                    'virtual_width': 919079771,
                    'virtual_height': 1186290125,
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
            'request_id': 3250721,
            'mapped_screens_by_monitors': [
                {
                    'description': 'ŌɎԗћǕDƼģΛûёφǃˎÕнӊŊҕ΅Ӯ;χǪȸǄ\x9e\x96Ԡƌ',
                    'monitors': [
                            {
                                        'identifier': 2912308,
                                        'width': 6219058433695717853,
                                        'height': -988667954933159764,
                                    },
                            {
                                        'identifier': 750839,
                                        'width': -7631497211141245888,
                                        'height': 1091223652602916775,
                                    },
                            {
                                        'identifier': 2182736,
                                        'width': 1438281153044116528,
                                        'height': 4278030954820128390,
                                    },
                            {
                                        'identifier': 760214,
                                        'width': 6092679779196603750,
                                        'height': 902344993326595547,
                                    },
                            {
                                        'identifier': -801565,
                                        'width': 7539755710395509921,
                                        'height': -3062192780303264793,
                                    },
                            {
                                        'identifier': 8625557,
                                        'width': 379726568741182927,
                                        'height': -2706024992774953473,
                                    },
                            {
                                        'identifier': 1238548,
                                        'width': 182671193149688747,
                                        'height': -4285234149489726099,
                                    },
                            {
                                        'identifier': -684175,
                                        'width': 6757369083001005985,
                                        'height': 4368579578956585305,
                                    },
                            {
                                        'identifier': 6938868,
                                        'width': -5215797105065901219,
                                        'height': -7162651578162535573,
                                    },
                            {
                                        'identifier': 8357021,
                                        'width': 793319215243038381,
                                        'height': -285790386816403780,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4272481,
                                        'source_nw_x_pixel': -8131766693579462228,
                                        'source_nw_y_pixel': -569855023043502701,
                                        'source_pixel_width': -6716808828798250175,
                                        'source_pixel_height': -3823056534033027576,
                                        'rotation': -270805901884840096,
                                        'virtual_nw_x_pixel': -1207358008,
                                        'virtual_nw_y_pixel': 86231121,
                                        'virtual_width': 215755840,
                                        'virtual_height': -496723652,
                                    },
                            {
                                        'source_monitor': 8091593,
                                        'source_nw_x_pixel': -3955728469098205832,
                                        'source_nw_y_pixel': -7272694633161303428,
                                        'source_pixel_width': -232906064354873686,
                                        'source_pixel_height': -2931216142576687160,
                                        'rotation': -3988216992110990123,
                                        'virtual_nw_x_pixel': -1583385069,
                                        'virtual_nw_y_pixel': -1216497770,
                                        'virtual_width': 1411100572,
                                        'virtual_height': 272887100,
                                    },
                            {
                                        'source_monitor': 849236,
                                        'source_nw_x_pixel': -5536430368919934615,
                                        'source_nw_y_pixel': -1933944628134743499,
                                        'source_pixel_width': -5713328683327978466,
                                        'source_pixel_height': -2260150429712777605,
                                        'rotation': -738657845887448624,
                                        'virtual_nw_x_pixel': -382416027,
                                        'virtual_nw_y_pixel': 1368863934,
                                        'virtual_width': 651816163,
                                        'virtual_height': 862593069,
                                    },
                            {
                                        'source_monitor': 4667246,
                                        'source_nw_x_pixel': -7773317006033824738,
                                        'source_nw_y_pixel': -4864185085694606340,
                                        'source_pixel_width': -745748407048496482,
                                        'source_pixel_height': -1808914768493897745,
                                        'rotation': -4301255684272806091,
                                        'virtual_nw_x_pixel': -963864005,
                                        'virtual_nw_y_pixel': -146707369,
                                        'virtual_width': 1651567961,
                                        'virtual_height': -1164339416,
                                    },
                            {
                                        'source_monitor': 5734912,
                                        'source_nw_x_pixel': -9057397546955280917,
                                        'source_nw_y_pixel': -5512670255371227114,
                                        'source_pixel_width': -7531528195583136894,
                                        'source_pixel_height': -3498136306784453859,
                                        'rotation': -6953260290632377948,
                                        'virtual_nw_x_pixel': 1197755927,
                                        'virtual_nw_y_pixel': 776344213,
                                        'virtual_width': -709548478,
                                        'virtual_height': -731194910,
                                    },
                            {
                                        'source_monitor': 8845654,
                                        'source_nw_x_pixel': -8653781833725747931,
                                        'source_nw_y_pixel': -7570160419663469632,
                                        'source_pixel_width': -1558824276636003910,
                                        'source_pixel_height': -5260197795756790525,
                                        'rotation': -665880957296037722,
                                        'virtual_nw_x_pixel': -768713642,
                                        'virtual_nw_y_pixel': -1037182513,
                                        'virtual_width': -1424985128,
                                        'virtual_height': -1522031500,
                                    },
                            {
                                        'source_monitor': 9264099,
                                        'source_nw_x_pixel': -1466030510482551344,
                                        'source_nw_y_pixel': -3463175859471302647,
                                        'source_pixel_width': -1051811499782549632,
                                        'source_pixel_height': -1686709426651371116,
                                        'rotation': -824513877574525340,
                                        'virtual_nw_x_pixel': 1006739687,
                                        'virtual_nw_y_pixel': 1053416252,
                                        'virtual_width': -604443220,
                                        'virtual_height': -745968369,
                                    },
                            {
                                        'source_monitor': 1363239,
                                        'source_nw_x_pixel': -1874547616867756668,
                                        'source_nw_y_pixel': -2458798549164119120,
                                        'source_pixel_width': -4937068051135964327,
                                        'source_pixel_height': -2516031459506930598,
                                        'rotation': -4647882822358893496,
                                        'virtual_nw_x_pixel': -14862325,
                                        'virtual_nw_y_pixel': 1611565589,
                                        'virtual_width': 1934881087,
                                        'virtual_height': 72104971,
                                    },
                            {
                                        'source_monitor': 8355495,
                                        'source_nw_x_pixel': -3714936308146796386,
                                        'source_nw_y_pixel': -3785709572586476026,
                                        'source_pixel_width': -9146600076023047775,
                                        'source_pixel_height': -8532170795224124545,
                                        'rotation': -7058712962449062700,
                                        'virtual_nw_x_pixel': 863667374,
                                        'virtual_nw_y_pixel': 1907000852,
                                        'virtual_width': 238658437,
                                        'virtual_height': 861103849,
                                    },
                            {
                                        'source_monitor': 2774716,
                                        'source_nw_x_pixel': -8379076389855741061,
                                        'source_nw_y_pixel': -4595957050212166692,
                                        'source_pixel_width': -9026380016083115719,
                                        'source_pixel_height': -7438789611012999465,
                                        'rotation': -3869683073986896205,
                                        'virtual_nw_x_pixel': 1520640724,
                                        'virtual_nw_y_pixel': 498195228,
                                        'virtual_width': -1408790734,
                                        'virtual_height': -966574385,
                                    },
                        ],
                },
                {
                    'description': 'ΰʣɹГƬӦƦԮҖӯřΠӐы_X\x8fӷõѱԪ҄ĐЂʨπ˓ÙĿ[',
                    'monitors': [
                            {
                                        'identifier': 3990683,
                                        'width': 8165052973095111696,
                                        'height': -5609653220999797868,
                                    },
                            {
                                        'identifier': 6460758,
                                        'width': -5325789523428897022,
                                        'height': -3213364115670164886,
                                    },
                            {
                                        'identifier': 5939984,
                                        'width': -592508241666200906,
                                        'height': -8071806264601678418,
                                    },
                            {
                                        'identifier': 7614599,
                                        'width': 7874116516313050567,
                                        'height': -9024805685537023080,
                                    },
                            {
                                        'identifier': 7718662,
                                        'width': -5041121252324740084,
                                        'height': 1589270207965606224,
                                    },
                            {
                                        'identifier': 733626,
                                        'width': -9007098567062803118,
                                        'height': -3139849725660777027,
                                    },
                            {
                                        'identifier': 9849806,
                                        'width': -3025816616119178921,
                                        'height': -2546195222933117531,
                                    },
                            {
                                        'identifier': 7827403,
                                        'width': -1038444915185356890,
                                        'height': -4022024280236604730,
                                    },
                            {
                                        'identifier': 9337426,
                                        'width': -5033041548257960615,
                                        'height': -2865121165756100471,
                                    },
                            {
                                        'identifier': 7623747,
                                        'width': -1785949595468338582,
                                        'height': 4149713775604742441,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6490698,
                                        'source_nw_x_pixel': -1759990566468682370,
                                        'source_nw_y_pixel': -5961452646780837628,
                                        'source_pixel_width': -5375058185554321935,
                                        'source_pixel_height': -7151428538830319104,
                                        'rotation': -6683991297086771763,
                                        'virtual_nw_x_pixel': 1917496213,
                                        'virtual_nw_y_pixel': -321538483,
                                        'virtual_width': -282523602,
                                        'virtual_height': -806731201,
                                    },
                            {
                                        'source_monitor': -44426,
                                        'source_nw_x_pixel': -5074283927677272440,
                                        'source_nw_y_pixel': -270972457850200049,
                                        'source_pixel_width': -767586135778520637,
                                        'source_pixel_height': -2430001801943133105,
                                        'rotation': -1813751921859570728,
                                        'virtual_nw_x_pixel': 792487122,
                                        'virtual_nw_y_pixel': -926996026,
                                        'virtual_width': 43050301,
                                        'virtual_height': -978205444,
                                    },
                            {
                                        'source_monitor': 6142294,
                                        'source_nw_x_pixel': -7403632271858519700,
                                        'source_nw_y_pixel': -5441433316819224463,
                                        'source_pixel_width': -634330795078215086,
                                        'source_pixel_height': -383523910802561153,
                                        'rotation': -868075205216217374,
                                        'virtual_nw_x_pixel': 372695524,
                                        'virtual_nw_y_pixel': 1917189881,
                                        'virtual_width': -679630617,
                                        'virtual_height': 314550180,
                                    },
                            {
                                        'source_monitor': 4095119,
                                        'source_nw_x_pixel': -5624542328071402037,
                                        'source_nw_y_pixel': -4693762846855240671,
                                        'source_pixel_width': -5168174726878760326,
                                        'source_pixel_height': -3446454996910976325,
                                        'rotation': -4257291616157615074,
                                        'virtual_nw_x_pixel': -1691160186,
                                        'virtual_nw_y_pixel': -1221979930,
                                        'virtual_width': 1833733339,
                                        'virtual_height': -477681845,
                                    },
                            {
                                        'source_monitor': 1249873,
                                        'source_nw_x_pixel': -2245394847821919349,
                                        'source_nw_y_pixel': -517933884341788333,
                                        'source_pixel_width': -7547404109439264730,
                                        'source_pixel_height': -9096839354604160963,
                                        'rotation': -9021047939605185328,
                                        'virtual_nw_x_pixel': 565487164,
                                        'virtual_nw_y_pixel': -1002766777,
                                        'virtual_width': -1720738389,
                                        'virtual_height': 1434709971,
                                    },
                            {
                                        'source_monitor': 3073000,
                                        'source_nw_x_pixel': -4564429752982987930,
                                        'source_nw_y_pixel': -274612151107717731,
                                        'source_pixel_width': -3847616385258979654,
                                        'source_pixel_height': -3827183163269922250,
                                        'rotation': -4022331166749138998,
                                        'virtual_nw_x_pixel': -267322058,
                                        'virtual_nw_y_pixel': -1699039498,
                                        'virtual_width': -1724042288,
                                        'virtual_height': -1589968222,
                                    },
                            {
                                        'source_monitor': 5732939,
                                        'source_nw_x_pixel': -7781547981230213503,
                                        'source_nw_y_pixel': -2199468463290892425,
                                        'source_pixel_width': -4459166000470335260,
                                        'source_pixel_height': -899659206861331277,
                                        'rotation': -3173672137187632793,
                                        'virtual_nw_x_pixel': -725719014,
                                        'virtual_nw_y_pixel': 718316337,
                                        'virtual_width': -1378197721,
                                        'virtual_height': 1264984072,
                                    },
                            {
                                        'source_monitor': 8909743,
                                        'source_nw_x_pixel': -546274741023038708,
                                        'source_nw_y_pixel': -3813974345872383306,
                                        'source_pixel_width': -3995588718069364811,
                                        'source_pixel_height': -3161636067718261884,
                                        'rotation': -4643980639059873313,
                                        'virtual_nw_x_pixel': -1125633077,
                                        'virtual_nw_y_pixel': 313756440,
                                        'virtual_width': -1450437124,
                                        'virtual_height': 1629445082,
                                    },
                            {
                                        'source_monitor': 895201,
                                        'source_nw_x_pixel': -356096483619262569,
                                        'source_nw_y_pixel': -5309118974125272956,
                                        'source_pixel_width': -7359539707244473537,
                                        'source_pixel_height': -3189549839910567972,
                                        'rotation': -8193277471631042403,
                                        'virtual_nw_x_pixel': -1732049655,
                                        'virtual_nw_y_pixel': -1544080594,
                                        'virtual_width': 706351902,
                                        'virtual_height': 177555096,
                                    },
                            {
                                        'source_monitor': 8841197,
                                        'source_nw_x_pixel': -3184054571585596233,
                                        'source_nw_y_pixel': -5780332351596284307,
                                        'source_pixel_width': -4422909671654482017,
                                        'source_pixel_height': -6348791181015531212,
                                        'rotation': -7957122339393301124,
                                        'virtual_nw_x_pixel': -243623393,
                                        'virtual_nw_y_pixel': 210836088,
                                        'virtual_width': 1433758951,
                                        'virtual_height': -847443740,
                                    },
                        ],
                },
                {
                    'description': 'ͷƪíƼƩÀʯџԣƛİӑԋşЈ˦Ƌ\x94˛ӎгЦɟǜzƋ"Ӂũ\x97',
                    'monitors': [
                            {
                                        'identifier': 4372491,
                                        'width': 6814538482355842858,
                                        'height': 2007371243118406547,
                                    },
                            {
                                        'identifier': 4762186,
                                        'width': -2568807074184542243,
                                        'height': -6160909878689177958,
                                    },
                            {
                                        'identifier': 8780997,
                                        'width': -8565399880979094992,
                                        'height': 5147317728735116312,
                                    },
                            {
                                        'identifier': 7728068,
                                        'width': 510615688279794825,
                                        'height': -5173296169878013042,
                                    },
                            {
                                        'identifier': 1638625,
                                        'width': -996179897890188634,
                                        'height': 2082234435614876690,
                                    },
                            {
                                        'identifier': 5671337,
                                        'width': 1674806491056418124,
                                        'height': 4698259415551783967,
                                    },
                            {
                                        'identifier': 9325790,
                                        'width': 653860387277431115,
                                        'height': -8358173361881178478,
                                    },
                            {
                                        'identifier': 4603601,
                                        'width': -4748168375957580261,
                                        'height': -5078628700163818585,
                                    },
                            {
                                        'identifier': 3418581,
                                        'width': -5003455023774304371,
                                        'height': -2406086825137490140,
                                    },
                            {
                                        'identifier': 1264574,
                                        'width': -5869268918509782085,
                                        'height': -2841780670309151679,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5978340,
                                        'source_nw_x_pixel': -1494994411576219550,
                                        'source_nw_y_pixel': -4140331298859411385,
                                        'source_pixel_width': -5230206552029143397,
                                        'source_pixel_height': -7593534767747321761,
                                        'rotation': -1922759004263478481,
                                        'virtual_nw_x_pixel': -1036727585,
                                        'virtual_nw_y_pixel': 367085127,
                                        'virtual_width': -155921929,
                                        'virtual_height': 1217087550,
                                    },
                            {
                                        'source_monitor': 3813722,
                                        'source_nw_x_pixel': -7257539385934100682,
                                        'source_nw_y_pixel': -4390636073805596076,
                                        'source_pixel_width': -3119589717984913065,
                                        'source_pixel_height': -2396934757714795531,
                                        'rotation': -5558132016775817355,
                                        'virtual_nw_x_pixel': -1714988357,
                                        'virtual_nw_y_pixel': 87285242,
                                        'virtual_width': 1107815426,
                                        'virtual_height': -1644222801,
                                    },
                            {
                                        'source_monitor': 4546249,
                                        'source_nw_x_pixel': -7284335177984734489,
                                        'source_nw_y_pixel': -5868663509642980372,
                                        'source_pixel_width': -4375494331591864054,
                                        'source_pixel_height': -8208043663906845052,
                                        'rotation': -8152714388768521733,
                                        'virtual_nw_x_pixel': 1322603309,
                                        'virtual_nw_y_pixel': 1704785939,
                                        'virtual_width': 1400263193,
                                        'virtual_height': 1684143831,
                                    },
                            {
                                        'source_monitor': 9469148,
                                        'source_nw_x_pixel': -8156356695921118877,
                                        'source_nw_y_pixel': -221088061252845431,
                                        'source_pixel_width': -3838288746439685795,
                                        'source_pixel_height': -3136881792153447230,
                                        'rotation': -948412398971300269,
                                        'virtual_nw_x_pixel': -1619197441,
                                        'virtual_nw_y_pixel': 938807556,
                                        'virtual_width': -1646648624,
                                        'virtual_height': 40800303,
                                    },
                            {
                                        'source_monitor': 1004259,
                                        'source_nw_x_pixel': -1805802342771196675,
                                        'source_nw_y_pixel': -3843452334656523764,
                                        'source_pixel_width': -299361720500875674,
                                        'source_pixel_height': -736618540408333206,
                                        'rotation': -7272493574847152049,
                                        'virtual_nw_x_pixel': 215689049,
                                        'virtual_nw_y_pixel': -1488345916,
                                        'virtual_width': 487639183,
                                        'virtual_height': -1962917179,
                                    },
                            {
                                        'source_monitor': 3967781,
                                        'source_nw_x_pixel': -6102268067978935728,
                                        'source_nw_y_pixel': -8345042190037942500,
                                        'source_pixel_width': -4290562473565397833,
                                        'source_pixel_height': -1534944812428365009,
                                        'rotation': -8965000986223497411,
                                        'virtual_nw_x_pixel': -1444265457,
                                        'virtual_nw_y_pixel': 1746897958,
                                        'virtual_width': -370330811,
                                        'virtual_height': 1641427256,
                                    },
                            {
                                        'source_monitor': -899462,
                                        'source_nw_x_pixel': -4988870647239601200,
                                        'source_nw_y_pixel': -2375664155925942019,
                                        'source_pixel_width': -2467299042311493122,
                                        'source_pixel_height': -2731279494718172467,
                                        'rotation': -5219399882465415252,
                                        'virtual_nw_x_pixel': 768507719,
                                        'virtual_nw_y_pixel': 1239351351,
                                        'virtual_width': -646863013,
                                        'virtual_height': 823938389,
                                    },
                            {
                                        'source_monitor': 2353533,
                                        'source_nw_x_pixel': -1400092823270248827,
                                        'source_nw_y_pixel': -6300963286094339882,
                                        'source_pixel_width': -4734434176768957629,
                                        'source_pixel_height': -5559171709506399881,
                                        'rotation': -154317762535828773,
                                        'virtual_nw_x_pixel': 67560378,
                                        'virtual_nw_y_pixel': -567471023,
                                        'virtual_width': -1145564025,
                                        'virtual_height': 835255763,
                                    },
                            {
                                        'source_monitor': 9375595,
                                        'source_nw_x_pixel': -9222112968692362364,
                                        'source_nw_y_pixel': -3531964880792974648,
                                        'source_pixel_width': -6152877897698227029,
                                        'source_pixel_height': -4302919433617036040,
                                        'rotation': -1295864384129484862,
                                        'virtual_nw_x_pixel': 1885810660,
                                        'virtual_nw_y_pixel': -973591159,
                                        'virtual_width': -698597710,
                                        'virtual_height': -1542963350,
                                    },
                            {
                                        'source_monitor': 7134623,
                                        'source_nw_x_pixel': -3284499280854704105,
                                        'source_nw_y_pixel': -5263296117535876678,
                                        'source_pixel_width': -551718684161882304,
                                        'source_pixel_height': -925436783701341953,
                                        'rotation': -2426266118297560493,
                                        'virtual_nw_x_pixel': 1741930573,
                                        'virtual_nw_y_pixel': -373461606,
                                        'virtual_width': -45597629,
                                        'virtual_height': 192647936,
                                    },
                        ],
                },
                {
                    'description': 'ȯәϖôːæʀіɀҟĠʿʜӭʹӮЍԗʙƤıȤϭϐˌΈ\x85˘˜ȟ',
                    'monitors': [
                            {
                                        'identifier': 5671381,
                                        'width': -8782441820844121437,
                                        'height': -3706568394558122125,
                                    },
                            {
                                        'identifier': 4609754,
                                        'width': 4255435603990952905,
                                        'height': 9129855407600822523,
                                    },
                            {
                                        'identifier': 1658845,
                                        'width': 3250484313346792095,
                                        'height': -6903732938250606455,
                                    },
                            {
                                        'identifier': 874331,
                                        'width': -6912219708055491379,
                                        'height': -2505800727160908034,
                                    },
                            {
                                        'identifier': 3725677,
                                        'width': 3319660644830391030,
                                        'height': -444406836695483464,
                                    },
                            {
                                        'identifier': 9908085,
                                        'width': -7612700996105949070,
                                        'height': 4322809686176666886,
                                    },
                            {
                                        'identifier': 5915481,
                                        'width': 7470118021284452066,
                                        'height': -2701200507640279173,
                                    },
                            {
                                        'identifier': 5579244,
                                        'width': 3600327073980166929,
                                        'height': -8991351525620653934,
                                    },
                            {
                                        'identifier': 2866200,
                                        'width': 338138856270342580,
                                        'height': 2993738227293324423,
                                    },
                            {
                                        'identifier': 492748,
                                        'width': 1509134618085387373,
                                        'height': -7392112741699606746,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6899769,
                                        'source_nw_x_pixel': -7546939384410538492,
                                        'source_nw_y_pixel': -227931879675977919,
                                        'source_pixel_width': -8337309635723745896,
                                        'source_pixel_height': -3352654383066893255,
                                        'rotation': -8449154869835445103,
                                        'virtual_nw_x_pixel': -1616636006,
                                        'virtual_nw_y_pixel': 798837524,
                                        'virtual_width': -459453788,
                                        'virtual_height': 300511726,
                                    },
                            {
                                        'source_monitor': 8482332,
                                        'source_nw_x_pixel': -8228135540002037411,
                                        'source_nw_y_pixel': -2710740286827652272,
                                        'source_pixel_width': -2178266250898461199,
                                        'source_pixel_height': -762738103514351871,
                                        'rotation': -4724138815464775719,
                                        'virtual_nw_x_pixel': 1322212598,
                                        'virtual_nw_y_pixel': 393174586,
                                        'virtual_width': 66735163,
                                        'virtual_height': -675616611,
                                    },
                            {
                                        'source_monitor': 3421766,
                                        'source_nw_x_pixel': -4861635694440823,
                                        'source_nw_y_pixel': -1631251459190048998,
                                        'source_pixel_width': -6576577865713403631,
                                        'source_pixel_height': -2336588186752453902,
                                        'rotation': -8433184184286837362,
                                        'virtual_nw_x_pixel': 571065082,
                                        'virtual_nw_y_pixel': -1602024369,
                                        'virtual_width': 1406748295,
                                        'virtual_height': -154113052,
                                    },
                            {
                                        'source_monitor': 6230869,
                                        'source_nw_x_pixel': -8331334262422148969,
                                        'source_nw_y_pixel': -5547413745327153525,
                                        'source_pixel_width': -1825493758258554054,
                                        'source_pixel_height': -7116042131226014990,
                                        'rotation': -8373146325948982143,
                                        'virtual_nw_x_pixel': 367235582,
                                        'virtual_nw_y_pixel': 1437371035,
                                        'virtual_width': -182579640,
                                        'virtual_height': 1524467248,
                                    },
                            {
                                        'source_monitor': 2520970,
                                        'source_nw_x_pixel': -1100279714871859597,
                                        'source_nw_y_pixel': -4089747259302959452,
                                        'source_pixel_width': -7579328675569487758,
                                        'source_pixel_height': -8216784104646765179,
                                        'rotation': -4211578384075825632,
                                        'virtual_nw_x_pixel': 1512254480,
                                        'virtual_nw_y_pixel': -1402172916,
                                        'virtual_width': -284549566,
                                        'virtual_height': 314367490,
                                    },
                            {
                                        'source_monitor': 3975585,
                                        'source_nw_x_pixel': -4939382749433179138,
                                        'source_nw_y_pixel': -3823308316859981127,
                                        'source_pixel_width': -6926694798085583751,
                                        'source_pixel_height': -2436220559720653924,
                                        'rotation': -1250581708826849000,
                                        'virtual_nw_x_pixel': -260745920,
                                        'virtual_nw_y_pixel': -1643336675,
                                        'virtual_width': 1736748614,
                                        'virtual_height': -1707759142,
                                    },
                            {
                                        'source_monitor': 6284379,
                                        'source_nw_x_pixel': -2616815084166062836,
                                        'source_nw_y_pixel': -7970747311424299145,
                                        'source_pixel_width': -7898541417203409974,
                                        'source_pixel_height': -5822399918063974187,
                                        'rotation': -3140653995228874284,
                                        'virtual_nw_x_pixel': -1142693739,
                                        'virtual_nw_y_pixel': -265643507,
                                        'virtual_width': 391619032,
                                        'virtual_height': -880544163,
                                    },
                            {
                                        'source_monitor': -582025,
                                        'source_nw_x_pixel': -7544206519681528630,
                                        'source_nw_y_pixel': -6457188151177437253,
                                        'source_pixel_width': -9020402588389521084,
                                        'source_pixel_height': -6339274256911588102,
                                        'rotation': -1458614706037058440,
                                        'virtual_nw_x_pixel': -1792064402,
                                        'virtual_nw_y_pixel': -1945488694,
                                        'virtual_width': -175182113,
                                        'virtual_height': 263685840,
                                    },
                            {
                                        'source_monitor': 1475018,
                                        'source_nw_x_pixel': -6786604001293816960,
                                        'source_nw_y_pixel': -2462410638282956918,
                                        'source_pixel_width': -427976316088865788,
                                        'source_pixel_height': -6407494301136430733,
                                        'rotation': -5076485742894538392,
                                        'virtual_nw_x_pixel': 1952697487,
                                        'virtual_nw_y_pixel': 1845371125,
                                        'virtual_width': 860960107,
                                        'virtual_height': 1386486631,
                                    },
                            {
                                        'source_monitor': 9116670,
                                        'source_nw_x_pixel': -4131100762014741076,
                                        'source_nw_y_pixel': -7717452984016659682,
                                        'source_pixel_width': -902900872898266839,
                                        'source_pixel_height': -1638745265389612603,
                                        'rotation': -2325464475161009609,
                                        'virtual_nw_x_pixel': -1806456554,
                                        'virtual_nw_y_pixel': -1707198709,
                                        'virtual_width': 605580785,
                                        'virtual_height': -1461370736,
                                    },
                        ],
                },
                {
                    'description': 'ϵňĨǥцЪ',
                    'monitors': [
                            {
                                        'identifier': 1507466,
                                        'width': -8581820156511648986,
                                        'height': -2397534079735320928,
                                    },
                            {
                                        'identifier': 3342149,
                                        'width': 564411968347566408,
                                        'height': 6638043245821940396,
                                    },
                            {
                                        'identifier': -345279,
                                        'width': -421318296250158221,
                                        'height': -123958644061541005,
                                    },
                            {
                                        'identifier': -330331,
                                        'width': -1150413778303789185,
                                        'height': 5338441671324831278,
                                    },
                            {
                                        'identifier': 1564826,
                                        'width': -787838179447062679,
                                        'height': 3882292194399016221,
                                    },
                            {
                                        'identifier': 4471486,
                                        'width': 4722904582149178090,
                                        'height': -258196631315828445,
                                    },
                            {
                                        'identifier': 8203624,
                                        'width': -6696275059821750797,
                                        'height': -902349095945635776,
                                    },
                            {
                                        'identifier': 9171944,
                                        'width': -5319196283821945993,
                                        'height': -1145835091543638000,
                                    },
                            {
                                        'identifier': 9522119,
                                        'width': 6398367523809784996,
                                        'height': -5329929749952628050,
                                    },
                            {
                                        'identifier': 1808528,
                                        'width': 7389033122147104484,
                                        'height': 690001873680840513,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -528658,
                                        'source_nw_x_pixel': -5474768905643970869,
                                        'source_nw_y_pixel': -8277387134340666834,
                                        'source_pixel_width': -4635133619275980069,
                                        'source_pixel_height': -7378006300111315690,
                                        'rotation': -6748481476030899343,
                                        'virtual_nw_x_pixel': 1119161053,
                                        'virtual_nw_y_pixel': 1639104712,
                                        'virtual_width': 1282796243,
                                        'virtual_height': 1476726830,
                                    },
                            {
                                        'source_monitor': 9756806,
                                        'source_nw_x_pixel': -6875739484923982322,
                                        'source_nw_y_pixel': -6891431540459134178,
                                        'source_pixel_width': -4044847345098894514,
                                        'source_pixel_height': -5262241367201877760,
                                        'rotation': -6554260642751467197,
                                        'virtual_nw_x_pixel': -753099832,
                                        'virtual_nw_y_pixel': 1005965831,
                                        'virtual_width': 475207326,
                                        'virtual_height': -1612456967,
                                    },
                            {
                                        'source_monitor': 8148042,
                                        'source_nw_x_pixel': -8496302294181323063,
                                        'source_nw_y_pixel': -369778715797044458,
                                        'source_pixel_width': -6635507757136825822,
                                        'source_pixel_height': -5869028751933527115,
                                        'rotation': -9121176297003328209,
                                        'virtual_nw_x_pixel': 1515416716,
                                        'virtual_nw_y_pixel': 1825084770,
                                        'virtual_width': 1630968933,
                                        'virtual_height': -1587190099,
                                    },
                            {
                                        'source_monitor': 5476255,
                                        'source_nw_x_pixel': -5996320103031554575,
                                        'source_nw_y_pixel': -2591610313808895983,
                                        'source_pixel_width': -3289670738822720552,
                                        'source_pixel_height': -1946333342515005409,
                                        'rotation': -4971725429976953139,
                                        'virtual_nw_x_pixel': -709833729,
                                        'virtual_nw_y_pixel': -1262454065,
                                        'virtual_width': -435566108,
                                        'virtual_height': -134080085,
                                    },
                            {
                                        'source_monitor': -909311,
                                        'source_nw_x_pixel': -8271545903409977000,
                                        'source_nw_y_pixel': -2126141844849930276,
                                        'source_pixel_width': -3848036899062069690,
                                        'source_pixel_height': -11428826165799490,
                                        'rotation': -9061095995276857735,
                                        'virtual_nw_x_pixel': -121186313,
                                        'virtual_nw_y_pixel': -221677947,
                                        'virtual_width': -1816307602,
                                        'virtual_height': -1665260008,
                                    },
                            {
                                        'source_monitor': 640466,
                                        'source_nw_x_pixel': -3667454025508015344,
                                        'source_nw_y_pixel': -3498610185883880966,
                                        'source_pixel_width': -603199323117533679,
                                        'source_pixel_height': -8942559047116782996,
                                        'rotation': -2824690695881687759,
                                        'virtual_nw_x_pixel': 1995624381,
                                        'virtual_nw_y_pixel': -210896758,
                                        'virtual_width': 119167522,
                                        'virtual_height': 1164730332,
                                    },
                            {
                                        'source_monitor': 8832798,
                                        'source_nw_x_pixel': -8886364803782096596,
                                        'source_nw_y_pixel': -1629909833426379001,
                                        'source_pixel_width': -9098191257308493110,
                                        'source_pixel_height': -2210715795216938139,
                                        'rotation': -1004137075025467159,
                                        'virtual_nw_x_pixel': 40884893,
                                        'virtual_nw_y_pixel': -1983529344,
                                        'virtual_width': -1045230049,
                                        'virtual_height': -1552967949,
                                    },
                            {
                                        'source_monitor': -546156,
                                        'source_nw_x_pixel': -8570799402957975511,
                                        'source_nw_y_pixel': -7579691882380080248,
                                        'source_pixel_width': -7562937992757309901,
                                        'source_pixel_height': -8148745809876396940,
                                        'rotation': -4735898202583137013,
                                        'virtual_nw_x_pixel': -359379761,
                                        'virtual_nw_y_pixel': -360306911,
                                        'virtual_width': -168818533,
                                        'virtual_height': -246935587,
                                    },
                            {
                                        'source_monitor': 8166410,
                                        'source_nw_x_pixel': -5735436827112027759,
                                        'source_nw_y_pixel': -7369683472314252131,
                                        'source_pixel_width': -8214703691283442930,
                                        'source_pixel_height': -6380999620594768322,
                                        'rotation': -7349292049832171825,
                                        'virtual_nw_x_pixel': 841978720,
                                        'virtual_nw_y_pixel': 1371157388,
                                        'virtual_width': -712000382,
                                        'virtual_height': -943702403,
                                    },
                            {
                                        'source_monitor': 3357751,
                                        'source_nw_x_pixel': -2780347183739605274,
                                        'source_nw_y_pixel': -3570501919752118132,
                                        'source_pixel_width': -2964812592950761766,
                                        'source_pixel_height': -4972983512752459559,
                                        'rotation': -2933605716398944043,
                                        'virtual_nw_x_pixel': -874759380,
                                        'virtual_nw_y_pixel': -1964210442,
                                        'virtual_width': -226648387,
                                        'virtual_height': 1452149945,
                                    },
                        ],
                },
                {
                    'description': 'źŕɦǹíɦɥʞљdʴțӦɟɍå1b҅ʵǸӉԭ¬Δǃѭѵл*',
                    'monitors': [
                            {
                                        'identifier': 3010697,
                                        'width': -749369298350252159,
                                        'height': -1031982815802042281,
                                    },
                            {
                                        'identifier': 9545287,
                                        'width': 199436972277896316,
                                        'height': -1791748380901184839,
                                    },
                            {
                                        'identifier': 8798684,
                                        'width': 6166310022169877612,
                                        'height': 738375865374324255,
                                    },
                            {
                                        'identifier': 9163919,
                                        'width': -5304791914982502892,
                                        'height': 858413099817588127,
                                    },
                            {
                                        'identifier': 5191035,
                                        'width': 8010483005436377605,
                                        'height': 1287650875717284779,
                                    },
                            {
                                        'identifier': 5454457,
                                        'width': 420396229091102775,
                                        'height': -5681725047540644320,
                                    },
                            {
                                        'identifier': 3488975,
                                        'width': 5973955200508868430,
                                        'height': -2588702933682620310,
                                    },
                            {
                                        'identifier': 5728616,
                                        'width': 4722253954636971480,
                                        'height': 3995121942985056695,
                                    },
                            {
                                        'identifier': -149935,
                                        'width': -8162565110122727273,
                                        'height': -3930261006062624720,
                                    },
                            {
                                        'identifier': 605632,
                                        'width': 120762012141422396,
                                        'height': 5562059204336246651,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -857074,
                                        'source_nw_x_pixel': -6806477969906430957,
                                        'source_nw_y_pixel': -3819748743457504907,
                                        'source_pixel_width': -6103054115549770306,
                                        'source_pixel_height': -202326009574315428,
                                        'rotation': -423711542420393894,
                                        'virtual_nw_x_pixel': 716881310,
                                        'virtual_nw_y_pixel': -409771925,
                                        'virtual_width': -621683790,
                                        'virtual_height': 1831161230,
                                    },
                            {
                                        'source_monitor': 2143689,
                                        'source_nw_x_pixel': -2533118566276542818,
                                        'source_nw_y_pixel': -9121929752916830943,
                                        'source_pixel_width': -988061910227875543,
                                        'source_pixel_height': -2358096895297922228,
                                        'rotation': -1438737400766202526,
                                        'virtual_nw_x_pixel': -288471285,
                                        'virtual_nw_y_pixel': -741631371,
                                        'virtual_width': 705402251,
                                        'virtual_height': -72197737,
                                    },
                            {
                                        'source_monitor': 2464905,
                                        'source_nw_x_pixel': -6489380850384310747,
                                        'source_nw_y_pixel': -1443905759388511161,
                                        'source_pixel_width': -9081283768371513061,
                                        'source_pixel_height': -6847494575204308672,
                                        'rotation': -7874512183851639628,
                                        'virtual_nw_x_pixel': 982960923,
                                        'virtual_nw_y_pixel': 1017211734,
                                        'virtual_width': -893894924,
                                        'virtual_height': 1591429545,
                                    },
                            {
                                        'source_monitor': 4331169,
                                        'source_nw_x_pixel': -95302309927089750,
                                        'source_nw_y_pixel': -3620502822793761845,
                                        'source_pixel_width': -6356489792850434568,
                                        'source_pixel_height': -5710740013661865507,
                                        'rotation': -7904355333769348307,
                                        'virtual_nw_x_pixel': 1362897716,
                                        'virtual_nw_y_pixel': -263407011,
                                        'virtual_width': 493871046,
                                        'virtual_height': 1163675864,
                                    },
                            {
                                        'source_monitor': 5068114,
                                        'source_nw_x_pixel': -46528500765261624,
                                        'source_nw_y_pixel': -7887956502730945683,
                                        'source_pixel_width': -538513141673389050,
                                        'source_pixel_height': -1644711468058270953,
                                        'rotation': -1424247476520145396,
                                        'virtual_nw_x_pixel': 1066188369,
                                        'virtual_nw_y_pixel': 1498339752,
                                        'virtual_width': 1091123889,
                                        'virtual_height': 666432416,
                                    },
                            {
                                        'source_monitor': 595525,
                                        'source_nw_x_pixel': -4882849710169475938,
                                        'source_nw_y_pixel': -4995571862504392629,
                                        'source_pixel_width': -4659129638214390961,
                                        'source_pixel_height': -4922491829025147225,
                                        'rotation': -8440125945540696425,
                                        'virtual_nw_x_pixel': 282709220,
                                        'virtual_nw_y_pixel': -1455547077,
                                        'virtual_width': 334115606,
                                        'virtual_height': 358593534,
                                    },
                            {
                                        'source_monitor': 5026825,
                                        'source_nw_x_pixel': -3102192526377277255,
                                        'source_nw_y_pixel': -2870741714719890336,
                                        'source_pixel_width': -7114993954227733478,
                                        'source_pixel_height': -7796319917555825621,
                                        'rotation': -3461195292437743385,
                                        'virtual_nw_x_pixel': 429101564,
                                        'virtual_nw_y_pixel': 397770725,
                                        'virtual_width': -1728419104,
                                        'virtual_height': 1589795251,
                                    },
                            {
                                        'source_monitor': 8887732,
                                        'source_nw_x_pixel': -5486767848333318391,
                                        'source_nw_y_pixel': -5970806618389025987,
                                        'source_pixel_width': -3526432316463893448,
                                        'source_pixel_height': -567676240912539482,
                                        'rotation': -3897718056574220851,
                                        'virtual_nw_x_pixel': -1469857311,
                                        'virtual_nw_y_pixel': -557777215,
                                        'virtual_width': 923296980,
                                        'virtual_height': 1439468907,
                                    },
                            {
                                        'source_monitor': 7821143,
                                        'source_nw_x_pixel': -403666585461653751,
                                        'source_nw_y_pixel': -8058290943307852346,
                                        'source_pixel_width': -3917421522147252860,
                                        'source_pixel_height': -421026092698586973,
                                        'rotation': -3430967676030205597,
                                        'virtual_nw_x_pixel': 305888472,
                                        'virtual_nw_y_pixel': -1932314525,
                                        'virtual_width': 1733932717,
                                        'virtual_height': -1685307736,
                                    },
                            {
                                        'source_monitor': 9471562,
                                        'source_nw_x_pixel': -7435193782800017729,
                                        'source_nw_y_pixel': -7599968753865641883,
                                        'source_pixel_width': -4107897537937856721,
                                        'source_pixel_height': -5694177959163160461,
                                        'rotation': -4353102145868418802,
                                        'virtual_nw_x_pixel': 1976191364,
                                        'virtual_nw_y_pixel': 633068322,
                                        'virtual_width': 93599360,
                                        'virtual_height': -989292001,
                                    },
                        ],
                },
                {
                    'description': 'ɵԚɶrƂϯOFɍoɤ(\x9bȓν$ԇИѴѓŭΤѹȾΉr˙Ёǀʥ',
                    'monitors': [
                            {
                                        'identifier': 7287938,
                                        'width': -7941913272102584229,
                                        'height': -4629151578710664057,
                                    },
                            {
                                        'identifier': 3061299,
                                        'width': -8919686253067979455,
                                        'height': -1598400437909814792,
                                    },
                            {
                                        'identifier': 7236175,
                                        'width': -6618363098862275224,
                                        'height': -1638061315399085597,
                                    },
                            {
                                        'identifier': 176027,
                                        'width': -7285898840944912946,
                                        'height': -2878885633145610313,
                                    },
                            {
                                        'identifier': 581934,
                                        'width': -4448634535837171672,
                                        'height': 6527287978170353536,
                                    },
                            {
                                        'identifier': 3621428,
                                        'width': 1994997782814274676,
                                        'height': 6235553318457338776,
                                    },
                            {
                                        'identifier': 9848850,
                                        'width': -1604539760859076990,
                                        'height': 3222578459895324461,
                                    },
                            {
                                        'identifier': 4917420,
                                        'width': 1348864100451243193,
                                        'height': 3390403127993796983,
                                    },
                            {
                                        'identifier': 8702754,
                                        'width': 2844427154946807722,
                                        'height': 7209531145546277388,
                                    },
                            {
                                        'identifier': 4087155,
                                        'width': -1598868962086492491,
                                        'height': 8210817595202288427,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3041354,
                                        'source_nw_x_pixel': -6359142035767348879,
                                        'source_nw_y_pixel': -8554892699960277676,
                                        'source_pixel_width': -2160511468316878026,
                                        'source_pixel_height': -3879207372651377898,
                                        'rotation': -6951094848627796719,
                                        'virtual_nw_x_pixel': 752441024,
                                        'virtual_nw_y_pixel': 460747759,
                                        'virtual_width': -644167064,
                                        'virtual_height': 1081677139,
                                    },
                            {
                                        'source_monitor': 4936323,
                                        'source_nw_x_pixel': -3587751922065109662,
                                        'source_nw_y_pixel': -5637924743040731261,
                                        'source_pixel_width': -7658544201179424958,
                                        'source_pixel_height': -4712233561763625347,
                                        'rotation': -5250446976581275074,
                                        'virtual_nw_x_pixel': -1827609018,
                                        'virtual_nw_y_pixel': -1632486913,
                                        'virtual_width': 127126974,
                                        'virtual_height': -1285251132,
                                    },
                            {
                                        'source_monitor': 7245513,
                                        'source_nw_x_pixel': -2665157242175065665,
                                        'source_nw_y_pixel': -961076712528597196,
                                        'source_pixel_width': -1593390179461508094,
                                        'source_pixel_height': -2529789206449760613,
                                        'rotation': -6959266558919156069,
                                        'virtual_nw_x_pixel': 173393783,
                                        'virtual_nw_y_pixel': 708702823,
                                        'virtual_width': -1531615426,
                                        'virtual_height': 1446941083,
                                    },
                            {
                                        'source_monitor': 5231666,
                                        'source_nw_x_pixel': -2288633227908678241,
                                        'source_nw_y_pixel': -3039064866277092968,
                                        'source_pixel_width': -4706733870863739700,
                                        'source_pixel_height': -4863601893739826228,
                                        'rotation': -5355901222251534742,
                                        'virtual_nw_x_pixel': 1302556834,
                                        'virtual_nw_y_pixel': 1264138353,
                                        'virtual_width': -1646737623,
                                        'virtual_height': 1458903546,
                                    },
                            {
                                        'source_monitor': 402263,
                                        'source_nw_x_pixel': -725885726426824129,
                                        'source_nw_y_pixel': -6766110319035313809,
                                        'source_pixel_width': -5718230852093848262,
                                        'source_pixel_height': -4461450825256701487,
                                        'rotation': -8813450853108605136,
                                        'virtual_nw_x_pixel': 857331752,
                                        'virtual_nw_y_pixel': 1892189165,
                                        'virtual_width': -933422025,
                                        'virtual_height': 947779569,
                                    },
                            {
                                        'source_monitor': 6357200,
                                        'source_nw_x_pixel': -2629952989363275653,
                                        'source_nw_y_pixel': -1951180096013626909,
                                        'source_pixel_width': -6371013292170501422,
                                        'source_pixel_height': -2813751243051179103,
                                        'rotation': -5949520725931078822,
                                        'virtual_nw_x_pixel': 288531155,
                                        'virtual_nw_y_pixel': 371778427,
                                        'virtual_width': -1240847255,
                                        'virtual_height': -231322711,
                                    },
                            {
                                        'source_monitor': 926625,
                                        'source_nw_x_pixel': -2911463298808783035,
                                        'source_nw_y_pixel': -1519959862109929020,
                                        'source_pixel_width': -7780905187652853977,
                                        'source_pixel_height': -1748992005359388605,
                                        'rotation': -2194734427563102007,
                                        'virtual_nw_x_pixel': -412297496,
                                        'virtual_nw_y_pixel': 24195474,
                                        'virtual_width': -1734403722,
                                        'virtual_height': 958484670,
                                    },
                            {
                                        'source_monitor': -360773,
                                        'source_nw_x_pixel': -4386901664205424422,
                                        'source_nw_y_pixel': -7889061862967017098,
                                        'source_pixel_width': -1526439920756525474,
                                        'source_pixel_height': -6255614113851836989,
                                        'rotation': -1715854806519165004,
                                        'virtual_nw_x_pixel': -857395914,
                                        'virtual_nw_y_pixel': -943564042,
                                        'virtual_width': -453158426,
                                        'virtual_height': 1326688747,
                                    },
                            {
                                        'source_monitor': 9258334,
                                        'source_nw_x_pixel': -2343475373887532762,
                                        'source_nw_y_pixel': -4374947353814103599,
                                        'source_pixel_width': -6750386904810485,
                                        'source_pixel_height': -2015185058826530277,
                                        'rotation': -1940129279957737581,
                                        'virtual_nw_x_pixel': 75598908,
                                        'virtual_nw_y_pixel': -241429345,
                                        'virtual_width': 1214948051,
                                        'virtual_height': -55982955,
                                    },
                            {
                                        'source_monitor': 8041240,
                                        'source_nw_x_pixel': -6123196567425782136,
                                        'source_nw_y_pixel': -7497914093172254155,
                                        'source_pixel_width': -329905017051621716,
                                        'source_pixel_height': -261261042442894177,
                                        'rotation': -3551685004429034184,
                                        'virtual_nw_x_pixel': 445953490,
                                        'virtual_nw_y_pixel': -1884756378,
                                        'virtual_width': -642796901,
                                        'virtual_height': -977839645,
                                    },
                        ],
                },
                {
                    'description': 'ſ$΄ɒOҸa\x7fҞɮХҧąÐϭ˳ѸӨʢŰК΄ÐҧΩϛȖѓЬǲ',
                    'monitors': [
                            {
                                        'identifier': 8491753,
                                        'width': 8470337119163170455,
                                        'height': -8780550172275270205,
                                    },
                            {
                                        'identifier': 6499457,
                                        'width': -3405911330344549561,
                                        'height': 4679008679418970614,
                                    },
                            {
                                        'identifier': 307395,
                                        'width': -9013051587039066727,
                                        'height': -287431606381908842,
                                    },
                            {
                                        'identifier': 1912851,
                                        'width': 2558720049198145789,
                                        'height': -7466791194103682009,
                                    },
                            {
                                        'identifier': 9193127,
                                        'width': 6457976404027080101,
                                        'height': 1910986492183582356,
                                    },
                            {
                                        'identifier': 5089067,
                                        'width': 6197708468749812014,
                                        'height': -78030455860215592,
                                    },
                            {
                                        'identifier': 3972223,
                                        'width': 2860415062888454170,
                                        'height': 4537787076204997237,
                                    },
                            {
                                        'identifier': 2574432,
                                        'width': -8837996078985068453,
                                        'height': -4129372309062210750,
                                    },
                            {
                                        'identifier': 1058575,
                                        'width': 4043590669435536616,
                                        'height': -5098843216389658851,
                                    },
                            {
                                        'identifier': 1093110,
                                        'width': -762209742114252931,
                                        'height': 8601604757025077993,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2413250,
                                        'source_nw_x_pixel': -7140782435761569543,
                                        'source_nw_y_pixel': -1617493480011542749,
                                        'source_pixel_width': -3104587814645451275,
                                        'source_pixel_height': -1396667135290609452,
                                        'rotation': -5541516175017146389,
                                        'virtual_nw_x_pixel': -1869799445,
                                        'virtual_nw_y_pixel': 270008126,
                                        'virtual_width': -465767501,
                                        'virtual_height': 1733042666,
                                    },
                            {
                                        'source_monitor': 6865064,
                                        'source_nw_x_pixel': -8995948206407137791,
                                        'source_nw_y_pixel': -8642953277472926574,
                                        'source_pixel_width': -577649794327613745,
                                        'source_pixel_height': -7689427468733585925,
                                        'rotation': -4362541450052044994,
                                        'virtual_nw_x_pixel': -848450918,
                                        'virtual_nw_y_pixel': 823855818,
                                        'virtual_width': -1439989846,
                                        'virtual_height': 67830686,
                                    },
                            {
                                        'source_monitor': 724293,
                                        'source_nw_x_pixel': -99633777714867729,
                                        'source_nw_y_pixel': -193691426499252909,
                                        'source_pixel_width': -5040847674835131050,
                                        'source_pixel_height': -4789836579369062493,
                                        'rotation': -1212107380716788436,
                                        'virtual_nw_x_pixel': -479457340,
                                        'virtual_nw_y_pixel': -1134585276,
                                        'virtual_width': -1012703014,
                                        'virtual_height': 648946572,
                                    },
                            {
                                        'source_monitor': 7947847,
                                        'source_nw_x_pixel': -8566524922603535030,
                                        'source_nw_y_pixel': -4842068469777395166,
                                        'source_pixel_width': -7487434553317769601,
                                        'source_pixel_height': -6237198963402995417,
                                        'rotation': -7714645741158199503,
                                        'virtual_nw_x_pixel': -1766304845,
                                        'virtual_nw_y_pixel': -1303012069,
                                        'virtual_width': 246664019,
                                        'virtual_height': 954000178,
                                    },
                            {
                                        'source_monitor': 6661984,
                                        'source_nw_x_pixel': -8874847711222175976,
                                        'source_nw_y_pixel': -8827135922340962729,
                                        'source_pixel_width': -6409056431707591832,
                                        'source_pixel_height': -7908276821956061549,
                                        'rotation': -2772933918304829249,
                                        'virtual_nw_x_pixel': 691117028,
                                        'virtual_nw_y_pixel': 745868764,
                                        'virtual_width': -1087121800,
                                        'virtual_height': -205081757,
                                    },
                            {
                                        'source_monitor': -940050,
                                        'source_nw_x_pixel': -6326480579907159849,
                                        'source_nw_y_pixel': -8106630742793079360,
                                        'source_pixel_width': -9136283910814735610,
                                        'source_pixel_height': -3282571235538165623,
                                        'rotation': -7468628190153194861,
                                        'virtual_nw_x_pixel': -1654602835,
                                        'virtual_nw_y_pixel': 1795507692,
                                        'virtual_width': 675272662,
                                        'virtual_height': 1433789770,
                                    },
                            {
                                        'source_monitor': 2999891,
                                        'source_nw_x_pixel': -2422194942412736504,
                                        'source_nw_y_pixel': -7269730995317950640,
                                        'source_pixel_width': -6695457387349858898,
                                        'source_pixel_height': -4718599812297719060,
                                        'rotation': -8808295278170998499,
                                        'virtual_nw_x_pixel': -126376077,
                                        'virtual_nw_y_pixel': 1523927269,
                                        'virtual_width': 739061275,
                                        'virtual_height': -1978014366,
                                    },
                            {
                                        'source_monitor': 4074160,
                                        'source_nw_x_pixel': -4227339916073357030,
                                        'source_nw_y_pixel': -5238962571731132733,
                                        'source_pixel_width': -3622168916962732157,
                                        'source_pixel_height': -3045979069410439157,
                                        'rotation': -2729876775665667830,
                                        'virtual_nw_x_pixel': -314249504,
                                        'virtual_nw_y_pixel': -803666540,
                                        'virtual_width': -1737000677,
                                        'virtual_height': -1428454092,
                                    },
                            {
                                        'source_monitor': 6362817,
                                        'source_nw_x_pixel': -5829726361667724549,
                                        'source_nw_y_pixel': -5806861428629445827,
                                        'source_pixel_width': -4679548290226056232,
                                        'source_pixel_height': -5805960650285379017,
                                        'rotation': -1436420870000464263,
                                        'virtual_nw_x_pixel': -1325414012,
                                        'virtual_nw_y_pixel': 358023824,
                                        'virtual_width': 1980100187,
                                        'virtual_height': -842514659,
                                    },
                            {
                                        'source_monitor': 2944117,
                                        'source_nw_x_pixel': -8960476151162675670,
                                        'source_nw_y_pixel': -3031891009404708065,
                                        'source_pixel_width': -6792097012538789763,
                                        'source_pixel_height': -3239061160835227827,
                                        'rotation': -1867138326755069804,
                                        'virtual_nw_x_pixel': 1435969397,
                                        'virtual_nw_y_pixel': 1840485124,
                                        'virtual_width': 767794842,
                                        'virtual_height': -1026793078,
                                    },
                        ],
                },
                {
                    'description': '˚ĜҞ5żˡ@Ѕ˄ФÎãoŚΑϏҔԙìǦĆ˻˙ʏɑЬʊ\x95īŔ',
                    'monitors': [
                            {
                                        'identifier': 5915796,
                                        'width': -643968535492716029,
                                        'height': 2365869270913304853,
                                    },
                            {
                                        'identifier': 2049316,
                                        'width': 6256136249075805621,
                                        'height': 3418381629425079421,
                                    },
                            {
                                        'identifier': 715449,
                                        'width': -106879553778899470,
                                        'height': 7167792891468207910,
                                    },
                            {
                                        'identifier': 4334986,
                                        'width': 7274549003020747343,
                                        'height': 3327954789618703974,
                                    },
                            {
                                        'identifier': 9863151,
                                        'width': 2741022581176107538,
                                        'height': 2918825491578689794,
                                    },
                            {
                                        'identifier': 7662747,
                                        'width': 3078058364396560468,
                                        'height': 8943945099865319651,
                                    },
                            {
                                        'identifier': -99765,
                                        'width': -8595968474410669934,
                                        'height': -3003339600832880870,
                                    },
                            {
                                        'identifier': 6627316,
                                        'width': -7979491516425742916,
                                        'height': 8961150820946113507,
                                    },
                            {
                                        'identifier': 3411697,
                                        'width': 7645241111024819050,
                                        'height': -1000630104377077365,
                                    },
                            {
                                        'identifier': 8526626,
                                        'width': -5300903315907827148,
                                        'height': 6339816209275302712,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -560426,
                                        'source_nw_x_pixel': -6971509270331300915,
                                        'source_nw_y_pixel': -3673630088732345481,
                                        'source_pixel_width': -3135902363003244206,
                                        'source_pixel_height': -7726036170365121287,
                                        'rotation': -1787888044063091794,
                                        'virtual_nw_x_pixel': 7063818,
                                        'virtual_nw_y_pixel': -1455444274,
                                        'virtual_width': 915992985,
                                        'virtual_height': 214185463,
                                    },
                            {
                                        'source_monitor': 5143774,
                                        'source_nw_x_pixel': -6152764582081060972,
                                        'source_nw_y_pixel': -3476567137588543961,
                                        'source_pixel_width': -96806855567946399,
                                        'source_pixel_height': -5404428252500405370,
                                        'rotation': -147198935682175749,
                                        'virtual_nw_x_pixel': 1170581225,
                                        'virtual_nw_y_pixel': -312483257,
                                        'virtual_width': -1161080138,
                                        'virtual_height': 1528073760,
                                    },
                            {
                                        'source_monitor': 8245072,
                                        'source_nw_x_pixel': -6285635290136702016,
                                        'source_nw_y_pixel': -3536987045053978951,
                                        'source_pixel_width': -3780247040241349710,
                                        'source_pixel_height': -342846804719591033,
                                        'rotation': -7960891567737262232,
                                        'virtual_nw_x_pixel': 20273759,
                                        'virtual_nw_y_pixel': -1687417807,
                                        'virtual_width': 1288031504,
                                        'virtual_height': 443768370,
                                    },
                            {
                                        'source_monitor': -524443,
                                        'source_nw_x_pixel': -1654398787671881857,
                                        'source_nw_y_pixel': -1187828270770340722,
                                        'source_pixel_width': -4849952805127084783,
                                        'source_pixel_height': -3506562547679312656,
                                        'rotation': -1280593440203074717,
                                        'virtual_nw_x_pixel': -1661124517,
                                        'virtual_nw_y_pixel': 383057914,
                                        'virtual_width': -638598236,
                                        'virtual_height': -533950055,
                                    },
                            {
                                        'source_monitor': 7396047,
                                        'source_nw_x_pixel': -5967565085086866065,
                                        'source_nw_y_pixel': -3288715199454712500,
                                        'source_pixel_width': -8897071366947411901,
                                        'source_pixel_height': -7415294837091319168,
                                        'rotation': -4960980954928674454,
                                        'virtual_nw_x_pixel': 1196710046,
                                        'virtual_nw_y_pixel': -932208561,
                                        'virtual_width': -1735394003,
                                        'virtual_height': 699896510,
                                    },
                            {
                                        'source_monitor': 8615432,
                                        'source_nw_x_pixel': -4601101663493778242,
                                        'source_nw_y_pixel': -4004949172054910756,
                                        'source_pixel_width': -1372811121294836632,
                                        'source_pixel_height': -4700870135801366255,
                                        'rotation': -6217532301992224171,
                                        'virtual_nw_x_pixel': -272079532,
                                        'virtual_nw_y_pixel': -300238284,
                                        'virtual_width': 1660091623,
                                        'virtual_height': -287107617,
                                    },
                            {
                                        'source_monitor': 9785454,
                                        'source_nw_x_pixel': -2694390684660330810,
                                        'source_nw_y_pixel': -2908796265687039908,
                                        'source_pixel_width': -3110596362188674824,
                                        'source_pixel_height': -599548150807320036,
                                        'rotation': -5189911939550845056,
                                        'virtual_nw_x_pixel': 578000095,
                                        'virtual_nw_y_pixel': -1971874606,
                                        'virtual_width': -162010620,
                                        'virtual_height': 1739329525,
                                    },
                            {
                                        'source_monitor': 4714227,
                                        'source_nw_x_pixel': -2990454120591099454,
                                        'source_nw_y_pixel': -8331477690662544900,
                                        'source_pixel_width': -3387328174870674751,
                                        'source_pixel_height': -2622072221884045044,
                                        'rotation': -3685435270829834928,
                                        'virtual_nw_x_pixel': -574191225,
                                        'virtual_nw_y_pixel': 1422777729,
                                        'virtual_width': 1666510651,
                                        'virtual_height': -266363035,
                                    },
                            {
                                        'source_monitor': 9549524,
                                        'source_nw_x_pixel': -3209592735077200563,
                                        'source_nw_y_pixel': -6576279443978370391,
                                        'source_pixel_width': -3727603389873954733,
                                        'source_pixel_height': -2477293792924961620,
                                        'rotation': -1770376820851834420,
                                        'virtual_nw_x_pixel': -115939932,
                                        'virtual_nw_y_pixel': 986018281,
                                        'virtual_width': -1672399093,
                                        'virtual_height': -1617025274,
                                    },
                            {
                                        'source_monitor': 2430348,
                                        'source_nw_x_pixel': -5108632138737058741,
                                        'source_nw_y_pixel': -250226198815437751,
                                        'source_pixel_width': -5819600448338466955,
                                        'source_pixel_height': -1833869008583658441,
                                        'rotation': -7021634306063472759,
                                        'virtual_nw_x_pixel': -992498985,
                                        'virtual_nw_y_pixel': -1556996426,
                                        'virtual_width': 1804335062,
                                        'virtual_height': 947737066,
                                    },
                        ],
                },
                {
                    'description': 'ώʚԥ0ʟԩɜβ҂˸HŪŃϜ~ȤωBһƒɃċ˶ɸϋƔǝȝƝƢ',
                    'monitors': [
                            {
                                        'identifier': 9648266,
                                        'width': -3757559571431250230,
                                        'height': -4600324919031907859,
                                    },
                            {
                                        'identifier': 6497205,
                                        'width': -8408048223659605409,
                                        'height': -2410272890031048856,
                                    },
                            {
                                        'identifier': 2471528,
                                        'width': -3370544087920747905,
                                        'height': 62101034226327979,
                                    },
                            {
                                        'identifier': 2364089,
                                        'width': -7342589771962469034,
                                        'height': 4333569883653478483,
                                    },
                            {
                                        'identifier': 1812865,
                                        'width': -1953800313012890342,
                                        'height': -9122333310517847603,
                                    },
                            {
                                        'identifier': 9457661,
                                        'width': -1255828316533873059,
                                        'height': 3828978703998008600,
                                    },
                            {
                                        'identifier': 4166814,
                                        'width': 398418572561372461,
                                        'height': 3794682468733830531,
                                    },
                            {
                                        'identifier': 3735908,
                                        'width': 5349872279716698606,
                                        'height': -8050772076962714764,
                                    },
                            {
                                        'identifier': 8287176,
                                        'width': 763231750790172877,
                                        'height': -8501418841376541877,
                                    },
                            {
                                        'identifier': 3402221,
                                        'width': 6858440031051589468,
                                        'height': 1252757122004890808,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6023855,
                                        'source_nw_x_pixel': -1923501497072639190,
                                        'source_nw_y_pixel': -8610007115298103095,
                                        'source_pixel_width': -6574622493763037284,
                                        'source_pixel_height': -7420854511355689924,
                                        'rotation': -6484040735955861188,
                                        'virtual_nw_x_pixel': -407651074,
                                        'virtual_nw_y_pixel': -251017313,
                                        'virtual_width': 1410837612,
                                        'virtual_height': 859324031,
                                    },
                            {
                                        'source_monitor': 5641798,
                                        'source_nw_x_pixel': -898768836237914181,
                                        'source_nw_y_pixel': -7634673705784703264,
                                        'source_pixel_width': -2870346125510735436,
                                        'source_pixel_height': -1911521322291133273,
                                        'rotation': -6910188616348181060,
                                        'virtual_nw_x_pixel': 659807642,
                                        'virtual_nw_y_pixel': -762584887,
                                        'virtual_width': 492566199,
                                        'virtual_height': 597410326,
                                    },
                            {
                                        'source_monitor': 630320,
                                        'source_nw_x_pixel': -6043393330789279174,
                                        'source_nw_y_pixel': -7647600428006297717,
                                        'source_pixel_width': -2790542232503182653,
                                        'source_pixel_height': -7274419604442335976,
                                        'rotation': -4363013268615308292,
                                        'virtual_nw_x_pixel': -1062886171,
                                        'virtual_nw_y_pixel': 449667283,
                                        'virtual_width': 1255812893,
                                        'virtual_height': 24880086,
                                    },
                            {
                                        'source_monitor': 5792588,
                                        'source_nw_x_pixel': -1039102965365448987,
                                        'source_nw_y_pixel': -2103536675362627233,
                                        'source_pixel_width': -3726732923614698559,
                                        'source_pixel_height': -7224480602533029340,
                                        'rotation': -5008578243355390517,
                                        'virtual_nw_x_pixel': -1223000052,
                                        'virtual_nw_y_pixel': 267634466,
                                        'virtual_width': -1627731598,
                                        'virtual_height': 530438973,
                                    },
                            {
                                        'source_monitor': 2544538,
                                        'source_nw_x_pixel': -7945710210348606797,
                                        'source_nw_y_pixel': -8686026696061622421,
                                        'source_pixel_width': -7435286852024520468,
                                        'source_pixel_height': -195419183777579031,
                                        'rotation': -1515758228876733617,
                                        'virtual_nw_x_pixel': 669744132,
                                        'virtual_nw_y_pixel': -509726508,
                                        'virtual_width': 931589900,
                                        'virtual_height': 1501804046,
                                    },
                            {
                                        'source_monitor': 7756069,
                                        'source_nw_x_pixel': -3068435427728961527,
                                        'source_nw_y_pixel': -360186066129127401,
                                        'source_pixel_width': -5466691405499029386,
                                        'source_pixel_height': -2843528322273862110,
                                        'rotation': -307822894150794096,
                                        'virtual_nw_x_pixel': 1483022969,
                                        'virtual_nw_y_pixel': 296714815,
                                        'virtual_width': -1842384599,
                                        'virtual_height': -994389256,
                                    },
                            {
                                        'source_monitor': 9797938,
                                        'source_nw_x_pixel': -5085366158943521752,
                                        'source_nw_y_pixel': -2925699116102657708,
                                        'source_pixel_width': -8818700447814191246,
                                        'source_pixel_height': -5298284780910124639,
                                        'rotation': -2017775459304228104,
                                        'virtual_nw_x_pixel': -1404018438,
                                        'virtual_nw_y_pixel': -789144411,
                                        'virtual_width': -375042535,
                                        'virtual_height': -899239393,
                                    },
                            {
                                        'source_monitor': 7972702,
                                        'source_nw_x_pixel': -8102818553830545171,
                                        'source_nw_y_pixel': -2116385608002296868,
                                        'source_pixel_width': -3082390422776485988,
                                        'source_pixel_height': -4455322986453766766,
                                        'rotation': -6240659677608929266,
                                        'virtual_nw_x_pixel': 842691553,
                                        'virtual_nw_y_pixel': 1136793649,
                                        'virtual_width': 774881686,
                                        'virtual_height': 155953783,
                                    },
                            {
                                        'source_monitor': 8029614,
                                        'source_nw_x_pixel': -3855814319288269046,
                                        'source_nw_y_pixel': -6962434340043576812,
                                        'source_pixel_width': -6660740297358077690,
                                        'source_pixel_height': -5966280386664449087,
                                        'rotation': -6462040847553707498,
                                        'virtual_nw_x_pixel': -1256356656,
                                        'virtual_nw_y_pixel': -1489454002,
                                        'virtual_width': -1201848148,
                                        'virtual_height': 340446525,
                                    },
                            {
                                        'source_monitor': 8347971,
                                        'source_nw_x_pixel': -4268841964792201653,
                                        'source_nw_y_pixel': -2731971659310013233,
                                        'source_pixel_width': -4926120373953953274,
                                        'source_pixel_height': -2717400390455191481,
                                        'rotation': -1446446618704233972,
                                        'virtual_nw_x_pixel': 853058007,
                                        'virtual_nw_y_pixel': -1620486487,
                                        'virtual_width': 615988128,
                                        'virtual_height': 1879594927,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 6359174,

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
            'request_id': 284683,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 104400,

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
            '$': 'Ч˨SәØľ˥ÇΣ_˸ËϕζǈȲԪɛőˊ9ӭъʱ\\ɌɊԩȆƫ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7824278706597918550,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 610424.1663958413,
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
            '$': '20210413:001817.137223:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ЏӢԒӟAǥЇ¯ԠϩΝȱӞ2˚ԀϡԠȊӌғΰѝњΤȇώřʶҐ',
                'ȣҫǁρ҅ʍGӢгҚ°ѤйԗӋôѽIVΈƏҬԊśˈϑ˩țυΈ',
                "ŗǴʧˆҬĸϘЦЍɐɚǁȉӭίȕҳ¾Ӈûѹ˥'ЪGɌоЯĄͱ",
                'ŝ˕ԃЊєų¨ˬһŶʐɫԎŭFś\u0382¯ҤҡЂΔơȷ÷_ˉ¢Ζп',
                'mʬа\u0378ͳӆ:\x84ʘåĺвМȰʵǬʰæƭ;<ǆэöōĨã¤Ŵ¼',
                'ʍ\u0380ŝйÐǮǣĔ˚ӧäЀǓ\x97Ғó´\x90˳Ѓ\u03a2ӄȹ˗©њÃgBʃ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -1866122531300938309,
                -2407398389297562618,
                5042904602728569080,
                7803201259687193080,
                -5780367704104424476,
                -6645272635784439587,
                -6213855054771379507,
                -6792172325124433979,
                3338752794047070813,
                -7041499938355869988,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                406287.1442529176,
                612535.3288340885,
                273099.39942402113,
                927340.2461879093,
                -69188.9779272568,
                939060.454607251,
                921122.7343579702,
                893319.9875063811,
                426114.4469130613,
                972711.6722036013,
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
                True,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210413:001818.231023:+0000',
                '20210413:001818.249963:+0000',
                '20210413:001818.266661:+0000',
                '20210413:001818.283996:+0000',
                '20210413:001818.301019:+0000',
                '20210413:001818.319616:+0000',
                '20210413:001818.336911:+0000',
                '20210413:001818.353614:+0000',
                '20210413:001818.370564:+0000',
                '20210413:001818.387625:+0000',
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
            'name': 'ɣFçǚӰɮѽĤмϒƻĴǆȭԨdƣȱόǴƮȟŎТѫ˅ϵͳØϸ',
            'value': {
                '^': 'string_list',
                '$': [
                    'ōϐϧԃßʬԍŶƭӰƤ\x95џҦĐʑÄ҃Ѝ=āΟЂͱÜɰǀϽˈʙ',
                    'юϦÚƵʭѠđġʯΙӃ\x86ƠƤЉ<цьӥѤэ6ɬÜʛĘ<ʮźǅ',
                    'ŤΠÂѨǈƜʞſĎϻʜ©ЃƇƹŸуʎǺ¿ӓӣǹ3ƤʾʿĴ Л',
                    'ҍQϵǢӚέȈυѨƧÐđҘΐðϾуνƉϹUԮƧ³ǰ˕˅h˪\x8e',
                    'ʒшdΞδҝΊ\u038dƳ§ǚˊȱŪƫΒ\u038dÅҫϞҝɎ~ӑ˚°ŘϚӍҒ',
                    'ұ˪ȿħԧǝƁҎ΅Ƣ\u038bϹǇͷƊCňЁθӨӡɌȶуκѯ\x91Ӱҙʕ',
                    'ĭͱ4ĩϲĤɈ˨Љó˩ÆϩǱӯżҚɜзͲėȉңȾӑҽòͰҐӝ',
                    'ˆD?ӔʞӨҤƱ˘ӽʇǥӷҮ5РʐoЉƽKɖǬȊ\x84ɞ͵˭Ŧĥ',
                    'ѝũʞͷѤȭȕӦбщĐ΅ŲʐȒӒƙςĘúӕʅйӄйȂƇǲĄǦ',
                    'хϞƴѭœ\u0382ҺȾмĐ˙ΩʤʶыѼȀǟˉÏиơЌїӟΦ\u0381Űȯ;',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Γ',

            'value': {
                '^': 'int',
                '$': 1295191655622344545,
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
            'catalog': 'ƽŢǃґˆˁѥў<ͰŊЁ=ʷˋŒɮѥɮ',
            'message': 'фȢЎϑϺwǈʱϴǑϤёΝ\u0379ò˞ν[Ӎ`ȏɤ7\x8bϯāӮĬЧt',
            'arguments': [
                {
                    'name': 'еȩǹ\x9aыΎӖЈǙêŀ±ĖάЛÍΐΖΟľïĽϋσ^ҚΛŻǢș',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -5768543881687780631,
                                        -8512769999599114924,
                                        5956184473994709320,
                                        -6253843116502075462,
                                        6998530904008440452,
                                        9213901128609978985,
                                        -3441072644444388592,
                                        -6999819333357239618,
                                        -4878289593169477976,
                                        -5545915348639531273,
                                    ],
                        },
                },
                {
                    'name': 'НʿѺѳŜҚϯϫ҄ıǴӬȭԟ',
                    'value': {
                            '^': 'int',
                            '$': 9032889620120657127,
                        },
                },
                {
                    'name': '¡ԉЪîɩ5ψˑдĚӍʒʩ©ɫŇҊГ¹ϠΖüʊɊΝĨ\xadȝͼϴ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ϋƪħρ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:001815.320072:+0000',
                                        '20210413:001815.337087:+0000',
                                        '20210413:001815.353901:+0000',
                                        '20210413:001815.373555:+0000',
                                        '20210413:001815.390596:+0000',
                                        '20210413:001815.410024:+0000',
                                        '20210413:001815.428726:+0000',
                                        '20210413:001815.446246:+0000',
                                        '20210413:001815.463483:+0000',
                                        '20210413:001815.480925:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Tϥԭ˴Ǫg´ȺӜ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -2844697631436921588,
                                        -8721138754234801319,
                                        7240788744206128044,
                                        -4983605749007951992,
                                        -6400055156431252706,
                                        -9083590092926439805,
                                        6716501769487109224,
                                        -1980707857774259413,
                                        7781901990661970374,
                                        1937378039627719799,
                                    ],
                        },
                },
                {
                    'name': 'ͱˑƈǚɒøȢüΑӫɹ\x8eƀԪƆȘӏŶƌ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ƞśРʗԃǮ҇ȚȔúoVʪԉƅʒǰλÕ˶ůņ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
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
                },
                {
                    'name': 'ϰқśӸQАƒrťԡӺ¦ʵu(mó%ԮSʮЙӸ\x92ҪFж!ңʨ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -425944485108624076,
                                        -7214303123385778424,
                                        5377398965697311881,
                                        -3952815206946720142,
                                        -9133314598923818252,
                                        -6500352376088771987,
                                        -8751215702632828189,
                                        7265895751573559670,
                                        2235804437395575166,
                                        8367254527905161780,
                                    ],
                        },
                },
                {
                    'name': 'ƱˀЖƾӜʲɶ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ȓĕʗʌȅǈ$ÁɌŝДŰŪˣҹjӁӬЗ϶ȏƷщ҂ùӆƯʲ£ǹ',
                                        '¥ʣƕŐƙ\x99ϵόΖԦӻʍÄʭĶƥͲϫϦMӓˎƩҟéɔĉѵȅʑ',
                                        'сӔ΅ʰҦ˔ϐƻ˻ҳԞºȊŶbЀ ϭζƁЉʐӣɔǦҥδμǁȔ',
                                        '\u0381^ЯѯяҼIR˪Ѵ´зЛӵȌơΔΊЗȖԌԟRь LҷȚљԭ',
                                        'УӞ\x98ˉҠАЕҘҗĿßψӀȣͶèɁҎňˏ\u038dþϣгƙӚϲЩ\x9aϭ',
                                    ],
                        },
                },
                {
                    'name': 'ƩӠ˞˾ˏJӹȑǪȎϵʀΣǺǁ=Ҩθu˫ЍгŝÑϱ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ґî',

            'message': '2',

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
            'identifier': 'ƙ˖Ùƃ9(ӚƌχöȠĦ@¨ҜҚҊǂЏƓƭˁӺѥ,ĒΒŉԅÆ',
            'categories': [
                'os',
                'network',
                'invalid-user-action',
                'access-restriction',
                'invalid-user-action',
                'access-restriction',
                'configuration',
                'file',
                'configuration',
                'file',
            ],
            'source': 'Ҏ¨сƞзȌɶΚʳʅȼЋˤǔtλóѦ÷΅ɸ\u03a2çʚéſԩ<нɷ',
            'messages': [
                {
                    'catalog': 'ӐģƩфȼɥðҟñʛɇҟʨ¿Ӊљ\x9cџԝμƓȧƭˊмԖ',
                    'message': 'ьˑϻƭʜ\x95f\u0380ňРXʿϴҍWΝŊ\u0379ΓѣʭÄȧūſϒϤзƏҽ',
                    'arguments': [
                            {
                                        'name': 'ƹӤͻѪӱTӡфΧ¸°ӥʄƽũȢrǎŷϵ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȋэ΅ӉȲҟӊϒӊŶЫƱԁғџҫсǣÞƭ˴ɱҢϩхĿ¶ƍµѥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001757.928911:+0000',
                                                                            '20210413:001757.946669:+0000',
                                                                            '20210413:001757.968954:+0000',
                                                                            '20210413:001757.991964:+0000',
                                                                            '20210413:001758.012170:+0000',
                                                                            '20210413:001758.032772:+0000',
                                                                            '20210413:001758.054896:+0000',
                                                                            '20210413:001758.075174:+0000',
                                                                            '20210413:001758.096221:+0000',
                                                                            '20210413:001758.114202:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĬľżʌɋÆ©Ԓ҃ʠȲÝώЄ²õ_ˢĽʹč;Ƨ\u0383иΑίˉ˼ʐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2056091177539372460,
                                                    },
                                    },
                            {
                                        'name': 'ȴɁ\x92ϰԈƮŀҐǦɫўƍĨѧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2926662084808428040,
                                                    },
                                    },
                            {
                                        'name': 'ϜÃϫƘČƉƳ˵Ǳȉғϗ`',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 250150.97059837333,
                                                    },
                                    },
                            {
                                        'name': 'ĒȀ*Һ/҂`ҋțԬϛƖȱĠϐÓźҦ\x8cǊԠҪïŏǦȐεƦ^k',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -60193.25818289021,
                                                    },
                                    },
                            {
                                        'name': 'Ǐѫ}ŉȦтťǃӈƜȎǄЇŭ\x98BϞȏ!ƒҦßǘʴӜʢéФĸɔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 94396.95016402553,
                                                    },
                                    },
                            {
                                        'name': 'ѠʱYéÐɱŹʱΎΓG#¼ϲŊȒǬ*Б§',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4653597336523343497,
                                                                            6994720137670671946,
                                                                            -7618216956964183348,
                                                                            3426689640634693212,
                                                                            2612271574900449788,
                                                                            924196507021850112,
                                                                            8343869200443974106,
                                                                            -7214325758204614331,
                                                                            8715378921946235388,
                                                                            -2587467704768310534,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'šћԔ҄',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŉŐȲ҅ԭӴӯ±ʕԝʘaǯϳķƨőĚÿқΙǮ*ɶˠũǥĴӪʈ',
                                                                            'sЃ˶Їƭė\u038bŦΌũęğʷҌϳɃQ\u0383ӰӘжɦʵ\\ŝӢƂxŨ\x98',
                                                                            'ƻζШҚ^ԠŹɖʼAɑăøԝɮ˼ˎђƳCҜ!¹ğθҭҜʺӀM',
                                                                            'ȔѲȡʛдΙԈϹRВĺɝԔÈәˎKҊƯólȁƴĈ˧Ļǌ\x8dϢţ',
                                                                            'ҲҶԞϮήǇƕƩʀʪѵΨʣE[þї?іͲӿɏҳǢâϨ&/\u0380Ͼ',
                                                                            'Ю҈į9ˉ³ϊҤŃ\x83ћ҄ӞŊΉȪϐ\xa0\x85ѦҴʸʁКƿѵɗϏÔ%',
                                                                            "ʹӚӔԕ\xa0%ʈХ1ˢǁԏƸϳĢ.ɨΩĝŴưԞƴѰŎNԗł˰'",
                                                                            'ҹÂʡÔʠѱƫȐʹпӍςËŮΝ¿Ȩ\u0381ԖрγțʷҞɑø\x87ϹϦƢ',
                                                                            '\u038bпĀЂ\x84ƸԮӪüȾѧȗϼ˂˝ʂ4ҤNМξaɯɠàǊ«ȀɮΙ',
                                                                            '˗҈ϮӟыS˅΄ǥΘˤЦΜÀ˦ӑƎhЦe\x9fúƪģǭĽśδ\x91ϓ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӡћαǃγâ˛Rǩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 56420.249189436785,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҷЂˤҧˏȇì\x8f\x7fӋԄŴ\u0379ζαЄǸÚǧԤÈʀǵɲ\xadΜäwϭԀ',
                    'message': 'ʡѪ)6ωǾȇĨċшĨǥűϯɾĩũԭɫςȕĝ΅ΊѿһБңÄ\x96',
                    'arguments': [
                            {
                                        'name': '˛Ӿ_ȅɝY¸}ǅԩǴʔӛɋʈHΗɚƈŉ/ǇѮƺȶԑɋN',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 59576.46055175876,
                                                    },
                                    },
                            {
                                        'name': 'ғŃЬĝƵƏо¦ҶӖҵʀΘƧЫŌв\x86ƌͱɸöťĺ,',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001759.472900:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƓÇрЃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4029935153094067067,
                                                    },
                                    },
                            {
                                        'name': '\u0379ЀĞʾȥ©Ɨѱƽ¹êӺјͿǌԂĝʦȠɐϓуͻƫG',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6021693961935407830,
                                                                            3941896293154369833,
                                                                            -910693912546259903,
                                                                            2490338015008041492,
                                                                            -6216819233101057558,
                                                                            5929953315674584566,
                                                                            2690091008696536966,
                                                                            -7358484153411934235,
                                                                            6518440749168360889,
                                                                            4078095637770667480,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѷӭ«',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001800.040435:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĤʥΞŽDӧҹʒ¬Ŋ\x90ψƉщη\x99\u0383XҀȬʧѨЗĚʰ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5813157245794471260,
                                                    },
                                    },
                            {
                                        'name': 'ĭҍƛZÔΊΈӢIǵϨҒǒ¥ΏǺˍ5ˑѤҽњΦΈԊӝɖѻdь',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 629436.2790481569,
                                                    },
                                    },
                            {
                                        'name': 'žНĬȋΏψӕόΤŝyƲͷҮԤѲѲԛϐҝDѺˀʱwĎ3Б\x91Є',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001800.286108:+0000',
                                                                            '20210413:001800.305164:+0000',
                                                                            '20210413:001800.324987:+0000',
                                                                            '20210413:001800.343338:+0000',
                                                                            '20210413:001800.360778:+0000',
                                                                            '20210413:001800.381817:+0000',
                                                                            '20210413:001800.400441:+0000',
                                                                            '20210413:001800.421164:+0000',
                                                                            '20210413:001800.438421:+0000',
                                                                            '20210413:001800.454708:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '^h/ұɩƟ\u0380ĿǐŁDΒƥЕԌdʟzȜҜȬЄҐΞŌ˭кϛɞӜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3446066266128375869,
                                                    },
                                    },
                            {
                                        'name': 'ɖӯ:nЕSċ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϕ½ηͲӿ:ӠѴ¬\x98ӛͺұǞҤҳǊ˹Ǝʷɼ҇ȯСˬqȮǇȦѣ',
                    'message': 'ɽҡ˅ˌӐăǄɾƔİɕȷTůʂϻɶ˺mƄӒĒ\\\u0378ӊӪ˚Țƴʉ',
                    'arguments': [
                            {
                                        'name': 'ʆǯЁŵ˰āʁÅϹҕȑíӔʱӅ҄ʊØȬ˰ѮȪ¼ƾԨŁǘČϠʣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ϥ\x85ǓϞ\u0381Ø',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 59777.87008510076,
                                                    },
                                    },
                            {
                                        'name': 'ͷϭĥœðͷɜΕԁƪFɔĉįԄ×ιзIљҼҜκȋҜѴûˍȜȑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɫˡëŭϒЃЍѪԇ\x80Ԉ\x86ҧνɏƚӿWQM\x93ɍɒƚǾӼԌьѷ˷',
                                                                            'ǄCф˶ϸQŻϺĩưҐΰƷә\x86϶ɦȆ\x99Ʌ>QïѦƘщçǌӥʍ',
                                                                            'ƩшχҠŏϙԌȉЁϐΓqİˎмŝ\x86ϩͲŐϼøXǾϫȸѳɷƈÄ',
                                                                            'ò\x8bȨƐӑ¡ГˁϭŉӺũЦͼɄǛ˶ŲАə\x96ϣдʴŋ;ЅīȦӠ',
                                                                            'Ԟǚ˧ƦҘĦͻʯýQǒ˶\x8d˙ýΠʋπѣѬŔ5ӸgО҇ǭʻ΅ˎ',
                                                                            'ͼт\x9bԮ\x9aˍ)¶Ǎ~ϋưʃōʽʄҕ˥rËђ΄ƖίљƑɛųΣĕ',
                                                                            '\x9dÛǢǊǡòçɼаéȊҞÏ΅\x8dƟĵ҅ԄõϨiўǏ\x84ЂɱƮ҆Ơ',
                                                                            "ÍŢԩxZԆǆɉʹӲęυǘɥӬҍύďòх'ɫưԇJЌʸИҞͱ",
                                                                            'ɭσĴɠӭԘѿԋӫŏ˭Łɢй`ʻӶɭϟ(OˈŕҕɊüʡҀŴŶ',
                                                                            'iǔD˜ɼǚƬĮǰäȈӏǦҵƤǣӇϠ\x82ȸΥˤ˧ԥĵ˂ѐҴ\x96_',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'İҦÞԈκņʠƸʕϸȟğȾħŧȪʪĖFԫόèĎҷ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 329743.95023515675,
                                                    },
                                    },
                            {
                                        'name': 'Ԡ/ԣ,ƱЋŏПǛ˲Ѯĉ˥ȷˈϦɎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԩǻ϶ơӭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÑАķϺƪŒ˛\x903ξ˞ŸҎ҇¸ƏϬƙ*ƇțʅȳʕɍȟSǪ?э',
                                                    },
                                    },
                            {
                                        'name': 'ǸÐŮ҇ðďYɷЃǺΩ˻ĎśUм\u0381ɕю%>ƠΪ"ÎȲԍЗӬʬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8341267196742379139,
                                                    },
                                    },
                            {
                                        'name': 'έϔʧκKɫæϕȁҿШǝTȔYʥӦȒʿƲĵoɇƿӝȪȄԛзV',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            518508.6314126416,
                                                                            126499.09498888152,
                                                                            962221.7335707324,
                                                                            857506.7966560894,
                                                                            271084.6949455958,
                                                                            557766.0577170736,
                                                                            -78121.7647803032,
                                                                            936577.2255332388,
                                                                            470654.4907627419,
                                                                            998552.0337209776,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'µǖЖԪĔĸϢʥyɏƗ˱5Ɨ¨Ȗ˪ԀЀɀъ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001801.992187:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӃʵΒɰжͻƪϓļгɯŁý«ҊȉƾŀϨҀүӯĚΖф¨źŜʵā',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001802.062467:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʅŉѺʫĕDÊΒ¿ÆƎ\x8eѵͻǱ\x8bśίшΠҾƒɶ\x95gԅȟϱžӅ',
                    'message': 'ӞзÛɿ!҆ǨҿѶϑӖÝκˇԦ(ΥȰҗM4σԧҠĤćϡѥȆХ',
                    'arguments': [
                            {
                                        'name': 'Ҹԏĉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8624073269159698626,
                                                                            -6832187067393553228,
                                                                            -5452287839411617227,
                                                                            -7987147076040945066,
                                                                            -1616358493916239640,
                                                                            -4637594689796390870,
                                                                            3074055131974579396,
                                                                            5691171137244034181,
                                                                            4460343880866654250,
                                                                            -3042317966629892364,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'νˠķӻэȮнċůÒ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7193959990225751929,
                                                                            -9180048271824426441,
                                                                            7040452761192662025,
                                                                            -1759075040519163197,
                                                                            -4656375512150836182,
                                                                            -5755710018819838342,
                                                                            -2084013292880582054,
                                                                            1950050765889429278,
                                                                            -3495211320317550948,
                                                                            8454695126368006269,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'рȦûǐӔʣНĻsɀγƠșͲҁjəyřʓ&Ϣˉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 449992.6298977728,
                                                    },
                                    },
                            {
                                        'name': 'ÆмӄʴȺͻľӺΐ\u0381ϐϰѾҦ\x9a΄Ï',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 904101.5883523355,
                                                    },
                                    },
                            {
                                        'name': 'ʸâĜ˶ǽƚøљӒи',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'åľљѶʑҮS÷ыԁ˻ènɤӭųǗG¬ħȌϳэȼˤGʖĜőˡ',
                                                    },
                                    },
                            {
                                        'name': 'қƇԐŻҶΈѶ[ͳęΨ˱ͶâӃɵĕÚӜӘÙÒķľȠúɇҲ˜ś',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001802.932121:+0000',
                                                                            '20210413:001802.943982:+0000',
                                                                            '20210413:001802.960275:+0000',
                                                                            '20210413:001802.976368:+0000',
                                                                            '20210413:001802.993060:+0000',
                                                                            '20210413:001803.010782:+0000',
                                                                            '20210413:001803.027406:+0000',
                                                                            '20210413:001803.047066:+0000',
                                                                            '20210413:001803.064540:+0000',
                                                                            '20210413:001803.082622:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӽˊrμòdЊЬȚҿǕ˧ŏѽӉ΅κӊɈБS',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001803.168515:+0000',
                                                                            '20210413:001803.185079:+0000',
                                                                            '20210413:001803.201952:+0000',
                                                                            '20210413:001803.219315:+0000',
                                                                            '20210413:001803.236428:+0000',
                                                                            '20210413:001803.253275:+0000',
                                                                            '20210413:001803.270463:+0000',
                                                                            '20210413:001803.287598:+0000',
                                                                            '20210413:001803.305759:+0000',
                                                                            '20210413:001803.322554:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '`ʋΙԢMϤʑìϾҼ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3489610054523776662,
                                                                            -4519699960037781704,
                                                                            -7670381599347206441,
                                                                            -3708534436441378045,
                                                                            -3859343474475187264,
                                                                            -4001993763072275044,
                                                                            -4557508245243602237,
                                                                            6712973606989695333,
                                                                            -2124042663861223824,
                                                                            8890506477156293345,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӏ\x88сӣзȀòɃǉг҆ȱбДɦԅȧWÖѸȦ˱ѕӡϮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4757946572387637289,
                                                    },
                                    },
                            {
                                        'name': 'ͶԖԓĭʜƘОJѻξ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001803.742235:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɫɰƻǝǇρԥ˴ÈȎКɬ/˲rψ½ӄɱĊ',
                    'message': 'ÎϿϤȐβĵѭʡԘǵΛǃ\x98ſuǀǣ҇Ƚ\x82\x8eɪҀөҤĸɵDȅΨ',
                    'arguments': [
                            {
                                        'name': 'Čξ#ƦʴǬčҾԑǉѷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȝ.ӟƝґҞ¶ǞˈоȯƊͶӁήǦ\x9bʊzъ»ÇΌȰҫɌĭҋȃϳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001804.184549:+0000',
                                                                            '20210413:001804.196566:+0000',
                                                                            '20210413:001804.209706:+0000',
                                                                            '20210413:001804.220814:+0000',
                                                                            '20210413:001804.232485:+0000',
                                                                            '20210413:001804.245029:+0000',
                                                                            '20210413:001804.257698:+0000',
                                                                            '20210413:001804.269506:+0000',
                                                                            '20210413:001804.281061:+0000',
                                                                            '20210413:001804.293869:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЊˆʟǕвӄУϹΊʝčҝNɍͰȾƍ\x8eȨЛǒ\x8c˹Ƹpϸȭƣ˜',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 587993.8201760844,
                                                    },
                                    },
                            {
                                        'name': 'ӽВÒ²Ǆˢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѤWӠһåȐŧɶƤŲҋӞҎºμшϑòȔӁȺͷψ¾ʫԎĊѷʎԈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            357878.2999046714,
                                                                            952808.5691064154,
                                                                            478920.7275522759,
                                                                            705326.0429578659,
                                                                            998294.0051893892,
                                                                            172458.8627223294,
                                                                            563049.2910342482,
                                                                            825715.6780541579,
                                                                            227253.3489494868,
                                                                            -8433.099270944731,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9dļȿϧӿʫɹԉȨƌÙʍǏȃ3ʚƵʗԏϸ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'ĻʘΕʘħԗѭȴňʌġͿĩг\x91ÕŜʇȤҡԔƵˁæώӣѷҪʄǛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2405540545076046207,
                                                                            -7195555138946633173,
                                                                            -928944404679250853,
                                                                            -7645060334544053975,
                                                                            5904639618102393194,
                                                                            -4187588679186434433,
                                                                            -9044613471819497591,
                                                                            6867197486549910136,
                                                                            6555558371862444744,
                                                                            7218595785691156342,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '$ϑ9',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǿɀҴ·(\u03a2ǁ˞ӟɮǴςģҁϭûӪϖ\u038dЅоȆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -43769.624504654144,
                                                                            249678.44945546193,
                                                                            704387.4156043425,
                                                                            465350.2566783619,
                                                                            -94665.8235202462,
                                                                            754293.0553017937,
                                                                            357180.1164930352,
                                                                            9038.804723124005,
                                                                            961739.6942607865,
                                                                            -18507.127430770866,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѻҲοΤɔѡ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɲʑŢºÎЅŖŗÕɂyи҆Ҋϳ˕tͷΏȨĒ˳˶ƦҐǼˣǺ(ɚ',
                    'message': '}Ұą&\x8bñҬȕ_ԚǄͳƞΣы¨ĕЧˈЈʍżȧӴƻӡ\xad\\ʻе',
                    'arguments': [
                            {
                                        'name': 'ȤƺʥЈ\x86ӝҔ϶ӕÚЇɂѯ\x8aӞ{ȹ·ʔԬ˳ȕҐǧɺɅπӃƦμ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʽʆӖČǵԄļ˩ŝΣѯԣTҾ=ηƃѺƉŢɗλоԔėʃѽʿȁζ',
                                                                            'ɵϛöϳ©ӫκЎϩƷȐş˺х˄ҦʹpϐαξÙӘϲ˔ƧЖӢKa',
                                                                            '1ϼŲźØѬΉшȥŶɘы÷ŵϘ˱Ȧ˾ɭϝνҤԅǳǰӾΙϿȂӤ',
                                                                            'ǃčƷĉ\x9cÊѳ\x9bü˳ԖФƙмÆŧƾƜǽýуĢǥЀї˗\x84Ƚ¡Í',
                                                                            '/ҶģÃʥҚζƪƫVлĜӕÁӈ\x8bҕʊΏǾNҷŅϺȞˏʑιəӆ',
                                                                            'ŕҨvҖ\u0381˩ԝȵɜɶčдŎȢȻӤїƮБPʗˮbLƲ҃Ɣʤȼ҅',
                                                                            'ӯɈΈeʨcOÇӞ\u0382пĚЍįBӓҟȼѫҹͷˀԚɔƨιπoƸԎ',
                                                                            'ƉΡƍϙӊҫȽ҄c(ƀɏŮΰǆη\x97˕ʺ7ʤ˺\u0380ɱЋǓԥƒҐý',
                                                                            '҂Ӗӑ\u0379ȵ\x84ĔÉ҄ӳҨ·ҮГͳϸѧΚïʺũԊȦӄŷϩÞјFD',
                                                                            'Ő½§ԅѴђЬ}οΠЫѺˊˬɌМĬ½^ƽmŸͽɵđÝȌƃȢȋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Зɋ\u0382Ԋν@ϔХGіɑѬöƐĖȟéԈϨÜҁʋƹϱϘƬvʐѤÍ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Įе\x89Ĭ]ȥ҉Ђ65ȒѹζƢҲˤҗbĄΑ\u038dԎʺǦҾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 60668.90998456499,
                                                    },
                                    },
                            {
                                        'name': 'ńбҋқɭμØɹůϝĸ£Ͱɿʃʀŧʖ¡ʡЫҜϲϓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 339139.7033201983,
                                                    },
                                    },
                            {
                                        'name': '\x8c',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1745552316054988593,
                                                    },
                                    },
                            {
                                        'name': 'ӀʸƻÐýԮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001806.883124:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x97Ýu\x8e\x82ǌȻ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001806.954260:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x88\x8cҾťѤЌƺԈđʇƂéêĀ\x93ϔ|%Rι°ԂԜȚȺ6АɎǁϲ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4556094028526300716,
                                                    },
                                    },
                            {
                                        'name': 'Ч\x91ȤΘǀƛƶДДʹЧȶҾʂԪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1739532632297476013,
                                                                            -6932704974826387319,
                                                                            -6931027785054271101,
                                                                            -539308296023875562,
                                                                            4920572151074567935,
                                                                            -5831580581012979362,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƿ\x87ϏйįíƈҗӼόǖӌƞˎWğȐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ұ\x93ϘϽ˒\x85õǖǐɼʬŧѸĥӶȍ\x9fŹѹʻęȩōοЙƋҽɶǭš',
                    'message': '҃ǸƗɿɥü¡ʣϚϢŀʡÃƮ=ϻɪnҖĖ˪ҁŅŌећβŁȭҘ',
                    'arguments': [
                            {
                                        'name': 'ǋùӟҖζҞɬЉ\u0380\x84ʌêȡȬԊϩȕȦюȀƔ\x90ԍғϧ҃ʄ;ӣι',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001807.373620:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ҧ~9ȃӓđXɯӥͻҊ\x9d',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ФŇƎGÉӄÐ˕Ƭʅȫ҈ÈқATƈȫɦ:Ċ˽tҝԖȫӜŤӯΕ',
                                                                            'ѦǆğġψrȨ1Ҷɓˈ\x9fǛßÿ"ˋѷŗҍkģnņѱˢƨňϜτ',
                                                                            'güǧƝŗ˪³ϩ˷WɪϥʭĔӴκsϊȁԦĮȃЃΫҖέɱƻҊҢ',
                                                                            'йľ\x97ÿśДĴˊ¬ȉĆɡѯ҂¼ϽŁǪϷΤ\u0378ΥԆiͳϼûǵɣɹ',
                                                                            'οƎӳ\x98цu\x86ЛҒļʿѹȖǯͰΒʽӢӊɢӚʆԋgłԄ¥ˏǬϡ',
                                                                            '΅Ѵ\x81êѷˁȟƷǂљԞǔƸĝɊǨŉǑԝģŽγɜĶѻɶģԁʥ\u0382',
                                                                            'ʀ\u038dζXǪӺöȤŸыZǯƯˇϧƀɤɤµƣɮ˔Ã˛Ӓōѻѹũ¸',
                                                                            'LɧŜɒЩҒǫмԋǢǕ˵МͰŵɽτˍĖMҹ´ӓΊȭĦҩҿɎĊ',
                                                                            'ϻӷ×ЙƍҶ<ҘΫŪǻfҕƚÍчɀ=ҼѲ4Ǉ©ìʣǫΓˣƧĻ',
                                                                            'œƶͳǋȯīȼ£ҔĴҦʹȻɟҨBzʖеοɇϮǳѪКѐԛͼʮԈ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˮΛSшEґͼ¤ƐʡKǥ˒Ƅџƚ˝ŞÜȚˀэů˳',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¬ɉ\x86ҊЦԨҥνԋ½ǴǠλôơ¥ǻǷȒǕ|ЗčҖɳ\x9fňѝđƮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1165209297022384568,
                                                    },
                                    },
                            {
                                        'name': 'Ҧă͵ɢІĶѷȂɯȁӗε·ЙęΊͿͲƄцɲЗЖ˂\u0382',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 889187.4140916832,
                                                    },
                                    },
                            {
                                        'name': '˄ҢԍѮŝхöɤБ¡ˑǞϫѯVý\x85сǩsǣτρӖҥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϕǝǌʴǙʱ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 714241.5186502368,
                                                    },
                                    },
                            {
                                        'name': "ȕˠ!²ƼӀˬȂŧͱӕΘнľӞʟƊ҂ԇǧǟӐӁˍ'ΤҥҲƴˡ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 918919.488987624,
                                                    },
                                    },
                            {
                                        'name': 'Ҁ˚ɕǆʴɢͺɍπɕſӍϔΙ˵ȱƭǇ˩ЂʐӖЂȘѥФĐǜͱͶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 620052.3633290869,
                                                    },
                                    },
                            {
                                        'name': 'ϸ+\x9eϷĥβʚɬѝƱ\x8dʔ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Đ¯ϓˋK˦уĨһкÍÏŜԘϧļǺН\x84ńʈЀҘëϺk¡Ϩīһ',
                    'message': 'AƂśƅIǒQȧĮϖԀƪӻȳΈϧ^Ѧǩ&ȿʫϭɋԁҎé˚үƺ',
                    'arguments': [
                            {
                                        'name': 'ˢEÝзpʔ\x83ԈұϻҜɿЋMԈ˳ǁԮÅ/ϟ;ǿёeҔ¬ңπ}',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            372359.278318041,
                                                                            399865.15072877024,
                                                                            631956.9792184542,
                                                                            544128.1286296727,
                                                                            133657.16165332356,
                                                                            273752.48560223525,
                                                                            867152.4193021161,
                                                                            313236.647475514,
                                                                            964623.1847446964,
                                                                            627746.1773133051,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '³®ƾūǄɀҸɘˊžɽȔSȈһʴȬO¸\x8dÓƫҫǢġΙҫÔƲà',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'į˂ЫǓƳĹΣ\u0381ȫĒňҟоȳҋ¨ʹʝ\x99ǼǊ2єǉȷˑĤʻȺÍ',
                                                    },
                                    },
                            {
                                        'name': '\x9dˢΆƆˮʍ\x8a',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u03a2тƂђҪХɤƛĶҤӹӝÆӉŬ˻ŇʇÛЩ˶ćϷȥĮѮѥϖΩȰ',
                                                                            'ɽ\u0380ƾ\x85ćƪԪӒ˦˪ͷ\u0379ĬƭǑȿͶʟƆǗԏΟ½³ҿǺ£ʄӈĥ',
                                                                            'ƠǡѼҫ˸±˲Û\x8dɧ\x86\x90ʣːǶƒԗѮҚ˛ǓАη¤ΈΎϘҧȠЩ',
                                                                            "ǖ\x8eˍάȻɏƓКōјȖΜk҇ƻϼăԝžæγ%ȿʴє'Ѯļάŝ",
                                                                            'ƎΑŧʲȕ"Ū˅έύ\x9aӊҏøʕR|ȫ˝ƙʅŽŊƴҪϵĜö{Ȳ',
                                                                            'ΐõbˊǢɞӹѢǾȊÞԁŗư\x8aǔkϕʅ¥ßǸѻʓѡȃâΙҌÖ',
                                                                            '˸ġĲȪÏm;\x92ЏЍѯԀĢԘ˫ӣˊħͽʯӾȬ\x9cȹӞțõЂ\x8b҉',
                                                                            'ʖƧčʕŖĸAĝȭҚǙįˇîуƵԚӀǸӻ˭\xa0óЧҼˣң|˻Ԥ',
                                                                            'Ӌώ\x99ſƺĆþһ¾˖Å҅ǯĠºӲЩңʻʉ;ѰҗǠʑ5н˃zĊ',
                                                                            'Ͳâ˱Ǆźҩ\u0380β{ı«ӹĸϝƗǐԗɥБƓӳèЄûşØÐŵvШ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'PhȔќΣѥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001809.875277:+0000',
                                                                            '20210413:001809.893797:+0000',
                                                                            '20210413:001809.911836:+0000',
                                                                            '20210413:001809.928399:+0000',
                                                                            '20210413:001809.943127:+0000',
                                                                            '20210413:001809.957972:+0000',
                                                                            '20210413:001809.973338:+0000',
                                                                            '20210413:001809.990841:+0000',
                                                                            '20210413:001810.007686:+0000',
                                                                            '20210413:001810.025490:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ĔʇӻÃӴȹĐʾȠϼˌɥ÷Ч'ŚòʹȐǾUЊƁɽϨƻdҮɄļ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -121823148941753003,
                                                                            1551076227591842104,
                                                                            -8651472245633396011,
                                                                            -3983156282972492251,
                                                                            7439212742918992129,
                                                                            -7422895449515678250,
                                                                            -7571460115574164008,
                                                                            224314559869102350,
                                                                            -8184415229418965774,
                                                                            -1649857811427963282,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'śԉҠƐÊЦѪ\x8bˡzԌұȈр',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001810.333814:+0000',
                                                                            '20210413:001810.350706:+0000',
                                                                            '20210413:001810.367945:+0000',
                                                                            '20210413:001810.385105:+0000',
                                                                            '20210413:001810.401805:+0000',
                                                                            '20210413:001810.420394:+0000',
                                                                            '20210413:001810.437218:+0000',
                                                                            '20210413:001810.454666:+0000',
                                                                            '20210413:001810.473069:+0000',
                                                                            '20210413:001810.490463:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʎҶƕʝҝȫ˦ŕ\x9cÎİИǈâÐöʩŨϵųŪ3ʪÜќԢҁɉĔǓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -61875.84212008732,
                                                                            980698.752253222,
                                                                            583122.5121967251,
                                                                            468699.8057577183,
                                                                            954759.1490410143,
                                                                            267944.3333359232,
                                                                            749002.7537632483,
                                                                            669193.5114514434,
                                                                            872809.8233199617,
                                                                            9589.870696320519,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ťԑʼҀ˵о',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            77470.19376738704,
                                                                            716073.5711954819,
                                                                            668321.9580835009,
                                                                            572182.3669720973,
                                                                            411322.7706391216,
                                                                            226839.6982116638,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÏЮӰ7ĶıˣƆ*ʱĠӡԙˢ\x8aʏȃɆ˛ўʫưpхШΛҳЕϘȽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            301959.59759109444,
                                                                            738322.9897026801,
                                                                            877248.7057349819,
                                                                            406426.52557268745,
                                                                            317106.6119234915,
                                                                            973735.1693468438,
                                                                            931142.2003469565,
                                                                            389149.5393159574,
                                                                            664071.9776212267,
                                                                            984788.9599969927,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƞ\x8eсŪŤҼƪñWŷƥ҃ӎΡǭQцÃϙӨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Iӵ҅˽ӌʬʜĆ˰ē@Ж˃ʊƬԢĴԊрɿˢʸԒȍƃҮɔԫ\x95ɒ',
                                                                            'ЂsҽƮŎ˾ΐʋ˘ʻԝƑ\x96ũ¼ЊƠ˺ƳцʚǜʦЪЊƜÿīʊɆ',
                                                                            'ɑJ[ƇąыїɬǺ\x8bӜҲěԮΞÂұɞ˘¸҄єφǫЀҪэԂɼ\\',
                                                                            'ЩʗǠǁʫŏ+ǭ\u0379ŰΜӡǂΊҌ&ϬɠШ\x7fżˇўҔқÈҳǯƏʈ',
                                                                            'Șҙϋ\u0379ϣʢҳˈȐрǢѶvПѧ\x9dͳĴŁŒéƚ\x8dɵǱԃʽ˙ӋШ',
                                                                            'шЬƋ:ʞѹ\x8eɢƐȚȊғ˅\x8eҷǚυʽļѭЃΓȹҤʷǫŎLѐ\x84',
                                                                            'ǩƍtȝоʂɖʺȧ\x8bīҚӒ˞μάПȸԮɚʠͿҥJӝʶϣћ҂ȭ',
                                                                            'Ƭͻʣ£ўʞϞɭњѿǅмɆÎɾ7ǥȺFʑΩӘӟӁԇҋǛˤʑÁ',
                                                                            '˻ԤţƋѼ˂úЃǍʻʮßƟȷʑƇʇ\x83ÓԜԧ\x8aӳʘɿ˛ĲȟȨĮ',
                                                                            'ƏǚĊíĉϓФǏΚrǖǹƣŧӟюƓ;ϱʶpϫѓ˼ǣǰǩƨȴР',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЉɫaаÅгМһŖӐħȧʢǑёƔǿɾŀyʂѸ˅ƭХŀԀҠρϣ',
                    'message': 'Ѵ˨ɍҹԥԎŶЂƟĂÏͱđəʓϚΑȀϛќҫԧӝÍǪѰƕōͳҶ',
                    'arguments': [
                            {
                                        'name': '¢˨ĳуΛϔśǇѧͲŖԐбG˓ƀˢдȨҞȾ\x90ɏgɛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ШπȗǪǛλГϢĝ\x83ǾкςĆҧ\x9eЂϧ\x81ɒΟGъ\x8eɍũȺǃɜĩ',
                                                                            'әЃԭʝ~¼Ǹέɘʐʽʄ§лʑӞӢʠÒÇţғŸĶĹҚЬȦѧȏ',
                                                                            'ҟŋНΏȔŸЗ5AÚʴ~ӃЮĸŷUΌΫĽ½ɫԔ/ѾǸɯƜѫP',
                                                                            'ǺĦ˷ЖЏž˖ͲЮÛjҜ¦јǛчɡБѽʭÄÄʲϿǻȹ˕Å[\x98',
                                                                            'ʑýɞ¦ƘХөч¢ҬЏ9ɅԃȡҊǖИҭЖΛɪζХǷɅЍ҄Ғʷ',
                                                                            'ͷ#ʨ˗дʣĜʯˏ͵ʁHōҭԋ҆ԂƩʭʾҩɆ<ȲВʞΘΝŬΥ',
                                                                            'çæЬ?βǘ˼ҟũѐÂΞ¨žΩɆÎ˗ĮʌƗˏѠƟԞãȴԜˈͼ',
                                                                            'ϙǲlɻђΆͺ΄ωШЙχє˃˽ŹѪ`ИҽΟʋʗɜ(҉ӢɍɈ΅',
                                                                            "Ю*ȐĶɭΈºķǪԅ҅˚ȝʧúŮЛ'ˈӘӡćǿǓ?.ʐʞНɢ",
                                                                            'ʨȂľфqŶ\x91ƜʓӐʃƢаʌҌǏѠπƏΨȽӫͰƴԩģƂĜʔϗ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǁѸ½ȦêϢǽɵɾʝέˠăԑγďòϞϵӧïCѥѩ\x8aҺŸǬǸɹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001811.818684:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʁӄҮφ˥¸ӲȚȒ¿ƖΠƧĽˈӭϥLƕƒѰӑЩ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001811.872236:+0000',
                                                    },
                                    },
                            {
                                        'name': 'уљǿά\x9bԆ\x95ϡӴн!ЎΒŃԝԟǇ˼ƂɔƟΡjƈȄԑɷνŋϱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001811.938716:+0000',
                                                                            '20210413:001811.956039:+0000',
                                                                            '20210413:001811.973002:+0000',
                                                                            '20210413:001811.989754:+0000',
                                                                            '20210413:001812.007363:+0000',
                                                                            '20210413:001812.026981:+0000',
                                                                            '20210413:001812.044010:+0000',
                                                                            '20210413:001812.060821:+0000',
                                                                            '20210413:001812.077767:+0000',
                                                                            '20210413:001812.095113:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɨ˅\x88ӦЕϒưĭӫȢãěΓӱʔ.ʔ¸Į\x9dѴ\x97Ǒł҈ҢǂċĆԮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'șȞ\u038děƞѸj}Ȼ"әŶ ңѴéԬԉʞňƺȢŃϱÃ1ӁlƇĦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x9eȧ˧åʽҖŁǠˇлȦθ˔ɃɎĀɐȸqѯFѶîп¾ʚәǱ˙Ň',
                                                    },
                                    },
                            {
                                        'name': 'fÎɬʡϫϭϷԪҫǴɹӿɹbŪǁʨϾЭӷққ\x91ΰɇɅˢв\x8fї',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ͻοƲʭEȒƳ˂ɾрęʲʴԤȲӍФӓͱʚĘʏȌ6ɇǛɩĂîI',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001812.416777:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȯЇξːşʑǂөҹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĥү\x9a_ҧӍǟîÔįl˯ǬϜŷĊPƶ\x9aчԍǯӷɾ\u0383ˡ·Ʈҟϫ',
                                                                            'đԢoЊÙϐΓè\u03a2ɮтʫӬ\x92ζ˶<ˤҭòƈʒĆǔөĈҗ˞0Ċ',
                                                                            'ÿȱûɐРǻύŇɩѼƐЂΰϨªа\x82҃вѴ·ĈԩňϫӯƒэԁҮ',
                                                                            'ҚêºƔхлżζͷΦͳfȗЦԕΗəнÁϪϪЗʰȉķɒοӄҭ ',
                                                                            'ĶԠΣΉҶAšƫeɏѮѡďȽĨɰͲmʍҖɭξßĢȇЂˍϨɤь',
                                                                            '˟r\x95ԣǄ"ɲ҈ƯμЇϚɪªɳʜ˦СǲȊЏҝƏ\x87ź\u038bŮʧ\x83γ',
                                                                            "¯ȏȚɎ͵Ӣο\x9c'Ӏ˴ҪɜʌҘϏ{ӨPѽʯȢӁʹ}ƾӇńöо",
                                                                            'ʈϵǤȫąЁɨ϶×ŠяϙίȒΑɖʤȾѬАΐɰЯǰˌƴîԝѓφ',
                                                                            'ȽðїˁэŷǂӉшίƒ/²£ԧWCģ£ɐ³ӆzƒǉӺЃϽȏӷ',
                                                                            'Ԉħѫμя˕ÿǟ|ȍӭŝέӳŲɬѥͻ:˗φʗѵԨѳ;ϺűϗΚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'çǽĉϣϊƼɤˣĢJ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4364321999610156419,
                                                                            3500445898037517674,
                                                                            -4860151461936087558,
                                                                            -1964504393912539873,
                                                                            2675375049859831840,
                                                                            2741222639208066047,
                                                                            2710709697524336826,
                                                                            -3242244885021728021,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɽɇNɡԪūȫ\u0380ɑɾˣљʵҀɢȖǙӿƶƑ˳҇àĢ)gԖӶɤɜ',
                    'message': 'пƐҝɪеǯ\u0383ЯɹӸ˪qɻ<ƦˁӽԜҚϐǹɦǔü˥¦Ωӧ˞ū',
                    'arguments': [
                            {
                                        'name': 'ϱ˰èȴĿдѻʻȭӵɂ\x98ӂωдӿ˲Ǔǲäĭ\u0382ű"ŀ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001813.203306:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƧӕɧÎŹϝJƸҡyϡþŧɋӉűȣ_ϣţ¦џɚ7˄ԬȊ9Ɇҗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɱҝҾĦŢɋìӒ$¡ńβûôʏҤԗјáιǩ˨λϮҎȫϡШ˦Ş',
                                                                            'Ǜţûɼ˾ǣŤŴ\x97\x9aîҨУǞʝЬƬҐFƭ\x85Ԗ϶ЫҞӒӗэѳ1',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ěѪȰӝəøɜԒÓʃұе\x8aƪД',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3773471823383385451,
                                                    },
                                    },
                            {
                                        'name': "\x83ĂӻҽàƧǭԟȎɣŴѻʐê΅'ўɮʎϔ˸˰ѷʟ×Ђ",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĿЅÁǻʢŵϠΒюҁԞ҇Xȶ°2¾λЗņȱǍǹȭ´ċćѶҘп',
                                                    },
                                    },
                            {
                                        'name': 'ʟԨ ˾ęmȭǧщс\u038dŨyҽ\u0383+PúèƲҧƓ˻ʓˈ¯ɭƱϏѢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'лːĨљėÖLƽLŷʸǰđϚȼԐȵЫƾƺґµ\x88ǜҘѸž',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5685798489238871400,
                                                                            3139264459598058070,
                                                                            1266781018324059295,
                                                                            -6381412316741109687,
                                                                            7769242565120704099,
                                                                            8257063123565400201,
                                                                            4460161851425660514,
                                                                            -67001911191156871,
                                                                            -5617208202617954586,
                                                                            -9038086048756145345,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '.͵ΧӃƪĳӘɾÁƾμ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 832831.2483064658,
                                                    },
                                    },
                            {
                                        'name': 'ɈoмҔ˒ÃwяKɡͺψɦɍҮѥǊҡʁӄ%шζÛѩʈĘ\x8aԉϖ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʍöϑĔ\x99žϪžŐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҹͺʾ҄ƖЙƾνòԨ\x9cVȀϵƚҢ`ЦШƫʚԎ˛с²ɍԉȮʹf',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "\x90ΡԗƯΌþńԙ˽ѺΣҜʓȸϗǐӜΈԇŐ'ҁӳʋäŝ-\x81НĹ",
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

            'identifier': '\xadԠйхб',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ɿѦ',
                    'message': "'",
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
            'request_id': -633401,
            'error': {
                'identifier': 'θʀνLǱ©˾ϬĝХŇЖӘԫϫϪŒҸХ6ӐO¿½ԉԎǗƖŖȕ',
                'categories': [
                    'invalid-user-action',
                    'os',
                    'os',
                    'network',
                    'internal',
                    'internal',
                    'file',
                    'invalid-user-action',
                    'configuration',
                    'access-restriction',
                ],
                'source': 'ӃȫźƾǓЙıτўεϖʁеҳʕзЋЈŖƀÞ°ӯƵʫѩȰŻ}ť',
                'messages': [
                    {
                            'catalog': 'ҿщ\x88ǁӈˢęГѽňɉУǪȶøԠǬдȨÒҬ\x87ʬȃƴҌ˗Ӿ\xadҜ',
                            'message': 'ƨƿlľΠӯǋԇЦ\x93ôʟįӸɛӿΝћkɛɱ\x8fɴԒā¿ȑ9ˤӷ',
                            'arguments': [
                                        {
                                                        'name': 'Ǻ%ʆŢÔıϬŚ`ǪɌΠɕ\u0379ӞЂҩĩӌƴҀɝuȠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ČǓʓΛԍĲƖÚwV\x9bˊʷǑђŲ˥ľӆń\x98·ŵǵġʆΧűӕÔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ņ˕čӒ˲Ȟ<ŃĩΤҀǇĦӧ~ɚмŇђƼϠσɬχǮΏ\x92O\x95λ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÏȤʭƩюɢϬôҼϣԪͼиǢңɎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 911744.4912647861,
                                                                        },
                                                    },
                                        {
                                                        'name': '$˥ɹϤǯVƅMÞ±',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÙјUÑɭ\u0381\x97ʅӹзε',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001748.775459:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\\Р҆ϗƌԙщÔŋüśƗѨҸΚȄlȸqӂȾӍԍΔĈmφÃӥК',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '¥λőҶҍѰāЕͶûʏлѓȓˌҮϜĝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1235915066939001813,
                                                                        },
                                                    },
                                        {
                                                        'name': "'Ϯ0\u0378\x8aʾŠʓ2ÚӐΝ«ÊϗʇԦб˼ϓPǿŹɲĄʩǍ˅ʖǭ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ңÎƆƙҭ˫\u0383\x8e϶ӜСɩ˶өʙϑƩɽϮšƓϚť',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦǥÅʺӉŵ˷ў',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 701713.2563404547,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'бŠŸΘδǉŃɂѶǉϥҴɤ҈ΗÆρȳԔƼ\u0382ǩΣҟɧËƆӨø³',
                            'message': 'ŏæc?ŧ˴IřϭώǸѬĐʅ˒Оҵ(ҸǠʣɦē҈˞ǝľɡ҂Ǯ',
                            'arguments': [
                                        {
                                                        'name': 'м\x9bȢӌȣĲȸǠɔTž҉ɠƺƏκҸбɮȬŉгǴʬBѽԞ}˕ͷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӋΒҾԁϺΗƽ\x86ʰÈęɠȖ˃ȧҞʮĵԄԖʯǷʐQȴ\x82-åϓȰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϻ\x8dФѻąǧђϝ\x82ŻҬ˯',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȄɣʭÆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'FҠɿҭ}ǃ~ǦШɶ¥ΣáΜҥ7ӟсŐϳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u0378ɷŔșӚȍ\x99\x9aѱƏzЁǻǃÏԓˍ˶ɥϖәȟԕϸn»ɈɖɈʛ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÝөƋԩśǧʏˬȰ˒ģӓƪťѨĽ]ĭƲќȂʑɻÛҾģԣĲӣĕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'äˢԑsʅęƢɑԑ1ψψ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǿęαǝϫГĚΘǳÙҢЕʁѮ\x89ͱѱѨҐӖȟΑȃʾЭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'båйΉӀɅԢ?щͻ«ľáşЭοʊ˗ωѕЖǸġʼ\x99çФEǂͶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001749.779831:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŇхƠG\x81?ҖĊϛ\x90ŷӇƪ:ѼŒКʎ%ϕͱŅʹόϑʍɾϗúƒ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҠΆǷÑѦĮѩǧyɿϜ¬ļȢЁѴɕЁ˦ËѡƖ˶˞ǻ@ŏÏǾ\x81',
                            'message': 'ΒͽѴŝŰʏϛо/ɊīɊnҋ±ɅÅԘȥ˙\x8bųŇұӵǣʯî\u0378Ǝ',
                            'arguments': [
                                        {
                                                        'name': 'ƼͼҬӖŗȤʇŏӠǖʬĮdŔз',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÒÅŞȱιĥǾq\xa0ǽѫ҄˥Ō=ȊīѣC¯Yȷʎ;^ҊѲǳ[ò',
                                                                        },
                                                    },
                                        {
                                                        'name': '¨ɀГΤˆyӬϢӍJҲ˼',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'rгÈ˒ǋҞŪҐ˭ѝԇďęѺА\u0379Ⱥ+ǷΗđ¥ƄьϲƱέɠҹϤ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļϧΰ.ɕ(ČāӛĩǇøǕ4üŢ˧ƀϧvõäŗ\x90ʌӜɑȔЎŚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ōǱҕɥˮ\u03a2®ΌŦĞŸ3ѯӍtɶӤϐYɬėͲȊŒӯŵӅЫːѡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ưϙ²ƬѰÿƊèȹ˓҆',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6189486804724057820,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˎʽҔ¼ԎťʎϠǩԇĺ\x90ԒΕƂɲЬSəŚΦӣҍсϝ˰ȬÙԠ҅',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1915147084371948066,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŌņȚǘˌȡќdφƅĮǈ"ҒƿuØĦӛƨóʔГɹѹư3˷Ɇɗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8195437906771952270,
                                                                        },
                                                    },
                                        {
                                                        'name': '7ʳʭȅЇЫѫѮǶӖȨɨÁ˫ĐƫͳŧaϡǒΚȤΥԅͽĶǟ҆у',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǝ Җǭ\x9aȦϒКдӼ\'ԘˎЏмг"QŲì Ÿ˜ϕԣʎÉɤä˃',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾIɍŏƮΞ\x93ɣĳvкЦԣ҇ǭҋҔ§φѭҧ\x86ǽŴ^`É',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001750.970761:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚǓČȣǋ%ͲЭʈҶ\x82ҲѾǯϨЊʬł\x9eεԠϻԇȂ\u038dŽԞȠſϽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001751.032034:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'њӼɋɝĪΕЏß\\çƬƓÃӋşƕ)ΈуӵΩȎʀɟƃӨˎƫ\u038bƄ',
                            'message': 'о˂»Ɋ˶{ңԫȾǕԬƶҺţǔ=ɔuΗǀηɪɌȤɀșǡˮǲα',
                            'arguments': [
                                        {
                                                        'name': 'PıCɉЩҽβ"ȂҮ¤RҋȧŞLΏԑȞ҃ļϯӝtǦѕÁӗѐÁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺϧҷӏʯӶęл9ĀÌɍ˼µŬóhˊЩ§ƥøΰɴʍl¨å\x92˼',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ZΡħŚȄӨ{˱ӻ˅êˣO˒ѳƲƸȝɂ˴ԫ¾ԐƙɚƧjφπ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5361877950203740848,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳ˦ԩдʡ˷lϙӀď˘ϙϯҐʞϫԅϊҥØХ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɅƱ҂˦ɽȅȀǄĳѺѼ´ěʶǐŏǆ+ҘҾτϙǝщҞ҇oĚʀϳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȹɋЮтʿ¿КĝҘΙ\x9eǅʷŨÀҋđŔϧӝʅЛЂѢԣмѺȼĉǺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ħӚϿĴ;ǕɻÔӭʃѼԕĴÈɖЂ\x8cρųůƜԃԎ˓ҖʁΊʌǛË',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 863160.3683833473,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȱŶŏŝѠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 954867.2167819785,
                                                                        },
                                                    },
                                        {
                                                        'name': "lȔʬʸŒ÷Ă΅äɠҗª'Ѫ©ƧęнРƻ£ђѢŠÑdżǌǍԪ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 835816.6140975275,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ëӉʝʘҩԦƈƞƥ\x9aƮ\u0381əЙÀΌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɼΑȤɺW±ʯԛΌҡ\u038bʀŅƮϼǍɠϨӱÖǊåȻɅŗ8iRʉЧ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŉħȁԫ\x9bŗǘŌťΉΔɋμγƤƒԠōƎҦêѫʪƺѥȜ\x85Ԑ˛ј',
                            'message': 'ʢβNҡʆ\u0379р˒ÂƕЪ˩\x91ÊȦӋǕƁŪȡĮɀέɞȮſѣʠčĵ',
                            'arguments': [
                                        {
                                                        'name': 'Şԉѱ\x9a\x93ўԨ˝',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'HԜȃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '*9ΆɂͶЂϲƣШĊѤώГФ\u03a2Ҕ\u0383ʌöӃК\x92ѻǥ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ίӺŇδ\x8fʖө\x9eϨȥɣʬԤӗĠӌчέʠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 78501.48173520723,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͽȼƹħ\xadxН΄Ć\x86Ҡƹ+ѤҮº˃ĺʗԟўЍԣʗ\x9dí«ЊȹϢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '}ӆеǔƙñϗҜτ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001752.394473:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝĥҟѦƧиīöĒѦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Πѥ˻ҤϴǚʥӀϹѨƙўʿyĤǬιȀЩъ=ʺɗ\x84Ŝ"',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '·˄ǱŮɲɄÛÃΡǴʖƞİƛӾƉǹ\x93ʁƆԍҖˣӯȴɾˏɶŐϑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÉԃԏǿǚԫКǡϵӼ\xadďљ˯˚ÎȗΏшԟԣʩǳ¹ǎăӁȕ#ʤ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀʿƒɊчўɉƊԅ˩^\\ɈʷξĨӮıʶĚǘпÒȱϐʷČӧȰϡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 835055.7381209317,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǴǄŇǲ\u0378ӫӻvʠôϧRƷΐˑƕ\x9cψҾɾӫӼ=ҞˤνŇѮӹǶ',
                            'message': 'zѝôҢ˟ӒȋЪĬƐõžÉιŶŒ²˴ĨÉѐ7ѫǻɜˈʭҳα˃',
                            'arguments': [
                                        {
                                                        'name': '\x7fӂһύtʟ\x8f҆ΕΖԭňѷŝӓǠ-Е\x84řǑɝüǳєҥĳˆЊδ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћǢĢěӛɤЛͲĀκМφȿ*ƙƊѼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 4763.052250886161,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉĹɾĆԁӟҹ¨\x8bӂʭ½ӈȐ˦ſĂĚčȺǇɝōȆиϵҸ\u0378ϏЖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u03a2ƀĉšԤ\x95',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001753.076981:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˤçƨˋÔ¤ǌГIĝiŗЮɅŴ@ȭÅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ƏͽȝƿӸñќѱ'Õϒƀ\x9dЫοΒƓɇɽ\x88EϜӁêʻɢ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȑ\x97ǸϤӹӪЙє˾ÐĎɎӐĆǣĕЈʌ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀ\x91\x82ԒėǝηǯˌҞѲʐ˺ЖǃԆǱ˗ύ6¡ҽǋη˥ðҼǲʨԃ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 92732.21160918497,
                                                                        },
                                                    },
                                        {
                                                        'name': '˷Έ-çƐʨҎĥѧɍȣR\x8eΎ¬ϜϋȢɧƉЛо҈ѽс0Ϥƭϯ˒',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӳgΦǼ=Tє\x9aûдҒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3869842901354990863,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ІӍÁΟƢŞӫ˯әƽȉ\x9cŌЁҋʷƣʁҌhŀƣ:ŚĨˡrΓԇҹ',
                            'message': 'ʢӗѵCáӊ϶ŀːρȵ˧ѨǧҫϗΦ@\x8fуɽɌùĀŊӠԥˡŖÑ',
                            'arguments': [
                                        {
                                                        'name': 'ĎǟԀțϰʸĮʏʺԐ=ˉɆľӻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Β',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԮÜԤCǔѣɌɠωҤ[œıTʝʞ\u0378ѡƠɲˢŦԬɣϋϧ\x8dûƯΉ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԭҠĊηѪ7ӕ÷Ã-ŤȭƱɅтʹͺʼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ғYԆ£вðEǌNϢƳUϮɌ\x99ĴņʖԃʾғϪƑ¡4ӷȫӞҀД',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001753.909804:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЯЬϥϐпҦ҆ʷ+Ôӯl)ÔӆďʬÞȳˡԒśħă¨Ñ\x9dЃԩԏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'öƶŎЅҏJϚǧˋ1\x8dϝƖ˸ĳԍyԤʉњкɇŋŒĔϴЌОČĘ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŸɘЃɭͶǏsƯѵαԔȵПÆ˃īʙΑǩϢé_ŰͽԃĳȺ˕',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001754.082511:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭ³ŲˑчǦȋɼǒʖʂʓБˑγĈрϼU҃ЙȁҐҐƸѷ˛ȶҔǤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 172297.10393941897,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĺ\x93ABѝŰƬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ң³²ҿOЩ/ǕԊӽàίɟӤˑķГ¢ʊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕһ¨әЁΓωЍǣԂʿ.vaԂÏɡ҂0¶ǇԕÄøѝԇ ưε',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Đ\x8bǘ˱ĵǹ¨Lɓͺҍ¤ȼрƨjА͵ʡμ!ӊgѾĝƿөʑЁƐ',
                            'message': 'ΖűƂ˦ƥɲFƧƽ˯ŌÛōi҉á˟ΰģŃŕƛƈ¨ѣҏ\x88ƪęǉ',
                            'arguments': [
                                        {
                                                        'name': 'ɔȒ¦ѧȤΈШϱǻÿӋЃͺơԇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 679197.2577983217,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԜζĜАΆŰǫÀыԒӀƣƐԨò҈˼ƜŔҁŔǏȰ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂƣŎԇ\x8aԛψҨΜСǅέɋŨИԞл',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǁƣĢԅĂԎ±Ȉҕ͵úđЭʎѐѨѮЦǎ\x94ʜЉǨҎΛҤƆҐƒε',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶШʢˏȊŊśЅE§ҨŻҞȠāʪȺăΎҡƩϡ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ίό´Х',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˅ȊƼͶĳŤӼȍў¡ǥǫțγ´ɬƺĈӈӏľȝҼɾЪ¥ӗѮ˔Ҿ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѾѵɼϷҤΜƣŌɊK˙âΣӷΙJÁеJԥԣҕűɪǫɐ΄элł',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϡGϷ~ǿЇӑҶ˚ЀɭɅɈϻK˶ѭˮμ\x99',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǽͷԜ϶£эѹqƩνԎѽԀԣӵɭȢǶȜϴЮӈ\x91șƂ˼ӦėԞǋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Пǰ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɄñΜҹßʀӍжģɭ\u0381ɔԐģѹāźȣњ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ιԖ\x8c\x9bаЫ\x93ӬϘφƳϛHɕ\u0379șԪˏZČɢФÇўЩÿǭʛωь',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ðʭγƪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -71902.17930157184,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԢˈŤĩƃl\x97ǕůŜΌĪΉɨ³әӻͶȜуĚϔǚ҅ĹÛӾ˯ΦƟ',
                            'message': '¤ΫPӯӑ·Ҹöҝ%ÚɗɢϨӢʪϐО(ςқȚʐƧǤíΒԗȸ.',
                            'arguments': [
                                        {
                                                        'name': 'ѾԪ˝˸Ǐƾƣpϔňϕ7¼ӇǲȍɖӀʜ·ƮÀ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ввƪȔŚԒ¾',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԈʳƍɡȿɈϞǝŧϷƎɿԍԑ=ϳƐɫмɅ(ѿvʤɦkǗҨǔσ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÍĈ˸ԢНϠ˳ǏɿѪԑȪƢʥӍ¼ǀыWζbеΥҔчΗ҅ɉȆə',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ң\u038b',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҇ɿ/ǬÕʢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "ƋΓˋάĘ\x8eɁιȺνϚŚҡwΝlӒΣƽБ'ˮKÖ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 467348347664573585,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x83ɩчñƕƴ\u0382ƅȧýȑȭȚ#ŋïûЭáĂżǻʥЕ҉]÷ǣſ$',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 826885.895580379,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳҌnȑ0QΔƻôƿʼ¬ȎŌƤcԎƐҵ҅έͽZMàěŌ\x9fƇʄ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѥιĭ\u0379ȷȊԡѽп\u0382ӊҹmϫӜȼОƂAǸƩԂ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ģ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7341952998916790099,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѯ{¾ȏϓƗíѕrѪǛαԀс×ө˙ϐȐűƴôȎɮìφʺƢǈϬ',
                            'message': 'ҽĒ\x91Ƥ\x86Ɉ>ņĀSώ҇Ɲ?ùɡϵƳԟ\x91Ţ˪ɘѼʜΨƫȉȵĻ',
                            'arguments': [
                                        {
                                                        'name': 'ȺÕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5831769200972573693,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƶϤșİψòӄǐѺԕ˫ъȂBäϋģԈȯŁŬ`έι҂ƯRђ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃEӸ˾êӁҠȀί*ȵы΄Ϳ\x8bŦ\u0378ȂɃ˒çӼǭ!ϖʲаʕð]',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˲ȷќƥәӷ©ĵӭхɅĐV\u038d˴Šӎ\u0379ʋƵӨþѸüŧʿ\x9dȣʱ1',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 769889.9169283614,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋЏTʚԮʷēԥ*ɰ͵ǗԒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҏʨҌЛЃҷјӭϕőʯ~ϱƜʕø˯Ǽһſ¶ҧˤ\x90çƎԟά¡˜',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001756.732665:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛәʵ˨ҷšʐϷǔɩϏЂр)',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѰȉȸђрȨ\x89Ɉũѓƿæ˯\x83«5мяΐ¡җȜχͺɈԟσҶlΘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˃˱Ӯ͵ʘʉӁĢŶсķſɩ\x8bΈCɟȋ¦Ê\x9dǱɓх\u0379ǈ¬϶ʯϬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'φ\u03a2ϏўżŀȡCԗχǐʐҋԉһɑ*á1ȤʘԂԨoч˯Πɖмƭ',
                                                                        },
                                                    },
                                        {
                                                        'name': '±\x9fƷˁô÷ÿÂҕсŕˣšӍɞƗΥЈҁ?ӀȐљʠϏăéaŪΩ',
                                                        'value': {
                                                                            '^': 'int_list',
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

            'request_id': 7140007,

            'error': {
                'identifier': 'ҿԔιԔȍ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'ц˷',
                            'message': 'Ť',
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
            'nw_x_pixel': -365138014,
            'nw_y_pixel': -746878807,
            'width': -5757142585107838857,
            'height': -2118651451885255563,
            'ratio_x': 3860009947371507978,
            'ratio_y': 1799731702468934496,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 1991898002,

            'nw_y_pixel': 1501941089,

            'width': -9157129487417677305,

            'height': -8159410896157759470,

            'ratio_x': -1463441270426080565,

            'ratio_y': -3462056029416695031,

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
                    'nw_x_pixel': 1312192628,
                    'nw_y_pixel': -65243166,
                    'width': -2399540769412710864,
                    'height': -3505992426823795975,
                    'ratio_x': -6166040692358789875,
                    'ratio_y': 2405868761672856915,
                },
                {
                    'nw_x_pixel': -273767848,
                    'nw_y_pixel': 1910689097,
                    'width': -2047221008908044313,
                    'height': -9184442340984863807,
                    'ratio_x': -9103627783699409340,
                    'ratio_y': 3235066589051124355,
                },
                {
                    'nw_x_pixel': -133718237,
                    'nw_y_pixel': 998695062,
                    'width': -5741982289211699915,
                    'height': -3386910282313602207,
                    'ratio_x': -1339710864232172776,
                    'ratio_y': -5826574989655618545,
                },
                {
                    'nw_x_pixel': 1026112457,
                    'nw_y_pixel': -889130197,
                    'width': -1547355654016462137,
                    'height': -1897578498562593247,
                    'ratio_x': 4685221862754504455,
                    'ratio_y': -7921559511420610841,
                },
                {
                    'nw_x_pixel': -551470122,
                    'nw_y_pixel': 1147166785,
                    'width': -2055728439305148019,
                    'height': -5556098240178002454,
                    'ratio_x': 8947549944006406916,
                    'ratio_y': 3729173753001762860,
                },
                {
                    'nw_x_pixel': 978326609,
                    'nw_y_pixel': -1226131662,
                    'width': -9141814027414079837,
                    'height': -6905695482648709561,
                    'ratio_x': -5176487491680965137,
                    'ratio_y': 8027283346717354451,
                },
                {
                    'nw_x_pixel': 116193548,
                    'nw_y_pixel': -1108088120,
                    'width': -1596507024411533351,
                    'height': -8206587771055619363,
                    'ratio_x': 2585696589014636796,
                    'ratio_y': -2134318730055461166,
                },
                {
                    'nw_x_pixel': 1679618446,
                    'nw_y_pixel': -1213432503,
                    'width': -5395209522297974606,
                    'height': -2163776812117507100,
                    'ratio_x': 597300243035025152,
                    'ratio_y': 8334710343086470924,
                },
                {
                    'nw_x_pixel': -1180768185,
                    'nw_y_pixel': 521124450,
                    'width': -4171955426777003202,
                    'height': -5170048007199140416,
                    'ratio_x': 7043782571041342547,
                    'ratio_y': 7300558607681859956,
                },
                {
                    'nw_x_pixel': -1381318092,
                    'nw_y_pixel': -1544166300,
                    'width': -2869474093665186846,
                    'height': -1952986372659548044,
                    'ratio_x': 8044802098550502763,
                    'ratio_y': -2408829667972475629,
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
                    'description': 'ϟѓŵǨƲ˾Þν-ώWˍĕεԜ\u03a2Ψ\u0378ӄύɸԄʲԙѫқ½ыÐʓ',
                    'monitors': [
                            {
                                        'identifier': 4460292,
                                        'width': -3284661578558646529,
                                        'height': 41328217016318544,
                                    },
                            {
                                        'identifier': 6736586,
                                        'width': 6846749899475200403,
                                        'height': -5962489101804257479,
                                    },
                            {
                                        'identifier': -997217,
                                        'width': -2849338743706123125,
                                        'height': 653076099192634370,
                                    },
                            {
                                        'identifier': 5837146,
                                        'width': -4634308738315372486,
                                        'height': -4427350345201838069,
                                    },
                            {
                                        'identifier': 4591749,
                                        'width': 1796449597358683086,
                                        'height': 2343107739409832775,
                                    },
                            {
                                        'identifier': 320941,
                                        'width': 4126530500595936986,
                                        'height': -6432108107253004315,
                                    },
                            {
                                        'identifier': -751539,
                                        'width': 3242184933098352728,
                                        'height': 7174600483964705257,
                                    },
                            {
                                        'identifier': 6776965,
                                        'width': -5757166342162991555,
                                        'height': 2519016567642089045,
                                    },
                            {
                                        'identifier': 2414969,
                                        'width': 5207674783195080710,
                                        'height': 1819643132120831489,
                                    },
                            {
                                        'identifier': 5557949,
                                        'width': -5715747514491445179,
                                        'height': -7961327717550134780,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9365124,
                                        'source_nw_x_pixel': -4997068365885553143,
                                        'source_nw_y_pixel': -6389544223528973385,
                                        'source_pixel_width': -5899387014991350787,
                                        'source_pixel_height': -6107199340598902777,
                                        'rotation': -3302891906289650122,
                                        'virtual_nw_x_pixel': 1330910593,
                                        'virtual_nw_y_pixel': 85082177,
                                        'virtual_width': 847495690,
                                        'virtual_height': -1456848902,
                                    },
                            {
                                        'source_monitor': 7633489,
                                        'source_nw_x_pixel': -5895049907141535985,
                                        'source_nw_y_pixel': -309085424103189168,
                                        'source_pixel_width': -1535689512808569261,
                                        'source_pixel_height': -8146681632471606214,
                                        'rotation': -2632624635507915440,
                                        'virtual_nw_x_pixel': -1674571742,
                                        'virtual_nw_y_pixel': 1677665527,
                                        'virtual_width': 301735818,
                                        'virtual_height': -1039989732,
                                    },
                            {
                                        'source_monitor': 5211254,
                                        'source_nw_x_pixel': -1198308280305852867,
                                        'source_nw_y_pixel': -5465678239501909515,
                                        'source_pixel_width': -3376804745882853587,
                                        'source_pixel_height': -3744795597612250543,
                                        'rotation': -6818601210455191710,
                                        'virtual_nw_x_pixel': 811239936,
                                        'virtual_nw_y_pixel': 1291187466,
                                        'virtual_width': -1166251808,
                                        'virtual_height': -268265037,
                                    },
                            {
                                        'source_monitor': -253538,
                                        'source_nw_x_pixel': -2937685361010548123,
                                        'source_nw_y_pixel': -6191826244826459692,
                                        'source_pixel_width': -7953787791471675243,
                                        'source_pixel_height': -9148598146366369541,
                                        'rotation': -9120465332585537194,
                                        'virtual_nw_x_pixel': -77466955,
                                        'virtual_nw_y_pixel': 604291794,
                                        'virtual_width': -739351490,
                                        'virtual_height': 1812670120,
                                    },
                            {
                                        'source_monitor': 851147,
                                        'source_nw_x_pixel': -4933676413915782509,
                                        'source_nw_y_pixel': -4514084440408476816,
                                        'source_pixel_width': -297375470463600502,
                                        'source_pixel_height': -7452030980323438439,
                                        'rotation': -7959203256846644686,
                                        'virtual_nw_x_pixel': -1215876769,
                                        'virtual_nw_y_pixel': 935470670,
                                        'virtual_width': -1823235043,
                                        'virtual_height': 1156564842,
                                    },
                            {
                                        'source_monitor': 3288805,
                                        'source_nw_x_pixel': -7991224978667667508,
                                        'source_nw_y_pixel': -4261385746842443541,
                                        'source_pixel_width': -799128492583789773,
                                        'source_pixel_height': -2068453011207485695,
                                        'rotation': -9056435699409332597,
                                        'virtual_nw_x_pixel': 831322213,
                                        'virtual_nw_y_pixel': 1196603210,
                                        'virtual_width': 1737334912,
                                        'virtual_height': 805542867,
                                    },
                            {
                                        'source_monitor': 7281791,
                                        'source_nw_x_pixel': -1085147160314242340,
                                        'source_nw_y_pixel': -1327422278010372825,
                                        'source_pixel_width': -8167359487441631334,
                                        'source_pixel_height': -4044924854679426215,
                                        'rotation': -3626331548014040069,
                                        'virtual_nw_x_pixel': -616371676,
                                        'virtual_nw_y_pixel': 1562014530,
                                        'virtual_width': -234031333,
                                        'virtual_height': 1971541608,
                                    },
                            {
                                        'source_monitor': -398730,
                                        'source_nw_x_pixel': -9077212439039971817,
                                        'source_nw_y_pixel': -7159285255780363835,
                                        'source_pixel_width': -84375486310883246,
                                        'source_pixel_height': -6079114951618716388,
                                        'rotation': -2418441752742714329,
                                        'virtual_nw_x_pixel': 339809154,
                                        'virtual_nw_y_pixel': 333006267,
                                        'virtual_width': 1600755949,
                                        'virtual_height': 616866249,
                                    },
                            {
                                        'source_monitor': 2023839,
                                        'source_nw_x_pixel': -5100321058238722629,
                                        'source_nw_y_pixel': -6105933061509137643,
                                        'source_pixel_width': -8933188268382125073,
                                        'source_pixel_height': -1872742165841439320,
                                        'rotation': -1302158407118980561,
                                        'virtual_nw_x_pixel': 792726868,
                                        'virtual_nw_y_pixel': -668811673,
                                        'virtual_width': -842265564,
                                        'virtual_height': -59983154,
                                    },
                            {
                                        'source_monitor': 7414373,
                                        'source_nw_x_pixel': -4540254231827918310,
                                        'source_nw_y_pixel': -1404876940263747777,
                                        'source_pixel_width': -2569166975594348885,
                                        'source_pixel_height': -2270644691613815845,
                                        'rotation': -6141532511190854998,
                                        'virtual_nw_x_pixel': -941403883,
                                        'virtual_nw_y_pixel': -1929987556,
                                        'virtual_width': -984553238,
                                        'virtual_height': -1628395718,
                                    },
                        ],
                },
                {
                    'description': 'ԙ¿ʰ²ŕďƛÚŮkŀƷȊȤϧɕʟăӴŌҸҝɋЄăɄьƸȨǤ',
                    'monitors': [
                            {
                                        'identifier': 9275890,
                                        'width': 4082893487552159073,
                                        'height': -8406037972246911590,
                                    },
                            {
                                        'identifier': 7077467,
                                        'width': 4847127808997473698,
                                        'height': 3647490965234873765,
                                    },
                            {
                                        'identifier': 2009145,
                                        'width': 2774743507728036168,
                                        'height': -8407830244785285412,
                                    },
                            {
                                        'identifier': -484498,
                                        'width': 7317987056639754612,
                                        'height': 6086843149860207106,
                                    },
                            {
                                        'identifier': 7558683,
                                        'width': 5586265532852389469,
                                        'height': 5814193828046440359,
                                    },
                            {
                                        'identifier': 3290230,
                                        'width': 5238813563200489945,
                                        'height': 4185884905306945216,
                                    },
                            {
                                        'identifier': -685556,
                                        'width': -361559095111513447,
                                        'height': -6975513799817488127,
                                    },
                            {
                                        'identifier': 3185780,
                                        'width': -810243096034772880,
                                        'height': -1589093128807706858,
                                    },
                            {
                                        'identifier': 3295343,
                                        'width': -5609957351745218120,
                                        'height': -5018469247958277320,
                                    },
                            {
                                        'identifier': 9721221,
                                        'width': 9188266629667966479,
                                        'height': 6785719210646524559,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4839692,
                                        'source_nw_x_pixel': -5764457758988585910,
                                        'source_nw_y_pixel': -8316504624005340365,
                                        'source_pixel_width': -3940737624931198971,
                                        'source_pixel_height': -451256379655236491,
                                        'rotation': -3353644894268222337,
                                        'virtual_nw_x_pixel': -1226042458,
                                        'virtual_nw_y_pixel': -1381830342,
                                        'virtual_width': -747972264,
                                        'virtual_height': 642221716,
                                    },
                            {
                                        'source_monitor': 7027063,
                                        'source_nw_x_pixel': -7897766658441990373,
                                        'source_nw_y_pixel': -483694647042628383,
                                        'source_pixel_width': -782221273743605006,
                                        'source_pixel_height': -4414944501695442250,
                                        'rotation': -3391727359536404750,
                                        'virtual_nw_x_pixel': -824031136,
                                        'virtual_nw_y_pixel': 840284614,
                                        'virtual_width': 1728163142,
                                        'virtual_height': 43403188,
                                    },
                            {
                                        'source_monitor': 9388731,
                                        'source_nw_x_pixel': -7434984172539764408,
                                        'source_nw_y_pixel': -2272665825722547297,
                                        'source_pixel_width': -5351818342416375512,
                                        'source_pixel_height': -6600124396168864419,
                                        'rotation': -1875954566757854873,
                                        'virtual_nw_x_pixel': 260535622,
                                        'virtual_nw_y_pixel': -479772122,
                                        'virtual_width': -1884885139,
                                        'virtual_height': 1521574964,
                                    },
                            {
                                        'source_monitor': 6845779,
                                        'source_nw_x_pixel': -262319595359649147,
                                        'source_nw_y_pixel': -9066154919665713208,
                                        'source_pixel_width': -385151353428735705,
                                        'source_pixel_height': -8946388312159662419,
                                        'rotation': -8087205769246324806,
                                        'virtual_nw_x_pixel': -295121121,
                                        'virtual_nw_y_pixel': 1269838840,
                                        'virtual_width': -1073074236,
                                        'virtual_height': -1622600948,
                                    },
                            {
                                        'source_monitor': 1879866,
                                        'source_nw_x_pixel': -9117459936910099827,
                                        'source_nw_y_pixel': -1648751197737393025,
                                        'source_pixel_width': -5827664667021011694,
                                        'source_pixel_height': -4422168109873356333,
                                        'rotation': -2245874372183059802,
                                        'virtual_nw_x_pixel': 1461007818,
                                        'virtual_nw_y_pixel': 1984704160,
                                        'virtual_width': -1917191017,
                                        'virtual_height': 1037249408,
                                    },
                            {
                                        'source_monitor': 2835368,
                                        'source_nw_x_pixel': -1493394418410539765,
                                        'source_nw_y_pixel': -1526313881533351450,
                                        'source_pixel_width': -7465007770270912249,
                                        'source_pixel_height': -1013736164467707126,
                                        'rotation': -3765174107629772085,
                                        'virtual_nw_x_pixel': 958770398,
                                        'virtual_nw_y_pixel': 1308730627,
                                        'virtual_width': -98157637,
                                        'virtual_height': 1948518948,
                                    },
                            {
                                        'source_monitor': 9309092,
                                        'source_nw_x_pixel': -1369539742676542767,
                                        'source_nw_y_pixel': -313258594410849319,
                                        'source_pixel_width': -4389557664828371211,
                                        'source_pixel_height': -2520039144811146384,
                                        'rotation': -3907031894989560574,
                                        'virtual_nw_x_pixel': 1300508077,
                                        'virtual_nw_y_pixel': 615677396,
                                        'virtual_width': 1892777918,
                                        'virtual_height': 416737197,
                                    },
                            {
                                        'source_monitor': 7390409,
                                        'source_nw_x_pixel': -1618337851453763626,
                                        'source_nw_y_pixel': -2529718123748298204,
                                        'source_pixel_width': -5967152821680850608,
                                        'source_pixel_height': -8594487752205252033,
                                        'rotation': -8307358629583765019,
                                        'virtual_nw_x_pixel': -1954848689,
                                        'virtual_nw_y_pixel': 601794928,
                                        'virtual_width': -541137005,
                                        'virtual_height': 1672474890,
                                    },
                            {
                                        'source_monitor': 514507,
                                        'source_nw_x_pixel': -2272194769771563860,
                                        'source_nw_y_pixel': -1812778452213901695,
                                        'source_pixel_width': -7797655945865412790,
                                        'source_pixel_height': -6993278896232145718,
                                        'rotation': -4874899316268677575,
                                        'virtual_nw_x_pixel': -1274427573,
                                        'virtual_nw_y_pixel': -1550889666,
                                        'virtual_width': 572751675,
                                        'virtual_height': 20718072,
                                    },
                            {
                                        'source_monitor': 7496475,
                                        'source_nw_x_pixel': -4166261250206769928,
                                        'source_nw_y_pixel': -1795522011962596286,
                                        'source_pixel_width': -2301394898672493013,
                                        'source_pixel_height': -8313370408334567747,
                                        'rotation': -5746604053190813104,
                                        'virtual_nw_x_pixel': 1640692522,
                                        'virtual_nw_y_pixel': 1569445199,
                                        'virtual_width': 1066138678,
                                        'virtual_height': 1863793435,
                                    },
                        ],
                },
                {
                    'description': '~ǁԫĠǴǃΚҏѝŝĜ϶,Ԗŕȅѷâ÷ѰƗ6ѨŃȷł˪ŵѥA',
                    'monitors': [
                            {
                                        'identifier': 7717389,
                                        'width': -594255817394920722,
                                        'height': -2392381424295537851,
                                    },
                            {
                                        'identifier': 8568926,
                                        'width': 458440169374585565,
                                        'height': -3790760480164005248,
                                    },
                            {
                                        'identifier': 3220884,
                                        'width': -707314299923603202,
                                        'height': -3581277434585439719,
                                    },
                            {
                                        'identifier': 9033479,
                                        'width': -8144400235958730249,
                                        'height': -5997770345824651712,
                                    },
                            {
                                        'identifier': 4191299,
                                        'width': -1988979983087064646,
                                        'height': 9007084552908181495,
                                    },
                            {
                                        'identifier': 290662,
                                        'width': -6495148704698626991,
                                        'height': 7213768549147599606,
                                    },
                            {
                                        'identifier': -385218,
                                        'width': -1727383798175982077,
                                        'height': 7099888759610605378,
                                    },
                            {
                                        'identifier': 2528183,
                                        'width': 5997391201519092896,
                                        'height': -6567095530161935183,
                                    },
                            {
                                        'identifier': 6931776,
                                        'width': -6503474111797677157,
                                        'height': 6148514940830764520,
                                    },
                            {
                                        'identifier': 6284824,
                                        'width': 2257103937659330989,
                                        'height': 3211942935275790951,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7287660,
                                        'source_nw_x_pixel': -5076275560840888118,
                                        'source_nw_y_pixel': -8322694728122544240,
                                        'source_pixel_width': -2488550116961453021,
                                        'source_pixel_height': -7258219654192288860,
                                        'rotation': -2746722556082313050,
                                        'virtual_nw_x_pixel': -1267789069,
                                        'virtual_nw_y_pixel': -415584063,
                                        'virtual_width': 671741335,
                                        'virtual_height': 1208924586,
                                    },
                            {
                                        'source_monitor': 6533227,
                                        'source_nw_x_pixel': -5433532722534872807,
                                        'source_nw_y_pixel': -4551569147332576396,
                                        'source_pixel_width': -8508840995402213719,
                                        'source_pixel_height': -2682813334590882420,
                                        'rotation': -3922447339390985981,
                                        'virtual_nw_x_pixel': -982019301,
                                        'virtual_nw_y_pixel': -1076952120,
                                        'virtual_width': 278771940,
                                        'virtual_height': 913796332,
                                    },
                            {
                                        'source_monitor': 9736389,
                                        'source_nw_x_pixel': -2122442376900533377,
                                        'source_nw_y_pixel': -7472137473140970324,
                                        'source_pixel_width': -3289017822554153067,
                                        'source_pixel_height': -4122272586656116005,
                                        'rotation': -6573525928618382735,
                                        'virtual_nw_x_pixel': 1188387149,
                                        'virtual_nw_y_pixel': 1411972312,
                                        'virtual_width': 476342050,
                                        'virtual_height': -971238623,
                                    },
                            {
                                        'source_monitor': 3898561,
                                        'source_nw_x_pixel': -4649950348640591488,
                                        'source_nw_y_pixel': -4956360992736724150,
                                        'source_pixel_width': -8962527129831958734,
                                        'source_pixel_height': -5118384717397276286,
                                        'rotation': -1505631330336935071,
                                        'virtual_nw_x_pixel': -635890281,
                                        'virtual_nw_y_pixel': -393827245,
                                        'virtual_width': 725628214,
                                        'virtual_height': -94664154,
                                    },
                            {
                                        'source_monitor': 8834562,
                                        'source_nw_x_pixel': -6115433667487771653,
                                        'source_nw_y_pixel': -1470844454855275271,
                                        'source_pixel_width': -3503022246786549992,
                                        'source_pixel_height': -2415169619727064941,
                                        'rotation': -8057024109713653149,
                                        'virtual_nw_x_pixel': 1706409592,
                                        'virtual_nw_y_pixel': 471408775,
                                        'virtual_width': 1206009874,
                                        'virtual_height': -1250410240,
                                    },
                            {
                                        'source_monitor': 526320,
                                        'source_nw_x_pixel': -5964353536578677698,
                                        'source_nw_y_pixel': -29279924472345661,
                                        'source_pixel_width': -1875961760806863027,
                                        'source_pixel_height': -6739488013930942400,
                                        'rotation': -1365429175427082924,
                                        'virtual_nw_x_pixel': 1819595920,
                                        'virtual_nw_y_pixel': 226609090,
                                        'virtual_width': 790982450,
                                        'virtual_height': -1391594530,
                                    },
                            {
                                        'source_monitor': 7116111,
                                        'source_nw_x_pixel': -527297492126262761,
                                        'source_nw_y_pixel': -1700550996742451902,
                                        'source_pixel_width': -7469290383130272778,
                                        'source_pixel_height': -4539764459232429348,
                                        'rotation': -7213191693336387500,
                                        'virtual_nw_x_pixel': 1086415606,
                                        'virtual_nw_y_pixel': -1280214952,
                                        'virtual_width': -431741798,
                                        'virtual_height': -493293217,
                                    },
                            {
                                        'source_monitor': 870859,
                                        'source_nw_x_pixel': -1005125166883880341,
                                        'source_nw_y_pixel': -9093138023769675075,
                                        'source_pixel_width': -1637049013563852898,
                                        'source_pixel_height': -3975624152435542598,
                                        'rotation': -8259596333248118961,
                                        'virtual_nw_x_pixel': -1947921725,
                                        'virtual_nw_y_pixel': -1622510741,
                                        'virtual_width': 683303611,
                                        'virtual_height': 1431006820,
                                    },
                            {
                                        'source_monitor': -964530,
                                        'source_nw_x_pixel': -5595498637191942969,
                                        'source_nw_y_pixel': -785272792828599999,
                                        'source_pixel_width': -8913415484510582489,
                                        'source_pixel_height': -7951284581108710545,
                                        'rotation': -2434670714106096926,
                                        'virtual_nw_x_pixel': 514414083,
                                        'virtual_nw_y_pixel': -1681316127,
                                        'virtual_width': 326073798,
                                        'virtual_height': 1872820166,
                                    },
                            {
                                        'source_monitor': 9655635,
                                        'source_nw_x_pixel': -2993727146601093580,
                                        'source_nw_y_pixel': -6856939132400491328,
                                        'source_pixel_width': -2007685752549714121,
                                        'source_pixel_height': -5615493195546663041,
                                        'rotation': -8012744134683482103,
                                        'virtual_nw_x_pixel': -472204870,
                                        'virtual_nw_y_pixel': -1413687595,
                                        'virtual_width': -1964647558,
                                        'virtual_height': -1559979859,
                                    },
                        ],
                },
                {
                    'description': '%ƱӺɐuľғӇz\x81ɍїԪӇҔîŒжԁ΄Қ\x99п˥ҳΤԙΚϟƒ',
                    'monitors': [
                            {
                                        'identifier': 1369794,
                                        'width': 5792768853973137752,
                                        'height': 8987917084867253821,
                                    },
                            {
                                        'identifier': 3228263,
                                        'width': -9156226301349619603,
                                        'height': -334699326984675323,
                                    },
                            {
                                        'identifier': 7878475,
                                        'width': -184076764754103235,
                                        'height': -6742004634942233783,
                                    },
                            {
                                        'identifier': 9500045,
                                        'width': -3596199854271293919,
                                        'height': -6593762173080409352,
                                    },
                            {
                                        'identifier': -184271,
                                        'width': 4949050792337483913,
                                        'height': 3401020297391072564,
                                    },
                            {
                                        'identifier': 1732297,
                                        'width': -6141909722098464272,
                                        'height': 9198676191321444745,
                                    },
                            {
                                        'identifier': 7771493,
                                        'width': -8434197555564520606,
                                        'height': -890387117217616460,
                                    },
                            {
                                        'identifier': -924902,
                                        'width': 5515599328139586193,
                                        'height': -1324002449657564477,
                                    },
                            {
                                        'identifier': 5507364,
                                        'width': -3086154121265435297,
                                        'height': 5301830411748437315,
                                    },
                            {
                                        'identifier': 8743035,
                                        'width': -3344106245225180192,
                                        'height': 5522197282986544274,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3545470,
                                        'source_nw_x_pixel': -7515689988851214134,
                                        'source_nw_y_pixel': -3392565390902811119,
                                        'source_pixel_width': -9058534174041515960,
                                        'source_pixel_height': -2382559582475161040,
                                        'rotation': -3590632587095390150,
                                        'virtual_nw_x_pixel': -794910094,
                                        'virtual_nw_y_pixel': 955335446,
                                        'virtual_width': -526201690,
                                        'virtual_height': -1614351298,
                                    },
                            {
                                        'source_monitor': 6448495,
                                        'source_nw_x_pixel': -5656320604128510134,
                                        'source_nw_y_pixel': -1055694639140778441,
                                        'source_pixel_width': -6064009467672748023,
                                        'source_pixel_height': -1504438447475139428,
                                        'rotation': -5039497377702276695,
                                        'virtual_nw_x_pixel': 1368829981,
                                        'virtual_nw_y_pixel': -9329463,
                                        'virtual_width': 1313454840,
                                        'virtual_height': 678046371,
                                    },
                            {
                                        'source_monitor': -325572,
                                        'source_nw_x_pixel': -5169001823416383716,
                                        'source_nw_y_pixel': -427354903897974045,
                                        'source_pixel_width': -1946835587229639400,
                                        'source_pixel_height': -2147888433893881184,
                                        'rotation': -8281677718314490878,
                                        'virtual_nw_x_pixel': -1364036210,
                                        'virtual_nw_y_pixel': 987038464,
                                        'virtual_width': 1082971039,
                                        'virtual_height': -1464565780,
                                    },
                            {
                                        'source_monitor': 6359353,
                                        'source_nw_x_pixel': -5002421465978356263,
                                        'source_nw_y_pixel': -638378777933976306,
                                        'source_pixel_width': -4997575824120211060,
                                        'source_pixel_height': -3380189863870343989,
                                        'rotation': -1545893093979339955,
                                        'virtual_nw_x_pixel': -1765476193,
                                        'virtual_nw_y_pixel': 1046346145,
                                        'virtual_width': 1530342700,
                                        'virtual_height': -309710069,
                                    },
                            {
                                        'source_monitor': 8758609,
                                        'source_nw_x_pixel': -8096439715801795783,
                                        'source_nw_y_pixel': -4827365692266134598,
                                        'source_pixel_width': -3922850247715650353,
                                        'source_pixel_height': -4072065328863088420,
                                        'rotation': -8524180289778998710,
                                        'virtual_nw_x_pixel': 1702282486,
                                        'virtual_nw_y_pixel': 1856009099,
                                        'virtual_width': 1936090238,
                                        'virtual_height': -1984065289,
                                    },
                            {
                                        'source_monitor': 5835452,
                                        'source_nw_x_pixel': -1846039600149206349,
                                        'source_nw_y_pixel': -3596351067709357684,
                                        'source_pixel_width': -5684062047995477209,
                                        'source_pixel_height': -542466214449578841,
                                        'rotation': -1420754082827564358,
                                        'virtual_nw_x_pixel': -1285625875,
                                        'virtual_nw_y_pixel': -585927855,
                                        'virtual_width': -544422894,
                                        'virtual_height': 1336193795,
                                    },
                            {
                                        'source_monitor': 1590326,
                                        'source_nw_x_pixel': -6685967405623476429,
                                        'source_nw_y_pixel': -5633975887359801976,
                                        'source_pixel_width': -6256263669590355356,
                                        'source_pixel_height': -841691408432188376,
                                        'rotation': -6928305621051510798,
                                        'virtual_nw_x_pixel': -1524837422,
                                        'virtual_nw_y_pixel': -388870838,
                                        'virtual_width': -447574635,
                                        'virtual_height': 1092149573,
                                    },
                            {
                                        'source_monitor': 2673763,
                                        'source_nw_x_pixel': -588810952554051680,
                                        'source_nw_y_pixel': -4642566749668664055,
                                        'source_pixel_width': -2122501683855833340,
                                        'source_pixel_height': -7366799557845752318,
                                        'rotation': -1772263973202277614,
                                        'virtual_nw_x_pixel': 1979468267,
                                        'virtual_nw_y_pixel': 1360128933,
                                        'virtual_width': 1450745250,
                                        'virtual_height': 136657867,
                                    },
                            {
                                        'source_monitor': 3635591,
                                        'source_nw_x_pixel': -6269320147676835131,
                                        'source_nw_y_pixel': -528035926009102225,
                                        'source_pixel_width': -922188049755267885,
                                        'source_pixel_height': -7870682455762878078,
                                        'rotation': -2991770078659138384,
                                        'virtual_nw_x_pixel': 85610410,
                                        'virtual_nw_y_pixel': -1257072018,
                                        'virtual_width': 527666534,
                                        'virtual_height': -1458088991,
                                    },
                            {
                                        'source_monitor': 8369742,
                                        'source_nw_x_pixel': -2359215136785885608,
                                        'source_nw_y_pixel': -4034180295398145511,
                                        'source_pixel_width': -3824944631554873520,
                                        'source_pixel_height': -3212151230850796854,
                                        'rotation': -6082045685213610234,
                                        'virtual_nw_x_pixel': -253087644,
                                        'virtual_nw_y_pixel': 661166802,
                                        'virtual_width': 1702905100,
                                        'virtual_height': 559292139,
                                    },
                        ],
                },
                {
                    'description': 'ɸ|ùҹ!ĹЩÍғǼӡ˰ԓӿɳȀ¡ƐâWĞ\x88 ʞűύȔŋºӜ',
                    'monitors': [
                            {
                                        'identifier': 9908864,
                                        'width': -5800690084955524731,
                                        'height': -2649014245523447492,
                                    },
                            {
                                        'identifier': 5655511,
                                        'width': 3081017133087509052,
                                        'height': 6365624070226951648,
                                    },
                            {
                                        'identifier': 8736281,
                                        'width': 6549278651768271245,
                                        'height': 2677823076963606128,
                                    },
                            {
                                        'identifier': 9530324,
                                        'width': -6358284868259423224,
                                        'height': 7587765144142724636,
                                    },
                            {
                                        'identifier': 7966099,
                                        'width': 3358416770967122139,
                                        'height': 3999839333423642210,
                                    },
                            {
                                        'identifier': 9279109,
                                        'width': 3612830317757491879,
                                        'height': -4633617118960305130,
                                    },
                            {
                                        'identifier': 8614805,
                                        'width': 4737260240935382212,
                                        'height': -1262176107742215393,
                                    },
                            {
                                        'identifier': 7359195,
                                        'width': -8384422744438314590,
                                        'height': 9137200398615100626,
                                    },
                            {
                                        'identifier': 7078648,
                                        'width': -8236944715464189078,
                                        'height': 170376548266913022,
                                    },
                            {
                                        'identifier': 3736679,
                                        'width': -924433135307917675,
                                        'height': -5110454207072286975,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2160907,
                                        'source_nw_x_pixel': -3407569670636278570,
                                        'source_nw_y_pixel': -2320785646523811383,
                                        'source_pixel_width': -5595922450744675983,
                                        'source_pixel_height': -7517969515764996811,
                                        'rotation': -2317248439096439236,
                                        'virtual_nw_x_pixel': -565138793,
                                        'virtual_nw_y_pixel': 1953155951,
                                        'virtual_width': 752092876,
                                        'virtual_height': -1838036310,
                                    },
                            {
                                        'source_monitor': 5758038,
                                        'source_nw_x_pixel': -2572775208322966371,
                                        'source_nw_y_pixel': -4046930410801508954,
                                        'source_pixel_width': -2158366444537287539,
                                        'source_pixel_height': -7377920611144101496,
                                        'rotation': -8323560015037690892,
                                        'virtual_nw_x_pixel': 1471744768,
                                        'virtual_nw_y_pixel': -1763970307,
                                        'virtual_width': -253103490,
                                        'virtual_height': 1659747604,
                                    },
                            {
                                        'source_monitor': 9372759,
                                        'source_nw_x_pixel': -4150309460469767267,
                                        'source_nw_y_pixel': -2392062119912515445,
                                        'source_pixel_width': -2563632775421553684,
                                        'source_pixel_height': -6375428641040176891,
                                        'rotation': -1119354333125454078,
                                        'virtual_nw_x_pixel': 64813643,
                                        'virtual_nw_y_pixel': -314199376,
                                        'virtual_width': 809141769,
                                        'virtual_height': -1622551293,
                                    },
                            {
                                        'source_monitor': 2046410,
                                        'source_nw_x_pixel': -2224044968671229957,
                                        'source_nw_y_pixel': -9163317330913910629,
                                        'source_pixel_width': -1243139994215899729,
                                        'source_pixel_height': -2554255543548820554,
                                        'rotation': -294167579441478051,
                                        'virtual_nw_x_pixel': -24682596,
                                        'virtual_nw_y_pixel': 857772138,
                                        'virtual_width': -641229523,
                                        'virtual_height': -732743414,
                                    },
                            {
                                        'source_monitor': 7015805,
                                        'source_nw_x_pixel': -188283657289562267,
                                        'source_nw_y_pixel': -4100240695199700351,
                                        'source_pixel_width': -8004219972259939219,
                                        'source_pixel_height': -6415748189067459601,
                                        'rotation': -6042099026797444654,
                                        'virtual_nw_x_pixel': -201171151,
                                        'virtual_nw_y_pixel': -1053360873,
                                        'virtual_width': -826091858,
                                        'virtual_height': -297113928,
                                    },
                            {
                                        'source_monitor': 4587220,
                                        'source_nw_x_pixel': -6403234379129556364,
                                        'source_nw_y_pixel': -6073749222231384566,
                                        'source_pixel_width': -7996749465869394499,
                                        'source_pixel_height': -5958474977596441200,
                                        'rotation': -127103117728182371,
                                        'virtual_nw_x_pixel': 1340758748,
                                        'virtual_nw_y_pixel': -1503483269,
                                        'virtual_width': -34995514,
                                        'virtual_height': 1169340821,
                                    },
                            {
                                        'source_monitor': -72521,
                                        'source_nw_x_pixel': -3943667921755545409,
                                        'source_nw_y_pixel': -4816347639974690316,
                                        'source_pixel_width': -4082232306308701093,
                                        'source_pixel_height': -1725742366027329591,
                                        'rotation': -3240295346273634667,
                                        'virtual_nw_x_pixel': 58155561,
                                        'virtual_nw_y_pixel': -711773156,
                                        'virtual_width': 1334567655,
                                        'virtual_height': -1838698263,
                                    },
                            {
                                        'source_monitor': 3268272,
                                        'source_nw_x_pixel': -5388812222691429125,
                                        'source_nw_y_pixel': -2718462280237369767,
                                        'source_pixel_width': -7029391713383722234,
                                        'source_pixel_height': -419860844348739541,
                                        'rotation': -5437276371703171351,
                                        'virtual_nw_x_pixel': 708169839,
                                        'virtual_nw_y_pixel': -99134871,
                                        'virtual_width': 964022740,
                                        'virtual_height': -582972692,
                                    },
                            {
                                        'source_monitor': 9670366,
                                        'source_nw_x_pixel': -8989615653467124301,
                                        'source_nw_y_pixel': -3588120211871671116,
                                        'source_pixel_width': -1483482105119583049,
                                        'source_pixel_height': -5965593302405514052,
                                        'rotation': -2464188210976285660,
                                        'virtual_nw_x_pixel': 140119186,
                                        'virtual_nw_y_pixel': 1809763571,
                                        'virtual_width': 1904576438,
                                        'virtual_height': 1796773848,
                                    },
                            {
                                        'source_monitor': 719426,
                                        'source_nw_x_pixel': -3825461993269632558,
                                        'source_nw_y_pixel': -4556189003717682538,
                                        'source_pixel_width': -1528431596376831572,
                                        'source_pixel_height': -5421996735258941548,
                                        'rotation': -4005527890163859644,
                                        'virtual_nw_x_pixel': -679146705,
                                        'virtual_nw_y_pixel': -74862725,
                                        'virtual_width': 530922353,
                                        'virtual_height': 651311361,
                                    },
                        ],
                },
                {
                    'description': ';ɴӤИ½ϡʠѥƢǯη˦ѲшάũωĆωҢɣˀ:ӨϢЃȶҒœɖ',
                    'monitors': [
                            {
                                        'identifier': 7557446,
                                        'width': 9107823745322410142,
                                        'height': -1060303837560366739,
                                    },
                            {
                                        'identifier': -84547,
                                        'width': -5128989457336551880,
                                        'height': -1026779224419956119,
                                    },
                            {
                                        'identifier': -863098,
                                        'width': 7286564286142305470,
                                        'height': 4349520280787529501,
                                    },
                            {
                                        'identifier': 2522390,
                                        'width': 1740240226483008423,
                                        'height': 6342792436975800184,
                                    },
                            {
                                        'identifier': 1598643,
                                        'width': 728352110933736003,
                                        'height': 8031203824946941275,
                                    },
                            {
                                        'identifier': 5512750,
                                        'width': -4995531349169872986,
                                        'height': -1607542636648115083,
                                    },
                            {
                                        'identifier': 1859929,
                                        'width': -14087934191436737,
                                        'height': 8707048009806939282,
                                    },
                            {
                                        'identifier': 9710890,
                                        'width': -536654656926665748,
                                        'height': 1379793764233282248,
                                    },
                            {
                                        'identifier': 8496441,
                                        'width': 7539950804526025971,
                                        'height': -7032594327841959185,
                                    },
                            {
                                        'identifier': 9259861,
                                        'width': -1260636988636359919,
                                        'height': 303129692160321503,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4363452,
                                        'source_nw_x_pixel': -8840529740765883757,
                                        'source_nw_y_pixel': -7107188694872075167,
                                        'source_pixel_width': -5510013529471766089,
                                        'source_pixel_height': -6393690191154210512,
                                        'rotation': -1313240916577948344,
                                        'virtual_nw_x_pixel': -1091698649,
                                        'virtual_nw_y_pixel': -1350982728,
                                        'virtual_width': 1156822246,
                                        'virtual_height': -113287130,
                                    },
                            {
                                        'source_monitor': 3396556,
                                        'source_nw_x_pixel': -3477661523181927017,
                                        'source_nw_y_pixel': -62365363722419736,
                                        'source_pixel_width': -7796698665304607774,
                                        'source_pixel_height': -1123049795486353538,
                                        'rotation': -3215552053104497856,
                                        'virtual_nw_x_pixel': -1702088572,
                                        'virtual_nw_y_pixel': -1119053337,
                                        'virtual_width': 961993356,
                                        'virtual_height': -785354623,
                                    },
                            {
                                        'source_monitor': 2437833,
                                        'source_nw_x_pixel': -2420651907654844803,
                                        'source_nw_y_pixel': -4660209352199457234,
                                        'source_pixel_width': -5267459936971644231,
                                        'source_pixel_height': -3699429949724314303,
                                        'rotation': -1522108231843339290,
                                        'virtual_nw_x_pixel': 1425162397,
                                        'virtual_nw_y_pixel': 690023055,
                                        'virtual_width': -1266236679,
                                        'virtual_height': -1772006082,
                                    },
                            {
                                        'source_monitor': 6833940,
                                        'source_nw_x_pixel': -93906787047361084,
                                        'source_nw_y_pixel': -4040174525968057707,
                                        'source_pixel_width': -4182346470337948969,
                                        'source_pixel_height': -6223932784654247304,
                                        'rotation': -6711087841236629385,
                                        'virtual_nw_x_pixel': 250482261,
                                        'virtual_nw_y_pixel': -1454645473,
                                        'virtual_width': -1147962232,
                                        'virtual_height': 422645680,
                                    },
                            {
                                        'source_monitor': 8352454,
                                        'source_nw_x_pixel': -818304164375253271,
                                        'source_nw_y_pixel': -3254676578773494933,
                                        'source_pixel_width': -6426876746634532654,
                                        'source_pixel_height': -771191342113665263,
                                        'rotation': -3204643887165445496,
                                        'virtual_nw_x_pixel': 1558040188,
                                        'virtual_nw_y_pixel': -1854137900,
                                        'virtual_width': 231612844,
                                        'virtual_height': -459141712,
                                    },
                            {
                                        'source_monitor': 5112683,
                                        'source_nw_x_pixel': -4894653991319209258,
                                        'source_nw_y_pixel': -6446371285484426808,
                                        'source_pixel_width': -8515017333819790399,
                                        'source_pixel_height': -9122474242587715864,
                                        'rotation': -8123291944516096449,
                                        'virtual_nw_x_pixel': 1504636028,
                                        'virtual_nw_y_pixel': -270454863,
                                        'virtual_width': 653035906,
                                        'virtual_height': 961190066,
                                    },
                            {
                                        'source_monitor': 6764639,
                                        'source_nw_x_pixel': -5810988840120851182,
                                        'source_nw_y_pixel': -9153308098588102745,
                                        'source_pixel_width': -4438141991827323555,
                                        'source_pixel_height': -2854778687808205320,
                                        'rotation': -2568154091760132358,
                                        'virtual_nw_x_pixel': 434764642,
                                        'virtual_nw_y_pixel': -1098833334,
                                        'virtual_width': -1535493599,
                                        'virtual_height': 1142809356,
                                    },
                            {
                                        'source_monitor': 2230936,
                                        'source_nw_x_pixel': -3874878175922408140,
                                        'source_nw_y_pixel': -4894144868551905503,
                                        'source_pixel_width': -3174316570542358001,
                                        'source_pixel_height': -1096675652113403985,
                                        'rotation': -6166346764652907313,
                                        'virtual_nw_x_pixel': 1223841304,
                                        'virtual_nw_y_pixel': 752040581,
                                        'virtual_width': -472254924,
                                        'virtual_height': 1444560964,
                                    },
                            {
                                        'source_monitor': 4203310,
                                        'source_nw_x_pixel': -8223469252376738565,
                                        'source_nw_y_pixel': -1771122474699042381,
                                        'source_pixel_width': -2173014805077813755,
                                        'source_pixel_height': -8932759473621414140,
                                        'rotation': -3856804834400501511,
                                        'virtual_nw_x_pixel': 1587709223,
                                        'virtual_nw_y_pixel': -993213321,
                                        'virtual_width': -1421812779,
                                        'virtual_height': 1975889433,
                                    },
                            {
                                        'source_monitor': 3998702,
                                        'source_nw_x_pixel': -8354878327229413010,
                                        'source_nw_y_pixel': -8166821636655392197,
                                        'source_pixel_width': -3568953176632360628,
                                        'source_pixel_height': -3864383437773825263,
                                        'rotation': -2397794427423975558,
                                        'virtual_nw_x_pixel': -1762898778,
                                        'virtual_nw_y_pixel': 143177300,
                                        'virtual_width': 865389425,
                                        'virtual_height': 1910289649,
                                    },
                        ],
                },
                {
                    'description': 'ΘΐӓĀ\x894ұҜӲƲ\x8eÛʲНɎȶŘ˄҉ԘºöŒǎʠ\x8fʤІʆ%',
                    'monitors': [
                            {
                                        'identifier': 5454412,
                                        'width': -4982799110548542620,
                                        'height': -7345512221459469411,
                                    },
                            {
                                        'identifier': 538565,
                                        'width': 6390901238140444915,
                                        'height': 2708760230693946568,
                                    },
                            {
                                        'identifier': 3284954,
                                        'width': 1781466806943630967,
                                        'height': 3089877760381105232,
                                    },
                            {
                                        'identifier': -109120,
                                        'width': 7304229542995501580,
                                        'height': -891444980977705000,
                                    },
                            {
                                        'identifier': 7614950,
                                        'width': 5918761523469557095,
                                        'height': -1107455701548907645,
                                    },
                            {
                                        'identifier': 1608597,
                                        'width': 3915341721887189487,
                                        'height': 4921663005399782428,
                                    },
                            {
                                        'identifier': 9161005,
                                        'width': 556657546995886276,
                                        'height': -6648580261903074284,
                                    },
                            {
                                        'identifier': 7779923,
                                        'width': -2585146884277975289,
                                        'height': 9213793023608655525,
                                    },
                            {
                                        'identifier': 2841117,
                                        'width': -2237930880568757591,
                                        'height': 1708989527882562373,
                                    },
                            {
                                        'identifier': 7563452,
                                        'width': 5728223213241007156,
                                        'height': 8216437119693068934,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3669656,
                                        'source_nw_x_pixel': -1769407851521178490,
                                        'source_nw_y_pixel': -1492379739130329888,
                                        'source_pixel_width': -4147433445759709190,
                                        'source_pixel_height': -3063681771540159277,
                                        'rotation': -7796478864660352142,
                                        'virtual_nw_x_pixel': -1127882558,
                                        'virtual_nw_y_pixel': -1131158886,
                                        'virtual_width': -463621087,
                                        'virtual_height': -47014206,
                                    },
                            {
                                        'source_monitor': 8085168,
                                        'source_nw_x_pixel': -6883285338193522324,
                                        'source_nw_y_pixel': -6076900585124794522,
                                        'source_pixel_width': -5129620995488650281,
                                        'source_pixel_height': -1959831401394587835,
                                        'rotation': -23225821716991935,
                                        'virtual_nw_x_pixel': -1041220442,
                                        'virtual_nw_y_pixel': 313377371,
                                        'virtual_width': 1678782059,
                                        'virtual_height': -923893191,
                                    },
                            {
                                        'source_monitor': 8082536,
                                        'source_nw_x_pixel': -6581415832069604167,
                                        'source_nw_y_pixel': -8108809804797048362,
                                        'source_pixel_width': -4915694537224363106,
                                        'source_pixel_height': -3701992774998386166,
                                        'rotation': -1344151489376365499,
                                        'virtual_nw_x_pixel': -877451762,
                                        'virtual_nw_y_pixel': 1211594958,
                                        'virtual_width': -1711257342,
                                        'virtual_height': -342841957,
                                    },
                            {
                                        'source_monitor': 6631431,
                                        'source_nw_x_pixel': -5805779256952539371,
                                        'source_nw_y_pixel': -6664941139122861464,
                                        'source_pixel_width': -4001778561582716488,
                                        'source_pixel_height': -2869510399391608893,
                                        'rotation': -4727441253576004600,
                                        'virtual_nw_x_pixel': -1232339580,
                                        'virtual_nw_y_pixel': 894687926,
                                        'virtual_width': 1337937408,
                                        'virtual_height': 261649026,
                                    },
                            {
                                        'source_monitor': 7598240,
                                        'source_nw_x_pixel': -4498908268260781941,
                                        'source_nw_y_pixel': -1143530073359131213,
                                        'source_pixel_width': -8069071950318275391,
                                        'source_pixel_height': -6746043952870252073,
                                        'rotation': -2939742413753602840,
                                        'virtual_nw_x_pixel': 784453847,
                                        'virtual_nw_y_pixel': -408751233,
                                        'virtual_width': 571556929,
                                        'virtual_height': -606228620,
                                    },
                            {
                                        'source_monitor': 7684507,
                                        'source_nw_x_pixel': -904889100662559402,
                                        'source_nw_y_pixel': -3580911652579391644,
                                        'source_pixel_width': -5626388843186826719,
                                        'source_pixel_height': -4833324485831501805,
                                        'rotation': -7553755632649056917,
                                        'virtual_nw_x_pixel': -1693682312,
                                        'virtual_nw_y_pixel': -1815529362,
                                        'virtual_width': 739520782,
                                        'virtual_height': -594816294,
                                    },
                            {
                                        'source_monitor': 1313672,
                                        'source_nw_x_pixel': -8818106409164747126,
                                        'source_nw_y_pixel': -3067900634760043655,
                                        'source_pixel_width': -7292132314711921023,
                                        'source_pixel_height': -4104862239579947065,
                                        'rotation': -3247204170595200295,
                                        'virtual_nw_x_pixel': -1678352060,
                                        'virtual_nw_y_pixel': 1864587602,
                                        'virtual_width': -222331974,
                                        'virtual_height': 1484251030,
                                    },
                            {
                                        'source_monitor': 7947223,
                                        'source_nw_x_pixel': -1103000080045256004,
                                        'source_nw_y_pixel': -9159144616298023856,
                                        'source_pixel_width': -603246340274430843,
                                        'source_pixel_height': -1635396626308636699,
                                        'rotation': -601702470938131622,
                                        'virtual_nw_x_pixel': -1434217811,
                                        'virtual_nw_y_pixel': -1128883231,
                                        'virtual_width': 1332703541,
                                        'virtual_height': -1597829502,
                                    },
                            {
                                        'source_monitor': 8037505,
                                        'source_nw_x_pixel': -6343410802161314675,
                                        'source_nw_y_pixel': -6123756886010450361,
                                        'source_pixel_width': -6617277960447061306,
                                        'source_pixel_height': -2267747739612783240,
                                        'rotation': -5974495518295845483,
                                        'virtual_nw_x_pixel': 471346512,
                                        'virtual_nw_y_pixel': -559921798,
                                        'virtual_width': -706980816,
                                        'virtual_height': -1139687245,
                                    },
                            {
                                        'source_monitor': 9858382,
                                        'source_nw_x_pixel': -4588002633791250198,
                                        'source_nw_y_pixel': -4548044492443253487,
                                        'source_pixel_width': -5036847838248785120,
                                        'source_pixel_height': -1817793826543455997,
                                        'rotation': -3647686405803402833,
                                        'virtual_nw_x_pixel': 1753659530,
                                        'virtual_nw_y_pixel': -269068504,
                                        'virtual_width': -1238647261,
                                        'virtual_height': -595652810,
                                    },
                        ],
                },
                {
                    'description': 'ΨŘ˖ɟÐė˴Ԍ·ɟҷӧѮЁɧɋŽǔǌўTǲ˗ΚˊŌƎΐшϓ',
                    'monitors': [
                            {
                                        'identifier': 8766928,
                                        'width': 7798505682048045347,
                                        'height': 2713927687209282741,
                                    },
                            {
                                        'identifier': -664646,
                                        'width': 4659972708900399610,
                                        'height': -1208510975563976571,
                                    },
                            {
                                        'identifier': 713564,
                                        'width': -2806575233419946175,
                                        'height': 4730446858617800698,
                                    },
                            {
                                        'identifier': 8123050,
                                        'width': -6257006711487902930,
                                        'height': -1521315865169026559,
                                    },
                            {
                                        'identifier': 5900014,
                                        'width': -8978752382625753367,
                                        'height': -1341543209174477119,
                                    },
                            {
                                        'identifier': 352502,
                                        'width': 5993959242876241557,
                                        'height': 2964868867971310024,
                                    },
                            {
                                        'identifier': -837674,
                                        'width': -1942003895780413453,
                                        'height': 3871148952867214703,
                                    },
                            {
                                        'identifier': 2066163,
                                        'width': 3802929335902974563,
                                        'height': 6425321623060577659,
                                    },
                            {
                                        'identifier': 325384,
                                        'width': -7392487369369001981,
                                        'height': -3553464507923263746,
                                    },
                            {
                                        'identifier': 4210552,
                                        'width': -2280507719558902908,
                                        'height': 7373112324659751057,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -517997,
                                        'source_nw_x_pixel': -8408156784092587348,
                                        'source_nw_y_pixel': -4893191603895684969,
                                        'source_pixel_width': -8550218121257427589,
                                        'source_pixel_height': -4433752286994035663,
                                        'rotation': -644279162276267937,
                                        'virtual_nw_x_pixel': -530710165,
                                        'virtual_nw_y_pixel': -354570760,
                                        'virtual_width': -1012441832,
                                        'virtual_height': -257430857,
                                    },
                            {
                                        'source_monitor': 8381665,
                                        'source_nw_x_pixel': -7466290504983689776,
                                        'source_nw_y_pixel': -630353815233124992,
                                        'source_pixel_width': -8220619797148329237,
                                        'source_pixel_height': -1700128615921857032,
                                        'rotation': -9003209112292017894,
                                        'virtual_nw_x_pixel': 1837500350,
                                        'virtual_nw_y_pixel': 1893052355,
                                        'virtual_width': -522375615,
                                        'virtual_height': -812733690,
                                    },
                            {
                                        'source_monitor': 4168886,
                                        'source_nw_x_pixel': -6187826885012986863,
                                        'source_nw_y_pixel': -3570619847747654418,
                                        'source_pixel_width': -6237018334608480154,
                                        'source_pixel_height': -1593886751321915023,
                                        'rotation': -1664545621303039365,
                                        'virtual_nw_x_pixel': 1051747205,
                                        'virtual_nw_y_pixel': -1158433906,
                                        'virtual_width': -623468785,
                                        'virtual_height': 398010684,
                                    },
                            {
                                        'source_monitor': 3843825,
                                        'source_nw_x_pixel': -7553709307463504388,
                                        'source_nw_y_pixel': -6120990834340921209,
                                        'source_pixel_width': -900043666392459706,
                                        'source_pixel_height': -6842562228668055741,
                                        'rotation': -6392753485173771658,
                                        'virtual_nw_x_pixel': 1225495229,
                                        'virtual_nw_y_pixel': -1130540215,
                                        'virtual_width': -978105319,
                                        'virtual_height': 552184159,
                                    },
                            {
                                        'source_monitor': 1365245,
                                        'source_nw_x_pixel': -4919274890248551815,
                                        'source_nw_y_pixel': -8436778851584056601,
                                        'source_pixel_width': -5607860958629829152,
                                        'source_pixel_height': -2088269009105270421,
                                        'rotation': -3308626893474816730,
                                        'virtual_nw_x_pixel': 240619552,
                                        'virtual_nw_y_pixel': 892248732,
                                        'virtual_width': 1819775707,
                                        'virtual_height': -119844259,
                                    },
                            {
                                        'source_monitor': 4820977,
                                        'source_nw_x_pixel': -823674258935563144,
                                        'source_nw_y_pixel': -4124819555564343880,
                                        'source_pixel_width': -3485180972838363227,
                                        'source_pixel_height': -1825843909690769803,
                                        'rotation': -7764249301683761523,
                                        'virtual_nw_x_pixel': -1561953227,
                                        'virtual_nw_y_pixel': -1255249862,
                                        'virtual_width': 1185688814,
                                        'virtual_height': -1828648106,
                                    },
                            {
                                        'source_monitor': 7017156,
                                        'source_nw_x_pixel': -2718160758055631877,
                                        'source_nw_y_pixel': -1294909777410692872,
                                        'source_pixel_width': -1914693830980819607,
                                        'source_pixel_height': -5172937914684927716,
                                        'rotation': -3318251797019874424,
                                        'virtual_nw_x_pixel': -1132163949,
                                        'virtual_nw_y_pixel': 1507477813,
                                        'virtual_width': 1848724830,
                                        'virtual_height': 61941032,
                                    },
                            {
                                        'source_monitor': 6564368,
                                        'source_nw_x_pixel': -399068719825071485,
                                        'source_nw_y_pixel': -3848885174436797285,
                                        'source_pixel_width': -4949493071696883795,
                                        'source_pixel_height': -6682674308615151054,
                                        'rotation': -4187625046829963268,
                                        'virtual_nw_x_pixel': -1834544972,
                                        'virtual_nw_y_pixel': 1619786413,
                                        'virtual_width': -1317034061,
                                        'virtual_height': -581533495,
                                    },
                            {
                                        'source_monitor': 9060426,
                                        'source_nw_x_pixel': -8683709138341139667,
                                        'source_nw_y_pixel': -1875398989726615035,
                                        'source_pixel_width': -2188550914613186323,
                                        'source_pixel_height': -6324193770304445524,
                                        'rotation': -6916785969663766147,
                                        'virtual_nw_x_pixel': 1585504630,
                                        'virtual_nw_y_pixel': -1397738283,
                                        'virtual_width': -703734500,
                                        'virtual_height': -303041854,
                                    },
                            {
                                        'source_monitor': 6719218,
                                        'source_nw_x_pixel': -1038578493709092369,
                                        'source_nw_y_pixel': -8946100387602185444,
                                        'source_pixel_width': -4350785517813546258,
                                        'source_pixel_height': -4119149337402267868,
                                        'rotation': -6889662542889644624,
                                        'virtual_nw_x_pixel': -1620656580,
                                        'virtual_nw_y_pixel': -1663850751,
                                        'virtual_width': 1412025014,
                                        'virtual_height': -14788574,
                                    },
                        ],
                },
                {
                    'description': 'ȟĮʤϑƶɁԌӄɘ\x83ԅϨƾŁϣʐȸȧԐǙǩķȉηТƏӻǵƝƎ',
                    'monitors': [
                            {
                                        'identifier': 727196,
                                        'width': 7992808748119305393,
                                        'height': -825458526184609074,
                                    },
                            {
                                        'identifier': 4606680,
                                        'width': -4055443093400826790,
                                        'height': 3893108945177170216,
                                    },
                            {
                                        'identifier': 819227,
                                        'width': -102437040629768120,
                                        'height': -2055061655637745301,
                                    },
                            {
                                        'identifier': 9689795,
                                        'width': 2326681162762724930,
                                        'height': -3813750078069727377,
                                    },
                            {
                                        'identifier': -926711,
                                        'width': -3706839331951370031,
                                        'height': 8953796441869270620,
                                    },
                            {
                                        'identifier': 3026628,
                                        'width': 8760331450913198516,
                                        'height': -2440241744136635008,
                                    },
                            {
                                        'identifier': 8631739,
                                        'width': 947385470213670303,
                                        'height': 6876208988122336547,
                                    },
                            {
                                        'identifier': -13646,
                                        'width': -6085566417432533088,
                                        'height': -4047540720063146827,
                                    },
                            {
                                        'identifier': 3094593,
                                        'width': -3017960608147546532,
                                        'height': -4359259531706181895,
                                    },
                            {
                                        'identifier': 5155742,
                                        'width': -7546296341614835179,
                                        'height': 6465696290227111741,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1059125,
                                        'source_nw_x_pixel': -2268078728838297897,
                                        'source_nw_y_pixel': -6324251790658011389,
                                        'source_pixel_width': -7515434299216132764,
                                        'source_pixel_height': -3992206577425359624,
                                        'rotation': -4981625578275160730,
                                        'virtual_nw_x_pixel': -1662858098,
                                        'virtual_nw_y_pixel': 333546029,
                                        'virtual_width': 344791495,
                                        'virtual_height': -874690726,
                                    },
                            {
                                        'source_monitor': 4866005,
                                        'source_nw_x_pixel': -8137649925475963529,
                                        'source_nw_y_pixel': -6162534490749674927,
                                        'source_pixel_width': -2606926531470300842,
                                        'source_pixel_height': -4549535162498246303,
                                        'rotation': -6486513955110322084,
                                        'virtual_nw_x_pixel': 1212622566,
                                        'virtual_nw_y_pixel': -1509257831,
                                        'virtual_width': 1961245330,
                                        'virtual_height': 185870462,
                                    },
                            {
                                        'source_monitor': 9788754,
                                        'source_nw_x_pixel': -2273291828889423363,
                                        'source_nw_y_pixel': -2454835503995760138,
                                        'source_pixel_width': -1766813838314968059,
                                        'source_pixel_height': -3378629394486696715,
                                        'rotation': -4720237848834916281,
                                        'virtual_nw_x_pixel': -1682278929,
                                        'virtual_nw_y_pixel': -1964431213,
                                        'virtual_width': -1887374817,
                                        'virtual_height': 938417858,
                                    },
                            {
                                        'source_monitor': 5845782,
                                        'source_nw_x_pixel': -5838926183963377095,
                                        'source_nw_y_pixel': -5716664918915296925,
                                        'source_pixel_width': -3463110722589036068,
                                        'source_pixel_height': -2189715412380881575,
                                        'rotation': -3477452657880220229,
                                        'virtual_nw_x_pixel': 1136589366,
                                        'virtual_nw_y_pixel': -1267213374,
                                        'virtual_width': 1633931344,
                                        'virtual_height': 1619457086,
                                    },
                            {
                                        'source_monitor': 8372400,
                                        'source_nw_x_pixel': -7235088380695447915,
                                        'source_nw_y_pixel': -9082323144914830753,
                                        'source_pixel_width': -3829267457948375262,
                                        'source_pixel_height': -2106200341544201564,
                                        'rotation': -5927684891359578320,
                                        'virtual_nw_x_pixel': -2248428,
                                        'virtual_nw_y_pixel': -672115413,
                                        'virtual_width': -646707183,
                                        'virtual_height': 1457793162,
                                    },
                            {
                                        'source_monitor': 8737402,
                                        'source_nw_x_pixel': -8752232342740635000,
                                        'source_nw_y_pixel': -2096279189005656867,
                                        'source_pixel_width': -6359352847453865294,
                                        'source_pixel_height': -3538469935200868791,
                                        'rotation': -544013650769165199,
                                        'virtual_nw_x_pixel': 1702004896,
                                        'virtual_nw_y_pixel': 1269153609,
                                        'virtual_width': -388910429,
                                        'virtual_height': -1459260941,
                                    },
                            {
                                        'source_monitor': 9596111,
                                        'source_nw_x_pixel': -3766334683754263843,
                                        'source_nw_y_pixel': -3496924009050440166,
                                        'source_pixel_width': -7788615123965307152,
                                        'source_pixel_height': -6287281415037300209,
                                        'rotation': -1086852145232100106,
                                        'virtual_nw_x_pixel': 1828541708,
                                        'virtual_nw_y_pixel': -352666415,
                                        'virtual_width': -1641057764,
                                        'virtual_height': -1591453140,
                                    },
                            {
                                        'source_monitor': -296955,
                                        'source_nw_x_pixel': -1310145445358459902,
                                        'source_nw_y_pixel': -8008559434169215720,
                                        'source_pixel_width': -3598459781821715241,
                                        'source_pixel_height': -5433507918985367016,
                                        'rotation': -870785022071129082,
                                        'virtual_nw_x_pixel': 287012176,
                                        'virtual_nw_y_pixel': -65241502,
                                        'virtual_width': -973014499,
                                        'virtual_height': -289299746,
                                    },
                            {
                                        'source_monitor': 227221,
                                        'source_nw_x_pixel': -7252250543904719192,
                                        'source_nw_y_pixel': -6360150642551220863,
                                        'source_pixel_width': -6564409697656317374,
                                        'source_pixel_height': -2192974307874498912,
                                        'rotation': -8743526561793853061,
                                        'virtual_nw_x_pixel': 389114187,
                                        'virtual_nw_y_pixel': 1481116143,
                                        'virtual_width': -1058623534,
                                        'virtual_height': -1333570335,
                                    },
                            {
                                        'source_monitor': 7484643,
                                        'source_nw_x_pixel': -3345028558435466218,
                                        'source_nw_y_pixel': -3965094584565038959,
                                        'source_pixel_width': -7015977559722426194,
                                        'source_pixel_height': -5830649380571642133,
                                        'rotation': -317199106251123050,
                                        'virtual_nw_x_pixel': -39292958,
                                        'virtual_nw_y_pixel': 1363599997,
                                        'virtual_width': -279758533,
                                        'virtual_height': -460694265,
                                    },
                        ],
                },
                {
                    'description': 'P҅ǔwČ˞ƿРɸʌІˠ¯Í\u0379Ƀ,ĭ:ΤĕНƏЋcȳĚЎǋř',
                    'monitors': [
                            {
                                        'identifier': 2589276,
                                        'width': -2649368592617351987,
                                        'height': 1515232048792464297,
                                    },
                            {
                                        'identifier': 3300792,
                                        'width': -8038533999459867267,
                                        'height': -1018749758128976824,
                                    },
                            {
                                        'identifier': 4979189,
                                        'width': -4508202297313855028,
                                        'height': 8021851666492371163,
                                    },
                            {
                                        'identifier': 8344901,
                                        'width': -8157751591523898262,
                                        'height': 2561872690640906612,
                                    },
                            {
                                        'identifier': 6884974,
                                        'width': 2972067166672237051,
                                        'height': 5533311063898216155,
                                    },
                            {
                                        'identifier': 1062162,
                                        'width': -4574487407798566558,
                                        'height': 5938895858168282521,
                                    },
                            {
                                        'identifier': 5404788,
                                        'width': 8153117212039374439,
                                        'height': 3170297539759818718,
                                    },
                            {
                                        'identifier': 7088042,
                                        'width': 2781336992026261470,
                                        'height': 8789420765453069901,
                                    },
                            {
                                        'identifier': 8238537,
                                        'width': -4644424540513964704,
                                        'height': 7579470903506405464,
                                    },
                            {
                                        'identifier': 5665371,
                                        'width': 4804365699803832570,
                                        'height': 6892390722199961516,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5085542,
                                        'source_nw_x_pixel': -5105581860490089700,
                                        'source_nw_y_pixel': -4031114781118516146,
                                        'source_pixel_width': -3858713496083873126,
                                        'source_pixel_height': -4556366870365537607,
                                        'rotation': -7486159680364782777,
                                        'virtual_nw_x_pixel': -1545581908,
                                        'virtual_nw_y_pixel': 1393143373,
                                        'virtual_width': -702725374,
                                        'virtual_height': 1121282944,
                                    },
                            {
                                        'source_monitor': 466362,
                                        'source_nw_x_pixel': -8672854720502091729,
                                        'source_nw_y_pixel': -6050330697402631188,
                                        'source_pixel_width': -6441326403893207249,
                                        'source_pixel_height': -8069529780745482106,
                                        'rotation': -100101957723424017,
                                        'virtual_nw_x_pixel': 1445926548,
                                        'virtual_nw_y_pixel': 1726251090,
                                        'virtual_width': -1138574175,
                                        'virtual_height': 1096630433,
                                    },
                            {
                                        'source_monitor': 4645456,
                                        'source_nw_x_pixel': -3574329774191541617,
                                        'source_nw_y_pixel': -5930968807285765641,
                                        'source_pixel_width': -5599295490768640584,
                                        'source_pixel_height': -8305139105390530098,
                                        'rotation': -5454943276386320780,
                                        'virtual_nw_x_pixel': 974495312,
                                        'virtual_nw_y_pixel': -643009835,
                                        'virtual_width': -346215588,
                                        'virtual_height': -141459481,
                                    },
                            {
                                        'source_monitor': 2378650,
                                        'source_nw_x_pixel': -5414559879522743410,
                                        'source_nw_y_pixel': -8806608330707169133,
                                        'source_pixel_width': -4242083227792628868,
                                        'source_pixel_height': -4325151625571664538,
                                        'rotation': -3824111161548161962,
                                        'virtual_nw_x_pixel': -204498553,
                                        'virtual_nw_y_pixel': -799516706,
                                        'virtual_width': 587240734,
                                        'virtual_height': -701879193,
                                    },
                            {
                                        'source_monitor': 3275959,
                                        'source_nw_x_pixel': -7186856212304308854,
                                        'source_nw_y_pixel': -1481142220043264092,
                                        'source_pixel_width': -8955055576760133084,
                                        'source_pixel_height': -1143684472774726025,
                                        'rotation': -3438848162638006556,
                                        'virtual_nw_x_pixel': -1793379949,
                                        'virtual_nw_y_pixel': -986303459,
                                        'virtual_width': 847489566,
                                        'virtual_height': 350394287,
                                    },
                            {
                                        'source_monitor': 8548809,
                                        'source_nw_x_pixel': -6947059638415932801,
                                        'source_nw_y_pixel': -5957182160960993009,
                                        'source_pixel_width': -8752507856153614676,
                                        'source_pixel_height': -3510086413202191339,
                                        'rotation': -1452840436359989632,
                                        'virtual_nw_x_pixel': -875650165,
                                        'virtual_nw_y_pixel': -318227076,
                                        'virtual_width': -18193129,
                                        'virtual_height': 36533736,
                                    },
                            {
                                        'source_monitor': 82527,
                                        'source_nw_x_pixel': -7090454796616676110,
                                        'source_nw_y_pixel': -1826611926715092706,
                                        'source_pixel_width': -2160404710329369961,
                                        'source_pixel_height': -926251680081625563,
                                        'rotation': -2644582476792402267,
                                        'virtual_nw_x_pixel': -1150904723,
                                        'virtual_nw_y_pixel': 640433624,
                                        'virtual_width': 73463886,
                                        'virtual_height': 1380966688,
                                    },
                            {
                                        'source_monitor': 8000661,
                                        'source_nw_x_pixel': -1649196283238074532,
                                        'source_nw_y_pixel': -8441016220144048554,
                                        'source_pixel_width': -3769477756502701811,
                                        'source_pixel_height': -6182882672982732700,
                                        'rotation': -7528599778776529284,
                                        'virtual_nw_x_pixel': 627996552,
                                        'virtual_nw_y_pixel': 687531208,
                                        'virtual_width': 824930757,
                                        'virtual_height': -1081515097,
                                    },
                            {
                                        'source_monitor': 8510625,
                                        'source_nw_x_pixel': -1717491254598641415,
                                        'source_nw_y_pixel': -7160286910849651700,
                                        'source_pixel_width': -6161257966755063240,
                                        'source_pixel_height': -5046941045143058379,
                                        'rotation': -6987487645088353631,
                                        'virtual_nw_x_pixel': -102742731,
                                        'virtual_nw_y_pixel': 1517235284,
                                        'virtual_width': -1890647028,
                                        'virtual_height': -974460205,
                                    },
                            {
                                        'source_monitor': 7501303,
                                        'source_nw_x_pixel': -8991500443935992975,
                                        'source_nw_y_pixel': -7476152986080695163,
                                        'source_pixel_width': -1432169487126842077,
                                        'source_pixel_height': -3991567315576698317,
                                        'rotation': -7845732895164508434,
                                        'virtual_nw_x_pixel': -1925452213,
                                        'virtual_nw_y_pixel': 1674374810,
                                        'virtual_width': 1393874448,
                                        'virtual_height': 550953321,
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
                                        'identifier': 5096880,
                                        'width': -4844356644761210345,
                                        'height': -303463371209655216,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -1366699762996775075,
                                        'source_nw_y_pixel': -4523663130315878486,
                                        'source_pixel_width': -8407439597420709690,
                                        'source_pixel_height': -4566247793036921013,
                                        'rotation': -5622745525177233325,
                                        'virtual_nw_x_pixel': -1923792382,
                                        'virtual_nw_y_pixel': 867180799,
                                        'virtual_width': 1613494392,
                                        'virtual_height': -423358033,
                                    },
                        ],
                },
            ],

        },
    ),
]
