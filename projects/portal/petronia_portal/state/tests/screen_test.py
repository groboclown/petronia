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
            'nw_x_pixel': 1731688419,
            'nw_y_pixel': 1327391770,
            'width': -637455442359103430,
            'height': -3626353047340293277,
            'ratio_x': -8334922164375941731,
            'ratio_y': -2056077914099309389,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -802769982,

            'nw_y_pixel': -321024606,

            'width': -4175726931149931821,

            'height': -7424727355044450258,

            'ratio_x': -7854900735580435807,

            'ratio_y': -467544197475743245,

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
                    'nw_x_pixel': -1667999240,
                    'nw_y_pixel': 993817678,
                    'width': -3376608523782348925,
                    'height': -4880927702522197619,
                    'ratio_x': -5695355985189210802,
                    'ratio_y': 3321423870419222182,
                },
                {
                    'nw_x_pixel': 104884025,
                    'nw_y_pixel': -670889203,
                    'width': -6660963292840962050,
                    'height': -575019318471649850,
                    'ratio_x': 8066583604089280080,
                    'ratio_y': -8910686326436811906,
                },
                {
                    'nw_x_pixel': -1132424500,
                    'nw_y_pixel': 1160866062,
                    'width': -5373146987062464793,
                    'height': -1649100415749430378,
                    'ratio_x': -2687915784507766911,
                    'ratio_y': -7839394880934951038,
                },
                {
                    'nw_x_pixel': 707617916,
                    'nw_y_pixel': -1979575114,
                    'width': -3688063295183563785,
                    'height': -3385003851523370351,
                    'ratio_x': 2453371622871352883,
                    'ratio_y': -3120652137414721089,
                },
                {
                    'nw_x_pixel': -660539750,
                    'nw_y_pixel': -251898800,
                    'width': -3852706313600452420,
                    'height': -1497057629793427334,
                    'ratio_x': 7687912228497896004,
                    'ratio_y': 2888231141897127828,
                },
                {
                    'nw_x_pixel': -1265859391,
                    'nw_y_pixel': -1666702287,
                    'width': -6871832585691441349,
                    'height': -3054461106050997496,
                    'ratio_x': 7027012313628719723,
                    'ratio_y': 8736930194806583989,
                },
                {
                    'nw_x_pixel': 109174961,
                    'nw_y_pixel': 536173651,
                    'width': -2210919914217762674,
                    'height': -1269684715932616473,
                    'ratio_x': -5389563021378578293,
                    'ratio_y': 6029178659931887377,
                },
                {
                    'nw_x_pixel': -1589009922,
                    'nw_y_pixel': -941909702,
                    'width': -5615094522185031696,
                    'height': -8554561184858209552,
                    'ratio_x': 6912203983634690824,
                    'ratio_y': -531021038333053452,
                },
                {
                    'nw_x_pixel': -987847099,
                    'nw_y_pixel': -1890971731,
                    'width': -7310912458805182346,
                    'height': -8969984333350230568,
                    'ratio_x': -4967042453396858978,
                    'ratio_y': -5345554994574506499,
                },
                {
                    'nw_x_pixel': -157722977,
                    'nw_y_pixel': -305260280,
                    'width': -4151019901068365193,
                    'height': -667224591072848849,
                    'ratio_x': 7347648203008064970,
                    'ratio_y': 6845287905875788875,
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
            'identifier': 693670,
            'width': -991430092738119936,
            'height': -8592705448787128378,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 3892780,

            'width': 2175800360007285267,

            'height': -2067925281425402748,

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
            'source_monitor': -679906,
            'source_nw_x_pixel': -6550483647401872024,
            'source_nw_y_pixel': -4767946582310210706,
            'source_pixel_width': -8487733161284977619,
            'source_pixel_height': -8612746576371754449,
            'rotation': -1228068455883128046,
            'virtual_nw_x_pixel': -41219655,
            'virtual_nw_y_pixel': -1820330311,
            'virtual_width': -711624740,
            'virtual_height': 157470600,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -7168048438716113260,

            'source_nw_y_pixel': -8181977893087627528,

            'source_pixel_width': -1492471135507732685,

            'source_pixel_height': -387759641132480479,

            'rotation': -877395430615371590,

            'virtual_nw_x_pixel': 562688632,

            'virtual_nw_y_pixel': 411127312,

            'virtual_width': 798533385,

            'virtual_height': -1698948586,

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
            'description': 'ŧͿϏù¼˱\x7fж˨˵џуɩʌЊƓĪҼûћ\x86ԚϒϻԄҨǆƜԈԘ',
            'monitors': [
                {
                    'identifier': 1195959,
                    'width': 2376541581607290089,
                    'height': -4877847257542738026,
                },
                {
                    'identifier': 2215243,
                    'width': 1556404240791005990,
                    'height': -3298456749180160909,
                },
                {
                    'identifier': 3526427,
                    'width': -4196871645298153058,
                    'height': -5453534334165766941,
                },
                {
                    'identifier': 488745,
                    'width': -6323532277103718102,
                    'height': -8784341315728761618,
                },
                {
                    'identifier': 1937657,
                    'width': 7646681188737953861,
                    'height': -7881719761953120953,
                },
                {
                    'identifier': 1826414,
                    'width': -5423817300845760632,
                    'height': 7553979175926798045,
                },
                {
                    'identifier': 243446,
                    'width': -5756510260431893803,
                    'height': 4649608402309285927,
                },
                {
                    'identifier': -502027,
                    'width': 970717525759707969,
                    'height': -2470087939371465154,
                },
                {
                    'identifier': 3554804,
                    'width': 2937589507183232674,
                    'height': -8168017251627720593,
                },
                {
                    'identifier': 7605385,
                    'width': -9072408412525704634,
                    'height': -7960063988872869614,
                },
            ],
            'screen': [
                {
                    'source_monitor': 6787838,
                    'source_nw_x_pixel': -5008788399091928508,
                    'source_nw_y_pixel': -1541046109965587290,
                    'source_pixel_width': -1739294421337016008,
                    'source_pixel_height': -914835530755398879,
                    'rotation': -5188590085675274413,
                    'virtual_nw_x_pixel': -234699967,
                    'virtual_nw_y_pixel': -144529097,
                    'virtual_width': 1296826209,
                    'virtual_height': 1455651693,
                },
                {
                    'source_monitor': 4521169,
                    'source_nw_x_pixel': -5928438053107095378,
                    'source_nw_y_pixel': -4485067698138099227,
                    'source_pixel_width': -3773994052111980206,
                    'source_pixel_height': -8237941552212907261,
                    'rotation': -4572448396708060161,
                    'virtual_nw_x_pixel': 515134621,
                    'virtual_nw_y_pixel': 52438207,
                    'virtual_width': -1589278296,
                    'virtual_height': 1621827403,
                },
                {
                    'source_monitor': 2197585,
                    'source_nw_x_pixel': -5668204355882700270,
                    'source_nw_y_pixel': -7042890692187079122,
                    'source_pixel_width': -5512247382182001477,
                    'source_pixel_height': -4914570702556626529,
                    'rotation': -9195613327622315468,
                    'virtual_nw_x_pixel': 86569487,
                    'virtual_nw_y_pixel': 450614772,
                    'virtual_width': -1621650502,
                    'virtual_height': -279003531,
                },
                {
                    'source_monitor': 2926647,
                    'source_nw_x_pixel': -327126658188717504,
                    'source_nw_y_pixel': -1581021807529567735,
                    'source_pixel_width': -9185967695500058802,
                    'source_pixel_height': -7524563959176610197,
                    'rotation': -8580472339483444722,
                    'virtual_nw_x_pixel': 119599469,
                    'virtual_nw_y_pixel': 316228129,
                    'virtual_width': 726286917,
                    'virtual_height': -707125717,
                },
                {
                    'source_monitor': 5640604,
                    'source_nw_x_pixel': -4391934004640811261,
                    'source_nw_y_pixel': -1884261678666438925,
                    'source_pixel_width': -1668391300239020066,
                    'source_pixel_height': -4643015683232711740,
                    'rotation': -9800272520146811,
                    'virtual_nw_x_pixel': -202816421,
                    'virtual_nw_y_pixel': 1789591331,
                    'virtual_width': 72013613,
                    'virtual_height': -618927689,
                },
                {
                    'source_monitor': 4196857,
                    'source_nw_x_pixel': -4716014856927351374,
                    'source_nw_y_pixel': -4776385507236761630,
                    'source_pixel_width': -3472707850953783315,
                    'source_pixel_height': -6263718411736680307,
                    'rotation': -3850575749570409678,
                    'virtual_nw_x_pixel': -1243186165,
                    'virtual_nw_y_pixel': -275489773,
                    'virtual_width': 348549734,
                    'virtual_height': -915237029,
                },
                {
                    'source_monitor': 2340192,
                    'source_nw_x_pixel': -2266397171425607509,
                    'source_nw_y_pixel': -6470123269407216780,
                    'source_pixel_width': -6594444529576490270,
                    'source_pixel_height': -6552181019467303762,
                    'rotation': -6139886117785015765,
                    'virtual_nw_x_pixel': -857570826,
                    'virtual_nw_y_pixel': -310839543,
                    'virtual_width': 1298716055,
                    'virtual_height': 226396259,
                },
                {
                    'source_monitor': 8925992,
                    'source_nw_x_pixel': -217461246046099260,
                    'source_nw_y_pixel': -4064269836784733151,
                    'source_pixel_width': -797620963875170052,
                    'source_pixel_height': -1116619415944485940,
                    'rotation': -2403841465197504220,
                    'virtual_nw_x_pixel': -1347521749,
                    'virtual_nw_y_pixel': -387182991,
                    'virtual_width': -93458701,
                    'virtual_height': 1808519400,
                },
                {
                    'source_monitor': 4697191,
                    'source_nw_x_pixel': -6045734985848540055,
                    'source_nw_y_pixel': -5675203654261363743,
                    'source_pixel_width': -3197853256361635605,
                    'source_pixel_height': -8744717266852270412,
                    'rotation': -4149539777059924441,
                    'virtual_nw_x_pixel': -1184126843,
                    'virtual_nw_y_pixel': 959290227,
                    'virtual_width': -176896236,
                    'virtual_height': 328691607,
                },
                {
                    'source_monitor': 4306775,
                    'source_nw_x_pixel': -8859752590370291204,
                    'source_nw_y_pixel': -1239682880915093376,
                    'source_pixel_width': -9219548582589885067,
                    'source_pixel_height': -8799509717667345264,
                    'rotation': -7503161348933877008,
                    'virtual_nw_x_pixel': 1953215935,
                    'virtual_nw_y_pixel': -1382556277,
                    'virtual_width': -895811981,
                    'virtual_height': -1248436709,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 4586901,
                    'width': 5333881978421623467,
                    'height': -3746317640268839292,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -204119504381028763,
                    'source_nw_y_pixel': -423415862492550347,
                    'source_pixel_width': -3420917084650689174,
                    'source_pixel_height': -2202917686166912444,
                    'rotation': -2213398094005522961,
                    'virtual_nw_x_pixel': 1186109228,
                    'virtual_nw_y_pixel': 560912083,
                    'virtual_width': -644425849,
                    'virtual_height': -315212981,
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
                    'description': 'ҎǠȪғŤɵӿЦŚσŏĻѽÑƕǱςѶ\x87ƛǌˍɈǾѻƬɊұâʝ',
                    'monitors': [
                            {
                                        'identifier': 7358953,
                                        'width': 7892026757168836540,
                                        'height': 24690030450196375,
                                    },
                            {
                                        'identifier': 6748025,
                                        'width': -7916431670299552084,
                                        'height': -4349636434613356029,
                                    },
                            {
                                        'identifier': 6198880,
                                        'width': 4141426231306504026,
                                        'height': 7898485502319703320,
                                    },
                            {
                                        'identifier': 3864972,
                                        'width': 7782406441700500971,
                                        'height': -4624691600040750438,
                                    },
                            {
                                        'identifier': 9565401,
                                        'width': -4472687799334856315,
                                        'height': -2994671921183177902,
                                    },
                            {
                                        'identifier': 8585361,
                                        'width': 4555124427744210321,
                                        'height': 6933453272804770046,
                                    },
                            {
                                        'identifier': -562984,
                                        'width': 4269672332975177593,
                                        'height': 1460614639067302679,
                                    },
                            {
                                        'identifier': 247683,
                                        'width': 2352115893072718345,
                                        'height': 8063021149637069048,
                                    },
                            {
                                        'identifier': 7943086,
                                        'width': -6748331406140734349,
                                        'height': -1149685904114242036,
                                    },
                            {
                                        'identifier': 3891158,
                                        'width': -820571752872707002,
                                        'height': -8942513603745888307,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 206800,
                                        'source_nw_x_pixel': -4833666738105934662,
                                        'source_nw_y_pixel': -5495748695820213557,
                                        'source_pixel_width': -7803431719048848529,
                                        'source_pixel_height': -2374455586306419432,
                                        'rotation': -539525512658795121,
                                        'virtual_nw_x_pixel': 169920474,
                                        'virtual_nw_y_pixel': 164060094,
                                        'virtual_width': -389395385,
                                        'virtual_height': 14176425,
                                    },
                            {
                                        'source_monitor': 7252505,
                                        'source_nw_x_pixel': -5003170185353769029,
                                        'source_nw_y_pixel': -7193853863014971166,
                                        'source_pixel_width': -9093703890872446747,
                                        'source_pixel_height': -8989772034915490865,
                                        'rotation': -8789096985694194502,
                                        'virtual_nw_x_pixel': -612358319,
                                        'virtual_nw_y_pixel': 450648353,
                                        'virtual_width': -1846436057,
                                        'virtual_height': 1807834844,
                                    },
                            {
                                        'source_monitor': 6957049,
                                        'source_nw_x_pixel': -237925308880394346,
                                        'source_nw_y_pixel': -4614084514767065441,
                                        'source_pixel_width': -1901628945221944132,
                                        'source_pixel_height': -2454674078773164978,
                                        'rotation': -3584755912911241221,
                                        'virtual_nw_x_pixel': 799289155,
                                        'virtual_nw_y_pixel': 1605742801,
                                        'virtual_width': 1799698302,
                                        'virtual_height': -262352544,
                                    },
                            {
                                        'source_monitor': 8034734,
                                        'source_nw_x_pixel': -5468211496265041233,
                                        'source_nw_y_pixel': -5005576282995349925,
                                        'source_pixel_width': -142203247920658889,
                                        'source_pixel_height': -1755216984427143141,
                                        'rotation': -423426048223645968,
                                        'virtual_nw_x_pixel': 1981083540,
                                        'virtual_nw_y_pixel': -1153852480,
                                        'virtual_width': 774201511,
                                        'virtual_height': 3251643,
                                    },
                            {
                                        'source_monitor': 7314454,
                                        'source_nw_x_pixel': -3695562828233719612,
                                        'source_nw_y_pixel': -730811195270917227,
                                        'source_pixel_width': -6498196987058746248,
                                        'source_pixel_height': -3971916708777791515,
                                        'rotation': -4446553178695258107,
                                        'virtual_nw_x_pixel': -102116137,
                                        'virtual_nw_y_pixel': -876042369,
                                        'virtual_width': 1940059040,
                                        'virtual_height': -446429777,
                                    },
                            {
                                        'source_monitor': -488544,
                                        'source_nw_x_pixel': -6232001702076360346,
                                        'source_nw_y_pixel': -2669116855752147560,
                                        'source_pixel_width': -7002836498958965750,
                                        'source_pixel_height': -4691281013261381634,
                                        'rotation': -3068334920476587129,
                                        'virtual_nw_x_pixel': 242346270,
                                        'virtual_nw_y_pixel': 102151263,
                                        'virtual_width': 1724920130,
                                        'virtual_height': -627881775,
                                    },
                            {
                                        'source_monitor': 9149969,
                                        'source_nw_x_pixel': -4601465763813753306,
                                        'source_nw_y_pixel': -6348669856003879474,
                                        'source_pixel_width': -6463036332103236616,
                                        'source_pixel_height': -5240658965162490589,
                                        'rotation': -2252039475016252821,
                                        'virtual_nw_x_pixel': 1674038891,
                                        'virtual_nw_y_pixel': 866583665,
                                        'virtual_width': -1460922813,
                                        'virtual_height': -1329082963,
                                    },
                            {
                                        'source_monitor': 3209909,
                                        'source_nw_x_pixel': -2733748678266761392,
                                        'source_nw_y_pixel': -3740646534253621097,
                                        'source_pixel_width': -15966466406673432,
                                        'source_pixel_height': -4398960429477028677,
                                        'rotation': -5991679579053884200,
                                        'virtual_nw_x_pixel': 335698808,
                                        'virtual_nw_y_pixel': 1586225353,
                                        'virtual_width': 334256014,
                                        'virtual_height': 53007000,
                                    },
                            {
                                        'source_monitor': 2165961,
                                        'source_nw_x_pixel': -8686577994354361363,
                                        'source_nw_y_pixel': -4789978066810086468,
                                        'source_pixel_width': -3316344457339709431,
                                        'source_pixel_height': -4585463677467335,
                                        'rotation': -826861485235428205,
                                        'virtual_nw_x_pixel': -1816190549,
                                        'virtual_nw_y_pixel': -225621200,
                                        'virtual_width': -1239230528,
                                        'virtual_height': -1702419659,
                                    },
                            {
                                        'source_monitor': 813945,
                                        'source_nw_x_pixel': -3701286203753554993,
                                        'source_nw_y_pixel': -2800594798087731794,
                                        'source_pixel_width': -2350035422476855824,
                                        'source_pixel_height': -7781360518296397495,
                                        'rotation': -3640156701427503192,
                                        'virtual_nw_x_pixel': 782507719,
                                        'virtual_nw_y_pixel': 954828155,
                                        'virtual_width': -607988512,
                                        'virtual_height': 801519233,
                                    },
                        ],
                },
                {
                    'description': 'ŐΝÙҒƠ\x83ıɯ˝ɻƘŖ\x84¤ͻѦƀ\x92ǽ˶҈ѲƬЖӸƊɱӖeӷ',
                    'monitors': [
                            {
                                        'identifier': 1095800,
                                        'width': 8913209047885681657,
                                        'height': -7851233113970317337,
                                    },
                            {
                                        'identifier': 859368,
                                        'width': 5562689423715564217,
                                        'height': 4427430287369632998,
                                    },
                            {
                                        'identifier': 6432799,
                                        'width': -9160670537228762363,
                                        'height': -5100444568489019702,
                                    },
                            {
                                        'identifier': 3419216,
                                        'width': -2266224790911484315,
                                        'height': -5732894811679070024,
                                    },
                            {
                                        'identifier': 5316606,
                                        'width': 2206642438845533859,
                                        'height': 6090354033258484161,
                                    },
                            {
                                        'identifier': 1946052,
                                        'width': 6528342441335873873,
                                        'height': 8927867461427608158,
                                    },
                            {
                                        'identifier': 7504613,
                                        'width': 1021238894035385753,
                                        'height': 3712981407339862855,
                                    },
                            {
                                        'identifier': 2759736,
                                        'width': 3046794495938164427,
                                        'height': 5546156724388827166,
                                    },
                            {
                                        'identifier': 4192677,
                                        'width': -786328386808272370,
                                        'height': 3266513636435688206,
                                    },
                            {
                                        'identifier': 5717723,
                                        'width': -5848824426398262185,
                                        'height': -361071653249629763,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5414606,
                                        'source_nw_x_pixel': -8521671414660749606,
                                        'source_nw_y_pixel': -8623749302448617232,
                                        'source_pixel_width': -7015514845069920763,
                                        'source_pixel_height': -1847578335026441367,
                                        'rotation': -2674196503422923736,
                                        'virtual_nw_x_pixel': -1649495951,
                                        'virtual_nw_y_pixel': -376445605,
                                        'virtual_width': 846764396,
                                        'virtual_height': -775344978,
                                    },
                            {
                                        'source_monitor': 3444421,
                                        'source_nw_x_pixel': -3386178371062517445,
                                        'source_nw_y_pixel': -4932809016004855540,
                                        'source_pixel_width': -4577466899746551730,
                                        'source_pixel_height': -7142319561591121415,
                                        'rotation': -4670133319149470993,
                                        'virtual_nw_x_pixel': -1868475123,
                                        'virtual_nw_y_pixel': 1984006059,
                                        'virtual_width': -231637105,
                                        'virtual_height': 1291756435,
                                    },
                            {
                                        'source_monitor': 4346824,
                                        'source_nw_x_pixel': -1287198808228230345,
                                        'source_nw_y_pixel': -6008178979901237940,
                                        'source_pixel_width': -4625874630405426292,
                                        'source_pixel_height': -1603600444304262661,
                                        'rotation': -4815615636317634464,
                                        'virtual_nw_x_pixel': 160993759,
                                        'virtual_nw_y_pixel': 532068059,
                                        'virtual_width': -1120506221,
                                        'virtual_height': 1859067355,
                                    },
                            {
                                        'source_monitor': 4831859,
                                        'source_nw_x_pixel': -2407695645809694474,
                                        'source_nw_y_pixel': -3941528176602140724,
                                        'source_pixel_width': -9065412772496525361,
                                        'source_pixel_height': -2981484555016706479,
                                        'rotation': -6083550347108961229,
                                        'virtual_nw_x_pixel': -156792987,
                                        'virtual_nw_y_pixel': 1187711843,
                                        'virtual_width': -301930051,
                                        'virtual_height': -1084629980,
                                    },
                            {
                                        'source_monitor': 5217546,
                                        'source_nw_x_pixel': -592587330705587027,
                                        'source_nw_y_pixel': -7944102658758913557,
                                        'source_pixel_width': -8377120271421944225,
                                        'source_pixel_height': -7223181894225754731,
                                        'rotation': -6594220214640010923,
                                        'virtual_nw_x_pixel': -1783913270,
                                        'virtual_nw_y_pixel': -1910398286,
                                        'virtual_width': -1328840202,
                                        'virtual_height': 196756080,
                                    },
                            {
                                        'source_monitor': 4103758,
                                        'source_nw_x_pixel': -7267930152258764910,
                                        'source_nw_y_pixel': -536414572173733634,
                                        'source_pixel_width': -7556846062726254909,
                                        'source_pixel_height': -796234009283493788,
                                        'rotation': -6517112084341709126,
                                        'virtual_nw_x_pixel': -931716256,
                                        'virtual_nw_y_pixel': 670481767,
                                        'virtual_width': -1306544481,
                                        'virtual_height': -1914584756,
                                    },
                            {
                                        'source_monitor': 6562535,
                                        'source_nw_x_pixel': -149008722231650256,
                                        'source_nw_y_pixel': -21589763777113627,
                                        'source_pixel_width': -6607084691804745884,
                                        'source_pixel_height': -1537153887240676592,
                                        'rotation': -6979147877244164630,
                                        'virtual_nw_x_pixel': -193967348,
                                        'virtual_nw_y_pixel': -1761319630,
                                        'virtual_width': 1314079135,
                                        'virtual_height': -280816678,
                                    },
                            {
                                        'source_monitor': 9468024,
                                        'source_nw_x_pixel': -8865067360781795310,
                                        'source_nw_y_pixel': -5175272077782928776,
                                        'source_pixel_width': -6688804094217781413,
                                        'source_pixel_height': -1101395383790550769,
                                        'rotation': -5086436053344307743,
                                        'virtual_nw_x_pixel': -352897049,
                                        'virtual_nw_y_pixel': -1072997233,
                                        'virtual_width': -651731718,
                                        'virtual_height': 1900884792,
                                    },
                            {
                                        'source_monitor': 8056724,
                                        'source_nw_x_pixel': -8287060728764032948,
                                        'source_nw_y_pixel': -5327087944080267882,
                                        'source_pixel_width': -8274415896865404125,
                                        'source_pixel_height': -1892128525708073476,
                                        'rotation': -8052168415549948970,
                                        'virtual_nw_x_pixel': -1225082801,
                                        'virtual_nw_y_pixel': 340668381,
                                        'virtual_width': 54573669,
                                        'virtual_height': -277045072,
                                    },
                            {
                                        'source_monitor': 1559029,
                                        'source_nw_x_pixel': -5730613010191011944,
                                        'source_nw_y_pixel': -7485985238806178609,
                                        'source_pixel_width': -3473467750412558557,
                                        'source_pixel_height': -6848875042751454945,
                                        'rotation': -2013561811253893199,
                                        'virtual_nw_x_pixel': 292540823,
                                        'virtual_nw_y_pixel': -723746367,
                                        'virtual_width': -1534440013,
                                        'virtual_height': -994440355,
                                    },
                        ],
                },
                {
                    'description': 'ʯ{Ћ¡ԘƝŊ\x7fԛʗɢɯƎҖʮĤ˕ˈƊЉ˓҂ʇ1а,ˑŸʀț',
                    'monitors': [
                            {
                                        'identifier': 4338549,
                                        'width': -2178532304616565246,
                                        'height': -7972672252802551405,
                                    },
                            {
                                        'identifier': -941311,
                                        'width': 3340491286612248065,
                                        'height': 4152994272186489117,
                                    },
                            {
                                        'identifier': 3104138,
                                        'width': 7898997927546030562,
                                        'height': -1147125098137056145,
                                    },
                            {
                                        'identifier': 5171167,
                                        'width': -2981801920298609753,
                                        'height': -2780782104788727526,
                                    },
                            {
                                        'identifier': -258908,
                                        'width': 1252538114716392090,
                                        'height': -5174301174392917864,
                                    },
                            {
                                        'identifier': -810310,
                                        'width': -8167730231223432632,
                                        'height': 2094167098893229930,
                                    },
                            {
                                        'identifier': 7333648,
                                        'width': 5563258415553700273,
                                        'height': -4638717209178258199,
                                    },
                            {
                                        'identifier': 72347,
                                        'width': 7721783724837165016,
                                        'height': -5280669297734134672,
                                    },
                            {
                                        'identifier': 6300938,
                                        'width': -7182283246380250557,
                                        'height': 8160809142753877133,
                                    },
                            {
                                        'identifier': -563640,
                                        'width': -8957490449015677808,
                                        'height': 5646329920052509744,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3133733,
                                        'source_nw_x_pixel': -2639426761796729572,
                                        'source_nw_y_pixel': -2857622082301254128,
                                        'source_pixel_width': -7710127094580587514,
                                        'source_pixel_height': -5799451400276260331,
                                        'rotation': -6899841733339823495,
                                        'virtual_nw_x_pixel': 223314597,
                                        'virtual_nw_y_pixel': 1367347675,
                                        'virtual_width': -1987852765,
                                        'virtual_height': 258756899,
                                    },
                            {
                                        'source_monitor': 9576234,
                                        'source_nw_x_pixel': -4294921780898534374,
                                        'source_nw_y_pixel': -335336344835980785,
                                        'source_pixel_width': -455321785349335832,
                                        'source_pixel_height': -7660462735238622914,
                                        'rotation': -618686774024682304,
                                        'virtual_nw_x_pixel': 618556696,
                                        'virtual_nw_y_pixel': -539055873,
                                        'virtual_width': 1086747799,
                                        'virtual_height': 1544240684,
                                    },
                            {
                                        'source_monitor': 4688648,
                                        'source_nw_x_pixel': -908944030983415125,
                                        'source_nw_y_pixel': -8616257044368328722,
                                        'source_pixel_width': -5282752983491473642,
                                        'source_pixel_height': -1060627621289816906,
                                        'rotation': -4254309053208903793,
                                        'virtual_nw_x_pixel': 1477540988,
                                        'virtual_nw_y_pixel': -1748871730,
                                        'virtual_width': 2784524,
                                        'virtual_height': 702392993,
                                    },
                            {
                                        'source_monitor': 5897294,
                                        'source_nw_x_pixel': -5178352450276004420,
                                        'source_nw_y_pixel': -9170913122138677014,
                                        'source_pixel_width': -1514505152291978826,
                                        'source_pixel_height': -7102413916390613024,
                                        'rotation': -1253464663767108802,
                                        'virtual_nw_x_pixel': 1284240587,
                                        'virtual_nw_y_pixel': -1342169019,
                                        'virtual_width': -251589702,
                                        'virtual_height': -1689277365,
                                    },
                            {
                                        'source_monitor': 1816572,
                                        'source_nw_x_pixel': -6008691249938388559,
                                        'source_nw_y_pixel': -118875745339112643,
                                        'source_pixel_width': -8312640299837434038,
                                        'source_pixel_height': -3543653691338171126,
                                        'rotation': -3963072017718294001,
                                        'virtual_nw_x_pixel': -854658045,
                                        'virtual_nw_y_pixel': 1173469590,
                                        'virtual_width': -1443343007,
                                        'virtual_height': 1930147273,
                                    },
                            {
                                        'source_monitor': 9603790,
                                        'source_nw_x_pixel': -3038641895351927019,
                                        'source_nw_y_pixel': -6676336023261269455,
                                        'source_pixel_width': -7575452739737468385,
                                        'source_pixel_height': -4512081334982735770,
                                        'rotation': -1637375908916483604,
                                        'virtual_nw_x_pixel': 684179653,
                                        'virtual_nw_y_pixel': 197419606,
                                        'virtual_width': -418954455,
                                        'virtual_height': 635005266,
                                    },
                            {
                                        'source_monitor': 7855356,
                                        'source_nw_x_pixel': -9055644568834616825,
                                        'source_nw_y_pixel': -7107545631923244864,
                                        'source_pixel_width': -8721022792509102573,
                                        'source_pixel_height': -8264423970618451073,
                                        'rotation': -8836973874598552647,
                                        'virtual_nw_x_pixel': -863699100,
                                        'virtual_nw_y_pixel': 1255355022,
                                        'virtual_width': -959194980,
                                        'virtual_height': 1571188999,
                                    },
                            {
                                        'source_monitor': 7391398,
                                        'source_nw_x_pixel': -2391390252548046890,
                                        'source_nw_y_pixel': -233779644372332289,
                                        'source_pixel_width': -3929888985710665030,
                                        'source_pixel_height': -3752026622813811942,
                                        'rotation': -2953834971022093719,
                                        'virtual_nw_x_pixel': 1270151025,
                                        'virtual_nw_y_pixel': -26216803,
                                        'virtual_width': 1869489188,
                                        'virtual_height': -491284350,
                                    },
                            {
                                        'source_monitor': 8112331,
                                        'source_nw_x_pixel': -7478982209594121057,
                                        'source_nw_y_pixel': -6037760797462767116,
                                        'source_pixel_width': -5317397168649295440,
                                        'source_pixel_height': -4988196280703043736,
                                        'rotation': -3499075445772173707,
                                        'virtual_nw_x_pixel': 1085446067,
                                        'virtual_nw_y_pixel': -297410238,
                                        'virtual_width': -956130013,
                                        'virtual_height': -1223010535,
                                    },
                            {
                                        'source_monitor': 7142575,
                                        'source_nw_x_pixel': -1623775677460259227,
                                        'source_nw_y_pixel': -2675030039687891138,
                                        'source_pixel_width': -430456228019511201,
                                        'source_pixel_height': -674004977354162207,
                                        'rotation': -8310044049284484531,
                                        'virtual_nw_x_pixel': 1790214361,
                                        'virtual_nw_y_pixel': -1458219844,
                                        'virtual_width': 1267431609,
                                        'virtual_height': -250618183,
                                    },
                        ],
                },
                {
                    'description': 'ŜʳʙĴȃϵεĐȁ\x88?PȅЗ˲ԒΐβƂһÑăMҘҾÛӈӼѡì',
                    'monitors': [
                            {
                                        'identifier': 1781377,
                                        'width': 8974404968479545746,
                                        'height': -6884726777303377544,
                                    },
                            {
                                        'identifier': -980898,
                                        'width': 33013207923041737,
                                        'height': -8899695670177005931,
                                    },
                            {
                                        'identifier': 3409540,
                                        'width': -8634674562850414029,
                                        'height': 5576698381844071627,
                                    },
                            {
                                        'identifier': 5810489,
                                        'width': 1432322351746670129,
                                        'height': -5855453915819873428,
                                    },
                            {
                                        'identifier': 9446592,
                                        'width': -3774136134220995447,
                                        'height': 1762859172599317032,
                                    },
                            {
                                        'identifier': 3868078,
                                        'width': 7281134411579473341,
                                        'height': -1524724059632954549,
                                    },
                            {
                                        'identifier': 1573335,
                                        'width': 3209245852208503724,
                                        'height': 8977632846106201390,
                                    },
                            {
                                        'identifier': 3104517,
                                        'width': -6548612640242751806,
                                        'height': 3522561541289188695,
                                    },
                            {
                                        'identifier': -648068,
                                        'width': -5916859097280825535,
                                        'height': 4940617906509680968,
                                    },
                            {
                                        'identifier': -571938,
                                        'width': -5730650236441482290,
                                        'height': 6320447185676149338,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8545531,
                                        'source_nw_x_pixel': -7750817822118226033,
                                        'source_nw_y_pixel': -8397057793146561884,
                                        'source_pixel_width': -3783709727636524997,
                                        'source_pixel_height': -1942840006480647630,
                                        'rotation': -7417600259275127186,
                                        'virtual_nw_x_pixel': 1393693909,
                                        'virtual_nw_y_pixel': 353795867,
                                        'virtual_width': -1107698689,
                                        'virtual_height': 1013354600,
                                    },
                            {
                                        'source_monitor': 3724606,
                                        'source_nw_x_pixel': -742569697404109051,
                                        'source_nw_y_pixel': -7361086623362492206,
                                        'source_pixel_width': -719002018269204,
                                        'source_pixel_height': -5128375922649659024,
                                        'rotation': -4260353400964268197,
                                        'virtual_nw_x_pixel': -765696319,
                                        'virtual_nw_y_pixel': -1754479529,
                                        'virtual_width': 1349590581,
                                        'virtual_height': 701826861,
                                    },
                            {
                                        'source_monitor': 2301592,
                                        'source_nw_x_pixel': -1833071404447257851,
                                        'source_nw_y_pixel': -6046279500514621109,
                                        'source_pixel_width': -6314770711470206565,
                                        'source_pixel_height': -3198454337028335806,
                                        'rotation': -8293084534396076031,
                                        'virtual_nw_x_pixel': 591226450,
                                        'virtual_nw_y_pixel': -861361740,
                                        'virtual_width': 21452414,
                                        'virtual_height': 874896586,
                                    },
                            {
                                        'source_monitor': 3160466,
                                        'source_nw_x_pixel': -4139643472346941781,
                                        'source_nw_y_pixel': -4790969311538702133,
                                        'source_pixel_width': -2264101261566118768,
                                        'source_pixel_height': -486017589408579969,
                                        'rotation': -6666661858104580611,
                                        'virtual_nw_x_pixel': 947841874,
                                        'virtual_nw_y_pixel': 1963618245,
                                        'virtual_width': -964847551,
                                        'virtual_height': -233587410,
                                    },
                            {
                                        'source_monitor': 6030038,
                                        'source_nw_x_pixel': -3449791680515573431,
                                        'source_nw_y_pixel': -8653222652777538170,
                                        'source_pixel_width': -1203844537081533232,
                                        'source_pixel_height': -6699745565103343854,
                                        'rotation': -89118887690686312,
                                        'virtual_nw_x_pixel': 792024787,
                                        'virtual_nw_y_pixel': -811357643,
                                        'virtual_width': 1441792937,
                                        'virtual_height': 1254015202,
                                    },
                            {
                                        'source_monitor': 9818601,
                                        'source_nw_x_pixel': -7946110163490857008,
                                        'source_nw_y_pixel': -4122111262936103920,
                                        'source_pixel_width': -1857216204834971311,
                                        'source_pixel_height': -8785650428606583853,
                                        'rotation': -4975575259784454428,
                                        'virtual_nw_x_pixel': -759385378,
                                        'virtual_nw_y_pixel': 928764218,
                                        'virtual_width': -294328048,
                                        'virtual_height': 921555522,
                                    },
                            {
                                        'source_monitor': 8185804,
                                        'source_nw_x_pixel': -5244421187847403279,
                                        'source_nw_y_pixel': -6475177334191518335,
                                        'source_pixel_width': -1028102615911010353,
                                        'source_pixel_height': -3679945997265612895,
                                        'rotation': -4232873016833536780,
                                        'virtual_nw_x_pixel': -956427751,
                                        'virtual_nw_y_pixel': -420723610,
                                        'virtual_width': -144350918,
                                        'virtual_height': -556022620,
                                    },
                            {
                                        'source_monitor': 5396636,
                                        'source_nw_x_pixel': -1221792555139139253,
                                        'source_nw_y_pixel': -8859129629812878248,
                                        'source_pixel_width': -7449331688271926683,
                                        'source_pixel_height': -4573846258834660083,
                                        'rotation': -1816453149845016464,
                                        'virtual_nw_x_pixel': -289724905,
                                        'virtual_nw_y_pixel': 1636791822,
                                        'virtual_width': -1159174171,
                                        'virtual_height': -1720926495,
                                    },
                            {
                                        'source_monitor': 8820101,
                                        'source_nw_x_pixel': -440932221351033842,
                                        'source_nw_y_pixel': -1189573495030990440,
                                        'source_pixel_width': -7359690843455060136,
                                        'source_pixel_height': -522705594392107518,
                                        'rotation': -3494335982739753949,
                                        'virtual_nw_x_pixel': 296650353,
                                        'virtual_nw_y_pixel': 637630016,
                                        'virtual_width': 1141421235,
                                        'virtual_height': -1668835220,
                                    },
                            {
                                        'source_monitor': 8134269,
                                        'source_nw_x_pixel': -9222354457417294576,
                                        'source_nw_y_pixel': -4385543213964918115,
                                        'source_pixel_width': -3435874474509055044,
                                        'source_pixel_height': -6942477617839659472,
                                        'rotation': -8386786422356152782,
                                        'virtual_nw_x_pixel': -367155874,
                                        'virtual_nw_y_pixel': 930114143,
                                        'virtual_width': 823513566,
                                        'virtual_height': -904324280,
                                    },
                        ],
                },
                {
                    'description': 'ѾůӔт˂ƥņ]ȥ˄Ƭ˱ϬRіɼҡϢЩĥ]Kˤ|ʧԢΙѢżГ',
                    'monitors': [
                            {
                                        'identifier': 7993127,
                                        'width': 2256773013744465275,
                                        'height': -394395465670802047,
                                    },
                            {
                                        'identifier': 6994512,
                                        'width': 7046994384321612005,
                                        'height': 5633082927776711919,
                                    },
                            {
                                        'identifier': 9910253,
                                        'width': 5012058093837798893,
                                        'height': 6890024670943568992,
                                    },
                            {
                                        'identifier': 1448274,
                                        'width': -7046998861140284609,
                                        'height': 3245819584061396935,
                                    },
                            {
                                        'identifier': 611331,
                                        'width': -7438699359981772777,
                                        'height': -9143440213909164544,
                                    },
                            {
                                        'identifier': 7371522,
                                        'width': 504909890379972448,
                                        'height': -8971825207339247151,
                                    },
                            {
                                        'identifier': 7437575,
                                        'width': 4053506400080402803,
                                        'height': 5713464820444730653,
                                    },
                            {
                                        'identifier': 5148623,
                                        'width': -690573522496313886,
                                        'height': -7920613545778510337,
                                    },
                            {
                                        'identifier': -761445,
                                        'width': -4712379640164903886,
                                        'height': 8362894487049105208,
                                    },
                            {
                                        'identifier': -170862,
                                        'width': 2613146077762790308,
                                        'height': -5432677752463690197,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7861577,
                                        'source_nw_x_pixel': -2635368533365770255,
                                        'source_nw_y_pixel': -7184735809999677598,
                                        'source_pixel_width': -6365118522897498536,
                                        'source_pixel_height': -5034711528512212880,
                                        'rotation': -3101568076234176948,
                                        'virtual_nw_x_pixel': -1392767180,
                                        'virtual_nw_y_pixel': -312642705,
                                        'virtual_width': -506201547,
                                        'virtual_height': -1190516049,
                                    },
                            {
                                        'source_monitor': 4926271,
                                        'source_nw_x_pixel': -8302066164951927981,
                                        'source_nw_y_pixel': -6172421676692985486,
                                        'source_pixel_width': -308247393073427862,
                                        'source_pixel_height': -5415612893663076976,
                                        'rotation': -3884648998780716553,
                                        'virtual_nw_x_pixel': -1466451027,
                                        'virtual_nw_y_pixel': -1338915331,
                                        'virtual_width': -1238248066,
                                        'virtual_height': 459544391,
                                    },
                            {
                                        'source_monitor': -893116,
                                        'source_nw_x_pixel': -2461407300623585791,
                                        'source_nw_y_pixel': -2751694505322696696,
                                        'source_pixel_width': -1197648502010761179,
                                        'source_pixel_height': -7610402134514868651,
                                        'rotation': -3769103517766969072,
                                        'virtual_nw_x_pixel': 792938330,
                                        'virtual_nw_y_pixel': 1424481456,
                                        'virtual_width': -414936343,
                                        'virtual_height': -1147382188,
                                    },
                            {
                                        'source_monitor': 8822047,
                                        'source_nw_x_pixel': -3376474448400042031,
                                        'source_nw_y_pixel': -3606390877381756187,
                                        'source_pixel_width': -3772250249887747623,
                                        'source_pixel_height': -4723263565551483803,
                                        'rotation': -4700828965602375650,
                                        'virtual_nw_x_pixel': 1211239671,
                                        'virtual_nw_y_pixel': 604804261,
                                        'virtual_width': -296649209,
                                        'virtual_height': 1753774683,
                                    },
                            {
                                        'source_monitor': 5463797,
                                        'source_nw_x_pixel': -8192332470153538196,
                                        'source_nw_y_pixel': -7031297914003556694,
                                        'source_pixel_width': -4494923775342081359,
                                        'source_pixel_height': -1520937961796176835,
                                        'rotation': -6156183220725809473,
                                        'virtual_nw_x_pixel': 167059070,
                                        'virtual_nw_y_pixel': -1547319574,
                                        'virtual_width': 1476126181,
                                        'virtual_height': -1486888029,
                                    },
                            {
                                        'source_monitor': -633478,
                                        'source_nw_x_pixel': -4149689582098251018,
                                        'source_nw_y_pixel': -3700432321378384804,
                                        'source_pixel_width': -7728618091958353827,
                                        'source_pixel_height': -2344835452252468497,
                                        'rotation': -2202450241744761992,
                                        'virtual_nw_x_pixel': 1281199944,
                                        'virtual_nw_y_pixel': 1298125258,
                                        'virtual_width': 665848977,
                                        'virtual_height': 1473603927,
                                    },
                            {
                                        'source_monitor': 5401179,
                                        'source_nw_x_pixel': -8451056850994979488,
                                        'source_nw_y_pixel': -8779910230180531187,
                                        'source_pixel_width': -5608975680599451924,
                                        'source_pixel_height': -8865447183179167535,
                                        'rotation': -4128699655928873899,
                                        'virtual_nw_x_pixel': 1256176690,
                                        'virtual_nw_y_pixel': -699365166,
                                        'virtual_width': -1228926559,
                                        'virtual_height': -1191099896,
                                    },
                            {
                                        'source_monitor': -494914,
                                        'source_nw_x_pixel': -2302796882050122791,
                                        'source_nw_y_pixel': -8393980712557669833,
                                        'source_pixel_width': -3314128521244025363,
                                        'source_pixel_height': -5781745986568096541,
                                        'rotation': -2129421885013425689,
                                        'virtual_nw_x_pixel': -1559275885,
                                        'virtual_nw_y_pixel': -1658912878,
                                        'virtual_width': 337263781,
                                        'virtual_height': -1713380170,
                                    },
                            {
                                        'source_monitor': 1220574,
                                        'source_nw_x_pixel': -328569004125722907,
                                        'source_nw_y_pixel': -1386113230532498957,
                                        'source_pixel_width': -2594956795071983131,
                                        'source_pixel_height': -8110068154117050709,
                                        'rotation': -5771502180281610893,
                                        'virtual_nw_x_pixel': -1728515307,
                                        'virtual_nw_y_pixel': 327955366,
                                        'virtual_width': 1545043805,
                                        'virtual_height': 487465414,
                                    },
                            {
                                        'source_monitor': 1582193,
                                        'source_nw_x_pixel': -343497460341673974,
                                        'source_nw_y_pixel': -2244511679230746562,
                                        'source_pixel_width': -4952013889965712652,
                                        'source_pixel_height': -5730872152833668381,
                                        'rotation': -4379886306446352156,
                                        'virtual_nw_x_pixel': 926583568,
                                        'virtual_nw_y_pixel': -1053342844,
                                        'virtual_width': -1125050304,
                                        'virtual_height': 356984907,
                                    },
                        ],
                },
                {
                    'description': '\x8dǎƛʂ˕ǇԄωтӘӰʞȌЯˈȣϵ\x82бJԏϥǨРϩԦħ˾ǃL',
                    'monitors': [
                            {
                                        'identifier': 1603865,
                                        'width': -6528722105664622971,
                                        'height': -4192718020085990775,
                                    },
                            {
                                        'identifier': 6354256,
                                        'width': -6719990910772304041,
                                        'height': 14331912039735848,
                                    },
                            {
                                        'identifier': 4608025,
                                        'width': -5938676414339572484,
                                        'height': -8147761583811798309,
                                    },
                            {
                                        'identifier': 6116698,
                                        'width': -4943538293597042250,
                                        'height': -3697127005827585842,
                                    },
                            {
                                        'identifier': 7455306,
                                        'width': -891480447938582369,
                                        'height': 174046074503552572,
                                    },
                            {
                                        'identifier': 8593785,
                                        'width': 1029878507337265183,
                                        'height': 7995141814524788510,
                                    },
                            {
                                        'identifier': 695187,
                                        'width': -7065584714796862205,
                                        'height': -5245635118235947202,
                                    },
                            {
                                        'identifier': 7805707,
                                        'width': -6237209586989408287,
                                        'height': -1383106859550268672,
                                    },
                            {
                                        'identifier': 8070042,
                                        'width': 5754834773091381434,
                                        'height': -6892687216322568497,
                                    },
                            {
                                        'identifier': 5030728,
                                        'width': 2249719613525287422,
                                        'height': 1177444713170447281,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2871966,
                                        'source_nw_x_pixel': -2674525239086931591,
                                        'source_nw_y_pixel': -4794974366479390893,
                                        'source_pixel_width': -1329988120345674320,
                                        'source_pixel_height': -1356001196379559007,
                                        'rotation': -3307301089394009448,
                                        'virtual_nw_x_pixel': -969657108,
                                        'virtual_nw_y_pixel': -865458553,
                                        'virtual_width': -104621238,
                                        'virtual_height': -128885595,
                                    },
                            {
                                        'source_monitor': 8634137,
                                        'source_nw_x_pixel': -1736589756034107511,
                                        'source_nw_y_pixel': -2196489376193339129,
                                        'source_pixel_width': -7600083690194051296,
                                        'source_pixel_height': -3142633661918218540,
                                        'rotation': -8953758029048379733,
                                        'virtual_nw_x_pixel': -858953633,
                                        'virtual_nw_y_pixel': -1860547545,
                                        'virtual_width': -553457519,
                                        'virtual_height': -1034876159,
                                    },
                            {
                                        'source_monitor': 5734438,
                                        'source_nw_x_pixel': -6696041216290936908,
                                        'source_nw_y_pixel': -3110684365251505505,
                                        'source_pixel_width': -3822287742634102461,
                                        'source_pixel_height': -8208810313653062056,
                                        'rotation': -5455237972115411472,
                                        'virtual_nw_x_pixel': 750865124,
                                        'virtual_nw_y_pixel': 1445171221,
                                        'virtual_width': -813346033,
                                        'virtual_height': -403461424,
                                    },
                            {
                                        'source_monitor': 8814751,
                                        'source_nw_x_pixel': -1867281157231979086,
                                        'source_nw_y_pixel': -6287019595443199237,
                                        'source_pixel_width': -2688819774890122701,
                                        'source_pixel_height': -1512119114126605839,
                                        'rotation': -1971736554022230721,
                                        'virtual_nw_x_pixel': 296189440,
                                        'virtual_nw_y_pixel': -1949972497,
                                        'virtual_width': 1611607999,
                                        'virtual_height': 1417196323,
                                    },
                            {
                                        'source_monitor': 4460256,
                                        'source_nw_x_pixel': -7367360077920907700,
                                        'source_nw_y_pixel': -2980790497703285934,
                                        'source_pixel_width': -7041871286950491655,
                                        'source_pixel_height': -1084941940027854018,
                                        'rotation': -7138474662881889771,
                                        'virtual_nw_x_pixel': -1141747409,
                                        'virtual_nw_y_pixel': 1244171611,
                                        'virtual_width': -1931932518,
                                        'virtual_height': -213194020,
                                    },
                            {
                                        'source_monitor': 486151,
                                        'source_nw_x_pixel': -8189801154643325039,
                                        'source_nw_y_pixel': -4263871545665767340,
                                        'source_pixel_width': -6251492142243932262,
                                        'source_pixel_height': -8450064689180980387,
                                        'rotation': -2070247459618752647,
                                        'virtual_nw_x_pixel': -190174490,
                                        'virtual_nw_y_pixel': -1276825462,
                                        'virtual_width': 858552689,
                                        'virtual_height': -1269690746,
                                    },
                            {
                                        'source_monitor': 1134572,
                                        'source_nw_x_pixel': -4490202579779529244,
                                        'source_nw_y_pixel': -5546196291332170630,
                                        'source_pixel_width': -2364186447859095887,
                                        'source_pixel_height': -3014281283147562193,
                                        'rotation': -897435287730556204,
                                        'virtual_nw_x_pixel': -73856254,
                                        'virtual_nw_y_pixel': 1002715541,
                                        'virtual_width': 1170600783,
                                        'virtual_height': -1582089349,
                                    },
                            {
                                        'source_monitor': 2193259,
                                        'source_nw_x_pixel': -546079584477466925,
                                        'source_nw_y_pixel': -6036509189404395648,
                                        'source_pixel_width': -7903207756613791408,
                                        'source_pixel_height': -1483350028497246342,
                                        'rotation': -6583683725432329659,
                                        'virtual_nw_x_pixel': -1770284390,
                                        'virtual_nw_y_pixel': 443035343,
                                        'virtual_width': -1228806499,
                                        'virtual_height': 1043110343,
                                    },
                            {
                                        'source_monitor': 6137906,
                                        'source_nw_x_pixel': -8750887804841961948,
                                        'source_nw_y_pixel': -4258428303331799775,
                                        'source_pixel_width': -8618499168665971969,
                                        'source_pixel_height': -8070632594195052831,
                                        'rotation': -1098203722900075606,
                                        'virtual_nw_x_pixel': 869711617,
                                        'virtual_nw_y_pixel': 1459963314,
                                        'virtual_width': 1232827287,
                                        'virtual_height': 288452316,
                                    },
                            {
                                        'source_monitor': 7383448,
                                        'source_nw_x_pixel': -4021207475686080260,
                                        'source_nw_y_pixel': -4631399701940225101,
                                        'source_pixel_width': -2314003823809302598,
                                        'source_pixel_height': -7970782294628430110,
                                        'rotation': -5644182231336022617,
                                        'virtual_nw_x_pixel': 1591220736,
                                        'virtual_nw_y_pixel': 1966373859,
                                        'virtual_width': -173254558,
                                        'virtual_height': 797999393,
                                    },
                        ],
                },
                {
                    'description': 'ȇϠĹǷŉš<өÚțqϡĀСϚģÄͲiǵƬċͲƝâ¦ғ\u03a2ĻȰ',
                    'monitors': [
                            {
                                        'identifier': 9692471,
                                        'width': 6779796712236129553,
                                        'height': 5450072432827058961,
                                    },
                            {
                                        'identifier': 4470935,
                                        'width': 4271955026911752152,
                                        'height': -7040784953225919011,
                                    },
                            {
                                        'identifier': 3044338,
                                        'width': -3398678550285624226,
                                        'height': -6384355278315065246,
                                    },
                            {
                                        'identifier': 1871620,
                                        'width': 1199707194908999784,
                                        'height': 5129763674594291092,
                                    },
                            {
                                        'identifier': 6426945,
                                        'width': -7640927880430563953,
                                        'height': 7743003202402685991,
                                    },
                            {
                                        'identifier': 3856068,
                                        'width': 9066470743220448690,
                                        'height': 52469736177706379,
                                    },
                            {
                                        'identifier': 133356,
                                        'width': -6034826434819749455,
                                        'height': -1963391380248035189,
                                    },
                            {
                                        'identifier': 8305235,
                                        'width': -1812609104236518993,
                                        'height': 8586628847895693625,
                                    },
                            {
                                        'identifier': 951039,
                                        'width': 1153353058148160729,
                                        'height': 4348606622510873566,
                                    },
                            {
                                        'identifier': 1207463,
                                        'width': -7491338779621083059,
                                        'height': -1699374553540491368,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8423630,
                                        'source_nw_x_pixel': -728904931612427160,
                                        'source_nw_y_pixel': -8729401933241369176,
                                        'source_pixel_width': -7046927425112749638,
                                        'source_pixel_height': -2958926203360790667,
                                        'rotation': -915296442980959976,
                                        'virtual_nw_x_pixel': 1363667307,
                                        'virtual_nw_y_pixel': 1784150174,
                                        'virtual_width': 1262290021,
                                        'virtual_height': -1873761145,
                                    },
                            {
                                        'source_monitor': -55943,
                                        'source_nw_x_pixel': -3957967813203951560,
                                        'source_nw_y_pixel': -6677532081914853820,
                                        'source_pixel_width': -8530272501398752023,
                                        'source_pixel_height': -5150663603989924099,
                                        'rotation': -1222591005674461912,
                                        'virtual_nw_x_pixel': -1625850754,
                                        'virtual_nw_y_pixel': 301798854,
                                        'virtual_width': 1058807181,
                                        'virtual_height': 1651954117,
                                    },
                            {
                                        'source_monitor': 7995376,
                                        'source_nw_x_pixel': -7876756915780022903,
                                        'source_nw_y_pixel': -4383331610123162564,
                                        'source_pixel_width': -8374960885345303809,
                                        'source_pixel_height': -8543171685565818387,
                                        'rotation': -7452077465784020131,
                                        'virtual_nw_x_pixel': 153758951,
                                        'virtual_nw_y_pixel': 1422756854,
                                        'virtual_width': 894741014,
                                        'virtual_height': 30675917,
                                    },
                            {
                                        'source_monitor': 6460536,
                                        'source_nw_x_pixel': -5803204744605165379,
                                        'source_nw_y_pixel': -6805029958656962047,
                                        'source_pixel_width': -342516969894973567,
                                        'source_pixel_height': -2732278600755736287,
                                        'rotation': -9012199198233602253,
                                        'virtual_nw_x_pixel': 1721664958,
                                        'virtual_nw_y_pixel': 757142213,
                                        'virtual_width': -1407630462,
                                        'virtual_height': 450581722,
                                    },
                            {
                                        'source_monitor': 9877613,
                                        'source_nw_x_pixel': -191280185461121518,
                                        'source_nw_y_pixel': -838375052537410765,
                                        'source_pixel_width': -7427897961759760179,
                                        'source_pixel_height': -5782198483471651238,
                                        'rotation': -5149358290443003172,
                                        'virtual_nw_x_pixel': 513894747,
                                        'virtual_nw_y_pixel': -233323469,
                                        'virtual_width': 235739367,
                                        'virtual_height': 896500056,
                                    },
                            {
                                        'source_monitor': 4357519,
                                        'source_nw_x_pixel': -9220020394314938919,
                                        'source_nw_y_pixel': -8816078622886184319,
                                        'source_pixel_width': -5031303742861598486,
                                        'source_pixel_height': -5367346927997692292,
                                        'rotation': -7271557908610954381,
                                        'virtual_nw_x_pixel': 802394372,
                                        'virtual_nw_y_pixel': 856876208,
                                        'virtual_width': 1447258250,
                                        'virtual_height': -587888423,
                                    },
                            {
                                        'source_monitor': 1489842,
                                        'source_nw_x_pixel': -1953554544537540115,
                                        'source_nw_y_pixel': -8042483349409469274,
                                        'source_pixel_width': -4357093842006462322,
                                        'source_pixel_height': -6033481318471498735,
                                        'rotation': -8298938492213272575,
                                        'virtual_nw_x_pixel': -1850619636,
                                        'virtual_nw_y_pixel': -1413183421,
                                        'virtual_width': 1808457567,
                                        'virtual_height': -1831345837,
                                    },
                            {
                                        'source_monitor': 8834154,
                                        'source_nw_x_pixel': -7446362023451149788,
                                        'source_nw_y_pixel': -8886741280222271519,
                                        'source_pixel_width': -4147648263777862158,
                                        'source_pixel_height': -8561868872716333607,
                                        'rotation': -7907186952610170945,
                                        'virtual_nw_x_pixel': -1847064298,
                                        'virtual_nw_y_pixel': -1454366102,
                                        'virtual_width': 720165422,
                                        'virtual_height': -474436864,
                                    },
                            {
                                        'source_monitor': 7285101,
                                        'source_nw_x_pixel': -5990571457436691592,
                                        'source_nw_y_pixel': -455047306827560208,
                                        'source_pixel_width': -766514772459227935,
                                        'source_pixel_height': -167543187978188100,
                                        'rotation': -7226338749028460930,
                                        'virtual_nw_x_pixel': 446830452,
                                        'virtual_nw_y_pixel': -868388942,
                                        'virtual_width': 37693890,
                                        'virtual_height': -784208310,
                                    },
                            {
                                        'source_monitor': 5892813,
                                        'source_nw_x_pixel': -1450052236201284133,
                                        'source_nw_y_pixel': -6839539683298789771,
                                        'source_pixel_width': -1696756055562400154,
                                        'source_pixel_height': -8207227260434574265,
                                        'rotation': -7862876706500383317,
                                        'virtual_nw_x_pixel': -758034795,
                                        'virtual_nw_y_pixel': 1718049923,
                                        'virtual_width': 481866923,
                                        'virtual_height': 780743587,
                                    },
                        ],
                },
                {
                    'description': 'ɱӅŶк"ι«ҕԕʵяϧӠāʎԦƘԮΐϮÔ˃˒ɖʌ\x8cѽИБˋ',
                    'monitors': [
                            {
                                        'identifier': 5825529,
                                        'width': 7805929164686601970,
                                        'height': 6610389612268507815,
                                    },
                            {
                                        'identifier': 4677741,
                                        'width': -6044787205708220267,
                                        'height': -8269159243174999921,
                                    },
                            {
                                        'identifier': 2619874,
                                        'width': -225843030606087729,
                                        'height': -5359747661169036529,
                                    },
                            {
                                        'identifier': 9730094,
                                        'width': 8909384241664577211,
                                        'height': -8303668388373357561,
                                    },
                            {
                                        'identifier': 2430732,
                                        'width': -5437831240580963397,
                                        'height': 8361641693106122160,
                                    },
                            {
                                        'identifier': 7460867,
                                        'width': 3169572707499755097,
                                        'height': 472452446792924653,
                                    },
                            {
                                        'identifier': 4987551,
                                        'width': 8095199539200762175,
                                        'height': -1822674486707503068,
                                    },
                            {
                                        'identifier': 2821900,
                                        'width': 5958729127389878315,
                                        'height': -2811781280746896384,
                                    },
                            {
                                        'identifier': 2941745,
                                        'width': 121342049880771828,
                                        'height': 4979972651609710865,
                                    },
                            {
                                        'identifier': 8283404,
                                        'width': 2203506493524470444,
                                        'height': 6791416894582164130,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7615806,
                                        'source_nw_x_pixel': -3595107230348689983,
                                        'source_nw_y_pixel': -627430789317695279,
                                        'source_pixel_width': -7528577993692918505,
                                        'source_pixel_height': -5333887594880517937,
                                        'rotation': -5667153341935220611,
                                        'virtual_nw_x_pixel': -994731701,
                                        'virtual_nw_y_pixel': -968074751,
                                        'virtual_width': -1598691485,
                                        'virtual_height': 826414950,
                                    },
                            {
                                        'source_monitor': 9097422,
                                        'source_nw_x_pixel': -7187548757963467037,
                                        'source_nw_y_pixel': -6942241167698246337,
                                        'source_pixel_width': -7192347747584069949,
                                        'source_pixel_height': -5570641830106378752,
                                        'rotation': -3770399297972284916,
                                        'virtual_nw_x_pixel': -848805889,
                                        'virtual_nw_y_pixel': 1994672099,
                                        'virtual_width': 208588732,
                                        'virtual_height': -1279245732,
                                    },
                            {
                                        'source_monitor': 5118957,
                                        'source_nw_x_pixel': -3060228465770994987,
                                        'source_nw_y_pixel': -8607949787900388617,
                                        'source_pixel_width': -444959468852146669,
                                        'source_pixel_height': -2143005149047087757,
                                        'rotation': -1385716377454683006,
                                        'virtual_nw_x_pixel': 301482288,
                                        'virtual_nw_y_pixel': 202845948,
                                        'virtual_width': 267222934,
                                        'virtual_height': 1667576152,
                                    },
                            {
                                        'source_monitor': 2398772,
                                        'source_nw_x_pixel': -7565398038306047460,
                                        'source_nw_y_pixel': -6338728854947981823,
                                        'source_pixel_width': -3801810420691168373,
                                        'source_pixel_height': -8602401028663267498,
                                        'rotation': -1922903679657116120,
                                        'virtual_nw_x_pixel': 237844614,
                                        'virtual_nw_y_pixel': -1110107109,
                                        'virtual_width': -1078589026,
                                        'virtual_height': -1279568922,
                                    },
                            {
                                        'source_monitor': 4793569,
                                        'source_nw_x_pixel': -4040848810284799767,
                                        'source_nw_y_pixel': -1502187824584789344,
                                        'source_pixel_width': -5123076933949965905,
                                        'source_pixel_height': -575567221589665496,
                                        'rotation': -1770695907570629347,
                                        'virtual_nw_x_pixel': 1166265661,
                                        'virtual_nw_y_pixel': 699663669,
                                        'virtual_width': 1230048074,
                                        'virtual_height': 1758184557,
                                    },
                            {
                                        'source_monitor': 7774312,
                                        'source_nw_x_pixel': -5510376459774118509,
                                        'source_nw_y_pixel': -5303532318003689922,
                                        'source_pixel_width': -8602836640136553052,
                                        'source_pixel_height': -6933525927252488886,
                                        'rotation': -3073825861139623540,
                                        'virtual_nw_x_pixel': 390998701,
                                        'virtual_nw_y_pixel': -288066172,
                                        'virtual_width': -1508688412,
                                        'virtual_height': -269513344,
                                    },
                            {
                                        'source_monitor': -547857,
                                        'source_nw_x_pixel': -1792630731417529878,
                                        'source_nw_y_pixel': -8724117509886966501,
                                        'source_pixel_width': -6948164646929021781,
                                        'source_pixel_height': -7745388869194445908,
                                        'rotation': -713516206779695653,
                                        'virtual_nw_x_pixel': 1911274450,
                                        'virtual_nw_y_pixel': -1881598729,
                                        'virtual_width': -520678015,
                                        'virtual_height': 1910311460,
                                    },
                            {
                                        'source_monitor': 2053093,
                                        'source_nw_x_pixel': -3667305970668649311,
                                        'source_nw_y_pixel': -8743000324657313341,
                                        'source_pixel_width': -1178892635465804139,
                                        'source_pixel_height': -227766845219600365,
                                        'rotation': -1657998534725112095,
                                        'virtual_nw_x_pixel': 1981508804,
                                        'virtual_nw_y_pixel': 1394631488,
                                        'virtual_width': -1030883775,
                                        'virtual_height': 1666470549,
                                    },
                            {
                                        'source_monitor': 5287741,
                                        'source_nw_x_pixel': -8641417849377425101,
                                        'source_nw_y_pixel': -7318318639667736881,
                                        'source_pixel_width': -4883485455263379838,
                                        'source_pixel_height': -3955393144378285156,
                                        'rotation': -4595250281858834203,
                                        'virtual_nw_x_pixel': -1507646755,
                                        'virtual_nw_y_pixel': -607644076,
                                        'virtual_width': -556759518,
                                        'virtual_height': 857476445,
                                    },
                            {
                                        'source_monitor': 7724167,
                                        'source_nw_x_pixel': -6631384988371580268,
                                        'source_nw_y_pixel': -3710500948672901375,
                                        'source_pixel_width': -4625912118038720499,
                                        'source_pixel_height': -7574708435877999298,
                                        'rotation': -5612467190253276532,
                                        'virtual_nw_x_pixel': 653021506,
                                        'virtual_nw_y_pixel': 1544347973,
                                        'virtual_width': 89265542,
                                        'virtual_height': 386808574,
                                    },
                        ],
                },
                {
                    'description': 'ѢɤČӴΞ\x9cˍщΉ\u0380ƧnԠZ³şӨÉġäŲƀșȅ¹ǟǆ÷\x9aњ',
                    'monitors': [
                            {
                                        'identifier': 2230038,
                                        'width': -3060554877013627911,
                                        'height': 5021041034469741988,
                                    },
                            {
                                        'identifier': 6148121,
                                        'width': 5982421535964167937,
                                        'height': -3669239546810656822,
                                    },
                            {
                                        'identifier': 7248528,
                                        'width': 4949777893582333074,
                                        'height': 4373982830599901043,
                                    },
                            {
                                        'identifier': 1405749,
                                        'width': 6382198099897883434,
                                        'height': 4663121134568497548,
                                    },
                            {
                                        'identifier': 3805173,
                                        'width': -5654525063147302256,
                                        'height': -468401153318521920,
                                    },
                            {
                                        'identifier': 1588627,
                                        'width': 549776712254504034,
                                        'height': -8867268989493674571,
                                    },
                            {
                                        'identifier': 6601921,
                                        'width': 4584687893681379165,
                                        'height': 5692843424302346735,
                                    },
                            {
                                        'identifier': 4717180,
                                        'width': -4531312155832737487,
                                        'height': -2783928938485077205,
                                    },
                            {
                                        'identifier': 1454214,
                                        'width': -9191958847982256923,
                                        'height': -3097776812453026693,
                                    },
                            {
                                        'identifier': 1591656,
                                        'width': -1829090463287371406,
                                        'height': 6717539696273170555,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6938831,
                                        'source_nw_x_pixel': -4518943776779646471,
                                        'source_nw_y_pixel': -7580860711852893270,
                                        'source_pixel_width': -4408180964899724054,
                                        'source_pixel_height': -4674708630239933320,
                                        'rotation': -4040064751852241053,
                                        'virtual_nw_x_pixel': -301387827,
                                        'virtual_nw_y_pixel': 347170500,
                                        'virtual_width': 1360778816,
                                        'virtual_height': -1581187879,
                                    },
                            {
                                        'source_monitor': 9786797,
                                        'source_nw_x_pixel': -712003810911480721,
                                        'source_nw_y_pixel': -5455306645500717600,
                                        'source_pixel_width': -8012342040062891284,
                                        'source_pixel_height': -6276015835130871976,
                                        'rotation': -151454808084126158,
                                        'virtual_nw_x_pixel': -745359382,
                                        'virtual_nw_y_pixel': -174193239,
                                        'virtual_width': -505279277,
                                        'virtual_height': -1888921572,
                                    },
                            {
                                        'source_monitor': 7666753,
                                        'source_nw_x_pixel': -8076425758143059100,
                                        'source_nw_y_pixel': -8057933127975516509,
                                        'source_pixel_width': -5487966717301174099,
                                        'source_pixel_height': -1908725029691520576,
                                        'rotation': -6324079815259820011,
                                        'virtual_nw_x_pixel': 1314465283,
                                        'virtual_nw_y_pixel': -1991200442,
                                        'virtual_width': -1039938329,
                                        'virtual_height': -1702113116,
                                    },
                            {
                                        'source_monitor': 9643683,
                                        'source_nw_x_pixel': -3981862436184074293,
                                        'source_nw_y_pixel': -5861009626280145788,
                                        'source_pixel_width': -2889374610782507697,
                                        'source_pixel_height': -2267155708808358083,
                                        'rotation': -9109560023746389048,
                                        'virtual_nw_x_pixel': -1424255211,
                                        'virtual_nw_y_pixel': -1727636481,
                                        'virtual_width': -760735565,
                                        'virtual_height': -39974295,
                                    },
                            {
                                        'source_monitor': 4680068,
                                        'source_nw_x_pixel': -8415887587557689215,
                                        'source_nw_y_pixel': -221783995921862803,
                                        'source_pixel_width': -976986049977789625,
                                        'source_pixel_height': -8972890422706086234,
                                        'rotation': -3181963989732619215,
                                        'virtual_nw_x_pixel': 1336099548,
                                        'virtual_nw_y_pixel': 1855804528,
                                        'virtual_width': -511025514,
                                        'virtual_height': 225656753,
                                    },
                            {
                                        'source_monitor': 8208861,
                                        'source_nw_x_pixel': -5040617566497202935,
                                        'source_nw_y_pixel': -7467435161303096846,
                                        'source_pixel_width': -5271513765408852355,
                                        'source_pixel_height': -2292936264255472916,
                                        'rotation': -7240644625154736884,
                                        'virtual_nw_x_pixel': -1347794303,
                                        'virtual_nw_y_pixel': 333898713,
                                        'virtual_width': -754891146,
                                        'virtual_height': -1419756425,
                                    },
                            {
                                        'source_monitor': 3884443,
                                        'source_nw_x_pixel': -5329675696284257284,
                                        'source_nw_y_pixel': -358422645270644635,
                                        'source_pixel_width': -6257547637531133969,
                                        'source_pixel_height': -245448482768608621,
                                        'rotation': -1803586879900440752,
                                        'virtual_nw_x_pixel': 1332364251,
                                        'virtual_nw_y_pixel': -1230454146,
                                        'virtual_width': 697756224,
                                        'virtual_height': -119198612,
                                    },
                            {
                                        'source_monitor': 9040582,
                                        'source_nw_x_pixel': -5430423223828258836,
                                        'source_nw_y_pixel': -7597201890307636946,
                                        'source_pixel_width': -1188014958680149391,
                                        'source_pixel_height': -2865956395600298414,
                                        'rotation': -3017183280629751902,
                                        'virtual_nw_x_pixel': -758086624,
                                        'virtual_nw_y_pixel': -51117863,
                                        'virtual_width': 403554754,
                                        'virtual_height': 1636607929,
                                    },
                            {
                                        'source_monitor': 513175,
                                        'source_nw_x_pixel': -7967159839795045260,
                                        'source_nw_y_pixel': -979965203452736559,
                                        'source_pixel_width': -1390152080328240500,
                                        'source_pixel_height': -9137424866750324861,
                                        'rotation': -3560639261339411188,
                                        'virtual_nw_x_pixel': 1226449457,
                                        'virtual_nw_y_pixel': 1797763601,
                                        'virtual_width': -265377364,
                                        'virtual_height': -730673079,
                                    },
                            {
                                        'source_monitor': 1292205,
                                        'source_nw_x_pixel': -1711422384716785999,
                                        'source_nw_y_pixel': -5815987249861770561,
                                        'source_pixel_width': -8593083357880425710,
                                        'source_pixel_height': -1348481828696677735,
                                        'rotation': -7710368843703808807,
                                        'virtual_nw_x_pixel': 1646636677,
                                        'virtual_nw_y_pixel': -290890113,
                                        'virtual_width': 514782522,
                                        'virtual_height': 38467366,
                                    },
                        ],
                },
                {
                    'description': 'eСѕωԤеȗұҾƊΕхЄɲƚ0icҫVʣ\x90gӠӻʭʨĞʮȵ',
                    'monitors': [
                            {
                                        'identifier': 6357097,
                                        'width': 6594498223508538545,
                                        'height': 3669819010058885549,
                                    },
                            {
                                        'identifier': 2508729,
                                        'width': 6395835914467866302,
                                        'height': -2400618760216258073,
                                    },
                            {
                                        'identifier': 6412401,
                                        'width': -1439823628426763367,
                                        'height': 850619482294790480,
                                    },
                            {
                                        'identifier': 419375,
                                        'width': 6132308751783423274,
                                        'height': -5008363788773199418,
                                    },
                            {
                                        'identifier': 2684000,
                                        'width': 7127970937174816413,
                                        'height': -7254066288721038025,
                                    },
                            {
                                        'identifier': 6815320,
                                        'width': 1696029409510083020,
                                        'height': 1422391150263738831,
                                    },
                            {
                                        'identifier': 2720305,
                                        'width': 420228534344132448,
                                        'height': 2137392910506133957,
                                    },
                            {
                                        'identifier': 2596612,
                                        'width': -3496763223062905089,
                                        'height': 1957331267313366728,
                                    },
                            {
                                        'identifier': 548290,
                                        'width': -7307713104400509535,
                                        'height': -4822520212689106254,
                                    },
                            {
                                        'identifier': 9894878,
                                        'width': 6967617136200642691,
                                        'height': -8659533351346262992,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5112037,
                                        'source_nw_x_pixel': -8361760065190091400,
                                        'source_nw_y_pixel': -6262878712262298388,
                                        'source_pixel_width': -9019343276699298879,
                                        'source_pixel_height': -3533648968620588920,
                                        'rotation': -8415273725395724480,
                                        'virtual_nw_x_pixel': -757867052,
                                        'virtual_nw_y_pixel': 501684873,
                                        'virtual_width': 619071605,
                                        'virtual_height': 397701841,
                                    },
                            {
                                        'source_monitor': 3736233,
                                        'source_nw_x_pixel': -4594676527719072546,
                                        'source_nw_y_pixel': -1691259926733989087,
                                        'source_pixel_width': -6389989895412913831,
                                        'source_pixel_height': -4358489330813597321,
                                        'rotation': -8794743885543706702,
                                        'virtual_nw_x_pixel': 98740733,
                                        'virtual_nw_y_pixel': 1197973291,
                                        'virtual_width': -865698641,
                                        'virtual_height': -1837873947,
                                    },
                            {
                                        'source_monitor': 3959549,
                                        'source_nw_x_pixel': -7636189686027460253,
                                        'source_nw_y_pixel': -4523323188356407096,
                                        'source_pixel_width': -2249541248160306665,
                                        'source_pixel_height': -7756122131964088746,
                                        'rotation': -672622679374225701,
                                        'virtual_nw_x_pixel': -292644748,
                                        'virtual_nw_y_pixel': 1161453860,
                                        'virtual_width': -484410313,
                                        'virtual_height': -475729164,
                                    },
                            {
                                        'source_monitor': 8179142,
                                        'source_nw_x_pixel': -7304443240452869233,
                                        'source_nw_y_pixel': -8914695701193936854,
                                        'source_pixel_width': -199399298357568666,
                                        'source_pixel_height': -6361613724090148212,
                                        'rotation': -7370297960004829468,
                                        'virtual_nw_x_pixel': -900743553,
                                        'virtual_nw_y_pixel': 1064560844,
                                        'virtual_width': -1762133181,
                                        'virtual_height': -1586795227,
                                    },
                            {
                                        'source_monitor': 3207796,
                                        'source_nw_x_pixel': -7038001592502524157,
                                        'source_nw_y_pixel': -8356260813406762166,
                                        'source_pixel_width': -3439898647499008546,
                                        'source_pixel_height': -2408960685417622685,
                                        'rotation': -9045369687527633737,
                                        'virtual_nw_x_pixel': 780632529,
                                        'virtual_nw_y_pixel': 126204259,
                                        'virtual_width': 324066192,
                                        'virtual_height': 1604029134,
                                    },
                            {
                                        'source_monitor': 8440539,
                                        'source_nw_x_pixel': -2248317141131263021,
                                        'source_nw_y_pixel': -479566858695569728,
                                        'source_pixel_width': -7942769507722264506,
                                        'source_pixel_height': -7228210642026720614,
                                        'rotation': -7522612929143675285,
                                        'virtual_nw_x_pixel': 1595984724,
                                        'virtual_nw_y_pixel': 391886388,
                                        'virtual_width': -960124539,
                                        'virtual_height': -822018624,
                                    },
                            {
                                        'source_monitor': 4571036,
                                        'source_nw_x_pixel': -9123857945860788208,
                                        'source_nw_y_pixel': -14996239026896003,
                                        'source_pixel_width': -6978873263763199505,
                                        'source_pixel_height': -6192980081865044749,
                                        'rotation': -1683765637840120449,
                                        'virtual_nw_x_pixel': -1558126529,
                                        'virtual_nw_y_pixel': 1619985684,
                                        'virtual_width': -1542285566,
                                        'virtual_height': 1815610920,
                                    },
                            {
                                        'source_monitor': -105664,
                                        'source_nw_x_pixel': -4965796164616701059,
                                        'source_nw_y_pixel': -8715989080036108974,
                                        'source_pixel_width': -4873242765422885745,
                                        'source_pixel_height': -4250729329232462228,
                                        'rotation': -1196296162487722128,
                                        'virtual_nw_x_pixel': -606221076,
                                        'virtual_nw_y_pixel': -934507431,
                                        'virtual_width': -840867404,
                                        'virtual_height': -781739398,
                                    },
                            {
                                        'source_monitor': 5517912,
                                        'source_nw_x_pixel': -5343623513606050582,
                                        'source_nw_y_pixel': -3241614736345523172,
                                        'source_pixel_width': -5753199805432934402,
                                        'source_pixel_height': -1523187040483156545,
                                        'rotation': -4160036448768205820,
                                        'virtual_nw_x_pixel': 544123860,
                                        'virtual_nw_y_pixel': -1814553539,
                                        'virtual_width': -1518271215,
                                        'virtual_height': -1529587456,
                                    },
                            {
                                        'source_monitor': 4201561,
                                        'source_nw_x_pixel': -1803374068590256442,
                                        'source_nw_y_pixel': -6987451730286224584,
                                        'source_pixel_width': -2202203328019995272,
                                        'source_pixel_height': -4869209729738591727,
                                        'rotation': -258086637716760021,
                                        'virtual_nw_x_pixel': -1916199937,
                                        'virtual_nw_y_pixel': -1419625068,
                                        'virtual_width': -452048702,
                                        'virtual_height': -932960175,
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
                                        'identifier': 9863458,
                                        'width': 6618442849375886196,
                                        'height': -3913831957722021461,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -710095302323452,
                                        'source_nw_y_pixel': -6393568013492270993,
                                        'source_pixel_width': -169963024714157060,
                                        'source_pixel_height': -3594992538338661531,
                                        'rotation': -235237341481378079,
                                        'virtual_nw_x_pixel': 1629170034,
                                        'virtual_nw_y_pixel': 966511502,
                                        'virtual_width': 532703762,
                                        'virtual_height': 392785513,
                                    },
                        ],
                },
            ],

        },
    ),
]
