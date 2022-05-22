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
            'nw_x_pixel': 1834384082,
            'nw_y_pixel': 920202857,
            'width': -6551985191504282851,
            'height': -7846845592685998919,
            'ratio_x': 8392489578890239077,
            'ratio_y': -6474196004074704033,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 1562921781,

            'nw_y_pixel': 194225523,

            'width': -8957971077083016704,

            'height': -790879522573556365,

            'ratio_x': 1260036594905815037,

            'ratio_y': -2790510573979986707,

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
                    'nw_x_pixel': -461781751,
                    'nw_y_pixel': -1218250552,
                    'width': -8261352192527614268,
                    'height': -7292119883149826551,
                    'ratio_x': 2019594899340556215,
                    'ratio_y': -5622835523568390537,
                },
                {
                    'nw_x_pixel': -1124637153,
                    'nw_y_pixel': 1562099119,
                    'width': -5464419067220155029,
                    'height': -1158523494041992636,
                    'ratio_x': 4465974651754446038,
                    'ratio_y': -7644895467868918471,
                },
                {
                    'nw_x_pixel': 722729352,
                    'nw_y_pixel': 171538053,
                    'width': -4970896137125977683,
                    'height': -1218863208428958728,
                    'ratio_x': 8345953410657855635,
                    'ratio_y': 3087535688479724769,
                },
                {
                    'nw_x_pixel': 62940360,
                    'nw_y_pixel': -1196855089,
                    'width': -8783481889424407010,
                    'height': -5029381473214143629,
                    'ratio_x': -2486662810936561619,
                    'ratio_y': -3656289772642372478,
                },
                {
                    'nw_x_pixel': -57636863,
                    'nw_y_pixel': -486901533,
                    'width': -921658280806222065,
                    'height': -7625409924028768477,
                    'ratio_x': -4798258669790337225,
                    'ratio_y': 1652507929677089779,
                },
                {
                    'nw_x_pixel': -1125122518,
                    'nw_y_pixel': -981718123,
                    'width': -4759768840078774540,
                    'height': -4361198093164839599,
                    'ratio_x': -2468827850699901375,
                    'ratio_y': -9176042455482051693,
                },
                {
                    'nw_x_pixel': -1592745968,
                    'nw_y_pixel': -287186393,
                    'width': -3025386896269352175,
                    'height': -8682477434620930454,
                    'ratio_x': 2344105593867384711,
                    'ratio_y': -6543022551209305165,
                },
                {
                    'nw_x_pixel': -1798428964,
                    'nw_y_pixel': -477065295,
                    'width': -5896157548289176042,
                    'height': -9017478864132217916,
                    'ratio_x': 793976005017241551,
                    'ratio_y': -2061333328643198129,
                },
                {
                    'nw_x_pixel': -1992695287,
                    'nw_y_pixel': 1593749159,
                    'width': -2320287033899372879,
                    'height': -5053154538328219469,
                    'ratio_x': -1725570077065442945,
                    'ratio_y': -8924267079065835956,
                },
                {
                    'nw_x_pixel': 1988027096,
                    'nw_y_pixel': 283822604,
                    'width': -4413544677289575058,
                    'height': -1491960055170795177,
                    'ratio_x': -3732140418744658936,
                    'ratio_y': 8369095159983892928,
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
            'identifier': 9817415,
            'width': 2753886667369609010,
            'height': 510533009087235756,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 1876442,

            'width': 5810547187977427695,

            'height': 1976921586625234879,

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
            'source_monitor': 2020932,
            'source_nw_x_pixel': -1088455380884565974,
            'source_nw_y_pixel': -5787942753001206916,
            'source_pixel_width': -8953340779838143365,
            'source_pixel_height': -6900878670881954600,
            'rotation': -2330944763305141729,
            'virtual_nw_x_pixel': -588948804,
            'virtual_nw_y_pixel': 1058024007,
            'virtual_width': 1959807082,
            'virtual_height': 938704881,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -4068140103946963012,

            'source_nw_y_pixel': -7477144951671405597,

            'source_pixel_width': -6402901629893758842,

            'source_pixel_height': -4152779461669793937,

            'rotation': -1492441891526889290,

            'virtual_nw_x_pixel': 498931154,

            'virtual_nw_y_pixel': -1014183769,

            'virtual_width': 1008030480,

            'virtual_height': -1939705944,

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
            'description': 'ťьΫрąήaϨϔӒśěҨԅҁɣŻĶζˬі\x9eíɅ҃ϯʮƻț\x9d',
            'monitors': [
                {
                    'identifier': 318913,
                    'width': -6043999489853227099,
                    'height': -6379020463485121474,
                },
                {
                    'identifier': 3196692,
                    'width': 2264478596217189970,
                    'height': -2522451821003877988,
                },
                {
                    'identifier': 1463421,
                    'width': -7266185215781283748,
                    'height': 4597081715666535756,
                },
                {
                    'identifier': 2721941,
                    'width': -256708620296143143,
                    'height': -8365139553355677179,
                },
                {
                    'identifier': 9054712,
                    'width': -8659299175884592677,
                    'height': -8498887750261579050,
                },
                {
                    'identifier': 9632282,
                    'width': -7184210461921058412,
                    'height': 1648512283824767424,
                },
                {
                    'identifier': 1976298,
                    'width': -1811276769667508717,
                    'height': 4316044625384769571,
                },
                {
                    'identifier': 3548504,
                    'width': -3386222467872813561,
                    'height': 9072578985070497379,
                },
                {
                    'identifier': 5464464,
                    'width': 4603587138769962273,
                    'height': -6330506231093779567,
                },
                {
                    'identifier': 7945500,
                    'width': -2700446539620575844,
                    'height': 9025605338309360895,
                },
            ],
            'screen': [
                {
                    'source_monitor': 4583817,
                    'source_nw_x_pixel': -5373968828005992732,
                    'source_nw_y_pixel': -1797398112372667227,
                    'source_pixel_width': -5296840044192887922,
                    'source_pixel_height': -8599563436971522456,
                    'rotation': -1722370825151326288,
                    'virtual_nw_x_pixel': 1014113290,
                    'virtual_nw_y_pixel': -1263267085,
                    'virtual_width': -355926038,
                    'virtual_height': 331280098,
                },
                {
                    'source_monitor': 9981962,
                    'source_nw_x_pixel': -7196923321893002957,
                    'source_nw_y_pixel': -8295239774478315528,
                    'source_pixel_width': -1165132830623077008,
                    'source_pixel_height': -4695410646861260797,
                    'rotation': -8479494821667070035,
                    'virtual_nw_x_pixel': 796183695,
                    'virtual_nw_y_pixel': 933666347,
                    'virtual_width': -826953726,
                    'virtual_height': 576518360,
                },
                {
                    'source_monitor': 6642875,
                    'source_nw_x_pixel': -2013763823474540796,
                    'source_nw_y_pixel': -3077773166050400235,
                    'source_pixel_width': -6444229519750791583,
                    'source_pixel_height': -1292900911537621182,
                    'rotation': -5848671784078771473,
                    'virtual_nw_x_pixel': 387002945,
                    'virtual_nw_y_pixel': 1988309806,
                    'virtual_width': 1214513506,
                    'virtual_height': 688122422,
                },
                {
                    'source_monitor': 7481671,
                    'source_nw_x_pixel': -2027667989724854068,
                    'source_nw_y_pixel': -3569845340427922579,
                    'source_pixel_width': -233550484399090862,
                    'source_pixel_height': -1998025157476064316,
                    'rotation': -198662000548257132,
                    'virtual_nw_x_pixel': -180122576,
                    'virtual_nw_y_pixel': -1654475890,
                    'virtual_width': 1096858339,
                    'virtual_height': 1494725438,
                },
                {
                    'source_monitor': 4878200,
                    'source_nw_x_pixel': -1003855944993877068,
                    'source_nw_y_pixel': -4139731717330691972,
                    'source_pixel_width': -160535352776970002,
                    'source_pixel_height': -5222578930732595593,
                    'rotation': -8306341073265422650,
                    'virtual_nw_x_pixel': -414178253,
                    'virtual_nw_y_pixel': -1559620940,
                    'virtual_width': 1389139773,
                    'virtual_height': 422220443,
                },
                {
                    'source_monitor': 5171361,
                    'source_nw_x_pixel': -2434404402484948583,
                    'source_nw_y_pixel': -7613510067148352039,
                    'source_pixel_width': -5848627789799701027,
                    'source_pixel_height': -7334559042727843623,
                    'rotation': -1942052384083459426,
                    'virtual_nw_x_pixel': 611983098,
                    'virtual_nw_y_pixel': 43129216,
                    'virtual_width': -500850861,
                    'virtual_height': -1449099274,
                },
                {
                    'source_monitor': 620995,
                    'source_nw_x_pixel': -773570114177872649,
                    'source_nw_y_pixel': -4666082316916809465,
                    'source_pixel_width': -7396190130586521877,
                    'source_pixel_height': -8985017155141237655,
                    'rotation': -6710373527092076051,
                    'virtual_nw_x_pixel': -1023603073,
                    'virtual_nw_y_pixel': -476155081,
                    'virtual_width': 1223582327,
                    'virtual_height': 316101334,
                },
                {
                    'source_monitor': 5683812,
                    'source_nw_x_pixel': -5432455199453436228,
                    'source_nw_y_pixel': -741927142552511778,
                    'source_pixel_width': -86293783956727485,
                    'source_pixel_height': -2279602489398733860,
                    'rotation': -9196196184102857546,
                    'virtual_nw_x_pixel': -600894507,
                    'virtual_nw_y_pixel': -1159821823,
                    'virtual_width': 1371346132,
                    'virtual_height': -678755956,
                },
                {
                    'source_monitor': 4907031,
                    'source_nw_x_pixel': -2457604056733774275,
                    'source_nw_y_pixel': -2318861132379743460,
                    'source_pixel_width': -934007706103122432,
                    'source_pixel_height': -5214310280399727075,
                    'rotation': -4139883913715215671,
                    'virtual_nw_x_pixel': 1008222530,
                    'virtual_nw_y_pixel': 1999436479,
                    'virtual_width': 384080474,
                    'virtual_height': -1968725710,
                },
                {
                    'source_monitor': 8114042,
                    'source_nw_x_pixel': -4561949961043228676,
                    'source_nw_y_pixel': -1975457923026900605,
                    'source_pixel_width': -4544238214072430304,
                    'source_pixel_height': -24572192953335868,
                    'rotation': -539164749105147418,
                    'virtual_nw_x_pixel': 1794726707,
                    'virtual_nw_y_pixel': -287676079,
                    'virtual_width': -214206152,
                    'virtual_height': -1066495206,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 8573196,
                    'width': 2544629148911758221,
                    'height': -2697097337602352993,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -3361920141341116663,
                    'source_nw_y_pixel': -9115442823741241162,
                    'source_pixel_width': -4202272637220139181,
                    'source_pixel_height': -5649780383657325016,
                    'rotation': -1188873000305051991,
                    'virtual_nw_x_pixel': 1944917816,
                    'virtual_nw_y_pixel': -1442869289,
                    'virtual_width': -1882822078,
                    'virtual_height': -248315973,
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
                    'description': 'Ѐʴɭ΄ɾ`Ҍϡ¡ʍːȎϏ\x94ӤõҲЉ[ʽʞƲǱ\x7fæёηҙԩ˽',
                    'monitors': [
                            {
                                        'identifier': 2212675,
                                        'width': -6152120957631527270,
                                        'height': -2826747672141573350,
                                    },
                            {
                                        'identifier': 860364,
                                        'width': -3009251881772902377,
                                        'height': 7468297817376694808,
                                    },
                            {
                                        'identifier': 294399,
                                        'width': -3754991472119603254,
                                        'height': 813581642993513730,
                                    },
                            {
                                        'identifier': 6610642,
                                        'width': -2046075409401807170,
                                        'height': -7996942072468196032,
                                    },
                            {
                                        'identifier': 7372978,
                                        'width': -1546189157602072727,
                                        'height': 6239058030724921470,
                                    },
                            {
                                        'identifier': 1012171,
                                        'width': -6970019588814856155,
                                        'height': -2876419039886162845,
                                    },
                            {
                                        'identifier': 7310725,
                                        'width': -8941177521777411699,
                                        'height': -6085168611710523042,
                                    },
                            {
                                        'identifier': 7485441,
                                        'width': -6198406524026933048,
                                        'height': -4006825587329922480,
                                    },
                            {
                                        'identifier': 5135911,
                                        'width': -4628392446192092398,
                                        'height': 725022795687997916,
                                    },
                            {
                                        'identifier': 7739701,
                                        'width': 5946583751036987198,
                                        'height': -8653486940126652685,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9296725,
                                        'source_nw_x_pixel': -5371115993276466429,
                                        'source_nw_y_pixel': -5051382172911147336,
                                        'source_pixel_width': -6504807128052099155,
                                        'source_pixel_height': -6144729183284868142,
                                        'rotation': -3651919565981908875,
                                        'virtual_nw_x_pixel': 1005571357,
                                        'virtual_nw_y_pixel': 1153744447,
                                        'virtual_width': -413191762,
                                        'virtual_height': 1036016912,
                                    },
                            {
                                        'source_monitor': 5422693,
                                        'source_nw_x_pixel': -1537404527996223859,
                                        'source_nw_y_pixel': -3404434258709975383,
                                        'source_pixel_width': -8232302655451488785,
                                        'source_pixel_height': -2098747386022844965,
                                        'rotation': -9182086194951912908,
                                        'virtual_nw_x_pixel': 1582771927,
                                        'virtual_nw_y_pixel': -377714089,
                                        'virtual_width': 1684503478,
                                        'virtual_height': -24663015,
                                    },
                            {
                                        'source_monitor': 6858603,
                                        'source_nw_x_pixel': -2478116048169127346,
                                        'source_nw_y_pixel': -6649254458551687642,
                                        'source_pixel_width': -2530179215070648171,
                                        'source_pixel_height': -2693169955324251170,
                                        'rotation': -5454771958008802808,
                                        'virtual_nw_x_pixel': 329279541,
                                        'virtual_nw_y_pixel': -1066742565,
                                        'virtual_width': -91924411,
                                        'virtual_height': 1776076765,
                                    },
                            {
                                        'source_monitor': 7487279,
                                        'source_nw_x_pixel': -948617088302648663,
                                        'source_nw_y_pixel': -1096851182842389208,
                                        'source_pixel_width': -535905041407374,
                                        'source_pixel_height': -5328903840161023733,
                                        'rotation': -7757848996006594757,
                                        'virtual_nw_x_pixel': -1572414271,
                                        'virtual_nw_y_pixel': 919671605,
                                        'virtual_width': 826911925,
                                        'virtual_height': 1381444020,
                                    },
                            {
                                        'source_monitor': 5769472,
                                        'source_nw_x_pixel': -6910202042198175047,
                                        'source_nw_y_pixel': -1723527782505750858,
                                        'source_pixel_width': -1955986864822760764,
                                        'source_pixel_height': -1865193426054237327,
                                        'rotation': -4253467569669406675,
                                        'virtual_nw_x_pixel': -1248149029,
                                        'virtual_nw_y_pixel': -783915150,
                                        'virtual_width': 1881060020,
                                        'virtual_height': -9873698,
                                    },
                            {
                                        'source_monitor': 3885071,
                                        'source_nw_x_pixel': -1540429580526818041,
                                        'source_nw_y_pixel': -3436565285650396516,
                                        'source_pixel_width': -3086609746284505435,
                                        'source_pixel_height': -9099720796902064148,
                                        'rotation': -6553897219957803054,
                                        'virtual_nw_x_pixel': 1494784180,
                                        'virtual_nw_y_pixel': 1414442520,
                                        'virtual_width': 1630886777,
                                        'virtual_height': -1741170691,
                                    },
                            {
                                        'source_monitor': 8236037,
                                        'source_nw_x_pixel': -3568512498644700852,
                                        'source_nw_y_pixel': -3472254467066842801,
                                        'source_pixel_width': -5333582746984882847,
                                        'source_pixel_height': -7359407164098585892,
                                        'rotation': -4170966718452709395,
                                        'virtual_nw_x_pixel': 1505839594,
                                        'virtual_nw_y_pixel': 1353904911,
                                        'virtual_width': 1712066769,
                                        'virtual_height': 601309419,
                                    },
                            {
                                        'source_monitor': 6074450,
                                        'source_nw_x_pixel': -3650715986554656721,
                                        'source_nw_y_pixel': -3062545169432273472,
                                        'source_pixel_width': -1680902053108008907,
                                        'source_pixel_height': -3997217108527984600,
                                        'rotation': -6070391263948996441,
                                        'virtual_nw_x_pixel': -1422368775,
                                        'virtual_nw_y_pixel': -232671385,
                                        'virtual_width': 1796167560,
                                        'virtual_height': 966235737,
                                    },
                            {
                                        'source_monitor': 9610856,
                                        'source_nw_x_pixel': -3808437144372181250,
                                        'source_nw_y_pixel': -1173719503163508946,
                                        'source_pixel_width': -8550853915889645887,
                                        'source_pixel_height': -3555447146289814513,
                                        'rotation': -4925673749194388043,
                                        'virtual_nw_x_pixel': 1251951100,
                                        'virtual_nw_y_pixel': 683411880,
                                        'virtual_width': -251535300,
                                        'virtual_height': -1833891048,
                                    },
                            {
                                        'source_monitor': 7173782,
                                        'source_nw_x_pixel': -1077210674712542263,
                                        'source_nw_y_pixel': -4192508591391948191,
                                        'source_pixel_width': -3803004479448527941,
                                        'source_pixel_height': -3565804539627774586,
                                        'rotation': -8505752373603689348,
                                        'virtual_nw_x_pixel': 1066006570,
                                        'virtual_nw_y_pixel': -1176416049,
                                        'virtual_width': 535463235,
                                        'virtual_height': 1059082828,
                                    },
                        ],
                },
                {
                    'description': 'ęʺҎѠ6Ԟʞӵ\xa0µʰȤpҕǰTsȄрÐ҈МɨѭɄҠtö}¼',
                    'monitors': [
                            {
                                        'identifier': 8014184,
                                        'width': -7193170355535374753,
                                        'height': 2778030336064652488,
                                    },
                            {
                                        'identifier': 4679116,
                                        'width': -108687636887948673,
                                        'height': 5189782149173325864,
                                    },
                            {
                                        'identifier': 3662345,
                                        'width': 1880398249629507083,
                                        'height': 2904322561255275735,
                                    },
                            {
                                        'identifier': 1446902,
                                        'width': -3337760126252535347,
                                        'height': 4424326479391188912,
                                    },
                            {
                                        'identifier': 9071349,
                                        'width': 2411856347441137087,
                                        'height': 9055879606971346324,
                                    },
                            {
                                        'identifier': 1298539,
                                        'width': -5229333980512388605,
                                        'height': -3632212521561933938,
                                    },
                            {
                                        'identifier': 9324382,
                                        'width': 7587436590272933733,
                                        'height': -3435533192351579993,
                                    },
                            {
                                        'identifier': 804082,
                                        'width': 996576490665959012,
                                        'height': 4272974529446893908,
                                    },
                            {
                                        'identifier': 4161590,
                                        'width': 7577700768133334430,
                                        'height': 6759283051909457813,
                                    },
                            {
                                        'identifier': 141366,
                                        'width': 1775727454750818653,
                                        'height': -3856322864752192937,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9411923,
                                        'source_nw_x_pixel': -1033262559502684955,
                                        'source_nw_y_pixel': -4628825588990731356,
                                        'source_pixel_width': -8408610399418897170,
                                        'source_pixel_height': -8572117410533759070,
                                        'rotation': -2178961698643598726,
                                        'virtual_nw_x_pixel': 846582881,
                                        'virtual_nw_y_pixel': 1707723994,
                                        'virtual_width': 96113202,
                                        'virtual_height': -776919715,
                                    },
                            {
                                        'source_monitor': 8114727,
                                        'source_nw_x_pixel': -1334465623247006354,
                                        'source_nw_y_pixel': -1218931142572694383,
                                        'source_pixel_width': -1211594121720030052,
                                        'source_pixel_height': -876756263772484145,
                                        'rotation': -1030342085456641642,
                                        'virtual_nw_x_pixel': 636798699,
                                        'virtual_nw_y_pixel': 1375313967,
                                        'virtual_width': -1944929725,
                                        'virtual_height': -607882668,
                                    },
                            {
                                        'source_monitor': 269989,
                                        'source_nw_x_pixel': -6553853619768540209,
                                        'source_nw_y_pixel': -3037306916371533343,
                                        'source_pixel_width': -7700559719149480758,
                                        'source_pixel_height': -321987692254747616,
                                        'rotation': -7913067309826736750,
                                        'virtual_nw_x_pixel': -1462870110,
                                        'virtual_nw_y_pixel': 328894034,
                                        'virtual_width': -1404567435,
                                        'virtual_height': -1715571218,
                                    },
                            {
                                        'source_monitor': 279818,
                                        'source_nw_x_pixel': -5732329316987631197,
                                        'source_nw_y_pixel': -5960413735663314409,
                                        'source_pixel_width': -7148908997688167331,
                                        'source_pixel_height': -684752738198553185,
                                        'rotation': -6536411870887165304,
                                        'virtual_nw_x_pixel': 365430040,
                                        'virtual_nw_y_pixel': 1182671135,
                                        'virtual_width': -725172270,
                                        'virtual_height': 788992704,
                                    },
                            {
                                        'source_monitor': 7184067,
                                        'source_nw_x_pixel': -2983868536260295927,
                                        'source_nw_y_pixel': -47417825814548427,
                                        'source_pixel_width': -4062017834692457752,
                                        'source_pixel_height': -1228188769052088970,
                                        'rotation': -2480344078604793675,
                                        'virtual_nw_x_pixel': 1510165696,
                                        'virtual_nw_y_pixel': -1649764358,
                                        'virtual_width': 580715922,
                                        'virtual_height': 1149040478,
                                    },
                            {
                                        'source_monitor': 8521743,
                                        'source_nw_x_pixel': -6073618631139711625,
                                        'source_nw_y_pixel': -4478526434713053219,
                                        'source_pixel_width': -7349161072718315053,
                                        'source_pixel_height': -2274289492297075115,
                                        'rotation': -5527615172007470154,
                                        'virtual_nw_x_pixel': -1816025460,
                                        'virtual_nw_y_pixel': -860810453,
                                        'virtual_width': 665419434,
                                        'virtual_height': -1014501596,
                                    },
                            {
                                        'source_monitor': 1027879,
                                        'source_nw_x_pixel': -3036522567322834054,
                                        'source_nw_y_pixel': -1085859753980725276,
                                        'source_pixel_width': -9155543610696617848,
                                        'source_pixel_height': -1001158848965390421,
                                        'rotation': -1972939016876452899,
                                        'virtual_nw_x_pixel': -1206725537,
                                        'virtual_nw_y_pixel': 623055020,
                                        'virtual_width': -1825781416,
                                        'virtual_height': -90037462,
                                    },
                            {
                                        'source_monitor': 8516020,
                                        'source_nw_x_pixel': -2099126640576070276,
                                        'source_nw_y_pixel': -1248045127039426979,
                                        'source_pixel_width': -2798592572612638999,
                                        'source_pixel_height': -6549149027761577188,
                                        'rotation': -1384109936185346061,
                                        'virtual_nw_x_pixel': -1256335650,
                                        'virtual_nw_y_pixel': -1813739183,
                                        'virtual_width': 395878808,
                                        'virtual_height': 1674981925,
                                    },
                            {
                                        'source_monitor': 2828084,
                                        'source_nw_x_pixel': -9059899707544962779,
                                        'source_nw_y_pixel': -7062835835694838306,
                                        'source_pixel_width': -1075298865789845545,
                                        'source_pixel_height': -4472724651092187471,
                                        'rotation': -7117951057324802476,
                                        'virtual_nw_x_pixel': 1061418605,
                                        'virtual_nw_y_pixel': 6218845,
                                        'virtual_width': -1741930265,
                                        'virtual_height': 297520190,
                                    },
                            {
                                        'source_monitor': 2734619,
                                        'source_nw_x_pixel': -4843922278630180882,
                                        'source_nw_y_pixel': -1811368677059967519,
                                        'source_pixel_width': -1787490647351515258,
                                        'source_pixel_height': -2078488886421380694,
                                        'rotation': -7482668532763441914,
                                        'virtual_nw_x_pixel': -871807979,
                                        'virtual_nw_y_pixel': 1516940592,
                                        'virtual_width': 1045591280,
                                        'virtual_height': -1996151743,
                                    },
                        ],
                },
                {
                    'description': 'ӉћμĖΐĸӆͱėʤĴȖiГņ҄ǫȓϑµƭЅʍÒ\x87ϛåʐќδ',
                    'monitors': [
                            {
                                        'identifier': 3810785,
                                        'width': -7195274202071992920,
                                        'height': -3043932265087932231,
                                    },
                            {
                                        'identifier': -927152,
                                        'width': 1952063794749946082,
                                        'height': -5854101234762233533,
                                    },
                            {
                                        'identifier': -688819,
                                        'width': -1679551265902417707,
                                        'height': -5903854697847586543,
                                    },
                            {
                                        'identifier': -646289,
                                        'width': 3022883868426207866,
                                        'height': 3801794368101487298,
                                    },
                            {
                                        'identifier': -460205,
                                        'width': 9192604682692808905,
                                        'height': -3271734339014631516,
                                    },
                            {
                                        'identifier': 2122182,
                                        'width': -340749392181742308,
                                        'height': 8554326317703238532,
                                    },
                            {
                                        'identifier': 5630506,
                                        'width': -1190144430635990018,
                                        'height': -5584364542336337854,
                                    },
                            {
                                        'identifier': 6641802,
                                        'width': -6979146090828791604,
                                        'height': 5604105387317618483,
                                    },
                            {
                                        'identifier': 7149137,
                                        'width': -7004465602384250097,
                                        'height': -4120448534163829211,
                                    },
                            {
                                        'identifier': 7590891,
                                        'width': -8244372904349220939,
                                        'height': -3565047685609307714,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5824419,
                                        'source_nw_x_pixel': -6215927657218729043,
                                        'source_nw_y_pixel': -593148708568580559,
                                        'source_pixel_width': -324597476944176484,
                                        'source_pixel_height': -285357736877726835,
                                        'rotation': -1334035083195923891,
                                        'virtual_nw_x_pixel': -1492405441,
                                        'virtual_nw_y_pixel': 1994560977,
                                        'virtual_width': -1456895463,
                                        'virtual_height': 867499186,
                                    },
                            {
                                        'source_monitor': 4659413,
                                        'source_nw_x_pixel': -1051088698014682580,
                                        'source_nw_y_pixel': -7071022673294343060,
                                        'source_pixel_width': -3991074551807500553,
                                        'source_pixel_height': -123553926751554746,
                                        'rotation': -4422594186715240399,
                                        'virtual_nw_x_pixel': 734655628,
                                        'virtual_nw_y_pixel': -426165268,
                                        'virtual_width': 378966676,
                                        'virtual_height': 720468302,
                                    },
                            {
                                        'source_monitor': 4182462,
                                        'source_nw_x_pixel': -1729593352539777294,
                                        'source_nw_y_pixel': -5010238217569619121,
                                        'source_pixel_width': -2351209969495632650,
                                        'source_pixel_height': -8312139362956345219,
                                        'rotation': -5892115554154031744,
                                        'virtual_nw_x_pixel': 112618028,
                                        'virtual_nw_y_pixel': 1094913736,
                                        'virtual_width': -1544120084,
                                        'virtual_height': -1618918068,
                                    },
                            {
                                        'source_monitor': 5572154,
                                        'source_nw_x_pixel': -310141270301988207,
                                        'source_nw_y_pixel': -2823814074689392413,
                                        'source_pixel_width': -4717001467206473032,
                                        'source_pixel_height': -7366194430935581575,
                                        'rotation': -6025470909506627766,
                                        'virtual_nw_x_pixel': -637375060,
                                        'virtual_nw_y_pixel': 1304121728,
                                        'virtual_width': -255535722,
                                        'virtual_height': -722325365,
                                    },
                            {
                                        'source_monitor': -78266,
                                        'source_nw_x_pixel': -4264784089321329933,
                                        'source_nw_y_pixel': -4567634072786026039,
                                        'source_pixel_width': -6094178342364599398,
                                        'source_pixel_height': -3840282768344526295,
                                        'rotation': -2509064063156371697,
                                        'virtual_nw_x_pixel': 177901121,
                                        'virtual_nw_y_pixel': -598830656,
                                        'virtual_width': 686817487,
                                        'virtual_height': -1848809731,
                                    },
                            {
                                        'source_monitor': 2878350,
                                        'source_nw_x_pixel': -2554809113368908453,
                                        'source_nw_y_pixel': -1275285734546292649,
                                        'source_pixel_width': -4976122240679076643,
                                        'source_pixel_height': -8306640228950432456,
                                        'rotation': -6390488251057102608,
                                        'virtual_nw_x_pixel': 935262848,
                                        'virtual_nw_y_pixel': 1601610607,
                                        'virtual_width': -391080742,
                                        'virtual_height': 1997888276,
                                    },
                            {
                                        'source_monitor': -525654,
                                        'source_nw_x_pixel': -7788480641633090287,
                                        'source_nw_y_pixel': -8149376644347295216,
                                        'source_pixel_width': -9217392180421305243,
                                        'source_pixel_height': -6265367712040705251,
                                        'rotation': -2186715504984539493,
                                        'virtual_nw_x_pixel': -30802995,
                                        'virtual_nw_y_pixel': 937491184,
                                        'virtual_width': -1496280772,
                                        'virtual_height': -291477761,
                                    },
                            {
                                        'source_monitor': 4383673,
                                        'source_nw_x_pixel': -4772438732125430570,
                                        'source_nw_y_pixel': -2684740810463181687,
                                        'source_pixel_width': -3209820215680662622,
                                        'source_pixel_height': -2397857677136780529,
                                        'rotation': -8802139039793376600,
                                        'virtual_nw_x_pixel': 502931000,
                                        'virtual_nw_y_pixel': -1023898653,
                                        'virtual_width': -1760520460,
                                        'virtual_height': 769518924,
                                    },
                            {
                                        'source_monitor': 4158332,
                                        'source_nw_x_pixel': -1707749252169297225,
                                        'source_nw_y_pixel': -9015673721238849512,
                                        'source_pixel_width': -3830698985734019959,
                                        'source_pixel_height': -935577861323859973,
                                        'rotation': -7756822305520802774,
                                        'virtual_nw_x_pixel': -1540301391,
                                        'virtual_nw_y_pixel': 13141942,
                                        'virtual_width': -1749519815,
                                        'virtual_height': 49617502,
                                    },
                            {
                                        'source_monitor': 6714501,
                                        'source_nw_x_pixel': -6912133522664658599,
                                        'source_nw_y_pixel': -6223306004218685594,
                                        'source_pixel_width': -7116078516049176746,
                                        'source_pixel_height': -1117959928868327680,
                                        'rotation': -4258770436866246587,
                                        'virtual_nw_x_pixel': -1143967966,
                                        'virtual_nw_y_pixel': -950549406,
                                        'virtual_width': -1098932272,
                                        'virtual_height': -249717725,
                                    },
                        ],
                },
                {
                    'description': 'ϔЛϯͽҁ\x84\x98°ӾÌбȖǜӚ\u038dԥʃпę˯ǿϧʺÓϞǋМ˻ϋé',
                    'monitors': [
                            {
                                        'identifier': 2455108,
                                        'width': -1659102289280016060,
                                        'height': -8247859739229866803,
                                    },
                            {
                                        'identifier': -54615,
                                        'width': -7293447058350000696,
                                        'height': -4530839378320208884,
                                    },
                            {
                                        'identifier': 1275725,
                                        'width': -1641538127510522995,
                                        'height': 7255688354188301443,
                                    },
                            {
                                        'identifier': 3650617,
                                        'width': -5472330164198766111,
                                        'height': -2127832913563196367,
                                    },
                            {
                                        'identifier': 6847795,
                                        'width': 6555183631069748376,
                                        'height': 7414745692327882689,
                                    },
                            {
                                        'identifier': 7889281,
                                        'width': 6636296282640125187,
                                        'height': -6969678979371257833,
                                    },
                            {
                                        'identifier': 4962485,
                                        'width': -2939938219797046808,
                                        'height': -8250318854035160937,
                                    },
                            {
                                        'identifier': 3388162,
                                        'width': 4539124435258078248,
                                        'height': -3407425127380257674,
                                    },
                            {
                                        'identifier': 9257544,
                                        'width': -9140341172833317272,
                                        'height': 1185004500878529431,
                                    },
                            {
                                        'identifier': 3665899,
                                        'width': 4908810812154060352,
                                        'height': 6192367543188332259,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7194194,
                                        'source_nw_x_pixel': -8158921532870736245,
                                        'source_nw_y_pixel': -1515268092104808746,
                                        'source_pixel_width': -6058600452259059642,
                                        'source_pixel_height': -700973263713330265,
                                        'rotation': -385851218452717036,
                                        'virtual_nw_x_pixel': 68754970,
                                        'virtual_nw_y_pixel': -531373190,
                                        'virtual_width': 270680778,
                                        'virtual_height': -228340418,
                                    },
                            {
                                        'source_monitor': -909545,
                                        'source_nw_x_pixel': -7424961068091428761,
                                        'source_nw_y_pixel': -7709088906276811910,
                                        'source_pixel_width': -3382602186809877942,
                                        'source_pixel_height': -5624785316037752411,
                                        'rotation': -1790699044909841049,
                                        'virtual_nw_x_pixel': -714690169,
                                        'virtual_nw_y_pixel': 1979903417,
                                        'virtual_width': -1311045911,
                                        'virtual_height': -346670084,
                                    },
                            {
                                        'source_monitor': 104369,
                                        'source_nw_x_pixel': -2671153411248761702,
                                        'source_nw_y_pixel': -8382227908175807769,
                                        'source_pixel_width': -511615086844382379,
                                        'source_pixel_height': -2513398012555917099,
                                        'rotation': -2728764303411947570,
                                        'virtual_nw_x_pixel': 1669044363,
                                        'virtual_nw_y_pixel': 1702357637,
                                        'virtual_width': 455911342,
                                        'virtual_height': -1607895695,
                                    },
                            {
                                        'source_monitor': 1760771,
                                        'source_nw_x_pixel': -5006981414038519988,
                                        'source_nw_y_pixel': -275287451973938080,
                                        'source_pixel_width': -9035742295545696062,
                                        'source_pixel_height': -7694422831859077055,
                                        'rotation': -2995185641417909687,
                                        'virtual_nw_x_pixel': -1408956481,
                                        'virtual_nw_y_pixel': -158286146,
                                        'virtual_width': 395610044,
                                        'virtual_height': 348224425,
                                    },
                            {
                                        'source_monitor': 3975402,
                                        'source_nw_x_pixel': -7632249976350441226,
                                        'source_nw_y_pixel': -1497795660000096686,
                                        'source_pixel_width': -8038963302305550759,
                                        'source_pixel_height': -7670259977353837700,
                                        'rotation': -555402824602574081,
                                        'virtual_nw_x_pixel': 170178318,
                                        'virtual_nw_y_pixel': 1156217315,
                                        'virtual_width': -350490064,
                                        'virtual_height': -1057119680,
                                    },
                            {
                                        'source_monitor': 5520229,
                                        'source_nw_x_pixel': -2973459777868758415,
                                        'source_nw_y_pixel': -4328750550517922066,
                                        'source_pixel_width': -1223624561583881451,
                                        'source_pixel_height': -5682082964668437482,
                                        'rotation': -4624264769831673966,
                                        'virtual_nw_x_pixel': 939586391,
                                        'virtual_nw_y_pixel': -254761062,
                                        'virtual_width': 956866841,
                                        'virtual_height': 502641302,
                                    },
                            {
                                        'source_monitor': 6124560,
                                        'source_nw_x_pixel': -3428445170491469569,
                                        'source_nw_y_pixel': -2282841482665879300,
                                        'source_pixel_width': -4918141528734231396,
                                        'source_pixel_height': -2723684838958005230,
                                        'rotation': -3506366377581283615,
                                        'virtual_nw_x_pixel': 1438130744,
                                        'virtual_nw_y_pixel': -286099047,
                                        'virtual_width': -482806542,
                                        'virtual_height': -1737527464,
                                    },
                            {
                                        'source_monitor': 1157802,
                                        'source_nw_x_pixel': -1566089570552300444,
                                        'source_nw_y_pixel': -6253917404963824642,
                                        'source_pixel_width': -3502601387912822361,
                                        'source_pixel_height': -7860627018897933106,
                                        'rotation': -1207648527020754293,
                                        'virtual_nw_x_pixel': 964108884,
                                        'virtual_nw_y_pixel': -467276973,
                                        'virtual_width': 209767683,
                                        'virtual_height': -1650585198,
                                    },
                            {
                                        'source_monitor': 7251319,
                                        'source_nw_x_pixel': -7358420984565085837,
                                        'source_nw_y_pixel': -708353426099189149,
                                        'source_pixel_width': -1255231234396930448,
                                        'source_pixel_height': -4414968736363034545,
                                        'rotation': -5498454822794681417,
                                        'virtual_nw_x_pixel': 1119928819,
                                        'virtual_nw_y_pixel': 1583070704,
                                        'virtual_width': -660300804,
                                        'virtual_height': -140056793,
                                    },
                            {
                                        'source_monitor': -787043,
                                        'source_nw_x_pixel': -1965554864491592845,
                                        'source_nw_y_pixel': -7610377064908322353,
                                        'source_pixel_width': -3437260407208017500,
                                        'source_pixel_height': -129473750696400382,
                                        'rotation': -8687053189483523345,
                                        'virtual_nw_x_pixel': -1413449162,
                                        'virtual_nw_y_pixel': -1717796387,
                                        'virtual_width': -141987636,
                                        'virtual_height': -458137488,
                                    },
                        ],
                },
                {
                    'description': '',
                    'monitors': [
                            {
                                        'identifier': 3750837,
                                        'width': -5656102431178022452,
                                        'height': 2895724563278017355,
                                    },
                            {
                                        'identifier': 1742457,
                                        'width': 3153580214620270902,
                                        'height': -7795837645670959706,
                                    },
                            {
                                        'identifier': 5768448,
                                        'width': 1698617388229269166,
                                        'height': 5507030870720645878,
                                    },
                            {
                                        'identifier': 7293400,
                                        'width': -7548847904141392808,
                                        'height': 6845233153730838507,
                                    },
                            {
                                        'identifier': 3012415,
                                        'width': -3774589237063703709,
                                        'height': -5042586064720235852,
                                    },
                            {
                                        'identifier': 4127168,
                                        'width': -4118250843554670573,
                                        'height': 3830549326670294888,
                                    },
                            {
                                        'identifier': 734560,
                                        'width': 4736379518254412502,
                                        'height': 4056529087041150168,
                                    },
                            {
                                        'identifier': 1338020,
                                        'width': 6102737495531242971,
                                        'height': -7868573043859744999,
                                    },
                            {
                                        'identifier': 5819968,
                                        'width': 4003033471366163159,
                                        'height': 5390706815559592725,
                                    },
                            {
                                        'identifier': 7423715,
                                        'width': 5228351666559815497,
                                        'height': -2854463667816148224,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5993740,
                                        'source_nw_x_pixel': -1849421810398568513,
                                        'source_nw_y_pixel': -9202908352082238576,
                                        'source_pixel_width': -2875690962157345039,
                                        'source_pixel_height': -7527233202701896883,
                                        'rotation': -4988649594648056449,
                                        'virtual_nw_x_pixel': -1240475494,
                                        'virtual_nw_y_pixel': -689431856,
                                        'virtual_width': 1510518175,
                                        'virtual_height': 1249234883,
                                    },
                            {
                                        'source_monitor': 8412686,
                                        'source_nw_x_pixel': -1550506076051532899,
                                        'source_nw_y_pixel': -5000130804090872214,
                                        'source_pixel_width': -4978482821345270889,
                                        'source_pixel_height': -8368245217742091537,
                                        'rotation': -3033548619840838925,
                                        'virtual_nw_x_pixel': 975947981,
                                        'virtual_nw_y_pixel': 1258602916,
                                        'virtual_width': 1170476398,
                                        'virtual_height': -1906820105,
                                    },
                            {
                                        'source_monitor': 7663427,
                                        'source_nw_x_pixel': -3515150153881539046,
                                        'source_nw_y_pixel': -6727858185001393047,
                                        'source_pixel_width': -3925618058999664136,
                                        'source_pixel_height': -3166394439610936111,
                                        'rotation': -5990043782320376299,
                                        'virtual_nw_x_pixel': 1925996115,
                                        'virtual_nw_y_pixel': -1086479823,
                                        'virtual_width': 1103705317,
                                        'virtual_height': -744482980,
                                    },
                            {
                                        'source_monitor': 3666201,
                                        'source_nw_x_pixel': -1207844956212245149,
                                        'source_nw_y_pixel': -6049331694254491989,
                                        'source_pixel_width': -24718927166146619,
                                        'source_pixel_height': -5668682483959554870,
                                        'rotation': -1575983386059518159,
                                        'virtual_nw_x_pixel': 489758998,
                                        'virtual_nw_y_pixel': -1341342669,
                                        'virtual_width': -369601589,
                                        'virtual_height': -387194141,
                                    },
                            {
                                        'source_monitor': 6543009,
                                        'source_nw_x_pixel': -5266200784849571989,
                                        'source_nw_y_pixel': -7846124620066067231,
                                        'source_pixel_width': -6815334140232235349,
                                        'source_pixel_height': -1732538448375180009,
                                        'rotation': -2981268817156772319,
                                        'virtual_nw_x_pixel': 1474675416,
                                        'virtual_nw_y_pixel': 1064878073,
                                        'virtual_width': 1565883956,
                                        'virtual_height': -644612431,
                                    },
                            {
                                        'source_monitor': 8323138,
                                        'source_nw_x_pixel': -3439452375896782231,
                                        'source_nw_y_pixel': -1828339778967098535,
                                        'source_pixel_width': -2757509312715865520,
                                        'source_pixel_height': -5335257524737906412,
                                        'rotation': -474123781146072354,
                                        'virtual_nw_x_pixel': -1722296509,
                                        'virtual_nw_y_pixel': -1355547440,
                                        'virtual_width': 99699452,
                                        'virtual_height': -432738988,
                                    },
                            {
                                        'source_monitor': 3336047,
                                        'source_nw_x_pixel': -8773117753559274237,
                                        'source_nw_y_pixel': -8767448270647218343,
                                        'source_pixel_width': -7797969964070723797,
                                        'source_pixel_height': -6271046186969162302,
                                        'rotation': -8136375096885295081,
                                        'virtual_nw_x_pixel': -367507246,
                                        'virtual_nw_y_pixel': -1642049369,
                                        'virtual_width': -917101737,
                                        'virtual_height': -186146662,
                                    },
                            {
                                        'source_monitor': 7074634,
                                        'source_nw_x_pixel': -2174772876595705000,
                                        'source_nw_y_pixel': -126604934428607629,
                                        'source_pixel_width': -6669586786371412994,
                                        'source_pixel_height': -7542448595844418093,
                                        'rotation': -6337577791567477653,
                                        'virtual_nw_x_pixel': 1996336889,
                                        'virtual_nw_y_pixel': 708567455,
                                        'virtual_width': 1441531497,
                                        'virtual_height': 304415370,
                                    },
                            {
                                        'source_monitor': 2961122,
                                        'source_nw_x_pixel': -2055900083399507395,
                                        'source_nw_y_pixel': -3618129316989892255,
                                        'source_pixel_width': -5704589343893277753,
                                        'source_pixel_height': -6156761707430509280,
                                        'rotation': -7187742588999467945,
                                        'virtual_nw_x_pixel': 150112076,
                                        'virtual_nw_y_pixel': -286904761,
                                        'virtual_width': -1602537884,
                                        'virtual_height': 1681248666,
                                    },
                            {
                                        'source_monitor': 9255218,
                                        'source_nw_x_pixel': -9082507995090332172,
                                        'source_nw_y_pixel': -2923156535487381508,
                                        'source_pixel_width': -8060188115673527976,
                                        'source_pixel_height': -1063030194249337015,
                                        'rotation': -2612224366715709203,
                                        'virtual_nw_x_pixel': -379297719,
                                        'virtual_nw_y_pixel': -1446685066,
                                        'virtual_width': 220269168,
                                        'virtual_height': 165948249,
                                    },
                        ],
                },
                {
                    'description': 'ҦϧZӎD҅!Öʣ^ҾЋӍɯsƻgǩȕфҹɷȡ«ûǧ9żуŴ',
                    'monitors': [
                            {
                                        'identifier': 2616726,
                                        'width': -3813998582165618501,
                                        'height': -5251845561980240245,
                                    },
                            {
                                        'identifier': 2896493,
                                        'width': -3261285712615837371,
                                        'height': 2166971007504767362,
                                    },
                            {
                                        'identifier': 1088739,
                                        'width': 4047527154025641163,
                                        'height': 8211500099174059476,
                                    },
                            {
                                        'identifier': 1218364,
                                        'width': 9130539830149880788,
                                        'height': 7347403197824886419,
                                    },
                            {
                                        'identifier': 8616714,
                                        'width': 660773001615422296,
                                        'height': 2732787484796498347,
                                    },
                            {
                                        'identifier': 9497926,
                                        'width': 5395787287450854630,
                                        'height': 1899465990284162075,
                                    },
                            {
                                        'identifier': 7866614,
                                        'width': 8359845565584952698,
                                        'height': 322684423771720007,
                                    },
                            {
                                        'identifier': 7419602,
                                        'width': -687685198423424137,
                                        'height': 5154483211774669786,
                                    },
                            {
                                        'identifier': 2426615,
                                        'width': -2061622024268790573,
                                        'height': 7992388033202908211,
                                    },
                            {
                                        'identifier': 2960294,
                                        'width': -6639877598804220446,
                                        'height': 6815037151919114677,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 54689,
                                        'source_nw_x_pixel': -8134262943862713532,
                                        'source_nw_y_pixel': -6776534305991987069,
                                        'source_pixel_width': -3319362983908565669,
                                        'source_pixel_height': -2739680847961931929,
                                        'rotation': -8236499433541190051,
                                        'virtual_nw_x_pixel': 84011298,
                                        'virtual_nw_y_pixel': 1766580999,
                                        'virtual_width': 469314683,
                                        'virtual_height': 1735219504,
                                    },
                            {
                                        'source_monitor': 5314141,
                                        'source_nw_x_pixel': -3737558570914018065,
                                        'source_nw_y_pixel': -4746382932955834236,
                                        'source_pixel_width': -2353173167151547110,
                                        'source_pixel_height': -2944162349068790117,
                                        'rotation': -7686099903144671891,
                                        'virtual_nw_x_pixel': 276542329,
                                        'virtual_nw_y_pixel': 457886638,
                                        'virtual_width': 680851053,
                                        'virtual_height': -83549896,
                                    },
                            {
                                        'source_monitor': 481570,
                                        'source_nw_x_pixel': -8624980439847472041,
                                        'source_nw_y_pixel': -4946800207712900790,
                                        'source_pixel_width': -507121489006601359,
                                        'source_pixel_height': -6484888423960668930,
                                        'rotation': -4501509429427985412,
                                        'virtual_nw_x_pixel': 1974092769,
                                        'virtual_nw_y_pixel': 1400598921,
                                        'virtual_width': 1696421448,
                                        'virtual_height': -1950652786,
                                    },
                            {
                                        'source_monitor': 7654738,
                                        'source_nw_x_pixel': -408537656766570621,
                                        'source_nw_y_pixel': -828145741649289815,
                                        'source_pixel_width': -8306765803647179843,
                                        'source_pixel_height': -5808772503306632352,
                                        'rotation': -5462636217438811515,
                                        'virtual_nw_x_pixel': 125201164,
                                        'virtual_nw_y_pixel': 1940659942,
                                        'virtual_width': -401241711,
                                        'virtual_height': -1104456141,
                                    },
                            {
                                        'source_monitor': 6861986,
                                        'source_nw_x_pixel': -2779340985875317272,
                                        'source_nw_y_pixel': -7017337662532067471,
                                        'source_pixel_width': -8031932760332238359,
                                        'source_pixel_height': -5772226019113470642,
                                        'rotation': -2666002750790795941,
                                        'virtual_nw_x_pixel': 1518985142,
                                        'virtual_nw_y_pixel': 1685569799,
                                        'virtual_width': 638487388,
                                        'virtual_height': -699288659,
                                    },
                            {
                                        'source_monitor': 4421031,
                                        'source_nw_x_pixel': -6027357841653576620,
                                        'source_nw_y_pixel': -5995082536772180987,
                                        'source_pixel_width': -5184422528138574617,
                                        'source_pixel_height': -405566988905791164,
                                        'rotation': -6437988029292508760,
                                        'virtual_nw_x_pixel': -231831585,
                                        'virtual_nw_y_pixel': -711070128,
                                        'virtual_width': -301243564,
                                        'virtual_height': -90168793,
                                    },
                            {
                                        'source_monitor': 689668,
                                        'source_nw_x_pixel': -998157594106193083,
                                        'source_nw_y_pixel': -3255927748891299001,
                                        'source_pixel_width': -4784865275619075088,
                                        'source_pixel_height': -3512133533173885381,
                                        'rotation': -995304629955323148,
                                        'virtual_nw_x_pixel': 1625340854,
                                        'virtual_nw_y_pixel': 1430185669,
                                        'virtual_width': -652486871,
                                        'virtual_height': -203688552,
                                    },
                            {
                                        'source_monitor': 7199079,
                                        'source_nw_x_pixel': -6357252223593151037,
                                        'source_nw_y_pixel': -5899530945492939892,
                                        'source_pixel_width': -7335925896962119234,
                                        'source_pixel_height': -957457005301146305,
                                        'rotation': -8983137158033210273,
                                        'virtual_nw_x_pixel': 101923336,
                                        'virtual_nw_y_pixel': -456383696,
                                        'virtual_width': -1858896827,
                                        'virtual_height': 147619441,
                                    },
                            {
                                        'source_monitor': 6042305,
                                        'source_nw_x_pixel': -1721029845306538252,
                                        'source_nw_y_pixel': -6875406745536760127,
                                        'source_pixel_width': -7080340853578608487,
                                        'source_pixel_height': -6004978101131968005,
                                        'rotation': -7705699605171857534,
                                        'virtual_nw_x_pixel': -513616397,
                                        'virtual_nw_y_pixel': -488597090,
                                        'virtual_width': 256814263,
                                        'virtual_height': -1332597222,
                                    },
                            {
                                        'source_monitor': 9104928,
                                        'source_nw_x_pixel': -700495755660962990,
                                        'source_nw_y_pixel': -6505047122822255785,
                                        'source_pixel_width': -7714910015859317939,
                                        'source_pixel_height': -574625381558020044,
                                        'rotation': -31354708748652786,
                                        'virtual_nw_x_pixel': -518496825,
                                        'virtual_nw_y_pixel': -607174052,
                                        'virtual_width': -1176857595,
                                        'virtual_height': -605290623,
                                    },
                        ],
                },
                {
                    'description': 'Ԕ`-\x8bȟΒƹʬvȢʷœˑǛҫЩ.ѨŔʋΞÑѵȉԢϷΖƐӄЍ',
                    'monitors': [
                            {
                                        'identifier': 2860410,
                                        'width': 8224881605182628022,
                                        'height': -5667305706348556103,
                                    },
                            {
                                        'identifier': 9158345,
                                        'width': 6562753194425848546,
                                        'height': -7067178077969450810,
                                    },
                            {
                                        'identifier': 2513319,
                                        'width': -3608446786615603711,
                                        'height': -6947444062461111940,
                                    },
                            {
                                        'identifier': 4417675,
                                        'width': -1898334888501643912,
                                        'height': -6026563796294667043,
                                    },
                            {
                                        'identifier': 3697809,
                                        'width': 8366697314492499376,
                                        'height': 3418455044630980381,
                                    },
                            {
                                        'identifier': 773168,
                                        'width': 7353953645691623878,
                                        'height': 1591845055799605204,
                                    },
                            {
                                        'identifier': 5106230,
                                        'width': 4503119122712669650,
                                        'height': -411581609962035282,
                                    },
                            {
                                        'identifier': 4699116,
                                        'width': -4265774936586180017,
                                        'height': 1687751296666713940,
                                    },
                            {
                                        'identifier': 5222531,
                                        'width': 1940773072655614054,
                                        'height': -3027323881244357145,
                                    },
                            {
                                        'identifier': 1666458,
                                        'width': 6305200087514773924,
                                        'height': -481794773840768568,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6684469,
                                        'source_nw_x_pixel': -1249980918193479664,
                                        'source_nw_y_pixel': -3740243720842421178,
                                        'source_pixel_width': -1822008840095335021,
                                        'source_pixel_height': -2442504417516675425,
                                        'rotation': -9031644943656236993,
                                        'virtual_nw_x_pixel': -1378273207,
                                        'virtual_nw_y_pixel': -1209773274,
                                        'virtual_width': 1722831045,
                                        'virtual_height': -1815570220,
                                    },
                            {
                                        'source_monitor': 1179014,
                                        'source_nw_x_pixel': -1510564063449518484,
                                        'source_nw_y_pixel': -4372887212078926741,
                                        'source_pixel_width': -5051078234732182234,
                                        'source_pixel_height': -7435704629952890254,
                                        'rotation': -5934203766145562117,
                                        'virtual_nw_x_pixel': 690396608,
                                        'virtual_nw_y_pixel': -491992418,
                                        'virtual_width': -1115665849,
                                        'virtual_height': 1297722234,
                                    },
                            {
                                        'source_monitor': 6567367,
                                        'source_nw_x_pixel': -9074167354400271934,
                                        'source_nw_y_pixel': -8958036541107841431,
                                        'source_pixel_width': -2031228443321295952,
                                        'source_pixel_height': -2607056128652924408,
                                        'rotation': -1080118268034832586,
                                        'virtual_nw_x_pixel': 1423241843,
                                        'virtual_nw_y_pixel': 12748229,
                                        'virtual_width': 1649445428,
                                        'virtual_height': -587400118,
                                    },
                            {
                                        'source_monitor': -551332,
                                        'source_nw_x_pixel': -4593252206040761200,
                                        'source_nw_y_pixel': -8526920898257949861,
                                        'source_pixel_width': -880697657311222076,
                                        'source_pixel_height': -5999791985651601962,
                                        'rotation': -1455324006110188075,
                                        'virtual_nw_x_pixel': 859180550,
                                        'virtual_nw_y_pixel': 725525757,
                                        'virtual_width': 533280552,
                                        'virtual_height': 342056209,
                                    },
                            {
                                        'source_monitor': 670135,
                                        'source_nw_x_pixel': -2781986408985914992,
                                        'source_nw_y_pixel': -7196731272204113650,
                                        'source_pixel_width': -5463750934226506327,
                                        'source_pixel_height': -7725344920361393227,
                                        'rotation': -6948584541169640919,
                                        'virtual_nw_x_pixel': -1693087003,
                                        'virtual_nw_y_pixel': 1969969096,
                                        'virtual_width': -1195121734,
                                        'virtual_height': -1445791165,
                                    },
                            {
                                        'source_monitor': 7356993,
                                        'source_nw_x_pixel': -339709529069562994,
                                        'source_nw_y_pixel': -2759929660374965760,
                                        'source_pixel_width': -3819374517791615619,
                                        'source_pixel_height': -9083009818272368524,
                                        'rotation': -3930755403188717442,
                                        'virtual_nw_x_pixel': 1647458528,
                                        'virtual_nw_y_pixel': -1584778572,
                                        'virtual_width': 13889482,
                                        'virtual_height': 774886287,
                                    },
                            {
                                        'source_monitor': 1373979,
                                        'source_nw_x_pixel': -1758165036190186411,
                                        'source_nw_y_pixel': -2216030605694747611,
                                        'source_pixel_width': -5845350218215120253,
                                        'source_pixel_height': -7538274579236075412,
                                        'rotation': -6031533133864747754,
                                        'virtual_nw_x_pixel': 939919501,
                                        'virtual_nw_y_pixel': -757482794,
                                        'virtual_width': 590759836,
                                        'virtual_height': -592471743,
                                    },
                            {
                                        'source_monitor': 1902262,
                                        'source_nw_x_pixel': -2862960176838075429,
                                        'source_nw_y_pixel': -6646717722319102242,
                                        'source_pixel_width': -6603780306364809305,
                                        'source_pixel_height': -4073352398754803409,
                                        'rotation': -5202316761773306889,
                                        'virtual_nw_x_pixel': -1184647870,
                                        'virtual_nw_y_pixel': 208625722,
                                        'virtual_width': 1790999921,
                                        'virtual_height': -1716611110,
                                    },
                            {
                                        'source_monitor': 4775879,
                                        'source_nw_x_pixel': -369142044726519008,
                                        'source_nw_y_pixel': -2416946040452384620,
                                        'source_pixel_width': -3229525121553577606,
                                        'source_pixel_height': -4692336277436322766,
                                        'rotation': -8682049425312812758,
                                        'virtual_nw_x_pixel': -618470674,
                                        'virtual_nw_y_pixel': 310056607,
                                        'virtual_width': -595836395,
                                        'virtual_height': 1318814215,
                                    },
                            {
                                        'source_monitor': 820332,
                                        'source_nw_x_pixel': -845047731735624573,
                                        'source_nw_y_pixel': -518085534925132088,
                                        'source_pixel_width': -4811571842867145545,
                                        'source_pixel_height': -2345249720285278904,
                                        'rotation': -9101965011878121780,
                                        'virtual_nw_x_pixel': 936591471,
                                        'virtual_nw_y_pixel': 978226321,
                                        'virtual_width': -926302774,
                                        'virtual_height': 375263915,
                                    },
                        ],
                },
                {
                    'description': '\xa0\u038bΓ˺ȋԚɛʀƕǶ=Ğǐ\x99ŅԋӜ\x8cИĻϹn',
                    'monitors': [
                            {
                                        'identifier': -735231,
                                        'width': -4981512174807996439,
                                        'height': 6596385818020024081,
                                    },
                            {
                                        'identifier': 7809095,
                                        'width': 2569670935091857351,
                                        'height': -7085286621063300771,
                                    },
                            {
                                        'identifier': 5555702,
                                        'width': 3846046648716262353,
                                        'height': -7135870835866588060,
                                    },
                            {
                                        'identifier': -62524,
                                        'width': 5555385141007830961,
                                        'height': 5450752231030019737,
                                    },
                            {
                                        'identifier': 1186189,
                                        'width': 5596900942267631337,
                                        'height': -2793439922617638782,
                                    },
                            {
                                        'identifier': 8665187,
                                        'width': 2506289961555081304,
                                        'height': 142250269654005159,
                                    },
                            {
                                        'identifier': 9592009,
                                        'width': -1757029450005900639,
                                        'height': -1078360034401224935,
                                    },
                            {
                                        'identifier': 7450949,
                                        'width': 7310996914999414065,
                                        'height': 4411744030775509122,
                                    },
                            {
                                        'identifier': 6881630,
                                        'width': -1662496391152266425,
                                        'height': 438312645762565113,
                                    },
                            {
                                        'identifier': -578650,
                                        'width': 3373620504552788580,
                                        'height': -8710262836732721035,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6625684,
                                        'source_nw_x_pixel': -8511624629897219828,
                                        'source_nw_y_pixel': -5870268048515364983,
                                        'source_pixel_width': -3388224657616123025,
                                        'source_pixel_height': -1536327474189047323,
                                        'rotation': -8159072952761637746,
                                        'virtual_nw_x_pixel': -1775733260,
                                        'virtual_nw_y_pixel': 337855329,
                                        'virtual_width': 150608017,
                                        'virtual_height': -549558026,
                                    },
                            {
                                        'source_monitor': 9203148,
                                        'source_nw_x_pixel': -920843782730116317,
                                        'source_nw_y_pixel': -41586450322709735,
                                        'source_pixel_width': -5420784797901161615,
                                        'source_pixel_height': -5023882145285762255,
                                        'rotation': -1467518687730231097,
                                        'virtual_nw_x_pixel': -1917945199,
                                        'virtual_nw_y_pixel': -1322160285,
                                        'virtual_width': 1894498476,
                                        'virtual_height': -337258995,
                                    },
                            {
                                        'source_monitor': 3914646,
                                        'source_nw_x_pixel': -8208107742072833060,
                                        'source_nw_y_pixel': -1791026452706577793,
                                        'source_pixel_width': -3851768062436820615,
                                        'source_pixel_height': -7078631711877226906,
                                        'rotation': -6162146126417256972,
                                        'virtual_nw_x_pixel': 1091730123,
                                        'virtual_nw_y_pixel': 1440935217,
                                        'virtual_width': -1898162825,
                                        'virtual_height': -83010220,
                                    },
                            {
                                        'source_monitor': 6216393,
                                        'source_nw_x_pixel': -8486743595567150377,
                                        'source_nw_y_pixel': -3883396952661240595,
                                        'source_pixel_width': -3703489440677643994,
                                        'source_pixel_height': -6260025107122491079,
                                        'rotation': -4622537772776793961,
                                        'virtual_nw_x_pixel': -1898478116,
                                        'virtual_nw_y_pixel': 404154170,
                                        'virtual_width': 932919507,
                                        'virtual_height': -857991851,
                                    },
                            {
                                        'source_monitor': 1780617,
                                        'source_nw_x_pixel': -3881582465239891963,
                                        'source_nw_y_pixel': -5884463487777203559,
                                        'source_pixel_width': -2540388793254035778,
                                        'source_pixel_height': -8474547994349614579,
                                        'rotation': -2498173992292038176,
                                        'virtual_nw_x_pixel': 275556346,
                                        'virtual_nw_y_pixel': -93878176,
                                        'virtual_width': -472860375,
                                        'virtual_height': 1632936607,
                                    },
                            {
                                        'source_monitor': 6614686,
                                        'source_nw_x_pixel': -215446002270972889,
                                        'source_nw_y_pixel': -1931569017926567668,
                                        'source_pixel_width': -3428947245371804622,
                                        'source_pixel_height': -5096056962106718746,
                                        'rotation': -9053361831721346994,
                                        'virtual_nw_x_pixel': 1121551025,
                                        'virtual_nw_y_pixel': 457010830,
                                        'virtual_width': -16660877,
                                        'virtual_height': 289556109,
                                    },
                            {
                                        'source_monitor': 4922139,
                                        'source_nw_x_pixel': -7483326885230144163,
                                        'source_nw_y_pixel': -5996259374528440602,
                                        'source_pixel_width': -8655064249397076846,
                                        'source_pixel_height': -7662076514070897013,
                                        'rotation': -3976094383613911081,
                                        'virtual_nw_x_pixel': -1496786216,
                                        'virtual_nw_y_pixel': 189923732,
                                        'virtual_width': 1000552597,
                                        'virtual_height': -984995687,
                                    },
                            {
                                        'source_monitor': 9503380,
                                        'source_nw_x_pixel': -6011557742113263650,
                                        'source_nw_y_pixel': -8900285518410000972,
                                        'source_pixel_width': -8026420488065903826,
                                        'source_pixel_height': -9094422310819420414,
                                        'rotation': -4267637550786054425,
                                        'virtual_nw_x_pixel': -207682716,
                                        'virtual_nw_y_pixel': 1692063203,
                                        'virtual_width': -371377321,
                                        'virtual_height': 472696305,
                                    },
                            {
                                        'source_monitor': -448069,
                                        'source_nw_x_pixel': -9010956775844633479,
                                        'source_nw_y_pixel': -5239372117597797294,
                                        'source_pixel_width': -8396693724581059317,
                                        'source_pixel_height': -3349208226956425678,
                                        'rotation': -1253064625420697091,
                                        'virtual_nw_x_pixel': -1032153986,
                                        'virtual_nw_y_pixel': 1971680306,
                                        'virtual_width': -852511845,
                                        'virtual_height': 550176606,
                                    },
                            {
                                        'source_monitor': 6619555,
                                        'source_nw_x_pixel': -7663425210882696068,
                                        'source_nw_y_pixel': -2115930003152844801,
                                        'source_pixel_width': -889361483720397309,
                                        'source_pixel_height': -8135963218937417162,
                                        'rotation': -4898880780417256593,
                                        'virtual_nw_x_pixel': 1452166563,
                                        'virtual_nw_y_pixel': 851080144,
                                        'virtual_width': -566006034,
                                        'virtual_height': 1069428526,
                                    },
                        ],
                },
                {
                    'description': 'ӆǾɱԍюɿӰʐσбĶ˲ʭ˅іΖʕYѥȱԇȉι¡ҦǿÈҋσЀ',
                    'monitors': [
                            {
                                        'identifier': 5435036,
                                        'width': 7901491975754903825,
                                        'height': -5927400865759774373,
                                    },
                            {
                                        'identifier': 7917555,
                                        'width': 5358720775089988556,
                                        'height': 4432578632314338050,
                                    },
                            {
                                        'identifier': 4293256,
                                        'width': 174268914483069826,
                                        'height': -7853621166902489125,
                                    },
                            {
                                        'identifier': 9841809,
                                        'width': -4640994776620070309,
                                        'height': 1100690569696279734,
                                    },
                            {
                                        'identifier': 648610,
                                        'width': 4849081620529350485,
                                        'height': -980631014653241981,
                                    },
                            {
                                        'identifier': 4197506,
                                        'width': 3078936020788075022,
                                        'height': -3583108657703879294,
                                    },
                            {
                                        'identifier': 3194794,
                                        'width': -9083925895803184139,
                                        'height': 2230302499868110706,
                                    },
                            {
                                        'identifier': 4043099,
                                        'width': 9070631285624526247,
                                        'height': -8520854194761309633,
                                    },
                            {
                                        'identifier': 6341623,
                                        'width': -4856288808207079807,
                                        'height': 1432247321784800962,
                                    },
                            {
                                        'identifier': 8392193,
                                        'width': 5673394383643799061,
                                        'height': 5697128639954222998,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5004987,
                                        'source_nw_x_pixel': -8894655179896933661,
                                        'source_nw_y_pixel': -486386750167332030,
                                        'source_pixel_width': -721644155403663351,
                                        'source_pixel_height': -7025770051028158158,
                                        'rotation': -1017490503138655705,
                                        'virtual_nw_x_pixel': -1668301377,
                                        'virtual_nw_y_pixel': 168455867,
                                        'virtual_width': 1308563696,
                                        'virtual_height': 696450648,
                                    },
                            {
                                        'source_monitor': 3643242,
                                        'source_nw_x_pixel': -5431316948209533564,
                                        'source_nw_y_pixel': -4034514480605505348,
                                        'source_pixel_width': -2795196253060253806,
                                        'source_pixel_height': -1345257896335375578,
                                        'rotation': -5522173316331885886,
                                        'virtual_nw_x_pixel': 1901000762,
                                        'virtual_nw_y_pixel': 1346403007,
                                        'virtual_width': -980899792,
                                        'virtual_height': 19134470,
                                    },
                            {
                                        'source_monitor': 4888691,
                                        'source_nw_x_pixel': -6793370101831443878,
                                        'source_nw_y_pixel': -3238987935794125974,
                                        'source_pixel_width': -2683200942331787149,
                                        'source_pixel_height': -9101920003133654490,
                                        'rotation': -7937110547804014127,
                                        'virtual_nw_x_pixel': 1241053892,
                                        'virtual_nw_y_pixel': -381088331,
                                        'virtual_width': -780307628,
                                        'virtual_height': 1602820295,
                                    },
                            {
                                        'source_monitor': -203839,
                                        'source_nw_x_pixel': -5408843136175604451,
                                        'source_nw_y_pixel': -2786846364514351790,
                                        'source_pixel_width': -3174064749895302558,
                                        'source_pixel_height': -3000222709417921148,
                                        'rotation': -2290740160844870563,
                                        'virtual_nw_x_pixel': 1217762394,
                                        'virtual_nw_y_pixel': 336649415,
                                        'virtual_width': 851387838,
                                        'virtual_height': -424502158,
                                    },
                            {
                                        'source_monitor': 3468104,
                                        'source_nw_x_pixel': -3768722606213002067,
                                        'source_nw_y_pixel': -4741788821573758597,
                                        'source_pixel_width': -2531430949384036003,
                                        'source_pixel_height': -5301640686658269422,
                                        'rotation': -4724653091047161216,
                                        'virtual_nw_x_pixel': 1653394082,
                                        'virtual_nw_y_pixel': 87699698,
                                        'virtual_width': -937829501,
                                        'virtual_height': 1673962168,
                                    },
                            {
                                        'source_monitor': 4000405,
                                        'source_nw_x_pixel': -259320104177574377,
                                        'source_nw_y_pixel': -1402782263770490799,
                                        'source_pixel_width': -8904070288369493977,
                                        'source_pixel_height': -4245745224428236193,
                                        'rotation': -619675037363412857,
                                        'virtual_nw_x_pixel': -1380475451,
                                        'virtual_nw_y_pixel': -1669419622,
                                        'virtual_width': 1138139019,
                                        'virtual_height': 1130556787,
                                    },
                            {
                                        'source_monitor': 2158705,
                                        'source_nw_x_pixel': -3868764438834179860,
                                        'source_nw_y_pixel': -7107797152852975733,
                                        'source_pixel_width': -9137762422823899419,
                                        'source_pixel_height': -4645255238582096779,
                                        'rotation': -1278912977519813623,
                                        'virtual_nw_x_pixel': -1074800422,
                                        'virtual_nw_y_pixel': -770125071,
                                        'virtual_width': 607247744,
                                        'virtual_height': -1084083470,
                                    },
                            {
                                        'source_monitor': 8263212,
                                        'source_nw_x_pixel': -3427836533169525814,
                                        'source_nw_y_pixel': -2035046509742871966,
                                        'source_pixel_width': -2295511947302522763,
                                        'source_pixel_height': -4276108998152654028,
                                        'rotation': -1707330003023580760,
                                        'virtual_nw_x_pixel': 1058128478,
                                        'virtual_nw_y_pixel': 1818252513,
                                        'virtual_width': -1194081655,
                                        'virtual_height': -585637404,
                                    },
                            {
                                        'source_monitor': 3340366,
                                        'source_nw_x_pixel': -4750155370138805294,
                                        'source_nw_y_pixel': -680376592396903536,
                                        'source_pixel_width': -5584590367008060992,
                                        'source_pixel_height': -7077807891246466921,
                                        'rotation': -945297324033894255,
                                        'virtual_nw_x_pixel': 1414096289,
                                        'virtual_nw_y_pixel': 173301704,
                                        'virtual_width': -1722039362,
                                        'virtual_height': -1487839250,
                                    },
                            {
                                        'source_monitor': 3955588,
                                        'source_nw_x_pixel': -2398530284641250229,
                                        'source_nw_y_pixel': -2168625819024201106,
                                        'source_pixel_width': -2909191227643694401,
                                        'source_pixel_height': -8931103207004935591,
                                        'rotation': -8331589399686907243,
                                        'virtual_nw_x_pixel': -620924409,
                                        'virtual_nw_y_pixel': -79918878,
                                        'virtual_width': -1130439141,
                                        'virtual_height': -74816560,
                                    },
                        ],
                },
                {
                    'description': 'ɋЩӉƸˌԒȐӘӍ/ѳҾŊЩɩ˥ŸΏюǺœ\x9dʮ\u0382÷ųөԟҙΣ',
                    'monitors': [
                            {
                                        'identifier': 1518831,
                                        'width': 4092436985055648882,
                                        'height': -1565921349394128803,
                                    },
                            {
                                        'identifier': -159278,
                                        'width': 3560156124023377504,
                                        'height': -4863997727495593529,
                                    },
                            {
                                        'identifier': 5999878,
                                        'width': -960702271637237425,
                                        'height': -3277945976909071609,
                                    },
                            {
                                        'identifier': 6884671,
                                        'width': 612062044749094882,
                                        'height': -8015645346157338559,
                                    },
                            {
                                        'identifier': 2283876,
                                        'width': 1930983286073757415,
                                        'height': 4601687245909051603,
                                    },
                            {
                                        'identifier': 4391710,
                                        'width': -3671359552963969460,
                                        'height': -7016244747431165234,
                                    },
                            {
                                        'identifier': -560346,
                                        'width': 7179193708440778734,
                                        'height': 2073630660281395748,
                                    },
                            {
                                        'identifier': 7713124,
                                        'width': -8213234491787974733,
                                        'height': -2156049998552355262,
                                    },
                            {
                                        'identifier': 4693515,
                                        'width': -3100204978760586442,
                                        'height': 5284314726567662179,
                                    },
                            {
                                        'identifier': 101785,
                                        'width': -6535705860660679936,
                                        'height': -8034335423466052756,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9805531,
                                        'source_nw_x_pixel': -8655458972850320612,
                                        'source_nw_y_pixel': -1792939979298311649,
                                        'source_pixel_width': -932171006410524008,
                                        'source_pixel_height': -7294928745906543657,
                                        'rotation': -8300730461668692880,
                                        'virtual_nw_x_pixel': 169883171,
                                        'virtual_nw_y_pixel': 211326671,
                                        'virtual_width': 1472899753,
                                        'virtual_height': -850017414,
                                    },
                            {
                                        'source_monitor': 4458411,
                                        'source_nw_x_pixel': -8829935045925513716,
                                        'source_nw_y_pixel': -7734663757781643798,
                                        'source_pixel_width': -6713377790352431128,
                                        'source_pixel_height': -6901484327082943305,
                                        'rotation': -7983978647563103880,
                                        'virtual_nw_x_pixel': 1576972688,
                                        'virtual_nw_y_pixel': -1151434031,
                                        'virtual_width': 1944966347,
                                        'virtual_height': -292793991,
                                    },
                            {
                                        'source_monitor': 7876477,
                                        'source_nw_x_pixel': -1051212227824580917,
                                        'source_nw_y_pixel': -7705892218862085079,
                                        'source_pixel_width': -3522618491700325870,
                                        'source_pixel_height': -1510456472929596691,
                                        'rotation': -1670669889865754971,
                                        'virtual_nw_x_pixel': -700011472,
                                        'virtual_nw_y_pixel': -918911966,
                                        'virtual_width': -1847664462,
                                        'virtual_height': -131579389,
                                    },
                            {
                                        'source_monitor': 2238731,
                                        'source_nw_x_pixel': -727412983471045607,
                                        'source_nw_y_pixel': -2983305467427191241,
                                        'source_pixel_width': -3456286368913733239,
                                        'source_pixel_height': -4098632587870176869,
                                        'rotation': -217920892195727191,
                                        'virtual_nw_x_pixel': -1511234829,
                                        'virtual_nw_y_pixel': 1807167419,
                                        'virtual_width': -729050787,
                                        'virtual_height': -1095420422,
                                    },
                            {
                                        'source_monitor': -574318,
                                        'source_nw_x_pixel': -4097180984645578498,
                                        'source_nw_y_pixel': -5652847582074087914,
                                        'source_pixel_width': -7022890342283607643,
                                        'source_pixel_height': -8987211887000445286,
                                        'rotation': -2029796106589007133,
                                        'virtual_nw_x_pixel': -568857991,
                                        'virtual_nw_y_pixel': 1789005545,
                                        'virtual_width': 391475639,
                                        'virtual_height': -1565973630,
                                    },
                            {
                                        'source_monitor': 3969874,
                                        'source_nw_x_pixel': -9144570632085893078,
                                        'source_nw_y_pixel': -6786797911809169544,
                                        'source_pixel_width': -8178749377167276336,
                                        'source_pixel_height': -4524838553302508494,
                                        'rotation': -8458676515689983388,
                                        'virtual_nw_x_pixel': 1194956619,
                                        'virtual_nw_y_pixel': -620360190,
                                        'virtual_width': 1096062562,
                                        'virtual_height': 1262193745,
                                    },
                            {
                                        'source_monitor': 6048558,
                                        'source_nw_x_pixel': -3665235070294732579,
                                        'source_nw_y_pixel': -8094169338344802364,
                                        'source_pixel_width': -5637559063288994885,
                                        'source_pixel_height': -3647309672440524097,
                                        'rotation': -1883681873572231882,
                                        'virtual_nw_x_pixel': -479360811,
                                        'virtual_nw_y_pixel': -357466997,
                                        'virtual_width': -1961778003,
                                        'virtual_height': 740115662,
                                    },
                            {
                                        'source_monitor': 2573748,
                                        'source_nw_x_pixel': -2815271665666561611,
                                        'source_nw_y_pixel': -8586572296010999220,
                                        'source_pixel_width': -2881893102895597269,
                                        'source_pixel_height': -7771630435350626393,
                                        'rotation': -3166220799758028462,
                                        'virtual_nw_x_pixel': 113520123,
                                        'virtual_nw_y_pixel': 857446942,
                                        'virtual_width': 656170125,
                                        'virtual_height': -1397519790,
                                    },
                            {
                                        'source_monitor': 2225610,
                                        'source_nw_x_pixel': -3158169410274389080,
                                        'source_nw_y_pixel': -670969046095743584,
                                        'source_pixel_width': -7298025304894631002,
                                        'source_pixel_height': -1494288758346208774,
                                        'rotation': -8426237907563158049,
                                        'virtual_nw_x_pixel': 1163240529,
                                        'virtual_nw_y_pixel': 1748271153,
                                        'virtual_width': 448324239,
                                        'virtual_height': 578043265,
                                    },
                            {
                                        'source_monitor': 4719986,
                                        'source_nw_x_pixel': -6012531471822874383,
                                        'source_nw_y_pixel': -9113380133713045672,
                                        'source_pixel_width': -5187467137199693137,
                                        'source_pixel_height': -8435170979279813376,
                                        'rotation': -5773052849772062365,
                                        'virtual_nw_x_pixel': -1428417498,
                                        'virtual_nw_y_pixel': 1040377351,
                                        'virtual_width': 1318592630,
                                        'virtual_height': -1469878499,
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
                                        'identifier': 8060473,
                                        'width': -964465666327566258,
                                        'height': -1812292901941554689,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -6193092239664287614,
                                        'source_nw_y_pixel': -5684875479783913970,
                                        'source_pixel_width': -2232957060759696884,
                                        'source_pixel_height': -2267558792054286451,
                                        'rotation': -7642314756459170220,
                                        'virtual_nw_x_pixel': -648114856,
                                        'virtual_nw_y_pixel': 195023097,
                                        'virtual_width': 640200781,
                                        'virtual_height': -842063528,
                                    },
                        ],
                },
            ],

        },
    ),
]
