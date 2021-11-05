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
            'nw_x_pixel': 113657923,
            'nw_y_pixel': 1598644071,
            'width': -3272939232915346978,
            'height': -5342910415767148609,
            'ratio_x': -4308451224314599633,
            'ratio_y': 9206456400808208343,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -1707337470,

            'nw_y_pixel': -1774751863,

            'width': -3949845993989301498,

            'height': -8811210915609699041,

            'ratio_x': 2715635637594784103,

            'ratio_y': -8577271839713163111,

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
                    'nw_x_pixel': 207505373,
                    'nw_y_pixel': -107768008,
                    'width': -3408557900540246350,
                    'height': -6523949637708519846,
                    'ratio_x': -90743198861206072,
                    'ratio_y': 1578082625954471565,
                },
                {
                    'nw_x_pixel': -1113459111,
                    'nw_y_pixel': -1257909845,
                    'width': -6970412400819041195,
                    'height': -4312311720464531757,
                    'ratio_x': -358247028339710530,
                    'ratio_y': 6770726924013327513,
                },
                {
                    'nw_x_pixel': 221020978,
                    'nw_y_pixel': 1108766220,
                    'width': -820332687877775284,
                    'height': -6928492459464894067,
                    'ratio_x': -4504864931726222613,
                    'ratio_y': -6816131574816119099,
                },
                {
                    'nw_x_pixel': -167249546,
                    'nw_y_pixel': -502637793,
                    'width': -1044233463233943020,
                    'height': -5192312283488882635,
                    'ratio_x': -8831183466792540311,
                    'ratio_y': 3947333223015852253,
                },
                {
                    'nw_x_pixel': 24701847,
                    'nw_y_pixel': -1241068148,
                    'width': -1344375307572002005,
                    'height': -6886602268751198996,
                    'ratio_x': 2147096649967729759,
                    'ratio_y': -3218147790610382051,
                },
                {
                    'nw_x_pixel': -600574933,
                    'nw_y_pixel': 1150911774,
                    'width': -2099265866784187850,
                    'height': -1378019142247611210,
                    'ratio_x': 437997318795089625,
                    'ratio_y': -8891581281070573359,
                },
                {
                    'nw_x_pixel': 445716506,
                    'nw_y_pixel': -538682794,
                    'width': -3757994555233804601,
                    'height': -8416779775667111251,
                    'ratio_x': 4553302147646150239,
                    'ratio_y': -6653880065093966240,
                },
                {
                    'nw_x_pixel': 501468939,
                    'nw_y_pixel': -291840850,
                    'width': -6671526063340407380,
                    'height': -3348591605567023723,
                    'ratio_x': 3637202171345623487,
                    'ratio_y': -4511890111735140317,
                },
                {
                    'nw_x_pixel': -813792319,
                    'nw_y_pixel': 1329887704,
                    'width': -2631147511105177750,
                    'height': -1097235747122054364,
                    'ratio_x': 8298059076122338993,
                    'ratio_y': -5494816728075288430,
                },
                {
                    'nw_x_pixel': -595444073,
                    'nw_y_pixel': -1923548541,
                    'width': -1784224361970952052,
                    'height': -2228689289503463713,
                    'ratio_x': 6573728605707244317,
                    'ratio_y': 5673794228661632489,
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
            'identifier': 3509293,
            'width': 8411006875210797103,
            'height': -6421983473168019592,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 6544963,

            'width': 793658288621867455,

            'height': 7943273941512851773,

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
            'source_monitor': 4285890,
            'source_nw_x_pixel': -5565943243172709203,
            'source_nw_y_pixel': -8555762861471793668,
            'source_pixel_width': -656328801907915964,
            'source_pixel_height': -2594566499592057645,
            'rotation': -8688936621793355487,
            'virtual_nw_x_pixel': -1894165184,
            'virtual_nw_y_pixel': 1194872135,
            'virtual_width': 1302082698,
            'virtual_height': -1034712736,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -7322846494387035777,

            'source_nw_y_pixel': -5898261287401158523,

            'source_pixel_width': -7782047177055618424,

            'source_pixel_height': -8509576159620972380,

            'rotation': -2588740369131334711,

            'virtual_nw_x_pixel': -1761545400,

            'virtual_nw_y_pixel': 358978909,

            'virtual_width': 132121784,

            'virtual_height': -1686092635,

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
            'description': 'ԄϼѮĂȢǧ͵γʯǐɩɞНɤћЩdдɓėȼʬśίʨҞD\u0378ʫу',
            'monitors': [
                {
                    'identifier': 4237155,
                    'width': 582717157431822104,
                    'height': 2596025197812108865,
                },
                {
                    'identifier': -517362,
                    'width': -2774343041300971068,
                    'height': 1529605676311913551,
                },
                {
                    'identifier': -318193,
                    'width': -831453218295990532,
                    'height': 1504387778146511207,
                },
                {
                    'identifier': 5808908,
                    'width': -7894090272093197051,
                    'height': 7052587673696675216,
                },
                {
                    'identifier': 8605066,
                    'width': 1221400883650777431,
                    'height': 1979377966187807923,
                },
                {
                    'identifier': 9279627,
                    'width': -6726296126144445913,
                    'height': 9185913061770503444,
                },
                {
                    'identifier': 4608477,
                    'width': 5799616149390401002,
                    'height': 8915381916055225852,
                },
                {
                    'identifier': 9479789,
                    'width': 8652150147481073529,
                    'height': -6658903726311213719,
                },
                {
                    'identifier': 1988793,
                    'width': 9163301267962558111,
                    'height': -1620729071804589747,
                },
                {
                    'identifier': 3422698,
                    'width': -2506351383615277850,
                    'height': 2773744144876439124,
                },
            ],
            'screen': [
                {
                    'source_monitor': 3510362,
                    'source_nw_x_pixel': -2113102007066212660,
                    'source_nw_y_pixel': -7945688263558608609,
                    'source_pixel_width': -4374610964594373436,
                    'source_pixel_height': -5291016424132121430,
                    'rotation': -8251965515276592550,
                    'virtual_nw_x_pixel': 1746149468,
                    'virtual_nw_y_pixel': 1029808072,
                    'virtual_width': -736442954,
                    'virtual_height': -352510492,
                },
                {
                    'source_monitor': 9720699,
                    'source_nw_x_pixel': -282403257725972360,
                    'source_nw_y_pixel': -1076127087506246549,
                    'source_pixel_width': -5880742423445283379,
                    'source_pixel_height': -1994814068706098317,
                    'rotation': -745491155623268279,
                    'virtual_nw_x_pixel': -1802623147,
                    'virtual_nw_y_pixel': -1004876141,
                    'virtual_width': -36276300,
                    'virtual_height': -812971006,
                },
                {
                    'source_monitor': 496194,
                    'source_nw_x_pixel': -9068755122993121383,
                    'source_nw_y_pixel': -4556668709613846166,
                    'source_pixel_width': -3392250810638910017,
                    'source_pixel_height': -2384520369987368055,
                    'rotation': -332094568972752510,
                    'virtual_nw_x_pixel': 1674501737,
                    'virtual_nw_y_pixel': -38679619,
                    'virtual_width': 821801886,
                    'virtual_height': -38482967,
                },
                {
                    'source_monitor': 7630326,
                    'source_nw_x_pixel': -3411013360903469614,
                    'source_nw_y_pixel': -4248583319387408531,
                    'source_pixel_width': -2556141975761253428,
                    'source_pixel_height': -5042687440138699019,
                    'rotation': -8673224648698573501,
                    'virtual_nw_x_pixel': 1408481370,
                    'virtual_nw_y_pixel': -1454264550,
                    'virtual_width': -648618213,
                    'virtual_height': -1505884510,
                },
                {
                    'source_monitor': 6246835,
                    'source_nw_x_pixel': -2867534257735739054,
                    'source_nw_y_pixel': -316778484618112633,
                    'source_pixel_width': -397769086349253020,
                    'source_pixel_height': -1986564767991526171,
                    'rotation': -7896496286173572457,
                    'virtual_nw_x_pixel': 501605506,
                    'virtual_nw_y_pixel': -1465602915,
                    'virtual_width': -794663571,
                    'virtual_height': 269433458,
                },
                {
                    'source_monitor': 7075109,
                    'source_nw_x_pixel': -286136320121338975,
                    'source_nw_y_pixel': -7717671768877216545,
                    'source_pixel_width': -4200500213276313,
                    'source_pixel_height': -4748068449610763124,
                    'rotation': -8878826382320561469,
                    'virtual_nw_x_pixel': 1807360899,
                    'virtual_nw_y_pixel': -1505919864,
                    'virtual_width': 397684388,
                    'virtual_height': 331318599,
                },
                {
                    'source_monitor': 3912612,
                    'source_nw_x_pixel': -753601736910189710,
                    'source_nw_y_pixel': -7733134296995353354,
                    'source_pixel_width': -8893448402168972409,
                    'source_pixel_height': -5611628195805324519,
                    'rotation': -4896884983639074581,
                    'virtual_nw_x_pixel': -1407907865,
                    'virtual_nw_y_pixel': 240968825,
                    'virtual_width': 951117692,
                    'virtual_height': -389144375,
                },
                {
                    'source_monitor': 9450831,
                    'source_nw_x_pixel': -3967211242300116751,
                    'source_nw_y_pixel': -947498524621429640,
                    'source_pixel_width': -5599547363385146212,
                    'source_pixel_height': -7145473043553944397,
                    'rotation': -8238979876250931534,
                    'virtual_nw_x_pixel': -218732738,
                    'virtual_nw_y_pixel': -393070383,
                    'virtual_width': 1023198907,
                    'virtual_height': 1007311567,
                },
                {
                    'source_monitor': 5606129,
                    'source_nw_x_pixel': -6391834154001476445,
                    'source_nw_y_pixel': -894339598141604773,
                    'source_pixel_width': -541724510196331777,
                    'source_pixel_height': -3590780128084928072,
                    'rotation': -2254814496107279201,
                    'virtual_nw_x_pixel': -844383707,
                    'virtual_nw_y_pixel': -1035922605,
                    'virtual_width': 1209814303,
                    'virtual_height': 1421914163,
                },
                {
                    'source_monitor': 164312,
                    'source_nw_x_pixel': -5120594646306852944,
                    'source_nw_y_pixel': -8528399292127588730,
                    'source_pixel_width': -8052664838368010508,
                    'source_pixel_height': -2693481661905581941,
                    'rotation': -8299046126209671914,
                    'virtual_nw_x_pixel': -38884957,
                    'virtual_nw_y_pixel': 946155973,
                    'virtual_width': 470063526,
                    'virtual_height': 1048407537,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 4292534,
                    'width': 1234511847265666876,
                    'height': 4600766097044284649,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -7636834775369277835,
                    'source_nw_y_pixel': -9051395825361763131,
                    'source_pixel_width': -888383812958013655,
                    'source_pixel_height': -1878118720606282551,
                    'rotation': -9217933738934368619,
                    'virtual_nw_x_pixel': -846167291,
                    'virtual_nw_y_pixel': -663055603,
                    'virtual_width': 140330291,
                    'virtual_height': -1882997102,
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
                    'description': '˚ϹšǤʋǁrϒϐǧǌȌʴǕѸьɋR˕˯ԖȱǃɒʢҊʫӿŠҐ',
                    'monitors': [
                            {
                                        'identifier': 2099368,
                                        'width': -7678343482069994766,
                                        'height': 4516661285945480631,
                                    },
                            {
                                        'identifier': 5009191,
                                        'width': 3868313073340768607,
                                        'height': 6254051249262261601,
                                    },
                            {
                                        'identifier': -672978,
                                        'width': -3662804714200709290,
                                        'height': -4228404720673095874,
                                    },
                            {
                                        'identifier': -234506,
                                        'width': 3503645749554004966,
                                        'height': 3006559221035820849,
                                    },
                            {
                                        'identifier': 7019117,
                                        'width': 6656711093064885545,
                                        'height': 7154201086262682817,
                                    },
                            {
                                        'identifier': 8705203,
                                        'width': 8911093060131704902,
                                        'height': 9055063599485611000,
                                    },
                            {
                                        'identifier': 357968,
                                        'width': 8560125959756233608,
                                        'height': -3965714571315246439,
                                    },
                            {
                                        'identifier': 86455,
                                        'width': 1427397931432263296,
                                        'height': -1091381339005826010,
                                    },
                            {
                                        'identifier': 5160787,
                                        'width': 8939639591468911490,
                                        'height': 4323210363147188913,
                                    },
                            {
                                        'identifier': 7788770,
                                        'width': 5261980089105695174,
                                        'height': 5073311531684567729,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8475974,
                                        'source_nw_x_pixel': -1038978344655942974,
                                        'source_nw_y_pixel': -8004899323675673848,
                                        'source_pixel_width': -33377681458583380,
                                        'source_pixel_height': -1513101887212477545,
                                        'rotation': -8321051101217698648,
                                        'virtual_nw_x_pixel': -610259338,
                                        'virtual_nw_y_pixel': 717412660,
                                        'virtual_width': 655400119,
                                        'virtual_height': 652136105,
                                    },
                            {
                                        'source_monitor': -137454,
                                        'source_nw_x_pixel': -6463222422422541112,
                                        'source_nw_y_pixel': -7185985098017065452,
                                        'source_pixel_width': -8818755796179704277,
                                        'source_pixel_height': -6836296077629463390,
                                        'rotation': -2991850455205785044,
                                        'virtual_nw_x_pixel': -728321090,
                                        'virtual_nw_y_pixel': 1425552793,
                                        'virtual_width': 252444255,
                                        'virtual_height': -578479596,
                                    },
                            {
                                        'source_monitor': 7396127,
                                        'source_nw_x_pixel': -6485085005166096541,
                                        'source_nw_y_pixel': -3156323558052103258,
                                        'source_pixel_width': -700593348322848917,
                                        'source_pixel_height': -2612095136778040429,
                                        'rotation': -8398981373658269165,
                                        'virtual_nw_x_pixel': -1716191896,
                                        'virtual_nw_y_pixel': -540539721,
                                        'virtual_width': 888938787,
                                        'virtual_height': -73032083,
                                    },
                            {
                                        'source_monitor': 1920221,
                                        'source_nw_x_pixel': -1357825215577216068,
                                        'source_nw_y_pixel': -1036204546927320265,
                                        'source_pixel_width': -2029178186073382835,
                                        'source_pixel_height': -7215555363332911947,
                                        'rotation': -6762403953598026531,
                                        'virtual_nw_x_pixel': -937837545,
                                        'virtual_nw_y_pixel': -1240256223,
                                        'virtual_width': -716807940,
                                        'virtual_height': -1193734491,
                                    },
                            {
                                        'source_monitor': 1852327,
                                        'source_nw_x_pixel': -2385447361947665958,
                                        'source_nw_y_pixel': -50508719718886540,
                                        'source_pixel_width': -6842331169721643047,
                                        'source_pixel_height': -2586440062308112043,
                                        'rotation': -8741968881820399500,
                                        'virtual_nw_x_pixel': -821273095,
                                        'virtual_nw_y_pixel': 780217839,
                                        'virtual_width': 1609201453,
                                        'virtual_height': 1554325033,
                                    },
                            {
                                        'source_monitor': 9350035,
                                        'source_nw_x_pixel': -5018556695781996306,
                                        'source_nw_y_pixel': -829191646606560365,
                                        'source_pixel_width': -2241886556692535896,
                                        'source_pixel_height': -762063307544826045,
                                        'rotation': -9173570323954204088,
                                        'virtual_nw_x_pixel': 486351343,
                                        'virtual_nw_y_pixel': -1088998408,
                                        'virtual_width': -836478171,
                                        'virtual_height': -318951187,
                                    },
                            {
                                        'source_monitor': 2647645,
                                        'source_nw_x_pixel': -3276876726940970661,
                                        'source_nw_y_pixel': -6149771151487227157,
                                        'source_pixel_width': -1230420643742989946,
                                        'source_pixel_height': -3998603574086904409,
                                        'rotation': -5001557523409879660,
                                        'virtual_nw_x_pixel': -1301737036,
                                        'virtual_nw_y_pixel': 1475148932,
                                        'virtual_width': 743826519,
                                        'virtual_height': -1132053943,
                                    },
                            {
                                        'source_monitor': 7953490,
                                        'source_nw_x_pixel': -4037811626425260148,
                                        'source_nw_y_pixel': -4575660304680498144,
                                        'source_pixel_width': -7087839451602800416,
                                        'source_pixel_height': -2112548669448891226,
                                        'rotation': -7775884522477136309,
                                        'virtual_nw_x_pixel': -698629283,
                                        'virtual_nw_y_pixel': -1755249646,
                                        'virtual_width': 13444325,
                                        'virtual_height': 173568503,
                                    },
                            {
                                        'source_monitor': 4560214,
                                        'source_nw_x_pixel': -6420361686038141280,
                                        'source_nw_y_pixel': -9142642056576349791,
                                        'source_pixel_width': -6526048113648087507,
                                        'source_pixel_height': -8280762773031968402,
                                        'rotation': -1807754784395498076,
                                        'virtual_nw_x_pixel': 665270604,
                                        'virtual_nw_y_pixel': -1056606444,
                                        'virtual_width': -1378368307,
                                        'virtual_height': -1599170760,
                                    },
                            {
                                        'source_monitor': 6976254,
                                        'source_nw_x_pixel': -8650871246818237499,
                                        'source_nw_y_pixel': -5307719227852886126,
                                        'source_pixel_width': -1638228981849065851,
                                        'source_pixel_height': -4219355889050660418,
                                        'rotation': -1285655525587770551,
                                        'virtual_nw_x_pixel': 275628891,
                                        'virtual_nw_y_pixel': 853145882,
                                        'virtual_width': 560800149,
                                        'virtual_height': -1205874065,
                                    },
                        ],
                },
                {
                    'description': 'Кųǰ\x84ғϩҗȚʲίĵϴѕɏ#ϵӢɮŉӶФwȌ\x9aυdąԁȭŅ',
                    'monitors': [
                            {
                                        'identifier': 1963645,
                                        'width': 2403320420054315779,
                                        'height': 1797730366156352244,
                                    },
                            {
                                        'identifier': 5621307,
                                        'width': -8579445967521317007,
                                        'height': -7297807914909824457,
                                    },
                            {
                                        'identifier': 5817303,
                                        'width': -6719601329014943455,
                                        'height': -145725469888560012,
                                    },
                            {
                                        'identifier': 2625561,
                                        'width': 3648114953666414889,
                                        'height': 1389575936425513371,
                                    },
                            {
                                        'identifier': 6855366,
                                        'width': 6757712939946718189,
                                        'height': 95099379736561278,
                                    },
                            {
                                        'identifier': 6364290,
                                        'width': -353127357280536561,
                                        'height': -3893236023175032632,
                                    },
                            {
                                        'identifier': -112935,
                                        'width': 3474433491070773640,
                                        'height': -5720268973271804500,
                                    },
                            {
                                        'identifier': 3302881,
                                        'width': -5110499019803269376,
                                        'height': -521327364313539819,
                                    },
                            {
                                        'identifier': 5748208,
                                        'width': 3210515599704474170,
                                        'height': -6366230237731506390,
                                    },
                            {
                                        'identifier': 3481854,
                                        'width': -8133726318076171066,
                                        'height': 1979533028701699814,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7716882,
                                        'source_nw_x_pixel': -4410328208303375931,
                                        'source_nw_y_pixel': -8029524563741010208,
                                        'source_pixel_width': -2907802103538202424,
                                        'source_pixel_height': -4497262059529581665,
                                        'rotation': -9131608640402746992,
                                        'virtual_nw_x_pixel': -372817398,
                                        'virtual_nw_y_pixel': -1419031532,
                                        'virtual_width': -1315700440,
                                        'virtual_height': 1674166561,
                                    },
                            {
                                        'source_monitor': 2177091,
                                        'source_nw_x_pixel': -8212001775721028640,
                                        'source_nw_y_pixel': -8418823702173687255,
                                        'source_pixel_width': -8834762958674180219,
                                        'source_pixel_height': -1757398284084918681,
                                        'rotation': -1559421403285713841,
                                        'virtual_nw_x_pixel': 532755439,
                                        'virtual_nw_y_pixel': -303293893,
                                        'virtual_width': -1373467025,
                                        'virtual_height': -845323100,
                                    },
                            {
                                        'source_monitor': -77240,
                                        'source_nw_x_pixel': -1773927649353122525,
                                        'source_nw_y_pixel': -2908748910135171482,
                                        'source_pixel_width': -984592942041905259,
                                        'source_pixel_height': -3671171085251761651,
                                        'rotation': -6383721779022290355,
                                        'virtual_nw_x_pixel': -414178008,
                                        'virtual_nw_y_pixel': 555938457,
                                        'virtual_width': -1741078778,
                                        'virtual_height': 165244777,
                                    },
                            {
                                        'source_monitor': -83043,
                                        'source_nw_x_pixel': -7742218080060115224,
                                        'source_nw_y_pixel': -5214422679801004934,
                                        'source_pixel_width': -5817330513582436197,
                                        'source_pixel_height': -9153372559628621871,
                                        'rotation': -1897099948977335891,
                                        'virtual_nw_x_pixel': -1976254468,
                                        'virtual_nw_y_pixel': 178218131,
                                        'virtual_width': -1603965119,
                                        'virtual_height': -747352244,
                                    },
                            {
                                        'source_monitor': 2734056,
                                        'source_nw_x_pixel': -927708613100589782,
                                        'source_nw_y_pixel': -6493654157405040165,
                                        'source_pixel_width': -4776336491811473813,
                                        'source_pixel_height': -6308779112371538495,
                                        'rotation': -3272088093327908961,
                                        'virtual_nw_x_pixel': 1401198995,
                                        'virtual_nw_y_pixel': -364090321,
                                        'virtual_width': 818427728,
                                        'virtual_height': 1465947425,
                                    },
                            {
                                        'source_monitor': 8555300,
                                        'source_nw_x_pixel': -5431730362976359505,
                                        'source_nw_y_pixel': -7231186340766632717,
                                        'source_pixel_width': -6426963212594691341,
                                        'source_pixel_height': -5583460159899112189,
                                        'rotation': -7227309582000209367,
                                        'virtual_nw_x_pixel': 1089958522,
                                        'virtual_nw_y_pixel': 740622075,
                                        'virtual_width': -1103475166,
                                        'virtual_height': 1981694475,
                                    },
                            {
                                        'source_monitor': 5932320,
                                        'source_nw_x_pixel': -5703134480383238332,
                                        'source_nw_y_pixel': -6457942381635910424,
                                        'source_pixel_width': -3224822884295827147,
                                        'source_pixel_height': -8103083692229949061,
                                        'rotation': -7179559700482211105,
                                        'virtual_nw_x_pixel': -270745458,
                                        'virtual_nw_y_pixel': -992995293,
                                        'virtual_width': -489225960,
                                        'virtual_height': 1513475850,
                                    },
                            {
                                        'source_monitor': 9128502,
                                        'source_nw_x_pixel': -661436374192338058,
                                        'source_nw_y_pixel': -5974685254755685467,
                                        'source_pixel_width': -4526312139987698095,
                                        'source_pixel_height': -2952400562507436718,
                                        'rotation': -9197040479793398948,
                                        'virtual_nw_x_pixel': -412730631,
                                        'virtual_nw_y_pixel': 1984235417,
                                        'virtual_width': 1661824422,
                                        'virtual_height': 1302784769,
                                    },
                            {
                                        'source_monitor': 796271,
                                        'source_nw_x_pixel': -1577247842157382,
                                        'source_nw_y_pixel': -5033998292127007335,
                                        'source_pixel_width': -7732763030195533522,
                                        'source_pixel_height': -4215806617446080714,
                                        'rotation': -2064060476261809014,
                                        'virtual_nw_x_pixel': -1775636940,
                                        'virtual_nw_y_pixel': 393355809,
                                        'virtual_width': 578898762,
                                        'virtual_height': -1775082380,
                                    },
                            {
                                        'source_monitor': 5314990,
                                        'source_nw_x_pixel': -4050047104975528701,
                                        'source_nw_y_pixel': -2947555661878730694,
                                        'source_pixel_width': -4940657471937752516,
                                        'source_pixel_height': -7523455013502964496,
                                        'rotation': -1122597436619161574,
                                        'virtual_nw_x_pixel': 1766247106,
                                        'virtual_nw_y_pixel': -1667983303,
                                        'virtual_width': -175080307,
                                        'virtual_height': -783201001,
                                    },
                        ],
                },
                {
                    'description': 'Ї¿ɸKĉǍήГŤƻӬ҂˼ӊԧɥʨØӟǺ\x897ũǊҜ<ŷ\x81ʩȨ',
                    'monitors': [
                            {
                                        'identifier': 5033330,
                                        'width': -5031053044945723173,
                                        'height': 795997077481744733,
                                    },
                            {
                                        'identifier': 2790752,
                                        'width': -8820637055662429016,
                                        'height': 8042434000947058887,
                                    },
                            {
                                        'identifier': -194722,
                                        'width': -7228167706414768262,
                                        'height': -6814153286030917605,
                                    },
                            {
                                        'identifier': -54865,
                                        'width': 2848622958406065745,
                                        'height': 4805969775062422239,
                                    },
                            {
                                        'identifier': 2818464,
                                        'width': -6750308728930264989,
                                        'height': 298663931839428897,
                                    },
                            {
                                        'identifier': 7432066,
                                        'width': 9003240826345195284,
                                        'height': 6699977447899956850,
                                    },
                            {
                                        'identifier': 6431301,
                                        'width': 2810707814159410321,
                                        'height': -3099726734930386636,
                                    },
                            {
                                        'identifier': 3155283,
                                        'width': 9069830693567689754,
                                        'height': -13761513738640978,
                                    },
                            {
                                        'identifier': 3520231,
                                        'width': -3418420125582816307,
                                        'height': 5190966087586505985,
                                    },
                            {
                                        'identifier': 6961488,
                                        'width': -6680170341677149240,
                                        'height': -7732739166821354896,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9696719,
                                        'source_nw_x_pixel': -2123864693703438740,
                                        'source_nw_y_pixel': -5773397791090051880,
                                        'source_pixel_width': -1812324344113665406,
                                        'source_pixel_height': -3534875396601364202,
                                        'rotation': -3934240148502639725,
                                        'virtual_nw_x_pixel': 1953122270,
                                        'virtual_nw_y_pixel': 788349626,
                                        'virtual_width': 528836890,
                                        'virtual_height': -1328505843,
                                    },
                            {
                                        'source_monitor': 9026171,
                                        'source_nw_x_pixel': -6462576640227671404,
                                        'source_nw_y_pixel': -6061323764917055911,
                                        'source_pixel_width': -8686853771688040,
                                        'source_pixel_height': -5958052955826335731,
                                        'rotation': -4788500443598630612,
                                        'virtual_nw_x_pixel': -1451864454,
                                        'virtual_nw_y_pixel': 317163356,
                                        'virtual_width': 1980768291,
                                        'virtual_height': 1901549203,
                                    },
                            {
                                        'source_monitor': 9123937,
                                        'source_nw_x_pixel': -7641972023980793901,
                                        'source_nw_y_pixel': -5611842915766486600,
                                        'source_pixel_width': -5831974367539720538,
                                        'source_pixel_height': -2573448808248131886,
                                        'rotation': -3960342317549169244,
                                        'virtual_nw_x_pixel': 1197595928,
                                        'virtual_nw_y_pixel': 68133385,
                                        'virtual_width': 742017266,
                                        'virtual_height': -1340894307,
                                    },
                            {
                                        'source_monitor': 4077236,
                                        'source_nw_x_pixel': -8077227081504859301,
                                        'source_nw_y_pixel': -1129993364503017715,
                                        'source_pixel_width': -460467678176665237,
                                        'source_pixel_height': -1997463765661649006,
                                        'rotation': -4651543412967482917,
                                        'virtual_nw_x_pixel': -1855748450,
                                        'virtual_nw_y_pixel': -657842471,
                                        'virtual_width': 1413223172,
                                        'virtual_height': -1602672599,
                                    },
                            {
                                        'source_monitor': 3209227,
                                        'source_nw_x_pixel': -4777436496451956070,
                                        'source_nw_y_pixel': -1894621802923807547,
                                        'source_pixel_width': -6240771875231655638,
                                        'source_pixel_height': -5903156317878395285,
                                        'rotation': -3064054130364397731,
                                        'virtual_nw_x_pixel': -1824630478,
                                        'virtual_nw_y_pixel': -758367704,
                                        'virtual_width': -1706588899,
                                        'virtual_height': 1046933106,
                                    },
                            {
                                        'source_monitor': 5727926,
                                        'source_nw_x_pixel': -5167624324305722602,
                                        'source_nw_y_pixel': -3389898022805460149,
                                        'source_pixel_width': -6037396282038968084,
                                        'source_pixel_height': -747780338792692502,
                                        'rotation': -374855808413965564,
                                        'virtual_nw_x_pixel': -107310881,
                                        'virtual_nw_y_pixel': 1016337137,
                                        'virtual_width': -166192069,
                                        'virtual_height': -1057167191,
                                    },
                            {
                                        'source_monitor': 8513319,
                                        'source_nw_x_pixel': -8766770692462656532,
                                        'source_nw_y_pixel': -427606161583322302,
                                        'source_pixel_width': -7380419477190415184,
                                        'source_pixel_height': -6760094922104728196,
                                        'rotation': -7809395191649296245,
                                        'virtual_nw_x_pixel': 1790471151,
                                        'virtual_nw_y_pixel': 854000274,
                                        'virtual_width': -605651476,
                                        'virtual_height': 434617215,
                                    },
                            {
                                        'source_monitor': 1287575,
                                        'source_nw_x_pixel': -2454997293597424195,
                                        'source_nw_y_pixel': -6836559070273117661,
                                        'source_pixel_width': -7727631878688351551,
                                        'source_pixel_height': -2927681430442124523,
                                        'rotation': -5866338387115614565,
                                        'virtual_nw_x_pixel': 306149398,
                                        'virtual_nw_y_pixel': 1012523752,
                                        'virtual_width': -41300249,
                                        'virtual_height': -1775638771,
                                    },
                            {
                                        'source_monitor': 8854467,
                                        'source_nw_x_pixel': -4779208328649998077,
                                        'source_nw_y_pixel': -5189578075618058629,
                                        'source_pixel_width': -7743339222001521325,
                                        'source_pixel_height': -5397741644663191454,
                                        'rotation': -4425599653228361537,
                                        'virtual_nw_x_pixel': -192937923,
                                        'virtual_nw_y_pixel': 1038239254,
                                        'virtual_width': -1491277365,
                                        'virtual_height': 661380009,
                                    },
                            {
                                        'source_monitor': 7900664,
                                        'source_nw_x_pixel': -6097009049269923415,
                                        'source_nw_y_pixel': -5079745719387558439,
                                        'source_pixel_width': -722744660536725498,
                                        'source_pixel_height': -7222414105626711991,
                                        'rotation': -2297002184755705048,
                                        'virtual_nw_x_pixel': 1093923976,
                                        'virtual_nw_y_pixel': 856632657,
                                        'virtual_width': -951108496,
                                        'virtual_height': 1259857035,
                                    },
                        ],
                },
                {
                    'description': 'ːŦĀ\u038dѯɚӕɵfʷϛŝȯЉл¢ΘφͿȧύȫңƷ˱ʠԆГԪʎ',
                    'monitors': [
                            {
                                        'identifier': 9430773,
                                        'width': -1132114739006978198,
                                        'height': -6526781836660506499,
                                    },
                            {
                                        'identifier': 9855138,
                                        'width': -2603229546405664597,
                                        'height': -2845600932063104051,
                                    },
                            {
                                        'identifier': 4826887,
                                        'width': -7024506333728626958,
                                        'height': -2642968717325735835,
                                    },
                            {
                                        'identifier': 6911295,
                                        'width': 7421562035793972458,
                                        'height': 6378896819232121549,
                                    },
                            {
                                        'identifier': 5562144,
                                        'width': 379979257715496892,
                                        'height': 4382802185204782632,
                                    },
                            {
                                        'identifier': -524682,
                                        'width': -4501298417857160034,
                                        'height': -1337050168549416676,
                                    },
                            {
                                        'identifier': 428493,
                                        'width': 7895309242616108324,
                                        'height': 8289235769392067109,
                                    },
                            {
                                        'identifier': 8729133,
                                        'width': -8363331747059949042,
                                        'height': -5084748990087042074,
                                    },
                            {
                                        'identifier': 1112574,
                                        'width': 1747459679598200870,
                                        'height': 3099290163347413706,
                                    },
                            {
                                        'identifier': 541585,
                                        'width': -3876695224594899969,
                                        'height': 7937846504408285054,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9366465,
                                        'source_nw_x_pixel': -864773783595847518,
                                        'source_nw_y_pixel': -4869244320765039853,
                                        'source_pixel_width': -4272695075117905651,
                                        'source_pixel_height': -4764317080433705822,
                                        'rotation': -7225633447609123796,
                                        'virtual_nw_x_pixel': 1335504150,
                                        'virtual_nw_y_pixel': -651519009,
                                        'virtual_width': -1970902181,
                                        'virtual_height': 1791158395,
                                    },
                            {
                                        'source_monitor': 1739542,
                                        'source_nw_x_pixel': -7519960502199648779,
                                        'source_nw_y_pixel': -9042521675429060804,
                                        'source_pixel_width': -5224564484319317232,
                                        'source_pixel_height': -3309134791523483584,
                                        'rotation': -7294004046673617004,
                                        'virtual_nw_x_pixel': 359785520,
                                        'virtual_nw_y_pixel': -375024844,
                                        'virtual_width': -1847651132,
                                        'virtual_height': 1146476190,
                                    },
                            {
                                        'source_monitor': 5728100,
                                        'source_nw_x_pixel': -4153173530582277484,
                                        'source_nw_y_pixel': -6331417661801324926,
                                        'source_pixel_width': -6510190136641424372,
                                        'source_pixel_height': -2312875858872845487,
                                        'rotation': -5592288694944669339,
                                        'virtual_nw_x_pixel': 1318741664,
                                        'virtual_nw_y_pixel': 1093898870,
                                        'virtual_width': -654602545,
                                        'virtual_height': -454978762,
                                    },
                            {
                                        'source_monitor': 9059832,
                                        'source_nw_x_pixel': -6968751525688555792,
                                        'source_nw_y_pixel': -1408013027083364955,
                                        'source_pixel_width': -5482839666382609611,
                                        'source_pixel_height': -5276432839884476302,
                                        'rotation': -1726295888334355692,
                                        'virtual_nw_x_pixel': 1040307216,
                                        'virtual_nw_y_pixel': -277250747,
                                        'virtual_width': -1613337875,
                                        'virtual_height': 852257492,
                                    },
                            {
                                        'source_monitor': 816418,
                                        'source_nw_x_pixel': -5273533980814352083,
                                        'source_nw_y_pixel': -3541271679550504617,
                                        'source_pixel_width': -9201396346614606884,
                                        'source_pixel_height': -4250135660328101479,
                                        'rotation': -1723545680580008567,
                                        'virtual_nw_x_pixel': 1446258454,
                                        'virtual_nw_y_pixel': -1811791508,
                                        'virtual_width': 1294677019,
                                        'virtual_height': 983959259,
                                    },
                            {
                                        'source_monitor': 7532707,
                                        'source_nw_x_pixel': -1093315475750915533,
                                        'source_nw_y_pixel': -8001636196645270062,
                                        'source_pixel_width': -3732996188212965644,
                                        'source_pixel_height': -1534065966684579369,
                                        'rotation': -476844393993534149,
                                        'virtual_nw_x_pixel': 470403338,
                                        'virtual_nw_y_pixel': -444112877,
                                        'virtual_width': -55385157,
                                        'virtual_height': -1204900023,
                                    },
                            {
                                        'source_monitor': 5694618,
                                        'source_nw_x_pixel': -6965843906213186554,
                                        'source_nw_y_pixel': -577472254031886406,
                                        'source_pixel_width': -5321462169000861085,
                                        'source_pixel_height': -8281764306038292711,
                                        'rotation': -1608662066718344951,
                                        'virtual_nw_x_pixel': -885348617,
                                        'virtual_nw_y_pixel': 1118372946,
                                        'virtual_width': 10050810,
                                        'virtual_height': 808891015,
                                    },
                            {
                                        'source_monitor': 4090063,
                                        'source_nw_x_pixel': -7496776877062849616,
                                        'source_nw_y_pixel': -2628728397318992224,
                                        'source_pixel_width': -2995689176334096526,
                                        'source_pixel_height': -6291453586701890353,
                                        'rotation': -933714556679554767,
                                        'virtual_nw_x_pixel': -1602696850,
                                        'virtual_nw_y_pixel': -997721507,
                                        'virtual_width': -612836481,
                                        'virtual_height': -297438197,
                                    },
                            {
                                        'source_monitor': 2092541,
                                        'source_nw_x_pixel': -7928613914387901466,
                                        'source_nw_y_pixel': -1800629730964953822,
                                        'source_pixel_width': -3948749201559256319,
                                        'source_pixel_height': -3806609514963726422,
                                        'rotation': -8100927206881361162,
                                        'virtual_nw_x_pixel': 1657150129,
                                        'virtual_nw_y_pixel': 743880712,
                                        'virtual_width': -943252190,
                                        'virtual_height': 81152394,
                                    },
                            {
                                        'source_monitor': 9917163,
                                        'source_nw_x_pixel': -3306251333430013483,
                                        'source_nw_y_pixel': -3615006304853057219,
                                        'source_pixel_width': -1146428976678384479,
                                        'source_pixel_height': -8024627657054475034,
                                        'rotation': -121847071227169478,
                                        'virtual_nw_x_pixel': -1857287242,
                                        'virtual_nw_y_pixel': -1916052875,
                                        'virtual_width': 226970018,
                                        'virtual_height': -1317252053,
                                    },
                        ],
                },
                {
                    'description': 'ǓƽʲBƩȽ\u038bLɳӌ˾ӄ\x9cÍǏɥģ2ӉұXĚtmҜͻΡ~ɰп',
                    'monitors': [
                            {
                                        'identifier': 7349958,
                                        'width': -2233874611433809666,
                                        'height': -8918049611383812507,
                                    },
                            {
                                        'identifier': 441028,
                                        'width': -4847121652341419233,
                                        'height': 1322023159522005669,
                                    },
                            {
                                        'identifier': 407712,
                                        'width': 6848606832007639158,
                                        'height': -5907742499987170590,
                                    },
                            {
                                        'identifier': 9527698,
                                        'width': 6347848846175136361,
                                        'height': -1556025950311399454,
                                    },
                            {
                                        'identifier': 8709238,
                                        'width': -3022706927443076925,
                                        'height': -2095503954055035281,
                                    },
                            {
                                        'identifier': 8323010,
                                        'width': 2101106497030945112,
                                        'height': -4701046979058338943,
                                    },
                            {
                                        'identifier': -354807,
                                        'width': 2721755567022652134,
                                        'height': -7231609690960448254,
                                    },
                            {
                                        'identifier': 288152,
                                        'width': 6953618552562825667,
                                        'height': -6842721734781447989,
                                    },
                            {
                                        'identifier': 7660516,
                                        'width': -1794173983156385209,
                                        'height': 616786455633833735,
                                    },
                            {
                                        'identifier': 1986301,
                                        'width': 6572253429959182556,
                                        'height': -3971392120792176335,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9774991,
                                        'source_nw_x_pixel': -8233975864169078291,
                                        'source_nw_y_pixel': -5398191089076887011,
                                        'source_pixel_width': -5926349123892528961,
                                        'source_pixel_height': -4358862686609975731,
                                        'rotation': -8521533850636937457,
                                        'virtual_nw_x_pixel': -1401614046,
                                        'virtual_nw_y_pixel': 1703160433,
                                        'virtual_width': -635112776,
                                        'virtual_height': 1628405385,
                                    },
                            {
                                        'source_monitor': 4660041,
                                        'source_nw_x_pixel': -3830897191671955063,
                                        'source_nw_y_pixel': -5292712725097504867,
                                        'source_pixel_width': -3568518903007498291,
                                        'source_pixel_height': -1827540864267836674,
                                        'rotation': -2583685891637424973,
                                        'virtual_nw_x_pixel': -775899671,
                                        'virtual_nw_y_pixel': 75089038,
                                        'virtual_width': -901524496,
                                        'virtual_height': 1611717083,
                                    },
                            {
                                        'source_monitor': 3749956,
                                        'source_nw_x_pixel': -5972695447310232580,
                                        'source_nw_y_pixel': -6032675927951875683,
                                        'source_pixel_width': -1665857471019713627,
                                        'source_pixel_height': -7685950778063578166,
                                        'rotation': -4376605307783742247,
                                        'virtual_nw_x_pixel': -1428988956,
                                        'virtual_nw_y_pixel': -406461582,
                                        'virtual_width': 1253002244,
                                        'virtual_height': 1447159331,
                                    },
                            {
                                        'source_monitor': 4388224,
                                        'source_nw_x_pixel': -288920670243588805,
                                        'source_nw_y_pixel': -3132846385561214658,
                                        'source_pixel_width': -1585255275143522998,
                                        'source_pixel_height': -6582934489102924332,
                                        'rotation': -2607627375290742727,
                                        'virtual_nw_x_pixel': -515346693,
                                        'virtual_nw_y_pixel': 1384210124,
                                        'virtual_width': -389398366,
                                        'virtual_height': -1463691135,
                                    },
                            {
                                        'source_monitor': 2712314,
                                        'source_nw_x_pixel': -3452006515822091974,
                                        'source_nw_y_pixel': -3056347399927743154,
                                        'source_pixel_width': -2141576505784434290,
                                        'source_pixel_height': -694809957147732270,
                                        'rotation': -7758065090306846774,
                                        'virtual_nw_x_pixel': -956782207,
                                        'virtual_nw_y_pixel': 1705307410,
                                        'virtual_width': 403406092,
                                        'virtual_height': 95933759,
                                    },
                            {
                                        'source_monitor': 2909664,
                                        'source_nw_x_pixel': -7265543786334450561,
                                        'source_nw_y_pixel': -2269887493232275695,
                                        'source_pixel_width': -3664582600344007941,
                                        'source_pixel_height': -6415485859636825169,
                                        'rotation': -6648996083554506791,
                                        'virtual_nw_x_pixel': 1968691626,
                                        'virtual_nw_y_pixel': 632510102,
                                        'virtual_width': 1485764774,
                                        'virtual_height': 1198145976,
                                    },
                            {
                                        'source_monitor': 5990924,
                                        'source_nw_x_pixel': -8859567937718263840,
                                        'source_nw_y_pixel': -5235295526859922269,
                                        'source_pixel_width': -3377339309903820971,
                                        'source_pixel_height': -1159007355520177689,
                                        'rotation': -6168737583657039713,
                                        'virtual_nw_x_pixel': -1847045181,
                                        'virtual_nw_y_pixel': 826954087,
                                        'virtual_width': -1621438439,
                                        'virtual_height': 1712379213,
                                    },
                            {
                                        'source_monitor': 1335251,
                                        'source_nw_x_pixel': -7748883790005301065,
                                        'source_nw_y_pixel': -3092550826841145806,
                                        'source_pixel_width': -2026293454924218880,
                                        'source_pixel_height': -3597178371449542218,
                                        'rotation': -7248838250463744799,
                                        'virtual_nw_x_pixel': -1349466551,
                                        'virtual_nw_y_pixel': 1747523391,
                                        'virtual_width': -1492762186,
                                        'virtual_height': -268612843,
                                    },
                            {
                                        'source_monitor': 5897041,
                                        'source_nw_x_pixel': -4520971795799206685,
                                        'source_nw_y_pixel': -3502621149979846351,
                                        'source_pixel_width': -8345659931554682013,
                                        'source_pixel_height': -5023069971336639510,
                                        'rotation': -5247638615067687649,
                                        'virtual_nw_x_pixel': 1980718985,
                                        'virtual_nw_y_pixel': -1655078918,
                                        'virtual_width': -873657626,
                                        'virtual_height': 1469426634,
                                    },
                            {
                                        'source_monitor': 7980533,
                                        'source_nw_x_pixel': -3233386009346675974,
                                        'source_nw_y_pixel': -6745630698565356178,
                                        'source_pixel_width': -7437167775428550257,
                                        'source_pixel_height': -584133161753122033,
                                        'rotation': -1400514352653056731,
                                        'virtual_nw_x_pixel': 1523116440,
                                        'virtual_nw_y_pixel': 1249526331,
                                        'virtual_width': 1134257368,
                                        'virtual_height': 1956453355,
                                    },
                        ],
                },
                {
                    'description': 'Ŷ҆IŢBDӈӃϗͶӽʩ2ĨĪʂѣΉ;ƬΟѲʨԜһсȣЖ\x8eЯ',
                    'monitors': [
                            {
                                        'identifier': 2624557,
                                        'width': -6808954553597502428,
                                        'height': 3324164068976356975,
                                    },
                            {
                                        'identifier': 1575535,
                                        'width': 8087913095182941965,
                                        'height': 9129847579356904372,
                                    },
                            {
                                        'identifier': 9444355,
                                        'width': 7330385061229207421,
                                        'height': -419500036255825878,
                                    },
                            {
                                        'identifier': 6390199,
                                        'width': -5400753718465671085,
                                        'height': 1126867834661213186,
                                    },
                            {
                                        'identifier': 5704895,
                                        'width': -113038173697069229,
                                        'height': 5614801782268906357,
                                    },
                            {
                                        'identifier': 9390486,
                                        'width': -7657223480476513676,
                                        'height': 6664336092083790753,
                                    },
                            {
                                        'identifier': 8580527,
                                        'width': -6134383238254789307,
                                        'height': -2704144822805950800,
                                    },
                            {
                                        'identifier': 2728997,
                                        'width': 5663794138121789318,
                                        'height': 2515692287175506530,
                                    },
                            {
                                        'identifier': 9815474,
                                        'width': -4477908613931007059,
                                        'height': -7247621050967879891,
                                    },
                            {
                                        'identifier': 4991824,
                                        'width': 5388946804539665354,
                                        'height': 475578724543108075,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1790234,
                                        'source_nw_x_pixel': -8908830338946617042,
                                        'source_nw_y_pixel': -615852723458333003,
                                        'source_pixel_width': -5189926851364417787,
                                        'source_pixel_height': -7313917437862300465,
                                        'rotation': -1579736053546285496,
                                        'virtual_nw_x_pixel': 261471944,
                                        'virtual_nw_y_pixel': -1261486517,
                                        'virtual_width': 20053335,
                                        'virtual_height': -1151734091,
                                    },
                            {
                                        'source_monitor': 7176474,
                                        'source_nw_x_pixel': -6881366193263294937,
                                        'source_nw_y_pixel': -1959741998133715432,
                                        'source_pixel_width': -5480900643821747191,
                                        'source_pixel_height': -1526745154946750857,
                                        'rotation': -6559469088406295924,
                                        'virtual_nw_x_pixel': 1776799026,
                                        'virtual_nw_y_pixel': -164890337,
                                        'virtual_width': -18100857,
                                        'virtual_height': -862711775,
                                    },
                            {
                                        'source_monitor': -288176,
                                        'source_nw_x_pixel': -5983963697893271318,
                                        'source_nw_y_pixel': -1764444326954374677,
                                        'source_pixel_width': -8161866923848106346,
                                        'source_pixel_height': -4672371477762487984,
                                        'rotation': -5553139551877286997,
                                        'virtual_nw_x_pixel': -439484138,
                                        'virtual_nw_y_pixel': 279368448,
                                        'virtual_width': 1979371649,
                                        'virtual_height': -1068899637,
                                    },
                            {
                                        'source_monitor': 7661582,
                                        'source_nw_x_pixel': -7788762576253038423,
                                        'source_nw_y_pixel': -4853749720661136359,
                                        'source_pixel_width': -174784542915211020,
                                        'source_pixel_height': -7493926941481609546,
                                        'rotation': -2652808909536188421,
                                        'virtual_nw_x_pixel': -654600156,
                                        'virtual_nw_y_pixel': 1723132715,
                                        'virtual_width': 178833289,
                                        'virtual_height': -1334321406,
                                    },
                            {
                                        'source_monitor': 6688956,
                                        'source_nw_x_pixel': -150534755681962522,
                                        'source_nw_y_pixel': -7404296330980481533,
                                        'source_pixel_width': -4063180728184579644,
                                        'source_pixel_height': -598084112962127824,
                                        'rotation': -1502825041529103862,
                                        'virtual_nw_x_pixel': 1630500220,
                                        'virtual_nw_y_pixel': 22706557,
                                        'virtual_width': 837278912,
                                        'virtual_height': -1256120173,
                                    },
                            {
                                        'source_monitor': 9095121,
                                        'source_nw_x_pixel': -6885520330729942705,
                                        'source_nw_y_pixel': -5355923476148169265,
                                        'source_pixel_width': -4098163551714424577,
                                        'source_pixel_height': -4758303199144455329,
                                        'rotation': -1989784535200304436,
                                        'virtual_nw_x_pixel': 430780510,
                                        'virtual_nw_y_pixel': 1057202307,
                                        'virtual_width': 900573029,
                                        'virtual_height': -1770893723,
                                    },
                            {
                                        'source_monitor': 477546,
                                        'source_nw_x_pixel': -2694463208011589273,
                                        'source_nw_y_pixel': -8648021935569193859,
                                        'source_pixel_width': -113315161361788841,
                                        'source_pixel_height': -1766041114012676046,
                                        'rotation': -2526099715261723103,
                                        'virtual_nw_x_pixel': 1211097602,
                                        'virtual_nw_y_pixel': 364049551,
                                        'virtual_width': 1833230910,
                                        'virtual_height': 1488780828,
                                    },
                            {
                                        'source_monitor': 9419813,
                                        'source_nw_x_pixel': -5516107205698828527,
                                        'source_nw_y_pixel': -6724266599229865045,
                                        'source_pixel_width': -6876596042200775605,
                                        'source_pixel_height': -7873929168546670805,
                                        'rotation': -8816168860670240255,
                                        'virtual_nw_x_pixel': -1098416861,
                                        'virtual_nw_y_pixel': 1829247525,
                                        'virtual_width': 754750950,
                                        'virtual_height': 267103565,
                                    },
                            {
                                        'source_monitor': 1233256,
                                        'source_nw_x_pixel': -470478928929352235,
                                        'source_nw_y_pixel': -223925267847930809,
                                        'source_pixel_width': -7360458935246096547,
                                        'source_pixel_height': -7950371308564633851,
                                        'rotation': -5158943742039305434,
                                        'virtual_nw_x_pixel': 962576179,
                                        'virtual_nw_y_pixel': -1690802,
                                        'virtual_width': 1023170562,
                                        'virtual_height': 541426205,
                                    },
                            {
                                        'source_monitor': 4319961,
                                        'source_nw_x_pixel': -1461871070749509095,
                                        'source_nw_y_pixel': -1525276787789888266,
                                        'source_pixel_width': -1954731993742188417,
                                        'source_pixel_height': -7603530798106055681,
                                        'rotation': -6762075135644349108,
                                        'virtual_nw_x_pixel': 1263956615,
                                        'virtual_nw_y_pixel': 768256554,
                                        'virtual_width': -1493551188,
                                        'virtual_height': -574376693,
                                    },
                        ],
                },
                {
                    'description': 'ħσǸԝϭ\x7fɇʛԋÚʃԙɩ\x8aθƠДѼňȺЀЎƊ>@ѽŅǚӶΖ',
                    'monitors': [
                            {
                                        'identifier': 5782089,
                                        'width': 3121405055130232322,
                                        'height': 2721576763005173735,
                                    },
                            {
                                        'identifier': 1299431,
                                        'width': 3494342357929680502,
                                        'height': -3026493897274586359,
                                    },
                            {
                                        'identifier': 9386169,
                                        'width': -5242484751646327330,
                                        'height': 1268014274246390150,
                                    },
                            {
                                        'identifier': 4432173,
                                        'width': -5989234808921840386,
                                        'height': 7526574649241558137,
                                    },
                            {
                                        'identifier': 7648628,
                                        'width': -5178131822170621276,
                                        'height': -410749942521342221,
                                    },
                            {
                                        'identifier': 9867551,
                                        'width': -1208806061026978217,
                                        'height': -5898344866245381593,
                                    },
                            {
                                        'identifier': -776994,
                                        'width': 7761581706997202247,
                                        'height': 8773226978974019070,
                                    },
                            {
                                        'identifier': 6951748,
                                        'width': -1937986412573070424,
                                        'height': -3597410112974087139,
                                    },
                            {
                                        'identifier': 1535462,
                                        'width': -7608942974181548548,
                                        'height': 7376880286956022203,
                                    },
                            {
                                        'identifier': 4102040,
                                        'width': -632079163123227440,
                                        'height': 1534560097825737757,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8009266,
                                        'source_nw_x_pixel': -3930937190186082137,
                                        'source_nw_y_pixel': -3025466231437405551,
                                        'source_pixel_width': -1354982681965928119,
                                        'source_pixel_height': -5683299983794304919,
                                        'rotation': -6446883887723569997,
                                        'virtual_nw_x_pixel': -527674153,
                                        'virtual_nw_y_pixel': -1040261898,
                                        'virtual_width': 208880661,
                                        'virtual_height': 923499569,
                                    },
                            {
                                        'source_monitor': 4852545,
                                        'source_nw_x_pixel': -434084072900568127,
                                        'source_nw_y_pixel': -746529886267725554,
                                        'source_pixel_width': -6906915404611867540,
                                        'source_pixel_height': -7432585921969243540,
                                        'rotation': -351305904894872988,
                                        'virtual_nw_x_pixel': -171476370,
                                        'virtual_nw_y_pixel': 1282344698,
                                        'virtual_width': 233147790,
                                        'virtual_height': 1253163627,
                                    },
                            {
                                        'source_monitor': 4278061,
                                        'source_nw_x_pixel': -5712648966061830254,
                                        'source_nw_y_pixel': -4157910462681121788,
                                        'source_pixel_width': -390292778231763242,
                                        'source_pixel_height': -5190995792326844625,
                                        'rotation': -4026822164572204660,
                                        'virtual_nw_x_pixel': -397846832,
                                        'virtual_nw_y_pixel': -1497884004,
                                        'virtual_width': 1426496333,
                                        'virtual_height': 848249210,
                                    },
                            {
                                        'source_monitor': 6191834,
                                        'source_nw_x_pixel': -6349788969836693868,
                                        'source_nw_y_pixel': -7464134454717803609,
                                        'source_pixel_width': -7566305409289440054,
                                        'source_pixel_height': -2887648379643465657,
                                        'rotation': -3265284695476886944,
                                        'virtual_nw_x_pixel': -427539264,
                                        'virtual_nw_y_pixel': -866910464,
                                        'virtual_width': -845681562,
                                        'virtual_height': 1174380983,
                                    },
                            {
                                        'source_monitor': -120126,
                                        'source_nw_x_pixel': -7791092667305789097,
                                        'source_nw_y_pixel': -5185081950605812879,
                                        'source_pixel_width': -8780174136523474457,
                                        'source_pixel_height': -6282290260257124805,
                                        'rotation': -91741180794870158,
                                        'virtual_nw_x_pixel': -565302576,
                                        'virtual_nw_y_pixel': 604940565,
                                        'virtual_width': 1007226284,
                                        'virtual_height': -58411867,
                                    },
                            {
                                        'source_monitor': 6149221,
                                        'source_nw_x_pixel': -8338180929482928824,
                                        'source_nw_y_pixel': -8965569774908447209,
                                        'source_pixel_width': -8831218891553412910,
                                        'source_pixel_height': -596737971107444073,
                                        'rotation': -1913225790895770088,
                                        'virtual_nw_x_pixel': -214331008,
                                        'virtual_nw_y_pixel': 1856312190,
                                        'virtual_width': 1263243104,
                                        'virtual_height': -1858974878,
                                    },
                            {
                                        'source_monitor': 876177,
                                        'source_nw_x_pixel': -5522135769798867941,
                                        'source_nw_y_pixel': -1958124392513142702,
                                        'source_pixel_width': -5910234317478746570,
                                        'source_pixel_height': -8766045701127128172,
                                        'rotation': -7192130665188364149,
                                        'virtual_nw_x_pixel': 372743295,
                                        'virtual_nw_y_pixel': -1135904375,
                                        'virtual_width': -11782418,
                                        'virtual_height': -65758476,
                                    },
                            {
                                        'source_monitor': 8737335,
                                        'source_nw_x_pixel': -3850533029558792742,
                                        'source_nw_y_pixel': -9213913280887246178,
                                        'source_pixel_width': -7957654593287404066,
                                        'source_pixel_height': -7886128510934163673,
                                        'rotation': -8277783483400490112,
                                        'virtual_nw_x_pixel': 629007158,
                                        'virtual_nw_y_pixel': 1201695739,
                                        'virtual_width': -51373254,
                                        'virtual_height': 518147785,
                                    },
                            {
                                        'source_monitor': 190283,
                                        'source_nw_x_pixel': -8215643136345268435,
                                        'source_nw_y_pixel': -7089989710870995862,
                                        'source_pixel_width': -8035271656028417693,
                                        'source_pixel_height': -6061759294621352978,
                                        'rotation': -3690752304165366045,
                                        'virtual_nw_x_pixel': -1326904413,
                                        'virtual_nw_y_pixel': -1488927844,
                                        'virtual_width': 950797384,
                                        'virtual_height': 1179298536,
                                    },
                            {
                                        'source_monitor': 1108652,
                                        'source_nw_x_pixel': -7694343861886076647,
                                        'source_nw_y_pixel': -3690062333263308059,
                                        'source_pixel_width': -4739724630345517246,
                                        'source_pixel_height': -8967118094962163707,
                                        'rotation': -6440601818930230188,
                                        'virtual_nw_x_pixel': -1446692481,
                                        'virtual_nw_y_pixel': 1433883251,
                                        'virtual_width': -1978346554,
                                        'virtual_height': 1465725365,
                                    },
                        ],
                },
                {
                    'description': 'ȅǧȑӫτ˵ĈǵЪÛεʯӠпŜɔԣɴÿԜӄπҹƨˍѫѲθљС',
                    'monitors': [
                            {
                                        'identifier': 5834553,
                                        'width': -4162184167257443776,
                                        'height': 2195925071416371659,
                                    },
                            {
                                        'identifier': 5824770,
                                        'width': -6273627005816018518,
                                        'height': -8935733278382469780,
                                    },
                            {
                                        'identifier': 3445393,
                                        'width': 7195570411607432156,
                                        'height': 4619457346425633640,
                                    },
                            {
                                        'identifier': 3717771,
                                        'width': 2107115840206307587,
                                        'height': -496831780077879989,
                                    },
                            {
                                        'identifier': 7111635,
                                        'width': -8836622775203613705,
                                        'height': 1090440736511779753,
                                    },
                            {
                                        'identifier': 446195,
                                        'width': -8087343769184839410,
                                        'height': 7118874390666789385,
                                    },
                            {
                                        'identifier': 9296754,
                                        'width': 8900631661159078920,
                                        'height': -2176449983144775735,
                                    },
                            {
                                        'identifier': 2959029,
                                        'width': -434059809840904017,
                                        'height': -4280982667909224772,
                                    },
                            {
                                        'identifier': 8375340,
                                        'width': 6779223657057312041,
                                        'height': -6692376862058701255,
                                    },
                            {
                                        'identifier': 3613643,
                                        'width': 3724709548795120214,
                                        'height': 3538805247384906469,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -861282,
                                        'source_nw_x_pixel': -2044557421383749537,
                                        'source_nw_y_pixel': -4144888758610909234,
                                        'source_pixel_width': -3422240697001973690,
                                        'source_pixel_height': -1560197817695313200,
                                        'rotation': -2739990352276533917,
                                        'virtual_nw_x_pixel': -1135537667,
                                        'virtual_nw_y_pixel': -265315328,
                                        'virtual_width': -439917335,
                                        'virtual_height': 353590701,
                                    },
                            {
                                        'source_monitor': 2216098,
                                        'source_nw_x_pixel': -9006424410212335821,
                                        'source_nw_y_pixel': -5953191258572452109,
                                        'source_pixel_width': -6332506190433880222,
                                        'source_pixel_height': -2025689602977704152,
                                        'rotation': -6330637839113480993,
                                        'virtual_nw_x_pixel': 1119311344,
                                        'virtual_nw_y_pixel': 1220385223,
                                        'virtual_width': -672106264,
                                        'virtual_height': -420916829,
                                    },
                            {
                                        'source_monitor': 9297695,
                                        'source_nw_x_pixel': -8011403709562397222,
                                        'source_nw_y_pixel': -1186953662675512904,
                                        'source_pixel_width': -8778292336841671705,
                                        'source_pixel_height': -8595459775420461542,
                                        'rotation': -2978519750433148356,
                                        'virtual_nw_x_pixel': -256940372,
                                        'virtual_nw_y_pixel': -88292519,
                                        'virtual_width': 1678206195,
                                        'virtual_height': -847036135,
                                    },
                            {
                                        'source_monitor': 4546343,
                                        'source_nw_x_pixel': -2766646640747168760,
                                        'source_nw_y_pixel': -7496262638466550071,
                                        'source_pixel_width': -8254489553342944987,
                                        'source_pixel_height': -1525622727818719573,
                                        'rotation': -213780181462218701,
                                        'virtual_nw_x_pixel': 72845500,
                                        'virtual_nw_y_pixel': 299376127,
                                        'virtual_width': -54608419,
                                        'virtual_height': -272623588,
                                    },
                            {
                                        'source_monitor': -982164,
                                        'source_nw_x_pixel': -2597196712930342538,
                                        'source_nw_y_pixel': -6705272959929352395,
                                        'source_pixel_width': -7093407460354443854,
                                        'source_pixel_height': -169994876934078239,
                                        'rotation': -6339334971754289295,
                                        'virtual_nw_x_pixel': -1952695784,
                                        'virtual_nw_y_pixel': -1702505704,
                                        'virtual_width': -1823808114,
                                        'virtual_height': -332024345,
                                    },
                            {
                                        'source_monitor': -582679,
                                        'source_nw_x_pixel': -704422447901348896,
                                        'source_nw_y_pixel': -7779680608758034208,
                                        'source_pixel_width': -7482574459197953332,
                                        'source_pixel_height': -2292963978106324138,
                                        'rotation': -2395121810118899984,
                                        'virtual_nw_x_pixel': -1607977610,
                                        'virtual_nw_y_pixel': 1063499081,
                                        'virtual_width': -1657120157,
                                        'virtual_height': 1408481672,
                                    },
                            {
                                        'source_monitor': 212117,
                                        'source_nw_x_pixel': -2877818907486437755,
                                        'source_nw_y_pixel': -7729091334145503599,
                                        'source_pixel_width': -6407269595338821698,
                                        'source_pixel_height': -3047336181630426623,
                                        'rotation': -6344185398798427071,
                                        'virtual_nw_x_pixel': -849820423,
                                        'virtual_nw_y_pixel': -1511935018,
                                        'virtual_width': -589049186,
                                        'virtual_height': 1827424055,
                                    },
                            {
                                        'source_monitor': 7959702,
                                        'source_nw_x_pixel': -1012237260900353519,
                                        'source_nw_y_pixel': -6250929315306596127,
                                        'source_pixel_width': -1332079636293734951,
                                        'source_pixel_height': -1692361254479487369,
                                        'rotation': -7641659023015912914,
                                        'virtual_nw_x_pixel': -1513169406,
                                        'virtual_nw_y_pixel': -457165144,
                                        'virtual_width': 859996296,
                                        'virtual_height': -1346510779,
                                    },
                            {
                                        'source_monitor': 446699,
                                        'source_nw_x_pixel': -489633967625834961,
                                        'source_nw_y_pixel': -2661843955290037213,
                                        'source_pixel_width': -4959635080738230262,
                                        'source_pixel_height': -2152236314421783970,
                                        'rotation': -4442453679474382532,
                                        'virtual_nw_x_pixel': 1863366015,
                                        'virtual_nw_y_pixel': -490181823,
                                        'virtual_width': -1626772151,
                                        'virtual_height': 1285995929,
                                    },
                            {
                                        'source_monitor': 4983752,
                                        'source_nw_x_pixel': -8574695048631768046,
                                        'source_nw_y_pixel': -2869489027105333057,
                                        'source_pixel_width': -6870135142625265723,
                                        'source_pixel_height': -3001908904299195678,
                                        'rotation': -3403005361318136334,
                                        'virtual_nw_x_pixel': -916178824,
                                        'virtual_nw_y_pixel': -531105848,
                                        'virtual_width': -1639742764,
                                        'virtual_height': -849281048,
                                    },
                        ],
                },
                {
                    'description': '˜ҌҼ\\ǱțԊѡɴƚȉΙƘӡ8ӵӴЅ4ӒσѫėɲɇæőÚԎҀ',
                    'monitors': [
                            {
                                        'identifier': 417526,
                                        'width': -8784797168558006061,
                                        'height': 4887298373203771417,
                                    },
                            {
                                        'identifier': 6504221,
                                        'width': -3216596500243604207,
                                        'height': -4602162690587527403,
                                    },
                            {
                                        'identifier': 1309867,
                                        'width': 421656119010433338,
                                        'height': -7192810776345142771,
                                    },
                            {
                                        'identifier': 7611579,
                                        'width': -4720105446224097628,
                                        'height': -7614942218558733245,
                                    },
                            {
                                        'identifier': 8401503,
                                        'width': 960677454306809212,
                                        'height': -6006884822394882589,
                                    },
                            {
                                        'identifier': -80165,
                                        'width': -4633860978867511784,
                                        'height': -1538567938624238699,
                                    },
                            {
                                        'identifier': 8019844,
                                        'width': 4315591055632574198,
                                        'height': -6262461377248062330,
                                    },
                            {
                                        'identifier': -932570,
                                        'width': -9164063607712597244,
                                        'height': 2332107629815090036,
                                    },
                            {
                                        'identifier': 6467644,
                                        'width': -1480072150137723824,
                                        'height': 2187143296325364567,
                                    },
                            {
                                        'identifier': 3301045,
                                        'width': 2887193715260651518,
                                        'height': 1968314954564109270,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1002786,
                                        'source_nw_x_pixel': -8346170124091861903,
                                        'source_nw_y_pixel': -4434455314442555506,
                                        'source_pixel_width': -851707351004589240,
                                        'source_pixel_height': -2100532793116034929,
                                        'rotation': -1171574689481268928,
                                        'virtual_nw_x_pixel': -290895320,
                                        'virtual_nw_y_pixel': 714866716,
                                        'virtual_width': -180219736,
                                        'virtual_height': -1997946568,
                                    },
                            {
                                        'source_monitor': 5515365,
                                        'source_nw_x_pixel': -1896047034647473567,
                                        'source_nw_y_pixel': -725394376530490994,
                                        'source_pixel_width': -7650189084883525934,
                                        'source_pixel_height': -6203093452979765277,
                                        'rotation': -3959625421331586231,
                                        'virtual_nw_x_pixel': 95800825,
                                        'virtual_nw_y_pixel': 1221424601,
                                        'virtual_width': -281263744,
                                        'virtual_height': -1534378869,
                                    },
                            {
                                        'source_monitor': 7450638,
                                        'source_nw_x_pixel': -3275907428442398695,
                                        'source_nw_y_pixel': -5595335081525404716,
                                        'source_pixel_width': -8020161428887848466,
                                        'source_pixel_height': -3925666981486013366,
                                        'rotation': -2993970087806652920,
                                        'virtual_nw_x_pixel': 800629170,
                                        'virtual_nw_y_pixel': 213042270,
                                        'virtual_width': 1191790947,
                                        'virtual_height': 147392999,
                                    },
                            {
                                        'source_monitor': 5356541,
                                        'source_nw_x_pixel': -7744276744870065642,
                                        'source_nw_y_pixel': -6458298393025551598,
                                        'source_pixel_width': -7760807965882379802,
                                        'source_pixel_height': -7692690676920199714,
                                        'rotation': -6087448686521116742,
                                        'virtual_nw_x_pixel': -1732510233,
                                        'virtual_nw_y_pixel': -89703435,
                                        'virtual_width': 1899918017,
                                        'virtual_height': 492710978,
                                    },
                            {
                                        'source_monitor': 1254289,
                                        'source_nw_x_pixel': -5938940567695378312,
                                        'source_nw_y_pixel': -3801743753698057177,
                                        'source_pixel_width': -3833570526144859883,
                                        'source_pixel_height': -1936916928398217006,
                                        'rotation': -1384250002528909522,
                                        'virtual_nw_x_pixel': -1454794847,
                                        'virtual_nw_y_pixel': 48337511,
                                        'virtual_width': 793540220,
                                        'virtual_height': -626872573,
                                    },
                            {
                                        'source_monitor': 2527113,
                                        'source_nw_x_pixel': -1914322395788666977,
                                        'source_nw_y_pixel': -6655710803938826611,
                                        'source_pixel_width': -1078455154435442135,
                                        'source_pixel_height': -1532494745344730214,
                                        'rotation': -8970939337682700102,
                                        'virtual_nw_x_pixel': 545839288,
                                        'virtual_nw_y_pixel': -1791772751,
                                        'virtual_width': -230550671,
                                        'virtual_height': -199515606,
                                    },
                            {
                                        'source_monitor': 5544069,
                                        'source_nw_x_pixel': -1947055946446906480,
                                        'source_nw_y_pixel': -5232261097599030745,
                                        'source_pixel_width': -8081357807884190364,
                                        'source_pixel_height': -7520538512548967847,
                                        'rotation': -7839003150092116753,
                                        'virtual_nw_x_pixel': 1397191114,
                                        'virtual_nw_y_pixel': 1725344939,
                                        'virtual_width': -759098247,
                                        'virtual_height': -785621949,
                                    },
                            {
                                        'source_monitor': 7354914,
                                        'source_nw_x_pixel': -6457368247183670001,
                                        'source_nw_y_pixel': -6321709170734884905,
                                        'source_pixel_width': -2473760689926051729,
                                        'source_pixel_height': -8667648115776536468,
                                        'rotation': -7272627335339472234,
                                        'virtual_nw_x_pixel': -409594941,
                                        'virtual_nw_y_pixel': 890063996,
                                        'virtual_width': 1010169740,
                                        'virtual_height': 330949684,
                                    },
                            {
                                        'source_monitor': 8068674,
                                        'source_nw_x_pixel': -5585462880809290272,
                                        'source_nw_y_pixel': -5874076402559289663,
                                        'source_pixel_width': -7038940669176328335,
                                        'source_pixel_height': -3023630129651781980,
                                        'rotation': -2821093231655209962,
                                        'virtual_nw_x_pixel': 123379982,
                                        'virtual_nw_y_pixel': -1730322532,
                                        'virtual_width': -505807842,
                                        'virtual_height': 60668981,
                                    },
                            {
                                        'source_monitor': 6432957,
                                        'source_nw_x_pixel': -2053765798412799431,
                                        'source_nw_y_pixel': -2354053031690633463,
                                        'source_pixel_width': -4590797524607805900,
                                        'source_pixel_height': -6069239532956432038,
                                        'rotation': -142478385477643723,
                                        'virtual_nw_x_pixel': -429133883,
                                        'virtual_nw_y_pixel': 1291422536,
                                        'virtual_width': 793876795,
                                        'virtual_height': -295610295,
                                    },
                        ],
                },
                {
                    'description': 'Ԁӿʸʪǔĳ4ʹǳϹ°βǘŌЩёͰԮeϳȄӯƭɏѩİоѶƞͶ',
                    'monitors': [
                            {
                                        'identifier': -282116,
                                        'width': 962101664560498023,
                                        'height': 1504901137039065832,
                                    },
                            {
                                        'identifier': 6986290,
                                        'width': 3982493597825782588,
                                        'height': -2594191901942955360,
                                    },
                            {
                                        'identifier': 6233112,
                                        'width': 8097911939940149240,
                                        'height': -9065224956950922032,
                                    },
                            {
                                        'identifier': 2131071,
                                        'width': -989473999160947409,
                                        'height': -436099802503028194,
                                    },
                            {
                                        'identifier': -782241,
                                        'width': 3944530559804289168,
                                        'height': -6979963554125268843,
                                    },
                            {
                                        'identifier': 4886274,
                                        'width': -5473337496127525677,
                                        'height': 1372931429558925529,
                                    },
                            {
                                        'identifier': 2501816,
                                        'width': -1586381153850638503,
                                        'height': -751306735172175139,
                                    },
                            {
                                        'identifier': 2870735,
                                        'width': 6257599875122558285,
                                        'height': 1724522123294085015,
                                    },
                            {
                                        'identifier': 8652404,
                                        'width': 3416028355877222139,
                                        'height': -6406327795735928465,
                                    },
                            {
                                        'identifier': 9959723,
                                        'width': 4799416965374518686,
                                        'height': -7237618596691070359,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -917761,
                                        'source_nw_x_pixel': -977401168157220224,
                                        'source_nw_y_pixel': -5607321953024275207,
                                        'source_pixel_width': -6973788524086004591,
                                        'source_pixel_height': -5626191664204917913,
                                        'rotation': -4855352682695905982,
                                        'virtual_nw_x_pixel': 762628819,
                                        'virtual_nw_y_pixel': -167091456,
                                        'virtual_width': -86473502,
                                        'virtual_height': 1177353152,
                                    },
                            {
                                        'source_monitor': 6043018,
                                        'source_nw_x_pixel': -5529369259908685425,
                                        'source_nw_y_pixel': -1009198249718560497,
                                        'source_pixel_width': -1300805708236723462,
                                        'source_pixel_height': -2587003856911432738,
                                        'rotation': -522582545723566257,
                                        'virtual_nw_x_pixel': 764211697,
                                        'virtual_nw_y_pixel': -42854195,
                                        'virtual_width': 1599844207,
                                        'virtual_height': -1701436739,
                                    },
                            {
                                        'source_monitor': 1701851,
                                        'source_nw_x_pixel': -3493602133744664622,
                                        'source_nw_y_pixel': -3105057005828334408,
                                        'source_pixel_width': -4787494343700968488,
                                        'source_pixel_height': -9196035422115502478,
                                        'rotation': -7338443710493833461,
                                        'virtual_nw_x_pixel': -962831274,
                                        'virtual_nw_y_pixel': -188000684,
                                        'virtual_width': 1354358740,
                                        'virtual_height': -1531131833,
                                    },
                            {
                                        'source_monitor': 8295789,
                                        'source_nw_x_pixel': -7666908597747786209,
                                        'source_nw_y_pixel': -3966098998158285002,
                                        'source_pixel_width': -4656391698102574242,
                                        'source_pixel_height': -8620177679213654822,
                                        'rotation': -1046118985869323967,
                                        'virtual_nw_x_pixel': 1922849058,
                                        'virtual_nw_y_pixel': -24398170,
                                        'virtual_width': -813157484,
                                        'virtual_height': 1073667082,
                                    },
                            {
                                        'source_monitor': 5837751,
                                        'source_nw_x_pixel': -6766726191249418044,
                                        'source_nw_y_pixel': -3434824468633427534,
                                        'source_pixel_width': -3470559256594474181,
                                        'source_pixel_height': -7619558913550036285,
                                        'rotation': -5277938387769148426,
                                        'virtual_nw_x_pixel': 307752165,
                                        'virtual_nw_y_pixel': -27460363,
                                        'virtual_width': -1077170244,
                                        'virtual_height': -877554760,
                                    },
                            {
                                        'source_monitor': 7738212,
                                        'source_nw_x_pixel': -1690351234560861599,
                                        'source_nw_y_pixel': -1026347239232055575,
                                        'source_pixel_width': -5213087793148555668,
                                        'source_pixel_height': -5812310914989391624,
                                        'rotation': -5416915423842967663,
                                        'virtual_nw_x_pixel': 1833652552,
                                        'virtual_nw_y_pixel': -877562132,
                                        'virtual_width': -260864195,
                                        'virtual_height': 252580649,
                                    },
                            {
                                        'source_monitor': 6605785,
                                        'source_nw_x_pixel': -2469184108697923419,
                                        'source_nw_y_pixel': -6029600695520800428,
                                        'source_pixel_width': -4318120939032101983,
                                        'source_pixel_height': -6292086434693487669,
                                        'rotation': -5487321267057364533,
                                        'virtual_nw_x_pixel': -891531710,
                                        'virtual_nw_y_pixel': 655870910,
                                        'virtual_width': 1027095943,
                                        'virtual_height': -1137774368,
                                    },
                            {
                                        'source_monitor': 8642419,
                                        'source_nw_x_pixel': -8375518072882520280,
                                        'source_nw_y_pixel': -3657953624087491563,
                                        'source_pixel_width': -8628383730708214884,
                                        'source_pixel_height': -5150062134059119774,
                                        'rotation': -9178123957885033715,
                                        'virtual_nw_x_pixel': 93357927,
                                        'virtual_nw_y_pixel': -525689922,
                                        'virtual_width': -313116141,
                                        'virtual_height': 710294223,
                                    },
                            {
                                        'source_monitor': 285785,
                                        'source_nw_x_pixel': -3916103979197383373,
                                        'source_nw_y_pixel': -6244541152921571239,
                                        'source_pixel_width': -755040140723944815,
                                        'source_pixel_height': -7544220157442466393,
                                        'rotation': -781904612408036812,
                                        'virtual_nw_x_pixel': -845517146,
                                        'virtual_nw_y_pixel': -1808981276,
                                        'virtual_width': 231588138,
                                        'virtual_height': -341274637,
                                    },
                            {
                                        'source_monitor': 6117290,
                                        'source_nw_x_pixel': -5911903307766010665,
                                        'source_nw_y_pixel': -1325994643360577613,
                                        'source_pixel_width': -8768436511619836070,
                                        'source_pixel_height': -6915737813268433022,
                                        'rotation': -1363523216176034617,
                                        'virtual_nw_x_pixel': -322659606,
                                        'virtual_nw_y_pixel': 631329288,
                                        'virtual_width': -1382056808,
                                        'virtual_height': 1058078509,
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
                                        'identifier': 1874157,
                                        'width': -5378212038033337044,
                                        'height': 2709702209982037808,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -7029002595610375100,
                                        'source_nw_y_pixel': -2037445687893023613,
                                        'source_pixel_width': -192007276022545953,
                                        'source_pixel_height': -6851910792066861493,
                                        'rotation': -3347585805056600438,
                                        'virtual_nw_x_pixel': 1535614196,
                                        'virtual_nw_y_pixel': 1832075326,
                                        'virtual_width': 551411483,
                                        'virtual_height': -385455257,
                                    },
                        ],
                },
            ],

        },
    ),
]
