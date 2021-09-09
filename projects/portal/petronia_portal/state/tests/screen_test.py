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
            'nw_x_pixel': -1650808330,
            'nw_y_pixel': 1063926077,
            'width': -3181608515819271,
            'height': -5067910599181683197,
            'ratio_x': -6336615985004935590,
            'ratio_y': 1361227854427999340,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 887184444,

            'nw_y_pixel': -1953141202,

            'width': -7518756884469136914,

            'height': -4907640601773151050,

            'ratio_x': -8480978340230450076,

            'ratio_y': 7630271462864879136,

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
                    'nw_x_pixel': -236052435,
                    'nw_y_pixel': 1713047922,
                    'width': -1799843809714943819,
                    'height': -7834483060477905837,
                    'ratio_x': -5812893238286405902,
                    'ratio_y': 1041769974681843432,
                },
                {
                    'nw_x_pixel': 1979449173,
                    'nw_y_pixel': -147769142,
                    'width': -7937277276679575363,
                    'height': -2847133363424530704,
                    'ratio_x': -3552675249092642869,
                    'ratio_y': 1699791961267729510,
                },
                {
                    'nw_x_pixel': -305545752,
                    'nw_y_pixel': 558791535,
                    'width': -7296032332958671950,
                    'height': -4656862404123940895,
                    'ratio_x': 429088109837598789,
                    'ratio_y': 4319582631652320294,
                },
                {
                    'nw_x_pixel': 1676392641,
                    'nw_y_pixel': 1892221361,
                    'width': -7154454108316803569,
                    'height': -7478842801870437868,
                    'ratio_x': 705059072592437763,
                    'ratio_y': -2928834959061654608,
                },
                {
                    'nw_x_pixel': 235693355,
                    'nw_y_pixel': -1802613589,
                    'width': -293243421331178582,
                    'height': -4683983934978033701,
                    'ratio_x': 1766481331872436552,
                    'ratio_y': -1899643264965373592,
                },
                {
                    'nw_x_pixel': -1026177558,
                    'nw_y_pixel': -628278871,
                    'width': -5210397287684737723,
                    'height': -746439018515541984,
                    'ratio_x': 9127896122753781441,
                    'ratio_y': -707626971608296318,
                },
                {
                    'nw_x_pixel': -659448973,
                    'nw_y_pixel': -240543386,
                    'width': -205043725937202366,
                    'height': -1112863564088586990,
                    'ratio_x': -1345501746282701695,
                    'ratio_y': -2209162172649560356,
                },
                {
                    'nw_x_pixel': -1309911689,
                    'nw_y_pixel': 1269363042,
                    'width': -898139773776149197,
                    'height': -2987188140766595455,
                    'ratio_x': 3642063616195980891,
                    'ratio_y': -5861517493524911772,
                },
                {
                    'nw_x_pixel': 324849184,
                    'nw_y_pixel': -1574598604,
                    'width': -1091157617375956055,
                    'height': -7577459284093214982,
                    'ratio_x': -8570899958612088096,
                    'ratio_y': -6034366343938295443,
                },
                {
                    'nw_x_pixel': -993611151,
                    'nw_y_pixel': 42887010,
                    'width': -6628399384688056779,
                    'height': -6269474461304542420,
                    'ratio_x': 6783004526795404776,
                    'ratio_y': -3153134773580049568,
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
            'identifier': 9884187,
            'width': -4842697700880989297,
            'height': -3562471113512362622,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 4705563,

            'width': -6672136543609797378,

            'height': -3099359884202653972,

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
            'source_monitor': 2833531,
            'source_nw_x_pixel': -70594939996471372,
            'source_nw_y_pixel': -6495104633129567287,
            'source_pixel_width': -6908518712740283654,
            'source_pixel_height': -9219980103520006573,
            'rotation': -7350491527629368821,
            'virtual_nw_x_pixel': 1929228123,
            'virtual_nw_y_pixel': -601068588,
            'virtual_width': 1774834472,
            'virtual_height': 1727746153,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -2898136519943113215,

            'source_nw_y_pixel': -5540982670187662441,

            'source_pixel_width': -503222906921237213,

            'source_pixel_height': -2317336844670242422,

            'rotation': -3618667366049336842,

            'virtual_nw_x_pixel': -920337187,

            'virtual_nw_y_pixel': 1802670509,

            'virtual_width': -440001744,

            'virtual_height': -1827604843,

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
            'description': 'ΒѺҒĳʑȴɊƅһкЊ˝˷űΚ)ӃӇϓȽȎҧŤ¡ĿəƉҦȁҢ',
            'monitors': [
                {
                    'identifier': 2843449,
                    'width': -4815799094797215355,
                    'height': 6173152835257913180,
                },
                {
                    'identifier': -927242,
                    'width': 6929166015026325001,
                    'height': -5261275456421398114,
                },
                {
                    'identifier': 3878588,
                    'width': 4519686244996676814,
                    'height': 2801409678952310855,
                },
                {
                    'identifier': 4583918,
                    'width': 1458071028700498587,
                    'height': 183599082098184021,
                },
                {
                    'identifier': 7974017,
                    'width': 1034376766363213368,
                    'height': -7314366764048877625,
                },
                {
                    'identifier': 8840374,
                    'width': -634020568914279925,
                    'height': 6584980664806177143,
                },
                {
                    'identifier': 1252558,
                    'width': 3629721806980511142,
                    'height': -2387921707784984606,
                },
                {
                    'identifier': 1582439,
                    'width': -1750226249133616284,
                    'height': 2641793727186851509,
                },
                {
                    'identifier': -781652,
                    'width': 7896864244451502129,
                    'height': -7880542897689910961,
                },
                {
                    'identifier': 1070115,
                    'width': -1029317836709783744,
                    'height': 2869855786661798450,
                },
            ],
            'screen': [
                {
                    'source_monitor': 2825669,
                    'source_nw_x_pixel': -8260048746553620345,
                    'source_nw_y_pixel': -7178555122156184615,
                    'source_pixel_width': -774204027000191050,
                    'source_pixel_height': -5112338635952411756,
                    'rotation': -4441015323053693464,
                    'virtual_nw_x_pixel': -703463375,
                    'virtual_nw_y_pixel': 698388338,
                    'virtual_width': 1337789543,
                    'virtual_height': 1983100396,
                },
                {
                    'source_monitor': 6255016,
                    'source_nw_x_pixel': -379108030825767829,
                    'source_nw_y_pixel': -7145311940505814041,
                    'source_pixel_width': -3354945995265033383,
                    'source_pixel_height': -3407650912496903553,
                    'rotation': -5072883202757612365,
                    'virtual_nw_x_pixel': -1316817550,
                    'virtual_nw_y_pixel': -713874040,
                    'virtual_width': 390825869,
                    'virtual_height': -1832898315,
                },
                {
                    'source_monitor': 7173904,
                    'source_nw_x_pixel': -8085476579087795495,
                    'source_nw_y_pixel': -3540577252401699845,
                    'source_pixel_width': -5002320541713149731,
                    'source_pixel_height': -944854455206759658,
                    'rotation': -29782836843353331,
                    'virtual_nw_x_pixel': -916580119,
                    'virtual_nw_y_pixel': -1776013138,
                    'virtual_width': 487996567,
                    'virtual_height': -1165484840,
                },
                {
                    'source_monitor': 1141094,
                    'source_nw_x_pixel': -4173409772571735424,
                    'source_nw_y_pixel': -1616356810568511014,
                    'source_pixel_width': -1477052889940204659,
                    'source_pixel_height': -5973187033135645027,
                    'rotation': -3296938730961218192,
                    'virtual_nw_x_pixel': 1942276536,
                    'virtual_nw_y_pixel': 47575751,
                    'virtual_width': -1394081632,
                    'virtual_height': 1091315410,
                },
                {
                    'source_monitor': 1577511,
                    'source_nw_x_pixel': -300449776736575866,
                    'source_nw_y_pixel': -5860684261436214496,
                    'source_pixel_width': -3589339680830093217,
                    'source_pixel_height': -4682326458526492814,
                    'rotation': -1095050763407285836,
                    'virtual_nw_x_pixel': 442270946,
                    'virtual_nw_y_pixel': 209546402,
                    'virtual_width': -248952834,
                    'virtual_height': 63168043,
                },
                {
                    'source_monitor': 3694719,
                    'source_nw_x_pixel': -3652405244851675708,
                    'source_nw_y_pixel': -1212214448940120086,
                    'source_pixel_width': -2275172704768751469,
                    'source_pixel_height': -2723441798570936890,
                    'rotation': -5603599682989466392,
                    'virtual_nw_x_pixel': 279954819,
                    'virtual_nw_y_pixel': -1389282435,
                    'virtual_width': -469425508,
                    'virtual_height': -1015343569,
                },
                {
                    'source_monitor': 6666860,
                    'source_nw_x_pixel': -4192103252069835175,
                    'source_nw_y_pixel': -1368208121361370367,
                    'source_pixel_width': -7115810747657796162,
                    'source_pixel_height': -6625415960560238635,
                    'rotation': -1838258648987335953,
                    'virtual_nw_x_pixel': -482245826,
                    'virtual_nw_y_pixel': -575372246,
                    'virtual_width': -1004680092,
                    'virtual_height': -1850026848,
                },
                {
                    'source_monitor': 2304686,
                    'source_nw_x_pixel': -5389799817169384674,
                    'source_nw_y_pixel': -8960819037765897190,
                    'source_pixel_width': -6138573831500946480,
                    'source_pixel_height': -7247522550448309156,
                    'rotation': -8998130327022310373,
                    'virtual_nw_x_pixel': -33269110,
                    'virtual_nw_y_pixel': 1060714016,
                    'virtual_width': -1280604159,
                    'virtual_height': 483177938,
                },
                {
                    'source_monitor': -502275,
                    'source_nw_x_pixel': -2461858980441842451,
                    'source_nw_y_pixel': -4914258939210427954,
                    'source_pixel_width': -2824360640225582687,
                    'source_pixel_height': -1078575685982509504,
                    'rotation': -4124611301886416998,
                    'virtual_nw_x_pixel': -373299129,
                    'virtual_nw_y_pixel': 1448241679,
                    'virtual_width': -853842523,
                    'virtual_height': 671080814,
                },
                {
                    'source_monitor': 3048040,
                    'source_nw_x_pixel': -8925110770465497392,
                    'source_nw_y_pixel': -2843568945945182396,
                    'source_pixel_width': -1470717906893527479,
                    'source_pixel_height': -4944451259201146224,
                    'rotation': -1104721692984594400,
                    'virtual_nw_x_pixel': -429968394,
                    'virtual_nw_y_pixel': -877682116,
                    'virtual_width': -934540204,
                    'virtual_height': -1566408011,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 3467118,
                    'width': 1113674621841995114,
                    'height': 3159820400269975578,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -2167649192949016814,
                    'source_nw_y_pixel': -7684385566400837779,
                    'source_pixel_width': -1813907025166171240,
                    'source_pixel_height': -7738140300732330475,
                    'rotation': -1505777756758900087,
                    'virtual_nw_x_pixel': -1442060280,
                    'virtual_nw_y_pixel': 1293823754,
                    'virtual_width': -361760024,
                    'virtual_height': -1352996150,
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
                    'description': 'ϝǔ˭ǎ\u038bÑϵωԭҡº%CƘҾГ8ΏƃϕȺϙ\u0380źġôшŻԂś',
                    'monitors': [
                            {
                                        'identifier': 3180688,
                                        'width': -2999846184431737396,
                                        'height': 6407216531474911745,
                                    },
                            {
                                        'identifier': 9516818,
                                        'width': -1556341539306943766,
                                        'height': 6396216560027101246,
                                    },
                            {
                                        'identifier': 2126221,
                                        'width': -3483503512186610378,
                                        'height': 1605824217947829843,
                                    },
                            {
                                        'identifier': 9813076,
                                        'width': 23288238121102409,
                                        'height': 2679968814947622233,
                                    },
                            {
                                        'identifier': 9752203,
                                        'width': -7232662694291629712,
                                        'height': 1844010921957000171,
                                    },
                            {
                                        'identifier': -18596,
                                        'width': -2861552976756362178,
                                        'height': 6315889990806851520,
                                    },
                            {
                                        'identifier': 6172191,
                                        'width': -2124257222342045387,
                                        'height': 6748773524058371829,
                                    },
                            {
                                        'identifier': 3205992,
                                        'width': 4635111633332502507,
                                        'height': -2566903173279078932,
                                    },
                            {
                                        'identifier': 4422501,
                                        'width': -8913329299690215959,
                                        'height': -1729752184484234183,
                                    },
                            {
                                        'identifier': 5344544,
                                        'width': -4029698300129149447,
                                        'height': -8745674527191778193,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 113877,
                                        'source_nw_x_pixel': -842934748626688509,
                                        'source_nw_y_pixel': -8403910501479202334,
                                        'source_pixel_width': -8593178385123356381,
                                        'source_pixel_height': -1205719582960242158,
                                        'rotation': -6338626881863143723,
                                        'virtual_nw_x_pixel': -1372679917,
                                        'virtual_nw_y_pixel': 838583395,
                                        'virtual_width': -1653313134,
                                        'virtual_height': -610544100,
                                    },
                            {
                                        'source_monitor': 5227410,
                                        'source_nw_x_pixel': -4548254931893622259,
                                        'source_nw_y_pixel': -5189375972619356760,
                                        'source_pixel_width': -829638185471262985,
                                        'source_pixel_height': -9162381357510050575,
                                        'rotation': -1557733332213416818,
                                        'virtual_nw_x_pixel': 1940683432,
                                        'virtual_nw_y_pixel': -8931767,
                                        'virtual_width': 1615458778,
                                        'virtual_height': 1285690890,
                                    },
                            {
                                        'source_monitor': 27243,
                                        'source_nw_x_pixel': -2553957438803180319,
                                        'source_nw_y_pixel': -4108058687937187614,
                                        'source_pixel_width': -5208115934008627087,
                                        'source_pixel_height': -4487933288247517777,
                                        'rotation': -1752277770313732546,
                                        'virtual_nw_x_pixel': 209714611,
                                        'virtual_nw_y_pixel': -217185826,
                                        'virtual_width': 1498142184,
                                        'virtual_height': -671966349,
                                    },
                            {
                                        'source_monitor': 3789311,
                                        'source_nw_x_pixel': -7454091677209748728,
                                        'source_nw_y_pixel': -5356622985749947183,
                                        'source_pixel_width': -3090255173785218843,
                                        'source_pixel_height': -228845056975346642,
                                        'rotation': -2537689952471714977,
                                        'virtual_nw_x_pixel': 807769838,
                                        'virtual_nw_y_pixel': -316218734,
                                        'virtual_width': -1962881384,
                                        'virtual_height': 1637991730,
                                    },
                            {
                                        'source_monitor': 1734418,
                                        'source_nw_x_pixel': -6042869204117991162,
                                        'source_nw_y_pixel': -759252368691120564,
                                        'source_pixel_width': -600208323883249073,
                                        'source_pixel_height': -3265959060745501353,
                                        'rotation': -45051421384170141,
                                        'virtual_nw_x_pixel': 796533646,
                                        'virtual_nw_y_pixel': 636668898,
                                        'virtual_width': 475672454,
                                        'virtual_height': 1224102657,
                                    },
                            {
                                        'source_monitor': 8175288,
                                        'source_nw_x_pixel': -3114763641630601912,
                                        'source_nw_y_pixel': -542052761088764922,
                                        'source_pixel_width': -7653863494352653534,
                                        'source_pixel_height': -7927752915143612614,
                                        'rotation': -2770663750778926301,
                                        'virtual_nw_x_pixel': -742644472,
                                        'virtual_nw_y_pixel': 1480340872,
                                        'virtual_width': 1262180125,
                                        'virtual_height': 55792759,
                                    },
                            {
                                        'source_monitor': 4538160,
                                        'source_nw_x_pixel': -1315059972868803780,
                                        'source_nw_y_pixel': -3789303535046952098,
                                        'source_pixel_width': -2056786915322415107,
                                        'source_pixel_height': -4381674000746310748,
                                        'rotation': -4818297031738164974,
                                        'virtual_nw_x_pixel': -1258504740,
                                        'virtual_nw_y_pixel': -1996843000,
                                        'virtual_width': -626979502,
                                        'virtual_height': 19670251,
                                    },
                            {
                                        'source_monitor': 9584972,
                                        'source_nw_x_pixel': -12539923508098859,
                                        'source_nw_y_pixel': -2470304594826793488,
                                        'source_pixel_width': -7078086400990029412,
                                        'source_pixel_height': -3860730902083641883,
                                        'rotation': -7390280042209895015,
                                        'virtual_nw_x_pixel': -742639770,
                                        'virtual_nw_y_pixel': -1869304708,
                                        'virtual_width': 1575788163,
                                        'virtual_height': 27831238,
                                    },
                            {
                                        'source_monitor': 3082658,
                                        'source_nw_x_pixel': -6420850509132989961,
                                        'source_nw_y_pixel': -7885345921766674002,
                                        'source_pixel_width': -7474100067583674043,
                                        'source_pixel_height': -1290592049379859010,
                                        'rotation': -8931008743323379099,
                                        'virtual_nw_x_pixel': 880357800,
                                        'virtual_nw_y_pixel': -1244475172,
                                        'virtual_width': -607281926,
                                        'virtual_height': 1994280263,
                                    },
                            {
                                        'source_monitor': 3233196,
                                        'source_nw_x_pixel': -8644794772427876191,
                                        'source_nw_y_pixel': -5810576817167670721,
                                        'source_pixel_width': -552853243010825070,
                                        'source_pixel_height': -1721013475683400337,
                                        'rotation': -5628848857491246156,
                                        'virtual_nw_x_pixel': -1280779703,
                                        'virtual_nw_y_pixel': 1106348097,
                                        'virtual_width': 1875091144,
                                        'virtual_height': 106609359,
                                    },
                        ],
                },
                {
                    'description': 'ʯΛɞʴȍǐР3˻Ȧ˞\x84ɦ¹҅ԧĵҵǚŢΆŇјͽŝΞԢ\x88ΔǷ',
                    'monitors': [
                            {
                                        'identifier': 2972791,
                                        'width': -5249864403405238388,
                                        'height': -3726269823705340231,
                                    },
                            {
                                        'identifier': 1244623,
                                        'width': 3467891406388053642,
                                        'height': -2179717077324575735,
                                    },
                            {
                                        'identifier': 3844592,
                                        'width': -3557317017059181127,
                                        'height': -268712062374772766,
                                    },
                            {
                                        'identifier': 6360547,
                                        'width': -1175361370064426763,
                                        'height': 6081458088346186001,
                                    },
                            {
                                        'identifier': 9920196,
                                        'width': -5118428000654447727,
                                        'height': 3066769774945674822,
                                    },
                            {
                                        'identifier': 3656408,
                                        'width': -3755070050356400613,
                                        'height': 8789741770745015670,
                                    },
                            {
                                        'identifier': 4663089,
                                        'width': -1345459168956520312,
                                        'height': -4394112537774479969,
                                    },
                            {
                                        'identifier': 9449913,
                                        'width': 6807723786795254194,
                                        'height': 1635511667965559607,
                                    },
                            {
                                        'identifier': 1263169,
                                        'width': -1248791528817559148,
                                        'height': -3046364959684264642,
                                    },
                            {
                                        'identifier': 8110100,
                                        'width': -7972437204706247874,
                                        'height': 3501095491048100211,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2602460,
                                        'source_nw_x_pixel': -3453740870367509301,
                                        'source_nw_y_pixel': -4142191687755272890,
                                        'source_pixel_width': -7657530395979626572,
                                        'source_pixel_height': -5852643670123031333,
                                        'rotation': -460811537193628607,
                                        'virtual_nw_x_pixel': -298819587,
                                        'virtual_nw_y_pixel': 929542687,
                                        'virtual_width': -218237036,
                                        'virtual_height': -1837248754,
                                    },
                            {
                                        'source_monitor': -95765,
                                        'source_nw_x_pixel': -7522321934138454796,
                                        'source_nw_y_pixel': -2368630133553127607,
                                        'source_pixel_width': -5316055418172141465,
                                        'source_pixel_height': -4373580500837500846,
                                        'rotation': -1539933268945660236,
                                        'virtual_nw_x_pixel': 405541312,
                                        'virtual_nw_y_pixel': 1483786554,
                                        'virtual_width': -527391901,
                                        'virtual_height': 1635355538,
                                    },
                            {
                                        'source_monitor': 3804764,
                                        'source_nw_x_pixel': -5093645073830865374,
                                        'source_nw_y_pixel': -2723250725103913392,
                                        'source_pixel_width': -5955422692336159816,
                                        'source_pixel_height': -1825602075703411300,
                                        'rotation': -6797880285025719661,
                                        'virtual_nw_x_pixel': 113433811,
                                        'virtual_nw_y_pixel': -881199358,
                                        'virtual_width': 438414247,
                                        'virtual_height': -1521950074,
                                    },
                            {
                                        'source_monitor': 1571836,
                                        'source_nw_x_pixel': -5889732351349581486,
                                        'source_nw_y_pixel': -5593919504405252864,
                                        'source_pixel_width': -7349619203357474051,
                                        'source_pixel_height': -1422809597463313221,
                                        'rotation': -4970119871196345949,
                                        'virtual_nw_x_pixel': 1478163395,
                                        'virtual_nw_y_pixel': -1082612189,
                                        'virtual_width': 1373825619,
                                        'virtual_height': 782022168,
                                    },
                            {
                                        'source_monitor': 3330214,
                                        'source_nw_x_pixel': -5384841505707605568,
                                        'source_nw_y_pixel': -2220249085576806385,
                                        'source_pixel_width': -7810104891194469931,
                                        'source_pixel_height': -8907724936787848602,
                                        'rotation': -6349172162953068667,
                                        'virtual_nw_x_pixel': -1665044101,
                                        'virtual_nw_y_pixel': 1881188828,
                                        'virtual_width': 483822014,
                                        'virtual_height': -151880070,
                                    },
                            {
                                        'source_monitor': 9959026,
                                        'source_nw_x_pixel': -2493611361190487001,
                                        'source_nw_y_pixel': -742802989312585392,
                                        'source_pixel_width': -5658844174981092206,
                                        'source_pixel_height': -7367009676378427458,
                                        'rotation': -4437133415205314999,
                                        'virtual_nw_x_pixel': 46583200,
                                        'virtual_nw_y_pixel': 795237617,
                                        'virtual_width': 991201621,
                                        'virtual_height': -1935314178,
                                    },
                            {
                                        'source_monitor': 8360526,
                                        'source_nw_x_pixel': -341524265261300721,
                                        'source_nw_y_pixel': -4161372075408681657,
                                        'source_pixel_width': -7694559832651745865,
                                        'source_pixel_height': -3592454356621086521,
                                        'rotation': -6054079037402626093,
                                        'virtual_nw_x_pixel': -1962664874,
                                        'virtual_nw_y_pixel': -1047158203,
                                        'virtual_width': -271097407,
                                        'virtual_height': -717137319,
                                    },
                            {
                                        'source_monitor': 5182127,
                                        'source_nw_x_pixel': -7652438494639650978,
                                        'source_nw_y_pixel': -9146967484241603266,
                                        'source_pixel_width': -5353963622881655491,
                                        'source_pixel_height': -3787488914283094666,
                                        'rotation': -8786050940105768231,
                                        'virtual_nw_x_pixel': 658752038,
                                        'virtual_nw_y_pixel': -1970859154,
                                        'virtual_width': -843554586,
                                        'virtual_height': 1630730421,
                                    },
                            {
                                        'source_monitor': 2718610,
                                        'source_nw_x_pixel': -477159661926872345,
                                        'source_nw_y_pixel': -4396936492266439862,
                                        'source_pixel_width': -8373742450989624892,
                                        'source_pixel_height': -849643275403496283,
                                        'rotation': -315601499367316756,
                                        'virtual_nw_x_pixel': 548127186,
                                        'virtual_nw_y_pixel': -1453239161,
                                        'virtual_width': 212184681,
                                        'virtual_height': -1029002711,
                                    },
                            {
                                        'source_monitor': 1947237,
                                        'source_nw_x_pixel': -5479004930811839886,
                                        'source_nw_y_pixel': -2560731449778154717,
                                        'source_pixel_width': -7897042795260451693,
                                        'source_pixel_height': -6114640567361383043,
                                        'rotation': -3773539095846613010,
                                        'virtual_nw_x_pixel': 129568642,
                                        'virtual_nw_y_pixel': 305301555,
                                        'virtual_width': -1337439755,
                                        'virtual_height': 859848850,
                                    },
                        ],
                },
                {
                    'description': 'ѿÂʵѓǰΗϜɯҀˉԟǩőǜѿ΄ĽǷǀʿЮŲCyćϕ¡včŒ',
                    'monitors': [
                            {
                                        'identifier': 7834346,
                                        'width': -2506196122263746079,
                                        'height': -5413902037085515668,
                                    },
                            {
                                        'identifier': 1818640,
                                        'width': 322705005735852353,
                                        'height': 4135920166700397973,
                                    },
                            {
                                        'identifier': 1364935,
                                        'width': -8298078331278059241,
                                        'height': -8619916104645290999,
                                    },
                            {
                                        'identifier': 197747,
                                        'width': -3069221112322289111,
                                        'height': -7103765195575355553,
                                    },
                            {
                                        'identifier': 2642795,
                                        'width': -7968366011101547628,
                                        'height': -7768394452744735000,
                                    },
                            {
                                        'identifier': 799118,
                                        'width': 2426879272831169730,
                                        'height': 5999194575905398537,
                                    },
                            {
                                        'identifier': 1436069,
                                        'width': 6953186426335417981,
                                        'height': 2315335556113047791,
                                    },
                            {
                                        'identifier': 4629669,
                                        'width': 3050348902781053069,
                                        'height': -6713506370058846735,
                                    },
                            {
                                        'identifier': 4613322,
                                        'width': -4064509395570447431,
                                        'height': -3920861565225824795,
                                    },
                            {
                                        'identifier': -649618,
                                        'width': 3400840042937134932,
                                        'height': 3370022069518590265,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3593221,
                                        'source_nw_x_pixel': -9153833910792135743,
                                        'source_nw_y_pixel': -1842986432366914,
                                        'source_pixel_width': -8800364361913755743,
                                        'source_pixel_height': -9120227846563452501,
                                        'rotation': -6655112452405874019,
                                        'virtual_nw_x_pixel': -1210182686,
                                        'virtual_nw_y_pixel': 1945462982,
                                        'virtual_width': 1213039508,
                                        'virtual_height': -1782843179,
                                    },
                            {
                                        'source_monitor': -630345,
                                        'source_nw_x_pixel': -2204331249674107815,
                                        'source_nw_y_pixel': -2015228830376575928,
                                        'source_pixel_width': -1864747736195146185,
                                        'source_pixel_height': -2170774773387219308,
                                        'rotation': -7341943706627180646,
                                        'virtual_nw_x_pixel': -632837518,
                                        'virtual_nw_y_pixel': 207657429,
                                        'virtual_width': -456690954,
                                        'virtual_height': 281690278,
                                    },
                            {
                                        'source_monitor': 1753255,
                                        'source_nw_x_pixel': -3305296576278578891,
                                        'source_nw_y_pixel': -128842744798417553,
                                        'source_pixel_width': -234936803185509855,
                                        'source_pixel_height': -6575974177590341800,
                                        'rotation': -2897078592052355466,
                                        'virtual_nw_x_pixel': -737183454,
                                        'virtual_nw_y_pixel': -1489332066,
                                        'virtual_width': -1321743020,
                                        'virtual_height': 1475125408,
                                    },
                            {
                                        'source_monitor': 4753658,
                                        'source_nw_x_pixel': -7786947141253532022,
                                        'source_nw_y_pixel': -4299847774914568324,
                                        'source_pixel_width': -3045811019824876987,
                                        'source_pixel_height': -9079145237990031432,
                                        'rotation': -8516214890101819902,
                                        'virtual_nw_x_pixel': -1694339295,
                                        'virtual_nw_y_pixel': -253996834,
                                        'virtual_width': -447659774,
                                        'virtual_height': -1635755518,
                                    },
                            {
                                        'source_monitor': 9848164,
                                        'source_nw_x_pixel': -510419402470099043,
                                        'source_nw_y_pixel': -1472345135307882516,
                                        'source_pixel_width': -8316500544618682878,
                                        'source_pixel_height': -8632315729968908984,
                                        'rotation': -944075601269344464,
                                        'virtual_nw_x_pixel': -1330579099,
                                        'virtual_nw_y_pixel': -902609773,
                                        'virtual_width': 1109506169,
                                        'virtual_height': -365246547,
                                    },
                            {
                                        'source_monitor': 7084507,
                                        'source_nw_x_pixel': -1547511383044704092,
                                        'source_nw_y_pixel': -2284880057710895062,
                                        'source_pixel_width': -6327445686773567754,
                                        'source_pixel_height': -1709683212149791062,
                                        'rotation': -497250287164945469,
                                        'virtual_nw_x_pixel': -1962384639,
                                        'virtual_nw_y_pixel': -991518652,
                                        'virtual_width': -1871288135,
                                        'virtual_height': -1468405525,
                                    },
                            {
                                        'source_monitor': 570445,
                                        'source_nw_x_pixel': -554184227739334887,
                                        'source_nw_y_pixel': -1669306504831413130,
                                        'source_pixel_width': -5729596161576461456,
                                        'source_pixel_height': -7431983178000462218,
                                        'rotation': -5280889106006750738,
                                        'virtual_nw_x_pixel': -99897201,
                                        'virtual_nw_y_pixel': 764178046,
                                        'virtual_width': -1527283149,
                                        'virtual_height': -1790031553,
                                    },
                            {
                                        'source_monitor': 7017308,
                                        'source_nw_x_pixel': -1883306559424861452,
                                        'source_nw_y_pixel': -6356058836168656934,
                                        'source_pixel_width': -2627074004286540081,
                                        'source_pixel_height': -5465282765577446674,
                                        'rotation': -9060628731236365703,
                                        'virtual_nw_x_pixel': 1640816529,
                                        'virtual_nw_y_pixel': -1630536281,
                                        'virtual_width': -386369899,
                                        'virtual_height': -1248879077,
                                    },
                            {
                                        'source_monitor': 3457134,
                                        'source_nw_x_pixel': -5532299317423830074,
                                        'source_nw_y_pixel': -2970639346959091587,
                                        'source_pixel_width': -1705847588097438062,
                                        'source_pixel_height': -168183581528792751,
                                        'rotation': -6147253040260051776,
                                        'virtual_nw_x_pixel': 1955091013,
                                        'virtual_nw_y_pixel': -1417628856,
                                        'virtual_width': -1419127376,
                                        'virtual_height': -67704083,
                                    },
                            {
                                        'source_monitor': -239015,
                                        'source_nw_x_pixel': -1501344011958671839,
                                        'source_nw_y_pixel': -652042779041645343,
                                        'source_pixel_width': -6186529039122416138,
                                        'source_pixel_height': -8422224787484307954,
                                        'rotation': -5718247889560715798,
                                        'virtual_nw_x_pixel': 1299146831,
                                        'virtual_nw_y_pixel': -539031224,
                                        'virtual_width': -1484856584,
                                        'virtual_height': 890471030,
                                    },
                        ],
                },
                {
                    'description': 'ŀϐƎºӪԕƸEǓӜÓˊɃʕԑҁνωȲʨѲӉʎКΆȂ΅χҖѯ',
                    'monitors': [
                            {
                                        'identifier': 9783470,
                                        'width': 5378557186163019620,
                                        'height': -1587384792278734337,
                                    },
                            {
                                        'identifier': 6226430,
                                        'width': 9029937867717098084,
                                        'height': 3316377999566937972,
                                    },
                            {
                                        'identifier': 2773361,
                                        'width': -8292883486595405413,
                                        'height': 1948394632636136813,
                                    },
                            {
                                        'identifier': 6608807,
                                        'width': -3266540811449156062,
                                        'height': -5137908578125692991,
                                    },
                            {
                                        'identifier': 51031,
                                        'width': 8217007219963622277,
                                        'height': -9026094791900353352,
                                    },
                            {
                                        'identifier': 5326927,
                                        'width': -3700471460095338494,
                                        'height': 2800306596187753690,
                                    },
                            {
                                        'identifier': 9567688,
                                        'width': -3837316707054245077,
                                        'height': -3112085982856718696,
                                    },
                            {
                                        'identifier': 2042002,
                                        'width': 673370716354888472,
                                        'height': -4574305691140199530,
                                    },
                            {
                                        'identifier': 6333127,
                                        'width': -157452721230672920,
                                        'height': -4342090444758747064,
                                    },
                            {
                                        'identifier': 2232437,
                                        'width': -4434651382863348222,
                                        'height': 5371187943059870042,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8517354,
                                        'source_nw_x_pixel': -3315018572216043268,
                                        'source_nw_y_pixel': -1869078594250260413,
                                        'source_pixel_width': -3494420879206096502,
                                        'source_pixel_height': -5096315952156974767,
                                        'rotation': -1624864175230943081,
                                        'virtual_nw_x_pixel': 792816672,
                                        'virtual_nw_y_pixel': -309173908,
                                        'virtual_width': -986032291,
                                        'virtual_height': -833265759,
                                    },
                            {
                                        'source_monitor': -636319,
                                        'source_nw_x_pixel': -1102322125900165638,
                                        'source_nw_y_pixel': -2086560884361799496,
                                        'source_pixel_width': -113463451171529048,
                                        'source_pixel_height': -5791904058359019643,
                                        'rotation': -1268286397623510048,
                                        'virtual_nw_x_pixel': 801052384,
                                        'virtual_nw_y_pixel': 1264717681,
                                        'virtual_width': -839482815,
                                        'virtual_height': 798521804,
                                    },
                            {
                                        'source_monitor': 523212,
                                        'source_nw_x_pixel': -1175083522475552872,
                                        'source_nw_y_pixel': -7576238084270217354,
                                        'source_pixel_width': -820745969162637960,
                                        'source_pixel_height': -5168543040389562449,
                                        'rotation': -8778661116241752188,
                                        'virtual_nw_x_pixel': 600505628,
                                        'virtual_nw_y_pixel': -1170580083,
                                        'virtual_width': -906875811,
                                        'virtual_height': 403827531,
                                    },
                            {
                                        'source_monitor': 8559434,
                                        'source_nw_x_pixel': -3915396891774867036,
                                        'source_nw_y_pixel': -3778433530274187131,
                                        'source_pixel_width': -4373683151761925389,
                                        'source_pixel_height': -4252826768290986462,
                                        'rotation': -3558033506152160859,
                                        'virtual_nw_x_pixel': -1429616177,
                                        'virtual_nw_y_pixel': 141984861,
                                        'virtual_width': 1229318033,
                                        'virtual_height': 1032229988,
                                    },
                            {
                                        'source_monitor': 2198371,
                                        'source_nw_x_pixel': -6889828115310502936,
                                        'source_nw_y_pixel': -1650398727628521589,
                                        'source_pixel_width': -3107338308674889415,
                                        'source_pixel_height': -6313236332973725202,
                                        'rotation': -6491101015829150519,
                                        'virtual_nw_x_pixel': -856789808,
                                        'virtual_nw_y_pixel': -1669572727,
                                        'virtual_width': 191517469,
                                        'virtual_height': 1485665335,
                                    },
                            {
                                        'source_monitor': 4575943,
                                        'source_nw_x_pixel': -3727045017007510287,
                                        'source_nw_y_pixel': -2812483809387781181,
                                        'source_pixel_width': -7066611249518499128,
                                        'source_pixel_height': -3499437519658666688,
                                        'rotation': -565764476520639373,
                                        'virtual_nw_x_pixel': 1487908173,
                                        'virtual_nw_y_pixel': -367189762,
                                        'virtual_width': 57783965,
                                        'virtual_height': 1497199902,
                                    },
                            {
                                        'source_monitor': 1007912,
                                        'source_nw_x_pixel': -7249094681737769109,
                                        'source_nw_y_pixel': -281610639555477740,
                                        'source_pixel_width': -3996277292133894282,
                                        'source_pixel_height': -4994224115523890521,
                                        'rotation': -3723999603504337257,
                                        'virtual_nw_x_pixel': 1904550825,
                                        'virtual_nw_y_pixel': -1764798205,
                                        'virtual_width': 1865195487,
                                        'virtual_height': 1664064772,
                                    },
                            {
                                        'source_monitor': 1675536,
                                        'source_nw_x_pixel': -4916893053483360044,
                                        'source_nw_y_pixel': -8827131301652899225,
                                        'source_pixel_width': -8752428349129360295,
                                        'source_pixel_height': -6185389732687778113,
                                        'rotation': -2096789732985224356,
                                        'virtual_nw_x_pixel': 417942763,
                                        'virtual_nw_y_pixel': 1032085361,
                                        'virtual_width': -1927532565,
                                        'virtual_height': -934399312,
                                    },
                            {
                                        'source_monitor': 7095959,
                                        'source_nw_x_pixel': -7751655931416528778,
                                        'source_nw_y_pixel': -2887696001933580415,
                                        'source_pixel_width': -8902736860331902766,
                                        'source_pixel_height': -1910256612480436031,
                                        'rotation': -2046806891326137043,
                                        'virtual_nw_x_pixel': -777153305,
                                        'virtual_nw_y_pixel': -620061488,
                                        'virtual_width': -1139246211,
                                        'virtual_height': -266746882,
                                    },
                            {
                                        'source_monitor': 8068400,
                                        'source_nw_x_pixel': -4020830668779823286,
                                        'source_nw_y_pixel': -1611690346850762921,
                                        'source_pixel_width': -581094682074490189,
                                        'source_pixel_height': -2345043677925757938,
                                        'rotation': -6526622293831431997,
                                        'virtual_nw_x_pixel': 352359161,
                                        'virtual_nw_y_pixel': -1558411872,
                                        'virtual_width': 721491745,
                                        'virtual_height': 29162354,
                                    },
                        ],
                },
                {
                    'description': '°&ОǩǣɐȜgҀƻӬԨ\x95ÌŴ˱ӥŠʀʕgϿԄƑzDД4ԠЯ',
                    'monitors': [
                            {
                                        'identifier': 6499634,
                                        'width': 4027483298354977994,
                                        'height': -2664040844674016338,
                                    },
                            {
                                        'identifier': 6718693,
                                        'width': 7127223695855240698,
                                        'height': -5278179266557826009,
                                    },
                            {
                                        'identifier': 3742162,
                                        'width': 8638993684437992472,
                                        'height': -797013707067311475,
                                    },
                            {
                                        'identifier': 1264864,
                                        'width': -6675839298759490745,
                                        'height': 6431307571138792333,
                                    },
                            {
                                        'identifier': 2518406,
                                        'width': 3943131845143040190,
                                        'height': -3576318487027515355,
                                    },
                            {
                                        'identifier': 9671147,
                                        'width': 6484569792893184870,
                                        'height': 5392118679237171905,
                                    },
                            {
                                        'identifier': 5403195,
                                        'width': 3330251530543804434,
                                        'height': -8169216418380339640,
                                    },
                            {
                                        'identifier': 8037830,
                                        'width': 467207781584042461,
                                        'height': 1517902058606836011,
                                    },
                            {
                                        'identifier': 7460752,
                                        'width': -5159643285789643326,
                                        'height': -4482806462453591063,
                                    },
                            {
                                        'identifier': 1588992,
                                        'width': -7038293354011595592,
                                        'height': 5805566732102711575,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4325283,
                                        'source_nw_x_pixel': -303658106938076054,
                                        'source_nw_y_pixel': -8617373484678404784,
                                        'source_pixel_width': -1940958462098314356,
                                        'source_pixel_height': -8268403236917867100,
                                        'rotation': -8595614562062424049,
                                        'virtual_nw_x_pixel': 1006996020,
                                        'virtual_nw_y_pixel': 1674654176,
                                        'virtual_width': 1198872715,
                                        'virtual_height': 603454980,
                                    },
                            {
                                        'source_monitor': 850799,
                                        'source_nw_x_pixel': -8289411937859910354,
                                        'source_nw_y_pixel': -5876629578145338957,
                                        'source_pixel_width': -85494570504717673,
                                        'source_pixel_height': -2536658262066672046,
                                        'rotation': -4671324397047999379,
                                        'virtual_nw_x_pixel': -1210646992,
                                        'virtual_nw_y_pixel': 708389049,
                                        'virtual_width': 170150387,
                                        'virtual_height': -1719596843,
                                    },
                            {
                                        'source_monitor': 9456483,
                                        'source_nw_x_pixel': -7789141462348846247,
                                        'source_nw_y_pixel': -7749134675323124491,
                                        'source_pixel_width': -4533650006596803027,
                                        'source_pixel_height': -2014765705549308293,
                                        'rotation': -1792310579262007353,
                                        'virtual_nw_x_pixel': -1567479945,
                                        'virtual_nw_y_pixel': -384956623,
                                        'virtual_width': -1193875486,
                                        'virtual_height': -785732012,
                                    },
                            {
                                        'source_monitor': 3799854,
                                        'source_nw_x_pixel': -3872833971899269038,
                                        'source_nw_y_pixel': -2507454190525854814,
                                        'source_pixel_width': -5977042878572597334,
                                        'source_pixel_height': -8672903703500721343,
                                        'rotation': -8312837145657599287,
                                        'virtual_nw_x_pixel': 739289521,
                                        'virtual_nw_y_pixel': 641271689,
                                        'virtual_width': -1825173528,
                                        'virtual_height': -1864101844,
                                    },
                            {
                                        'source_monitor': 3474154,
                                        'source_nw_x_pixel': -8472751641062945216,
                                        'source_nw_y_pixel': -7874120445278185403,
                                        'source_pixel_width': -2271160387957194705,
                                        'source_pixel_height': -1422381002929824809,
                                        'rotation': -4243359086530340421,
                                        'virtual_nw_x_pixel': -68197515,
                                        'virtual_nw_y_pixel': -1977337598,
                                        'virtual_width': 46595974,
                                        'virtual_height': -461233550,
                                    },
                            {
                                        'source_monitor': 6988232,
                                        'source_nw_x_pixel': -3983152868224514710,
                                        'source_nw_y_pixel': -6955282144332853980,
                                        'source_pixel_width': -4499000797387319646,
                                        'source_pixel_height': -8141988828719272026,
                                        'rotation': -8619310620206475866,
                                        'virtual_nw_x_pixel': -713266582,
                                        'virtual_nw_y_pixel': -1760185858,
                                        'virtual_width': -532564697,
                                        'virtual_height': -786645283,
                                    },
                            {
                                        'source_monitor': 978546,
                                        'source_nw_x_pixel': -1618843723510358846,
                                        'source_nw_y_pixel': -4043190272507479411,
                                        'source_pixel_width': -9061473134228330277,
                                        'source_pixel_height': -8421287777019292760,
                                        'rotation': -8417383600271222384,
                                        'virtual_nw_x_pixel': 1397463267,
                                        'virtual_nw_y_pixel': 220135436,
                                        'virtual_width': -1298454711,
                                        'virtual_height': -1629663922,
                                    },
                            {
                                        'source_monitor': 185865,
                                        'source_nw_x_pixel': -7066790482104952821,
                                        'source_nw_y_pixel': -5694487474568242035,
                                        'source_pixel_width': -3513448119316779787,
                                        'source_pixel_height': -5028885115082852624,
                                        'rotation': -2571886037819818262,
                                        'virtual_nw_x_pixel': -379204191,
                                        'virtual_nw_y_pixel': 1271279288,
                                        'virtual_width': 273506591,
                                        'virtual_height': 152416160,
                                    },
                            {
                                        'source_monitor': 7760235,
                                        'source_nw_x_pixel': -8530470922382353297,
                                        'source_nw_y_pixel': -5614291579845472536,
                                        'source_pixel_width': -5793430327178886775,
                                        'source_pixel_height': -2100014127141527073,
                                        'rotation': -8518852339373854735,
                                        'virtual_nw_x_pixel': -662275491,
                                        'virtual_nw_y_pixel': -1249999509,
                                        'virtual_width': -321257043,
                                        'virtual_height': 1315123907,
                                    },
                            {
                                        'source_monitor': 378608,
                                        'source_nw_x_pixel': -2354273935197932395,
                                        'source_nw_y_pixel': -2681776978327678395,
                                        'source_pixel_width': -3710225980345112835,
                                        'source_pixel_height': -6309263047751134348,
                                        'rotation': -7160291691720509730,
                                        'virtual_nw_x_pixel': -1551980325,
                                        'virtual_nw_y_pixel': 1754546497,
                                        'virtual_width': -23679518,
                                        'virtual_height': -1676233653,
                                    },
                        ],
                },
                {
                    'description': 'ЎѲϋԆčŜƳµ˺Í˂ЃτŇɼӎāлɞɗ\u0382ԐϚ˒ɒҘɬИǩУ',
                    'monitors': [
                            {
                                        'identifier': 7932949,
                                        'width': -7861523567084881434,
                                        'height': 740130586265695610,
                                    },
                            {
                                        'identifier': 688425,
                                        'width': -2867214570121487262,
                                        'height': -2626265802041428943,
                                    },
                            {
                                        'identifier': 4372713,
                                        'width': 4432990493339191026,
                                        'height': 5015194573879537066,
                                    },
                            {
                                        'identifier': 4385868,
                                        'width': -5953884943563303076,
                                        'height': -1672899678453167725,
                                    },
                            {
                                        'identifier': 6288143,
                                        'width': -6651820869343924465,
                                        'height': 3958637583246503503,
                                    },
                            {
                                        'identifier': 4207803,
                                        'width': 1322553291832251415,
                                        'height': 2830467405569684068,
                                    },
                            {
                                        'identifier': 6499637,
                                        'width': -8387554612004567606,
                                        'height': -6138653560881660791,
                                    },
                            {
                                        'identifier': 107974,
                                        'width': 6003374074043716699,
                                        'height': -2710832671152029276,
                                    },
                            {
                                        'identifier': 7222999,
                                        'width': -466588997892537608,
                                        'height': 3857386245792211607,
                                    },
                            {
                                        'identifier': 9707864,
                                        'width': -2555412596653242067,
                                        'height': -4219563382510409197,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8543714,
                                        'source_nw_x_pixel': -7123189147879670746,
                                        'source_nw_y_pixel': -2082147601244669810,
                                        'source_pixel_width': -1451579230563294167,
                                        'source_pixel_height': -475897964519659489,
                                        'rotation': -5052985294947924361,
                                        'virtual_nw_x_pixel': -898686663,
                                        'virtual_nw_y_pixel': 909823595,
                                        'virtual_width': -470431492,
                                        'virtual_height': -1608755430,
                                    },
                            {
                                        'source_monitor': 8164279,
                                        'source_nw_x_pixel': -5886404144737095670,
                                        'source_nw_y_pixel': -5872176014917618644,
                                        'source_pixel_width': -25101676361136668,
                                        'source_pixel_height': -7454699488866922258,
                                        'rotation': -7430846488580512224,
                                        'virtual_nw_x_pixel': -649024914,
                                        'virtual_nw_y_pixel': 1519461843,
                                        'virtual_width': 1741744058,
                                        'virtual_height': 1471547249,
                                    },
                            {
                                        'source_monitor': -542632,
                                        'source_nw_x_pixel': -3851936218510410667,
                                        'source_nw_y_pixel': -3798760095848878807,
                                        'source_pixel_width': -3598992614600176465,
                                        'source_pixel_height': -3748617202936826416,
                                        'rotation': -4488653867050346676,
                                        'virtual_nw_x_pixel': -931420647,
                                        'virtual_nw_y_pixel': 314544097,
                                        'virtual_width': 97951446,
                                        'virtual_height': 1998377188,
                                    },
                            {
                                        'source_monitor': 7555047,
                                        'source_nw_x_pixel': -505749775840245120,
                                        'source_nw_y_pixel': -2020668188062909040,
                                        'source_pixel_width': -2764535627257243016,
                                        'source_pixel_height': -6150217317546821221,
                                        'rotation': -5327841277329442159,
                                        'virtual_nw_x_pixel': -683131839,
                                        'virtual_nw_y_pixel': 357697419,
                                        'virtual_width': 1000139958,
                                        'virtual_height': 1733590233,
                                    },
                            {
                                        'source_monitor': 5109156,
                                        'source_nw_x_pixel': -2544477974328405833,
                                        'source_nw_y_pixel': -1218841729722086567,
                                        'source_pixel_width': -3287662802297527380,
                                        'source_pixel_height': -4769335956992005049,
                                        'rotation': -3790794758983425975,
                                        'virtual_nw_x_pixel': 206980363,
                                        'virtual_nw_y_pixel': 100624426,
                                        'virtual_width': -1073879258,
                                        'virtual_height': 1761418163,
                                    },
                            {
                                        'source_monitor': 5553291,
                                        'source_nw_x_pixel': -1096782892342871777,
                                        'source_nw_y_pixel': -6641696422212105421,
                                        'source_pixel_width': -3093134362767077606,
                                        'source_pixel_height': -1199921895815040281,
                                        'rotation': -999042243470545524,
                                        'virtual_nw_x_pixel': 1099671961,
                                        'virtual_nw_y_pixel': 584440468,
                                        'virtual_width': 221223359,
                                        'virtual_height': -1006805363,
                                    },
                            {
                                        'source_monitor': 8819339,
                                        'source_nw_x_pixel': -1021635187656378811,
                                        'source_nw_y_pixel': -8241576436969104486,
                                        'source_pixel_width': -6697769541516563605,
                                        'source_pixel_height': -7377185735226969644,
                                        'rotation': -5566217262221722050,
                                        'virtual_nw_x_pixel': -1780489208,
                                        'virtual_nw_y_pixel': 1429879556,
                                        'virtual_width': -625385564,
                                        'virtual_height': 714424474,
                                    },
                            {
                                        'source_monitor': 22009,
                                        'source_nw_x_pixel': -7200506990320205021,
                                        'source_nw_y_pixel': -7429113329565299702,
                                        'source_pixel_width': -93637749746616665,
                                        'source_pixel_height': -454510836378620163,
                                        'rotation': -8805463319227620083,
                                        'virtual_nw_x_pixel': -593180836,
                                        'virtual_nw_y_pixel': -1308389608,
                                        'virtual_width': -1627505874,
                                        'virtual_height': -1569000515,
                                    },
                            {
                                        'source_monitor': 6501811,
                                        'source_nw_x_pixel': -3726482303425415460,
                                        'source_nw_y_pixel': -8589860396412932733,
                                        'source_pixel_width': -3645752166939768614,
                                        'source_pixel_height': -287832084082601825,
                                        'rotation': -396683085033690432,
                                        'virtual_nw_x_pixel': 905359676,
                                        'virtual_nw_y_pixel': -987170896,
                                        'virtual_width': 182059470,
                                        'virtual_height': -1201361030,
                                    },
                            {
                                        'source_monitor': 6195257,
                                        'source_nw_x_pixel': -1166855816389043044,
                                        'source_nw_y_pixel': -4831443724926814976,
                                        'source_pixel_width': -8373843493459207799,
                                        'source_pixel_height': -2504606136431336487,
                                        'rotation': -2959914972273837383,
                                        'virtual_nw_x_pixel': 664444177,
                                        'virtual_nw_y_pixel': 938497718,
                                        'virtual_width': -1673327112,
                                        'virtual_height': 619663798,
                                    },
                        ],
                },
                {
                    'description': 'ӨūàӎѪǼĲĶðώͺeƣҳǿȃКЛЀ҈Ɋѯ\u0379ЯѼӍɇȶÎʦ',
                    'monitors': [
                            {
                                        'identifier': 9295965,
                                        'width': 951179186271491320,
                                        'height': 3462435503973352540,
                                    },
                            {
                                        'identifier': 3800058,
                                        'width': 2651230334617371707,
                                        'height': -752911193746851086,
                                    },
                            {
                                        'identifier': -931233,
                                        'width': 3982707261468712982,
                                        'height': 4288432519645244694,
                                    },
                            {
                                        'identifier': 9562973,
                                        'width': -4688395779717052875,
                                        'height': 7218333403000989029,
                                    },
                            {
                                        'identifier': -447901,
                                        'width': -5167250096801041817,
                                        'height': -5096603031488025821,
                                    },
                            {
                                        'identifier': 2061904,
                                        'width': 3923565792153437949,
                                        'height': -6478223675544874905,
                                    },
                            {
                                        'identifier': 2840371,
                                        'width': -3714058211298387165,
                                        'height': 3009679056297108385,
                                    },
                            {
                                        'identifier': 326330,
                                        'width': 8193397447752022653,
                                        'height': 7521157608571601754,
                                    },
                            {
                                        'identifier': 6985213,
                                        'width': -3268952494045644271,
                                        'height': 2250995208352402923,
                                    },
                            {
                                        'identifier': 7258954,
                                        'width': 2714595438625197075,
                                        'height': -2745092005586033788,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3343090,
                                        'source_nw_x_pixel': -7345622049856481513,
                                        'source_nw_y_pixel': -7218935753638332486,
                                        'source_pixel_width': -7510955060928489670,
                                        'source_pixel_height': -407439228952750669,
                                        'rotation': -6411718314135707944,
                                        'virtual_nw_x_pixel': -1364986914,
                                        'virtual_nw_y_pixel': 904955160,
                                        'virtual_width': 204369352,
                                        'virtual_height': 1443325101,
                                    },
                            {
                                        'source_monitor': 8227501,
                                        'source_nw_x_pixel': -7522339009607578851,
                                        'source_nw_y_pixel': -2211578993841167840,
                                        'source_pixel_width': -4324580278215176758,
                                        'source_pixel_height': -4911798571731222147,
                                        'rotation': -4805922396162284102,
                                        'virtual_nw_x_pixel': -194644221,
                                        'virtual_nw_y_pixel': -148007606,
                                        'virtual_width': -117792657,
                                        'virtual_height': 700898718,
                                    },
                            {
                                        'source_monitor': -905584,
                                        'source_nw_x_pixel': -3959276353165039722,
                                        'source_nw_y_pixel': -8897192564020447754,
                                        'source_pixel_width': -4639359617667146628,
                                        'source_pixel_height': -2413625036099467549,
                                        'rotation': -6781379398930939935,
                                        'virtual_nw_x_pixel': 1208330902,
                                        'virtual_nw_y_pixel': 1687570637,
                                        'virtual_width': -1802364079,
                                        'virtual_height': -199315606,
                                    },
                            {
                                        'source_monitor': 1613537,
                                        'source_nw_x_pixel': -2765160972313344900,
                                        'source_nw_y_pixel': -2484497287360423529,
                                        'source_pixel_width': -517202157233628096,
                                        'source_pixel_height': -336214886813855776,
                                        'rotation': -3007103683573176593,
                                        'virtual_nw_x_pixel': -1497694286,
                                        'virtual_nw_y_pixel': -412787472,
                                        'virtual_width': -972630078,
                                        'virtual_height': -1219526724,
                                    },
                            {
                                        'source_monitor': 1302718,
                                        'source_nw_x_pixel': -3191074874057974725,
                                        'source_nw_y_pixel': -8739739620534494320,
                                        'source_pixel_width': -6702941055969615079,
                                        'source_pixel_height': -1154643887031092865,
                                        'rotation': -1939777841033870531,
                                        'virtual_nw_x_pixel': -294502902,
                                        'virtual_nw_y_pixel': -1641983135,
                                        'virtual_width': -1916018967,
                                        'virtual_height': -658628043,
                                    },
                            {
                                        'source_monitor': -16909,
                                        'source_nw_x_pixel': -6199696065421145522,
                                        'source_nw_y_pixel': -5238246432630814678,
                                        'source_pixel_width': -5338165956590430550,
                                        'source_pixel_height': -5216401667406813406,
                                        'rotation': -6213874519178308578,
                                        'virtual_nw_x_pixel': -1275099474,
                                        'virtual_nw_y_pixel': 1066122396,
                                        'virtual_width': 1217807401,
                                        'virtual_height': -1924019773,
                                    },
                            {
                                        'source_monitor': 7342251,
                                        'source_nw_x_pixel': -5204793907950557481,
                                        'source_nw_y_pixel': -6612672054738836067,
                                        'source_pixel_width': -2320934511430746437,
                                        'source_pixel_height': -8265790281315455473,
                                        'rotation': -8431819090586468366,
                                        'virtual_nw_x_pixel': 1926525466,
                                        'virtual_nw_y_pixel': 787932072,
                                        'virtual_width': -130051374,
                                        'virtual_height': -1132796234,
                                    },
                            {
                                        'source_monitor': 1854518,
                                        'source_nw_x_pixel': -6673903819988331513,
                                        'source_nw_y_pixel': -2403084768248280620,
                                        'source_pixel_width': -5466114736054346635,
                                        'source_pixel_height': -3110561838828070410,
                                        'rotation': -3377971897417382020,
                                        'virtual_nw_x_pixel': -1233811223,
                                        'virtual_nw_y_pixel': -441769967,
                                        'virtual_width': 795484033,
                                        'virtual_height': -730062543,
                                    },
                            {
                                        'source_monitor': 473966,
                                        'source_nw_x_pixel': -7037591690181979617,
                                        'source_nw_y_pixel': -8467192727745725476,
                                        'source_pixel_width': -4474939584745093452,
                                        'source_pixel_height': -582331951695010155,
                                        'rotation': -2096461422836314210,
                                        'virtual_nw_x_pixel': 1900881141,
                                        'virtual_nw_y_pixel': 1832570053,
                                        'virtual_width': -856375274,
                                        'virtual_height': 639962524,
                                    },
                            {
                                        'source_monitor': 2474869,
                                        'source_nw_x_pixel': -7378794111853088973,
                                        'source_nw_y_pixel': -4483799935542873313,
                                        'source_pixel_width': -5615155379148659607,
                                        'source_pixel_height': -2445000701056418540,
                                        'rotation': -5077644051649010343,
                                        'virtual_nw_x_pixel': 654889826,
                                        'virtual_nw_y_pixel': -71195449,
                                        'virtual_width': -653617427,
                                        'virtual_height': 1497810171,
                                    },
                        ],
                },
                {
                    'description': 'ƸȬTƙ˅Čǂ@гºԡŠ»іŪɌѫҠēôӼЊȔB8ĵȡєӤʇ',
                    'monitors': [
                            {
                                        'identifier': 3380532,
                                        'width': -8436599975410094732,
                                        'height': -354515878992280643,
                                    },
                            {
                                        'identifier': -770196,
                                        'width': 5101931480068581642,
                                        'height': -8385768472374155799,
                                    },
                            {
                                        'identifier': 5726720,
                                        'width': 1449507741921319585,
                                        'height': 7857793220134484080,
                                    },
                            {
                                        'identifier': 5292030,
                                        'width': 5165271156876917520,
                                        'height': 5910782069537816968,
                                    },
                            {
                                        'identifier': 3600789,
                                        'width': 1881290281984760223,
                                        'height': 5402972994028877923,
                                    },
                            {
                                        'identifier': 4917205,
                                        'width': 206208361073829670,
                                        'height': -6526430795654830269,
                                    },
                            {
                                        'identifier': 8537245,
                                        'width': -1803753318235189461,
                                        'height': 7245639955257359218,
                                    },
                            {
                                        'identifier': 8035647,
                                        'width': -637125612532046278,
                                        'height': -2050586270686823785,
                                    },
                            {
                                        'identifier': 3306256,
                                        'width': -5682329670599236564,
                                        'height': -4675179783352967712,
                                    },
                            {
                                        'identifier': -275892,
                                        'width': 3796162153393075924,
                                        'height': -5284251117030087046,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1970169,
                                        'source_nw_x_pixel': -5353518758868511218,
                                        'source_nw_y_pixel': -4974947702822054957,
                                        'source_pixel_width': -614906712280274745,
                                        'source_pixel_height': -1181794549716837795,
                                        'rotation': -3376587788839467600,
                                        'virtual_nw_x_pixel': 947988284,
                                        'virtual_nw_y_pixel': 26145907,
                                        'virtual_width': 178407651,
                                        'virtual_height': -505726767,
                                    },
                            {
                                        'source_monitor': 7799044,
                                        'source_nw_x_pixel': -2935984880300899566,
                                        'source_nw_y_pixel': -7697277272858800340,
                                        'source_pixel_width': -5353242155936566798,
                                        'source_pixel_height': -764368731707985467,
                                        'rotation': -3446089478538774282,
                                        'virtual_nw_x_pixel': 562813509,
                                        'virtual_nw_y_pixel': 60494269,
                                        'virtual_width': 1097786468,
                                        'virtual_height': -1215279638,
                                    },
                            {
                                        'source_monitor': 1692826,
                                        'source_nw_x_pixel': -2819887259373637648,
                                        'source_nw_y_pixel': -690308760870084281,
                                        'source_pixel_width': -8712731575274190710,
                                        'source_pixel_height': -8422379365968118680,
                                        'rotation': -8938406914946119550,
                                        'virtual_nw_x_pixel': -1274021425,
                                        'virtual_nw_y_pixel': -1183072141,
                                        'virtual_width': 918488796,
                                        'virtual_height': -483598159,
                                    },
                            {
                                        'source_monitor': 1541680,
                                        'source_nw_x_pixel': -6072662229228105978,
                                        'source_nw_y_pixel': -113790659287060857,
                                        'source_pixel_width': -5475295864344965741,
                                        'source_pixel_height': -7985573970785562239,
                                        'rotation': -8223696881901707164,
                                        'virtual_nw_x_pixel': 1690742102,
                                        'virtual_nw_y_pixel': 885769663,
                                        'virtual_width': 1627460573,
                                        'virtual_height': 1718932497,
                                    },
                            {
                                        'source_monitor': 9207196,
                                        'source_nw_x_pixel': -3940736580482469237,
                                        'source_nw_y_pixel': -7931073727003853078,
                                        'source_pixel_width': -1900860156890504507,
                                        'source_pixel_height': -4315888522294269327,
                                        'rotation': -5075666430221575359,
                                        'virtual_nw_x_pixel': -1572072410,
                                        'virtual_nw_y_pixel': 664040065,
                                        'virtual_width': 740336407,
                                        'virtual_height': 43285941,
                                    },
                            {
                                        'source_monitor': 8675118,
                                        'source_nw_x_pixel': -2130402444446160718,
                                        'source_nw_y_pixel': -8120088307013582819,
                                        'source_pixel_width': -6340882698492386988,
                                        'source_pixel_height': -8451127863828135469,
                                        'rotation': -6515423218017148835,
                                        'virtual_nw_x_pixel': 237692711,
                                        'virtual_nw_y_pixel': 1603730815,
                                        'virtual_width': 161533461,
                                        'virtual_height': -793541020,
                                    },
                            {
                                        'source_monitor': -308991,
                                        'source_nw_x_pixel': -6346312360444829384,
                                        'source_nw_y_pixel': -2607874945937981126,
                                        'source_pixel_width': -7554971522510379789,
                                        'source_pixel_height': -8180635910736855683,
                                        'rotation': -6334761825004943626,
                                        'virtual_nw_x_pixel': -1917894136,
                                        'virtual_nw_y_pixel': -1745053507,
                                        'virtual_width': -1889970328,
                                        'virtual_height': 167803290,
                                    },
                            {
                                        'source_monitor': 4413181,
                                        'source_nw_x_pixel': -9172117608343588900,
                                        'source_nw_y_pixel': -1417201415766802369,
                                        'source_pixel_width': -6235943920913423819,
                                        'source_pixel_height': -2685485645187669134,
                                        'rotation': -5157439604629698205,
                                        'virtual_nw_x_pixel': 1440530095,
                                        'virtual_nw_y_pixel': 1008888346,
                                        'virtual_width': -972979288,
                                        'virtual_height': 673387195,
                                    },
                            {
                                        'source_monitor': 3538180,
                                        'source_nw_x_pixel': -7123956953685750199,
                                        'source_nw_y_pixel': -1076167494749166691,
                                        'source_pixel_width': -350131602287392709,
                                        'source_pixel_height': -50545360809282641,
                                        'rotation': -7447553818737362141,
                                        'virtual_nw_x_pixel': -1615935505,
                                        'virtual_nw_y_pixel': 1087665288,
                                        'virtual_width': -954126670,
                                        'virtual_height': -659684398,
                                    },
                            {
                                        'source_monitor': 2304970,
                                        'source_nw_x_pixel': -5509642355739535873,
                                        'source_nw_y_pixel': -1398529388747583326,
                                        'source_pixel_width': -7538674128740529874,
                                        'source_pixel_height': -7522560339530961592,
                                        'rotation': -8779157608858543485,
                                        'virtual_nw_x_pixel': 1104689818,
                                        'virtual_nw_y_pixel': -1301793415,
                                        'virtual_width': 602537237,
                                        'virtual_height': -1072019705,
                                    },
                        ],
                },
                {
                    'description': 'ɾìϸȽƊόíIϘМéȌ˹˻˳ƏɏĂˍтϡ)ϟԦӅ½ƘқɞҚ',
                    'monitors': [
                            {
                                        'identifier': 6107783,
                                        'width': -1524098335712411097,
                                        'height': 7143197240205743599,
                                    },
                            {
                                        'identifier': 8003055,
                                        'width': 5039949916582891102,
                                        'height': -6306868147156105729,
                                    },
                            {
                                        'identifier': 1316222,
                                        'width': 8028314767760060413,
                                        'height': -5283494822049022718,
                                    },
                            {
                                        'identifier': 1921529,
                                        'width': 1925009777105422518,
                                        'height': 5714340515627527575,
                                    },
                            {
                                        'identifier': 3269193,
                                        'width': -1579717359161288615,
                                        'height': -9136581466208779714,
                                    },
                            {
                                        'identifier': -741030,
                                        'width': 8994699565895315642,
                                        'height': 3988558911456087869,
                                    },
                            {
                                        'identifier': 8291875,
                                        'width': -4522842397469013075,
                                        'height': 5324379067880781467,
                                    },
                            {
                                        'identifier': 9794022,
                                        'width': 2825154713117670252,
                                        'height': -7838482072061628380,
                                    },
                            {
                                        'identifier': 2942295,
                                        'width': 6611743411761037196,
                                        'height': 5849124117505892479,
                                    },
                            {
                                        'identifier': 5055163,
                                        'width': -510341836496501412,
                                        'height': 6222601259058686474,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3046076,
                                        'source_nw_x_pixel': -2154927768731325064,
                                        'source_nw_y_pixel': -1933402359255850611,
                                        'source_pixel_width': -1477720323671495367,
                                        'source_pixel_height': -4635806628357578649,
                                        'rotation': -8924741943771665682,
                                        'virtual_nw_x_pixel': -953626833,
                                        'virtual_nw_y_pixel': -1549593992,
                                        'virtual_width': -842805451,
                                        'virtual_height': -1759070734,
                                    },
                            {
                                        'source_monitor': 7566590,
                                        'source_nw_x_pixel': -1976409518172613575,
                                        'source_nw_y_pixel': -9045072156395658335,
                                        'source_pixel_width': -3908085194757018466,
                                        'source_pixel_height': -314665245896941724,
                                        'rotation': -1361276316947364638,
                                        'virtual_nw_x_pixel': 882454454,
                                        'virtual_nw_y_pixel': -1587492964,
                                        'virtual_width': -1728336696,
                                        'virtual_height': 628181743,
                                    },
                            {
                                        'source_monitor': 9762435,
                                        'source_nw_x_pixel': -2486717555969905646,
                                        'source_nw_y_pixel': -1905899266134735025,
                                        'source_pixel_width': -7798346192496236,
                                        'source_pixel_height': -572086099134367734,
                                        'rotation': -7751746967968753744,
                                        'virtual_nw_x_pixel': 1274501370,
                                        'virtual_nw_y_pixel': -1959250019,
                                        'virtual_width': 1490163477,
                                        'virtual_height': -231332149,
                                    },
                            {
                                        'source_monitor': 9518000,
                                        'source_nw_x_pixel': -6865198887668102360,
                                        'source_nw_y_pixel': -721614622681112965,
                                        'source_pixel_width': -4966383079833874872,
                                        'source_pixel_height': -5777602288120277139,
                                        'rotation': -4035521278924095700,
                                        'virtual_nw_x_pixel': 364607734,
                                        'virtual_nw_y_pixel': 771543086,
                                        'virtual_width': -740019537,
                                        'virtual_height': -305862996,
                                    },
                            {
                                        'source_monitor': 5782031,
                                        'source_nw_x_pixel': -6838084789639639098,
                                        'source_nw_y_pixel': -1803499865584612205,
                                        'source_pixel_width': -2566093251656933091,
                                        'source_pixel_height': -7290798682578370984,
                                        'rotation': -1545457114352425581,
                                        'virtual_nw_x_pixel': -1609260581,
                                        'virtual_nw_y_pixel': 24857993,
                                        'virtual_width': 1650508540,
                                        'virtual_height': -1601241205,
                                    },
                            {
                                        'source_monitor': 8557060,
                                        'source_nw_x_pixel': -1693128511493909326,
                                        'source_nw_y_pixel': -8702884450483340715,
                                        'source_pixel_width': -7274714868657920228,
                                        'source_pixel_height': -4538089633329141274,
                                        'rotation': -1870602891883235319,
                                        'virtual_nw_x_pixel': -877268402,
                                        'virtual_nw_y_pixel': -675326819,
                                        'virtual_width': -1558610519,
                                        'virtual_height': 758672506,
                                    },
                            {
                                        'source_monitor': 8904755,
                                        'source_nw_x_pixel': -7116044009460930098,
                                        'source_nw_y_pixel': -8347273099080221351,
                                        'source_pixel_width': -1965730211625424542,
                                        'source_pixel_height': -1775273667497886271,
                                        'rotation': -1541309984825025221,
                                        'virtual_nw_x_pixel': 577842362,
                                        'virtual_nw_y_pixel': 1371175492,
                                        'virtual_width': 1362010840,
                                        'virtual_height': 1296327528,
                                    },
                            {
                                        'source_monitor': 2611015,
                                        'source_nw_x_pixel': -1693107541367104689,
                                        'source_nw_y_pixel': -5343343488875988480,
                                        'source_pixel_width': -8224782593787099381,
                                        'source_pixel_height': -3300264088340554621,
                                        'rotation': -1214896391118031893,
                                        'virtual_nw_x_pixel': -197750565,
                                        'virtual_nw_y_pixel': 881683460,
                                        'virtual_width': -959743595,
                                        'virtual_height': 1584324669,
                                    },
                            {
                                        'source_monitor': 5898092,
                                        'source_nw_x_pixel': -5478460129790029496,
                                        'source_nw_y_pixel': -7883761563052338847,
                                        'source_pixel_width': -7687782160671899809,
                                        'source_pixel_height': -3881873421711010677,
                                        'rotation': -7463576183591333314,
                                        'virtual_nw_x_pixel': -1971775113,
                                        'virtual_nw_y_pixel': -212701214,
                                        'virtual_width': 1868425196,
                                        'virtual_height': 1557319434,
                                    },
                            {
                                        'source_monitor': 6345565,
                                        'source_nw_x_pixel': -6902951792116380886,
                                        'source_nw_y_pixel': -6138667422741117934,
                                        'source_pixel_width': -7322023576431153763,
                                        'source_pixel_height': -3004783063942101481,
                                        'rotation': -1597535889287154547,
                                        'virtual_nw_x_pixel': -1160647704,
                                        'virtual_nw_y_pixel': -124984389,
                                        'virtual_width': 1821393761,
                                        'virtual_height': 1680766804,
                                    },
                        ],
                },
                {
                    'description': 'ǎȈơЪϜǺƭΖѤȉѠӕвâҐзϠĺϢԊһȟƕȼŒͺ˻ΕРɷ',
                    'monitors': [
                            {
                                        'identifier': 545124,
                                        'width': 8531104977440941295,
                                        'height': 1718983243962305358,
                                    },
                            {
                                        'identifier': 9374282,
                                        'width': 2250557083460369387,
                                        'height': -122663605672966418,
                                    },
                            {
                                        'identifier': 291420,
                                        'width': -447309925548357677,
                                        'height': 6166215995447140612,
                                    },
                            {
                                        'identifier': 7468204,
                                        'width': -3891244258639786322,
                                        'height': -1691428054086899146,
                                    },
                            {
                                        'identifier': 1011165,
                                        'width': -8781309349126907803,
                                        'height': -6052150281601277576,
                                    },
                            {
                                        'identifier': 6889373,
                                        'width': -385926716483436878,
                                        'height': -8744132129544091754,
                                    },
                            {
                                        'identifier': 8669922,
                                        'width': -7622526451010621975,
                                        'height': -2450369934808717099,
                                    },
                            {
                                        'identifier': 2695722,
                                        'width': 5490703061152526713,
                                        'height': -1859270690402053280,
                                    },
                            {
                                        'identifier': 9246602,
                                        'width': -5752963957305925981,
                                        'height': -3862449705934695083,
                                    },
                            {
                                        'identifier': 4501441,
                                        'width': 7989654541088490921,
                                        'height': -6732382299453186895,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5308652,
                                        'source_nw_x_pixel': -4429055046050621256,
                                        'source_nw_y_pixel': -6663391241109554080,
                                        'source_pixel_width': -2675302219897462888,
                                        'source_pixel_height': -3104673879173595911,
                                        'rotation': -7440276061738992135,
                                        'virtual_nw_x_pixel': -1690961900,
                                        'virtual_nw_y_pixel': 610013688,
                                        'virtual_width': 516052776,
                                        'virtual_height': -1517143277,
                                    },
                            {
                                        'source_monitor': -128708,
                                        'source_nw_x_pixel': -8572174251335918023,
                                        'source_nw_y_pixel': -4785228074438126866,
                                        'source_pixel_width': -8888768897693166832,
                                        'source_pixel_height': -8889076935312672228,
                                        'rotation': -7144389206650428328,
                                        'virtual_nw_x_pixel': 803569554,
                                        'virtual_nw_y_pixel': -1048460934,
                                        'virtual_width': -1287320738,
                                        'virtual_height': 1234924803,
                                    },
                            {
                                        'source_monitor': 4694430,
                                        'source_nw_x_pixel': -9125083928774585189,
                                        'source_nw_y_pixel': -5120597206760975852,
                                        'source_pixel_width': -5750956404690503935,
                                        'source_pixel_height': -1448000478653555142,
                                        'rotation': -5395958584049789345,
                                        'virtual_nw_x_pixel': 877550858,
                                        'virtual_nw_y_pixel': 1555293002,
                                        'virtual_width': -1266991102,
                                        'virtual_height': 1716841904,
                                    },
                            {
                                        'source_monitor': 3895405,
                                        'source_nw_x_pixel': -4175161068680495361,
                                        'source_nw_y_pixel': -5086614319676029284,
                                        'source_pixel_width': -1439611810011259602,
                                        'source_pixel_height': -6588123310314643080,
                                        'rotation': -1625608856372688881,
                                        'virtual_nw_x_pixel': -60079434,
                                        'virtual_nw_y_pixel': -1174403976,
                                        'virtual_width': -124243203,
                                        'virtual_height': -1056870896,
                                    },
                            {
                                        'source_monitor': 8295520,
                                        'source_nw_x_pixel': -8596021582694466673,
                                        'source_nw_y_pixel': -5478099016923293686,
                                        'source_pixel_width': -4871707616437564452,
                                        'source_pixel_height': -5001383138817104336,
                                        'rotation': -7933360343844525638,
                                        'virtual_nw_x_pixel': 1698608419,
                                        'virtual_nw_y_pixel': -1670843518,
                                        'virtual_width': 213807016,
                                        'virtual_height': 1693314584,
                                    },
                            {
                                        'source_monitor': -370537,
                                        'source_nw_x_pixel': -5136746284779744615,
                                        'source_nw_y_pixel': -512958455267306030,
                                        'source_pixel_width': -1884176730180099203,
                                        'source_pixel_height': -4234747796994650684,
                                        'rotation': -4434144121617879269,
                                        'virtual_nw_x_pixel': 475196285,
                                        'virtual_nw_y_pixel': -1122168982,
                                        'virtual_width': 1853855797,
                                        'virtual_height': -1909290124,
                                    },
                            {
                                        'source_monitor': 4101054,
                                        'source_nw_x_pixel': -5070696697602707141,
                                        'source_nw_y_pixel': -4693912696062985649,
                                        'source_pixel_width': -3676255335859814937,
                                        'source_pixel_height': -4072430256140885044,
                                        'rotation': -2588066475160132550,
                                        'virtual_nw_x_pixel': 1569385651,
                                        'virtual_nw_y_pixel': -238539335,
                                        'virtual_width': -420724833,
                                        'virtual_height': 395473444,
                                    },
                            {
                                        'source_monitor': 328781,
                                        'source_nw_x_pixel': -357254150488359973,
                                        'source_nw_y_pixel': -744509139378357252,
                                        'source_pixel_width': -8519038549930106526,
                                        'source_pixel_height': -6276964096825031458,
                                        'rotation': -5695997619121744884,
                                        'virtual_nw_x_pixel': 1180338164,
                                        'virtual_nw_y_pixel': -706522876,
                                        'virtual_width': -478332485,
                                        'virtual_height': -1615172577,
                                    },
                            {
                                        'source_monitor': 5258509,
                                        'source_nw_x_pixel': -5969689606909212641,
                                        'source_nw_y_pixel': -6929962392449177191,
                                        'source_pixel_width': -6273468858629484063,
                                        'source_pixel_height': -2721107350317479329,
                                        'rotation': -7431688751213335461,
                                        'virtual_nw_x_pixel': -1976347124,
                                        'virtual_nw_y_pixel': 265110182,
                                        'virtual_width': -1734807624,
                                        'virtual_height': -370333584,
                                    },
                            {
                                        'source_monitor': -115702,
                                        'source_nw_x_pixel': -6317098658334911783,
                                        'source_nw_y_pixel': -7128328901300562365,
                                        'source_pixel_width': -8363493955071144156,
                                        'source_pixel_height': -1474450433544144071,
                                        'rotation': -2323849820507023778,
                                        'virtual_nw_x_pixel': 1326794243,
                                        'virtual_nw_y_pixel': 1212339676,
                                        'virtual_width': 1426114995,
                                        'virtual_height': 10453385,
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
                                        'identifier': 5362531,
                                        'width': -9127156764256642195,
                                        'height': -7358253638374895253,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -831862852179354986,
                                        'source_nw_y_pixel': -1292297381616527867,
                                        'source_pixel_width': -8730039829724445359,
                                        'source_pixel_height': -7408008645277742522,
                                        'rotation': -2234181965907075321,
                                        'virtual_nw_x_pixel': -611948053,
                                        'virtual_nw_y_pixel': -635608998,
                                        'virtual_width': 261074278,
                                        'virtual_height': 532695144,
                                    },
                        ],
                },
            ],

        },
    ),
]
