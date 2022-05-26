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
            'nw_x_pixel': 947876953,
            'nw_y_pixel': 139914442,
            'width': -2354063917831684510,
            'height': -864296071775813585,
            'ratio_x': -2764847202318269825,
            'ratio_y': 1761959844136250664,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 277009855,

            'nw_y_pixel': 853941709,

            'width': -7570643506218703897,

            'height': -2733898746969063668,

            'ratio_x': 6144431974089206828,

            'ratio_y': 2932740820966819621,

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
                    'nw_x_pixel': 399759685,
                    'nw_y_pixel': -620303410,
                    'width': -5132661689247643487,
                    'height': -2461665174560454979,
                    'ratio_x': 3764226843931382811,
                    'ratio_y': 3873918371374236120,
                },
                {
                    'nw_x_pixel': -1436090470,
                    'nw_y_pixel': 1410019540,
                    'width': -5090469500355679534,
                    'height': -7006191008759685787,
                    'ratio_x': -6909276051638131245,
                    'ratio_y': -5673002436609924616,
                },
                {
                    'nw_x_pixel': -1854431509,
                    'nw_y_pixel': 702113520,
                    'width': -3046839343306647186,
                    'height': -1328376776777926532,
                    'ratio_x': -8085598281612877233,
                    'ratio_y': 249331095496711008,
                },
                {
                    'nw_x_pixel': 56653044,
                    'nw_y_pixel': 603627134,
                    'width': -6850608754091938311,
                    'height': -3101847480460213310,
                    'ratio_x': 7922005543411325340,
                    'ratio_y': -1909529889070246423,
                },
                {
                    'nw_x_pixel': 364653865,
                    'nw_y_pixel': -327769959,
                    'width': -1836375939311461978,
                    'height': -9120351797990099266,
                    'ratio_x': 2843503023697920939,
                    'ratio_y': -1496667951217825524,
                },
                {
                    'nw_x_pixel': -616972542,
                    'nw_y_pixel': -1488475135,
                    'width': -4794917491501395617,
                    'height': -4028581048490431013,
                    'ratio_x': 4044666336686048688,
                    'ratio_y': 6840965663239035984,
                },
                {
                    'nw_x_pixel': 168103943,
                    'nw_y_pixel': 831246683,
                    'width': -6373390258245714815,
                    'height': -2118529148311680153,
                    'ratio_x': -1396851133808113438,
                    'ratio_y': -3309355345926731959,
                },
                {
                    'nw_x_pixel': 1369658037,
                    'nw_y_pixel': -1696695723,
                    'width': -3956273625256744112,
                    'height': -2937417515055390685,
                    'ratio_x': -6391706371048090176,
                    'ratio_y': -53206127655696936,
                },
                {
                    'nw_x_pixel': 1318341292,
                    'nw_y_pixel': 1295534855,
                    'width': -1530230043418317434,
                    'height': -3403048455228821458,
                    'ratio_x': 9022974535342146286,
                    'ratio_y': 5637538914720666521,
                },
                {
                    'nw_x_pixel': 100282868,
                    'nw_y_pixel': 409079150,
                    'width': -4600559096414785321,
                    'height': -7706358868492966651,
                    'ratio_x': -2489276919270657574,
                    'ratio_y': -4209529609912613772,
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
            'identifier': 887276,
            'width': 6017307039941027298,
            'height': -1926118728053267929,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 5242314,

            'width': -5227445169756064429,

            'height': 2173455673383131781,

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
            'source_monitor': 8766128,
            'source_nw_x_pixel': -5519803011515026387,
            'source_nw_y_pixel': -5386483991653094341,
            'source_pixel_width': -8488110014121938036,
            'source_pixel_height': -5358994779217128745,
            'rotation': -2033138895795892433,
            'virtual_nw_x_pixel': 143740251,
            'virtual_nw_y_pixel': -1742925563,
            'virtual_width': -183693341,
            'virtual_height': 500617199,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -5296773212492451933,

            'source_nw_y_pixel': -3918150588116188746,

            'source_pixel_width': -6820970862545928623,

            'source_pixel_height': -625154224641567972,

            'rotation': -7764566873883255700,

            'virtual_nw_x_pixel': 1056811313,

            'virtual_nw_y_pixel': 76720256,

            'virtual_width': -454782510,

            'virtual_height': 1783415173,

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
            'description': 'ЮӜ\x87ӡˢŐ\x97ёƎеԏǴÅ˵ͺˁ-\x7fЊӠơЗǇϦѣɇǧԧÔÚ',
            'monitors': [
                {
                    'identifier': 9649040,
                    'width': 1267166479371095199,
                    'height': -2118824752211140079,
                },
                {
                    'identifier': 3488928,
                    'width': 5186732211269186414,
                    'height': -166854467777257296,
                },
                {
                    'identifier': 1028898,
                    'width': 8921926240647635300,
                    'height': -5083293115213335396,
                },
                {
                    'identifier': 3794620,
                    'width': -2412886665105385151,
                    'height': 1721705515187877392,
                },
                {
                    'identifier': 2954039,
                    'width': -5185548722523575721,
                    'height': 2729913149134101438,
                },
                {
                    'identifier': 692100,
                    'width': 7471634999577843910,
                    'height': -7954092183509381303,
                },
                {
                    'identifier': 6562834,
                    'width': -6596712846094058563,
                    'height': 7833796555560071800,
                },
                {
                    'identifier': 1926278,
                    'width': 6990643159954003940,
                    'height': -8921530040106686671,
                },
                {
                    'identifier': 2068542,
                    'width': -4587895310192097510,
                    'height': 722404146750490601,
                },
                {
                    'identifier': 9944786,
                    'width': 4156103337188497481,
                    'height': 7786968142114564245,
                },
            ],
            'screen': [
                {
                    'source_monitor': 3828260,
                    'source_nw_x_pixel': -7453226499425626623,
                    'source_nw_y_pixel': -1903169278501754258,
                    'source_pixel_width': -4010058633741159442,
                    'source_pixel_height': -4330645464441791597,
                    'rotation': -3112577841102384227,
                    'virtual_nw_x_pixel': 1930186552,
                    'virtual_nw_y_pixel': -328666367,
                    'virtual_width': -1677960075,
                    'virtual_height': 749208704,
                },
                {
                    'source_monitor': 9989165,
                    'source_nw_x_pixel': -8215068715998271542,
                    'source_nw_y_pixel': -8177902793607856249,
                    'source_pixel_width': -8802268753987250133,
                    'source_pixel_height': -6310617679872588495,
                    'rotation': -5783209379097155676,
                    'virtual_nw_x_pixel': 1554167794,
                    'virtual_nw_y_pixel': -1894065344,
                    'virtual_width': -1421840538,
                    'virtual_height': 609221662,
                },
                {
                    'source_monitor': 1203597,
                    'source_nw_x_pixel': -922572900776298263,
                    'source_nw_y_pixel': -6068505139389043601,
                    'source_pixel_width': -9101685854987100970,
                    'source_pixel_height': -6219814961620776847,
                    'rotation': -744454327476302616,
                    'virtual_nw_x_pixel': 144364933,
                    'virtual_nw_y_pixel': 147503725,
                    'virtual_width': 530950322,
                    'virtual_height': 987877061,
                },
                {
                    'source_monitor': 6724074,
                    'source_nw_x_pixel': -7783684982770215399,
                    'source_nw_y_pixel': -4040181766421102605,
                    'source_pixel_width': -7534790303009318864,
                    'source_pixel_height': -1844725598571511520,
                    'rotation': -8993403227219215834,
                    'virtual_nw_x_pixel': -1793092958,
                    'virtual_nw_y_pixel': -1384195347,
                    'virtual_width': -103861081,
                    'virtual_height': -191497482,
                },
                {
                    'source_monitor': 4075874,
                    'source_nw_x_pixel': -5083232604693314517,
                    'source_nw_y_pixel': -5777378092325407363,
                    'source_pixel_width': -5875084338896026847,
                    'source_pixel_height': -6034584473309278796,
                    'rotation': -729105536615521618,
                    'virtual_nw_x_pixel': -898136910,
                    'virtual_nw_y_pixel': 245518585,
                    'virtual_width': 1750580069,
                    'virtual_height': 1625084750,
                },
                {
                    'source_monitor': 6804022,
                    'source_nw_x_pixel': -4801520322319625047,
                    'source_nw_y_pixel': -1236270919970581387,
                    'source_pixel_width': -7409566748776095514,
                    'source_pixel_height': -5360035907029890686,
                    'rotation': -6923693173285873216,
                    'virtual_nw_x_pixel': 122709921,
                    'virtual_nw_y_pixel': 803319779,
                    'virtual_width': -297497934,
                    'virtual_height': 1997407260,
                },
                {
                    'source_monitor': 9115888,
                    'source_nw_x_pixel': -4222052391895191343,
                    'source_nw_y_pixel': -636345490834493350,
                    'source_pixel_width': -1603481660104162814,
                    'source_pixel_height': -8359307545988594672,
                    'rotation': -1532243979385667620,
                    'virtual_nw_x_pixel': -1792201399,
                    'virtual_nw_y_pixel': 1566066869,
                    'virtual_width': -229440289,
                    'virtual_height': 233971490,
                },
                {
                    'source_monitor': 4095440,
                    'source_nw_x_pixel': -8624582052682929715,
                    'source_nw_y_pixel': -5237176598509493865,
                    'source_pixel_width': -1716565499461036672,
                    'source_pixel_height': -4185185119569928731,
                    'rotation': -8398592968299084529,
                    'virtual_nw_x_pixel': -1822373776,
                    'virtual_nw_y_pixel': 1582250385,
                    'virtual_width': 1375527697,
                    'virtual_height': 1343969028,
                },
                {
                    'source_monitor': 8832550,
                    'source_nw_x_pixel': -3423308328569262759,
                    'source_nw_y_pixel': -2539678417324157546,
                    'source_pixel_width': -4269486149004258892,
                    'source_pixel_height': -8239976053280730007,
                    'rotation': -3531125135627307555,
                    'virtual_nw_x_pixel': 1016732479,
                    'virtual_nw_y_pixel': -1225465777,
                    'virtual_width': 681146606,
                    'virtual_height': 637506065,
                },
                {
                    'source_monitor': 8520629,
                    'source_nw_x_pixel': -2350784304654241034,
                    'source_nw_y_pixel': -6535390555971023183,
                    'source_pixel_width': -3851096434559259458,
                    'source_pixel_height': -3109709324839293891,
                    'rotation': -5981222466596170675,
                    'virtual_nw_x_pixel': 688622470,
                    'virtual_nw_y_pixel': -132619456,
                    'virtual_width': 200356290,
                    'virtual_height': -579080348,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': -671883,
                    'width': -1975755624987484389,
                    'height': -8822973209834783868,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -6259224145923124340,
                    'source_nw_y_pixel': -7790381346255828569,
                    'source_pixel_width': -1533835047410538311,
                    'source_pixel_height': -7256263348955671175,
                    'rotation': -8536014985953753507,
                    'virtual_nw_x_pixel': 1696250802,
                    'virtual_nw_y_pixel': 384335808,
                    'virtual_width': -1572924539,
                    'virtual_height': 1335086173,
                },
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
                    'description': 'ƾĐƸԥЋϏүӬ˂ľ\x8fe˝ӕŽºvŨsɵΰԮІΐΟȓ`ѥĲϒ',
                    'monitors': [
                            {
                                        'identifier': 2225484,
                                        'width': -8119130799280680092,
                                        'height': -142667386928306404,
                                    },
                            {
                                        'identifier': 4180212,
                                        'width': -6470830357295513308,
                                        'height': 6388353610420224287,
                                    },
                            {
                                        'identifier': -460668,
                                        'width': -2009668815490168876,
                                        'height': -4775630932497690958,
                                    },
                            {
                                        'identifier': -258160,
                                        'width': 6996020076497192795,
                                        'height': 4780253335076926601,
                                    },
                            {
                                        'identifier': 5779839,
                                        'width': -5758361275396637958,
                                        'height': -3692464367717762379,
                                    },
                            {
                                        'identifier': 1797502,
                                        'width': 3322197155961565122,
                                        'height': 5528517346795257842,
                                    },
                            {
                                        'identifier': 1132579,
                                        'width': 1957403472308235343,
                                        'height': -4297054835422833223,
                                    },
                            {
                                        'identifier': 6189088,
                                        'width': 5291456535074863385,
                                        'height': 7677106194234416242,
                                    },
                            {
                                        'identifier': 9825748,
                                        'width': 3219709815629924851,
                                        'height': -6392873845272682402,
                                    },
                            {
                                        'identifier': 288542,
                                        'width': -1673094424858907419,
                                        'height': -112377209034910117,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7733799,
                                        'source_nw_x_pixel': -6674341316587392973,
                                        'source_nw_y_pixel': -4759476281557730892,
                                        'source_pixel_width': -6677216809712150867,
                                        'source_pixel_height': -7792641791894034197,
                                        'rotation': -5668232526847901981,
                                        'virtual_nw_x_pixel': -1071483124,
                                        'virtual_nw_y_pixel': 1971019294,
                                        'virtual_width': 132378246,
                                        'virtual_height': -1589447937,
                                    },
                            {
                                        'source_monitor': 3781915,
                                        'source_nw_x_pixel': -1638688100417022665,
                                        'source_nw_y_pixel': -2006933144122450316,
                                        'source_pixel_width': -5863921775818130834,
                                        'source_pixel_height': -7881067149508218530,
                                        'rotation': -1413969761596818162,
                                        'virtual_nw_x_pixel': 316855257,
                                        'virtual_nw_y_pixel': -412926081,
                                        'virtual_width': 1696280933,
                                        'virtual_height': -993892048,
                                    },
                            {
                                        'source_monitor': 530908,
                                        'source_nw_x_pixel': -8202287261799393674,
                                        'source_nw_y_pixel': -3959920747671254067,
                                        'source_pixel_width': -6333299951503091766,
                                        'source_pixel_height': -5407279094339664569,
                                        'rotation': -1957925007495096386,
                                        'virtual_nw_x_pixel': 14294072,
                                        'virtual_nw_y_pixel': 1722179808,
                                        'virtual_width': -1565070017,
                                        'virtual_height': -920397214,
                                    },
                            {
                                        'source_monitor': 7983517,
                                        'source_nw_x_pixel': -5367679211268630946,
                                        'source_nw_y_pixel': -3148949746080081422,
                                        'source_pixel_width': -7246245418597313443,
                                        'source_pixel_height': -1954481473189868253,
                                        'rotation': -6914609995431445059,
                                        'virtual_nw_x_pixel': 432170029,
                                        'virtual_nw_y_pixel': 418246647,
                                        'virtual_width': -221260176,
                                        'virtual_height': 1311460953,
                                    },
                            {
                                        'source_monitor': 3113881,
                                        'source_nw_x_pixel': -1648769841167631096,
                                        'source_nw_y_pixel': -2692106779968677469,
                                        'source_pixel_width': -3374475605095798815,
                                        'source_pixel_height': -5679061318833026933,
                                        'rotation': -6249430969124465434,
                                        'virtual_nw_x_pixel': -188696889,
                                        'virtual_nw_y_pixel': 1634966673,
                                        'virtual_width': -1428373436,
                                        'virtual_height': 823449786,
                                    },
                            {
                                        'source_monitor': 8897201,
                                        'source_nw_x_pixel': -1110727599476332843,
                                        'source_nw_y_pixel': -7940738569456074263,
                                        'source_pixel_width': -1343653410806333178,
                                        'source_pixel_height': -4090677542807556081,
                                        'rotation': -8805949799266263731,
                                        'virtual_nw_x_pixel': 24752106,
                                        'virtual_nw_y_pixel': -1445049686,
                                        'virtual_width': -1935331327,
                                        'virtual_height': -1653673370,
                                    },
                            {
                                        'source_monitor': 4882866,
                                        'source_nw_x_pixel': -1854192253303245563,
                                        'source_nw_y_pixel': -2490793865006051333,
                                        'source_pixel_width': -633754552444166849,
                                        'source_pixel_height': -4798981072470665037,
                                        'rotation': -7441328210390059864,
                                        'virtual_nw_x_pixel': -837774178,
                                        'virtual_nw_y_pixel': -886042668,
                                        'virtual_width': 728686595,
                                        'virtual_height': 1785887641,
                                    },
                            {
                                        'source_monitor': -393749,
                                        'source_nw_x_pixel': -2350061757911463687,
                                        'source_nw_y_pixel': -921922187277171490,
                                        'source_pixel_width': -2265416610366838876,
                                        'source_pixel_height': -4185718116936523945,
                                        'rotation': -443061293236456920,
                                        'virtual_nw_x_pixel': -160523184,
                                        'virtual_nw_y_pixel': 988884988,
                                        'virtual_width': 516418556,
                                        'virtual_height': 1389394931,
                                    },
                            {
                                        'source_monitor': 3138459,
                                        'source_nw_x_pixel': -1111308857922451708,
                                        'source_nw_y_pixel': -6621828427833652464,
                                        'source_pixel_width': -8666360076476667505,
                                        'source_pixel_height': -8021424040605140974,
                                        'rotation': -443422047798507126,
                                        'virtual_nw_x_pixel': -123645358,
                                        'virtual_nw_y_pixel': 841466480,
                                        'virtual_width': -11021412,
                                        'virtual_height': 1036452728,
                                    },
                            {
                                        'source_monitor': 8452232,
                                        'source_nw_x_pixel': -8908644600676310375,
                                        'source_nw_y_pixel': -1389853601592472971,
                                        'source_pixel_width': -4290968820421477148,
                                        'source_pixel_height': -2538327767949631877,
                                        'rotation': -3800559457155907779,
                                        'virtual_nw_x_pixel': -1019263340,
                                        'virtual_nw_y_pixel': -1462592087,
                                        'virtual_width': 968834839,
                                        'virtual_height': 1280823135,
                                    },
                        ],
                },
                {
                    'description': 'ȍ\x8aĥȉ¼ѡʽ\x87ΚģȜ*ƱmʫˍЛӝPϭӮÆǕϪԟƒїЅӃӡ',
                    'monitors': [
                            {
                                        'identifier': 9961895,
                                        'width': 3631195641712535668,
                                        'height': 8948377879194673833,
                                    },
                            {
                                        'identifier': 1069109,
                                        'width': 1475824217592170926,
                                        'height': 1304085458995988504,
                                    },
                            {
                                        'identifier': 1892032,
                                        'width': 3916968342805664205,
                                        'height': -8496544769540882647,
                                    },
                            {
                                        'identifier': 4437117,
                                        'width': -2561983863911341817,
                                        'height': -2443796293893273380,
                                    },
                            {
                                        'identifier': 9501114,
                                        'width': -4650215925424252440,
                                        'height': 2810047252639178052,
                                    },
                            {
                                        'identifier': 2682889,
                                        'width': -3547452934810609392,
                                        'height': 1419254513765459330,
                                    },
                            {
                                        'identifier': 5714914,
                                        'width': -2581619238927881833,
                                        'height': -6505524811374021061,
                                    },
                            {
                                        'identifier': 4155077,
                                        'width': -7515541622339594733,
                                        'height': -7879053478869977241,
                                    },
                            {
                                        'identifier': 3123569,
                                        'width': 2739483034419417671,
                                        'height': -2370512991813019562,
                                    },
                            {
                                        'identifier': -478316,
                                        'width': 8883199166865758175,
                                        'height': -1515245837108504858,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6340338,
                                        'source_nw_x_pixel': -3272960710870437211,
                                        'source_nw_y_pixel': -8303500548003977403,
                                        'source_pixel_width': -4833655307210938159,
                                        'source_pixel_height': -8886955844786514550,
                                        'rotation': -9051778575633871080,
                                        'virtual_nw_x_pixel': 1436841236,
                                        'virtual_nw_y_pixel': -1182974288,
                                        'virtual_width': -1960583981,
                                        'virtual_height': 1500926643,
                                    },
                            {
                                        'source_monitor': 1600456,
                                        'source_nw_x_pixel': -772736430483123058,
                                        'source_nw_y_pixel': -7303374887816325844,
                                        'source_pixel_width': -3672248669524733987,
                                        'source_pixel_height': -856341843940782952,
                                        'rotation': -3582437297200322118,
                                        'virtual_nw_x_pixel': -634546713,
                                        'virtual_nw_y_pixel': 280615456,
                                        'virtual_width': 927034568,
                                        'virtual_height': -1823109485,
                                    },
                            {
                                        'source_monitor': 2575334,
                                        'source_nw_x_pixel': -7957988135304795739,
                                        'source_nw_y_pixel': -5073522427000696418,
                                        'source_pixel_width': -3762485471789422894,
                                        'source_pixel_height': -9165710385175648605,
                                        'rotation': -2157332291600848367,
                                        'virtual_nw_x_pixel': -1925973031,
                                        'virtual_nw_y_pixel': 1752975714,
                                        'virtual_width': 1529807050,
                                        'virtual_height': 1647433333,
                                    },
                            {
                                        'source_monitor': -650230,
                                        'source_nw_x_pixel': -6014175710112635059,
                                        'source_nw_y_pixel': -4171904199955246555,
                                        'source_pixel_width': -2864184910087124083,
                                        'source_pixel_height': -6141802845721233043,
                                        'rotation': -3802617468311445660,
                                        'virtual_nw_x_pixel': -643965976,
                                        'virtual_nw_y_pixel': -1354830193,
                                        'virtual_width': -1795683985,
                                        'virtual_height': -252162530,
                                    },
                            {
                                        'source_monitor': 2368744,
                                        'source_nw_x_pixel': -1858737848037732806,
                                        'source_nw_y_pixel': -4338030212755716097,
                                        'source_pixel_width': -7745309842934305999,
                                        'source_pixel_height': -8940410190461409019,
                                        'rotation': -2766639458682535935,
                                        'virtual_nw_x_pixel': -101611650,
                                        'virtual_nw_y_pixel': -982181457,
                                        'virtual_width': -141296029,
                                        'virtual_height': 1761215400,
                                    },
                            {
                                        'source_monitor': 884325,
                                        'source_nw_x_pixel': -7714745057666670243,
                                        'source_nw_y_pixel': -2122061351174334364,
                                        'source_pixel_width': -3468570952966183187,
                                        'source_pixel_height': -2269581969409092872,
                                        'rotation': -2314455246458251424,
                                        'virtual_nw_x_pixel': -121384971,
                                        'virtual_nw_y_pixel': 1005853182,
                                        'virtual_width': -734974313,
                                        'virtual_height': 727936101,
                                    },
                            {
                                        'source_monitor': 688055,
                                        'source_nw_x_pixel': -6360192193827554199,
                                        'source_nw_y_pixel': -3504786214157846605,
                                        'source_pixel_width': -8721474465518999182,
                                        'source_pixel_height': -2543791489812293609,
                                        'rotation': -5687927744359241129,
                                        'virtual_nw_x_pixel': 1414527456,
                                        'virtual_nw_y_pixel': 1585672466,
                                        'virtual_width': -1734478109,
                                        'virtual_height': -530458882,
                                    },
                            {
                                        'source_monitor': 8947068,
                                        'source_nw_x_pixel': -326976401939612596,
                                        'source_nw_y_pixel': -1481009434413491961,
                                        'source_pixel_width': -4818989170463250354,
                                        'source_pixel_height': -5064708195583078382,
                                        'rotation': -4797874056760637254,
                                        'virtual_nw_x_pixel': 569288733,
                                        'virtual_nw_y_pixel': -1860125258,
                                        'virtual_width': -342885804,
                                        'virtual_height': -1933302068,
                                    },
                            {
                                        'source_monitor': 1284565,
                                        'source_nw_x_pixel': -1441279726197237572,
                                        'source_nw_y_pixel': -6974604935272107996,
                                        'source_pixel_width': -7230750872718451970,
                                        'source_pixel_height': -3085228706277925794,
                                        'rotation': -1687147771723955122,
                                        'virtual_nw_x_pixel': -1581714759,
                                        'virtual_nw_y_pixel': -1028148120,
                                        'virtual_width': -1434970063,
                                        'virtual_height': 814130389,
                                    },
                            {
                                        'source_monitor': 5773719,
                                        'source_nw_x_pixel': -6026199747777958147,
                                        'source_nw_y_pixel': -6316943250254082891,
                                        'source_pixel_width': -1723886847654955933,
                                        'source_pixel_height': -4409548385060257211,
                                        'rotation': -1698191579665033362,
                                        'virtual_nw_x_pixel': -639913842,
                                        'virtual_nw_y_pixel': -1806508537,
                                        'virtual_width': -1410370850,
                                        'virtual_height': -8828753,
                                    },
                        ],
                },
                {
                    'description': 'ƏɿˏȈȝ˥ӨЧ:½Э˷ÅӕϙĈӆτ+ԅ8ƺͱƒͻŁӚʱƂů',
                    'monitors': [
                            {
                                        'identifier': -848563,
                                        'width': 7424954124567699238,
                                        'height': -4944040269516268434,
                                    },
                            {
                                        'identifier': 1075090,
                                        'width': 7676638220642548148,
                                        'height': -8367097899512840313,
                                    },
                            {
                                        'identifier': 7774164,
                                        'width': 6366889378480730550,
                                        'height': -3795815636439409219,
                                    },
                            {
                                        'identifier': 9557855,
                                        'width': -3355238452163830724,
                                        'height': 6697972153783586746,
                                    },
                            {
                                        'identifier': 8746507,
                                        'width': 974825797418139812,
                                        'height': 7582897213565159783,
                                    },
                            {
                                        'identifier': 1082356,
                                        'width': 8746422905472936048,
                                        'height': 2988432587332559091,
                                    },
                            {
                                        'identifier': 1174925,
                                        'width': 3955409400775252337,
                                        'height': -2668237229666822816,
                                    },
                            {
                                        'identifier': 1354059,
                                        'width': -9168196293209871566,
                                        'height': -8075831071961773513,
                                    },
                            {
                                        'identifier': 5863714,
                                        'width': 3878255589175342332,
                                        'height': -4007345527263159054,
                                    },
                            {
                                        'identifier': 8926587,
                                        'width': 6352301350297805440,
                                        'height': -8044101840892136608,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8648511,
                                        'source_nw_x_pixel': -5051758884075276549,
                                        'source_nw_y_pixel': -5534210542631523833,
                                        'source_pixel_width': -5679685323582841472,
                                        'source_pixel_height': -4076139950316007915,
                                        'rotation': -475746835982570566,
                                        'virtual_nw_x_pixel': -765060343,
                                        'virtual_nw_y_pixel': -1549852224,
                                        'virtual_width': 1543955129,
                                        'virtual_height': -664392191,
                                    },
                            {
                                        'source_monitor': 7644766,
                                        'source_nw_x_pixel': -7946534902529608127,
                                        'source_nw_y_pixel': -2669922143580047124,
                                        'source_pixel_width': -597431175591147865,
                                        'source_pixel_height': -5380996843015420700,
                                        'rotation': -2790901604400390797,
                                        'virtual_nw_x_pixel': -894070862,
                                        'virtual_nw_y_pixel': -361232820,
                                        'virtual_width': 1429251304,
                                        'virtual_height': -189806490,
                                    },
                            {
                                        'source_monitor': 4176127,
                                        'source_nw_x_pixel': -973217401293161789,
                                        'source_nw_y_pixel': -644642492971914093,
                                        'source_pixel_width': -3958584854026050010,
                                        'source_pixel_height': -9034390084386415324,
                                        'rotation': -8764900383635500705,
                                        'virtual_nw_x_pixel': 1890763058,
                                        'virtual_nw_y_pixel': 1631613839,
                                        'virtual_width': -357247127,
                                        'virtual_height': -1189314824,
                                    },
                            {
                                        'source_monitor': 1359516,
                                        'source_nw_x_pixel': -3046015730423821222,
                                        'source_nw_y_pixel': -420407189280667051,
                                        'source_pixel_width': -4569369166126201369,
                                        'source_pixel_height': -8463262295602845352,
                                        'rotation': -1152853852573531031,
                                        'virtual_nw_x_pixel': 1676519591,
                                        'virtual_nw_y_pixel': 1408683907,
                                        'virtual_width': -112735388,
                                        'virtual_height': 1997337766,
                                    },
                            {
                                        'source_monitor': 6376875,
                                        'source_nw_x_pixel': -6930841083536521330,
                                        'source_nw_y_pixel': -3765982761253263413,
                                        'source_pixel_width': -1965623780145282510,
                                        'source_pixel_height': -9172854365746950216,
                                        'rotation': -2041584836254077148,
                                        'virtual_nw_x_pixel': 1292824110,
                                        'virtual_nw_y_pixel': -1544707678,
                                        'virtual_width': 1381902734,
                                        'virtual_height': -1055941703,
                                    },
                            {
                                        'source_monitor': 5604361,
                                        'source_nw_x_pixel': -8593621066618554873,
                                        'source_nw_y_pixel': -2519930512051766130,
                                        'source_pixel_width': -8585084007125449100,
                                        'source_pixel_height': -7443361755742551473,
                                        'rotation': -3794846335301785255,
                                        'virtual_nw_x_pixel': -932595823,
                                        'virtual_nw_y_pixel': 42965363,
                                        'virtual_width': 1047715516,
                                        'virtual_height': -354112221,
                                    },
                            {
                                        'source_monitor': 2082478,
                                        'source_nw_x_pixel': -5085055419803885834,
                                        'source_nw_y_pixel': -9153588691144830935,
                                        'source_pixel_width': -4977836749844785381,
                                        'source_pixel_height': -7710361416212436067,
                                        'rotation': -6430022866020402985,
                                        'virtual_nw_x_pixel': 1685919653,
                                        'virtual_nw_y_pixel': 735618599,
                                        'virtual_width': 924532842,
                                        'virtual_height': 606499463,
                                    },
                            {
                                        'source_monitor': 6248377,
                                        'source_nw_x_pixel': -2777821479957258100,
                                        'source_nw_y_pixel': -6223738203428421637,
                                        'source_pixel_width': -52496837382466304,
                                        'source_pixel_height': -7429556171566500013,
                                        'rotation': -8651422560449815947,
                                        'virtual_nw_x_pixel': -1581465144,
                                        'virtual_nw_y_pixel': 1563997015,
                                        'virtual_width': 1443799999,
                                        'virtual_height': -503384782,
                                    },
                            {
                                        'source_monitor': -418760,
                                        'source_nw_x_pixel': -6134056784166223995,
                                        'source_nw_y_pixel': -956493769858479392,
                                        'source_pixel_width': -4666433387079728528,
                                        'source_pixel_height': -2499690940991409238,
                                        'rotation': -5019022880995532719,
                                        'virtual_nw_x_pixel': 1397860441,
                                        'virtual_nw_y_pixel': 1635531420,
                                        'virtual_width': -1942567942,
                                        'virtual_height': -1028494,
                                    },
                            {
                                        'source_monitor': 1929977,
                                        'source_nw_x_pixel': -1957177207978301727,
                                        'source_nw_y_pixel': -6823053523041411275,
                                        'source_pixel_width': -7479392420311825125,
                                        'source_pixel_height': -7651842463713050801,
                                        'rotation': -1760662726224914374,
                                        'virtual_nw_x_pixel': -6008355,
                                        'virtual_nw_y_pixel': -69263007,
                                        'virtual_width': 1826214877,
                                        'virtual_height': -1850242052,
                                    },
                        ],
                },
                {
                    'description': 'ǈȂθɔʖƁӵӖҖәWҲΉΎθɽˉř¯уêÇԙӋ\x99Ϸͼ˔\x98ğ',
                    'monitors': [
                            {
                                        'identifier': 7224610,
                                        'width': 2737193340985792492,
                                        'height': -3110738998393686130,
                                    },
                            {
                                        'identifier': 9775861,
                                        'width': -8818054209502085583,
                                        'height': -3854466295984626271,
                                    },
                            {
                                        'identifier': 2379475,
                                        'width': 495143093434709827,
                                        'height': 7235986223852207706,
                                    },
                            {
                                        'identifier': 2308117,
                                        'width': -6299246171020944366,
                                        'height': -9131072369800135626,
                                    },
                            {
                                        'identifier': 2333587,
                                        'width': 8993991596921073715,
                                        'height': 6036342288091011615,
                                    },
                            {
                                        'identifier': 4967552,
                                        'width': 2269204848003900708,
                                        'height': 4375533610817477933,
                                    },
                            {
                                        'identifier': 201139,
                                        'width': 1693929449834258490,
                                        'height': -6510586354950482847,
                                    },
                            {
                                        'identifier': 5824062,
                                        'width': 7285046736503658098,
                                        'height': 89319476588204103,
                                    },
                            {
                                        'identifier': 5028050,
                                        'width': 9013799081334267241,
                                        'height': -4362075771895592797,
                                    },
                            {
                                        'identifier': 1174129,
                                        'width': 8408380669825493453,
                                        'height': -754871044735989840,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7836898,
                                        'source_nw_x_pixel': -5164806988740936941,
                                        'source_nw_y_pixel': -5790824819018905520,
                                        'source_pixel_width': -1438273472234573410,
                                        'source_pixel_height': -1295407945423081627,
                                        'rotation': -7053775613284812492,
                                        'virtual_nw_x_pixel': 849763694,
                                        'virtual_nw_y_pixel': -1115378502,
                                        'virtual_width': -67382626,
                                        'virtual_height': 1823797238,
                                    },
                            {
                                        'source_monitor': 5030432,
                                        'source_nw_x_pixel': -2579506509392506244,
                                        'source_nw_y_pixel': -2943489175639943894,
                                        'source_pixel_width': -4117873955565159044,
                                        'source_pixel_height': -1276929640272778979,
                                        'rotation': -7883520904016552493,
                                        'virtual_nw_x_pixel': 780273757,
                                        'virtual_nw_y_pixel': 1530087783,
                                        'virtual_width': 58907986,
                                        'virtual_height': -425440442,
                                    },
                            {
                                        'source_monitor': 5735086,
                                        'source_nw_x_pixel': -2787012112264643309,
                                        'source_nw_y_pixel': -4147955120101621922,
                                        'source_pixel_width': -7833667917000224495,
                                        'source_pixel_height': -3202456610560025838,
                                        'rotation': -177672556936794777,
                                        'virtual_nw_x_pixel': -1150490576,
                                        'virtual_nw_y_pixel': -12485319,
                                        'virtual_width': -1311359413,
                                        'virtual_height': 1712412481,
                                    },
                            {
                                        'source_monitor': 3831724,
                                        'source_nw_x_pixel': -3916963546637757915,
                                        'source_nw_y_pixel': -7140250031220126975,
                                        'source_pixel_width': -5043100699588194684,
                                        'source_pixel_height': -3933950065904351857,
                                        'rotation': -457108693852315432,
                                        'virtual_nw_x_pixel': -1144835816,
                                        'virtual_nw_y_pixel': -1132131497,
                                        'virtual_width': 267483722,
                                        'virtual_height': -1995017878,
                                    },
                            {
                                        'source_monitor': -866030,
                                        'source_nw_x_pixel': -5315879710063141339,
                                        'source_nw_y_pixel': -2379753774543540708,
                                        'source_pixel_width': -2753980284350476476,
                                        'source_pixel_height': -184843849771985253,
                                        'rotation': -4652486982133233075,
                                        'virtual_nw_x_pixel': -1956895373,
                                        'virtual_nw_y_pixel': 1864381283,
                                        'virtual_width': 987861297,
                                        'virtual_height': 1363089271,
                                    },
                            {
                                        'source_monitor': 6094930,
                                        'source_nw_x_pixel': -4164964064651967028,
                                        'source_nw_y_pixel': -3403791384084156010,
                                        'source_pixel_width': -2805466027508219973,
                                        'source_pixel_height': -1109516247529686509,
                                        'rotation': -4192818716500875604,
                                        'virtual_nw_x_pixel': -1658622585,
                                        'virtual_nw_y_pixel': -55097489,
                                        'virtual_width': -1833508801,
                                        'virtual_height': -323686308,
                                    },
                            {
                                        'source_monitor': 6063871,
                                        'source_nw_x_pixel': -7162371704998836251,
                                        'source_nw_y_pixel': -6216720217843098547,
                                        'source_pixel_width': -7174283075917635149,
                                        'source_pixel_height': -9196569442262217261,
                                        'rotation': -3796017202805582462,
                                        'virtual_nw_x_pixel': -1154066664,
                                        'virtual_nw_y_pixel': -39078995,
                                        'virtual_width': 127555042,
                                        'virtual_height': 449968090,
                                    },
                            {
                                        'source_monitor': 5374608,
                                        'source_nw_x_pixel': -9019218698797475328,
                                        'source_nw_y_pixel': -121125958068734364,
                                        'source_pixel_width': -6204679024362451375,
                                        'source_pixel_height': -2436887435345051356,
                                        'rotation': -419420029901760869,
                                        'virtual_nw_x_pixel': -1930994523,
                                        'virtual_nw_y_pixel': 1389692171,
                                        'virtual_width': -957917919,
                                        'virtual_height': -1637205241,
                                    },
                            {
                                        'source_monitor': 7159178,
                                        'source_nw_x_pixel': -1578659246552349235,
                                        'source_nw_y_pixel': -749029169729536033,
                                        'source_pixel_width': -5340431360448385502,
                                        'source_pixel_height': -5577140155906989322,
                                        'rotation': -7934300598153287094,
                                        'virtual_nw_x_pixel': 1180454321,
                                        'virtual_nw_y_pixel': 1799822081,
                                        'virtual_width': 1402222701,
                                        'virtual_height': -1460193601,
                                    },
                            {
                                        'source_monitor': 3942011,
                                        'source_nw_x_pixel': -153470860492268606,
                                        'source_nw_y_pixel': -5803908036856102550,
                                        'source_pixel_width': -1166793256926492061,
                                        'source_pixel_height': -3494610363612723975,
                                        'rotation': -5157175833014474412,
                                        'virtual_nw_x_pixel': 912130568,
                                        'virtual_nw_y_pixel': 209257239,
                                        'virtual_width': -1717063716,
                                        'virtual_height': 1682767243,
                                    },
                        ],
                },
                {
                    'description': 'ǠϏ¨ԩОʢ˱щˀŪБƵҞǌӓɈЅņШԅƑõÿ˻ԍ˟ʔμ¾Ÿ',
                    'monitors': [
                            {
                                        'identifier': 2996597,
                                        'width': -8133601765658176998,
                                        'height': 7991039183173294302,
                                    },
                            {
                                        'identifier': 3285405,
                                        'width': 39122075752765045,
                                        'height': 6359988911973379702,
                                    },
                            {
                                        'identifier': 7816051,
                                        'width': -5438562182062842140,
                                        'height': -6335711387728647210,
                                    },
                            {
                                        'identifier': 4302568,
                                        'width': 2439901407717180971,
                                        'height': 6624449983972100565,
                                    },
                            {
                                        'identifier': -862399,
                                        'width': -8285587076413622371,
                                        'height': 1798108590025365703,
                                    },
                            {
                                        'identifier': 1720371,
                                        'width': -688338603342175742,
                                        'height': 5615198515370897003,
                                    },
                            {
                                        'identifier': 4786409,
                                        'width': 6931323063799996649,
                                        'height': -479137009780140823,
                                    },
                            {
                                        'identifier': 3197994,
                                        'width': 2612832876429347730,
                                        'height': 6838092858760271875,
                                    },
                            {
                                        'identifier': 999597,
                                        'width': -7114792330851851907,
                                        'height': -212909079119688916,
                                    },
                            {
                                        'identifier': 6879753,
                                        'width': 4562989705103737251,
                                        'height': 4574007723318078365,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5736173,
                                        'source_nw_x_pixel': -4885573138435118664,
                                        'source_nw_y_pixel': -2203998344266663317,
                                        'source_pixel_width': -7822666098857730644,
                                        'source_pixel_height': -4239757779039411348,
                                        'rotation': -3631235305555480440,
                                        'virtual_nw_x_pixel': -1319545600,
                                        'virtual_nw_y_pixel': -1205467483,
                                        'virtual_width': -502500989,
                                        'virtual_height': 1499632371,
                                    },
                            {
                                        'source_monitor': 9622572,
                                        'source_nw_x_pixel': -8518525647001449610,
                                        'source_nw_y_pixel': -4560914014470014422,
                                        'source_pixel_width': -7182588208078655420,
                                        'source_pixel_height': -7284212865821298363,
                                        'rotation': -7495202739917722199,
                                        'virtual_nw_x_pixel': 268777351,
                                        'virtual_nw_y_pixel': 542981067,
                                        'virtual_width': -1407819972,
                                        'virtual_height': 1486659848,
                                    },
                            {
                                        'source_monitor': 5847566,
                                        'source_nw_x_pixel': -8340175761984748243,
                                        'source_nw_y_pixel': -8321262708547665926,
                                        'source_pixel_width': -9037954946150639571,
                                        'source_pixel_height': -7067557531364926022,
                                        'rotation': -4671202011571242125,
                                        'virtual_nw_x_pixel': 188542377,
                                        'virtual_nw_y_pixel': 192028227,
                                        'virtual_width': 113244443,
                                        'virtual_height': 846838358,
                                    },
                            {
                                        'source_monitor': 378892,
                                        'source_nw_x_pixel': -3412142776811462818,
                                        'source_nw_y_pixel': -5871532803351065691,
                                        'source_pixel_width': -9137976756957876304,
                                        'source_pixel_height': -2433802690088715951,
                                        'rotation': -8527253001839917980,
                                        'virtual_nw_x_pixel': 41421010,
                                        'virtual_nw_y_pixel': -1239032320,
                                        'virtual_width': -1975749822,
                                        'virtual_height': -967697462,
                                    },
                            {
                                        'source_monitor': 9236328,
                                        'source_nw_x_pixel': -4227713015452902356,
                                        'source_nw_y_pixel': -7075242831185129529,
                                        'source_pixel_width': -1553660494222270472,
                                        'source_pixel_height': -257381795012014317,
                                        'rotation': -7909880800434598179,
                                        'virtual_nw_x_pixel': -1483417914,
                                        'virtual_nw_y_pixel': -945041977,
                                        'virtual_width': -1151986223,
                                        'virtual_height': -751890680,
                                    },
                            {
                                        'source_monitor': 4701528,
                                        'source_nw_x_pixel': -8301687346600800498,
                                        'source_nw_y_pixel': -9167209288869239782,
                                        'source_pixel_width': -5053518869447882915,
                                        'source_pixel_height': -4016484256125903956,
                                        'rotation': -5284663458376747119,
                                        'virtual_nw_x_pixel': 1105712190,
                                        'virtual_nw_y_pixel': 97537761,
                                        'virtual_width': -1182064912,
                                        'virtual_height': -755175701,
                                    },
                            {
                                        'source_monitor': 8278415,
                                        'source_nw_x_pixel': -8450132843738728411,
                                        'source_nw_y_pixel': -2915582484231317333,
                                        'source_pixel_width': -6277821578004153173,
                                        'source_pixel_height': -7169770700285459886,
                                        'rotation': -4808568542678868863,
                                        'virtual_nw_x_pixel': 69006956,
                                        'virtual_nw_y_pixel': 905526847,
                                        'virtual_width': 1522202766,
                                        'virtual_height': -1391510680,
                                    },
                            {
                                        'source_monitor': 8676791,
                                        'source_nw_x_pixel': -3922371143701681580,
                                        'source_nw_y_pixel': -2530500000649016939,
                                        'source_pixel_width': -1877636415351839185,
                                        'source_pixel_height': -9106143071019862792,
                                        'rotation': -3051665108937978067,
                                        'virtual_nw_x_pixel': 1120536606,
                                        'virtual_nw_y_pixel': -1105718165,
                                        'virtual_width': 1947916770,
                                        'virtual_height': -1920811202,
                                    },
                            {
                                        'source_monitor': 7108081,
                                        'source_nw_x_pixel': -4248425746818427802,
                                        'source_nw_y_pixel': -1746109813274080200,
                                        'source_pixel_width': -7975105071783784454,
                                        'source_pixel_height': -8355298243632598413,
                                        'rotation': -1603925676491214630,
                                        'virtual_nw_x_pixel': 1291011738,
                                        'virtual_nw_y_pixel': -984392437,
                                        'virtual_width': 1010780521,
                                        'virtual_height': 787022534,
                                    },
                            {
                                        'source_monitor': 2451276,
                                        'source_nw_x_pixel': -8181370059417110988,
                                        'source_nw_y_pixel': -763415129224245514,
                                        'source_pixel_width': -6857263143584835050,
                                        'source_pixel_height': -5010922624994277345,
                                        'rotation': -3520011805871089004,
                                        'virtual_nw_x_pixel': 850775108,
                                        'virtual_nw_y_pixel': 1921325301,
                                        'virtual_width': -1103626493,
                                        'virtual_height': 443529129,
                                    },
                        ],
                },
                {
                    'description': 'љ¥ǉҲUĔѓfɷŢ˻Дėжч˝ŌĄϸ\x8aɨЅ˒ҽȎȢͺŶȸѤ',
                    'monitors': [
                            {
                                        'identifier': 7135984,
                                        'width': -7910969197182671035,
                                        'height': -5099095132814804933,
                                    },
                            {
                                        'identifier': 9537928,
                                        'width': -644972355400426752,
                                        'height': -5670287063137117450,
                                    },
                            {
                                        'identifier': 5021250,
                                        'width': -4118236444995896380,
                                        'height': 1014779831747065765,
                                    },
                            {
                                        'identifier': 1171335,
                                        'width': -2333994973755008484,
                                        'height': 5581206131595599010,
                                    },
                            {
                                        'identifier': 9481435,
                                        'width': -4101820442701969343,
                                        'height': 839520086608699977,
                                    },
                            {
                                        'identifier': 2217345,
                                        'width': 4236804798322573049,
                                        'height': -945651860556234618,
                                    },
                            {
                                        'identifier': 2585700,
                                        'width': -8881014986987177561,
                                        'height': -675902023770432241,
                                    },
                            {
                                        'identifier': 164660,
                                        'width': -758128853316145319,
                                        'height': 4626780293456267914,
                                    },
                            {
                                        'identifier': 1845195,
                                        'width': 1904489234262697300,
                                        'height': 7719936291256483907,
                                    },
                            {
                                        'identifier': 8265691,
                                        'width': -2064638718715391576,
                                        'height': 7942877338736710971,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8441402,
                                        'source_nw_x_pixel': -3967555865254373930,
                                        'source_nw_y_pixel': -2407095676791325519,
                                        'source_pixel_width': -262355057481913397,
                                        'source_pixel_height': -8954008466619658794,
                                        'rotation': -792784379922241468,
                                        'virtual_nw_x_pixel': -719631407,
                                        'virtual_nw_y_pixel': 1423803260,
                                        'virtual_width': 888916465,
                                        'virtual_height': -1737536792,
                                    },
                            {
                                        'source_monitor': 8274107,
                                        'source_nw_x_pixel': -3029526774458067208,
                                        'source_nw_y_pixel': -1031467171402862875,
                                        'source_pixel_width': -744942487329940429,
                                        'source_pixel_height': -5076554918970834387,
                                        'rotation': -1153416495769574770,
                                        'virtual_nw_x_pixel': 1784491121,
                                        'virtual_nw_y_pixel': -690118632,
                                        'virtual_width': 1827856617,
                                        'virtual_height': -657006897,
                                    },
                            {
                                        'source_monitor': 9584536,
                                        'source_nw_x_pixel': -5734694289485886278,
                                        'source_nw_y_pixel': -1570033860613143865,
                                        'source_pixel_width': -5951511174996916396,
                                        'source_pixel_height': -6066774410636007464,
                                        'rotation': -3428980310142690527,
                                        'virtual_nw_x_pixel': -248693355,
                                        'virtual_nw_y_pixel': 412700646,
                                        'virtual_width': 572854738,
                                        'virtual_height': 315012048,
                                    },
                            {
                                        'source_monitor': 8087877,
                                        'source_nw_x_pixel': -2969980917144727799,
                                        'source_nw_y_pixel': -6493269731742319033,
                                        'source_pixel_width': -4880310907611808116,
                                        'source_pixel_height': -1532691922351015767,
                                        'rotation': -4239840053507696832,
                                        'virtual_nw_x_pixel': 83819864,
                                        'virtual_nw_y_pixel': 1717310600,
                                        'virtual_width': 152733984,
                                        'virtual_height': -1942426308,
                                    },
                            {
                                        'source_monitor': 5116367,
                                        'source_nw_x_pixel': -6424018674146620203,
                                        'source_nw_y_pixel': -3720926595453010667,
                                        'source_pixel_width': -5904153072632568084,
                                        'source_pixel_height': -2672004497042857988,
                                        'rotation': -6833707588099461429,
                                        'virtual_nw_x_pixel': 286991006,
                                        'virtual_nw_y_pixel': -52324294,
                                        'virtual_width': 737309451,
                                        'virtual_height': -634784347,
                                    },
                            {
                                        'source_monitor': 5097496,
                                        'source_nw_x_pixel': -6513863686868764158,
                                        'source_nw_y_pixel': -3328934186929662618,
                                        'source_pixel_width': -7305181114271905598,
                                        'source_pixel_height': -4252197645602979779,
                                        'rotation': -6149340033970015984,
                                        'virtual_nw_x_pixel': 1692542330,
                                        'virtual_nw_y_pixel': 1946145344,
                                        'virtual_width': 232904702,
                                        'virtual_height': -1117054339,
                                    },
                            {
                                        'source_monitor': 4891853,
                                        'source_nw_x_pixel': -6996767420103841999,
                                        'source_nw_y_pixel': -6413753722819094859,
                                        'source_pixel_width': -1965239279735842463,
                                        'source_pixel_height': -2583130464023137179,
                                        'rotation': -8076368744186327507,
                                        'virtual_nw_x_pixel': 1213701349,
                                        'virtual_nw_y_pixel': -452796411,
                                        'virtual_width': -189781875,
                                        'virtual_height': -1667920238,
                                    },
                            {
                                        'source_monitor': 9723687,
                                        'source_nw_x_pixel': -6659857961355784892,
                                        'source_nw_y_pixel': -4306808142770822127,
                                        'source_pixel_width': -5201367634202440340,
                                        'source_pixel_height': -9149516676386150739,
                                        'rotation': -3765308079971625342,
                                        'virtual_nw_x_pixel': 1155830368,
                                        'virtual_nw_y_pixel': -706750372,
                                        'virtual_width': 1883601659,
                                        'virtual_height': 1815334219,
                                    },
                            {
                                        'source_monitor': 4211113,
                                        'source_nw_x_pixel': -5295608676486832874,
                                        'source_nw_y_pixel': -1572586150238746740,
                                        'source_pixel_width': -7210619449934513544,
                                        'source_pixel_height': -1706544144645068922,
                                        'rotation': -5955717230804837173,
                                        'virtual_nw_x_pixel': -1721828752,
                                        'virtual_nw_y_pixel': 1927145935,
                                        'virtual_width': 164267507,
                                        'virtual_height': 687916920,
                                    },
                            {
                                        'source_monitor': 4816147,
                                        'source_nw_x_pixel': -4494480977189247916,
                                        'source_nw_y_pixel': -2151964849572916848,
                                        'source_pixel_width': -3923586602232015580,
                                        'source_pixel_height': -688684332733391536,
                                        'rotation': -8024200474597912848,
                                        'virtual_nw_x_pixel': -396042238,
                                        'virtual_nw_y_pixel': 852298640,
                                        'virtual_width': -1820976132,
                                        'virtual_height': 960413340,
                                    },
                        ],
                },
                {
                    'description': 'ĜҷbʺşΝԥоXƉЏƤƮЦѱã\x8f¾tÊǸǒʬâӇԇǢҬȓH',
                    'monitors': [
                            {
                                        'identifier': 306230,
                                        'width': 4902332405891126217,
                                        'height': -4960454358164385436,
                                    },
                            {
                                        'identifier': 9245104,
                                        'width': -66764410140160396,
                                        'height': 7980945996587657341,
                                    },
                            {
                                        'identifier': 520548,
                                        'width': -7552552324142504904,
                                        'height': 636429918053866863,
                                    },
                            {
                                        'identifier': 3262128,
                                        'width': 6317497885612330887,
                                        'height': -5876939947472182626,
                                    },
                            {
                                        'identifier': 6445096,
                                        'width': 973457255405047607,
                                        'height': 6754271439955017072,
                                    },
                            {
                                        'identifier': 8413914,
                                        'width': 7346203479823575648,
                                        'height': -3125035937223212069,
                                    },
                            {
                                        'identifier': 6356110,
                                        'width': -6469830966416246118,
                                        'height': 1459834471167474992,
                                    },
                            {
                                        'identifier': 4973884,
                                        'width': 6741998490940960112,
                                        'height': 2539493781291685242,
                                    },
                            {
                                        'identifier': 1047099,
                                        'width': 3717276362667083882,
                                        'height': -2580140574919449826,
                                    },
                            {
                                        'identifier': 1865602,
                                        'width': -5743108203157501503,
                                        'height': -1348879167653860975,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4695372,
                                        'source_nw_x_pixel': -138454391296429305,
                                        'source_nw_y_pixel': -2915487132862265179,
                                        'source_pixel_width': -7128055936561951338,
                                        'source_pixel_height': -8254101678815654515,
                                        'rotation': -5800132703304013507,
                                        'virtual_nw_x_pixel': 595601153,
                                        'virtual_nw_y_pixel': -318001747,
                                        'virtual_width': -1539134893,
                                        'virtual_height': -320092533,
                                    },
                            {
                                        'source_monitor': 686454,
                                        'source_nw_x_pixel': -1953431660490971379,
                                        'source_nw_y_pixel': -6052402220809597396,
                                        'source_pixel_width': -6917910107272540097,
                                        'source_pixel_height': -7018678795138822542,
                                        'rotation': -3286289650824036145,
                                        'virtual_nw_x_pixel': 59911617,
                                        'virtual_nw_y_pixel': 139260805,
                                        'virtual_width': -741595225,
                                        'virtual_height': -752954936,
                                    },
                            {
                                        'source_monitor': 2842769,
                                        'source_nw_x_pixel': -7733029816173865326,
                                        'source_nw_y_pixel': -612870555806369427,
                                        'source_pixel_width': -8651525433322533361,
                                        'source_pixel_height': -1399820474951998442,
                                        'rotation': -901003601760563619,
                                        'virtual_nw_x_pixel': 1693596417,
                                        'virtual_nw_y_pixel': 645824203,
                                        'virtual_width': -1216999880,
                                        'virtual_height': -222065649,
                                    },
                            {
                                        'source_monitor': 9998134,
                                        'source_nw_x_pixel': -5878315396122661457,
                                        'source_nw_y_pixel': -1734835708859481046,
                                        'source_pixel_width': -1353651496769278218,
                                        'source_pixel_height': -3998968369100411810,
                                        'rotation': -8252222512106860818,
                                        'virtual_nw_x_pixel': 431439564,
                                        'virtual_nw_y_pixel': -519474796,
                                        'virtual_width': -1562609407,
                                        'virtual_height': -1026244255,
                                    },
                            {
                                        'source_monitor': 5510305,
                                        'source_nw_x_pixel': -5123574116414896284,
                                        'source_nw_y_pixel': -8444431907839819456,
                                        'source_pixel_width': -5159292970085841035,
                                        'source_pixel_height': -5867348429809147049,
                                        'rotation': -3553016748694361706,
                                        'virtual_nw_x_pixel': -832403105,
                                        'virtual_nw_y_pixel': 946468182,
                                        'virtual_width': 1491442383,
                                        'virtual_height': 90432435,
                                    },
                            {
                                        'source_monitor': 3614517,
                                        'source_nw_x_pixel': -4467431699923378017,
                                        'source_nw_y_pixel': -161475973522692530,
                                        'source_pixel_width': -2832392313407860789,
                                        'source_pixel_height': -3245487930404061862,
                                        'rotation': -6928455752077913833,
                                        'virtual_nw_x_pixel': -1331566975,
                                        'virtual_nw_y_pixel': 1893571496,
                                        'virtual_width': -1969051987,
                                        'virtual_height': 1140241176,
                                    },
                            {
                                        'source_monitor': 8771987,
                                        'source_nw_x_pixel': -7650686043720635273,
                                        'source_nw_y_pixel': -2399697220459045840,
                                        'source_pixel_width': -3378043560049772287,
                                        'source_pixel_height': -4444588176365816660,
                                        'rotation': -720619862124933914,
                                        'virtual_nw_x_pixel': 1269916368,
                                        'virtual_nw_y_pixel': -328972941,
                                        'virtual_width': -1115954288,
                                        'virtual_height': -797592516,
                                    },
                            {
                                        'source_monitor': 7183583,
                                        'source_nw_x_pixel': -5666106352666003259,
                                        'source_nw_y_pixel': -7955103454551678109,
                                        'source_pixel_width': -9190045211927722820,
                                        'source_pixel_height': -7187715303826503713,
                                        'rotation': -7335528057162224834,
                                        'virtual_nw_x_pixel': -240799653,
                                        'virtual_nw_y_pixel': 1996182988,
                                        'virtual_width': 551257993,
                                        'virtual_height': -1185987623,
                                    },
                            {
                                        'source_monitor': 5308684,
                                        'source_nw_x_pixel': -6865300941085178139,
                                        'source_nw_y_pixel': -3552437673145500103,
                                        'source_pixel_width': -3634220399642061616,
                                        'source_pixel_height': -1939489336758728088,
                                        'rotation': -2028714401022018098,
                                        'virtual_nw_x_pixel': 1339293476,
                                        'virtual_nw_y_pixel': -733053412,
                                        'virtual_width': 1452863555,
                                        'virtual_height': 1726576924,
                                    },
                            {
                                        'source_monitor': -262769,
                                        'source_nw_x_pixel': -7394064296399091619,
                                        'source_nw_y_pixel': -6435379686411100578,
                                        'source_pixel_width': -8082768775974329979,
                                        'source_pixel_height': -8577894024671037904,
                                        'rotation': -6244430137051814904,
                                        'virtual_nw_x_pixel': 903857500,
                                        'virtual_nw_y_pixel': 1426535707,
                                        'virtual_width': 370598443,
                                        'virtual_height': -1408280011,
                                    },
                        ],
                },
                {
                    'description': '!ӨӰά)!ʿˁKŪȭХ˞ϗϪƬλ<ŹǉǉêфŽȨ҃lέ<Ƹ',
                    'monitors': [
                            {
                                        'identifier': 7854670,
                                        'width': 9209089346358840959,
                                        'height': 3489756453806804555,
                                    },
                            {
                                        'identifier': 2817846,
                                        'width': -8474772804085645472,
                                        'height': -589720495204324421,
                                    },
                            {
                                        'identifier': 6968079,
                                        'width': 7584810625851292954,
                                        'height': 1203098909174191421,
                                    },
                            {
                                        'identifier': 173048,
                                        'width': 5627915789145733238,
                                        'height': 5845150709396879101,
                                    },
                            {
                                        'identifier': 2839092,
                                        'width': 7494369770711680806,
                                        'height': -1644517883535582151,
                                    },
                            {
                                        'identifier': -600048,
                                        'width': -1222236150095722966,
                                        'height': 4756197382393045968,
                                    },
                            {
                                        'identifier': 4311821,
                                        'width': -6945410436370093002,
                                        'height': 439501074080134132,
                                    },
                            {
                                        'identifier': 6180680,
                                        'width': -5843085719836787026,
                                        'height': -1312443563987729511,
                                    },
                            {
                                        'identifier': 4352221,
                                        'width': -3680401146215796181,
                                        'height': -3160592617274871143,
                                    },
                            {
                                        'identifier': 8692305,
                                        'width': 7043691549580364894,
                                        'height': -5357945799648996452,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3725870,
                                        'source_nw_x_pixel': -5707965082989861220,
                                        'source_nw_y_pixel': -5112195558303306629,
                                        'source_pixel_width': -5763574192753546151,
                                        'source_pixel_height': -2683201208139474908,
                                        'rotation': -4722144214808072996,
                                        'virtual_nw_x_pixel': -114417248,
                                        'virtual_nw_y_pixel': -332775416,
                                        'virtual_width': -1595838562,
                                        'virtual_height': 1973845732,
                                    },
                            {
                                        'source_monitor': 248243,
                                        'source_nw_x_pixel': -7346610090961354429,
                                        'source_nw_y_pixel': -7492142788340258954,
                                        'source_pixel_width': -4962827797336941739,
                                        'source_pixel_height': -3741235345796504597,
                                        'rotation': -5050800688223108070,
                                        'virtual_nw_x_pixel': 1233400773,
                                        'virtual_nw_y_pixel': 1652912,
                                        'virtual_width': -1627120307,
                                        'virtual_height': -1739055652,
                                    },
                            {
                                        'source_monitor': 7364504,
                                        'source_nw_x_pixel': -8768791911904472719,
                                        'source_nw_y_pixel': -2512074699513734528,
                                        'source_pixel_width': -2793420101277334430,
                                        'source_pixel_height': -4602063088314552156,
                                        'rotation': -1758376413581405838,
                                        'virtual_nw_x_pixel': 980014168,
                                        'virtual_nw_y_pixel': -1832055631,
                                        'virtual_width': -1336626041,
                                        'virtual_height': -40800772,
                                    },
                            {
                                        'source_monitor': 9812991,
                                        'source_nw_x_pixel': -1572930377742680727,
                                        'source_nw_y_pixel': -3237853520274075543,
                                        'source_pixel_width': -3985392206862619294,
                                        'source_pixel_height': -1017821094277829059,
                                        'rotation': -7866459977153561182,
                                        'virtual_nw_x_pixel': 1508403449,
                                        'virtual_nw_y_pixel': -1426509981,
                                        'virtual_width': 1121261136,
                                        'virtual_height': -160413441,
                                    },
                            {
                                        'source_monitor': -24387,
                                        'source_nw_x_pixel': -8696963928173729727,
                                        'source_nw_y_pixel': -7577724608788656228,
                                        'source_pixel_width': -3212631109131235114,
                                        'source_pixel_height': -3633855910566892913,
                                        'rotation': -3211875613282383863,
                                        'virtual_nw_x_pixel': -73090453,
                                        'virtual_nw_y_pixel': -1561373809,
                                        'virtual_width': -219921804,
                                        'virtual_height': 108506435,
                                    },
                            {
                                        'source_monitor': 4086419,
                                        'source_nw_x_pixel': -3183587274034265637,
                                        'source_nw_y_pixel': -7406543513848481337,
                                        'source_pixel_width': -1877790112937007986,
                                        'source_pixel_height': -103041854147987687,
                                        'rotation': -3189745035114037837,
                                        'virtual_nw_x_pixel': 1203486897,
                                        'virtual_nw_y_pixel': 1832594550,
                                        'virtual_width': 1410412441,
                                        'virtual_height': -91071367,
                                    },
                            {
                                        'source_monitor': 2752009,
                                        'source_nw_x_pixel': -610661712715699934,
                                        'source_nw_y_pixel': -7638635646856473447,
                                        'source_pixel_width': -2703168936203178230,
                                        'source_pixel_height': -3657753522588338781,
                                        'rotation': -9139811910170377637,
                                        'virtual_nw_x_pixel': -121912109,
                                        'virtual_nw_y_pixel': 1384659155,
                                        'virtual_width': 224483298,
                                        'virtual_height': 585111729,
                                    },
                            {
                                        'source_monitor': 6755195,
                                        'source_nw_x_pixel': -8091350165377317603,
                                        'source_nw_y_pixel': -3868766824199186202,
                                        'source_pixel_width': -1644090223965057075,
                                        'source_pixel_height': -1805291527687172284,
                                        'rotation': -8861224592924956430,
                                        'virtual_nw_x_pixel': -1611101235,
                                        'virtual_nw_y_pixel': -1230949753,
                                        'virtual_width': 941243677,
                                        'virtual_height': 1766034058,
                                    },
                            {
                                        'source_monitor': 7744556,
                                        'source_nw_x_pixel': -1566079568104317468,
                                        'source_nw_y_pixel': -8672364244903776966,
                                        'source_pixel_width': -5051230855603125509,
                                        'source_pixel_height': -4009405547402297873,
                                        'rotation': -4994578581668614057,
                                        'virtual_nw_x_pixel': 793587313,
                                        'virtual_nw_y_pixel': -273478034,
                                        'virtual_width': 1284886664,
                                        'virtual_height': -518224571,
                                    },
                            {
                                        'source_monitor': 3272942,
                                        'source_nw_x_pixel': -6827920432980545265,
                                        'source_nw_y_pixel': -4768672622882262854,
                                        'source_pixel_width': -8994587973698215368,
                                        'source_pixel_height': -8696260626182129411,
                                        'rotation': -6049893780040568604,
                                        'virtual_nw_x_pixel': -1677474334,
                                        'virtual_nw_y_pixel': -1936668144,
                                        'virtual_width': 574085820,
                                        'virtual_height': 593598555,
                                    },
                        ],
                },
                {
                    'description': 'зŇӪӗǾ(ʄ҇уǭΧԡҡԂϦːѕQτӖÄΥîԜѵY\x9dŪɉƈ',
                    'monitors': [
                            {
                                        'identifier': 5742826,
                                        'width': -5799316432124006897,
                                        'height': -6458332918014770148,
                                    },
                            {
                                        'identifier': 4708751,
                                        'width': -3510643739434907725,
                                        'height': -4963389360071639764,
                                    },
                            {
                                        'identifier': 9739636,
                                        'width': 7235895779351322530,
                                        'height': -2961520847027677330,
                                    },
                            {
                                        'identifier': 200296,
                                        'width': -4222772159595450125,
                                        'height': -8537190891443485796,
                                    },
                            {
                                        'identifier': 7933049,
                                        'width': 2931692439094428837,
                                        'height': 5109346373628604436,
                                    },
                            {
                                        'identifier': 372417,
                                        'width': 4819595166904018495,
                                        'height': -6846934129931507057,
                                    },
                            {
                                        'identifier': 5810427,
                                        'width': 1706013086416809473,
                                        'height': -6895877413189289401,
                                    },
                            {
                                        'identifier': 7889842,
                                        'width': -5735726245632974823,
                                        'height': 2448375999585459084,
                                    },
                            {
                                        'identifier': 8599610,
                                        'width': -4721055111757941506,
                                        'height': -6514178378713246742,
                                    },
                            {
                                        'identifier': 1015313,
                                        'width': -1569100700042388767,
                                        'height': 2132282956966482963,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1111154,
                                        'source_nw_x_pixel': -6447910467768607432,
                                        'source_nw_y_pixel': -6879354044231449159,
                                        'source_pixel_width': -7515095104476744359,
                                        'source_pixel_height': -7939149219996961403,
                                        'rotation': -4160378713765645608,
                                        'virtual_nw_x_pixel': -533766287,
                                        'virtual_nw_y_pixel': -285523870,
                                        'virtual_width': -853537346,
                                        'virtual_height': 597180511,
                                    },
                            {
                                        'source_monitor': 7747177,
                                        'source_nw_x_pixel': -4673019903241698225,
                                        'source_nw_y_pixel': -7701247487002785198,
                                        'source_pixel_width': -5923868031740596057,
                                        'source_pixel_height': -564800536853384025,
                                        'rotation': -6698498009886843571,
                                        'virtual_nw_x_pixel': -1954322049,
                                        'virtual_nw_y_pixel': 1432367088,
                                        'virtual_width': -171208845,
                                        'virtual_height': 1143233740,
                                    },
                            {
                                        'source_monitor': 5852821,
                                        'source_nw_x_pixel': -1507683024636483991,
                                        'source_nw_y_pixel': -4138991083283827932,
                                        'source_pixel_width': -3506421063284145964,
                                        'source_pixel_height': -4619544675066191893,
                                        'rotation': -2951673091054149308,
                                        'virtual_nw_x_pixel': -346939402,
                                        'virtual_nw_y_pixel': 345839297,
                                        'virtual_width': -449414482,
                                        'virtual_height': 379495820,
                                    },
                            {
                                        'source_monitor': 4193744,
                                        'source_nw_x_pixel': -14596258995157183,
                                        'source_nw_y_pixel': -1273938562327479454,
                                        'source_pixel_width': -4551270591911876547,
                                        'source_pixel_height': -5783902922864275652,
                                        'rotation': -1135629536921489709,
                                        'virtual_nw_x_pixel': -185806076,
                                        'virtual_nw_y_pixel': 1583710549,
                                        'virtual_width': -1043586254,
                                        'virtual_height': 1562394942,
                                    },
                            {
                                        'source_monitor': 8113716,
                                        'source_nw_x_pixel': -4040516619892025947,
                                        'source_nw_y_pixel': -7634203693528123213,
                                        'source_pixel_width': -8779163847291228124,
                                        'source_pixel_height': -263910720387450493,
                                        'rotation': -7424472695930751216,
                                        'virtual_nw_x_pixel': -249748283,
                                        'virtual_nw_y_pixel': -869478478,
                                        'virtual_width': 227993447,
                                        'virtual_height': 562431808,
                                    },
                            {
                                        'source_monitor': 7025314,
                                        'source_nw_x_pixel': -1961932764632218287,
                                        'source_nw_y_pixel': -7173598182665096277,
                                        'source_pixel_width': -5822381033539860578,
                                        'source_pixel_height': -1210561465492929875,
                                        'rotation': -5108874752811142305,
                                        'virtual_nw_x_pixel': -1306032001,
                                        'virtual_nw_y_pixel': -1270370149,
                                        'virtual_width': 222836955,
                                        'virtual_height': 1256055563,
                                    },
                            {
                                        'source_monitor': 6477835,
                                        'source_nw_x_pixel': -4013067924732763110,
                                        'source_nw_y_pixel': -8918618894603413394,
                                        'source_pixel_width': -7096587995824217547,
                                        'source_pixel_height': -5892704313709994951,
                                        'rotation': -965499514051674893,
                                        'virtual_nw_x_pixel': 497901037,
                                        'virtual_nw_y_pixel': 1221713123,
                                        'virtual_width': -1250077997,
                                        'virtual_height': -606788376,
                                    },
                            {
                                        'source_monitor': 3044516,
                                        'source_nw_x_pixel': -2022493878426832508,
                                        'source_nw_y_pixel': -2180762013512569800,
                                        'source_pixel_width': -4907851839655279076,
                                        'source_pixel_height': -365592089023405078,
                                        'rotation': -5661487237649127135,
                                        'virtual_nw_x_pixel': 55799844,
                                        'virtual_nw_y_pixel': 1061821631,
                                        'virtual_width': 1022804199,
                                        'virtual_height': 1286706559,
                                    },
                            {
                                        'source_monitor': 3635988,
                                        'source_nw_x_pixel': -3220594410560003769,
                                        'source_nw_y_pixel': -8586918650684315804,
                                        'source_pixel_width': -9014974132288281498,
                                        'source_pixel_height': -1198323074772834114,
                                        'rotation': -1465594385410016350,
                                        'virtual_nw_x_pixel': -973136690,
                                        'virtual_nw_y_pixel': -1222869914,
                                        'virtual_width': 791612634,
                                        'virtual_height': 845143820,
                                    },
                            {
                                        'source_monitor': 1162785,
                                        'source_nw_x_pixel': -784471780541027404,
                                        'source_nw_y_pixel': -4157111917784548908,
                                        'source_pixel_width': -1556601502311569826,
                                        'source_pixel_height': -7155590126334204589,
                                        'rotation': -6043181984655741259,
                                        'virtual_nw_x_pixel': 1442519456,
                                        'virtual_nw_y_pixel': 1171793180,
                                        'virtual_width': -716968712,
                                        'virtual_height': -20752633,
                                    },
                        ],
                },
                {
                    'description': "þɊёļ˭ʍƛćӔѼzάκƍƋƙàӪȰɹ'әŋԀΨîҧŲϬҁ",
                    'monitors': [
                            {
                                        'identifier': 3827900,
                                        'width': -148927324166373222,
                                        'height': 550136746863451350,
                                    },
                            {
                                        'identifier': 4811158,
                                        'width': 4615892071396564202,
                                        'height': 2224381052879413644,
                                    },
                            {
                                        'identifier': 8069452,
                                        'width': -6880178023926158643,
                                        'height': 1061591187130718398,
                                    },
                            {
                                        'identifier': 9523200,
                                        'width': 849239591830948875,
                                        'height': 3152710663834511451,
                                    },
                            {
                                        'identifier': -577729,
                                        'width': -517330670521720626,
                                        'height': 4921525911764729632,
                                    },
                            {
                                        'identifier': 1108343,
                                        'width': 7622959622091688314,
                                        'height': 2742773895890486395,
                                    },
                            {
                                        'identifier': 7423949,
                                        'width': -5269011711957248204,
                                        'height': 76730100231078837,
                                    },
                            {
                                        'identifier': 4907740,
                                        'width': 7755805312611838562,
                                        'height': -1435650852961182560,
                                    },
                            {
                                        'identifier': 5168018,
                                        'width': -5788006574792533026,
                                        'height': -3384879508242364347,
                                    },
                            {
                                        'identifier': 2214103,
                                        'width': 7919749132269963377,
                                        'height': 2303897156145991120,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 335053,
                                        'source_nw_x_pixel': -1934359903313213725,
                                        'source_nw_y_pixel': -3519228016913169929,
                                        'source_pixel_width': -4174230420236163681,
                                        'source_pixel_height': -7963574940637905626,
                                        'rotation': -1937862775114555736,
                                        'virtual_nw_x_pixel': 1246154597,
                                        'virtual_nw_y_pixel': -525777662,
                                        'virtual_width': 1724072944,
                                        'virtual_height': 17897706,
                                    },
                            {
                                        'source_monitor': 7169166,
                                        'source_nw_x_pixel': -5351229475329263585,
                                        'source_nw_y_pixel': -8636036249604267638,
                                        'source_pixel_width': -5050418310125954790,
                                        'source_pixel_height': -854628799041644502,
                                        'rotation': -8228700644642361583,
                                        'virtual_nw_x_pixel': 1081445759,
                                        'virtual_nw_y_pixel': -779591172,
                                        'virtual_width': 454497085,
                                        'virtual_height': -80346389,
                                    },
                            {
                                        'source_monitor': 2858234,
                                        'source_nw_x_pixel': -722166492557248768,
                                        'source_nw_y_pixel': -837678196913150372,
                                        'source_pixel_width': -6781903178606259825,
                                        'source_pixel_height': -4012659593940555097,
                                        'rotation': -1476088258663049044,
                                        'virtual_nw_x_pixel': -1855913657,
                                        'virtual_nw_y_pixel': -1500403143,
                                        'virtual_width': -916310578,
                                        'virtual_height': 1440092391,
                                    },
                            {
                                        'source_monitor': 3579264,
                                        'source_nw_x_pixel': -3607872194918553635,
                                        'source_nw_y_pixel': -4471180529755836884,
                                        'source_pixel_width': -6709953222245992926,
                                        'source_pixel_height': -5879401754183936022,
                                        'rotation': -5268854220763512492,
                                        'virtual_nw_x_pixel': -1107333734,
                                        'virtual_nw_y_pixel': 1450615889,
                                        'virtual_width': -1066259892,
                                        'virtual_height': 1097790830,
                                    },
                            {
                                        'source_monitor': 5610463,
                                        'source_nw_x_pixel': -1016464937201224921,
                                        'source_nw_y_pixel': -4334479073806188602,
                                        'source_pixel_width': -6720071696912938784,
                                        'source_pixel_height': -2134549935192010224,
                                        'rotation': -6667046223500215174,
                                        'virtual_nw_x_pixel': -560251197,
                                        'virtual_nw_y_pixel': 1007757204,
                                        'virtual_width': 1922305861,
                                        'virtual_height': 661226111,
                                    },
                            {
                                        'source_monitor': 136799,
                                        'source_nw_x_pixel': -6580352783733930091,
                                        'source_nw_y_pixel': -466923443779692785,
                                        'source_pixel_width': -2288169281762211796,
                                        'source_pixel_height': -3746855848451121126,
                                        'rotation': -1646515692349869453,
                                        'virtual_nw_x_pixel': -1203623629,
                                        'virtual_nw_y_pixel': 107743060,
                                        'virtual_width': 43960490,
                                        'virtual_height': 1721876605,
                                    },
                            {
                                        'source_monitor': 4000926,
                                        'source_nw_x_pixel': -4144506571999332894,
                                        'source_nw_y_pixel': -1238954332182387147,
                                        'source_pixel_width': -5033918122678067584,
                                        'source_pixel_height': -6834957382611635180,
                                        'rotation': -2802592143138307585,
                                        'virtual_nw_x_pixel': -400792936,
                                        'virtual_nw_y_pixel': 798851658,
                                        'virtual_width': 1712401189,
                                        'virtual_height': -1310680611,
                                    },
                            {
                                        'source_monitor': 6523212,
                                        'source_nw_x_pixel': -2595777129792635516,
                                        'source_nw_y_pixel': -7893369221699180325,
                                        'source_pixel_width': -1321576048382121937,
                                        'source_pixel_height': -5720221817117432588,
                                        'rotation': -3966192385059499842,
                                        'virtual_nw_x_pixel': 1631571364,
                                        'virtual_nw_y_pixel': -1617235153,
                                        'virtual_width': -390267356,
                                        'virtual_height': -145322469,
                                    },
                            {
                                        'source_monitor': 3952297,
                                        'source_nw_x_pixel': -8112120928404297286,
                                        'source_nw_y_pixel': -5809433604020790199,
                                        'source_pixel_width': -3322147655175959718,
                                        'source_pixel_height': -1982344507795850838,
                                        'rotation': -324179445992476847,
                                        'virtual_nw_x_pixel': -922736141,
                                        'virtual_nw_y_pixel': -51057897,
                                        'virtual_width': -611436161,
                                        'virtual_height': 1355641784,
                                    },
                            {
                                        'source_monitor': 6594761,
                                        'source_nw_x_pixel': -2923858665439820852,
                                        'source_nw_y_pixel': -1729231858783486166,
                                        'source_pixel_width': -4556925681330737036,
                                        'source_pixel_height': -6735191148325864932,
                                        'rotation': -3589729156854715131,
                                        'virtual_nw_x_pixel': 283402892,
                                        'virtual_nw_y_pixel': -640234934,
                                        'virtual_width': -1960218740,
                                        'virtual_height': -1774079351,
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
                                        'identifier': 2262779,
                                        'width': 700582110848472131,
                                        'height': 6243792326900932973,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -924149919585702243,
                                        'source_nw_y_pixel': -2330275770149841053,
                                        'source_pixel_width': -8964599071865379974,
                                        'source_pixel_height': -6452441805074326385,
                                        'rotation': -4924803135423789791,
                                        'virtual_nw_x_pixel': 262885772,
                                        'virtual_nw_y_pixel': -1639726025,
                                        'virtual_width': -1370904682,
                                        'virtual_height': -1528655706,
                                    },
                        ],
                },
            ],

        },
    ),
]
