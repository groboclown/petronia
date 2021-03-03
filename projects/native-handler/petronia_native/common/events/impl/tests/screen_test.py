# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-02T17:00:14.395460+00:00

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
            'identifier': 1358601,
            'width': 6327120594409594129,
            'height': -6073261648623619558,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 726877,

            'width': 8434566500114397989,

            'height': -6482659610765371825,

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
            'source_monitor': 6440206,
            'source_nw_x_pixel': -7052013538705948903,
            'source_nw_y_pixel': -8361206669349270390,
            'source_pixel_width': -1195377934840730119,
            'source_pixel_height': -7815707334254699542,
            'rotation': -7531893173738113773,
            'virtual_nw_x_pixel': -303931092,
            'virtual_nw_y_pixel': -1190510829,
            'virtual_width': -766574164,
            'virtual_height': 145581576,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -7928232307455400223,

            'source_nw_y_pixel': -1056128132354689422,

            'source_pixel_width': -2050878160076673199,

            'source_pixel_height': -2091271581850849087,

            'rotation': -1684428300004580946,

            'virtual_nw_x_pixel': 819524507,

            'virtual_nw_y_pixel': -1963717256,

            'virtual_width': 1585148706,

            'virtual_height': -404485578,

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
            'description': 'ƾǅWĽ)˪рȽŖȟԇƩԋӦԝҾϐBº¼КѼšǄɷԬǟ\x93\x7fʺ',
            'monitors': [
                {
                    'identifier': 5471303,
                    'width': -6826698920408819593,
                    'height': 4902898248666263254,
                },
                {
                    'identifier': 255885,
                    'width': 929990277283304918,
                    'height': -5101510648757054985,
                },
                {
                    'identifier': 3118471,
                    'width': -4571640499292301104,
                    'height': 8982192876908830179,
                },
                {
                    'identifier': 7784185,
                    'width': -2271403532205773366,
                    'height': -7913107043286061164,
                },
                {
                    'identifier': 5794324,
                    'width': 3498560841313000699,
                    'height': 7336542577624680685,
                },
                {
                    'identifier': 3262614,
                    'width': 3685946764114156193,
                    'height': 1257748195201807539,
                },
                {
                    'identifier': -248425,
                    'width': 2289144417617405609,
                    'height': -2634562355969255853,
                },
                {
                    'identifier': 6835504,
                    'width': -4450339202184866968,
                    'height': 3007431240796341755,
                },
                {
                    'identifier': 4849070,
                    'width': 2909905204894762545,
                    'height': -5355224856779037381,
                },
                {
                    'identifier': 9981423,
                    'width': 3530831929865246191,
                    'height': 5436121598560564551,
                },
            ],
            'screen': [
                {
                    'source_monitor': 4635871,
                    'source_nw_x_pixel': -3173370663427031634,
                    'source_nw_y_pixel': -2637830165788492067,
                    'source_pixel_width': -4124130866428696466,
                    'source_pixel_height': -6503646304114350458,
                    'rotation': -3487522683727801604,
                    'virtual_nw_x_pixel': -897794594,
                    'virtual_nw_y_pixel': 398935882,
                    'virtual_width': 512585346,
                    'virtual_height': 1375538742,
                },
                {
                    'source_monitor': 5618471,
                    'source_nw_x_pixel': -7858032804630963246,
                    'source_nw_y_pixel': -8426668245512368751,
                    'source_pixel_width': -4997504904442070904,
                    'source_pixel_height': -587418732392465142,
                    'rotation': -1313919011221540811,
                    'virtual_nw_x_pixel': -1507438376,
                    'virtual_nw_y_pixel': 392975570,
                    'virtual_width': 1391441663,
                    'virtual_height': 291473996,
                },
                {
                    'source_monitor': 8656275,
                    'source_nw_x_pixel': -1975171614102418444,
                    'source_nw_y_pixel': -2376783206758225615,
                    'source_pixel_width': -2230127034116092977,
                    'source_pixel_height': -9185318834229334920,
                    'rotation': -8617553210435312219,
                    'virtual_nw_x_pixel': -1740268584,
                    'virtual_nw_y_pixel': -1383042026,
                    'virtual_width': -430141648,
                    'virtual_height': -229461709,
                },
                {
                    'source_monitor': 4811587,
                    'source_nw_x_pixel': -13701562718262719,
                    'source_nw_y_pixel': -829922229865816144,
                    'source_pixel_width': -6347273441531394390,
                    'source_pixel_height': -3130829884830822479,
                    'rotation': -8443742504056171399,
                    'virtual_nw_x_pixel': 974788670,
                    'virtual_nw_y_pixel': -715216268,
                    'virtual_width': 1247496811,
                    'virtual_height': -350665900,
                },
                {
                    'source_monitor': 8132930,
                    'source_nw_x_pixel': -8861064178555917104,
                    'source_nw_y_pixel': -8590005547879527855,
                    'source_pixel_width': -6598636934889243066,
                    'source_pixel_height': -4207182467585187039,
                    'rotation': -3477011477147912137,
                    'virtual_nw_x_pixel': 1588955131,
                    'virtual_nw_y_pixel': -681739803,
                    'virtual_width': 1664125795,
                    'virtual_height': 466488521,
                },
                {
                    'source_monitor': 4757496,
                    'source_nw_x_pixel': -5578481676548486692,
                    'source_nw_y_pixel': -8281995631145412547,
                    'source_pixel_width': -4038738027099820206,
                    'source_pixel_height': -8994963483870023157,
                    'rotation': -1013527399319073360,
                    'virtual_nw_x_pixel': 13223318,
                    'virtual_nw_y_pixel': -603193226,
                    'virtual_width': -223817658,
                    'virtual_height': -1824461992,
                },
                {
                    'source_monitor': 3982568,
                    'source_nw_x_pixel': -8955114756649090584,
                    'source_nw_y_pixel': -1092723921041456997,
                    'source_pixel_width': -7438079682486136762,
                    'source_pixel_height': -3236518483097186932,
                    'rotation': -6659882313382669891,
                    'virtual_nw_x_pixel': -1306372808,
                    'virtual_nw_y_pixel': -723129649,
                    'virtual_width': -1676933599,
                    'virtual_height': 1066470589,
                },
                {
                    'source_monitor': 8507005,
                    'source_nw_x_pixel': -2378608121496718719,
                    'source_nw_y_pixel': -4083796682620301034,
                    'source_pixel_width': -1258423620299746555,
                    'source_pixel_height': -5282702044724017323,
                    'rotation': -6546598217435941135,
                    'virtual_nw_x_pixel': 530840934,
                    'virtual_nw_y_pixel': -438624068,
                    'virtual_width': -812120890,
                    'virtual_height': 933630612,
                },
                {
                    'source_monitor': 644650,
                    'source_nw_x_pixel': -2729128033014649202,
                    'source_nw_y_pixel': -2563428452801621759,
                    'source_pixel_width': -7324060572519804288,
                    'source_pixel_height': -5499186654414986941,
                    'rotation': -3292655396396357983,
                    'virtual_nw_x_pixel': -1625464300,
                    'virtual_nw_y_pixel': -1718791083,
                    'virtual_width': 1239003639,
                    'virtual_height': 1305941489,
                },
                {
                    'source_monitor': 1011111,
                    'source_nw_x_pixel': -8267731486957738714,
                    'source_nw_y_pixel': -2218387828466055039,
                    'source_pixel_width': -5365167297703832832,
                    'source_pixel_height': -2038942114734904507,
                    'rotation': -8520072705197214545,
                    'virtual_nw_x_pixel': 311441064,
                    'virtual_nw_y_pixel': -300332333,
                    'virtual_width': -673485012,
                    'virtual_height': 853970248,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 7112176,
                    'width': 2025806929982420031,
                    'height': -2013660928995342165,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -8874502214283260906,
                    'source_nw_y_pixel': -5647336341824124987,
                    'source_pixel_width': -9135681878155112041,
                    'source_pixel_height': -2286938661514661718,
                    'rotation': -8416094141525929610,
                    'virtual_nw_x_pixel': -1545585968,
                    'virtual_nw_y_pixel': -1504237058,
                    'virtual_width': 1208829237,
                    'virtual_height': 1545770533,
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
            'request_id': 5448709,
            'mapped_screens_by_monitors': [
                {
                    'description': '-ƳԚŖΦ˪҉Σ\u0381Āϟǳ zʰҜ&½1Vԁι÷Ǎȯ©ίгȾį',
                    'monitors': [
                            {
                                        'identifier': 778345,
                                        'width': 7461094294485982705,
                                        'height': 739376967308861441,
                                    },
                            {
                                        'identifier': 1939594,
                                        'width': -852026472751743627,
                                        'height': -5312029979216867827,
                                    },
                            {
                                        'identifier': 4267874,
                                        'width': 2645210659275457666,
                                        'height': -8601899547700945264,
                                    },
                            {
                                        'identifier': 2880021,
                                        'width': 2191255606830855617,
                                        'height': 6723381825034348401,
                                    },
                            {
                                        'identifier': 6444824,
                                        'width': -3576179788901154446,
                                        'height': 1258107013074869324,
                                    },
                            {
                                        'identifier': 4840443,
                                        'width': 5810788737791433749,
                                        'height': -6839933031546042097,
                                    },
                            {
                                        'identifier': 991902,
                                        'width': 3601528051810198395,
                                        'height': -8572865413563348261,
                                    },
                            {
                                        'identifier': 18542,
                                        'width': -160454344414934469,
                                        'height': 2516959743727540755,
                                    },
                            {
                                        'identifier': 4650026,
                                        'width': 7734729901589169748,
                                        'height': 1922474301345468467,
                                    },
                            {
                                        'identifier': 1190951,
                                        'width': 3022625676726408150,
                                        'height': 9036876646068853641,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6427537,
                                        'source_nw_x_pixel': -2019001293440367877,
                                        'source_nw_y_pixel': -8286883912863992304,
                                        'source_pixel_width': -8695609416944031402,
                                        'source_pixel_height': -815160549625618600,
                                        'rotation': -1084839550019377622,
                                        'virtual_nw_x_pixel': -1358468469,
                                        'virtual_nw_y_pixel': -721454061,
                                        'virtual_width': -1057459546,
                                        'virtual_height': 803356676,
                                    },
                            {
                                        'source_monitor': 8832354,
                                        'source_nw_x_pixel': -1398644826137031480,
                                        'source_nw_y_pixel': -2424139117784090232,
                                        'source_pixel_width': -8406914481216643085,
                                        'source_pixel_height': -5486231003889875107,
                                        'rotation': -7648876699221269039,
                                        'virtual_nw_x_pixel': -1533776744,
                                        'virtual_nw_y_pixel': -1695708373,
                                        'virtual_width': 1529437095,
                                        'virtual_height': 542974561,
                                    },
                            {
                                        'source_monitor': -337377,
                                        'source_nw_x_pixel': -5693668250436569350,
                                        'source_nw_y_pixel': -5863140141529788282,
                                        'source_pixel_width': -5885363824203017531,
                                        'source_pixel_height': -3680100451132166727,
                                        'rotation': -1402057782563318177,
                                        'virtual_nw_x_pixel': -1066899962,
                                        'virtual_nw_y_pixel': -522054238,
                                        'virtual_width': -1825266077,
                                        'virtual_height': -1851958751,
                                    },
                            {
                                        'source_monitor': 9326743,
                                        'source_nw_x_pixel': -8943798251292129598,
                                        'source_nw_y_pixel': -8034780050139610,
                                        'source_pixel_width': -4293994205013142081,
                                        'source_pixel_height': -641480345106635361,
                                        'rotation': -1433624833917560599,
                                        'virtual_nw_x_pixel': -987101048,
                                        'virtual_nw_y_pixel': 632328390,
                                        'virtual_width': -1326595339,
                                        'virtual_height': 1730225545,
                                    },
                            {
                                        'source_monitor': 7169988,
                                        'source_nw_x_pixel': -1512212739317130814,
                                        'source_nw_y_pixel': -5472142267695027485,
                                        'source_pixel_width': -4739873281519979749,
                                        'source_pixel_height': -5119237878701751421,
                                        'rotation': -8620680228265422932,
                                        'virtual_nw_x_pixel': 483580137,
                                        'virtual_nw_y_pixel': -188822090,
                                        'virtual_width': -1992347071,
                                        'virtual_height': 154459532,
                                    },
                            {
                                        'source_monitor': 4432450,
                                        'source_nw_x_pixel': -1032513861455043784,
                                        'source_nw_y_pixel': -107255062678926274,
                                        'source_pixel_width': -383801737252567017,
                                        'source_pixel_height': -4669190417418307639,
                                        'rotation': -441025973643284739,
                                        'virtual_nw_x_pixel': 115671377,
                                        'virtual_nw_y_pixel': -1201739156,
                                        'virtual_width': 1641471521,
                                        'virtual_height': -121674746,
                                    },
                            {
                                        'source_monitor': 1622171,
                                        'source_nw_x_pixel': -5592780190844458272,
                                        'source_nw_y_pixel': -6334116552170465201,
                                        'source_pixel_width': -2951726972764627792,
                                        'source_pixel_height': -6388228887153254033,
                                        'rotation': -8949255514249880374,
                                        'virtual_nw_x_pixel': 654436550,
                                        'virtual_nw_y_pixel': 391989,
                                        'virtual_width': 691222446,
                                        'virtual_height': -101898047,
                                    },
                            {
                                        'source_monitor': 1510864,
                                        'source_nw_x_pixel': -7442647379430747060,
                                        'source_nw_y_pixel': -6457145582451932394,
                                        'source_pixel_width': -1276335379340267211,
                                        'source_pixel_height': -1847780522576645700,
                                        'rotation': -8686961636204769113,
                                        'virtual_nw_x_pixel': -1124182900,
                                        'virtual_nw_y_pixel': 1894309169,
                                        'virtual_width': -1550172742,
                                        'virtual_height': 1220825184,
                                    },
                            {
                                        'source_monitor': -602907,
                                        'source_nw_x_pixel': -9215001936174721833,
                                        'source_nw_y_pixel': -5820048035974323827,
                                        'source_pixel_width': -1970703783480187227,
                                        'source_pixel_height': -2965450454297027314,
                                        'rotation': -442178438121783883,
                                        'virtual_nw_x_pixel': -217517230,
                                        'virtual_nw_y_pixel': -810761426,
                                        'virtual_width': 1934706995,
                                        'virtual_height': -1403348994,
                                    },
                            {
                                        'source_monitor': 3159319,
                                        'source_nw_x_pixel': -2804131974595025214,
                                        'source_nw_y_pixel': -2579474125272198980,
                                        'source_pixel_width': -3560227277609896339,
                                        'source_pixel_height': -3622423909018894343,
                                        'rotation': -2973115076382567258,
                                        'virtual_nw_x_pixel': 981170058,
                                        'virtual_nw_y_pixel': -1371052200,
                                        'virtual_width': 283146088,
                                        'virtual_height': -1507027036,
                                    },
                        ],
                },
                {
                    'description': 'À˕Çнƨ\x90ƟщУНԫè˦UāɘˏÚˮǄîƆĲͽĹБβL˗˲',
                    'monitors': [
                            {
                                        'identifier': 5783205,
                                        'width': -2621876905920656405,
                                        'height': -1592719614951435143,
                                    },
                            {
                                        'identifier': 4990025,
                                        'width': -9031748205678511103,
                                        'height': -7553686721875305918,
                                    },
                            {
                                        'identifier': 1677956,
                                        'width': 2827024243693798680,
                                        'height': -5654125198448339049,
                                    },
                            {
                                        'identifier': 7921203,
                                        'width': 4789450007443299108,
                                        'height': -9199635178050858998,
                                    },
                            {
                                        'identifier': 7638593,
                                        'width': -4837803815054180413,
                                        'height': -6895899007608185729,
                                    },
                            {
                                        'identifier': 24454,
                                        'width': 5818996589540294424,
                                        'height': 7056458031573135140,
                                    },
                            {
                                        'identifier': -971707,
                                        'width': -1014105749028603022,
                                        'height': 6249423093041705554,
                                    },
                            {
                                        'identifier': 7434287,
                                        'width': -7230214709960873816,
                                        'height': -6049418817733067199,
                                    },
                            {
                                        'identifier': 235176,
                                        'width': -3861229559417329923,
                                        'height': 1798753336275066242,
                                    },
                            {
                                        'identifier': 9897725,
                                        'width': -2414323669112952552,
                                        'height': 643877556816616867,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 562081,
                                        'source_nw_x_pixel': -2701080175870466940,
                                        'source_nw_y_pixel': -1305386805270936174,
                                        'source_pixel_width': -7248981961675801541,
                                        'source_pixel_height': -8331153444560464615,
                                        'rotation': -7478802712736262549,
                                        'virtual_nw_x_pixel': 189966329,
                                        'virtual_nw_y_pixel': 449356718,
                                        'virtual_width': 909222366,
                                        'virtual_height': -100676671,
                                    },
                            {
                                        'source_monitor': 6589666,
                                        'source_nw_x_pixel': -6037163108436103705,
                                        'source_nw_y_pixel': -5508719747069794695,
                                        'source_pixel_width': -6548207075185516811,
                                        'source_pixel_height': -1859272249196344758,
                                        'rotation': -8040343258153327657,
                                        'virtual_nw_x_pixel': 91522868,
                                        'virtual_nw_y_pixel': 1672910462,
                                        'virtual_width': 646647429,
                                        'virtual_height': -466554346,
                                    },
                            {
                                        'source_monitor': 9576657,
                                        'source_nw_x_pixel': -5233380206674752298,
                                        'source_nw_y_pixel': -8108593952953055323,
                                        'source_pixel_width': -2877706673837633381,
                                        'source_pixel_height': -6287141961797381917,
                                        'rotation': -8073263451373878224,
                                        'virtual_nw_x_pixel': 1569178836,
                                        'virtual_nw_y_pixel': 1938696938,
                                        'virtual_width': 1183105975,
                                        'virtual_height': -124930805,
                                    },
                            {
                                        'source_monitor': 1703396,
                                        'source_nw_x_pixel': -5507227474531775107,
                                        'source_nw_y_pixel': -2847381339792114446,
                                        'source_pixel_width': -5738033801931952468,
                                        'source_pixel_height': -608489470725923527,
                                        'rotation': -5181876600408102983,
                                        'virtual_nw_x_pixel': -1727614305,
                                        'virtual_nw_y_pixel': -1408824015,
                                        'virtual_width': -1774268306,
                                        'virtual_height': -1985734549,
                                    },
                            {
                                        'source_monitor': 4612258,
                                        'source_nw_x_pixel': -1327364415096323413,
                                        'source_nw_y_pixel': -2129501364914524138,
                                        'source_pixel_width': -8563794445232099747,
                                        'source_pixel_height': -1019752524441920947,
                                        'rotation': -1849396041098029308,
                                        'virtual_nw_x_pixel': -638560221,
                                        'virtual_nw_y_pixel': -13998087,
                                        'virtual_width': -475291322,
                                        'virtual_height': -960652387,
                                    },
                            {
                                        'source_monitor': 4294261,
                                        'source_nw_x_pixel': -6280375051715857611,
                                        'source_nw_y_pixel': -4452605670474031842,
                                        'source_pixel_width': -7422189425870180396,
                                        'source_pixel_height': -5412447954354155697,
                                        'rotation': -3896059435212982189,
                                        'virtual_nw_x_pixel': -679968454,
                                        'virtual_nw_y_pixel': -1162195162,
                                        'virtual_width': -1953805522,
                                        'virtual_height': 690767882,
                                    },
                            {
                                        'source_monitor': 1694062,
                                        'source_nw_x_pixel': -3561310842848833796,
                                        'source_nw_y_pixel': -3485479961217092338,
                                        'source_pixel_width': -2510422168988535182,
                                        'source_pixel_height': -9202033332466561868,
                                        'rotation': -7778071307968756075,
                                        'virtual_nw_x_pixel': -579045489,
                                        'virtual_nw_y_pixel': 1535641914,
                                        'virtual_width': -1958032944,
                                        'virtual_height': -1040378400,
                                    },
                            {
                                        'source_monitor': 2692045,
                                        'source_nw_x_pixel': -6485575099257987987,
                                        'source_nw_y_pixel': -8383581102356551033,
                                        'source_pixel_width': -1681193071825222071,
                                        'source_pixel_height': -8404825319048020840,
                                        'rotation': -7465863402801638343,
                                        'virtual_nw_x_pixel': 1022393224,
                                        'virtual_nw_y_pixel': -1630918126,
                                        'virtual_width': -1260236851,
                                        'virtual_height': 337271488,
                                    },
                            {
                                        'source_monitor': 3601825,
                                        'source_nw_x_pixel': -2815665584694136065,
                                        'source_nw_y_pixel': -6284167720557806769,
                                        'source_pixel_width': -7705646540846757242,
                                        'source_pixel_height': -2522536652651484653,
                                        'rotation': -2359370145028851305,
                                        'virtual_nw_x_pixel': 1589133735,
                                        'virtual_nw_y_pixel': -114907752,
                                        'virtual_width': -268317826,
                                        'virtual_height': -1232977222,
                                    },
                            {
                                        'source_monitor': 8785161,
                                        'source_nw_x_pixel': -4636212802394437269,
                                        'source_nw_y_pixel': -5413983930290023812,
                                        'source_pixel_width': -3119890577354931298,
                                        'source_pixel_height': -4640083155785831708,
                                        'rotation': -5784893213906221609,
                                        'virtual_nw_x_pixel': -467131388,
                                        'virtual_nw_y_pixel': 951109851,
                                        'virtual_width': 271367554,
                                        'virtual_height': 1694443450,
                                    },
                        ],
                },
                {
                    'description': "ӻp˲ȭΛ»ѺʁҁŸ6ƌӕŪȞ϶ӘҢĘё\x85˚ǕӋʶž҂'ȜȂ",
                    'monitors': [
                            {
                                        'identifier': 690133,
                                        'width': -3991289294464368719,
                                        'height': -6745440010412247817,
                                    },
                            {
                                        'identifier': 6816039,
                                        'width': 6747351442844540252,
                                        'height': -3869910560931617796,
                                    },
                            {
                                        'identifier': 4918924,
                                        'width': -7271493076421256520,
                                        'height': -1283620894640401333,
                                    },
                            {
                                        'identifier': 2303424,
                                        'width': 3420534512569589492,
                                        'height': 492573325894995111,
                                    },
                            {
                                        'identifier': 3599288,
                                        'width': 7509161899586318093,
                                        'height': -403919466939282475,
                                    },
                            {
                                        'identifier': 8089318,
                                        'width': 270733524947383920,
                                        'height': -3629383249589301350,
                                    },
                            {
                                        'identifier': 7532596,
                                        'width': -3827459665803846436,
                                        'height': -5937526118526013104,
                                    },
                            {
                                        'identifier': 2044805,
                                        'width': -4206638582293186708,
                                        'height': 7383438594894415654,
                                    },
                            {
                                        'identifier': 7453296,
                                        'width': 5969796627549843165,
                                        'height': 6569895129840637168,
                                    },
                            {
                                        'identifier': 701051,
                                        'width': 8608767420822543967,
                                        'height': -5518914321325362304,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2345172,
                                        'source_nw_x_pixel': -7373191230343391597,
                                        'source_nw_y_pixel': -5975634411007086619,
                                        'source_pixel_width': -6661321135963474039,
                                        'source_pixel_height': -9172945399546131845,
                                        'rotation': -3650266396842206175,
                                        'virtual_nw_x_pixel': -488257414,
                                        'virtual_nw_y_pixel': -1172242148,
                                        'virtual_width': 610392322,
                                        'virtual_height': -1407603117,
                                    },
                            {
                                        'source_monitor': 1217010,
                                        'source_nw_x_pixel': -2052215071849463437,
                                        'source_nw_y_pixel': -1819570610358136079,
                                        'source_pixel_width': -4364335875139298786,
                                        'source_pixel_height': -9011187697442146245,
                                        'rotation': -6239745138803910536,
                                        'virtual_nw_x_pixel': -1293540555,
                                        'virtual_nw_y_pixel': 1010506407,
                                        'virtual_width': 535250945,
                                        'virtual_height': -721757352,
                                    },
                            {
                                        'source_monitor': 881541,
                                        'source_nw_x_pixel': -4139744075399450140,
                                        'source_nw_y_pixel': -9178075938427082557,
                                        'source_pixel_width': -5146040822345876567,
                                        'source_pixel_height': -6204127853300711458,
                                        'rotation': -6785541725130420339,
                                        'virtual_nw_x_pixel': 408401556,
                                        'virtual_nw_y_pixel': -1145385021,
                                        'virtual_width': -191787037,
                                        'virtual_height': -1302663555,
                                    },
                            {
                                        'source_monitor': 9709095,
                                        'source_nw_x_pixel': -4595101333232817503,
                                        'source_nw_y_pixel': -2526654702375620761,
                                        'source_pixel_width': -8434517059152128795,
                                        'source_pixel_height': -7489229048531504733,
                                        'rotation': -5030323787639808032,
                                        'virtual_nw_x_pixel': 1054101744,
                                        'virtual_nw_y_pixel': 359062572,
                                        'virtual_width': 1390927791,
                                        'virtual_height': 1842543869,
                                    },
                            {
                                        'source_monitor': 311418,
                                        'source_nw_x_pixel': -2468511146001000189,
                                        'source_nw_y_pixel': -1938348952803585459,
                                        'source_pixel_width': -5315112276470788212,
                                        'source_pixel_height': -5135468318125895137,
                                        'rotation': -462064828259243543,
                                        'virtual_nw_x_pixel': 924088277,
                                        'virtual_nw_y_pixel': -102036709,
                                        'virtual_width': -546620963,
                                        'virtual_height': 742484099,
                                    },
                            {
                                        'source_monitor': 411121,
                                        'source_nw_x_pixel': -425105580013135584,
                                        'source_nw_y_pixel': -7135575687709677549,
                                        'source_pixel_width': -7234769067889962543,
                                        'source_pixel_height': -5179910383605417114,
                                        'rotation': -8611962295080821128,
                                        'virtual_nw_x_pixel': -1677623416,
                                        'virtual_nw_y_pixel': -196592618,
                                        'virtual_width': -1460447702,
                                        'virtual_height': -828987185,
                                    },
                            {
                                        'source_monitor': 9847719,
                                        'source_nw_x_pixel': -5241770141623342227,
                                        'source_nw_y_pixel': -2839709351231310844,
                                        'source_pixel_width': -4095428167385912601,
                                        'source_pixel_height': -7322029163999019764,
                                        'rotation': -3957339534550281103,
                                        'virtual_nw_x_pixel': 1394974673,
                                        'virtual_nw_y_pixel': 207298767,
                                        'virtual_width': -1797463082,
                                        'virtual_height': 143972579,
                                    },
                            {
                                        'source_monitor': 3176231,
                                        'source_nw_x_pixel': -8278604372563771390,
                                        'source_nw_y_pixel': -4774006398534532969,
                                        'source_pixel_width': -7720485558077120499,
                                        'source_pixel_height': -1847676985847870948,
                                        'rotation': -2967758164769973882,
                                        'virtual_nw_x_pixel': -1373974343,
                                        'virtual_nw_y_pixel': -766635499,
                                        'virtual_width': 1991549370,
                                        'virtual_height': 1846729243,
                                    },
                            {
                                        'source_monitor': 8104329,
                                        'source_nw_x_pixel': -5055155287776924925,
                                        'source_nw_y_pixel': -2773150853820784852,
                                        'source_pixel_width': -1432977502695841188,
                                        'source_pixel_height': -6689877563346927155,
                                        'rotation': -7492181069474963047,
                                        'virtual_nw_x_pixel': -981597002,
                                        'virtual_nw_y_pixel': -894870504,
                                        'virtual_width': -1474175864,
                                        'virtual_height': -828184754,
                                    },
                            {
                                        'source_monitor': 4382587,
                                        'source_nw_x_pixel': -1808422136394968772,
                                        'source_nw_y_pixel': -9211951375188996570,
                                        'source_pixel_width': -5966440227175266804,
                                        'source_pixel_height': -8289813864196040520,
                                        'rotation': -889983962892105003,
                                        'virtual_nw_x_pixel': 1164292291,
                                        'virtual_nw_y_pixel': -1057971791,
                                        'virtual_width': -609657569,
                                        'virtual_height': 1978429764,
                                    },
                        ],
                },
                {
                    'description': 'ƇҮńĶèΡӰ(ȔϣǏԏѱĺƃʂȤҀԜȨӢĪӧ˃ҳϙYɩąϫ',
                    'monitors': [
                            {
                                        'identifier': 9403424,
                                        'width': -1604270401843078929,
                                        'height': 849008642577458570,
                                    },
                            {
                                        'identifier': 6723381,
                                        'width': -2193683613503040078,
                                        'height': -1238434652000388725,
                                    },
                            {
                                        'identifier': 7876433,
                                        'width': 6322769761982911905,
                                        'height': 2693923061456798540,
                                    },
                            {
                                        'identifier': 6835709,
                                        'width': -9218476906405647284,
                                        'height': 2256247033172907835,
                                    },
                            {
                                        'identifier': 9896940,
                                        'width': -2616963126511039941,
                                        'height': -1484358019756250387,
                                    },
                            {
                                        'identifier': 637332,
                                        'width': 8278037489571040205,
                                        'height': -6977642025139727180,
                                    },
                            {
                                        'identifier': 9885571,
                                        'width': 242956250540096190,
                                        'height': 6435735194717733049,
                                    },
                            {
                                        'identifier': 165665,
                                        'width': 2866520064506452929,
                                        'height': -2176313639364008496,
                                    },
                            {
                                        'identifier': 8164932,
                                        'width': -3799699392856004428,
                                        'height': 8401372253637711849,
                                    },
                            {
                                        'identifier': 8759883,
                                        'width': -1986831661280578735,
                                        'height': -3816807879407710384,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7448558,
                                        'source_nw_x_pixel': -4502878918920057174,
                                        'source_nw_y_pixel': -4794595419340251908,
                                        'source_pixel_width': -6063022743018614149,
                                        'source_pixel_height': -683324054948859953,
                                        'rotation': -2782381762751754061,
                                        'virtual_nw_x_pixel': 1416638365,
                                        'virtual_nw_y_pixel': -1270975961,
                                        'virtual_width': -1171529593,
                                        'virtual_height': -1810181506,
                                    },
                            {
                                        'source_monitor': 8112651,
                                        'source_nw_x_pixel': -6000149179990576453,
                                        'source_nw_y_pixel': -4661208855767133751,
                                        'source_pixel_width': -4193253829906870030,
                                        'source_pixel_height': -7892643632639567509,
                                        'rotation': -2941195634963488773,
                                        'virtual_nw_x_pixel': -95761674,
                                        'virtual_nw_y_pixel': -20010735,
                                        'virtual_width': 1079678452,
                                        'virtual_height': -1565374455,
                                    },
                            {
                                        'source_monitor': 6716457,
                                        'source_nw_x_pixel': -2625185030693224291,
                                        'source_nw_y_pixel': -1915208593037056577,
                                        'source_pixel_width': -1318809177844922536,
                                        'source_pixel_height': -2944039604396923254,
                                        'rotation': -4812680824396684164,
                                        'virtual_nw_x_pixel': -738434041,
                                        'virtual_nw_y_pixel': -1207926689,
                                        'virtual_width': -1340432543,
                                        'virtual_height': 742127634,
                                    },
                            {
                                        'source_monitor': 8170131,
                                        'source_nw_x_pixel': -686797642280083800,
                                        'source_nw_y_pixel': -7726409524485879832,
                                        'source_pixel_width': -2626145039880027172,
                                        'source_pixel_height': -9024367226012439655,
                                        'rotation': -2726866543215412720,
                                        'virtual_nw_x_pixel': -509225424,
                                        'virtual_nw_y_pixel': 1631709412,
                                        'virtual_width': 1383056812,
                                        'virtual_height': -372479783,
                                    },
                            {
                                        'source_monitor': 1159614,
                                        'source_nw_x_pixel': -3544041529075031396,
                                        'source_nw_y_pixel': -5359261007791954193,
                                        'source_pixel_width': -1856169256080225331,
                                        'source_pixel_height': -8497817143735606387,
                                        'rotation': -6773079405338211783,
                                        'virtual_nw_x_pixel': -179033601,
                                        'virtual_nw_y_pixel': -655934055,
                                        'virtual_width': 848958833,
                                        'virtual_height': -466361078,
                                    },
                            {
                                        'source_monitor': 3542659,
                                        'source_nw_x_pixel': -3677827479375951968,
                                        'source_nw_y_pixel': -3526853102924260508,
                                        'source_pixel_width': -8057854296061805525,
                                        'source_pixel_height': -6343931579734345872,
                                        'rotation': -2826009397861509549,
                                        'virtual_nw_x_pixel': 1535251948,
                                        'virtual_nw_y_pixel': 1129005898,
                                        'virtual_width': 406603714,
                                        'virtual_height': 1928667533,
                                    },
                            {
                                        'source_monitor': 9880404,
                                        'source_nw_x_pixel': -1728716261624221399,
                                        'source_nw_y_pixel': -1450393690763255094,
                                        'source_pixel_width': -505777217775926242,
                                        'source_pixel_height': -7584949502691948584,
                                        'rotation': -625404807699026111,
                                        'virtual_nw_x_pixel': -1001059240,
                                        'virtual_nw_y_pixel': -1287208890,
                                        'virtual_width': -988988280,
                                        'virtual_height': -565286305,
                                    },
                            {
                                        'source_monitor': 2558141,
                                        'source_nw_x_pixel': -3347431312749621100,
                                        'source_nw_y_pixel': -6701738143515690256,
                                        'source_pixel_width': -7407051478092605787,
                                        'source_pixel_height': -287025612296573399,
                                        'rotation': -5272954368105174121,
                                        'virtual_nw_x_pixel': 1810675237,
                                        'virtual_nw_y_pixel': 672999455,
                                        'virtual_width': 629014727,
                                        'virtual_height': -1505312173,
                                    },
                            {
                                        'source_monitor': 6368082,
                                        'source_nw_x_pixel': -5256361386974723557,
                                        'source_nw_y_pixel': -8857893833081168792,
                                        'source_pixel_width': -3929353718328599447,
                                        'source_pixel_height': -5611081942281492067,
                                        'rotation': -3440585149083750034,
                                        'virtual_nw_x_pixel': -139804847,
                                        'virtual_nw_y_pixel': -1361458991,
                                        'virtual_width': 1527935340,
                                        'virtual_height': 1923948990,
                                    },
                            {
                                        'source_monitor': 8624903,
                                        'source_nw_x_pixel': -1913212543346340583,
                                        'source_nw_y_pixel': -229301103916772265,
                                        'source_pixel_width': -427294070320322417,
                                        'source_pixel_height': -6021619255597999614,
                                        'rotation': -6296010403151524785,
                                        'virtual_nw_x_pixel': 789127710,
                                        'virtual_nw_y_pixel': 1794154954,
                                        'virtual_width': -1856359093,
                                        'virtual_height': 1625513116,
                                    },
                        ],
                },
                {
                    'description': 'ԞӕűƂɘǡͺІíǒɞ͵үгˣԂɰ\x82&ĊԉЂñϥӡњǀѱįƝ',
                    'monitors': [
                            {
                                        'identifier': 6008922,
                                        'width': 29639575998492341,
                                        'height': -3478450137560115815,
                                    },
                            {
                                        'identifier': 1026825,
                                        'width': -7169717659276705376,
                                        'height': 7384536925696174443,
                                    },
                            {
                                        'identifier': 5357421,
                                        'width': 2780651446718145475,
                                        'height': 5432748622683315103,
                                    },
                            {
                                        'identifier': 9075715,
                                        'width': -1601699620586860098,
                                        'height': -692192878240657988,
                                    },
                            {
                                        'identifier': 6847525,
                                        'width': 8329216625390108253,
                                        'height': -488760788839595822,
                                    },
                            {
                                        'identifier': -947459,
                                        'width': -4076470683012200791,
                                        'height': -61258767746013442,
                                    },
                            {
                                        'identifier': 3454426,
                                        'width': -1468340395638232737,
                                        'height': -3484894951781480285,
                                    },
                            {
                                        'identifier': 5782311,
                                        'width': 3946785831951822593,
                                        'height': -6107997324880342393,
                                    },
                            {
                                        'identifier': 1720666,
                                        'width': 2624941151172327118,
                                        'height': 8473663280796492871,
                                    },
                            {
                                        'identifier': 2145433,
                                        'width': -1847192969730797381,
                                        'height': -2486217419397487044,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9843743,
                                        'source_nw_x_pixel': -3341213625027591211,
                                        'source_nw_y_pixel': -777749163137553414,
                                        'source_pixel_width': -1194679391831785369,
                                        'source_pixel_height': -6533007494583350395,
                                        'rotation': -6863970609684626671,
                                        'virtual_nw_x_pixel': -1419071784,
                                        'virtual_nw_y_pixel': -373540221,
                                        'virtual_width': 1793790989,
                                        'virtual_height': -1155751897,
                                    },
                            {
                                        'source_monitor': 1711417,
                                        'source_nw_x_pixel': -8699884509979428061,
                                        'source_nw_y_pixel': -4706700250998186680,
                                        'source_pixel_width': -3836344779584239301,
                                        'source_pixel_height': -1814547138306005724,
                                        'rotation': -3649204760121802391,
                                        'virtual_nw_x_pixel': 567647372,
                                        'virtual_nw_y_pixel': -1453196097,
                                        'virtual_width': 891270522,
                                        'virtual_height': 1616690080,
                                    },
                            {
                                        'source_monitor': 2758180,
                                        'source_nw_x_pixel': -6625451793843813701,
                                        'source_nw_y_pixel': -8992993017169982358,
                                        'source_pixel_width': -8622122786450945440,
                                        'source_pixel_height': -3133479969597501121,
                                        'rotation': -987920340614256060,
                                        'virtual_nw_x_pixel': -229932886,
                                        'virtual_nw_y_pixel': -506887794,
                                        'virtual_width': 811453822,
                                        'virtual_height': 274052418,
                                    },
                            {
                                        'source_monitor': -883934,
                                        'source_nw_x_pixel': -7803458458672438290,
                                        'source_nw_y_pixel': -6021401081794903219,
                                        'source_pixel_width': -6168843475602245900,
                                        'source_pixel_height': -4999882875963657530,
                                        'rotation': -3017185817721831893,
                                        'virtual_nw_x_pixel': 749057948,
                                        'virtual_nw_y_pixel': -938480949,
                                        'virtual_width': 1032669871,
                                        'virtual_height': -1420134135,
                                    },
                            {
                                        'source_monitor': 1650437,
                                        'source_nw_x_pixel': -1808321855026618907,
                                        'source_nw_y_pixel': -7232719526518617537,
                                        'source_pixel_width': -6836849237475990655,
                                        'source_pixel_height': -6577044747298031669,
                                        'rotation': -5564785068083829376,
                                        'virtual_nw_x_pixel': -864849916,
                                        'virtual_nw_y_pixel': 762754002,
                                        'virtual_width': 1171955101,
                                        'virtual_height': 1193084315,
                                    },
                            {
                                        'source_monitor': 3204147,
                                        'source_nw_x_pixel': -4937731751396068096,
                                        'source_nw_y_pixel': -478817582549705521,
                                        'source_pixel_width': -7707559181100108955,
                                        'source_pixel_height': -4071406017264134068,
                                        'rotation': -368190777587575560,
                                        'virtual_nw_x_pixel': 1494264108,
                                        'virtual_nw_y_pixel': -1950234265,
                                        'virtual_width': -1510288102,
                                        'virtual_height': 405400376,
                                    },
                            {
                                        'source_monitor': -206165,
                                        'source_nw_x_pixel': -4793437969568505034,
                                        'source_nw_y_pixel': -4812820616578715332,
                                        'source_pixel_width': -2294301167662498894,
                                        'source_pixel_height': -4505864914901004998,
                                        'rotation': -3811994735968738364,
                                        'virtual_nw_x_pixel': -1074469737,
                                        'virtual_nw_y_pixel': -617858765,
                                        'virtual_width': 752109699,
                                        'virtual_height': 141139588,
                                    },
                            {
                                        'source_monitor': 7956206,
                                        'source_nw_x_pixel': -7296440696327179188,
                                        'source_nw_y_pixel': -6944944174472405619,
                                        'source_pixel_width': -5615861225129593539,
                                        'source_pixel_height': -5383458216996479634,
                                        'rotation': -97938103991026621,
                                        'virtual_nw_x_pixel': 317749700,
                                        'virtual_nw_y_pixel': 452611247,
                                        'virtual_width': 1191960821,
                                        'virtual_height': 1739094728,
                                    },
                            {
                                        'source_monitor': 1208250,
                                        'source_nw_x_pixel': -6413419220226330082,
                                        'source_nw_y_pixel': -4254102786281675911,
                                        'source_pixel_width': -6976001737203651110,
                                        'source_pixel_height': -1152262657018951811,
                                        'rotation': -7005507262430960118,
                                        'virtual_nw_x_pixel': 1772581756,
                                        'virtual_nw_y_pixel': 108909787,
                                        'virtual_width': -879171457,
                                        'virtual_height': -273323644,
                                    },
                            {
                                        'source_monitor': 1240557,
                                        'source_nw_x_pixel': -707957558691965946,
                                        'source_nw_y_pixel': -4437102601438423490,
                                        'source_pixel_width': -2764118650466138676,
                                        'source_pixel_height': -1965509624026023349,
                                        'rotation': -2930316036323065639,
                                        'virtual_nw_x_pixel': -385165142,
                                        'virtual_nw_y_pixel': 1642447560,
                                        'virtual_width': 1059550324,
                                        'virtual_height': 707883187,
                                    },
                        ],
                },
                {
                    'description': 'Ơ´îϩāÓǕǹԭɿТ˗гřǂBǯɜѼт\x99ǛwŔɱȜц©ɡȿ',
                    'monitors': [
                            {
                                        'identifier': 4723404,
                                        'width': 1594239397291322809,
                                        'height': 2845049615288904293,
                                    },
                            {
                                        'identifier': 2438127,
                                        'width': -7729652432276154627,
                                        'height': 1420846404710480006,
                                    },
                            {
                                        'identifier': 9119540,
                                        'width': -595164917607436249,
                                        'height': 8917621987526044210,
                                    },
                            {
                                        'identifier': 5076005,
                                        'width': 9209853458598516095,
                                        'height': 7280090352410939557,
                                    },
                            {
                                        'identifier': 279963,
                                        'width': 1613074480511975903,
                                        'height': 6648914118278557285,
                                    },
                            {
                                        'identifier': 9300551,
                                        'width': 4283344402677947887,
                                        'height': -2499708082179942767,
                                    },
                            {
                                        'identifier': 305473,
                                        'width': -5986207293355696325,
                                        'height': 3408593755537181109,
                                    },
                            {
                                        'identifier': 5018267,
                                        'width': -4082456927617645696,
                                        'height': -6929442235128535542,
                                    },
                            {
                                        'identifier': 6179433,
                                        'width': 2238248048781955001,
                                        'height': 4379088049461631858,
                                    },
                            {
                                        'identifier': 9480557,
                                        'width': 1309627289587530650,
                                        'height': 4412972670312181942,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 928353,
                                        'source_nw_x_pixel': -1399271140819624436,
                                        'source_nw_y_pixel': -3782294478455930090,
                                        'source_pixel_width': -7512199976817101746,
                                        'source_pixel_height': -1275032892122171730,
                                        'rotation': -2630250526217322541,
                                        'virtual_nw_x_pixel': 1543606523,
                                        'virtual_nw_y_pixel': -18847377,
                                        'virtual_width': -1955200654,
                                        'virtual_height': -1721197540,
                                    },
                            {
                                        'source_monitor': 9529187,
                                        'source_nw_x_pixel': -2909902958344644605,
                                        'source_nw_y_pixel': -867121401265609500,
                                        'source_pixel_width': -8207798147026841803,
                                        'source_pixel_height': -2201655799870752001,
                                        'rotation': -6285271872298889376,
                                        'virtual_nw_x_pixel': 1699864002,
                                        'virtual_nw_y_pixel': -634466683,
                                        'virtual_width': -319824788,
                                        'virtual_height': 667011179,
                                    },
                            {
                                        'source_monitor': 5732160,
                                        'source_nw_x_pixel': -5409152975999077727,
                                        'source_nw_y_pixel': -875233416603769670,
                                        'source_pixel_width': -1577438028954765937,
                                        'source_pixel_height': -1147537938802229876,
                                        'rotation': -6039500426635014466,
                                        'virtual_nw_x_pixel': -794493583,
                                        'virtual_nw_y_pixel': -499255593,
                                        'virtual_width': 416005354,
                                        'virtual_height': -1066112554,
                                    },
                            {
                                        'source_monitor': 3877847,
                                        'source_nw_x_pixel': -2363498943234399849,
                                        'source_nw_y_pixel': -6591177476757881705,
                                        'source_pixel_width': -6906214788831263270,
                                        'source_pixel_height': -6613863190436956486,
                                        'rotation': -4469371841689534683,
                                        'virtual_nw_x_pixel': -1939411196,
                                        'virtual_nw_y_pixel': 1694733885,
                                        'virtual_width': 1978138063,
                                        'virtual_height': -1126014123,
                                    },
                            {
                                        'source_monitor': 5977002,
                                        'source_nw_x_pixel': -8983524913544874304,
                                        'source_nw_y_pixel': -8017954119439550960,
                                        'source_pixel_width': -3871273672270551946,
                                        'source_pixel_height': -4581269359602190318,
                                        'rotation': -7438130380370761975,
                                        'virtual_nw_x_pixel': 683999470,
                                        'virtual_nw_y_pixel': 1626896096,
                                        'virtual_width': -1025942756,
                                        'virtual_height': 265291009,
                                    },
                            {
                                        'source_monitor': 9453713,
                                        'source_nw_x_pixel': -1939585411440537625,
                                        'source_nw_y_pixel': -4742527481292050665,
                                        'source_pixel_width': -7803768804113488419,
                                        'source_pixel_height': -10626031883741427,
                                        'rotation': -5087348065880898970,
                                        'virtual_nw_x_pixel': -678921286,
                                        'virtual_nw_y_pixel': 602135537,
                                        'virtual_width': -1245029962,
                                        'virtual_height': -613679730,
                                    },
                            {
                                        'source_monitor': 6601618,
                                        'source_nw_x_pixel': -7399911952158096916,
                                        'source_nw_y_pixel': -6014427741290814962,
                                        'source_pixel_width': -1381078340763689579,
                                        'source_pixel_height': -5887588782763994119,
                                        'rotation': -166831680459190070,
                                        'virtual_nw_x_pixel': 54579648,
                                        'virtual_nw_y_pixel': -881836450,
                                        'virtual_width': -862950436,
                                        'virtual_height': -1290987860,
                                    },
                            {
                                        'source_monitor': 5033897,
                                        'source_nw_x_pixel': -1276515951354576960,
                                        'source_nw_y_pixel': -1087073584181661823,
                                        'source_pixel_width': -9172201059080989872,
                                        'source_pixel_height': -8651218519440177050,
                                        'rotation': -6497543504304284680,
                                        'virtual_nw_x_pixel': 709305319,
                                        'virtual_nw_y_pixel': -1512544393,
                                        'virtual_width': -756868884,
                                        'virtual_height': 747598436,
                                    },
                            {
                                        'source_monitor': 8048138,
                                        'source_nw_x_pixel': -8648853982811592107,
                                        'source_nw_y_pixel': -4283415962215892835,
                                        'source_pixel_width': -1153199332096358800,
                                        'source_pixel_height': -199462445090788674,
                                        'rotation': -3358821838065384184,
                                        'virtual_nw_x_pixel': -1887448889,
                                        'virtual_nw_y_pixel': 1468199706,
                                        'virtual_width': 1596902295,
                                        'virtual_height': 1651965637,
                                    },
                            {
                                        'source_monitor': 7437832,
                                        'source_nw_x_pixel': -5843758939167832,
                                        'source_nw_y_pixel': -8423210585323512963,
                                        'source_pixel_width': -7120797216597294382,
                                        'source_pixel_height': -4911772671796105588,
                                        'rotation': -8810610760679553762,
                                        'virtual_nw_x_pixel': 195900273,
                                        'virtual_nw_y_pixel': 788607131,
                                        'virtual_width': -475912950,
                                        'virtual_height': 527676730,
                                    },
                        ],
                },
                {
                    'description': 'жdЌř\x8cͼ^Ƹ4ɷcӛѦͺˑQӢҭ(УėOmĨčԉяȱҎ»',
                    'monitors': [
                            {
                                        'identifier': 7825838,
                                        'width': 1822064646285010181,
                                        'height': -4688970190502808902,
                                    },
                            {
                                        'identifier': 8748291,
                                        'width': -806757234829976044,
                                        'height': -218382959496414749,
                                    },
                            {
                                        'identifier': 8873841,
                                        'width': 8218374706317043326,
                                        'height': -4530230943099225488,
                                    },
                            {
                                        'identifier': 5571078,
                                        'width': -140908722141925486,
                                        'height': 7286232866529453047,
                                    },
                            {
                                        'identifier': 2001609,
                                        'width': -6422008847065038632,
                                        'height': -5266942800907733413,
                                    },
                            {
                                        'identifier': 3559494,
                                        'width': 4281788034842377975,
                                        'height': 8897285142905480031,
                                    },
                            {
                                        'identifier': 3729592,
                                        'width': -3256458119156517261,
                                        'height': -475801472663091960,
                                    },
                            {
                                        'identifier': 3039847,
                                        'width': 7342200951252743519,
                                        'height': 1428440337839795141,
                                    },
                            {
                                        'identifier': 3285594,
                                        'width': -54836531939029126,
                                        'height': -1045935774724560457,
                                    },
                            {
                                        'identifier': 7183075,
                                        'width': 1836714449361161198,
                                        'height': -7068275716858969798,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3935959,
                                        'source_nw_x_pixel': -7588281976785296141,
                                        'source_nw_y_pixel': -2739511048334392225,
                                        'source_pixel_width': -2574615830531428676,
                                        'source_pixel_height': -2540512791549268050,
                                        'rotation': -291871267321372304,
                                        'virtual_nw_x_pixel': -309638199,
                                        'virtual_nw_y_pixel': 1203327804,
                                        'virtual_width': 1400620483,
                                        'virtual_height': -332717887,
                                    },
                            {
                                        'source_monitor': 5529592,
                                        'source_nw_x_pixel': -2051507557712490435,
                                        'source_nw_y_pixel': -2652204545515075734,
                                        'source_pixel_width': -7096794701349834789,
                                        'source_pixel_height': -6687038984035712537,
                                        'rotation': -6312639556249523521,
                                        'virtual_nw_x_pixel': 697492681,
                                        'virtual_nw_y_pixel': 650108760,
                                        'virtual_width': 1744045,
                                        'virtual_height': -475311744,
                                    },
                            {
                                        'source_monitor': 62924,
                                        'source_nw_x_pixel': -4437895640642425267,
                                        'source_nw_y_pixel': -4702435712652410566,
                                        'source_pixel_width': -5216554660761640886,
                                        'source_pixel_height': -3562004268503995049,
                                        'rotation': -3071089874457612876,
                                        'virtual_nw_x_pixel': -1451277211,
                                        'virtual_nw_y_pixel': -40426367,
                                        'virtual_width': 1812145866,
                                        'virtual_height': -1166333630,
                                    },
                            {
                                        'source_monitor': 2668905,
                                        'source_nw_x_pixel': -4441198380798134559,
                                        'source_nw_y_pixel': -8059110417518044531,
                                        'source_pixel_width': -2850286878415205668,
                                        'source_pixel_height': -1720294449835979088,
                                        'rotation': -5538149946512712315,
                                        'virtual_nw_x_pixel': 1442032093,
                                        'virtual_nw_y_pixel': 488435030,
                                        'virtual_width': -1045652737,
                                        'virtual_height': -1909084563,
                                    },
                            {
                                        'source_monitor': -850903,
                                        'source_nw_x_pixel': -349580374392363392,
                                        'source_nw_y_pixel': -4884652141883787816,
                                        'source_pixel_width': -8308068881817969825,
                                        'source_pixel_height': -1090572099050920179,
                                        'rotation': -7578938265048243043,
                                        'virtual_nw_x_pixel': 170418170,
                                        'virtual_nw_y_pixel': -1656315434,
                                        'virtual_width': -1485769495,
                                        'virtual_height': 1416165217,
                                    },
                            {
                                        'source_monitor': 7148271,
                                        'source_nw_x_pixel': -3547456743121071866,
                                        'source_nw_y_pixel': -5472160083148662826,
                                        'source_pixel_width': -2875774962539305138,
                                        'source_pixel_height': -107962628656801753,
                                        'rotation': -7877312734949628081,
                                        'virtual_nw_x_pixel': 1563867255,
                                        'virtual_nw_y_pixel': 56785639,
                                        'virtual_width': -1189461433,
                                        'virtual_height': -1793353784,
                                    },
                            {
                                        'source_monitor': 2609842,
                                        'source_nw_x_pixel': -8653936213233983127,
                                        'source_nw_y_pixel': -5734939427898177640,
                                        'source_pixel_width': -7663821873000171464,
                                        'source_pixel_height': -972921420949358776,
                                        'rotation': -5336352924943388067,
                                        'virtual_nw_x_pixel': 1613435708,
                                        'virtual_nw_y_pixel': 1498035301,
                                        'virtual_width': -1727715798,
                                        'virtual_height': -1185995210,
                                    },
                            {
                                        'source_monitor': -139736,
                                        'source_nw_x_pixel': -6369285219739741846,
                                        'source_nw_y_pixel': -1420623317204164723,
                                        'source_pixel_width': -3562400103036956839,
                                        'source_pixel_height': -600734595476184263,
                                        'rotation': -3049194978620389262,
                                        'virtual_nw_x_pixel': -441957811,
                                        'virtual_nw_y_pixel': -1149110570,
                                        'virtual_width': 1931782097,
                                        'virtual_height': 430874598,
                                    },
                            {
                                        'source_monitor': 6004746,
                                        'source_nw_x_pixel': -2911103214201436740,
                                        'source_nw_y_pixel': -8897847875781681469,
                                        'source_pixel_width': -5254929494347478463,
                                        'source_pixel_height': -8609725890618202410,
                                        'rotation': -5349687110548172029,
                                        'virtual_nw_x_pixel': 107292154,
                                        'virtual_nw_y_pixel': 827098750,
                                        'virtual_width': -1487087323,
                                        'virtual_height': 1086514182,
                                    },
                            {
                                        'source_monitor': 670545,
                                        'source_nw_x_pixel': -1380351049675760346,
                                        'source_nw_y_pixel': -6008538900450184519,
                                        'source_pixel_width': -1084215458167329032,
                                        'source_pixel_height': -2263764922777141177,
                                        'rotation': -3652558697830512418,
                                        'virtual_nw_x_pixel': 1782384628,
                                        'virtual_nw_y_pixel': -1709920397,
                                        'virtual_width': -1145287430,
                                        'virtual_height': 1497959804,
                                    },
                        ],
                },
                {
                    'description': 'ą΅˄Ѧhӥǿǆӄ%àȅŬʝđÿІ\u0380ǛΝʁΒʿÚƅĒƻňνM',
                    'monitors': [
                            {
                                        'identifier': 4898203,
                                        'width': 4412667653084614513,
                                        'height': 1204647961602402243,
                                    },
                            {
                                        'identifier': 8275524,
                                        'width': 5691444892674278438,
                                        'height': 1758898517830959818,
                                    },
                            {
                                        'identifier': -624006,
                                        'width': 8876824595292021310,
                                        'height': 2817001737396129488,
                                    },
                            {
                                        'identifier': 1258094,
                                        'width': 2431666281610459380,
                                        'height': 2872428492532556544,
                                    },
                            {
                                        'identifier': 4243867,
                                        'width': 7032076124206091511,
                                        'height': -5397603223641477649,
                                    },
                            {
                                        'identifier': 254070,
                                        'width': -24111434161389915,
                                        'height': 2472740116052554468,
                                    },
                            {
                                        'identifier': 1461112,
                                        'width': 7707039469082806383,
                                        'height': 7001890751590359749,
                                    },
                            {
                                        'identifier': -166432,
                                        'width': -6574406665301306429,
                                        'height': -5276175922968026284,
                                    },
                            {
                                        'identifier': 1798775,
                                        'width': -5639833753217747828,
                                        'height': 2244035307360355231,
                                    },
                            {
                                        'identifier': 9757264,
                                        'width': 6344573808942107585,
                                        'height': -6324758077758007364,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6659101,
                                        'source_nw_x_pixel': -7328223018976943882,
                                        'source_nw_y_pixel': -6613115809935297866,
                                        'source_pixel_width': -1966159283737423261,
                                        'source_pixel_height': -5688383224379459914,
                                        'rotation': -4131117852186246950,
                                        'virtual_nw_x_pixel': 392016550,
                                        'virtual_nw_y_pixel': 158435403,
                                        'virtual_width': -1028388711,
                                        'virtual_height': 1884877668,
                                    },
                            {
                                        'source_monitor': 6758773,
                                        'source_nw_x_pixel': -4652764312425200023,
                                        'source_nw_y_pixel': -2856502684967009263,
                                        'source_pixel_width': -7095826803250234262,
                                        'source_pixel_height': -3749529373724860403,
                                        'rotation': -71124715633447428,
                                        'virtual_nw_x_pixel': 147363887,
                                        'virtual_nw_y_pixel': 774697489,
                                        'virtual_width': 704675808,
                                        'virtual_height': -959337701,
                                    },
                            {
                                        'source_monitor': 7544255,
                                        'source_nw_x_pixel': -3716540902882444171,
                                        'source_nw_y_pixel': -4098105385029620961,
                                        'source_pixel_width': -4570311405714932088,
                                        'source_pixel_height': -8493930040167915576,
                                        'rotation': -8252106712989593740,
                                        'virtual_nw_x_pixel': -1329724364,
                                        'virtual_nw_y_pixel': -1216568597,
                                        'virtual_width': 864367857,
                                        'virtual_height': 149726589,
                                    },
                            {
                                        'source_monitor': 6317282,
                                        'source_nw_x_pixel': -3191820114297583038,
                                        'source_nw_y_pixel': -8841692275675517164,
                                        'source_pixel_width': -7015055650463282477,
                                        'source_pixel_height': -3357633027452364332,
                                        'rotation': -7802149421691750044,
                                        'virtual_nw_x_pixel': -193161630,
                                        'virtual_nw_y_pixel': 1414064308,
                                        'virtual_width': 1459235653,
                                        'virtual_height': -522071266,
                                    },
                            {
                                        'source_monitor': 3941896,
                                        'source_nw_x_pixel': -8890919680673235335,
                                        'source_nw_y_pixel': -1713577592138461513,
                                        'source_pixel_width': -4980016321824205342,
                                        'source_pixel_height': -5352047916341630992,
                                        'rotation': -7929890717015322111,
                                        'virtual_nw_x_pixel': -159139279,
                                        'virtual_nw_y_pixel': -1772905116,
                                        'virtual_width': -995402544,
                                        'virtual_height': 114636565,
                                    },
                            {
                                        'source_monitor': 2771583,
                                        'source_nw_x_pixel': -6197548731645414121,
                                        'source_nw_y_pixel': -4838440420865710380,
                                        'source_pixel_width': -8863626682667807051,
                                        'source_pixel_height': -7698980183988628972,
                                        'rotation': -6969768610146621493,
                                        'virtual_nw_x_pixel': -291014221,
                                        'virtual_nw_y_pixel': 1109377122,
                                        'virtual_width': 850086895,
                                        'virtual_height': -917903852,
                                    },
                            {
                                        'source_monitor': 9639779,
                                        'source_nw_x_pixel': -7488159539079212617,
                                        'source_nw_y_pixel': -2795960137965270573,
                                        'source_pixel_width': -4248371845209483665,
                                        'source_pixel_height': -7068396742868615518,
                                        'rotation': -8685047077687233651,
                                        'virtual_nw_x_pixel': -748840412,
                                        'virtual_nw_y_pixel': -17684774,
                                        'virtual_width': -311936426,
                                        'virtual_height': 1343657921,
                                    },
                            {
                                        'source_monitor': 9895435,
                                        'source_nw_x_pixel': -6342350506371767813,
                                        'source_nw_y_pixel': -6402728891911554907,
                                        'source_pixel_width': -4778460978875577531,
                                        'source_pixel_height': -3988747582216182900,
                                        'rotation': -3554980885771465426,
                                        'virtual_nw_x_pixel': -1773525615,
                                        'virtual_nw_y_pixel': -1323403064,
                                        'virtual_width': 1341510783,
                                        'virtual_height': 1608973205,
                                    },
                            {
                                        'source_monitor': 6129740,
                                        'source_nw_x_pixel': -7611176990157840465,
                                        'source_nw_y_pixel': -600206225295544282,
                                        'source_pixel_width': -1902221006235547856,
                                        'source_pixel_height': -1225131203059011145,
                                        'rotation': -4000877165664887467,
                                        'virtual_nw_x_pixel': 1287556669,
                                        'virtual_nw_y_pixel': -1728865332,
                                        'virtual_width': 1263018502,
                                        'virtual_height': 770214901,
                                    },
                            {
                                        'source_monitor': -559620,
                                        'source_nw_x_pixel': -5661197036124729282,
                                        'source_nw_y_pixel': -5559624492951993084,
                                        'source_pixel_width': -5779619516721757835,
                                        'source_pixel_height': -3444788439694385712,
                                        'rotation': -5060962822073870327,
                                        'virtual_nw_x_pixel': 1209358175,
                                        'virtual_nw_y_pixel': -131978419,
                                        'virtual_width': -230265133,
                                        'virtual_height': -930664988,
                                    },
                        ],
                },
                {
                    'description': "ЖêˌωŤÞȁɩȉӡϟШʯơ'HɌϐëøӂĄĳıǾӿ³§śĬ",
                    'monitors': [
                            {
                                        'identifier': 5756265,
                                        'width': -8804108673097283873,
                                        'height': 8158143048007313191,
                                    },
                            {
                                        'identifier': -55127,
                                        'width': -4626457685932686438,
                                        'height': -5347380236673203986,
                                    },
                            {
                                        'identifier': 5864904,
                                        'width': -2652266870452351208,
                                        'height': 5145662353499420427,
                                    },
                            {
                                        'identifier': 2411837,
                                        'width': -1746763505386484426,
                                        'height': 451185290628556830,
                                    },
                            {
                                        'identifier': 5615453,
                                        'width': -6522734776160225413,
                                        'height': 7658499155276230744,
                                    },
                            {
                                        'identifier': 8377541,
                                        'width': -8742568334341944406,
                                        'height': 8100119461028612003,
                                    },
                            {
                                        'identifier': 1663794,
                                        'width': -3045524832166263861,
                                        'height': 8823471588850872855,
                                    },
                            {
                                        'identifier': 9235224,
                                        'width': 5539957702364803332,
                                        'height': -4554388335148229600,
                                    },
                            {
                                        'identifier': 8303543,
                                        'width': 8860363316041499881,
                                        'height': -6138393379406971538,
                                    },
                            {
                                        'identifier': 5081579,
                                        'width': -1654829093833249518,
                                        'height': 3803670321663760183,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4084043,
                                        'source_nw_x_pixel': -1538274377286954470,
                                        'source_nw_y_pixel': -1128823971181895922,
                                        'source_pixel_width': -4383867486754170381,
                                        'source_pixel_height': -8281646554789124086,
                                        'rotation': -7186503481134255493,
                                        'virtual_nw_x_pixel': 813265629,
                                        'virtual_nw_y_pixel': -605770890,
                                        'virtual_width': -1582993324,
                                        'virtual_height': 118234434,
                                    },
                            {
                                        'source_monitor': 1108493,
                                        'source_nw_x_pixel': -4123245680684605635,
                                        'source_nw_y_pixel': -7892270581745577527,
                                        'source_pixel_width': -8297468775683511664,
                                        'source_pixel_height': -7306317016925102107,
                                        'rotation': -8430019233791580482,
                                        'virtual_nw_x_pixel': -922228004,
                                        'virtual_nw_y_pixel': -1548335206,
                                        'virtual_width': 493760873,
                                        'virtual_height': -1113317996,
                                    },
                            {
                                        'source_monitor': 4792261,
                                        'source_nw_x_pixel': -3828281562485649248,
                                        'source_nw_y_pixel': -2853701678199001160,
                                        'source_pixel_width': -1925499088620106580,
                                        'source_pixel_height': -927742115979179276,
                                        'rotation': -3831101500005977066,
                                        'virtual_nw_x_pixel': 1883425372,
                                        'virtual_nw_y_pixel': 1326299277,
                                        'virtual_width': -558771229,
                                        'virtual_height': 584861879,
                                    },
                            {
                                        'source_monitor': 6764340,
                                        'source_nw_x_pixel': -7730612490492412829,
                                        'source_nw_y_pixel': -3957950442904626344,
                                        'source_pixel_width': -5302222498573306119,
                                        'source_pixel_height': -9021378049895622677,
                                        'rotation': -40993994291655960,
                                        'virtual_nw_x_pixel': -250452915,
                                        'virtual_nw_y_pixel': 1611280481,
                                        'virtual_width': 1299968816,
                                        'virtual_height': -1406090863,
                                    },
                            {
                                        'source_monitor': 589270,
                                        'source_nw_x_pixel': -5363746358338322843,
                                        'source_nw_y_pixel': -7820327140252657518,
                                        'source_pixel_width': -6064419996984680820,
                                        'source_pixel_height': -5134385429248583648,
                                        'rotation': -8006734234322081344,
                                        'virtual_nw_x_pixel': 1831238746,
                                        'virtual_nw_y_pixel': 365594215,
                                        'virtual_width': -1035784184,
                                        'virtual_height': 1986381826,
                                    },
                            {
                                        'source_monitor': 1760756,
                                        'source_nw_x_pixel': -2251808881793153904,
                                        'source_nw_y_pixel': -1544653319145794791,
                                        'source_pixel_width': -2577310138500276411,
                                        'source_pixel_height': -3106490235466415701,
                                        'rotation': -2328233443125637577,
                                        'virtual_nw_x_pixel': -1305325801,
                                        'virtual_nw_y_pixel': -1745597964,
                                        'virtual_width': 518012284,
                                        'virtual_height': -198881760,
                                    },
                            {
                                        'source_monitor': 9067724,
                                        'source_nw_x_pixel': -3721497687265554939,
                                        'source_nw_y_pixel': -9094525156151842150,
                                        'source_pixel_width': -838324541813857688,
                                        'source_pixel_height': -2492394311356907968,
                                        'rotation': -3383177945836605889,
                                        'virtual_nw_x_pixel': -1628648135,
                                        'virtual_nw_y_pixel': 262634844,
                                        'virtual_width': 219848682,
                                        'virtual_height': 101203607,
                                    },
                            {
                                        'source_monitor': 2912019,
                                        'source_nw_x_pixel': -778518986332476154,
                                        'source_nw_y_pixel': -4802681498235809588,
                                        'source_pixel_width': -8751165686901480862,
                                        'source_pixel_height': -1124769137839287081,
                                        'rotation': -2277954107423705486,
                                        'virtual_nw_x_pixel': -1635629014,
                                        'virtual_nw_y_pixel': 88786432,
                                        'virtual_width': -1536494653,
                                        'virtual_height': -491577219,
                                    },
                            {
                                        'source_monitor': 8442729,
                                        'source_nw_x_pixel': -2169849126731274434,
                                        'source_nw_y_pixel': -3336850835849821810,
                                        'source_pixel_width': -3276873264436579271,
                                        'source_pixel_height': -3796160049655518689,
                                        'rotation': -5195132013193998116,
                                        'virtual_nw_x_pixel': 1012290827,
                                        'virtual_nw_y_pixel': 1313136315,
                                        'virtual_width': 345505633,
                                        'virtual_height': -658609037,
                                    },
                            {
                                        'source_monitor': -505276,
                                        'source_nw_x_pixel': -6340759695448714690,
                                        'source_nw_y_pixel': -1122875107064315187,
                                        'source_pixel_width': -5122566994132318511,
                                        'source_pixel_height': -4500454967188585237,
                                        'rotation': -3872796378483543826,
                                        'virtual_nw_x_pixel': -1980559647,
                                        'virtual_nw_y_pixel': 1721307608,
                                        'virtual_width': -210238550,
                                        'virtual_height': -1655059866,
                                    },
                        ],
                },
                {
                    'description': 'ҐӜšǎ°ǬλʿΠѵǭɨǐʲʾέśʆìЇҹҕэНиz\x9cŦχІ',
                    'monitors': [
                            {
                                        'identifier': 1367747,
                                        'width': 6139855834495292164,
                                        'height': 8939715298883683132,
                                    },
                            {
                                        'identifier': 5697762,
                                        'width': -9197238363294639377,
                                        'height': 8069540164933053537,
                                    },
                            {
                                        'identifier': 4857194,
                                        'width': -7417599423016450431,
                                        'height': -1704225300430179465,
                                    },
                            {
                                        'identifier': 1931779,
                                        'width': -103910977360926140,
                                        'height': 3112568099769274478,
                                    },
                            {
                                        'identifier': -428156,
                                        'width': -1666528956391730913,
                                        'height': -6090825198337746199,
                                    },
                            {
                                        'identifier': 5186975,
                                        'width': -145240804258830403,
                                        'height': -1907217816029680374,
                                    },
                            {
                                        'identifier': 6816677,
                                        'width': 5870589502740947442,
                                        'height': -2958681917554423938,
                                    },
                            {
                                        'identifier': 8951487,
                                        'width': 9051766946731647706,
                                        'height': -6625705043904822599,
                                    },
                            {
                                        'identifier': 8182259,
                                        'width': -4600180886313392601,
                                        'height': -5290599263705404991,
                                    },
                            {
                                        'identifier': 5788808,
                                        'width': -7114231040741912825,
                                        'height': -3490046808383370942,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9794638,
                                        'source_nw_x_pixel': -8293639174948455112,
                                        'source_nw_y_pixel': -2619580944833345117,
                                        'source_pixel_width': -8313802861111864783,
                                        'source_pixel_height': -755359804415847401,
                                        'rotation': -2061496013072226656,
                                        'virtual_nw_x_pixel': -53368422,
                                        'virtual_nw_y_pixel': 1940206774,
                                        'virtual_width': -96183031,
                                        'virtual_height': -564136893,
                                    },
                            {
                                        'source_monitor': 8740698,
                                        'source_nw_x_pixel': -6817491267574163397,
                                        'source_nw_y_pixel': -5543412441724939569,
                                        'source_pixel_width': -428000648389012996,
                                        'source_pixel_height': -254263131332233733,
                                        'rotation': -6794401377996929946,
                                        'virtual_nw_x_pixel': 161883637,
                                        'virtual_nw_y_pixel': -1350779077,
                                        'virtual_width': 478025075,
                                        'virtual_height': 1833659431,
                                    },
                            {
                                        'source_monitor': 3015390,
                                        'source_nw_x_pixel': -9101987523821101191,
                                        'source_nw_y_pixel': -986939424379871679,
                                        'source_pixel_width': -639526897686551553,
                                        'source_pixel_height': -1047740785022808343,
                                        'rotation': -3382396459531744272,
                                        'virtual_nw_x_pixel': 997879537,
                                        'virtual_nw_y_pixel': 1388106455,
                                        'virtual_width': -461292772,
                                        'virtual_height': -98168126,
                                    },
                            {
                                        'source_monitor': 2494045,
                                        'source_nw_x_pixel': -3280699140593010588,
                                        'source_nw_y_pixel': -3312962377016122266,
                                        'source_pixel_width': -8704271711505473039,
                                        'source_pixel_height': -3951390314970343833,
                                        'rotation': -2706026632066376829,
                                        'virtual_nw_x_pixel': -1920660153,
                                        'virtual_nw_y_pixel': -1187723402,
                                        'virtual_width': 1934384834,
                                        'virtual_height': -1880955093,
                                    },
                            {
                                        'source_monitor': 6547791,
                                        'source_nw_x_pixel': -4140899068076501306,
                                        'source_nw_y_pixel': -5706745299632829688,
                                        'source_pixel_width': -1817309866807180198,
                                        'source_pixel_height': -4930966113180648612,
                                        'rotation': -5313260711217508281,
                                        'virtual_nw_x_pixel': 392503124,
                                        'virtual_nw_y_pixel': 971680878,
                                        'virtual_width': -844853690,
                                        'virtual_height': -1545685572,
                                    },
                            {
                                        'source_monitor': 4767550,
                                        'source_nw_x_pixel': -5180351325006382230,
                                        'source_nw_y_pixel': -8452568652912629147,
                                        'source_pixel_width': -3902872937222908489,
                                        'source_pixel_height': -9196594378602891867,
                                        'rotation': -2600759579999638296,
                                        'virtual_nw_x_pixel': -1714950559,
                                        'virtual_nw_y_pixel': -71271870,
                                        'virtual_width': 380956050,
                                        'virtual_height': -76287938,
                                    },
                            {
                                        'source_monitor': 1908127,
                                        'source_nw_x_pixel': -480186386849828379,
                                        'source_nw_y_pixel': -7854179267631048859,
                                        'source_pixel_width': -436820850207157555,
                                        'source_pixel_height': -7684798748734094275,
                                        'rotation': -1963664676658656175,
                                        'virtual_nw_x_pixel': 286471213,
                                        'virtual_nw_y_pixel': -1346563143,
                                        'virtual_width': 1319345245,
                                        'virtual_height': 6364713,
                                    },
                            {
                                        'source_monitor': 8084315,
                                        'source_nw_x_pixel': -2034105679052016631,
                                        'source_nw_y_pixel': -6768315504799965486,
                                        'source_pixel_width': -2353511931302163589,
                                        'source_pixel_height': -6630412799439417827,
                                        'rotation': -4851900831688819197,
                                        'virtual_nw_x_pixel': 638782760,
                                        'virtual_nw_y_pixel': 767536781,
                                        'virtual_width': -1276353592,
                                        'virtual_height': 701214815,
                                    },
                            {
                                        'source_monitor': -223031,
                                        'source_nw_x_pixel': -9094364333113039374,
                                        'source_nw_y_pixel': -8494021842390347698,
                                        'source_pixel_width': -6292782627300491448,
                                        'source_pixel_height': -943115192575856072,
                                        'rotation': -6433395829788177129,
                                        'virtual_nw_x_pixel': -741269586,
                                        'virtual_nw_y_pixel': 540262960,
                                        'virtual_width': -1360543040,
                                        'virtual_height': 495460084,
                                    },
                            {
                                        'source_monitor': 3467355,
                                        'source_nw_x_pixel': -4359447878610586921,
                                        'source_nw_y_pixel': -7685846467834269112,
                                        'source_pixel_width': -1887344198172858518,
                                        'source_pixel_height': -6913127534277806138,
                                        'rotation': -6735222410725284802,
                                        'virtual_nw_x_pixel': 768619989,
                                        'virtual_nw_y_pixel': 621984893,
                                        'virtual_width': 217863677,
                                        'virtual_height': -1291520101,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 8894061,

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
            'request_id': 1556765,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 7925213,

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
            '$': 'bìŽϡӚɽЛŢƐûĄѩɴԫ\\¼όʺϨɽЯEȱʱˊҸҰʟƗΗ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7999673231924026247,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 210440.4766722105,
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
            '$': '20210302:165933.833673:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ԈʣǉʝŀӣʙƃƿčǙƕǹ)ƃìѦĞĘʟƘ\x80˷Σӿϝ2αǉˉ',
                '±ÏшǲӜȣΧˀ\x97ѳ˞əƈʗПǳƯȊ˅ƲʩɓҮ¤ʍsϰԀŘ˫',
                'љǣˊҨɻĳŇ;лǃԑNҴŊȢԮцҤϐǇ§ʩʔżƄƨӄrєο',
                'ӫƩźԋˣaŌαɲíHѰU\x7f¡ʂ\x81^²Lęо\x9eѴζˬơ\x9cӯӟ',
                'ϫÀϙ˽ϰδaȌɡϥŰ³ɌɠŦʖХьЯϻΎѾPĜÒƳßͰзɴ',
                'ɌʥЦё^ťКƙѨçŏIĈʰӺά\x9eĩEϒȤǚѫ҈Ӈ΄ʳɚԣƄ',
                'æâ9˽ӕ΅ÓƘѠAȏħęұЛ¢\x95ԖNòǈҶҽʑϤ}ƠúϾˇ',
                'ÎĔėѡϙɴҔÜӀ[ԡЋԋυӸʁѵƓԑԀ%ɸ\x9b˖ˎŎŃƄ¼ӆ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                3917903443322296823,
                2428099262999030235,
                -2736713130017217744,
                -695729671056288110,
                8276924398773995963,
                -9209253970423404851,
                4827641629849953063,
                -5286661114697734309,
                -2110566309876491650,
                -5629968609327260975,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                895532.6660500659,
                635278.7722367736,
                980745.6441835724,
                394315.49823723995,
                57790.97986914776,
                246103.47512073774,
                846012.3874566746,
                862043.2509156342,
                -33545.75739558565,
                721592.3856429178,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
                False,
                False,
                False,
                False,
                True,
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
                '20210302:165934.891739:+0000',
                '20210302:165934.907736:+0000',
                '20210302:165934.923433:+0000',
                '20210302:165934.939383:+0000',
                '20210302:165934.955792:+0000',
                '20210302:165934.972493:+0000',
                '20210302:165934.987593:+0000',
                '20210302:165935.002025:+0000',
                '20210302:165935.017352:+0000',
                '20210302:165935.032873:+0000',
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
            'name': 'МгѴӴѓӨ˶ȕŠƘňҧ',
            'value': {
                '^': 'string',
                '$': 'ʜïĠÄǷ©ÓϑȀɢɽǿȱƳ˰²Ӝɲ¬ίМÛ΅ϛˇϺԠɓӜ@',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ż',

            'value': {
                '^': 'string',
                '$': '',
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
            'catalog': 'ġŞɎ˞χΣȔ˭ƙ6ͶŎȠͷĤĎȝϘŧŚԥïЯȦüԙӯ}ƧѺ',
            'message': 'ʬԎǑΡϋώіΣϫΧÅśGӀΈȄʓѽɊƸЫєѹȾŖäҞ͵ʄǠ',
            'arguments': [
                {
                    'name': 'Ɛ®',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        604356.7532618961,
                                        786194.7833947564,
                                        186065.1273531635,
                                        51728.07823893431,
                                        803151.4021065944,
                                        425497.6761914402,
                                        38446.65355326122,
                                        -47783.182251026534,
                                        241638.71981476923,
                                        814638.5156945414,
                                    ],
                        },
                },
                {
                    'name': 'џҚΥ˼ҖȜ¸ѻʴΧҕǏϡђКTΌįĈќіҶǧ˄½ˮȉˠɆà',
                    'value': {
                            '^': 'int',
                            '$': -4331881378263654687,
                        },
                },
                {
                    'name': 'ßϷ$Џ˝ɥԠ\x8fȩԩμʻǞçɯFÒȺȠΎц1ЊϏƄ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210302:165932.081731:+0000',
                        },
                },
                {
                    'name': 'ΧŞŎɱˉˑƗͺĄҹȯОˊŇӊÊɹʖǉ\x86ҐˁѡĹáОҡÜȓϐ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210302:165932.155891:+0000',
                                        '20210302:165932.173273:+0000',
                                        '20210302:165932.191653:+0000',
                                        '20210302:165932.213583:+0000',
                                        '20210302:165932.231078:+0000',
                                        '20210302:165932.248054:+0000',
                                        '20210302:165932.265051:+0000',
                                        '20210302:165932.282873:+0000',
                                        '20210302:165932.301293:+0000',
                                        '20210302:165932.318657:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ӌќѸвǋDчΙƮĜ\x9cҋǀԅĔǁcǕ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210302:165932.400255:+0000',
                        },
                },
                {
                    'name': 'ćǥ˾пԞʂѸΙ˼γι?ΰΌдŦʭӀϜʻą¼эϵĊьΦѠǯo',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': '˹ɽгŞÛΏʟȖùѲʮŞjŷjѡиϛȘмƿˁ\x9fÃWλѴšǒȗ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ʃәɣũʵøγɕ҂˓ȏȊėĉˎŷѩКz.͵ɰċϓĳŜƖ҃ƺä',
                                        '%ɤÖӹԙ´ԝHџɂӵɣԩƧ\x80іĜ\x9e˻ņ\u0379ѥҾǙОҀ2\x92˩\x8b',
                                        'фǖƺѓоʓ/|ŵƟMѵǗǒžÔ¼±ħ¦wΈɷȴĀĉˇƝόx',
                                        'ĳýΞʦ\x91ĪΚŷҌƬҮʶĻºƆԝơ\u0383ϾȬӥȈŕлҀƓԪz·ƨ',
                                        'ɏΓԍƧҸҤ¡ӈʠѯƈпԆɈ²˫ʵƄʇ««ãd\u038b˜˗Э˛Şε',
                                        'Ŝ˂ͽˁȇɾκ&ɣє ʠӼVјѿϒ¸ĽgǏХҞƏ@ˊдʽӢʠ',
                                        'Õ3ÞͽӨǖ\x9bɶΖɃʸɁʋΈӵµčʴʺ˫ˑҝɥMȐϴчӊţȗ',
                                        'ɱŗʕŷķΨ§˥ɆӦˇφѽŭqƘѢƃƢӿ˘¤v҆ӿќ҄ҙ˄˶',
                                        'ЊӭƻӾЭʷ˺ЇǛЪÖδԮȥωFʴØ\x86ɌѴÙʑҩʥKŠ˵ˏΠ',
                                        'ҫɓ\x9bļɃǡŢíɹİǐ4ӀʇяЉ\x85üŵ\u0382śĀзơŝʋǶƔê.',
                                    ],
                        },
                },
                {
                    'name': 'ōԗӡőϞˢƒʅɍʟȆƁƇͲƃΎʄɽ«ǲӸğǧҌ˱ҦйРȓ¢',
                    'value': {
                            '^': 'datetime',
                            '$': '20210302:165932.881991:+0000',
                        },
                },
                {
                    'name': 'ýίБÔŢΤӅъǌʓVǞԄΉҭӴҟǼ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        8236539718408355515,
                                        -344453997690586523,
                                        -8706039567838821201,
                                        3163806054469387779,
                                        -7377649040498353201,
                                        -1803666406315997399,
                                        6121091577849249592,
                                        -2664057943218428599,
                                        7259138282236450382,
                                        5988593405889062507,
                                    ],
                        },
                },
                {
                    'name': 'ӫЙϟ\xa0\u0381ʢЖśѸʭłªõϰΫŉϳű<ўӰ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -5428887343065728551,
                                        -3360481840808769598,
                                        3713228434935877330,
                                        3475096934681764958,
                                        -4729944011871695642,
                                        -240770127285198190,
                                        -687952869741141845,
                                        -5054306987523579628,
                                        -1785503223159535388,
                                        7187355671781974986,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ϭ·',

            'message': '¨',

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
            'identifier': 'Ɓ˹ʽюɾԬгţþԔˡHһδЩϷǟ\x93ȣGcǈ˶Ж\xa0пщȥвƪ',
            'categories': [
                'invalid-user-action',
                'network',
                'network',
                'internal',
                'file',
                'file',
                'file',
            ],
            'source': 'ɅʜӆЁгΗҴȹПΈȕБ\x85ϬΖѮΆӭʁòÓÒɃʮ3cԏɁȈ\x87',
            'messages': [
                {
                    'catalog': 'Á\x9fˮɩĳȣʼϐǺºʱƍɴӈ¬ɲšǘɂϩζͼ϶ϜҼZØʏĐ³',
                    'message': 'Ҹ҇ӏХ˱Ѫ^\x96řԘţԚǦѪq\x9bπƬ¸ɽ˻ȅ\x92³ԓҧӕљЩΙ',
                    'arguments': [
                            {
                                        'name': '¯ҽɯϧü¹řšȜ¬ƸˏοɍЍŎƭˠ˘ŀǤːɈĊɁϢљÙ˷',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165911.725454:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȊБ˲ŎçÔӅΩ˚ǯХӷBҙčфɬƅȖĨʁ˲ɽǃɹģȤƒ҈П',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5339889339272028347,
                                                    },
                                    },
                            {
                                        'name': 'Ü\x8eðϏʉΊf«ϖӋчHʞѻȸЮѳȶ˹Ƕ«ǛǰШƁϽνϾǷύ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8245995375278327514,
                                                    },
                                    },
                            {
                                        'name': 'ƋЊέ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 477279.9332523007,
                                                    },
                                    },
                            {
                                        'name': 'Ѽй?ѨӾń)Ǭԟ\x8aH_ĝȿÖ˷ҊłϯƣϛхɑϾɣδĔ±Ѯʂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165912.095539:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЍӼʯȖ´ЪʜѭæΟљÍԓƥϽǒ¦ʭˈʵŒͷЀʐûœȟˍѪƾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3270534096056026154,
                                                    },
                                    },
                            {
                                        'name': 'ԋƫ˾\x93ԍБϟΧǭTЌȲѧåɁ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            751804.9982237619,
                                                                            644839.7154839751,
                                                                            315612.39144927566,
                                                                            416127.03866235266,
                                                                            112841.98619275543,
                                                                            351321.20340473746,
                                                                            178406.6103733097,
                                                                            111584.10753636391,
                                                                            -50567.03713632296,
                                                                            401556.26652077667,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˃\x95Ƞŵӛȿŧǵ¹ƊʙɾŎ˰Eɑlόçґе҂ǆӤʔϔҶĕȨδ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            706380.4711075702,
                                                                            551584.0449859392,
                                                                            590850.3228009995,
                                                                            686127.6746715393,
                                                                            164337.3854522134,
                                                                            654272.5589732551,
                                                                            798957.388180598,
                                                                            15059.793203344394,
                                                                            485654.2100962119,
                                                                            20250.839228768193,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'pĄūp°ǩÚƝє',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -27108.13291411735,
                                                    },
                                    },
                            {
                                        'name': 'ωԗǼϔѢȚĵЫǘǗȒ<Eϟ\\πʎͰΒˀӮ\x96ȯυȎÒԃџ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 623592.357387068,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӀƭVÐӛӋ ǯɱПԛʇԪɥӳʪфƲū\xadɀȋȩ҄ȧČWǿѪѽ',
                    'message': 'BiϨɉԂԣʨЅůΨČǍЗ±Gˈ SŌȋʿʴͷ\x9c©҇Ưҕġʢ',
                    'arguments': [
                            {
                                        'name': 'ʠϱŔĸԢ˶ЭΪʛӌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165913.177520:+0000',
                                                                            '20210302:165913.202547:+0000',
                                                                            '20210302:165913.226169:+0000',
                                                                            '20210302:165913.250673:+0000',
                                                                            '20210302:165913.274088:+0000',
                                                                            '20210302:165913.300981:+0000',
                                                                            '20210302:165913.324151:+0000',
                                                                            '20210302:165913.349148:+0000',
                                                                            '20210302:165913.371958:+0000',
                                                                            '20210302:165913.397868:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӗЇЕʉƍӫΒɷɝ˯ɉÏįâƞʩîϘӓ\x80ЌҨȼ\u0381҅ʕѕƝїĬ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˴ҺΉŘǭȁԧϘρ_κӉƥɸϿȆԁXЙϢӕƚŘŶС',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            849265.6948302533,
                                                                            434772.5670190498,
                                                                            354835.2728030229,
                                                                            482055.0859290059,
                                                                            751821.396970351,
                                                                            183490.496512843,
                                                                            898023.714638194,
                                                                            -85387.11257280012,
                                                                            -18349.187070772736,
                                                                            34023.26507361463,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҾҰʊʮǯюþΎ΅{ȃɓĞ\x9e\u0379ǠɞӅЯŵԄˍˏȀ˗ϱсΆ¼\x98',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'Ȕδϳþԙ3ɂ¥ϞÑӄ\x9d¬КГѢȮШҀʲĀƁԡӛӜΏϔʩ\x9aʳ',
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
                                        'name': '\x95Ȟɺ\x94ȣÉĬųjǤĞϒʧz£\u0380õиǻ1ĠҬΟȳʠѰξ\x95ūԆ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЂíȊвGǸǓ|ĳ˴ςӴ\x81ӟӨ{ɍxΆҢӭˣѱЭNќӶ¬ӛȀ',
                                                                            'ßɒɓšͼӖѣѧ˅ńǼШèɶƳҍýˡČԋQȼȻIъqǓňcύ',
                                                                            '˸dӮѾԩ˖ŝȻȘ\u0381ʯūԪ\x80ˮøľҲʦ˺ԇʎƿQɈˆėҩΔE',
                                                                            'ϽʃʌӾϓӰ+Ξ´ύŋ\x93Ҽ\x93Ӿ,ʶȎăѐӍKʜĘӡIƺǦԨϒ',
                                                                            '@ΒΛɉμʖeԜȂЄ³ˬä\xadȐǩѻҦӮWԋę˂ԍ҆ҊŞθŕȈ',
                                                                            "Ͻ'ƕɝшǈҠ\u0381UԢҫBƻvɐĄiƋɚǙˌϪƿҶ\x8dGʷǇȠŧ",
                                                                            'ͻщǇѡǿρȕůōĵʶԚƕÜʡνβѓ\u038dƷҫˑ¿Ʃ˃Οϑҹрù',
                                                                            'ĲʹȑʃəüȴȋίΏƖρ\xadԪļƈ~çǵKŜĞЯѝ[Ԃk`ΤƐ',
                                                                            'УąмǩʵӚʚϖμϠҖ\x9fƸ\x92ό-ɳόĄЀƓȒȲrȔÅϱӏÀά',
                                                                            'ԢɧҩĆЙ¤ŒoǕеЉbӤůĄǦĸPӜȴeЖȷʔĂӧӤʨɮĵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΙЫĳ\x8dĘпǌԥǶ\x91ȌƘ˭ÒӭӥИϓΰѺΛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165914.983221:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǀ\u03a2ŰǄϱњ¶ŁӶɆ\x9eǳжόнӕѐғҪŗƬ}Ⱦч5Θ˞\x8bԣʣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 779923.460692313,
                                                    },
                                    },
                            {
                                        'name': 'ƼˉíǪаэқґðǞ΅Ŷʈԋƻ]ùϢhәӐȈȜˉ˞ԝ°ȑ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8958169825681267183,
                                                    },
                                    },
                            {
                                        'name': 'ԦÞ\x9bЮԧƖʧǪŜǝǤ˥\u038bĚѝӔʝŏUˈҳĊҊȥ\u038bjв\x94ǝɳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                        ],
                },
                {
                    'catalog': 'ȞɧӍȯȅĺ§ˮ©ԒһÝ˻ЬŃԋҟĚŞВȸӋĦƱƩɡҤȊͶˑ',
                    'message': 'ӨŏԪ(Źаž˄˦WȞԕʣ~Ļ1ƄҥèřϬ9ΥϹƐҗʕƇͶϸ',
                    'arguments': [
                            {
                                        'name': 'ӲӞѕěÞƭҜŉˠȆӄȋɧzβ\x9cüŶǘ\u03a2ɠСŀįӝþ˽ēɥƪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'âɫцĤ˨ԭƓѽÊδˬȜʁ\u0378ǭΏǀʴԙĜķ#ʍȥƐθӔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165915.763691:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŁԔ%џλ\x9eӈǠΧǁɋǹʰԝˁӔѝѾ¦JLѬ˲ȈƢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 376325.87191909674,
                                                    },
                                    },
                            {
                                        'name': 'ϪAԧϵÒү*˭ȮԙGǒΤԙvšǌў°ôLŏ÷ӕϳȝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˛эɌɽœјĴĎ\x8dϹȱXý§ʎĤ˴ɬɲǮԠĈÆƫʚЎÐǆ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӢΨҮťҘŔȨӱѴσҌ˧ƢҖų',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165916.385203:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǝ»ÐϹӿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2001903093087854558,
                                                                            -3726618026083471634,
                                                                            -8552522352655173169,
                                                                            138441798123035319,
                                                                            1032059624160745838,
                                                                            -1905536414033261292,
                                                                            -1271761315420103797,
                                                                            6534642107904511256,
                                                                            -4343325156871290153,
                                                                            -2330852991122455238,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΥҘѯҳƑņÒӼȜǗєӕ˅ȵ\u0380ĵό<\x8eӌѬǌţюӸ˔',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 352056.94725428877,
                                                    },
                                    },
                            {
                                        'name': 'ÊǍВ?\x95ƾԐȮҴȠ+ϰǦȹўƷϷɈʹŶʼҤŭĪ%ɠԕ¤Ԧş',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165916.870004:+0000',
                                                                            '20210302:165916.892117:+0000',
                                                                            '20210302:165916.914630:+0000',
                                                                            '20210302:165916.936275:+0000',
                                                                            '20210302:165916.961121:+0000',
                                                                            '20210302:165916.983049:+0000',
                                                                            '20210302:165917.005993:+0000',
                                                                            '20210302:165917.028880:+0000',
                                                                            '20210302:165917.051842:+0000',
                                                                            '20210302:165917.077042:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɸîΞҎГȂɊӅĝӊØśύɝΦ˱ˎ˶ҸҭŸʍǡ˅Ł¼όǊѻХ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ѻ\x9fȔѨɔԟ2з§ϘϳƔȫИҹӀЙ˕˲ӬѺϥďƖ˷ў·ВԂԟ',
                                                                            'ι\\˛δ/åɳйʦˉȊ©һǮϻćЕѩʢĒʉИȍĲɦ|ŖӧΞ\xad',
                                                                            'ĕӥşϿƼȳǝśԋČ\u038bɐŒςɪʦåǒN§ʇЉĎԝɳģʏωш·',
                                                                            '^Ƀȉ:ɯÛоˢΟÓʤɼÉӯȌЙǷтȄӦтƩΧϔӛàĲɢӯH',
                                                                            'ϲČǓȑ\x8cČǪʊҁҤηζ%\x94ƙҁŝȗýǸЌʂȤҨҹʽӌɏѡҎ',
                                                                            'ȅīѯҪӠťʣŤѽΠËǛͻ҂ԕԟɑÌǓǔʅ\x97ԥұİɹī\x93ĆѮ',
                                                                            'ӎȷ;aьť,ŭŎǑŐFɑ\u0378ĲÏ˄șҪҞӿӮӪ5Ɣѐƿ϶гǽ',
                                                                            'kӬ÷\u038bɌCѫÃͺФĦůϾԃȇΤƘ6ћϻΥƊĨŶĿ˛×ǐċѐ',
                                                                            'ǙкŽљȑɻǘđҾӅ˼ŲXӍǐʩȏǳĘMҙΉBͼҍªƴĪȖӥ',
                                                                            'ΩΞҍ\x8a²βźLǍϓÌҡǣƁӈĻžʶʾQ·\x8aƅёĥί¢Ԙ1ʉ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˹ɧ˖ēȾ˼ԋƃuĈџÏԐ\x88ԦʤҚĞӨ[ʭͱѴ\x9cȷÒтˑ˻Ӥ',
                    'message': 'ɩ\x94ȁȤÅĹːбF\x81JĨ\x9cʜƫdʔăфŎɺǊǢȌǬ7ɷϙυɫ',
                    'arguments': [
                            {
                                        'name': 'ʰǺūϤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165917.643740:+0000',
                                                                            '20210302:165917.667306:+0000',
                                                                            '20210302:165917.686903:+0000',
                                                                            '20210302:165917.706087:+0000',
                                                                            '20210302:165917.724697:+0000',
                                                                            '20210302:165917.747011:+0000',
                                                                            '20210302:165917.767400:+0000',
                                                                            '20210302:165917.788871:+0000',
                                                                            '20210302:165917.812690:+0000',
                                                                            '20210302:165917.834899:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԆŘˍҾҏÅӠҺ`3',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            701224.7435650608,
                                                                            384692.2971503278,
                                                                            542827.3834242285,
                                                                            849749.3354114284,
                                                                            960742.6315719956,
                                                                            273322.9676402315,
                                                                            388373.3310350782,
                                                                            204529.57433546695,
                                                                            698711.7784260252,
                                                                            166910.8478107112,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'FӜκȵǟ¢ҁ\x9eƮˊŖƳ2Ɨ=ӿǃƸvӍœϝɃɡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165918.261185:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѤӤƜǁϧм3)PˉƬγЎê0ϣǘ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165918.351220:+0000',
                                                                            '20210302:165918.372561:+0000',
                                                                            '20210302:165918.394073:+0000',
                                                                            '20210302:165918.424237:+0000',
                                                                            '20210302:165918.453147:+0000',
                                                                            '20210302:165918.473628:+0000',
                                                                            '20210302:165918.497959:+0000',
                                                                            '20210302:165918.519069:+0000',
                                                                            '20210302:165918.542823:+0000',
                                                                            '20210302:165918.568068:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˥пԟ¬ǺȔoЗχ˺ʴŐҢēУưżƊɌ˘ԤɱYȗΰѕӠ¨¤',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'țɜ9є¿[˯ǻ˫ɧ?У˭ѼĤʗŦ®ϊɢ°ț\x84ĒŬϗ˴\x9bѮҩ',
                                                    },
                                    },
                            {
                                        'name': 'ʖQ˓ҝƐSϔɡҗѱÔҏɗŷūʓЊĤ}ĊǍŔԪϚϪ\x89\x8bųȢю',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165918.814433:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȴˏƫȫÉvǳ҆g~ЪĀWԮýԧӾ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɂƒŧ\u038d˗ǁӉǹѲΖ9ƚ˹ɩ˖ȞōĨǆӅу͵ˍЋƮөдØνȑ',
                                                                            'ǴǢΣˑA\x90ϵƝԃńԬί<\x91~Źɉķ˧΅ɺŜƒġěΕīԄ|т',
                                                                            '\x8cÒԚςȇŧRƦРÒp˫ԀτΛ˪ӿҊƎŪǖ˽ӹɰ(ōɩԫѵ˾',
                                                                            'ЂǳwȀŎwFŬӬĴȶȑñ҇ȍÇιɻȢȝ\x7fћıԂρƹî1Сǈ',
                                                                            'ǈͶϞЄҁƙǖ\x85¡PҰɷĩ҃ŷƅӏδ\x93ϦɬLYĖñͶɽǢӈĿ',
                                                                            'њĭ1сԒƁӠºʙ\x87ʽι҄ůӄвǑâËԃ³VӴçЮӝ\x8fʹФ˖',
                                                                            'ƟԃȉѻКӑæƢȄѷӠƝԖԐԈʡËΊҴʲϐȨˡʁʢȮΪ=θӓ',
                                                                            'P\\ψƘ¥Ҿç˛ğԐӋӡɈȦˮЀҌ¤>өӽѓϖϐѽԟķƞ˅ϓ',
                                                                            "ŕыъȮЭǢǍӁˇҹ'ŝхŮŚŤ·\x85Ԑèÿĵũ'ĜѣĒƎҌǁ",
                                                                            'ƋϗӗΓŧЫŶͽΎÚžͿҁӱӢ\u03a2чѯǻǱǕΈǜϒяϺȗˎӍΫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĵӗ)ϏʗĉϊȋʁԅĩʷǺǙЌԑȱҼђәʇʉԐģʹŬѕÞπ\x81',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165919.267204:+0000',
                                                    },
                                    },
                            {
                                        'name': 'һϼȵгĪ¸¢',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȇ\x98ǠϏϵ÷H˼ӻí\x9cˡӧäԆ\x98ɭФΔ)ӾßҳǪÇtɦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165919.451422:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƿƹЮƌϕjҬƂӟҝƽĬƘcӑŵưÃЮҡʣŚϞȀԪѴǓѴFǾ',
                    'message': 'ϤϩȶȶͱРZ͵Ӊэ\x81ˈļΞɂϝϊҨϞƌČͰǸĿKȲ5Јÿ˧',
                    'arguments': [
                            {
                                        'name': 'ҡʮϩԤˢĠͺΧɮԂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҨȀЉΔѤ<ćĶѿʘ7ƚ˰7ϦȦ=Фӧ·пǒǟҞϛ÷ϗ҂Ģʠ',
                                                                            'ЉǂҏȩӆÄ¥˕ȠħǳӬϭƃԨЋǗ͵ĴЪЮı#ȍńʖЀƑJǾ',
                                                                            'ćүƫȓʃҤϮ!ƽƱӚɃԮ҄ûҁӽъèʀγkΣǃʷϟưɣĊv',
                                                                            'νİҀҏӗɛ#Ҕņ ʍҘҒħҙҷɲȚӔТмʀȝѲĸπ\u0382ïńò',
                                                                            'åΪ:ǎ¨\x96`Y˂éӣͲƿɻӼҝł&˳ҠҴʥ\xadѧˆ:ƳΡKƁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѻҳ¹MҞ΅ÇƒҷάϢ҉ϸȏɈӨ˼ɗŏƄˌǿwÜϵ˧ΈŽϡЩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƜŁъԤ˺ĽǱφøɍʮ\x8bœ½ʹѻѡ³ǋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1361663962879003931,
                                                                            1798450538729301245,
                                                                            -50073475286855874,
                                                                            3112659209128560031,
                                                                            2502625706936810767,
                                                                            -7966180179488062493,
                                                                            5893775776098347909,
                                                                            -7924954689214372541,
                                                                            5129327690676277708,
                                                                            7059995778990036365,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƳȗʟΥАͶϼÚ®Κ͵èJѮИѻԩӲ$4ӕʍ҉©ӟ×ʮǮӷɖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165920.265295:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ħeӛ´ȫΕԉâŌ\x91ɀϠΧӎƮʜ˽ЙҪӄǯȋƍ¥Ȕҙzȿʗҟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -62150.67555883752,
                                                    },
                                    },
                            {
                                        'name': 'øӽҥŭУʕλľΖťƎЬº\u0379ϤʿѣʧÛŝȲΡÕƌӳҜ˾ϛɡè',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\u038bұËɥƝԍȂ˥ĄƍǗ˶(ʉįŚӅ×ɐϣҳԒ=щԚˀεӿɽ¡',
                                                    },
                                    },
                            {
                                        'name': 'ϻ˞ǻƬøƾ\x99ʱĀѻʦΓĂӉɝ÷û÷ҏŬg\x80ѫÅdɜc',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5961060265302825376,
                                                    },
                                    },
                            {
                                        'name': 'ˆȒѪɦϒ\x99ӲεҹȶѴȃ',
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
                            {
                                        'name': 'ʺf\x88ΥшŉʮǏÁЦϵƹоГκƊ|ĞơȣɺͶ˔Ư',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 248382.24093525537,
                                                    },
                                    },
                            {
                                        'name': 'ƝǍƷ\x93ǰń.',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѻƈǝҥάåҾˋÚйӴʘҽ´͵҈ˣӳȅϏσФэËҲÍʚɲý\u0378',
                    'message': 'ƟÓџЛʴҌŶġȘƎ]ԈĘ±ϡӃʖϒ\x9fˠˊʠǍЊɒŭL\xadŠż',
                    'arguments': [
                            {
                                        'name': 'ͻŎҟʨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -45868.035764179185,
                                                    },
                                    },
                            {
                                        'name': 'ʷϺʺΝѾѯϥɒÆʿŉԕɮĎżr¢\x84\u0378ţÊǸʟƏύЮӡê',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˱ϐʅԒɎ°ΠϼƃrԖҬϘӡŖɦāөĂêȭʶƥѥѦʋʶѺȠƸ',
                                                    },
                                    },
                            {
                                        'name': '¶йм˄ȯԁĝСʓӲыΙw\x9aǽјΉ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': '\u0381ϒҠȹŠк¿ɑƢћžΰƈfUӌ˔БϧӺԨħǨѲϣęūɩľĨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8009541135488599452,
                                                    },
                                    },
                            {
                                        'name': 'VǴˡԉŅ˺ӣëĸĿ\x95Łĭǝ\u0382÷ӁиÞΝӇӆӣӫԚğԫҾȪR',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7645082127513337273,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '_ʖɇ¹ѷŪ\x92ɨ;ԓЖº¡ёӀИ',
                    'message': 'ʟȰТeȶѕİɥŊӜʣˇ΄ЃϔǚӉΗϯŮŜ]ӾƇƐʞԍ˖ǔ˚',
                    'arguments': [
                            {
                                        'name': '\x9dʕѸƢϱ\x9dȕѓPΪɶΞшʇóάƣ\x935ӳʴѰåүӶԦƎί¾Æ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԤȭƗu\xa0',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4423412302277050244,
                                                    },
                                    },
                            {
                                        'name': '~ˠȪĳF1µɋњȣ˦ƁǟίɷǭҶǤΪс',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҺɿYǾОğǠÿ\x9c1ò|ĄѲҶ\x8bԒɖlǇȀįч˷ѳωЭŴŲƘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            369234.85515145963,
                                                                            450856.9254460167,
                                                                            504969.8699309741,
                                                                            208309.87520760426,
                                                                            428028.2465406365,
                                                                            892457.2265736754,
                                                                            334736.8931170539,
                                                                            122718.05098709787,
                                                                            106544.78846106736,
                                                                            -20137.126422581146,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԦȗӥŶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ˏΏΎwӨȿ\x90Ïʨ\x85ǕƜBægȡѥʨǌNƑ˩ӶЪäƭϪ˲\x98Ό',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ă˸ʱĂΛʅήΔƃϛзñĀƕή\x8cʫҖ\u0378ÈąøŏЎiмҔ˞˒Ȍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӢϸљƺЇúҩѩ\x90B@ϲχÀbҍʓ;ˊВȥǨύвҾƆɱίUΩ',
                                                                            'ĵӹђ·5ХΛ˸ƥČƏĭĊȠ˵ɩǡʾǿОѢҰԨɿ˗ŗĿćýê',
                                                                            'çŽ§ˌ˫˃ʧ;ԇԋȦβ˪ĥǙӚɩӹȢ\x92Ï>ΛŊГӳ˗uҒԙ',
                                                                            'Ιѯƾпŧǥñ\x95ЭәұϽҰƳõǄ˜\x93dȉŮҋҵǤM˕Ь\x7fȀλ',
                                                                            'Е¿ǃȄҷ\x89Ȋ\x80\x92ћǎЫϧŧԦ˹ҪӘΈԆ\x89JЅě͵Ă;ЋӡM',
                                                                            '\x91ΧƐÒȻϛʒ,Χθȃҙµ\x87βӒϴύçʏѶ\x9dԍĒ\x93ɤͺǻӸǇ',
                                                                            'Ѕ\u038dΰƧʎŅ˘\x86ԈM"ȥЁŘ˰XгϤΆʠȨρӫΧѳ˃ҵƧχȭ',
                                                                            'vɵѢɥʺШη\x93ΕϬңĵҜź3ҬÍ8ӺzΑĜԟʻɹ˰Ǌ\x95\x96ƹ',
                                                                            '\x81ǈԤάʙқΖ\x83Ό?сȵ¦˪ňİ˃ÇϓќêΞϿƷɏѻƠŐʒ%',
                                                                            '¡ʸşƲɐ\x81ҀbӎđȾВMӃɃĉę˧ðƲϲįƏ˅Ѕ\u03a2ӞƳқЩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϽɪĺɵԔħĻȟʀżɖƂϺӵÈԂġʽJԑYÚÒŶӒȍ^ԚΨʷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѷĦÜďɂ\x97ȺπҕӖӡwșŘŗΎçȇƂĚƷ=ʐҀɜˏȼЫʕЉ',
                                                    },
                                    },
                            {
                                        'name': 'ү\u0378ѬʦʋņÕƩÉɶˡɋ£Ǣʳш˜ǦЈȺèθкҧԛˬЙ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĦăПFҧ\x9cҾɥɑϯҍӂϾ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'бǀȭȶȉɗɇƒʘįҗәĽ·ýʪȵїȯɝÍÝΤƇԘśӓϟ\u03a2ȃ',
                    'message': 'ω\u038dŻ\x95ȒϵêĿȒΟϸҕ˰ϚɆ\x82\u03a2зȠʣm*Ǟȿ\x98*,Ԥđӎ',
                    'arguments': [
                            {
                                        'name': 'Æșǫ\x7fѷ±ѨȨɃǷƭuТԩȉĩɮěȌΈУȆŵϏ\u0378эҥǲ˅˻',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ËҳҊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6985193868893197937,
                                                    },
                                    },
                            {
                                        'name': 'ʫką',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            396069.2226515973,
                                                                            107865.71427674894,
                                                                            217174.33751912025,
                                                                            549895.2096046378,
                                                                            25650.2761199885,
                                                                            406086.7121398983,
                                                                            128489.27454265486,
                                                                            556074.0102735063,
                                                                            432148.9927887104,
                                                                            359599.1954201633,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѝˈɒπлѰϿΝŐԖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -70632.71622697641,
                                                    },
                                    },
                            {
                                        'name': 'ƼǺȬęǯĻι҄Гðɝ¡-³ʨϥŔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165925.256987:+0000',
                                                                            '20210302:165925.278053:+0000',
                                                                            '20210302:165925.298972:+0000',
                                                                            '20210302:165925.322726:+0000',
                                                                            '20210302:165925.345758:+0000',
                                                                            '20210302:165925.369905:+0000',
                                                                            '20210302:165925.392036:+0000',
                                                                            '20210302:165925.415842:+0000',
                                                                            '20210302:165925.439042:+0000',
                                                                            '20210302:165925.464419:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ňӥõƘĝɁśȃҝҫƣΦśѶÿ҄СÂʏӂʆПȤȪѾξԡџЀʢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6252585295579299125,
                                                                            -2862588290061001076,
                                                                            -2777732799640003303,
                                                                            -8983123693478929258,
                                                                            799546580625184510,
                                                                            -4511084339851749468,
                                                                            8350207496115554806,
                                                                            1702280589202400208,
                                                                            -7745112501023620249,
                                                                            -499052309445417983,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҉ƯǌЉӱƤǝԕí=ēӌȑ"ӥԖԦʥұӘCõȳѱǗҠϓҜƹĕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƈɕŷϋ˩ҕҠǖϿс¿ʤəƟϜȝ˒оŜсґѹ5ÇԀĂ/ί˵Ǳ',
                                                    },
                                    },
                            {
                                        'name': 'κȦψԀȖĆóÉͲʪȅÂɛčɊγʢɅԭ˽˨¡ҔɳŒĔЇ;ɷȆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2785778054126776877,
                                                    },
                                    },
                            {
                                        'name': 'Řȋųň\x8bʖ\x95ƷÔΎƎƊөȯvȹι',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Џ˴īƑͷп˽ZŀĊԝľƩԟɣǢˉҐ˲X\x8eɳ˰ˮ˫ұίƐGю',
                                                                            'Ņĕ˔ԇųĩ«Мċ˯!ŘЃӑԣԦԊҊӉͲӄ=ϖƪVçəԝǖѻ',
                                                                            'ѐɼϾѦêȴʎǢԫʱРʉҎ9ƆβƟӦʀ\x9eўŦЦ˟ÁƿԖǸмǱ',
                                                                            'мȅϨȲĊЧɃ\x88ʆȳǴɉԫūȯЛѐԩˆʫê4ΓɎ7ϻР\x82ϘȤ',
                                                                            'ºĐ\x92ӨHϗó\\ƅɹ˶ФϽ{ӨĖЙоƴż&=ƇȯҤąǞҐ4ь',
                                                                            'ˢĩӢ έ>ĤЎƼ¹ˇŞŀίˁͶşn˽ϟҠЌġϐѬҐΆÂ\x99о',
                                                                            '?γфǯҥРŐ˚ƘàƋǙʃăǔȩͿԔĆƢȊ˖ʩΡǒÊˀɘèͲ',
                                                                            'ӃƿӢΧʭўЅϽђӗųόȟˆĪǊϾƻŖċ\x98ĊʧĨųʅ˵ɏӔӿ',
                                                                            'ƒѶӖȍŴ\u0383ɉɾҪѲѨSљСϛԭˏɨңƦ҇ĎřſӠˋʈԌҖү',
                                                                            'ȫĂϛΕɁǔͻŊȐͲˌĳˋэ˹×ƉĶǭͽ͵ôєtˋԣӍ±ϥƗ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'иӝ˧ϏαӁΚ˔ŽӠѩȻɣð˼',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5041501566860569462,
                                                                            2414619955205013668,
                                                                            -5599531422922026087,
                                                                            501117048339461994,
                                                                            2266851623775571823,
                                                                            6988216267956093130,
                                                                            -7419741086918581748,
                                                                            7286605072304478600,
                                                                            4482905146620951209,
                                                                            -7038263726018177066,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': ']ȭķȱȥԆˍOҴæϾӴȊпѓѻΨɔ˼ӬÅ\u0381ǿҴҫƝaѪĈý',
                    'message': 'ԕҚʟ\x9bȖIʘʈ×КHɾӦ\x91дİŶĒd\x9eĻзʓҥϽγÀšƙɒ',
                    'arguments': [
                            {
                                        'name': 'ɥƵԈïȱůŕћѵԟӣϳʯͺ\x91ȸ˸ԠǬȕҦĶ˛әҫӦʜŏʷ_',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165927.153107:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ёщ8mĩ˺ҝÇӲΆϺ)Ȅ\x96ÑÝӾƍªӝͻ˰ĿŁ˥ȹýJ˼ı',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': "ϸĹ\u0380ʸ˕ǐҤʚiȶż˴ʜ'ӆ.ѾӃʂɃ\u03a2ʨȨĳǮӳӳκǘΟ",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            694193.6742589948,
                                                                            556279.0658645335,
                                                                            178153.2571258722,
                                                                            15522.349220445089,
                                                                            811303.4777706244,
                                                                            935756.0163696919,
                                                                            114737.94078457094,
                                                                            50077.65665167995,
                                                                            604128.4747687594,
                                                                            -43953.89339588829,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȡҩрʛѴ˭μυŲſƒԖĩ8ҒțʟʻŁƱЪέɛΉŪ϶ԮİŒƏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ѵņ~tԓ˝ȹƛъԛǸǙ\xa0ɐɥӛgɲ/ȉʁθ҈ːɻϢ\x9c\u0379Iζ',
                                                    },
                                    },
                            {
                                        'name': 'М˳ѠƱѭwˮƵғ΅іϭɶЬxiˮϓǘò˟˸рȈȈӸЋȟʕ>',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɒÚԢƀԩ\x9aʙšԂʌ>іԎӡȳɭǧΣčнƷΞԓ˪ϻҖρϽԩÏ',
                                                    },
                                    },
                            {
                                        'name': '\x9eΓԐÀüӞӈɗ÷\u03a2ĉ\x88Ȍѡ6˧&κ˩ƆҐg˥ŌЙ2ķǤʭЇ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ι\\ЧaΗԡ%Γ\x91ɨҾ˰Ȳ˗љѱüķӏьыƺǦɍŵШǭҺпś',
                                                                            'ɋɌӻԏŃǛԠƣ҉ó¼*τùƚӇŬɓɧͶHӡ8ʜӯӴІМǨƲ',
                                                                            '_ŉÍȅaɘȭȕ<ϻʽ\\E»Ƀ˲΅ΈʟĜŚӒĴƢ\u0383Ɯȵ˰Ŕř',
                                                                            'ϕʿЧΓîɝɢBr]ҖťќÕ˳ËǝФ˝ͺӬȱψԆʟyïSǌ\x85',
                                                                            'ҧδʞɬӆǷːɻƽƀӋǌ«ĈūΠˈ˰ѕԎʢĈƻˁӼěǠ˔˔˫',
                                                                            '˯΅ɵԬq\u038bͷʊԈѤӗʪŐŁԈʙɃτȫ\x84ȢѯĜҀͱÅпīϭʭ',
                                                                            'ҭţɥʑ\u0379ƍàƌƷȲФĜƋүɊǾǉɽȫԆ¸ԥŎЯŶǮfΜԒԪ',
                                                                            'gМDȪǧ-£ɪp>γǗҪЯșʛϙķ·ıƵŴϺʞ´2Βҷ!ɢ',
                                                                            '9ϫˁɀʹþκҏ.ʉˆŕƀͲʢϓeɿƜȃӫΟĽ5öйÞʱƗ\x81',
                                                                            'ӵĤˋѢɩʆƥʥȬùЧҨLǜæ·ʮ\x82Vʗ®˹ӆȔӍɪЮʽ\x99\xa0',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ǓǏлбƔȜϔ'е\\ȑ²Șϑg˼ɡw",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            392859.82844697766,
                                                                            548376.6778149831,
                                                                            652317.142845596,
                                                                            404017.5966898348,
                                                                            364789.007307051,
                                                                            -56797.364967727604,
                                                                            -91959.5501493918,
                                                                            -87720.9836414517,
                                                                            936465.0484431401,
                                                                            419575.4204819045,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѿԚǪчίǫϔʸҠ±K',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 11133.259617171498,
                                                    },
                                    },
                            {
                                        'name': 'ãр˻ȃđǵǴӉΥ\u0381ѫ΅ΓkŘÇΓї²ΓЧύ˫ʶ˘LӶƚ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165928.622528:+0000',
                                                                            '20210302:165928.653217:+0000',
                                                                            '20210302:165928.684278:+0000',
                                                                            '20210302:165928.714057:+0000',
                                                                            '20210302:165928.742689:+0000',
                                                                            '20210302:165928.772939:+0000',
                                                                            '20210302:165928.804081:+0000',
                                                                            '20210302:165928.831377:+0000',
                                                                            '20210302:165928.854407:+0000',
                                                                            '20210302:165928.879631:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ғӀŋVë',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӥŞŝ˼Ўˊ\x9fͻ%ξϩƈ}ƅ˹ʞȯĵϐ\x84Ĵ¾ŜӝѫˆΞϺȨʇ',
                                                                            'Ǡďb҅ƣгyҔԩЄŶɦĒȒӑòѳždҷєŜɣψȺҪɈƴ;ȃ',
                                                                            'ȱĳьʩÅԆɛҦʠƥɩǯҜψљƕLЙɘĨȗƩEĞˍЖWÎїͷ',
                                                                            'cĈўǮҠȊ҃Șӏ\x8dȌԄξˠкΈǒӟÑ\x86ćƣ\u0378ʤʲÛƕƄċϑ',
                                                                            'ĹʦϤӵәƣßUԙеɠŋƍǸ҉ưʕ7Ӎƾ®\x94ǆ*ю\x88϶Ä͵ß',
                                                                            'ʑ>Ʈ\x94ϗÕĒӆƚʨɼϵđȼʙˉƥљƇΊЇфҶҫүŏˇɯˋӟ',
                                                                            '˸ȦɲɟǥɚʦMҲĴЯșö8ºͺǱŖЬƶԃǠɁɆϫϻƦQˈн',
                                                                            'мǌȂӻǆɻ(ћǜ\x7fΐϏËӹοΧĎ·ǦȯȌӉˤ\u038dǰѥüĐΤf',
                                                                            'ƌaDϽҀʯҷϾԙЬYǍɟ´ѳǔ¾ϟȠ\u0382ѭͳŉϵżϼѫΟπĬ',
                                                                            'ĚåҡɇŸ\x8d\x9dӟöΧƪ/Һ˗ϪӀ»ŀˏʓĭΠԔѓʨȾȍ˗Ѻƒ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŁKΎòèŹ˝ȂЦәɚΟ`Є\x84ʞ˧ǘʞɲѱƃҊΐǵȃηʣԏʚ',
                    'message': 'ƬĞ¹үϮɘъ˭˦ǐϘǁǧɧnƱÞԒ\x98˂ŦȣԝҌ®чήΩ?і',
                    'arguments': [
                            {
                                        'name': 'Łџ"XŉԥæȗȊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʙºͿȈ\x90PÍǷЦ\u0378˗ӻȼÊыīРĠþĬǖҹÜш˗˗Ϩɚϼ©',
                                                    },
                                    },
                            {
                                        'name': 'ΆȰę\u0382ѻҶĔ\x9b´ӛƪƬdņˀRÅ\u038bǣӞБ\u0381ɞFȉ¥Ŋò˫[',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -14728.66768640095,
                                                                            223799.94043549924,
                                                                            138413.36901558912,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЍәϠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'эʇʨȹθǶʗƄѸqŵȓӠʍćʿѭќөǛɵ¥úǛǷǩуQȢΪ',
                                                                            '\x94~ˮȕϪÏ\x98ƑԑyĴ҃ˑáưԍħЪϲаěԭґ˾ȾϴύԊҁů',
                                                                            'ӪƂȥƍÙӏƪϺAͷŻǗèԏ¼ņѠɆӖ±ʈƘъÞӞϓȚȧʮЉ',
                                                                            'ò»ĬѱʟȳмŽɃǯήѨʤτÔɰʲÍċņƓŮƯ˸Ą˦ɏϨˀŪ',
                                                                            'ʩɲ9ÆέʗɿǪЌЭ\u0383ϐˬѵȒԢĹƞĸЃȐӗʌ2ӼȎÖʓғƇ',
                                                                            'É˳ŎͻӐҪ)ȪЪхқ²P£ɯÝǌȵΛɭĢ¡Ԝɐёν{С҄ӗ',
                                                                            '2ϓԛԨŶӮ§˖Ѹǀ˟ǇʴȚҐīŗПТӯƹJǴÃÔÝԋѡ÷ѣ',
                                                                            '>ʼѤҌɪˁɀѵӗ·:¾ʙ:ͽԮԅΧȃӓˮ%ҶõͷΖ°\x9dʼH',
                                                                            'ƙїǗκҗÝыˁJʕǷ\x9aĿз\x84ʗȇҵԂΉғıʢҰιʋȖӵ҄Я',
                                                                            'Ӹ\x9dαŭĆƮʻȃǔǬťЯŠůŷ\x82ΩҠǢ²<ĬӯļėӁĺƜЧ2',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ω',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 204338.31701604364,
                                                    },
                                    },
                            {
                                        'name': 'αѯԤӊԆƈӄȐӿ˲ëԬȲγŹ˼˵˛ç҄ϗKпЩԍ˯ξɃх\x97',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3329491078931430111,
                                                                            -2789647561013376865,
                                                                            -5948877430586979878,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǽŷƅ:ȥŠ\x95ʪҲͶϛ²ӥ\u0383ǽΚġèȇʐʨдυ~к',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165930.179356:+0000',
                                                                            '20210302:165930.202480:+0000',
                                                                            '20210302:165930.226125:+0000',
                                                                            '20210302:165930.248880:+0000',
                                                                            '20210302:165930.273452:+0000',
                                                                            '20210302:165930.297137:+0000',
                                                                            '20210302:165930.322497:+0000',
                                                                            '20210302:165930.347050:+0000',
                                                                            '20210302:165930.370054:+0000',
                                                                            '20210302:165930.394162:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'KԨţǸŷԨǨϮ˫ǁÌ϶ɿċǮø\x9bΜ\x80ÌúVˮàòɄԢэá2',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĲğĠɣ͵дɓōŬӕ,\x97χн"ľͱ\x88ȎԊιŪʺūØkӮƕԧξ',
                                                    },
                                    },
                            {
                                        'name': 'UɵŚĺʳGʘœţɚҜҒюɏђ±ъԪϐԄǚҚʞˡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˎΟϏήПϳ\xa0@љȔ˄ƹÔȆԜDƁҩqǔӇÄӲԖȵȥ}eƟɈ',
                                                                            'κ¯ԭѱ¬ϋʔϋҰӗЋȘȐʨ˃ʹћňíΰР[ԮȤӀȗϘʠэӱ',
                                                                            'ɹ>ҮԦƠЖĺʎ˗СΧ҇҄oɢӕȔ§ɞȳƕϟԘȨЮӋыġ\x91.',
                                                                            '\u038dǔÎĒүɁѣϛɎϰθʎíə҄ĸʎɀϡöǼß~ʬśĨ;˺ԜЩ',
                                                                            'ʡӈӈǱ˙ʝьȩȹǒџѨαҦ»Ē®ӪʿzƋoЙОӍɊǁνӧɮ',
                                                                            'ϓ\x92"gӡԤĻԎ˓ѸԑмrȽϦυű˦ǹ˝ҩεϠЮѧЊȹȚXǙ',
                                                                            'ɻѿưбȉϟȔʁԋΫОż҇óѩΪӉì©Řѯȩѣ\x83ĩɴÄɉŝҽ',
                                                                            'ɨĽŵӖ®ʽ@ƾ˦ǅȟŀѡҌƎЫӕСö«ΕƄУ\x8cɏĴ\u0382҂Ӕӥ',
                                                                            'ĐЮӫʫ,ƣҰ"ʈɒʠӯЙͶ\x8fӹƕʣóėȀS\u0382уȰԪ´Ԯҝ§',
                                                                            'ЪǫǈÏͶңǀˏωȺʹͿǓЃ\u0383hǜjǵϘҒɨʷ\x85ː˧ÂǓƐѡ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˨Α´ǵӦɏΏēӣ˽ɛɆ\u038bǖӍĖŞĭҹɤιɡʆą\x98ԥƁɁ;ћ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ȺƹКŢ¥ʝɥЯЙӃˇϪΧƾм'ŭƾηԠĢŹþɨRӔı\u0383ǻˢ",
                                                                            'Ƥ2ǿӐԈŶùĎ¸ҐԞűƠЁǥϼҟφϵĔª\x93\x84˄½ˉɁԮƏλ',
                                                                            'ǱɂжȣíҳņɬҶϦЙȥ/ʌȉǨƂԍˊϤʢԋʅϵůҠÑɜԘÐ',
                                                                            'ΠãΚǉŷÓˌΘƮҢҝŧ\x96Ȏʪӹãĸ#\x8eÔЌҏ\x9bϽďǈѡ҅ŝ',
                                                                            '¶оʡЮУ\x96ŅǗԅƶǸӰτǵϳʡͰԉƊҫ϶ȵ\x9aZȔɇƃöԍр',
                                                                            'ʙæAԁ҂ϹЊͺƹȅԅRD=ɘńѓ(ʮƳłͳöΈlġƮ\x8d\x84Ӧ',
                                                                            'ĊɇɸǍїǩ¿Ǘɱ¾ƦӉǤɝƺΙиŠdŶƚӞЈӯ҃s»ˊ&ш',
                                                                            '\x86ϚeǄĠλʍƠѶb<ʧ\x92њǕ³ȕǨhΎфгǤŰԆėǺɻƂV',
                                                                            "ƀÅLњѧgӍҁιȱϣЖɇ'ǍȽėхŧЁӞцʙnrȬӇŕ˧ԩ",
                                                                            'āǶ˩ϩŉɸΌЪͶͽƻӌѲ±ŴɴȂΌƚƞȰȰ˕ˌɸӹɎǪ7ѿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʙ\x95Ϊİ*ĲҥͲǆƭÆŧӎͺɜȱӏʴ>˞ѦĂ\\ԩ?ӋԧĜԋĵ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'yʈӥʷΆ¥χȼȍЗϮͷӍñǤӟԙɟƈҬҟʀʋѥ\x81л\u03a2ĢĊȥ',
                                                                            'Ҍ˃ԙˊϼЖҪȾAӸzѻćԡɿǮ.ĄЈԓѶǤϧΤԅϪ˦ϱć\x86',
                                                                            'ɂNǭѱˋˈì\x80хŤÆ\x89˥ǟͻˬİїԐ:MΒґή˃ӳӍңӪУ',
                                                                            '5ȫ\x84ʹ¤Ӗé΄ȻҮcfєуЊŻǾȺĠĠæӚÔǡȱēģҫһԧ',
                                                                            'ĈԙЖĵƒEɠµҕ8ōȠųďҺT˃Ǐ˝yɝϴǨҼκԎ§ԍʠ¼',
                                                                            'ˬMȅЀȰƣƶӦHϋȈó×˻сŹȲύˡ˶ʅɦǹҀ~өŀƂqĎ',
                                                                            'ΨɶȬUȬyғĿǟĺn³ɨĪŉǃŘȸƖ\x86Ŏ3˲SҗȑϴʼюȤ',
                                                                            'ћˬΜ\x8bʣȿŧȸŢОȝϮȍŎɻДǙΘɮ˷\x80ɱϸť,ρѬúăϵ',
                                                                            'Ԙİǭ\x89ãԫȾČԄΔ¯ąưǫȮąΫ}ƂȓԘ\x99˾ÏʂƐх˅řm',
                                                                            'ˊŠԫϊ҄¤ӸΨȄɳőύ\x95ǃĝ˽\x84ÌπԡΜĬõҚԓ0ū@Őϻ',
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

            'identifier': 'ɻƵ˃Πʆ',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'Àå',
                    'message': '{',
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
            'request_id': 7310516,
            'error': {
                'identifier': 'ûКԈӛˆЊԔ˩ʰΫ¦˦ÑǽӧӿǒʖŘѲȧєǈкԖӡ¸Ψϣˈ',
                'categories': [
                    'invalid-user-action',
                    'access-restriction',
                    'internal',
                    'internal',
                    'internal',
                    'access-restriction',
                    'invalid-user-action',
                    'configuration',
                    'os',
                    'internal',
                ],
                'source': 'Ԗғ\x90ͻ<ĠЀµҀŬӱΘ˲Ȅθ_ӲōвǗÂŮÏ˚5Ԝʜ¹ћм',
                'messages': [
                    {
                            'catalog': '\x83ÐɸЍϊ΄ϬʼɝтǒɐƨʟǢіO˂ŖӘίϣĜOȄœù³ňU',
                            'message': 'Ø\u0382\x98JҡζŖǍԝϺŰɌЭŇϹʆȵѱʑхʐʟȡͰҬӋѱӑʚɡ',
                            'arguments': [
                                        {
                                                        'name': 'ĸɔԐϊǈɁŴϊ?\x9dˆsҚԗȨɐЉлɺĴȼʿСԄӧʫƪԇɏʳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5477519198933758055,
                                                                        },
                                                    },
                                        {
                                                        'name': '҈ǎԂӇɽӛŌҬ;Ҥȿ˨EȈ\x93ϕЫžϪЙƖгɦŻ`ϪύԚԨA',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2398260581816068037,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϙʚ^ӻӚʯɖԢɘкĵˣӺΏ]ʐƩªһë=ФʼˋωΦǐ.Е˛',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÐȶBǌʛĭƞеˍˬӅƸÉƹϳѫƖāԐƢɛdǋԐĸēă\x92ʣӇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'љЏ҄T',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165901.978518:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍƦ¶ϏǫǰҪϥșÎЅʨЭϊΦʹЧuǝɰ\u0380ţϛиːǲƋ˅¿ʯ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '϶Øӿ\x94ŝȁшϚ5ϣėćЄŧǍýΏӠRӔ{ԙԀҖbɏϾʮƲΞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165902.219741:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɤ½ǇǥϞБ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'åвͷ:Ёˈ%ÂˌõƶʁЉ¡/ϬϠʨŘŸÀsǔjӇćϖ˲Ąʨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӹ¡',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʜȹGFԭʫˬ&\x98ϞûòɆ\x90cǵаɆÿ\x90ǖɰΖҒΠǫ6(Qǭ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȈϺľӃұьɖŌ7ǊˤğňϋǽάHЄʟQұɽƺƖĩЮɩԏģī',
                            'message': 'ʺƁ`ԤҰӮӌ¬ǹƳːӺY\x91Ø÷ҶЁʩðԈïҲìɖʏӸȒҝ϶',
                            'arguments': [
                                        {
                                                        'name': 'ʌǫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165902.669540:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЍҘЕʝț]ԁ˜ĪѮͶŒ|җŘźөfϧʚ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1942575412450119443,
                                                                        },
                                                    },
                                        {
                                                        'name': '҄ǰûɺǽҏƜӫԤѥŽӷӛӪ˴Ǖїϑ˕ƨ9Óԏǔ҇ƪўνʷ\x84',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁƽΤįâѕϖ˖¸ŷƔ«ӈӔʊˏԥҙӇĝΓˆƧǞԕÓʾƏ#ʆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǵЬԤɝϏщеΥіDŹɢǥ˵Ѱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'éѹΎɲȇϩϪӅΊʦ\x9bâȰĔϯԫԌȯРŶ˝ӻӚ˨ͻσӧÅċž',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƗӬώȼѿȔ<ѬΟ˝уĸŲ[ɐŪČ¤ȡƸ\u0383Iҍ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǣɖғʦĥ\x81ѱѩɤϑŭρEˢýԆơΠÞӌȿҼ\x86>Ʒƛΰӛϲˎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǌ˭ǸѨ{ƧþǪǴɕŭɣӎØЀȤȝōӻnГÒSѕґѤ¨ɀҢf',
                                                                        },
                                                    },
                                        {
                                                        'name': 'τԏ5ʽԛÇ\x92ûǓΠ\x99\xad϶Л΅×\x92˷пŶԦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165903.409924:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔǓťУǁǆàϴԇмŧ)hҋÕȿçȃΨʬǮÃԗ½ɵЃűċɜі',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΫƾϘ˶\x82ēĲϧģĢǜɩȸ?ƫȦʐ7GϿӈ0zϯ\x8dɫӿɯ¹Ћ',
                            'message': 'ԀȎǎˠсΨə&ӣӭ˾ҸɹìȗŠƱCΆĩЎήǽѲʈĄǇƽǷġ',
                            'arguments': [
                                        {
                                                        'name': 'ѫƭҏԍĤЭaϩŰφĄұ˒ԤƮɫӘēŻӴJ¤ͽŗ˵Έ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x82ÎȚΣҐ7˭ƌǁ½ŎƉτϭʒԌѼ\x98ɮҶýʑǕµӳвҏϫϟ+',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˛ˣȰйЯéŞϦ®ӧ3ƙ4ȹÒ˥è˹ŊҨAӣҍʙώϔ5ǨΗԏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɩ0¿ȄȶƂ,şȝBķƫԡŊΥ\x8fƱƮñkΒʠǵʐԊѠȩЃ3+',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԗr',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˾ěõЦ\x8b¼',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґŏÆ\x8c!ǻҘщƏǨDȖөВҤƺļɩƈTˎʲžĔʉĎԀ˔',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7991936363112870173,
                                                                        },
                                                    },
                                        {
                                                        'name': '¯ȆȉŠԚlЇʔÜʖȿӐƆǰľʁ\x7f˔˴ўÚMΌÀρЇĦϮҙÕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʺÖōˇԅџұ<\x8fůĝԒɁʠĸϡρŏӑğδƌR\x9fмΰ˰ǥƁα',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÇʘġԖ\x81ġȩɹćԭ3EΎć϶ϮųˁɵţƩӵ¢Яʚ{ӈғͼҷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165904.383788:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύĬԊʬȌԫɟҍƆИȝÝvŞʡ\x7fԢѻ˂fСъƄο',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165904.470477:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϲ9щɘ[ʁřҟĈЩňΰ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϸAƿѺ\x8d+ĔɖȰjѡϊǐˬùÅŃȊÂщÜӍȖ^˽Ǧk\\ǧӝ',
                            'message': 'ԮӎŻǏƑЕΦȫŤІÈμҾУɌΔԩŮ\x9fɐȔȾ˃¢AɕŉÈ\x9cȜ',
                            'arguments': [
                                        {
                                                        'name': 'ʬ\x7fҟԠӗʩãҍ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '1ĀʎªӱÍӘɖұɎƭȵįˮӄзҚəѦʣӀȎŚϊӍ˟ѶЫƃƬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȯ\x8d˰0т}ȉɢÓԢƝϡѕǰʖŝĳɾԜ˽`ŁҎĬΟԂŌȔ\x93Ϭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 590804.1376885639,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ä\u038dξǢϜÃɓ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165905.070840:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÅzȔȃȜҨ˲ԄġÉΔѤëѵM;ҲzǟbҾŜąÉŞyӒǲԛs',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸ\x9dӿȡƸӨ\x8fĮҩԙ\u038dԛɩƷúѩԋΘʯҗѶҥςƼӻäгѦʼǗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 260630.265844376,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˡΙTԢӢƵЄɋʻɃԕ!҆Ī˴ǥцВǽɔƂǞԇĳϏɁɳҐxҬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʬÈ\x81ƅĄ˳ҝʜƶҘЃϛŉŕԭ+ԨͱΡãɪѾȗѥҚɌĖϔљÚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛĜЭͼȠǠЮ3ʲǷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŬШ¨Gó\x9f@ɵɧơʶϳǥǗѢğ˅Ęëƽñ/ȼφʷΜƋùΧ$',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔüˠÆ@ϱ¹ǑāӍϗÝǊҠŠżĵǉĪľҍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165905.626117:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƿΊұԭϟΈǽɡŝŤ˳ΊɫԇӫǼ\u0381şºϙȢб}ϰЋμĂĜ|Ѝ',
                            'message': 'ҼǨŏӰϫҔ\x8fӉë\x95ϝʛȠԎӰŮёӇϷŻɅ0эƄˤáµ²κɟ',
                            'arguments': [
                                        {
                                                        'name': 'ΚɮρӧƼѠҖÝɣМљ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȏ|˶ӉǣOӇƚ˲X΅ąξFȉůčϯΞӻȨԞǸȍЫǪtɐһҡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԉͽ˲þʱŅЮ˪пʑƼҍǘφźԪφˁǸ:ƔȁѺɕӔÙΜɥǃ;',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '9ʫ҅ϟН-*ԅȪ˺¢МʊĚѴúģ¾ЄɥǁˡȿҭУǎɴφĀ4',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԓǹhȬДδɬԀÃǁĵō˔ӵԀɞȣØ\u0380ӳńʔҙ\x82ƩƇӕƫɪ˫',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛ\xa0äƸ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʁƁÛ0εʜĿvěвÕΎғǣҐĵʗ¶ă˟*Lʈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɴПĐБZǁĞĘɛӣӒ˂В4,ɾУĆүԔȉ\u038b˘˱ƴȴÏ\x88¥É',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165906.411590:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Wŏî¡ӴέȾˈΥ҉ʽɹӤ\xa0ôȤŞkˉΎԣǗϛG`ͻЮ\x8fÅ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҬʈŭνǕƃӸ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '÷чÅӭӲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ñǒһ9ΜĠӜӀҍǃŵĉϧзɯňēÈӐ\u0380Ψ]ԋѬņƳŻϧ˴ŷ',
                            'message': 'a˦Ҁѵɭƕϋπ˟ɄԑÙƭќзŦʍǡǂԖΌЏɼg¼лӏ\x8cʑζ',
                            'arguments': [
                                        {
                                                        'name': 'ӨƔɓ\x95eӱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʵ;үҦǧЇƋѮЎˊиv·ǧίԍœȡˆϺɱǮāϐѡȡCΓ-ϭ',
                            'message': 'ԌсӤѓҥҶ·ɦÈӾƹ7ӀóĀӱÝ˹ӄȯ\u03a2΅ϊɱȸʪΙΥŅѺ',
                            'arguments': [
                                        {
                                                        'name': 'ʩȩƜ_ǩщÀ_Ҝ"υɴӹĜПǂӅ ȏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˩ѹӋȏǿ\x86ѣϓȽ+ˇ¨',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˜ϕІɆƹȾŴ\x87ņӶѝĐĊӏҖƈƁӜ\x93ǁҁ\u038dT,°ЩΏƣȧȎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 376886.89913453645,
                                                                        },
                                                    },
                                        {
                                                        'name': '°қƂΎŚ\u0378tJzǢƎŎ?ȏˍӋ9ĄҵĹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165907.291579:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹЮ˕ÜȾωƋƟɍǚФ\x9c×ϴd˧ʾĳJǕ\u0383ǋԟΝaΊϐЄÔ¬',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˍɟƠϋ\x86Іū\x80%ӻʯˁȩˮ,Ӝŕʢɏͷϰ˲Ɵȗ\x81˭4',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϲҺәѬɾΫΥCʺF2҂øɳˠƀˇƽ˄ӀˣìǞƴАҾņůΌė',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ďȬ|Ʌѧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ğĪɺГħȍŵаӓǛԞԑǭˊåƔӋѭЁϳ˗˕ΉНίĉƋȃƐ}',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4113627630966726071,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƲűԮҘŸԕ×ɭԄǉʝƿɳǊ˩ĘЖҽĕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˴ˊ΄ΧԠÑӋăwȤɔĵΪЫҘΓ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΒȅņѡɻÂ]ϳśѓԈ˵ОβƒƉǗѿԜǬͺÎϢԋҞԁԈ\u0383ýǸ',
                            'message': 'ɉˀ)ħÊѻѤҕ\x86\x93oǂªʥI҉ɹÜѯ\xa0ϊ˹С=Ќϭќ˓ˏ²',
                            'arguments': [
                                        {
                                                        'name': '¨ЄHˢœGǬʘnţÌӽӥ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -776522529674672337,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɲĭ˽ζǆсԞÙĐɱȑȖʃʵ¦ϤƄϮ\x82',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʨҁɓȴθсŬǪϗλƇȶ˷ʵʄʢ͵ʧԭŗʣтƜЅqƵ˸űſͶ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÅH9ȪӿȬĠăЪɞǱŽϴ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'šӑɂ\u0380јĴvђЗʶѐʆт3ҰɭÌ\x9fʹÔŌ¦',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6189036547153320339,
                                                                        },
                                                    },
                                        {
                                                        'name': 'αƯѣджѧŒҧЎÂ~ѴĒƧĮάЭʜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 841796594804493372,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕуĊUӵƝѭǰʖAôʟŠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϷȀГ\x83\x8c¦ļѲ=ÔӗǎƝȚԓƹǛĸɃȊ˾ҖƄϿɡϜŞϚù«',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ςŠÄѿαĜȾŵЉɶ\x81ʒ\x9cǬҊ҇˕ѫʒ\x86ƵϬԇĺ`Ͻò',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -21055.514388403084,
                                                                        },
                                                    },
                                        {
                                                        'name': 'µǹʽɉáǳюÃǊʎĬ\u038bӿӯűOЇpџӮɸҤϓɣЁсÏȔѭͿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'œeŗϰėǒυΎЪøŇǎҴnȄɀҩКԀ\u0379ӻʦѲĵîƶɬŝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԝsͰ\u0380\x82ӎӀ˧ʨòД³˟˳ʋ\x84ɮ¼οϺБԡґȮʹäϑ\x94ɰʠ',
                            'message': 'ѬҹѳțȀêϣ˴ϕIǾʑ˛ɦԓЌǴӎǨǊʡЧ´ȐɃʦȯǓƢ»',
                            'arguments': [
                                        {
                                                        'name': 'ÙĝîЁЄҧ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮǦήŋʊȫǁҐÊʁĎƜԆĝϡ£ҪŨ\x86ǣϴҜCΡҹ×ˣȭĥҒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5058894997281232173,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϚȯŭȳTЧĢέʼѺ(ȯс˷ɍ¡Úѯȇ8ӖÖєηˋŗȳƭɃŘ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˕ěǡƱПҬѓɪ-˰˸˃ĩ®ŏĠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʋċ¼ӊƆɠЦɀ͵ҕʭɦϢƜĮ˥ɍǢœ҇ɡî˵2ґԣӵϴȫX',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'єƊ\u0381ĺиǭʽ7/ʓӊȺϚљ)ĒʠҖˡɼύŲ,Ͳr:6˘˜ό',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'нÚҐ˶Γ\x8eɲΘȂóΙһʹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑӂȋˠȀ˻\x9aĘ¹ϐǏΝǫ.ŬϤÿʈѦԕɉʓôυúȾǑнɲk',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165909.782166:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆľÇˇԓԪͶ/\x96ːυĘäǢ\u038bÂҢÅʆǻô+ыʣħЄҗɰϊ8',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƒ\x9cǞʕԗĳя˥ΖǭϷJ\x98\x92\x98ǽǽƿȋǙƌɦĥѡϤɠÖЍӡТ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҭͷԚ\x84Ϧɪӫǥν\x8fØ҇Ǖ˶ȸίɲɬЌěʾÎJǸǻʦèåӡ҇',
                            'message': 'БǪȢMҖÌκȵÀɵŵԏɥĂɄƐςæΖ˸ïĜƄͷʽщˮȤâˋ',
                            'arguments': [
                                        {
                                                        'name': 'ɜ¹ƵĮчÛųѝîõƿïVǈǓSƐЀ҄έȯΩǜLɑРʵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÕӛÖM1ʙоĔƧŉđɎķӛĎѲɌɈɧϛʂӚԡӤҶĉˬ\x81ͰĊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΠÜɶƊ¹ЪˮӠʂ\x92Ӆ\x88ÔчǒΤƳӔǱʟХҝ¥ɥĈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѓҼɅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '?ʯͼΧɶ˯ϳC¿ˁϏј$ʘȑӹƥȨ˻ʀѳӣ\x89ćΛѹ\u0381ɆчҰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 119998.97595262734,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĎҚϦώɢɔ¹ίʶǏNƉȞ˅ԝ\x83Ν|çҒȸОɉԃ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2299832598346319461,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀɃʪøвҩ2°Űūʽjʹ6ƜҢ6ҹ˽Ɏϕō˩ҋƴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'љtȞɠҟϢŸʅȞƬԇΰȖʐ˾Ą',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'èҺ0ԉЙƢтĂǌƗԋÒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˙ѼƓ\xadȲŚ҆|ſԄӓҭȸřʈϞÎȰѓ8űώǄ\xa0ˍōƛǂİȖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌɃʚοǗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 678457.360842703,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ą˯\u0378',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -9207360381997014910,
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

            'request_id': -611009,

            'error': {
                'identifier': 'ɑɖīԖª',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'űɦ',
                            'message': 'ì',
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
            'nw_x_pixel': -374227891,
            'nw_y_pixel': -918055698,
            'width': -1267716664485526547,
            'height': -8106644494814078859,
            'ratio_x': 409586375134360382,
            'ratio_y': -9067414979983746786,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -1913169936,

            'nw_y_pixel': 24094254,

            'width': -924176563881735723,

            'height': -3351733135431293745,

            'ratio_x': 8491309696616235331,

            'ratio_y': -2088455393048882575,

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
                    'nw_x_pixel': -1716322540,
                    'nw_y_pixel': 768610124,
                    'width': -6378006437080866257,
                    'height': -6265907372162639091,
                    'ratio_x': -82186400048419806,
                    'ratio_y': 9207354270471631145,
                },
                {
                    'nw_x_pixel': 1879466486,
                    'nw_y_pixel': 1131363916,
                    'width': -8965943938593000299,
                    'height': -7881261428742916324,
                    'ratio_x': -4225252181789258712,
                    'ratio_y': -4696635781679251844,
                },
                {
                    'nw_x_pixel': 1756542857,
                    'nw_y_pixel': -1272858630,
                    'width': -5986641054804614677,
                    'height': -369278447135056833,
                    'ratio_x': 4888986069062134082,
                    'ratio_y': 4591792303109606279,
                },
                {
                    'nw_x_pixel': -1356645549,
                    'nw_y_pixel': -1690332273,
                    'width': -7005247682687861389,
                    'height': -5367248091920396090,
                    'ratio_x': -6032207316692205837,
                    'ratio_y': 5954602044408987011,
                },
                {
                    'nw_x_pixel': -1084918443,
                    'nw_y_pixel': -1550967171,
                    'width': -4509432285149511608,
                    'height': -8745221520293727308,
                    'ratio_x': -2329216388123286167,
                    'ratio_y': 6661436120756712977,
                },
                {
                    'nw_x_pixel': -1801614187,
                    'nw_y_pixel': 385860792,
                    'width': -9132082523263475694,
                    'height': -688695274194207184,
                    'ratio_x': 5377416662696821427,
                    'ratio_y': 7132113775437531883,
                },
                {
                    'nw_x_pixel': -1297477805,
                    'nw_y_pixel': 197351677,
                    'width': -1755786301807875530,
                    'height': -1777543640693131291,
                    'ratio_x': -6025804364849293745,
                    'ratio_y': 4140708983672436611,
                },
                {
                    'nw_x_pixel': -1548054592,
                    'nw_y_pixel': -796747124,
                    'width': -651972040143318400,
                    'height': -8426099710392842953,
                    'ratio_x': -8484258601441865743,
                    'ratio_y': 421296459855708943,
                },
                {
                    'nw_x_pixel': -1239054905,
                    'nw_y_pixel': 1610378046,
                    'width': -8632291632097579506,
                    'height': -8478610898664917102,
                    'ratio_x': -2157780354436717129,
                    'ratio_y': 8430946624993664375,
                },
                {
                    'nw_x_pixel': -1677162229,
                    'nw_y_pixel': -1039650519,
                    'width': -6097394910157997722,
                    'height': -7950774585277605092,
                    'ratio_x': -5146506514930992068,
                    'ratio_y': 6662266225329539904,
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
                    'description': 'ЊAȲyǂӨ˧4ЯѻӝčɻЉαěǵɃСҔǖǬ˅ҝ\x94ѧ)ԡҴԜ',
                    'monitors': [
                            {
                                        'identifier': 5211568,
                                        'width': 90737625887376079,
                                        'height': -8476608548877776626,
                                    },
                            {
                                        'identifier': 5894640,
                                        'width': -5359558190162909193,
                                        'height': 726227192030216310,
                                    },
                            {
                                        'identifier': 6207988,
                                        'width': -681377267698320544,
                                        'height': 8390442010867885046,
                                    },
                            {
                                        'identifier': 828070,
                                        'width': -7096848741230536291,
                                        'height': -572798422865377423,
                                    },
                            {
                                        'identifier': 2417229,
                                        'width': 3876656533652689108,
                                        'height': -4077404165443773355,
                                    },
                            {
                                        'identifier': 4857435,
                                        'width': 4065848341288037588,
                                        'height': -3774832914845706760,
                                    },
                            {
                                        'identifier': -555085,
                                        'width': -1041857925891180290,
                                        'height': 6392595796944377489,
                                    },
                            {
                                        'identifier': 7535653,
                                        'width': 220761867924981593,
                                        'height': 6367641249687840286,
                                    },
                            {
                                        'identifier': -882284,
                                        'width': -8548860343532118497,
                                        'height': 1250822294667277275,
                                    },
                            {
                                        'identifier': 5401045,
                                        'width': 6387625629992695942,
                                        'height': 4980346393547793150,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4987005,
                                        'source_nw_x_pixel': -2749952657611863680,
                                        'source_nw_y_pixel': -9117927929815904095,
                                        'source_pixel_width': -678146029235371736,
                                        'source_pixel_height': -2555175100391228965,
                                        'rotation': -5595214490043727793,
                                        'virtual_nw_x_pixel': -855533776,
                                        'virtual_nw_y_pixel': -1179399340,
                                        'virtual_width': 501939205,
                                        'virtual_height': 1634082606,
                                    },
                            {
                                        'source_monitor': 550929,
                                        'source_nw_x_pixel': -1173672343473856205,
                                        'source_nw_y_pixel': -6942181958644641410,
                                        'source_pixel_width': -6708280448399860439,
                                        'source_pixel_height': -1846624476168076813,
                                        'rotation': -4909219693018108613,
                                        'virtual_nw_x_pixel': -1268421068,
                                        'virtual_nw_y_pixel': 1062093174,
                                        'virtual_width': -1431477317,
                                        'virtual_height': -1292688484,
                                    },
                            {
                                        'source_monitor': 444875,
                                        'source_nw_x_pixel': -7191958646934330394,
                                        'source_nw_y_pixel': -8301139979642077912,
                                        'source_pixel_width': -4526164677985560247,
                                        'source_pixel_height': -4607960296413074950,
                                        'rotation': -5818601169152546979,
                                        'virtual_nw_x_pixel': -463476171,
                                        'virtual_nw_y_pixel': -901547234,
                                        'virtual_width': 644765853,
                                        'virtual_height': 1681906800,
                                    },
                            {
                                        'source_monitor': 2421703,
                                        'source_nw_x_pixel': -8940809159755699648,
                                        'source_nw_y_pixel': -6951531275475375203,
                                        'source_pixel_width': -8972678215471894991,
                                        'source_pixel_height': -785786142798560567,
                                        'rotation': -7252842729743530416,
                                        'virtual_nw_x_pixel': -370727759,
                                        'virtual_nw_y_pixel': -719218199,
                                        'virtual_width': -423291046,
                                        'virtual_height': 1316363977,
                                    },
                            {
                                        'source_monitor': 4548892,
                                        'source_nw_x_pixel': -1566519610794468500,
                                        'source_nw_y_pixel': -7399929897911464047,
                                        'source_pixel_width': -1913418120581037446,
                                        'source_pixel_height': -2961032686205563802,
                                        'rotation': -2931664690893670838,
                                        'virtual_nw_x_pixel': -411701973,
                                        'virtual_nw_y_pixel': 672828547,
                                        'virtual_width': -947128592,
                                        'virtual_height': -912245941,
                                    },
                            {
                                        'source_monitor': 7588025,
                                        'source_nw_x_pixel': -6140229155916120415,
                                        'source_nw_y_pixel': -1265955633907377193,
                                        'source_pixel_width': -2851977682008677544,
                                        'source_pixel_height': -1263120534558838758,
                                        'rotation': -5234117609905599306,
                                        'virtual_nw_x_pixel': 1191812631,
                                        'virtual_nw_y_pixel': -279766563,
                                        'virtual_width': -1549344441,
                                        'virtual_height': -1177548866,
                                    },
                            {
                                        'source_monitor': 1936534,
                                        'source_nw_x_pixel': -6007170896017455374,
                                        'source_nw_y_pixel': -3618943337100788179,
                                        'source_pixel_width': -7770671900750465598,
                                        'source_pixel_height': -205504749581607784,
                                        'rotation': -2279093309110184712,
                                        'virtual_nw_x_pixel': -1190228174,
                                        'virtual_nw_y_pixel': 56135393,
                                        'virtual_width': 1777191595,
                                        'virtual_height': -19766676,
                                    },
                            {
                                        'source_monitor': 3120893,
                                        'source_nw_x_pixel': -6365799329143231680,
                                        'source_nw_y_pixel': -439633885816946005,
                                        'source_pixel_width': -6263673548975944859,
                                        'source_pixel_height': -4333890857055562674,
                                        'rotation': -843591352905972675,
                                        'virtual_nw_x_pixel': 1760094138,
                                        'virtual_nw_y_pixel': 1928407808,
                                        'virtual_width': -1103666298,
                                        'virtual_height': 397813066,
                                    },
                            {
                                        'source_monitor': 9061265,
                                        'source_nw_x_pixel': -2915457177415415412,
                                        'source_nw_y_pixel': -2021355592323969268,
                                        'source_pixel_width': -2902105242482753112,
                                        'source_pixel_height': -9187399829378773778,
                                        'rotation': -8113374588936695690,
                                        'virtual_nw_x_pixel': 856712859,
                                        'virtual_nw_y_pixel': -658570636,
                                        'virtual_width': 651468277,
                                        'virtual_height': 1264034994,
                                    },
                            {
                                        'source_monitor': 5351144,
                                        'source_nw_x_pixel': -8320908491844604376,
                                        'source_nw_y_pixel': -8268742191621320395,
                                        'source_pixel_width': -7110401129122404621,
                                        'source_pixel_height': -827572671196143401,
                                        'rotation': -5621914905141249523,
                                        'virtual_nw_x_pixel': -1272583921,
                                        'virtual_nw_y_pixel': 1318241337,
                                        'virtual_width': -345625074,
                                        'virtual_height': 1325824921,
                                    },
                        ],
                },
                {
                    'description': 'ǚңЧ҄ǒ˯úďΰńÍϠȤмǇҬ`pФϾǖЬJ\u0379Ŝг,4ˊҦ',
                    'monitors': [
                            {
                                        'identifier': 8162895,
                                        'width': -2040107953818671533,
                                        'height': 902462883300822651,
                                    },
                            {
                                        'identifier': 9057113,
                                        'width': 3130563713864097903,
                                        'height': 4921787772516995549,
                                    },
                            {
                                        'identifier': -836036,
                                        'width': -5291779390524203526,
                                        'height': -4683651538720881709,
                                    },
                            {
                                        'identifier': 4642893,
                                        'width': -5217585749026126269,
                                        'height': 7304194536988590349,
                                    },
                            {
                                        'identifier': 4835860,
                                        'width': -258744251331920223,
                                        'height': -3213347863256962026,
                                    },
                            {
                                        'identifier': 761660,
                                        'width': -5742888212303254968,
                                        'height': -6669747987001936805,
                                    },
                            {
                                        'identifier': 1425646,
                                        'width': 1047710818044130204,
                                        'height': -1226870466381608336,
                                    },
                            {
                                        'identifier': 481058,
                                        'width': -8033027331127861192,
                                        'height': 288211756382230088,
                                    },
                            {
                                        'identifier': 9319053,
                                        'width': 1213943506991682242,
                                        'height': 3324152275066845422,
                                    },
                            {
                                        'identifier': 1715243,
                                        'width': -1961492311764202938,
                                        'height': -3044798323405316856,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9458376,
                                        'source_nw_x_pixel': -1455541141383812668,
                                        'source_nw_y_pixel': -7514082724852518119,
                                        'source_pixel_width': -5491319989614897555,
                                        'source_pixel_height': -7866310784515677538,
                                        'rotation': -4568203386900250631,
                                        'virtual_nw_x_pixel': -149237682,
                                        'virtual_nw_y_pixel': 1878106228,
                                        'virtual_width': 1467090067,
                                        'virtual_height': 1400481418,
                                    },
                            {
                                        'source_monitor': 4563634,
                                        'source_nw_x_pixel': -429491012100800347,
                                        'source_nw_y_pixel': -3644431738300668829,
                                        'source_pixel_width': -7685395523642998257,
                                        'source_pixel_height': -2062297726860260695,
                                        'rotation': -7181491944250438335,
                                        'virtual_nw_x_pixel': 1925171199,
                                        'virtual_nw_y_pixel': -1118914609,
                                        'virtual_width': 1167115654,
                                        'virtual_height': 1431635157,
                                    },
                            {
                                        'source_monitor': 2422956,
                                        'source_nw_x_pixel': -4448496285009278941,
                                        'source_nw_y_pixel': -4422359829274959798,
                                        'source_pixel_width': -8060779505241763868,
                                        'source_pixel_height': -5501928387527756205,
                                        'rotation': -4682437003545465,
                                        'virtual_nw_x_pixel': -401643626,
                                        'virtual_nw_y_pixel': -1149041182,
                                        'virtual_width': 1191570959,
                                        'virtual_height': -1577390218,
                                    },
                            {
                                        'source_monitor': 6015042,
                                        'source_nw_x_pixel': -3867291596203335267,
                                        'source_nw_y_pixel': -5157506438542082361,
                                        'source_pixel_width': -6654432617964239332,
                                        'source_pixel_height': -3245822102897213997,
                                        'rotation': -4544597290601157769,
                                        'virtual_nw_x_pixel': 1854503075,
                                        'virtual_nw_y_pixel': -566577261,
                                        'virtual_width': -185448192,
                                        'virtual_height': -614476755,
                                    },
                            {
                                        'source_monitor': 9208838,
                                        'source_nw_x_pixel': -2151154248605282391,
                                        'source_nw_y_pixel': -7300061440955878820,
                                        'source_pixel_width': -7896650714289803097,
                                        'source_pixel_height': -7161430559884627684,
                                        'rotation': -7475939715945080975,
                                        'virtual_nw_x_pixel': 280840080,
                                        'virtual_nw_y_pixel': 206249849,
                                        'virtual_width': -1208693052,
                                        'virtual_height': 259118222,
                                    },
                            {
                                        'source_monitor': 870486,
                                        'source_nw_x_pixel': -3077110976581403737,
                                        'source_nw_y_pixel': -2528657421374688662,
                                        'source_pixel_width': -6576234299048205655,
                                        'source_pixel_height': -7984352440854671190,
                                        'rotation': -7028942088354201853,
                                        'virtual_nw_x_pixel': -560059525,
                                        'virtual_nw_y_pixel': -1454889502,
                                        'virtual_width': 1585566789,
                                        'virtual_height': 1133783938,
                                    },
                            {
                                        'source_monitor': 1313011,
                                        'source_nw_x_pixel': -8277488352525015012,
                                        'source_nw_y_pixel': -5170621926835246795,
                                        'source_pixel_width': -259138516309595518,
                                        'source_pixel_height': -7520771367466927807,
                                        'rotation': -8756440827071067140,
                                        'virtual_nw_x_pixel': 727432637,
                                        'virtual_nw_y_pixel': 446064058,
                                        'virtual_width': -359552461,
                                        'virtual_height': -1678362010,
                                    },
                            {
                                        'source_monitor': 4711267,
                                        'source_nw_x_pixel': -8676384811106549391,
                                        'source_nw_y_pixel': -7708207260875616083,
                                        'source_pixel_width': -3314008620264480168,
                                        'source_pixel_height': -2458894029597220057,
                                        'rotation': -5020664587106203651,
                                        'virtual_nw_x_pixel': 1496703437,
                                        'virtual_nw_y_pixel': -1463089037,
                                        'virtual_width': -1195879119,
                                        'virtual_height': 1067626740,
                                    },
                            {
                                        'source_monitor': 8495152,
                                        'source_nw_x_pixel': -6976361373432085538,
                                        'source_nw_y_pixel': -883992174431115697,
                                        'source_pixel_width': -805617052893853155,
                                        'source_pixel_height': -2959296392608068203,
                                        'rotation': -8699589025951028463,
                                        'virtual_nw_x_pixel': -1184020902,
                                        'virtual_nw_y_pixel': 239741761,
                                        'virtual_width': 375677122,
                                        'virtual_height': 1589351128,
                                    },
                            {
                                        'source_monitor': 5138898,
                                        'source_nw_x_pixel': -1731824356213026381,
                                        'source_nw_y_pixel': -5720772763971297965,
                                        'source_pixel_width': -6595758921834628902,
                                        'source_pixel_height': -8494553138308568515,
                                        'rotation': -9012961543809507962,
                                        'virtual_nw_x_pixel': -1353010867,
                                        'virtual_nw_y_pixel': 1895765096,
                                        'virtual_width': 748546998,
                                        'virtual_height': 1362469271,
                                    },
                        ],
                },
                {
                    'description': '\u0378®ĒɖZ\u0381Wʞ¸ҵʢÉůȰҜϟӛΪŁͰŢϕƈӾÕӰÔǡҶʢ',
                    'monitors': [
                            {
                                        'identifier': 1024723,
                                        'width': 7939597211003807376,
                                        'height': 807195024653053504,
                                    },
                            {
                                        'identifier': 1452257,
                                        'width': -3562686904946361213,
                                        'height': 6543427645668135196,
                                    },
                            {
                                        'identifier': 6107376,
                                        'width': -7652287375647584989,
                                        'height': 1284023131877010236,
                                    },
                            {
                                        'identifier': 5683787,
                                        'width': 2900055557157685344,
                                        'height': -1279704058696441145,
                                    },
                            {
                                        'identifier': 3938137,
                                        'width': -8160282075861222932,
                                        'height': -6082850555814141909,
                                    },
                            {
                                        'identifier': 9444667,
                                        'width': -6658908392659205504,
                                        'height': 7579846556795401147,
                                    },
                            {
                                        'identifier': 1275744,
                                        'width': -3899577888098470208,
                                        'height': 8243339325457316043,
                                    },
                            {
                                        'identifier': 209255,
                                        'width': -6048992796554895121,
                                        'height': -9025151644732765944,
                                    },
                            {
                                        'identifier': -822497,
                                        'width': 3683947220902415874,
                                        'height': 1165818746900985338,
                                    },
                            {
                                        'identifier': 165,
                                        'width': -7839669946606456723,
                                        'height': 4435266178752487971,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6382730,
                                        'source_nw_x_pixel': -4268602101890128132,
                                        'source_nw_y_pixel': -891668132754904244,
                                        'source_pixel_width': -6389252085996934205,
                                        'source_pixel_height': -5130094966927882422,
                                        'rotation': -1876478057433428308,
                                        'virtual_nw_x_pixel': 1157323812,
                                        'virtual_nw_y_pixel': 186232096,
                                        'virtual_width': -327855990,
                                        'virtual_height': 1596335258,
                                    },
                            {
                                        'source_monitor': 7877837,
                                        'source_nw_x_pixel': -5178013621385082094,
                                        'source_nw_y_pixel': -8147321781843282622,
                                        'source_pixel_width': -3757732186839619217,
                                        'source_pixel_height': -5733609652310200601,
                                        'rotation': -3002476253145006287,
                                        'virtual_nw_x_pixel': -1865589667,
                                        'virtual_nw_y_pixel': 258559227,
                                        'virtual_width': -1513409644,
                                        'virtual_height': -1835628493,
                                    },
                            {
                                        'source_monitor': 6393347,
                                        'source_nw_x_pixel': -4734881835203864675,
                                        'source_nw_y_pixel': -8234212339856539708,
                                        'source_pixel_width': -3902835606535359678,
                                        'source_pixel_height': -4488906326691769841,
                                        'rotation': -7261204958658974116,
                                        'virtual_nw_x_pixel': 1056753777,
                                        'virtual_nw_y_pixel': -526206830,
                                        'virtual_width': 340822470,
                                        'virtual_height': 1762528270,
                                    },
                            {
                                        'source_monitor': 3934796,
                                        'source_nw_x_pixel': -4380907191825730081,
                                        'source_nw_y_pixel': -4784323094338159635,
                                        'source_pixel_width': -1802582793264823290,
                                        'source_pixel_height': -3036822617076229465,
                                        'rotation': -8528786839079389017,
                                        'virtual_nw_x_pixel': -1117273146,
                                        'virtual_nw_y_pixel': -1127098670,
                                        'virtual_width': -642678796,
                                        'virtual_height': 1996641288,
                                    },
                            {
                                        'source_monitor': 3317545,
                                        'source_nw_x_pixel': -1525547203713150440,
                                        'source_nw_y_pixel': -7051622388409636456,
                                        'source_pixel_width': -2971327825650376777,
                                        'source_pixel_height': -6966659821808062952,
                                        'rotation': -3378684223917157320,
                                        'virtual_nw_x_pixel': 1747632926,
                                        'virtual_nw_y_pixel': -1445234367,
                                        'virtual_width': -1245699790,
                                        'virtual_height': -1036573602,
                                    },
                            {
                                        'source_monitor': 1887513,
                                        'source_nw_x_pixel': -3546936888593478471,
                                        'source_nw_y_pixel': -3022536836487308186,
                                        'source_pixel_width': -6526615885064610115,
                                        'source_pixel_height': -2798103890560592220,
                                        'rotation': -656778438912441632,
                                        'virtual_nw_x_pixel': -558287170,
                                        'virtual_nw_y_pixel': 1648482706,
                                        'virtual_width': 1782954839,
                                        'virtual_height': -1382119215,
                                    },
                            {
                                        'source_monitor': 3813946,
                                        'source_nw_x_pixel': -3529351249415671135,
                                        'source_nw_y_pixel': -8044066221380739337,
                                        'source_pixel_width': -2219306381594910973,
                                        'source_pixel_height': -2270922918870465675,
                                        'rotation': -3252965648883495322,
                                        'virtual_nw_x_pixel': 879526655,
                                        'virtual_nw_y_pixel': -781462022,
                                        'virtual_width': 1938985427,
                                        'virtual_height': 184939418,
                                    },
                            {
                                        'source_monitor': 5562898,
                                        'source_nw_x_pixel': -9114302352681848856,
                                        'source_nw_y_pixel': -3518198863552197007,
                                        'source_pixel_width': -4391470085045934694,
                                        'source_pixel_height': -3903087892168680048,
                                        'rotation': -6561974279341202865,
                                        'virtual_nw_x_pixel': -286392613,
                                        'virtual_nw_y_pixel': -1634560292,
                                        'virtual_width': 602909609,
                                        'virtual_height': -1550110200,
                                    },
                            {
                                        'source_monitor': 9350518,
                                        'source_nw_x_pixel': -6790232716346546540,
                                        'source_nw_y_pixel': -7190767372791957631,
                                        'source_pixel_width': -7149089959053924515,
                                        'source_pixel_height': -243911129282503146,
                                        'rotation': -2004036218387766459,
                                        'virtual_nw_x_pixel': 1878075495,
                                        'virtual_nw_y_pixel': 591034039,
                                        'virtual_width': 339209516,
                                        'virtual_height': -1178361645,
                                    },
                            {
                                        'source_monitor': 3185000,
                                        'source_nw_x_pixel': -3656005628444075104,
                                        'source_nw_y_pixel': -6437371101452180251,
                                        'source_pixel_width': -3329131768651518112,
                                        'source_pixel_height': -1969825218649843522,
                                        'rotation': -6399220353277702750,
                                        'virtual_nw_x_pixel': 1836934451,
                                        'virtual_nw_y_pixel': 1027918551,
                                        'virtual_width': -337188498,
                                        'virtual_height': 1995471338,
                                    },
                        ],
                },
                {
                    'description': 'ʙԃЀǩŤɍԓɷȺ#λXнȢɻ\x91ǍԙӸϔͲхŲ\\ҊŐň˧ƫǙ',
                    'monitors': [
                            {
                                        'identifier': 1799992,
                                        'width': -8020671840760751363,
                                        'height': 1496322463440288472,
                                    },
                            {
                                        'identifier': 8851032,
                                        'width': -3707244999516557454,
                                        'height': -4549719630978160504,
                                    },
                            {
                                        'identifier': 9479244,
                                        'width': 3264085265587623480,
                                        'height': -3697815430874514100,
                                    },
                            {
                                        'identifier': 7024181,
                                        'width': -6201427953765075685,
                                        'height': 354623804895191766,
                                    },
                            {
                                        'identifier': 6537569,
                                        'width': -3984853000710175586,
                                        'height': 8066710117015028818,
                                    },
                            {
                                        'identifier': 3441902,
                                        'width': 2401706890732776258,
                                        'height': -5970442316136416875,
                                    },
                            {
                                        'identifier': 9809575,
                                        'width': 272972832179504731,
                                        'height': -6328257261631637641,
                                    },
                            {
                                        'identifier': 8779108,
                                        'width': 7820514245797764967,
                                        'height': -7715317129420435816,
                                    },
                            {
                                        'identifier': 208943,
                                        'width': -1697498413361772953,
                                        'height': -9104285452170952612,
                                    },
                            {
                                        'identifier': 6207245,
                                        'width': 8859636893201686104,
                                        'height': -2316681431354898838,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -524857,
                                        'source_nw_x_pixel': -704088638144687069,
                                        'source_nw_y_pixel': -919770748905204546,
                                        'source_pixel_width': -8297572099825264145,
                                        'source_pixel_height': -8748268212053204834,
                                        'rotation': -1309864883393569804,
                                        'virtual_nw_x_pixel': -782757530,
                                        'virtual_nw_y_pixel': 1218343079,
                                        'virtual_width': -1192191942,
                                        'virtual_height': 173190873,
                                    },
                            {
                                        'source_monitor': 3426509,
                                        'source_nw_x_pixel': -4343922213810237991,
                                        'source_nw_y_pixel': -7010680955854171036,
                                        'source_pixel_width': -3966497327397778990,
                                        'source_pixel_height': -1394286375849404313,
                                        'rotation': -2928853544503767755,
                                        'virtual_nw_x_pixel': -315831812,
                                        'virtual_nw_y_pixel': 319963198,
                                        'virtual_width': -1903092296,
                                        'virtual_height': -1076128941,
                                    },
                            {
                                        'source_monitor': 9286220,
                                        'source_nw_x_pixel': -2551023172546929914,
                                        'source_nw_y_pixel': -3698301649451479323,
                                        'source_pixel_width': -7030150571616048459,
                                        'source_pixel_height': -1555979841065656932,
                                        'rotation': -3686769978783224255,
                                        'virtual_nw_x_pixel': -491879370,
                                        'virtual_nw_y_pixel': -566898710,
                                        'virtual_width': 1984423386,
                                        'virtual_height': -624546022,
                                    },
                            {
                                        'source_monitor': 6269791,
                                        'source_nw_x_pixel': -975208492408965830,
                                        'source_nw_y_pixel': -8392210693037539820,
                                        'source_pixel_width': -3648938743629135210,
                                        'source_pixel_height': -8275159662477952150,
                                        'rotation': -9045935092394685055,
                                        'virtual_nw_x_pixel': 1665253230,
                                        'virtual_nw_y_pixel': -1544296419,
                                        'virtual_width': -1548509331,
                                        'virtual_height': -1984140118,
                                    },
                            {
                                        'source_monitor': 1802510,
                                        'source_nw_x_pixel': -4737269989326553580,
                                        'source_nw_y_pixel': -3238914030957586782,
                                        'source_pixel_width': -2684438893326793910,
                                        'source_pixel_height': -8780056541113432996,
                                        'rotation': -6822601832556768043,
                                        'virtual_nw_x_pixel': 1301310491,
                                        'virtual_nw_y_pixel': -69121794,
                                        'virtual_width': -661538780,
                                        'virtual_height': 1568501917,
                                    },
                            {
                                        'source_monitor': 1244909,
                                        'source_nw_x_pixel': -2956579970768361836,
                                        'source_nw_y_pixel': -2437692141853213222,
                                        'source_pixel_width': -3542228747356751242,
                                        'source_pixel_height': -2054648360016318991,
                                        'rotation': -5626480295591119993,
                                        'virtual_nw_x_pixel': 1465908536,
                                        'virtual_nw_y_pixel': -243034460,
                                        'virtual_width': 579640891,
                                        'virtual_height': 741780452,
                                    },
                            {
                                        'source_monitor': 1182786,
                                        'source_nw_x_pixel': -5349044005726607923,
                                        'source_nw_y_pixel': -6797282213914087976,
                                        'source_pixel_width': -6690347024974622721,
                                        'source_pixel_height': -3948460832687978709,
                                        'rotation': -2373046187962574339,
                                        'virtual_nw_x_pixel': 743673557,
                                        'virtual_nw_y_pixel': 1642079381,
                                        'virtual_width': -241799164,
                                        'virtual_height': -1045160795,
                                    },
                            {
                                        'source_monitor': 3003023,
                                        'source_nw_x_pixel': -576667969055867620,
                                        'source_nw_y_pixel': -6113174095537427441,
                                        'source_pixel_width': -4589325452313030665,
                                        'source_pixel_height': -913293674061402985,
                                        'rotation': -334302120604709836,
                                        'virtual_nw_x_pixel': 1214780959,
                                        'virtual_nw_y_pixel': -833789031,
                                        'virtual_width': -1660695315,
                                        'virtual_height': 1770710290,
                                    },
                            {
                                        'source_monitor': 9872998,
                                        'source_nw_x_pixel': -5483471472351068072,
                                        'source_nw_y_pixel': -5452023107872438595,
                                        'source_pixel_width': -6654593380950406867,
                                        'source_pixel_height': -1166839818225128314,
                                        'rotation': -8407725667730607842,
                                        'virtual_nw_x_pixel': -792173148,
                                        'virtual_nw_y_pixel': -1107986833,
                                        'virtual_width': -1011637749,
                                        'virtual_height': -966501307,
                                    },
                            {
                                        'source_monitor': 3675903,
                                        'source_nw_x_pixel': -1080670782351667584,
                                        'source_nw_y_pixel': -7127670811494321030,
                                        'source_pixel_width': -2907489047953506908,
                                        'source_pixel_height': -7571845572019904461,
                                        'rotation': -1453411316521735772,
                                        'virtual_nw_x_pixel': 1385884275,
                                        'virtual_nw_y_pixel': 1872748747,
                                        'virtual_width': -881628599,
                                        'virtual_height': -308322684,
                                    },
                        ],
                },
                {
                    'description': 'ȑÃTˑς˵ɑȸƦɮŁÃ8ԕ˩ѰȘӫˀѕӝİόˊҭ\x80ħʺƚʪ',
                    'monitors': [
                            {
                                        'identifier': 623221,
                                        'width': -5782079508538728909,
                                        'height': 403853626863701838,
                                    },
                            {
                                        'identifier': 7093455,
                                        'width': 2108517924584630277,
                                        'height': -1114069711849496719,
                                    },
                            {
                                        'identifier': 7088742,
                                        'width': 2153069694030784652,
                                        'height': -7311200647791789827,
                                    },
                            {
                                        'identifier': 3143293,
                                        'width': 158398522905408818,
                                        'height': 1983189915689737266,
                                    },
                            {
                                        'identifier': 4366431,
                                        'width': 6410866552786197312,
                                        'height': 7365470214729865442,
                                    },
                            {
                                        'identifier': 8863102,
                                        'width': -9194664964177127603,
                                        'height': 8301636972715019271,
                                    },
                            {
                                        'identifier': -398402,
                                        'width': 2352237480715963505,
                                        'height': -2410383010420332921,
                                    },
                            {
                                        'identifier': 5675965,
                                        'width': -2306563039427584310,
                                        'height': 1122527132006011765,
                                    },
                            {
                                        'identifier': 6397955,
                                        'width': 1993443786695081566,
                                        'height': 1575927141096675583,
                                    },
                            {
                                        'identifier': 4634200,
                                        'width': 1177093763328329958,
                                        'height': 4956668265589595068,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6695945,
                                        'source_nw_x_pixel': -3627816823504357712,
                                        'source_nw_y_pixel': -5218899045100220705,
                                        'source_pixel_width': -9035778821416197675,
                                        'source_pixel_height': -1976680410700472556,
                                        'rotation': -4888178951923610849,
                                        'virtual_nw_x_pixel': 747129493,
                                        'virtual_nw_y_pixel': -61162426,
                                        'virtual_width': -1730287533,
                                        'virtual_height': -1692702999,
                                    },
                            {
                                        'source_monitor': 1502977,
                                        'source_nw_x_pixel': -7571287271406583219,
                                        'source_nw_y_pixel': -6390325154588217013,
                                        'source_pixel_width': -6845471860010946714,
                                        'source_pixel_height': -2531314369068655681,
                                        'rotation': -3077528061319037988,
                                        'virtual_nw_x_pixel': -588245010,
                                        'virtual_nw_y_pixel': -551857861,
                                        'virtual_width': -619215844,
                                        'virtual_height': 1593744772,
                                    },
                            {
                                        'source_monitor': 1254045,
                                        'source_nw_x_pixel': -2730341653504359022,
                                        'source_nw_y_pixel': -9101275230279275418,
                                        'source_pixel_width': -6097666855620122114,
                                        'source_pixel_height': -8474196644183707730,
                                        'rotation': -8868037257554292425,
                                        'virtual_nw_x_pixel': -1937323658,
                                        'virtual_nw_y_pixel': -989264268,
                                        'virtual_width': -700362379,
                                        'virtual_height': -1574463511,
                                    },
                            {
                                        'source_monitor': 1117500,
                                        'source_nw_x_pixel': -6235722820726513023,
                                        'source_nw_y_pixel': -6079992538959259936,
                                        'source_pixel_width': -626940590816805184,
                                        'source_pixel_height': -6440426539332519838,
                                        'rotation': -2555154172583189767,
                                        'virtual_nw_x_pixel': -86079115,
                                        'virtual_nw_y_pixel': -961344798,
                                        'virtual_width': -1709424680,
                                        'virtual_height': -903315844,
                                    },
                            {
                                        'source_monitor': -809473,
                                        'source_nw_x_pixel': -5318105791407382018,
                                        'source_nw_y_pixel': -8632116709038074649,
                                        'source_pixel_width': -6998470366998133185,
                                        'source_pixel_height': -4184967087368461394,
                                        'rotation': -7975423289416109131,
                                        'virtual_nw_x_pixel': 457218127,
                                        'virtual_nw_y_pixel': -301883282,
                                        'virtual_width': -381683261,
                                        'virtual_height': -1060484093,
                                    },
                            {
                                        'source_monitor': 1033673,
                                        'source_nw_x_pixel': -7145334758323972030,
                                        'source_nw_y_pixel': -6097464904819602796,
                                        'source_pixel_width': -2250297044201235162,
                                        'source_pixel_height': -5176458677281264839,
                                        'rotation': -6914033960957551376,
                                        'virtual_nw_x_pixel': -848993360,
                                        'virtual_nw_y_pixel': -1158019981,
                                        'virtual_width': -162168519,
                                        'virtual_height': 1233116991,
                                    },
                            {
                                        'source_monitor': 3681558,
                                        'source_nw_x_pixel': -815757160817608535,
                                        'source_nw_y_pixel': -1480133877432665989,
                                        'source_pixel_width': -1374432368997478598,
                                        'source_pixel_height': -32604676891255524,
                                        'rotation': -198042304340621669,
                                        'virtual_nw_x_pixel': -830477762,
                                        'virtual_nw_y_pixel': -1766382369,
                                        'virtual_width': -860162393,
                                        'virtual_height': -70150124,
                                    },
                            {
                                        'source_monitor': 1003945,
                                        'source_nw_x_pixel': -6393210843270482796,
                                        'source_nw_y_pixel': -7779582156272357397,
                                        'source_pixel_width': -4625032618932257160,
                                        'source_pixel_height': -8327019666019673494,
                                        'rotation': -8587202695874224964,
                                        'virtual_nw_x_pixel': 381236546,
                                        'virtual_nw_y_pixel': 1968866087,
                                        'virtual_width': -1345485047,
                                        'virtual_height': 235628283,
                                    },
                            {
                                        'source_monitor': 2198895,
                                        'source_nw_x_pixel': -7093709614857155622,
                                        'source_nw_y_pixel': -3255061911459376602,
                                        'source_pixel_width': -3320335451575540151,
                                        'source_pixel_height': -1638946747838716896,
                                        'rotation': -4941304358291008842,
                                        'virtual_nw_x_pixel': -716728261,
                                        'virtual_nw_y_pixel': 1286695431,
                                        'virtual_width': 80972574,
                                        'virtual_height': -1883794254,
                                    },
                            {
                                        'source_monitor': 4214134,
                                        'source_nw_x_pixel': -3122394679327547647,
                                        'source_nw_y_pixel': -3032277314967078688,
                                        'source_pixel_width': -5251346198597738456,
                                        'source_pixel_height': -6599380348816889014,
                                        'rotation': -4483121334257823954,
                                        'virtual_nw_x_pixel': -1664247248,
                                        'virtual_nw_y_pixel': 182648818,
                                        'virtual_width': -264282111,
                                        'virtual_height': 1878219685,
                                    },
                        ],
                },
                {
                    'description': 'ȻО-ɮ҆ҁǮêĖѸͺʤƨ˲ɪŔ¹ǝЎƀʊѧԀȟƤԭːˉōá',
                    'monitors': [
                            {
                                        'identifier': 714349,
                                        'width': 229510538136647640,
                                        'height': -5768323276482793796,
                                    },
                            {
                                        'identifier': 2767990,
                                        'width': 1614126068693999246,
                                        'height': 6752417447995503601,
                                    },
                            {
                                        'identifier': -935506,
                                        'width': 5764187059578117772,
                                        'height': -7812000575327268306,
                                    },
                            {
                                        'identifier': 2654797,
                                        'width': -5564962123909507635,
                                        'height': -2561134993538632070,
                                    },
                            {
                                        'identifier': 6757443,
                                        'width': 6864438895028026101,
                                        'height': 6128103970128170151,
                                    },
                            {
                                        'identifier': 2040066,
                                        'width': 5330666079425197891,
                                        'height': -5829355266101667463,
                                    },
                            {
                                        'identifier': 15666,
                                        'width': 7483282513741929003,
                                        'height': 4138771456895755622,
                                    },
                            {
                                        'identifier': 7924251,
                                        'width': -4308386448890449321,
                                        'height': 6244678192449363860,
                                    },
                            {
                                        'identifier': 7934370,
                                        'width': 3881509058028899881,
                                        'height': 1872354398900851252,
                                    },
                            {
                                        'identifier': 1077259,
                                        'width': -1927560377368110073,
                                        'height': -7957231877391095193,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5486511,
                                        'source_nw_x_pixel': -8759801988278026346,
                                        'source_nw_y_pixel': -7903428557419733263,
                                        'source_pixel_width': -7666088637257987005,
                                        'source_pixel_height': -715302447133171076,
                                        'rotation': -1157389020733172284,
                                        'virtual_nw_x_pixel': -122456280,
                                        'virtual_nw_y_pixel': -1128385355,
                                        'virtual_width': 22682112,
                                        'virtual_height': 976180532,
                                    },
                            {
                                        'source_monitor': -943497,
                                        'source_nw_x_pixel': -7934478200258829127,
                                        'source_nw_y_pixel': -6022320962661347596,
                                        'source_pixel_width': -9219735822495249684,
                                        'source_pixel_height': -7918419954235669169,
                                        'rotation': -4072772018851502731,
                                        'virtual_nw_x_pixel': -21688636,
                                        'virtual_nw_y_pixel': 820980039,
                                        'virtual_width': -1108456790,
                                        'virtual_height': 1747165840,
                                    },
                            {
                                        'source_monitor': 2967617,
                                        'source_nw_x_pixel': -139372523884517064,
                                        'source_nw_y_pixel': -375805460760350647,
                                        'source_pixel_width': -4152593077188118864,
                                        'source_pixel_height': -2493329648378713297,
                                        'rotation': -3946216715706474648,
                                        'virtual_nw_x_pixel': -1709700333,
                                        'virtual_nw_y_pixel': 1096232201,
                                        'virtual_width': 233872201,
                                        'virtual_height': -93282723,
                                    },
                            {
                                        'source_monitor': 6662514,
                                        'source_nw_x_pixel': -4847877160214902285,
                                        'source_nw_y_pixel': -4663601603820701835,
                                        'source_pixel_width': -3015133261038956935,
                                        'source_pixel_height': -5057682936536441208,
                                        'rotation': -1968308045145301727,
                                        'virtual_nw_x_pixel': -830749480,
                                        'virtual_nw_y_pixel': 1690303618,
                                        'virtual_width': -1094907135,
                                        'virtual_height': 413789099,
                                    },
                            {
                                        'source_monitor': 208529,
                                        'source_nw_x_pixel': -7470497662479719854,
                                        'source_nw_y_pixel': -7478795066550753510,
                                        'source_pixel_width': -9165551086840020159,
                                        'source_pixel_height': -4785308077566917591,
                                        'rotation': -2037058504062884132,
                                        'virtual_nw_x_pixel': -1389014254,
                                        'virtual_nw_y_pixel': -1046103219,
                                        'virtual_width': 562086404,
                                        'virtual_height': 393956159,
                                    },
                            {
                                        'source_monitor': 2608145,
                                        'source_nw_x_pixel': -6698017529454773030,
                                        'source_nw_y_pixel': -7132746444039503674,
                                        'source_pixel_width': -8510746119965114311,
                                        'source_pixel_height': -3391117005779698018,
                                        'rotation': -4125187963043615805,
                                        'virtual_nw_x_pixel': -1309694123,
                                        'virtual_nw_y_pixel': -528979374,
                                        'virtual_width': 1321416727,
                                        'virtual_height': 694090924,
                                    },
                            {
                                        'source_monitor': 3316618,
                                        'source_nw_x_pixel': -4545858522391802008,
                                        'source_nw_y_pixel': -5137089372839232445,
                                        'source_pixel_width': -3257543725056603108,
                                        'source_pixel_height': -2011091032027138342,
                                        'rotation': -1973755138302564859,
                                        'virtual_nw_x_pixel': -735007219,
                                        'virtual_nw_y_pixel': -16248894,
                                        'virtual_width': 839619000,
                                        'virtual_height': 1369579460,
                                    },
                            {
                                        'source_monitor': 7161611,
                                        'source_nw_x_pixel': -574095684998029621,
                                        'source_nw_y_pixel': -7708682633189045633,
                                        'source_pixel_width': -6995898489643891630,
                                        'source_pixel_height': -6532714664611441087,
                                        'rotation': -4903754896379686349,
                                        'virtual_nw_x_pixel': 1650553681,
                                        'virtual_nw_y_pixel': -1335338090,
                                        'virtual_width': -605512183,
                                        'virtual_height': 1620926485,
                                    },
                            {
                                        'source_monitor': 8218070,
                                        'source_nw_x_pixel': -1258208671052472411,
                                        'source_nw_y_pixel': -3629046859426489177,
                                        'source_pixel_width': -6555310269847134988,
                                        'source_pixel_height': -7578521036588770717,
                                        'rotation': -6668827077389244770,
                                        'virtual_nw_x_pixel': -1046349452,
                                        'virtual_nw_y_pixel': -1498376068,
                                        'virtual_width': 1510537535,
                                        'virtual_height': 1147500818,
                                    },
                            {
                                        'source_monitor': 2984583,
                                        'source_nw_x_pixel': -4045816809177218828,
                                        'source_nw_y_pixel': -1786722084015019444,
                                        'source_pixel_width': -4678175734604709935,
                                        'source_pixel_height': -361794310531013094,
                                        'rotation': -8104560282193855286,
                                        'virtual_nw_x_pixel': 1245337792,
                                        'virtual_nw_y_pixel': 1624089588,
                                        'virtual_width': -367853302,
                                        'virtual_height': -790572353,
                                    },
                        ],
                },
                {
                    'description': 'ԇјзˬqɩѼƖЧìүȇԂƺɘǶɇĺʳќ˵śіԩӝ½ƢβԄӷ',
                    'monitors': [
                            {
                                        'identifier': 632592,
                                        'width': 2334306507936252226,
                                        'height': 1756346076212709638,
                                    },
                            {
                                        'identifier': 3902396,
                                        'width': -1412606833095433081,
                                        'height': 174441668211050784,
                                    },
                            {
                                        'identifier': 1950429,
                                        'width': -9118645611581434645,
                                        'height': -1539668153313161835,
                                    },
                            {
                                        'identifier': 9858411,
                                        'width': -5184416812370189351,
                                        'height': -4271702684450796255,
                                    },
                            {
                                        'identifier': 9329743,
                                        'width': -6529089922929600816,
                                        'height': 8105452429821956300,
                                    },
                            {
                                        'identifier': 9205965,
                                        'width': -563536851343809,
                                        'height': 7195143806800978311,
                                    },
                            {
                                        'identifier': -314899,
                                        'width': 3056769454837848006,
                                        'height': 7644165544948727430,
                                    },
                            {
                                        'identifier': 2078493,
                                        'width': 5757610824391922553,
                                        'height': -5058408027023003210,
                                    },
                            {
                                        'identifier': 3099242,
                                        'width': 6891331632574311359,
                                        'height': 845985446339157911,
                                    },
                            {
                                        'identifier': -986781,
                                        'width': -8301656606910174207,
                                        'height': 1750877514934440421,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7145448,
                                        'source_nw_x_pixel': -8252885952762875966,
                                        'source_nw_y_pixel': -4972641736384188835,
                                        'source_pixel_width': -4229421866843212138,
                                        'source_pixel_height': -4268685559809544428,
                                        'rotation': -8513618432155407790,
                                        'virtual_nw_x_pixel': 1400822631,
                                        'virtual_nw_y_pixel': -891446465,
                                        'virtual_width': -1188737578,
                                        'virtual_height': -1808432419,
                                    },
                            {
                                        'source_monitor': 3342279,
                                        'source_nw_x_pixel': -2677537428278421492,
                                        'source_nw_y_pixel': -3053756094284310088,
                                        'source_pixel_width': -555901326857112430,
                                        'source_pixel_height': -6925782161041017147,
                                        'rotation': -9126227483456148480,
                                        'virtual_nw_x_pixel': -56816569,
                                        'virtual_nw_y_pixel': 1410114252,
                                        'virtual_width': 1976313192,
                                        'virtual_height': 1587466430,
                                    },
                            {
                                        'source_monitor': 7897543,
                                        'source_nw_x_pixel': -5550201969231556132,
                                        'source_nw_y_pixel': -6035413009008547348,
                                        'source_pixel_width': -528920846110245958,
                                        'source_pixel_height': -1528611095911471883,
                                        'rotation': -9206178404247366009,
                                        'virtual_nw_x_pixel': -313892488,
                                        'virtual_nw_y_pixel': -1495507710,
                                        'virtual_width': -1484564426,
                                        'virtual_height': 1927848852,
                                    },
                            {
                                        'source_monitor': 1426325,
                                        'source_nw_x_pixel': -116895522204293328,
                                        'source_nw_y_pixel': -3855918104055121691,
                                        'source_pixel_width': -374719282166624879,
                                        'source_pixel_height': -577949606324735373,
                                        'rotation': -5232476840766178539,
                                        'virtual_nw_x_pixel': 1950779908,
                                        'virtual_nw_y_pixel': 1400182329,
                                        'virtual_width': 482681731,
                                        'virtual_height': -1887667997,
                                    },
                            {
                                        'source_monitor': 2187890,
                                        'source_nw_x_pixel': -8892819493779648015,
                                        'source_nw_y_pixel': -201501299975493701,
                                        'source_pixel_width': -982976844883313175,
                                        'source_pixel_height': -8995921947944291365,
                                        'rotation': -3857378803119213266,
                                        'virtual_nw_x_pixel': -573486571,
                                        'virtual_nw_y_pixel': 1820225622,
                                        'virtual_width': 565107524,
                                        'virtual_height': 1680848239,
                                    },
                            {
                                        'source_monitor': 2377036,
                                        'source_nw_x_pixel': -5672876965223117485,
                                        'source_nw_y_pixel': -7309951207246711039,
                                        'source_pixel_width': -8821825775850402482,
                                        'source_pixel_height': -210427962144307688,
                                        'rotation': -7057193639503604393,
                                        'virtual_nw_x_pixel': 921120713,
                                        'virtual_nw_y_pixel': 238035344,
                                        'virtual_width': 486623693,
                                        'virtual_height': -1827688516,
                                    },
                            {
                                        'source_monitor': 4484998,
                                        'source_nw_x_pixel': -6463142169469223902,
                                        'source_nw_y_pixel': -787570326113848734,
                                        'source_pixel_width': -1156540366830650501,
                                        'source_pixel_height': -3450464036833244772,
                                        'rotation': -6997584431680721184,
                                        'virtual_nw_x_pixel': 1487601193,
                                        'virtual_nw_y_pixel': -1663233802,
                                        'virtual_width': 1014401320,
                                        'virtual_height': 1105458440,
                                    },
                            {
                                        'source_monitor': 174919,
                                        'source_nw_x_pixel': -8876851240301944912,
                                        'source_nw_y_pixel': -5800973138593025786,
                                        'source_pixel_width': -9077494222479090808,
                                        'source_pixel_height': -7576371073662958322,
                                        'rotation': -7156386782578242017,
                                        'virtual_nw_x_pixel': -920505155,
                                        'virtual_nw_y_pixel': -1280850965,
                                        'virtual_width': 114977887,
                                        'virtual_height': 669888911,
                                    },
                            {
                                        'source_monitor': 4821624,
                                        'source_nw_x_pixel': -8264106018412298450,
                                        'source_nw_y_pixel': -8689369496728744933,
                                        'source_pixel_width': -4570406817392648416,
                                        'source_pixel_height': -142179968832938068,
                                        'rotation': -3012284589377239462,
                                        'virtual_nw_x_pixel': 1594624921,
                                        'virtual_nw_y_pixel': -872403608,
                                        'virtual_width': -1470310790,
                                        'virtual_height': -1055723220,
                                    },
                            {
                                        'source_monitor': 5824148,
                                        'source_nw_x_pixel': -7119103884756509588,
                                        'source_nw_y_pixel': -3613433970550078339,
                                        'source_pixel_width': -4977309279470878831,
                                        'source_pixel_height': -2920149388308438607,
                                        'rotation': -661547215608505437,
                                        'virtual_nw_x_pixel': -1685971467,
                                        'virtual_nw_y_pixel': -202218605,
                                        'virtual_width': 1529574694,
                                        'virtual_height': 1453153990,
                                    },
                        ],
                },
                {
                    'description': 'Ɲԡ½\x9dћԦѱ˨ʦ³ʬƟȽÔЉӋѦ˩ʡˆѼƾšԜ,Ғ˄\x8fԣв',
                    'monitors': [
                            {
                                        'identifier': 3576857,
                                        'width': -3027239433744180167,
                                        'height': 7961034819933406975,
                                    },
                            {
                                        'identifier': -574674,
                                        'width': -5092408090674752410,
                                        'height': -5115632711309392544,
                                    },
                            {
                                        'identifier': -761813,
                                        'width': 1132981541760996804,
                                        'height': -4713685076837144371,
                                    },
                            {
                                        'identifier': 876262,
                                        'width': 717500389860821444,
                                        'height': 8232199006502756300,
                                    },
                            {
                                        'identifier': -780202,
                                        'width': 4201342581219118940,
                                        'height': 112418614055996517,
                                    },
                            {
                                        'identifier': 2495382,
                                        'width': -6171595106188359460,
                                        'height': 2868657762376227347,
                                    },
                            {
                                        'identifier': 4958227,
                                        'width': 3690718019730086456,
                                        'height': 3869970033849600343,
                                    },
                            {
                                        'identifier': 646786,
                                        'width': 7914282111051878242,
                                        'height': 6852342031861689792,
                                    },
                            {
                                        'identifier': 9504690,
                                        'width': -1826344026064982972,
                                        'height': -5951102835987436378,
                                    },
                            {
                                        'identifier': 4998027,
                                        'width': -788436050933274124,
                                        'height': 8719137281906289459,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6687208,
                                        'source_nw_x_pixel': -4283094676706186584,
                                        'source_nw_y_pixel': -3665873230571209633,
                                        'source_pixel_width': -7476179456026377489,
                                        'source_pixel_height': -1012521747266324822,
                                        'rotation': -3384231710372531805,
                                        'virtual_nw_x_pixel': 1557127058,
                                        'virtual_nw_y_pixel': 614262982,
                                        'virtual_width': -732877837,
                                        'virtual_height': 850400387,
                                    },
                            {
                                        'source_monitor': 5927091,
                                        'source_nw_x_pixel': -2572533536031922166,
                                        'source_nw_y_pixel': -2480045960081895468,
                                        'source_pixel_width': -9191149083798630763,
                                        'source_pixel_height': -1243615980792483932,
                                        'rotation': -1454997289724176661,
                                        'virtual_nw_x_pixel': 547678570,
                                        'virtual_nw_y_pixel': 1915640831,
                                        'virtual_width': -65154517,
                                        'virtual_height': -1967020751,
                                    },
                            {
                                        'source_monitor': 58498,
                                        'source_nw_x_pixel': -421513281169686991,
                                        'source_nw_y_pixel': -517400708728554842,
                                        'source_pixel_width': -1387212990383173808,
                                        'source_pixel_height': -8117619028749640874,
                                        'rotation': -6061105327266693774,
                                        'virtual_nw_x_pixel': 269560640,
                                        'virtual_nw_y_pixel': 1225490316,
                                        'virtual_width': 1532954228,
                                        'virtual_height': 1575260942,
                                    },
                            {
                                        'source_monitor': 1204406,
                                        'source_nw_x_pixel': -1229463690437273400,
                                        'source_nw_y_pixel': -3722377760762103110,
                                        'source_pixel_width': -5838121958735148529,
                                        'source_pixel_height': -5319584149264211100,
                                        'rotation': -9055916111807681628,
                                        'virtual_nw_x_pixel': 131682737,
                                        'virtual_nw_y_pixel': -1331750939,
                                        'virtual_width': 320468277,
                                        'virtual_height': -988351343,
                                    },
                            {
                                        'source_monitor': 8111345,
                                        'source_nw_x_pixel': -1703800096467793128,
                                        'source_nw_y_pixel': -1387053936721883586,
                                        'source_pixel_width': -1685380785885552368,
                                        'source_pixel_height': -1814401731999042259,
                                        'rotation': -6842101743452937510,
                                        'virtual_nw_x_pixel': 956554224,
                                        'virtual_nw_y_pixel': -535698923,
                                        'virtual_width': -1163255006,
                                        'virtual_height': -1950030151,
                                    },
                            {
                                        'source_monitor': 9351830,
                                        'source_nw_x_pixel': -6485827032241687705,
                                        'source_nw_y_pixel': -1144765595089311776,
                                        'source_pixel_width': -8495981827325931502,
                                        'source_pixel_height': -7096106610444651522,
                                        'rotation': -6933779001458679453,
                                        'virtual_nw_x_pixel': 1033508277,
                                        'virtual_nw_y_pixel': -793717724,
                                        'virtual_width': 964132476,
                                        'virtual_height': -1082989233,
                                    },
                            {
                                        'source_monitor': 7799314,
                                        'source_nw_x_pixel': -9046603843717650827,
                                        'source_nw_y_pixel': -2291188263157419216,
                                        'source_pixel_width': -2890899939895826530,
                                        'source_pixel_height': -4397173105670859614,
                                        'rotation': -5108039693544834353,
                                        'virtual_nw_x_pixel': 773048032,
                                        'virtual_nw_y_pixel': -854106850,
                                        'virtual_width': 1216509007,
                                        'virtual_height': 470694699,
                                    },
                            {
                                        'source_monitor': 8227588,
                                        'source_nw_x_pixel': -1945058722165062123,
                                        'source_nw_y_pixel': -3150264553241388959,
                                        'source_pixel_width': -2975166809462911825,
                                        'source_pixel_height': -660611239358263873,
                                        'rotation': -5305745370154505555,
                                        'virtual_nw_x_pixel': -495991594,
                                        'virtual_nw_y_pixel': -1965052252,
                                        'virtual_width': 283652875,
                                        'virtual_height': -950200671,
                                    },
                            {
                                        'source_monitor': 1535658,
                                        'source_nw_x_pixel': -5274697463643854519,
                                        'source_nw_y_pixel': -1199938606797557644,
                                        'source_pixel_width': -7335108650977733677,
                                        'source_pixel_height': -8480779542340059017,
                                        'rotation': -981783560319979357,
                                        'virtual_nw_x_pixel': -1520907091,
                                        'virtual_nw_y_pixel': 135960843,
                                        'virtual_width': 1565672739,
                                        'virtual_height': 420742341,
                                    },
                            {
                                        'source_monitor': 657757,
                                        'source_nw_x_pixel': -2995108539819937827,
                                        'source_nw_y_pixel': -5140404957912851336,
                                        'source_pixel_width': -4425900425002865813,
                                        'source_pixel_height': -2146764554587828507,
                                        'rotation': -7581103973506984870,
                                        'virtual_nw_x_pixel': 6112647,
                                        'virtual_nw_y_pixel': 1923561137,
                                        'virtual_width': 997613577,
                                        'virtual_height': -52098387,
                                    },
                        ],
                },
                {
                    'description': 'ďϹӺžҿ\x93˥ĞũΗ3ТpȀAɼ\x84ѷȊĊːȯōмpşԫˆ.ɸ',
                    'monitors': [
                            {
                                        'identifier': 2089639,
                                        'width': -7100205507672942293,
                                        'height': -4752689606300895798,
                                    },
                            {
                                        'identifier': 6995564,
                                        'width': -7084165444283346054,
                                        'height': -1391745106216678109,
                                    },
                            {
                                        'identifier': 4912681,
                                        'width': -8818992806261814521,
                                        'height': -1861436173033295830,
                                    },
                            {
                                        'identifier': -389695,
                                        'width': -1832453826391849293,
                                        'height': -8169941942941718758,
                                    },
                            {
                                        'identifier': 924315,
                                        'width': -2182171525896962980,
                                        'height': 1457283176827282717,
                                    },
                            {
                                        'identifier': 7123899,
                                        'width': 8560683418453449420,
                                        'height': -7375618656590851517,
                                    },
                            {
                                        'identifier': 6282379,
                                        'width': 4221833161415746444,
                                        'height': 286682180791299834,
                                    },
                            {
                                        'identifier': 7124163,
                                        'width': -4518530915925853281,
                                        'height': 7436389083097490001,
                                    },
                            {
                                        'identifier': 6841559,
                                        'width': -332135269383338275,
                                        'height': 5161335836774990823,
                                    },
                            {
                                        'identifier': 1894957,
                                        'width': 6389051931972504800,
                                        'height': -417133662821992543,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6823074,
                                        'source_nw_x_pixel': -6504118063897640071,
                                        'source_nw_y_pixel': -5066286432519606177,
                                        'source_pixel_width': -4807956068425590131,
                                        'source_pixel_height': -1221132665455047061,
                                        'rotation': -327200676467334477,
                                        'virtual_nw_x_pixel': -26770489,
                                        'virtual_nw_y_pixel': -529556239,
                                        'virtual_width': 804909648,
                                        'virtual_height': 675245815,
                                    },
                            {
                                        'source_monitor': 9574020,
                                        'source_nw_x_pixel': -370546573103953860,
                                        'source_nw_y_pixel': -2156754767784209957,
                                        'source_pixel_width': -5039552684217406171,
                                        'source_pixel_height': -594871765672373225,
                                        'rotation': -8412170686675646227,
                                        'virtual_nw_x_pixel': 111449095,
                                        'virtual_nw_y_pixel': -1711354651,
                                        'virtual_width': 774989290,
                                        'virtual_height': 1956972320,
                                    },
                            {
                                        'source_monitor': 544883,
                                        'source_nw_x_pixel': -9081378455068071037,
                                        'source_nw_y_pixel': -5767039474791800321,
                                        'source_pixel_width': -9146586687085712620,
                                        'source_pixel_height': -7667561915031965321,
                                        'rotation': -8551947574655517348,
                                        'virtual_nw_x_pixel': -1018097883,
                                        'virtual_nw_y_pixel': 1935798378,
                                        'virtual_width': -40562378,
                                        'virtual_height': -1831555251,
                                    },
                            {
                                        'source_monitor': -694732,
                                        'source_nw_x_pixel': -317723511778019138,
                                        'source_nw_y_pixel': -7931052850756556428,
                                        'source_pixel_width': -6017885559922445652,
                                        'source_pixel_height': -8889364704256515819,
                                        'rotation': -4104684004753391651,
                                        'virtual_nw_x_pixel': -1499330578,
                                        'virtual_nw_y_pixel': 418345919,
                                        'virtual_width': -1797390127,
                                        'virtual_height': 654834853,
                                    },
                            {
                                        'source_monitor': 4127131,
                                        'source_nw_x_pixel': -248881186315606506,
                                        'source_nw_y_pixel': -670716888973815605,
                                        'source_pixel_width': -6506023366662312766,
                                        'source_pixel_height': -64882067786294423,
                                        'rotation': -7832051940638230367,
                                        'virtual_nw_x_pixel': -1546278010,
                                        'virtual_nw_y_pixel': 379296720,
                                        'virtual_width': 39795744,
                                        'virtual_height': -668778087,
                                    },
                            {
                                        'source_monitor': 2468790,
                                        'source_nw_x_pixel': -1534293979245838624,
                                        'source_nw_y_pixel': -9165279943475669553,
                                        'source_pixel_width': -5259702916076572422,
                                        'source_pixel_height': -6216702233535987953,
                                        'rotation': -4961957078038848514,
                                        'virtual_nw_x_pixel': -671910085,
                                        'virtual_nw_y_pixel': -391369190,
                                        'virtual_width': 1457549643,
                                        'virtual_height': -1208893777,
                                    },
                            {
                                        'source_monitor': 4343792,
                                        'source_nw_x_pixel': -6157881018867394845,
                                        'source_nw_y_pixel': -3500887608546059314,
                                        'source_pixel_width': -3340661237077407467,
                                        'source_pixel_height': -6104742791499710429,
                                        'rotation': -1389206656483305251,
                                        'virtual_nw_x_pixel': 1330731291,
                                        'virtual_nw_y_pixel': -1920691612,
                                        'virtual_width': -760744906,
                                        'virtual_height': -343593654,
                                    },
                            {
                                        'source_monitor': 8550292,
                                        'source_nw_x_pixel': -977212283849021954,
                                        'source_nw_y_pixel': -2434716228791487785,
                                        'source_pixel_width': -7463456891473155688,
                                        'source_pixel_height': -1277358735384649089,
                                        'rotation': -7178545317250178928,
                                        'virtual_nw_x_pixel': 441709361,
                                        'virtual_nw_y_pixel': 565614059,
                                        'virtual_width': 423539563,
                                        'virtual_height': -27755248,
                                    },
                            {
                                        'source_monitor': 5518397,
                                        'source_nw_x_pixel': -6028857561405110007,
                                        'source_nw_y_pixel': -1589368593868982716,
                                        'source_pixel_width': -7034236757187697609,
                                        'source_pixel_height': -3254444079271723769,
                                        'rotation': -8580267865594354915,
                                        'virtual_nw_x_pixel': 1199281325,
                                        'virtual_nw_y_pixel': -797701897,
                                        'virtual_width': -52199513,
                                        'virtual_height': -1731216206,
                                    },
                            {
                                        'source_monitor': 5284631,
                                        'source_nw_x_pixel': -4509483785630953951,
                                        'source_nw_y_pixel': -6240877887789928358,
                                        'source_pixel_width': -2375611874366639294,
                                        'source_pixel_height': -7238805318375342141,
                                        'rotation': -1889353918469719772,
                                        'virtual_nw_x_pixel': -564956647,
                                        'virtual_nw_y_pixel': 460283125,
                                        'virtual_width': 1555396654,
                                        'virtual_height': 744779026,
                                    },
                        ],
                },
                {
                    'description': 'ϲYԍѤń*Ʒ\\ˠ\x84Ǵʓ,ѦȋβɋɟҸѝƥƱǐſįǈǱԡʢʰ',
                    'monitors': [
                            {
                                        'identifier': 2853163,
                                        'width': 5981320978647843153,
                                        'height': 1446210914299176705,
                                    },
                            {
                                        'identifier': 9237409,
                                        'width': -4549986375891616614,
                                        'height': 6897741989394778889,
                                    },
                            {
                                        'identifier': 4011741,
                                        'width': 1064171646549495844,
                                        'height': -5968681808424223021,
                                    },
                            {
                                        'identifier': 4958459,
                                        'width': -9119868186850023361,
                                        'height': -6446552044659319702,
                                    },
                            {
                                        'identifier': 679791,
                                        'width': 4106201564535450573,
                                        'height': -6149165307641501769,
                                    },
                            {
                                        'identifier': 8713762,
                                        'width': 2273673583923981042,
                                        'height': -1995635756609297427,
                                    },
                            {
                                        'identifier': 1258212,
                                        'width': 3285552229351933952,
                                        'height': 6952646668783512586,
                                    },
                            {
                                        'identifier': 1192182,
                                        'width': 6243695216785233276,
                                        'height': -713206437971003103,
                                    },
                            {
                                        'identifier': 4462056,
                                        'width': -2980087084234719463,
                                        'height': -6670751184619237653,
                                    },
                            {
                                        'identifier': 8833248,
                                        'width': 5373456138556435567,
                                        'height': 3735796547803680586,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5910597,
                                        'source_nw_x_pixel': -9079121769557410736,
                                        'source_nw_y_pixel': -4381581998221934478,
                                        'source_pixel_width': -2010211925785378826,
                                        'source_pixel_height': -5161375414581489075,
                                        'rotation': -7048598743080268104,
                                        'virtual_nw_x_pixel': 338816038,
                                        'virtual_nw_y_pixel': -32834335,
                                        'virtual_width': -947283642,
                                        'virtual_height': -765868611,
                                    },
                            {
                                        'source_monitor': 1251008,
                                        'source_nw_x_pixel': -6423288878634748407,
                                        'source_nw_y_pixel': -6426907719148228330,
                                        'source_pixel_width': -8704893224592973571,
                                        'source_pixel_height': -6830254343343239886,
                                        'rotation': -7589870622919407489,
                                        'virtual_nw_x_pixel': -44208380,
                                        'virtual_nw_y_pixel': -1829703256,
                                        'virtual_width': 1005186226,
                                        'virtual_height': 993456545,
                                    },
                            {
                                        'source_monitor': 7771492,
                                        'source_nw_x_pixel': -2347883796202043998,
                                        'source_nw_y_pixel': -5599263221644956460,
                                        'source_pixel_width': -8234770649916438988,
                                        'source_pixel_height': -8439444436123421254,
                                        'rotation': -581394753077724930,
                                        'virtual_nw_x_pixel': 747933027,
                                        'virtual_nw_y_pixel': -752108081,
                                        'virtual_width': -507265609,
                                        'virtual_height': -1072195819,
                                    },
                            {
                                        'source_monitor': 1847759,
                                        'source_nw_x_pixel': -1304134041800887284,
                                        'source_nw_y_pixel': -6470563947271585702,
                                        'source_pixel_width': -5624023098122714867,
                                        'source_pixel_height': -6597908610055048049,
                                        'rotation': -3149919164266564170,
                                        'virtual_nw_x_pixel': -1273457130,
                                        'virtual_nw_y_pixel': -426356182,
                                        'virtual_width': 1704684460,
                                        'virtual_height': -816813178,
                                    },
                            {
                                        'source_monitor': 7430038,
                                        'source_nw_x_pixel': -5448270724941941853,
                                        'source_nw_y_pixel': -880425337570523138,
                                        'source_pixel_width': -8243225426357163411,
                                        'source_pixel_height': -4217817513362059341,
                                        'rotation': -4816425335837228517,
                                        'virtual_nw_x_pixel': -1994635682,
                                        'virtual_nw_y_pixel': 1825845208,
                                        'virtual_width': 1025394952,
                                        'virtual_height': -334292106,
                                    },
                            {
                                        'source_monitor': 863624,
                                        'source_nw_x_pixel': -1288960286742581725,
                                        'source_nw_y_pixel': -5747598825179913460,
                                        'source_pixel_width': -1208250468015687725,
                                        'source_pixel_height': -2638603545400615082,
                                        'rotation': -6185765058752354323,
                                        'virtual_nw_x_pixel': 679107132,
                                        'virtual_nw_y_pixel': 1984352154,
                                        'virtual_width': -1849548930,
                                        'virtual_height': 535041183,
                                    },
                            {
                                        'source_monitor': -15076,
                                        'source_nw_x_pixel': -8910724651475952597,
                                        'source_nw_y_pixel': -8541882592925456869,
                                        'source_pixel_width': -8320873520313411865,
                                        'source_pixel_height': -4537817989256574509,
                                        'rotation': -2912575648282067656,
                                        'virtual_nw_x_pixel': -1420524258,
                                        'virtual_nw_y_pixel': 56303853,
                                        'virtual_width': 1560075036,
                                        'virtual_height': 1678197171,
                                    },
                            {
                                        'source_monitor': 3972104,
                                        'source_nw_x_pixel': -455175182151908537,
                                        'source_nw_y_pixel': -838301837006826495,
                                        'source_pixel_width': -5567586203942041664,
                                        'source_pixel_height': -1388661713186893501,
                                        'rotation': -5595704384238935115,
                                        'virtual_nw_x_pixel': 1989705155,
                                        'virtual_nw_y_pixel': -314073747,
                                        'virtual_width': -1052799069,
                                        'virtual_height': -396044744,
                                    },
                            {
                                        'source_monitor': 4198595,
                                        'source_nw_x_pixel': -1494656556883447618,
                                        'source_nw_y_pixel': -3238334949795957641,
                                        'source_pixel_width': -5286372486018079180,
                                        'source_pixel_height': -4429114578006247930,
                                        'rotation': -30935666597353543,
                                        'virtual_nw_x_pixel': 1843396926,
                                        'virtual_nw_y_pixel': 545228901,
                                        'virtual_width': 636419525,
                                        'virtual_height': -917322943,
                                    },
                            {
                                        'source_monitor': 9885049,
                                        'source_nw_x_pixel': -6410290321621994564,
                                        'source_nw_y_pixel': -5707785741614514929,
                                        'source_pixel_width': -5828189431584413182,
                                        'source_pixel_height': -5447081625492287425,
                                        'rotation': -2311765205259174174,
                                        'virtual_nw_x_pixel': -337554274,
                                        'virtual_nw_y_pixel': -1695200737,
                                        'virtual_width': -904237392,
                                        'virtual_height': -1169568014,
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
                                        'identifier': 824400,
                                        'width': 1348560638174585996,
                                        'height': 2331553977647020411,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -8615003370020722995,
                                        'source_nw_y_pixel': -4214991395549330104,
                                        'source_pixel_width': -8398379405982121060,
                                        'source_pixel_height': -3960787092996077811,
                                        'rotation': -8724348776265839459,
                                        'virtual_nw_x_pixel': -939798105,
                                        'virtual_nw_y_pixel': -435727706,
                                        'virtual_width': -98931005,
                                        'virtual_height': 381934384,
                                    },
                        ],
                },
            ],

        },
    ),
]
